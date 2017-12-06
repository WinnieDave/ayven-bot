# ayven-bot
ayven\`s bot for the MAN contest


to deploy on heroku.com go to apps=>new=>create new app=>deploy=> in deployment method choose github=>
add a repo=>deploy=>install heroku cli(https://devcenter.heroku.com/articles/getting-started-with-python#introduction) =>clone your repo into local folder=>
run there git remote add heroku git@heroku:*your_project_name_here*.git(https://stackoverflow.com/questions/5129598/how-to-link-a-folder-with-an-existing-heroku-app)
=>scale your dynos to at least 1 with heroku ps:scale worker=1(that\`s the type of worker that\`s declared in Procfile)(https://devcenter.heroku.com/articles/getting-started-with-python#scale-the-app).
