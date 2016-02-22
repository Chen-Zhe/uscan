from django.contrib import admin

from .models import Event, Goodie, School, Problem

'''
	list_display = ['id', 'title', 'get_school', 'start', 'finish']
	def get_school(self, obj):
		return "\n".join([s.name for s in obj.school.all()])
'''

class EventAdmin(admin.ModelAdmin):
	list_display = ['id', 'title', 'start', 'finish', 'code','regex']

class GoodieAdmin(admin.ModelAdmin):
	list_display = ['matric', 'get_event', 'time']
	def get_event(self, obj):
		return obj.event.title
	get_event.short_description = 'Event'
	get_event.admin_order_field = 'event__title'
'''
class SchoolAdmin(admin.ModelAdmin):
	list_display = ['name', 'code']

class ProblemAdmin(admin.ModelAdmin):
	list_display = ['matric', 'get_school']
	def get_school(self, obj):
		return "\n".join([s.name for s in obj.school.all()])

admin.site.register(School, SchoolAdmin)
admin.site.register(Problem, ProblemAdmin)
'''
admin.site.register(Event, EventAdmin)
admin.site.register(Goodie, GoodieAdmin)