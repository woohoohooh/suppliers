from django.shortcuts import render, redirect, get_object_or_404
from .models import Company, Rubrics, Country, Region, City, Comment
import json
import os
from django.shortcuts import render
import datetime


def rubric_detail(request, rubric):
    rubric_obj = Rubrics.objects.get(name=rubric)
    companies_with_rubric = Company.objects.filter(rubrics=rubric_obj)
    return render(request, 'catalog/rubric_result.html',
                  context={'rubric': rubric_obj, 'companies': companies_with_rubric})



def index(request):
    current_year = datetime.datetime.now().year
    rubrics = Rubrics.objects.all()
    companies = Company.objects.all()
    return render(request, 'catalog/index.html',
                  context={'companies': companies, 'rubrics': rubrics, 'request': request, 'current_year': current_year})


def company_detail(request, pk):
    company = get_object_or_404(Company, pk=pk)
    rubrics2 = Rubrics.objects.all()
    comments = company.comments.all()
    return render(request, 'catalog/company_detail.html',
                  context={'company': company, 'rubrics2': rubrics2, 'comments': comments})


def add_comment(request, post_id):
    company = get_object_or_404(Company, pk=post_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        content = request.POST.get('content')
        feedback_type = request.POST.get('feedback_type')

        if name and content and feedback_type:
            is_positive = (feedback_type == 'positive')
            comment = Comment(company=company, name=name, content=content, is_positive=is_positive)
            comment.save()

    return redirect('company_detail', pk=post_id)


def start(request):
    return render(request, 'catalog/start.html')

def start2(request):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_directory, '../test3.json')
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        ok = json.load(f)
        if request.method == 'POST':
            q = len(ok)
            count = 0
            for i in range(0, q):
                try:
                    tmp_rubrics = ok[count]['rubrics']
                    rubrics_list = []
                    for rubric_data in tmp_rubrics:
                        rubric_name = rubric_data['name']
                        rubric_instance, created = Rubrics.objects.get_or_create(name=rubric_name)
                        rubrics_list.append(rubric_instance)
                except (IndexError, KeyError):
                    rubrics_list = []

                country_name = ok[count]['adm_div'][0]['name']
                country_instance, created = Country.objects.get_or_create(name=country_name)

                region_name = ok[count]['adm_div'][1]['name']
                region_instance, created = Region.objects.get_or_create(name=region_name)

                city_name = ok[count]['adm_div'][3]['name']
                city_instance, created = City.objects.get_or_create(name=city_name)
                try:
                    org_name = ok[count]['org']['name']
                except (IndexError, KeyError):
                    org_name = None
                try:
                    address_name = ok[count]['address_name']
                except (IndexError, KeyError):
                    address_name = None
                try:
                    address_comment = ok[count]['address_comment']
                except (IndexError, KeyError):
                    address_comment = None
                try:
                    one = ok[count]['contact_groups'][0]['contacts'][0]['value']
                    if '?http' in one:
                        two = one.find('?http')
                        three = one[two+1:]
                        contact_groups_contacts1_text1 = three
                    elif '?text' in one:
                        two = one.find('?text')
                        three = one[:two]
                        contact_groups_contacts1_text1 = three
                    else:
                        contact_groups_contacts1_text1 = one
                except (IndexError, KeyError):
                    contact_groups_contacts1_text1 = None
                try:
                    one = ok[count]['contact_groups'][0]['contacts'][1]['value']
                    if '?http' in one:
                        two = one.find('?http')
                        three = one[two+1:]
                        contact_groups_contacts1_text2 = three
                    elif '?text' in one:
                        two = one.find('?text')
                        three = one[:two]
                        contact_groups_contacts1_text2 = three
                    else:
                        contact_groups_contacts1_text2 = one
                except (IndexError, KeyError):
                    contact_groups_contacts1_text2 = None
                try:
                    one = ok[count]['contact_groups'][0]['contacts'][2]['value']
                    if '?http' in one:
                        two = one.find('?http')
                        three = one[two+1:]
                        contact_groups_contacts1_text3 = three
                    elif '?text' in one:
                        two = one.find('?text')
                        three = one[:two]
                        contact_groups_contacts1_text3 = three
                    else:
                        contact_groups_contacts1_text3 = one
                except (IndexError, KeyError):
                    contact_groups_contacts1_text3 = None
                try:
                    one = ok[count]['contact_groups'][1]['contacts'][0]['value']
                    if '?http' in one:
                        two = one.find('?http')
                        three = one[two+1:]
                        contact_groups_contacts2_text1 = three
                    elif '?text' in one:
                        two = one.find('?text')
                        three = one[:two]
                        contact_groups_contacts2_text1 = three
                    else:
                        contact_groups_contacts2_text1 = one
                except (IndexError, KeyError):
                    contact_groups_contacts2_text1 = None
                try:
                    one = ok[count]['contact_groups'][1]['contacts'][1]['value']
                    if '?http' in one:
                        two = one.find('?http')
                        three = one[two+1:]
                        contact_groups_contacts2_text2 = three
                    elif '?text' in one:
                        two = one.find('?text')
                        three = one[:two]
                        contact_groups_contacts2_text2 = three
                    else:
                        contact_groups_contacts2_text2 = one
                except (IndexError, KeyError):
                    contact_groups_contacts2_text2 = None
                try:
                    one = ok[count]['contact_groups'][1]['contacts'][2]['value']
                    if '?http' in one:
                        two = one.find('?http')
                        three = one[two+1:]
                        contact_groups_contacts2_text3 = three
                    elif '?text' in one:
                        two = one.find('?text')
                        three = one[:two]
                        contact_groups_contacts2_text3 = three
                    else:
                        contact_groups_contacts2_text3 = one
                except (IndexError, KeyError):
                    contact_groups_contacts2_text3 = None
                try:
                    ads_article = ok[count]['ads']['article']
                except (IndexError, KeyError):
                    ads_article = None
                try:
                    article_warning = ok[count]['ads']['article_warning']
                except (IndexError, KeyError):
                    article_warning = None
                count += 1

                company_instance = Company.objects.create(
                    org_name=org_name,
                    address_name=address_name,
                    address_comment=address_comment,
                    contact_groups_contacts1_text1=contact_groups_contacts1_text1,
                    contact_groups_contacts1_text2=contact_groups_contacts1_text2,
                    contact_groups_contacts1_text3=contact_groups_contacts1_text3,
                    contact_groups_contacts2_text1=contact_groups_contacts2_text1,
                    contact_groups_contacts2_text2=contact_groups_contacts2_text2,
                    contact_groups_contacts2_text3=contact_groups_contacts2_text3,
                    ads_article=ads_article,
                    article_warning=article_warning,
                    country=country_instance,
                    region=region_instance,
                    city=city_instance,
                )

                # Adding rubrics to the many-to-many relationship
                company_instance.rubrics.set(rubrics_list)

    return redirect(index)
