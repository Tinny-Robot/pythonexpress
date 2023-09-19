from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import date
from .models import Challenge, Participant
from .forms import SolutionForm

@login_required
def daily_challenge(request):
    # Retrieve the challenge for today's date
    today = date.today()
    challenge = get_object_or_404(Challenge, date=today)

    # Check if the user has already participated in this challenge
    user_participation = Participant.objects.filter(
        user=request.user,
        challenge=challenge
    ).first()

    # Handle the code submission form if the request method is POST
    if request.method == 'POST':
        form = SolutionForm(request.POST)
        if form.is_valid():
            code_solution = form.cleaned_data['code_solution']
            
            # Implement your code evaluation logic here, including scoring
            # Update the user's score based on the result of the evaluation
            
            # Create or update the Participant model for this user and challenge
            if not user_participation:
                user_participation = Participant(
                    user=request.user,
                    challenge=challenge,
                    code_solution=code_solution,
                    score=0  # Initialize score as needed
                )
            else:
                user_participation.code_solution = code_solution
                user_participation.score = 0  # Update score as needed
            
            user_participation.save()

            # Redirect the user back to the challenge page
            return redirect('leaderboard')
    else:
        form = SolutionForm()

    context = {
        'challenge': challenge,
        'user_participation': user_participation,
        'form': form,
    }

    return render(request, 'challenges/daily_challenge.html', context)



def leaderboard(request):
    # Retrieve the top participants based on their scores
    leaderboard_data = Participant.objects.filter(
        challenge__date=date.today()
    ).order_by('-score')[:10]  # Display top 10 participants

    context = {
        'leaderboard_data': leaderboard_data,
    }

    return render(request, 'challenges/leaderboard.html', context)
