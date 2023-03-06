from structures import User

# alt vores data er kun gemt i programmets hukommelse.
# dvs. at alt vil blive glemt, hvis du genstarter programmet.

VALID_STUDY_FIELDS = (
    "Bioinformatik",
    "Computer Science - Informatik",
    "Computer Science - Programmering",
    "Geoscience",
    "Science Fysik",
    "Science Kemi",
    "Teknologi og Design",
    "Teknologi og Samfundsfag",
)

VALID_VALGFAG = (
    "Astronomi",
    "Biologi",
    "Design",
    "Engelsk",
    "Erhversøkonomi",
    "Filosofi",
    "Fransk",
    "Fysik",
    "Idræt",
    "Informatik",
    "Innovation",
    "Kemi",
    "Kommunikation og IT",
    "Matematik",
    "Mediefag",
    "Musik",
    "Programmering",
    "Psykologi",
    "Retorik",
    "Samfundsfag",
    "Statik og Styrkelære",
    "Statistik",
    "Teknologi",
    "Tysk",
)

DEFAULT_SESSION = {
    "logged_in": False,
    "username": "",
    "id": -1,
    "display": "",
    "grade": "",
    "field_of_study": "",
    "optional_subject": "",
}

data = {
    "reviews_for_studieretninger": [
        {
            "posted": 25,
            "user": User(
                username="simonglob",
                display="Simon Glob",
                id=1,
                field_of_study="Bioinformatik",
                optional_subject="Psykologi",
                grade="1.C",
                password="b30bd351371c686298d32281b337e8e9",  # simon
            ).__dict__,
            "id": 2,
            "title": "jeg elsker biologi",
            "content": "biologi er det bedste der findes.",
            "hearts": 23,
            "rating": 0,
            "field_of_study": "Bioinformatik",
            "comments": [
                {
                    "user": User(
                        username="emilvoss",
                        display="Emil Voss Kjærgaard",
                        id=3,
                        field_of_study="Bioinformatik",
                        optional_subject="Idræt",
                        grade="1.C",
                        password="745892a68d01cc274bfb82b5b8616904",  # voss
                    ).__dict__,
                    "id": 12,
                    "content": "Jeg er fuldstændig enig med dig.",
                    "hearts": 11,
                },
                {
                    "user": User(
                        username="emilrem",
                        display="Emil Rem Rasmussen",
                        id=2,
                        field_of_study="Bioinformatik",
                        optional_subject="Idræt",
                        grade="1.C",
                        password="5cadb523cb6909f92350f70f124adfb8",  # rem
                    ).__dict__,
                    "content": "Helt enig",
                    "hearts": 0,
                },
            ],
        }
    ],
    "reviews_for_valgfag": [
        {
            "posted": 21384344,
            "user": User(
                username="simonglob",
                display="Simon Glob",
                id=1,
                field_of_study="Bioinformatik",
                optional_subject="Psykologi",
                grade="1.C",
                password="b30bd351371c686298d32281b337e8e9",  # simon
            ).__dict__,
            "id": 1,
            "title": "ez 7 tal i psykologi",
            "content": "Psykologi kan man pjække fra og stadig få 7",
            "hearts": 23,
            "rating": 0,
            "subject": "Psykologi",
            "comments": [
                {
                    "user": User(
                        username="emilvoss",
                        display="Emil Voss Kjærgaard",
                        id=3,
                        field_of_study="Bioinformatik",
                        optional_subject="Idræt",
                        grade="1.C",
                        password="745892a68d01cc274bfb82b5b8616904",  # voss
                    ).__dict__,
                    "id": 12,
                    "content": "Jeg er fuldstændig enig med dig.",
                    "hearts": 1,
                },
                {
                    "user": User(
                        username="emilrem",
                        display="Emil Rem Rasmussen",
                        id=2,
                        field_of_study="Bioinformatik",
                        optional_subject="Idræt",
                        grade="1.C",
                        password="5cadb523cb6909f92350f70f124adfb8",  # rem
                    ).__dict__,
                    "content": "Helt enig",
                    "hearts": 0,
                },
            ],
        }
    ],
    "users": [
        User(
            username="admin",
            display="admin",
            id=0,
            field_of_study="Science Fysik",
            optional_subject="Fransk",
            grade="1.X",
            password="21232f297a57a5a743894a0e4a801fc3",  # admin
        ),
        User(
            username="simonglob",
            display="Simon Glob",
            id=1,
            field_of_study="Bioinformatik",
            optional_subject="Psykologi",
            grade="1.C",
            password="b30bd351371c686298d32281b337e8e9",  # simon
        ),
        User(
            username="emilrem",
            display="Emil Rem Rasmussen",
            id=2,
            field_of_study="Bioinformatik",
            optional_subject="Idræt",
            grade="1.C",
            password="5cadb523cb6909f92350f70f124adfb8",  # rem
        ),
        User(
            username="emilvoss",
            display="Emil Voss Kjærgaard",
            id=3,
            field_of_study="Bioinformatik",
            optional_subject="Idræt",
            grade="1.C",
            password="745892a68d01cc274bfb82b5b8616904",  # voss
        ),
    ],
    "likes": {3: [1]},
}
