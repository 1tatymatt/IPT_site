from django.shortcuts import render

# Create your views here.

def history(request):
	"""
	This view generates the Job history page.
	"""
	# retrieve the users Jobs from Agave - this will return JSON

	# check errors, and convert the response to a "jobs" dictionary.
	jobs = [{"uname": "tzmatt", "id": "123", "name": "test", "status": "RUNNING", "start": "July 6 2017 9:47 AM", "end": "None", "type": "RUN"}, 
	{"id": "456", "name": "test2", "status": "FINISHED", "start": "July 7 2017 10:18 AM", "end": "July 7 2017 11:01 AM", "type": "BUILD"}]
	context = {"jobs": jobs, }
	# render the history template, passing in the jobs dictionary.
	return render(request, 'iptsite/history.html', context, content_type='text/html')

def run(request):
	"""
	This view generates the Run page.
	"""
	# retrieve the users Jobs from Agave - this will return JSON

	# check errors, and convert the response to a "jobs" dictionary.
	# jobs = [{"id": "123", "name": "test", "status": "RUNNING", "start": "July 6 2017 9:47 AM", "end": "None", "type": "RUN"}]
	# context = {"jobs": jobs, }
	runinput = [{"rcommand": "ibrun", "bin": "rose_foo_mpi.c", "rcommandargs": "$args"}]
	context = {"runinput": runinput, }
	# render the history template, passing in the jobs dictionary.
	return render(request, 'iptsite/run.html', context, content_type='text/html')

def help(request):
	"""
	This view generates the Help page.
	"""
	# retrieve the users Jobs from Agave - this will return JSON

	# check errors, and convert the response to a "jobs" dictionary.
	# jobs = [{"id": "123", "name": "test", "status": "RUNNING", "start": "July 6 2017 9:47 AM", "end": "None", "type": "RUN"}]
	# context = {"jobs": jobs, }
	# render the history template, passing in the jobs dictionary.
	return render(request, 'iptsite/help.html')

def compile(request):
	"""
	This view generates the Compile page.
	"""
	# retrieve the users Jobs from Agave - this will return JSON

	# check errors, and convert the response to a "jobs" dictionary.
	compileinput = [{"ccommand": "icc", "driver": "rose_foo_mpi.c", "outfiles": "a.out", "addfiles": "None", "ccommandargs": "$args"}]
	context = {"compileinput": compileinput, }
	# render the history template, passing in the jobs dictionary.
	return render(request, 'iptsite/compile.html', context, content_type='text/html')

def login(request):
	"""
	This view generates the User Login page.
	"""
	# retrieve the users Jobs from Agave - this will return JSON

	# check errors, and convert the response to a "jobs" dictionary.
	# compileinput = [{"ccommand": "icc", "driver": "rose_foo_mpi.c", "outfiles": "a.out", "addfiles": "None", "ccommandargs": "$args"}]
	# context = {"compileinput": compileinput, }
	# render the history template, passing in the jobs dictionary.
	return render(request, 'iptsite/login.html', content_type='text/html')














