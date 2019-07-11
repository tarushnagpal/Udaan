# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

# Asset Controllers

class AssetManager(models.Manager):
    def create_asset(self,asset_name):
        asset = self.create(asset_name=asset_name)        
        return asset

class Asset(models.Model):
    # first_name = models.CharField(max_length=30)
    asset_name = models.CharField(max_length=50)
    objects = AssetManager()

    def __str__(self):
        return "%s" % (self.asset_name)


# Task Controllers

class TaskManager(models.Manager):
    def create_task(self, task_name, frequency):
        task = self.create(task_name=task_name, frequency=frequency)        
        return task

class Task(models.Model):
    task_name = models.CharField(max_length=50)
    # time_of_allocation = models.DateTimeField()
    frequency = models.CharField(
        max_length=7,
        choices=(
            ("hourly", "Hourly"),
            ("daily", "Daily"),
            ("weekly", "Weekly"),
            ("monthly", "Monthly"),
            ("yearly", "Yearly"),
        )
    )
    objects = TaskManager()

    def __str__(self):
        return "%s" % (self.task_name)


# Admin Controllers

class AdminManager(models.Model):
    def create_admin(self, admin_name):
        admin = self.create(admin_name=admin_name)
        return admin

class Admin(models.Model):
    admin_name = models.CharField(max_length=50)
    objects = AdminManager()

    def __str__(self):
        return "%s" % (self.admin_name)

# Worker Controllers
class WorkerManager(models.Manager):
    def create_worker(self, worker_name):
        worker = self.create(worker_name=worker_name)        
        return worker

class Worker(models.Model):
    worker_name = models.CharField(max_length=50)
    objects = WorkerManager()

    def __str__(self):
        return "%s" % (self.worker_name)

class WorkerSkillSetManager(models.Manager):
    
    def create_worker_skill_set(self, worker, task):
        skill_set = self.create(worker=worker, task=task)
        return skill_set

class WorkerSkillSet(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    objects = WorkerSkillSetManager()
    
    class Meta:
        unique_together = ('worker', 'task')

# Task Allocation

class AllocatedTasksManager(models.Manager):

    def allocate_task(self, asset, task, worker, task_to_be_performed_by):
        allocated_task = self.create(asset=asset, task=task, worker=worker, task_to_be_performed_by=task_to_be_performed_by)
        return allocated_task

class AllocatedTasks(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)

    time_of_allocation = models.DateTimeField(auto_now_add=True)
    task_to_be_performed_by = models.DateTimeField()

    objects=AllocatedTasksManager()

    class Meta:
        unique_together = ('asset', 'task', 'worker')
