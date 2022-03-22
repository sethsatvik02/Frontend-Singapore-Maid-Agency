from django.shortcuts import render


def index(request):
    return render(request,'dashboard.html')

def FDWs(request):
    return render(request,'FDWs.html')

def myagency(request):
    return render(request,'My_agency.html')

def myagencyedit(request):
    return render(request,'Edit_My_agency.html')


def add_FDWs(request):
    return render(request,'add_FDWs.html')



def FDWs_profile(request):
    return render(request,'FDWs_profile.html')

def Employers(request):
    return render(request,'Employers.html')

def add_Employers(request):
    return render(request,'add_Employers.html')

def Agents(request):
    return render(request,'Agents.html')

def add_Agent(request):
    return render(request,'add_Agent.html')

def add_Agent_Local_Company(request):
    return render(request,'add_Agent_Local_Company.html')

def Agent_Details(request):
    return render(request,'Agent_Details.html')

def Agent_Photo(request):
    return render(request,'Agent_Photo.html')

def add_Agent_Overseas_Company(request):
    return render(request,'add_Agent_Overseas_Company.html')

def add_Agent_Overseas_Individual(request):
    return render(request,'add_Agent_Overseas_Individual.html')

def Edit_Agent_List(request):
    return render(request,'Edit_Agent_List.html')