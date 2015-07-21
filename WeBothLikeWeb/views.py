from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render
from WeBothLikeWeb.models import Question, UserAnswer
from WeBothLikeWeb.forms import AnswerQuestionForm


def frontpage(request):
    user_social_account = None
    user_fb_account = None
    next_question_to_answer = None
    match_count = None
    my_match_fb_account = None
    if request.method == 'POST' and request.user.id:
        form = AnswerQuestionForm(request.POST)
        if form.is_valid():
            a = UserAnswer(
                question=form.cleaned_data['question'],
                user=request.user,
                answer=form.cleaned_data['answer']
            )
            a.save()
    if request.user.id:
        user_social_account = SocialAccount.objects.filter(provider='facebook', user=request.user).first()
        next_question_to_answer = Question.objects.filter(active=True)\
            .exclude(id__in=request.user.questions.values_list('id', flat=True)).first()
        total_questions = Question.objects.count()
        my_answers = UserAnswer.objects.filter(user=request.user).order_by('question', '-created').distinct('question')
        my_answers_count = my_answers.count()
        matching_answer_qs = UserAnswer.objects.exclude(user=request.user)
        match_backup = matching_answer_qs.distinct('user').order_by('user').first()
        last_match = match_backup
        for ma in my_answers.all():
            matching_answer_qs = matching_answer_qs.exclude(Q(question=ma.question) and ~Q(answer=ma.answer))
            match_backup = matching_answer_qs.distinct('user').order_by('user').first()
            if match_backup:
                last_match = match_backup
        matching_answer_qs = matching_answer_qs.distinct('user')
        match_count = matching_answer_qs.count()
        if match_count == 1 or total_questions == my_answers_count and last_match:
            my_match_user = last_match.user
            my_match_fb_account = SocialAccount.objects\
                .filter(provider='facebook', user=my_match_user).first()\
                .get_provider_account()
    if user_social_account:
        user_fb_account = user_social_account.get_provider_account()

    context = {
        'user_fb_account': user_fb_account if user_fb_account else None,
        'question': next_question_to_answer,
        'match_count': match_count,
        'my_match_fb_account': my_match_fb_account
    }
    return render(request, 'frontpage.html', context)