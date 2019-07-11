# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from housekeeping.housekeepingManagement.models import Asset, Task, Admin, Worker, WorkerSkillSet, AllocatedTasks

# Register your models here.
admin.site.register(Asset)
admin.site.register(Task)
admin.site.register(Admin)
admin.site.register(Worker)
admin.site.register(WorkerSkillSet)
admin.site.register(AllocatedTasks)
