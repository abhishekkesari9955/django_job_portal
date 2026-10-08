from django.shortcuts import render, get_object_or_404 , redirect
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from .models import Company
from .forms import CompanyForm

# Create your views here.

def company_list(request):
    query = request.GET.get('q','')
    location = request.GET.get('location','')
    
    companies = Company.objects.annotate(job_count=Count('jobs')).order_by('name')

    if query:
        companies = companies.filter(name__icontains=query)

    if location:
        companies = companies.filter(location__icontains=location)

    return render(request, 'companies/company_list.html', {'companies': companies,
                                                           'query': query,
                                                           'location': location})

def company_detail(request, company_id):

    company = get_object_or_404(Company, id=company_id)
    jobs = company.jobs.all().order_by('-created_at')  # Access the related jobs using the related_name 'jobs'
    return render(request, 'companies/company_detail.html', {'company': company
                                                             , 'jobs': jobs})

@login_required
def manage_company(request):

    company = Company.objects.filter(
        recruiter=request.user
    ).first()

    if request.method == "POST":

        form = CompanyForm(
            request.POST,
            instance=company
        )

        if form.is_valid():

            company = form.save(commit=False)
            company.recruiter = request.user
            company.save()

            return redirect("manage_company")

    else:

        form = CompanyForm(instance=company)

    return render(
        request,
        "companies/manage_company.html",
        {
            "form": form,
            "company": company,
        }
    )