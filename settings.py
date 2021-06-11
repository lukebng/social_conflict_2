from os import environ


SESSION_CONFIGS = [
    dict(
        name='SoCo',
        display_name="Entscheidungsaufgabe",
        num_demo_participants=2,
        app_sequence=['labids', 'consent', 'instructions', 'samegroup', 'randomgroup', 'showup'],
        use_browser_bots=False,
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=0.01, participation_fee=2.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'de'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = True

POINTS_CUSTOM_NAME = 'Cent'

ROOMS = [
    dict(
        name='soziale_interaktionen',
        display_name='Entscheidungsaufgabe Raum'
    )
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """


SECRET_KEY = 'xj$ii$mrxjjtg)dz$-9ll&b#i5ac2!cguf!gj%z6e02a=1-cf_'

INSTALLED_APPS = ['otree']

PARTICIPANT_FIELDS = ['DecisionLabID', 'wait_page_arrival', 'role', 'partner', 'treat', 'timo']
