# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from housekeeping.housekeepingManagement.models import Asset, Task, Admin, Worker, WorkerSkillSet, AllocatedTasks
from rest_framework import viewsets
from housekeeping.housekeepingManagement.serializers import AssetSerializer, TaskSerializer, AdminSerializer, WorkerSerializer
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
import json
# Create your views here.
from rest_framework.response import Response
from rest_framework import status
from dateutil.parser import parse
@csrf_exempt
def addAsset(self):
    req = self.POST
    print(req)
    asset_name = req.get("assetName", "-1")
    asset = Asset.objects.create_asset(asset_name)
    return HttpResponse(asset_name, content_type ="application/json")

@csrf_exempt
def addTask(self):
    req = self.POST
    task_name = req.get("taskName", "-1")
    frequency = req.get("frequency", "-1")

    task = Task.objects.create_task(task_name, frequency)
    return HttpResponse(task_name, content_type ="application/json")

@csrf_exempt
def addWorker(self):
    req = self.POST
    worker_name = req.get("workerName", "-1")

    worker = Worker.objects.create_worker(worker_name)
    return HttpResponse(worker_name, content_type ="application/json")

@csrf_exempt
def getAssets(self):
    # req = self.
    to_ret = []

    for i in Asset.objects.all():
        # print(model_to_dict(i))
        model = model_to_dict(i)
        dict_obj = {
            "asset_name": model['asset_name'],
            "id": model['id']
        }
        to_ret.append( dict_obj )
        # to_ret.append( model_to_dict(i)['id'] )
    
    json_stuff = json.dumps({ "assets" : to_ret })    
    return HttpResponse(json_stuff, content_type ="application/json")

@csrf_exempt
def getWorkers(self):
    # req = self.
    to_ret = []

    for i in Worker.objects.all():
        # print(model_to_dict(i))
        model = model_to_dict(i)
        dict_obj = {
            "worker_name": model['worker_name'],
            "id": model['id']
        }
        to_ret.append( dict_obj )
        # to_ret.append( model_to_dict(i)['id'] )
    
    json_stuff = json.dumps({ "workers" : to_ret })    
    return HttpResponse(json_stuff, content_type ="application/json")

@csrf_exempt
def getTasks(self):
    # req = self.
    to_ret = []

    for i in Task.objects.all():
        # print(model_to_dict(i))
        model = model_to_dict(i)
        dict_obj = {
            "task_name": model['task_name'],
            "id": model['id']
        }
        to_ret.append( dict_obj )
        # to_ret.append( model_to_dict(i)['id'] )
    
    json_stuff = json.dumps({ "tasks" : to_ret })    
    return HttpResponse(json_stuff, content_type ="application/json")


@csrf_exempt
def addWorkerSkill(self):
    
    req = self.POST
    worker_id = req.get("workerId", "-1")
    task_id = req.get("taskId", "-1")

    worker = Worker.objects.get(id=worker_id)
    task = Task.objects.get(id=task_id)    
    
    if(worker and task):
        try:        
            WorkerSkillSetObject = WorkerSkillSet.objects.create_worker_skill_set(worker,task)
            if(WorkerSkillSetObject):
                return HttpResponse("hi", content_type="application/json")
            else:
                return HttpResponse("Error", status=status.HTTP_409_CONFLICT) 
        except:
            return HttpResponse("Error", status=status.HTTP_409_CONFLICT)
    else:
        return HttpResponse("Error", status=status.HTTP_409_CONFLICT)

@csrf_exempt
def allocateTask(self):
    req = self.POST
    
    worker_id = req.get("workerId", "-1")
    task_id = req.get("taskId", "-1")
    asset_id = req.get("assetId", "-1")
    # time_of_allocation = req.get("timeOfAllocation", "-1")
    task_to_be_performed_by = req.get("taskToBePerformedBy", "-1")

    worker = Worker.objects.get(id=worker_id)    
    task = Task.objects.get(id=task_id)        
    asset = Asset.objects.get(id=asset_id)
    print(parse(task_to_be_performed_by))
    if(worker and task and asset):
        # try:        
        AllocatedTask = AllocatedTasks.objects.allocate_task(asset, task, worker, parse(task_to_be_performed_by))
        if(AllocatedTask):
            return HttpResponse("Success", content_type="application/json")
        else:
            return HttpResponse("Error", status=status.HTTP_409_CONFLICT)    
        # except:
        #     return HttpResponse("Error", status=status.HTTP_409_CONFLICT)
    else:
        return HttpResponse("Error", status=status.HTTP_409_CONFLICT)

@csrf_exempt
def getTasksForWorkers(self,workerId):

    req = self.GET
    # print(username, "yolo")
    worker_id = workerId
    if(worker_id):
        print("workerid", worker_id)
        try:
            worker = Worker.objects.get(id=worker_id)    
            allocatedTasks = AllocatedTasks.objects.filter(worker=worker)   
            print(allocatedTasks)
            to_ret = []
            for i in allocatedTasks:
                model = model_to_dict(i)
                print(model)
                to_ret.append({
                    'task': model['task'],
                    # 'time_of_allocation': str(model['time_of_allocation']),
                    'worker': model['worker'],
                    'task_to_be_performed_by': str(model['task_to_be_performed_by']),
                    'asset': model['asset']
                })
            json_stuff = json.dumps({ "allocatedTasks" : to_ret })    
            return HttpResponse(json_stuff, content_type ="application/json")
        except:
            return HttpResponse('Whoops') 
    else:
        return HttpResponse('Whoops') 
     
    