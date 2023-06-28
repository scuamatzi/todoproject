# TODO API with FastAPI

#### Exercise from freecodecamp at youtube (FARM Stack project)

Simple TODO Project. The backend was created following the tutorial from freecodecamp using FastAPI. After that, I modify it to use mongodb. It can run completely on AWS Lambda for testing.

https://youtu.be/OzUzrs8uJl8




## Sensible Data

Include user, password and uri for database connection in a file called pass.json.

```json
{
    "user":"user",
    "pass":"password",
    "uri":"URL"
}
```


## Run Locally

Get a mongodb database running, it could be with docker.

Update info in pass.json

In linux follow this steps inside the folder project (may use env):

```bash
pip install -r requirements.txt
```
```bash
uvicorn main:app --reload
```

Now the app runs on localhost:
```bash
http://localhost:8000/api/todo/
```


## Run on AWS Lambda

Get a mongodb database running on mongodb Atlas or other service.

Update data in pass.json

In linux follow this steps inside the folder project:

```bash
mkdir dep
```
```bash
pip install -t dep -r requirements.txt
```
```bash
cd dep
```
```bash
zip ../lambdafastapi.zip -r .
```
```bash
cd ../
```
```bash
zip -r -u lambdafastapi.zip database.py main.py model.py pass.json templates/

```

Now create a lambda function on AWS and upload the file lambdafastapi.zip

Be sure to enable "Function URL" and set it to NONE for authN for testing purposes.

After creation, change lambda handler to 'main.handler'

Add /api/todo to AWS URL.

