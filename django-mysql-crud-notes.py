"""
data: july 18, 2019
tutorial: https://www.youtube.com/watch?v=e-o0L3lmsdQ

learnings: 	- how mvc works 1. urls.py, 2. views.py, 3. html
			- how to use css
			- crud
			- how to get id - edit and delete
			- how to link
			- redirect

find: 	run application



1. 	create admin app to this path:		C:\Users\TAE\Desktop\django-mysql-crud - django-admin startproject webapplication

2. 	inside admin app create child app: 	C:\Users\TAE\Desktop\django-mysql-crud\webapplication - python manage.py startapp crudapplication

3.	create mysql database and name it "webapp"

4. webapplication/settings.py 	

	INSTALLED_APPS = [
	    'crudapplication',
	]

5. 	webapplication/settings.py change default database to mysql database connection like

	DATABASES = {
	    'default': {
	        'ENGINE': 'django.db.backends.mysql',
	        'NAME': 'webapp',
	        'USER': 'root',
	        'PASSWORD': '',
	        'HOST': '127.0.0.1',
	        'PORT': '3306',
	    }
	}

6. 	open cmd and run this code like C:\Users\TAE>pip install mysqlclient

7. crudapplication(child)/models.py 	from django.db import models

										class Employee(models.Model):
											eid = models.CharField(max_length=20)
											ename = models.CharField(max_length=100)
											eemail = models.EmailField()
											econtact = models.CharField(max_length=15)
											class Meta:
												db_table = "employee"

8. C:\Users\TAE\Desktop\django-mysql-crud\webapplication (project folder NOT the mother folder)

	- python manage.py makemigrations
	- python manage.py migrate

9. create folder templates and static in crudapplication(child)

10. webapplication(admin)/settings.py

	STATIC_URL = '/static/'  # this is the static folder you create

11. crudapplication(child)/views.py

	from django.shortcuts import render, redirect
	from crudapplication.forms import EmployeeForm
	from crudapplication.models import Employee

	def emp(request):
		if request.method == "POST":
			form = EmployeeForm(request.POST)
			if form.is_valid():
				try:
					form.save()
					return redirect("/show")
				except:
					pass
		else:
			form = EmployeeForm()
		return render(request,"index.html",{'form':form})

	def show(request):
		employees = Employee.objects.all()
		return render(request,"show.html", {'employees' : employees})

	def edit(request, id):
		employee = Employee.objects.get(id=id)
		return render(request, "edit.html", {'employee' : employee})

	def update(request, id):
		employee = Employee.objects.get(id=id)
		form = EmployeeForm(request.POST, instance = employee)
		if form.is_valid():
			form.save()
			return redirect('/show')
		return render(request, "edit.html", {'employee' : employee})

	def delete(request, id):
		employee = Employee.objects.get(id=id)
		employee.delete()
		return redirect("/show")

12. templates/index.html

	<!DOCTYPE html>
	<html>
	<head>
		<title>Index</title>
		{% load staticfiles %}
		<link rel="stylesheet" type="text/css" href="{% static '/style.css' %}">
	</head>
	<body>
		<form method="POST" class="post-form" action="/emp">  <!-- views.py/def emp() -->
			{% csrf_token %}
			<div class="container">
				<br>

				<div class="form-group row">
					<label class="col-sm-1 col-form-label"></label>
					<div class="col-sm-4">
						<h3>Enter Details</h3>
					</div>
				</div>

				<div class="form-group row">
					<label class="col-sm-2 col-form-label">Employee Id: </label>
					<div class="col-sm-4">
						{{ form.eid }}
					</div>
				</div>

				<div class="form-group row">
					<label class="col-sm-2 col-form-label">Employee Name: </label>
					<div class="col-sm-4">
						{{ form.ename }}
					</div>
				</div>

				<div class="form-group row">
					<label class="col-sm-2 col-form-label">Employee Email: </label>
					<div class="col-sm-4">
						{{ form.eemail }}
					</div>
				</div>

				<div class="form-group row">
					<label class="col-sm-2 col-form-label">Employee Contact: </label>
					<div class="col-sm-4">
						{{ form.econtact }}
					</div>
				</div>

				<div class="form-group row">
					<label class="col-sm-1 col-form-label"></label>
					<div class="col-sm-4">
						<button type="submit" class="btn btn-primary">Submit</button>
					</div>
				</div>

			</div>
		</form>
	</body>
	</html>


12. templates/show.html

	<!DOCTYPE html>
	<html>
	<head>
		<title>Employee Records</title>
		{% load staticfiles %}
		<link rel="stylesheet" type="text/css" href="{% static '/style.css' %}">
	</head>
	<body>
		<table class="table table-striped table-bordered table-sm">
			<thead class="thead-dark">
				<tr>
					<th>Employee ID</th>
					<th>Employee Name</th>
					<th>Employee Email</th>
					<th>Employee Contact</th>
					<th>Actions</th>
				</tr>
			</thead>
			<tbody>
				{% for employee in employees %}
					<tr>
						<td>{{ employee.eid }}</td>
						<td>{{ employee.ename }}</td>
						<td>{{ employee.eemail }}</td>
						<td>{{ employee.econtact }}</td>
						<td>
							<a href="/edit/{{ employee.id }}"><span glyphicon glyphicon-pencil>Edit</span></a>
							<a href="/delete/{{ employee.id }}">Delete</a>
						</td>
					</tr>
				{% endfor %}
			</tbody>
		</table>
		<br>
		<br>
		<center><a href="/emp" class="btn btn-primary">Add New Records</a></center>
	</body>
	</html>


13. templates/edit.html

	<!DOCTYPE html>
	<html>
	<head>
		<title>Index</title>
		{% load staticfiles %}
		<link rel="stylesheet" type="text/css" href="{% static '/style.css' %}">
	</head>
	<body>
		<form method="POST" class="post-form" action="/update/{{ employee.id }}">
			{% csrf_token %}
			<div class="container">
				<br>

				<div class="form-group row">
					<label class="col-sm-1 col-form-label"></label>
					<div class="col-sm-4">
						<h3>Enter Details</h3>
					</div>
				</div>

				<div class="form-group row">
					<label class="col-sm-2 col-form-label">Employee Id: </label>
					<div class="col-sm-4">
						<input type="text" name="eid" id="id_eid" required maxlength="20" value="{{ employee.eid }}">
					</div>
				</div>

				<div class="form-group row">
					<label class="col-sm-2 col-form-label">Employee Name: </label>
					<div class="col-sm-4">
						<input type="text" name="ename" id="id_ename" required maxlength="100" value="{{ employee.ename }}">
					</div>
				</div>

				<div class="form-group row">
					<label class="col-sm-2 col-form-label">Employee Email: </label>
					<div class="col-sm-4">
						<input type="text" name="eemail" id="id_eemail" required maxlength="254" value="{{ employee.eemail }}">
					</div>
				</div>

				<div class="form-group row">
					<label class="col-sm-2 col-form-label">Employee Contact: </label>
					<div class="col-sm-4">
						<input type="text" name="econtact" id="id_econtact" required maxlength="15" value="{{ employee.econtact }}">
					</div>
				</div>

				<div class="form-group row">
					<label class="col-sm-1 col-form-label"></label>
					<div class="col-sm-4">
						<button type="submit" class="btn btn-success">Update</button>
					</div>
				</div>

			</div>
		</form>
	</body>
	</html>


14. webapplication(admin)/urls.py

	from django.contrib import admin
	from django.urls import path
	from crudapplication import views

	urlpatterns = [
	    path('admin/', admin.site.urls),
	    path('emp', views.emp),
	    path('show', views.show),
	    path('edit/<int:id>', views.edit),
	    path('update/<int:id>', views.update),
	    path('delete/<int:id>', views.delete),
	]


15. run application

	C:\Users\TAE\Desktop\django-mysql-crud\webapplication
	python manage.py runserver

	http://localhost:8000/show 	- run
	http://localhost:8000		- error

	note: dont forget to turn on the mysql