


# Final-Project !

Web Programming with Python and JavaScript



# Introduction
 This is a full featured dynamic  portfolio website using django . portfolio website includes personal blog ,personal details listing out personal skills ,experience and  showcase of achievement .user can share his knowledge ,opinion with much more community by writing through blog .
 introductory video : url: https://youtu.be/5hskNQ-vInk


# Project Structure

## Main Page

In main page , you will see  all personal details of the user .

Besides, if you just want to read articles shared by user, just click on blog button in top of the page ,it will redirect you to blog page . you can see the accomplishment of owner by clicking on accomplishment button in top of the page .

![main page](/screenshot/slideshow.png)

## About section
here you will see the personal details of user
![about](/screenshot/about.png)

## accomplishment section

By clicking on accomplishment button ,you will see the achievement of owner .
![accomplishment](/screenshot/training.png)


## blog Page
you will see the latest blog created by user . you will also see different catagories listed there ,you can choose any catagory and read related blog by clicking there .
![blog](/screenshot/blog.png)

## blog details
if you click on any post listed in blog page ,you will be redirect to details page ,there you can read the article and also put your comment there .
![details](/screenshot/detail.png)
![details](/screenshot/comment.png)

# Back End
in Backend ,i ahve used postgresql for database . there have 4 models including Achievement ,blog ,catagory ,comment .
![backend](/screenshot/backend.png)

## Super User
super user is the powerful data manipulation tool provided by django . you can create super user by running command : python manage.py createsuperuser

#comment approval :
you can approve and control  comments of other users to display in blog page ,by deafult it is not approved .

# Setup
git clone https://github.com/me50/Abu-Kowcher-Rmstu2.git
cd Abu-Kowcher-Rmstu2
pip install -r requirements.txt

When the dependent packages are installed, you can run this command to run your server.

```shell script
python manage.py runserver
```

Run those following commands to migrate database.

```shell script
python manage.py makemigrations
python manage.py migrate
```

Or you can run this command to shell window.

```shell script
python manage.py shell
```





# Finally

Thanks to all members of [CS50's Web Programming with Python and JavaScript](https://www.edx.org/course/cs50s-web-programming-with-python-and-javascript) course . Especially, i want to mention  for [Brain Yu](https://www.edx.org/bio/brian-yu)'s excellent lecture and his "great question", which motivate me to finish the course study.
