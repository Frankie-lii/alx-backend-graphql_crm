INSTALLED_APPS = [
    # other apps
    'django_crontab',
]

CRONJOBS = [
    ('*/5 * * * *', 'crm.cron.logcrmheartbeat'),
]

