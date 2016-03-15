# Phresko REST API

## Folder structure
* *config* : django rest api project settings
* *restapi* : REST server

## Development Environment Setup

```bash
git clone https://github.com/langJohn/phresko.git
```

###Virtual Environment

```bash
cd phresko
./pysetup
```

The project root folder stucture should look like the following:

```
phresko/
py-venv-phresko
```

To enter project virtual env, run:

```bash
/pyenv
(py-venv-phresko) $
```
###mySQL

You'll need to create MySQL database locally

```bash
mysql -u username -puser_password
create database phresko
```

###First Start

```bash
./pyenv ./manage.py makemigrations
./pyenv ./manage.py migrate
./pyenv ./manage.py runserver
```

###TBD