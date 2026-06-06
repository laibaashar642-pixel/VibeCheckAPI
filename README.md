# VibeCheck API 🎮

> *tell me your vibe. i'll tell you what to do.*

a mood-based entertainment recommender built with Django REST Framework + Linear Regression. you give it your mood — it tells you whether to game, chill, meditate, or watch something. built in 2 days as a learning project combining ML + backend dev.

---

## what it does

```
POST /api/predict/

input:  { mood, energy, time_of_day }
output: { recommendation }
```

that's it. simple. clean. works.

---

## tech stack

```python
backend    = "Django + Django REST Framework"
ml_model   = "Linear Regression (sklearn)"
database   = "SQLite"
language   = "Python 3.13"
```

---

## endpoints

| method | endpoint | what it does |
|--------|----------|-------------|
| GET | `/api/vibe/` | get all vibes |
| POST | `/api/vibe/` | save a new vibe |
| PUT | `/api/vibe/<id>/` | update a vibe |
| DELETE | `/api/vibe/<id>/` | delete a vibe |
| POST | `/api/predict/` | get a recommendation |

---

## how to run

```bash
# clone karo
git clone https://github.com/laibaashar642-pixel/vibecheck-api
cd vibecheck-api

# venv banao
python -m venv venv
venv\Scripts\activate  # windows

# install karo
pip install django djangorestframework scikit-learn numpy matplotlib

# migrate karo
python manage.py makemigrations
python manage.py migrate

# chala lo
python manage.py runserver
```

---

## example request

```json
POST /api/predict/

{
    "mood": "happy",
    "energy": 8,
    "time": "morning"
}
```

```json
response:

{
    "recommendation": "play games 🎮"
}
```

---

## mood options

```
happy / angry / sad / excited / anxious
```

## time options

```
morning / afternoon / evening / night
```

## recommendations

```
1 → go for a walk 🚶
2 → listen to music 🎵
3 → meditate 🧘
4 → play games 🎮
5 → watch a movie 🎬
```

---

## project structure

```
vibecheck/
├── core/
│   ├── settings.py
│   └── urls.py
├── vibe/
│   ├── models.py        # Vibe model
│   ├── serializers.py   # VibeSerializers
│   ├── views.py         # APIView — GET POST PUT DELETE + PredictView
│   ├── urls.py          # URL routing
│   ├── ml_model.py      # Linear Regression model
│   └── graph.py         # matplotlib visualization
└── manage.py
```

---

## what i learned

- combining ML with a REST API
- Django REST Framework — APIView end to end
- Linear Regression for recommendation logic
- debugging import errors at 11pm 💀

---

## built by

**Laiba Ashar** — AI Intern @ Webevis Technology · 4th Sem IT Student · Lahore, PK 🇵🇰

*"build it, break it, learn from it."*

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/laibaashar642-pixel)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com/in/laiba-ashar-782b96376/)
