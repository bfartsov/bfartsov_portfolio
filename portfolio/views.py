from typing import List
from django.shortcuts import render
from .models import Banner, About, Skill_Section, PortFolio


def home(request):
    banners = Banner.objects.all()
    about = About.objects.get(farts_name='Blagovest')
    skills_about = Skill_Section.objects.all()[:1]
    skills = skills_about[0].skills.all().order_by('-prosent')
    portfolio = PortFolio.objects.all()
    print(skills)
    context = {
        'banners': banners,
        'about': about,
        'skills_about':  skills_about[0],
        'skills': skills,
        'portfolio': portfolio
    }
    return render(request, 'index.html', context)
