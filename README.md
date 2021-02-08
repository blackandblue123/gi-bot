# Genshin Bot 

Discord bot that tries to integrate an ORM via a beta version of sqlalchemy to an sqlite database 


### Setup

Install pipenv
```
python install pipenv
```

Activate environment then install requirements
```
pipenv shell
```
```
pipenv install
```

Input discord token to the `.env` file 
```
TOKEN=<token>
```

### Input data to the database
run populate.py
```
python populate.py
```

### Run the bot
```
python bot.py
```

### Commands
`<input>` can be an incomplete string/name (acting like a search), the commands use sqlalchemy object query's `like`

```
!character <input>
```
```
!weapon <input>
```
```
!artifact <input>
```