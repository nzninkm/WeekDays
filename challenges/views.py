from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string


# Create your views here.


days ={
    'saturday': 'this is saturday in dictionary',
    'sunday': 'this is sunday in dictionary',
    'monday': 'this is monday in dictionary',
    'tuesday': 'this is tuesday in dictionary',
    'wednesday': 'this is wednesday in dictionary',
    'thursday': 'this is thursday in dictionary',
    'friday': None
}


def days_list(request):
    days_list = list(days.keys())
    # list_items = ""
    
    # for day in days_list:
    #     url_path = reverse('days-of-week', args=[day])
    #     list_items += f'<li> <a href="{url_path}"> {day} </a> </li>'
    # content = f'<ul> \n {list_items} \n</ul>'
    # return HttpResponse(content)
    context = {
        'days':days_list
    }
    return render(request, "challenges/index.html", context)

def dynamic_days_by_number(request, day):
    days_names = list(days.keys())
    if day > len(days_names):
        return HttpResponseNotFound('day does not exists')
    redirect_day = days_names[day - 1]
    redirect_url = reverse('days-of-week', args=[redirect_day]) # /days/
    return HttpResponseRedirect(redirect_url)
    # return HttpResponse(day)





def dynamic_days(request, day):
    day_data = days.get(day)
    # if day_data is not None:
    #     day_data = "there is no data"
        context = {
            "data": day_data,
            "day": f'selected DAY is {day}'
        }
       
        # DTL -> Django Template Language
        return render(request, 'challenges/challenge.html', context)
        # response_data = render_to_string('challenges/challenges.html')
        # return HttpResponse(response_data)
    return HttpResponseNotFound('day does not exists')