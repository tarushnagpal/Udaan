"""housekeeping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from housekeeping.housekeepingManagement.views import addAsset, addTask, addWorker, getAssets, getWorkers, getTasks, addWorkerSkill, allocateTask, getTasksForWorkers

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^add-asset/', addAsset),
    url(r'^add-task/', addTask),
    url(r'^add-worker/', addWorker),
    url(r'^assets/all/', getAssets),
    url(r'^workers/all/', getWorkers),
    url(r'^tasks/all/', getTasks),
    url(r'^add-worker-skill/', addWorkerSkill),
    url(r'^allocate-task/', allocateTask),
    url(r'^get-tasks-for-worker/(?P<workerId>\w{0,50})/', getTasksForWorkers),

]
