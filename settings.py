INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Third-party
    "graphene_django",

    # Local apps
    "crm",
]

# Add Graphene settings
GRAPHENE = {
    "SCHEMA": "alx_backend_graphql_crm.schema.schema",  # path to schema
}

