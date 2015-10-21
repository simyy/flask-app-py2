#Flask-Example

> This is a example of flask project.

##structure

--app (project src)
  -- __init__.py (flask app)
  -- config.py   (project config)
  -- email.py    (project email)
  -- models.py   (models by sqlalchemy)
  -- static      
  -- templates
  -- main        (an application of project, a project can contains more than one it)
-- tests         (unittest)
-- venv          (python virtual envirenment)

##requirement

generate a new requirement

```
pip freeze > requirement.txt
```

install all the requirement

```
pip install -r requirement.txt
```

##migrate

To create a new table or upgrade it, run 

```
python manage.py db upgrade
```

Before it, the dir of `migarations` must be deleted.
