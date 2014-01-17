# -*- coding: utf-8 -*-
#
#  This file is part of django-powerdns-manager.
#
#  django-powerdns-manager is a web based PowerDNS administration panel.
#
#  Development Web Site:
#    - http://www.codetrax.org/projects/django-powerdns-manager
#  Public Source Code Repository:
#    - https://source.codetrax.org/hgroot/django-powerdns-manager
#
#  Copyright 2012 George Notaras <gnot [at] g-loaded.eu>
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

class PowerdnsManagerDbRouter(object):
    """A router to control all database operations on models in
    the 'powerdns_manager' application.
    
    Based on the default example router of Django 1.4:
    
        https://docs.djangoproject.com/en/1.4/topics/db/multi-db/#an-example
    
    It is highly recommended to configure django-powerdns-manager to use a
    different database than the rest of the apps of the Django project for
    security and performance reasons.
    
    The ``PowerdnsManagerDbRouter`` database router is provided for this
    purpose. All you need to do, is configure an extra database in
    ``settings.py`` named ``powerdns`` and add this router to the
    ``DATABASE_ROUTERS`` list.
    
    The following example assumes using SQLite databases, but your are free to
    use any database backend you want, provided that it is also supported by
    the PowerDNS server software::
    
        DATABASES = {
            'default': {    # Used by all apps of the Django project except django-powerdns-manager
                'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
                'NAME': 'main.db',               # Or path to database file if using sqlite3.
                'USER': '',                      # Not used with sqlite3.
                'PASSWORD': '',                  # Not used with sqlite3.
                'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
                'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
            },
            'powerdns': {    # Used by django-powerdns-manager and PowerDNS server
                'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
                'NAME': 'powerdns.db',           # Or path to database file if using sqlite3.
                'USER': '',                      # Not used with sqlite3.
                'PASSWORD': '',                  # Not used with sqlite3.
                'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
                'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
            }
        }

        DATABASE_ROUTERS = ['powerdns_manager.routers.PowerdnsManagerDbRouter']
    
    The configuration above indicates that ``main.db`` will be used by all
    the apps of the Django project, except ``django-powerdns-manager``. The
    ``powerdns.db`` database will be used by ``django-powerdns-manager``.
    PowerDNS should also be configured to use ``powerdns.db``.
    
    Run syncdb like this:
    
        python manage.py syncdb
        python manage.py syncdb --database=powerdns
    
    """

#    def db_for_read(self, model, **hints):
#        """Point all operations on powerdns_manager models to 'powerdns'"""
#        
#         if model._meta.app_label == 'powerdns_manager':
#             if hints.has_key('instance'):
#                 obj = hints['instance']
#                 raise Exception(obj._state.db)
#                 from django.db.models.loading import cache
#                 Domain = cache.get_model('powerdns_manager', 'Domain')
#                 
#                 if not isinstance(obj, Domain):
#                     return 'default'
#             return 'powerdns'
#         return None
#         if hints.has_key('instance'):
#             from django.contrib.auth import get_user_model
#             from django.db.models.loading import cache
#             User = get_user_model()
#             Domain = cache.get_model('powerdns_manager', 'Domain')
#             
#             obj = hints['instance']
#             
#             if isinstance(obj, Domain):
#                 return 'powerdns'
#             return 'default'
#         
#             #if isinstance(obj, User):
#             #    return 'default'
#             #elif isinstance(obj, Domain):
#             #    return 'powerdns'
#             ##raise Exception(hints)
#             raise Exception( 'READ OBJ: ' + str(type(hints['instance'])) + str(hints) )
#         if len(hints.keys()) > 1:
#             raise Exception(hints)
#         
#         if model._meta.app_label == 'powerdns_manager':
#             if hints.has_key('instance'):
#                 from django.db.models.loading import cache
#                 Domain = cache.get_model('powerdns_manager', 'Domain')
#                 obj = hints['instance']
#                 if not isinstance(obj, Domain):
#                     return 'default'
#             return 'powerdns'
#         
#         if hints.has_key('instance'):
#             from django.db.models.loading import cache
#             Domain = cache.get_model('powerdns_manager', 'Domain')
#             obj = hints['instance']
#             if isinstance(obj, Domain):
#                 return 'powerdns'
#         return 'default'
#
#         elif model._meta.app_label == 'auth':
#             #raise Exception(hints)
#             #raise Exception( 'READ OBJ: ' + str(type(hints['instance'])) + str(hints) )
#             return 'default'
#         elif model._meta.app_label == 'sessions':
#             return 'default'
#         elif model._meta.app_label == 'contenttypes':
#             return 'default'
#         
#         #raise Exception('READ app label: ' + model._meta.app_label)
#     
#         #raise Exception(type(hints['instance']))
#         #elif model._meta.app_label == 'sessions':
#         #    return 'default'
#         
#         #if hints.has_key('instance'):
#             # The ModelAdmin for the Domain model needs to display information
#             # about a user (zone owner) or determine which fields to show based
#             # on user superuser status. By default it searches for the user
#             # table in the 'powerdns' database (used for Domain model).
#             # The table does not exist there, but in the 'default database,
#             # so there is an error: notable auth_user.
#             # In those cases we use the hints dictionary and check if the
#             # instance object is an instance of the auth.User model.
#             # If yes, then we return the 'default' database.
#             #
#             # Determined the type with:
#             #raise Exception(type(hints['instance']))
#             
#             # This works partially.
#             obj = hints['instance']
#             from django.contrib.auth import get_user_model
#             from django.db.models.loading import cache
#             User = get_user_model()
#             Domain = cache.get_model('powerdns_manager', 'Domain')
#             if isinstance(obj, User):
#                 return 'default'
#             if isinstance(obj, Domain):
#                 return 'powerdns'
# 
#             # OTHER
#             #
#             #raise Exception(type(hints['instance']))
#             #obj = hints['instance']
#             #from django.contrib.auth import get_user_model
#             #raise Exception(get_user_model())
#             #User = get_user_model()
#             #if isinstance(obj, User):
#             #    raise Exception(model._meta.app_label)
#             #from django.contrib.contenttypes.models import ContentType
#             #if ContentType.objects.get_for_model(obj).name == 'user':
#             #    #raise Exception('here')
#             #    return 'default'
#             #raise Exception(model._meta.app_label)
#             #raise Exception(type(hints['instance']))
#             #if ContentType.objects.get_for_model(obj) == ContentType.objects.get_for_model(User):
#             #if ContentType.objects.get_for_model(obj).name == 'user':
#             #    raise Exception(type(hints['instance']))
#             #    return 'default'
#             #from django.contrib.auth.models import User
#             #if isinstance(hints['instance'], get_user_model()):
#             #return 'default'
#             #if isinstance(obj, User):
#             #if hasattr(obj, 'get_full_name'):
#                 # Return the default database, since the user table is there.
#             #    return 'default'
#         #raise Exception(model._meta.app_label)
#         #return None
# 
#     def db_for_write(self, model, **hints):
#         """Point all operations on powerdns_manager models to 'powerdns'"""
#         if len(hints.keys()) > 1:
#             raise Exception(hints)
#         if model._meta.app_label == 'powerdns_manager':
#             if hints.has_key('instance'):
#                 from django.db.models.loading import cache
#                 Domain = cache.get_model('powerdns_manager', 'Domain')
#                 obj = hints['instance']
#                 if not isinstance(obj, Domain):
#                     return 'default'
#             return 'powerdns'
#         
#         if hints.has_key('instance'):
#             from django.db.models.loading import cache
#             Domain = cache.get_model('powerdns_manager', 'Domain')
#             obj = hints['instance']
#             if isinstance(obj, Domain):
#                 return 'powerdns'
#         return 'default'
#        
#         if hints.has_key('instance'):
#             from django.contrib.auth import get_user_model
#             from django.db.models.loading import cache
#             User = get_user_model()
#             Domain = cache.get_model('powerdns_manager', 'Domain')
#             
#             obj = hints['instance']
#             
#             if isinstance(obj, Domain):
#                 return 'powerdns'
#             return 'default'
#             #if isinstance(obj, User):
#             #    return 'default'
#             #elif isinstance(obj, Domain):
#             #    return 'powerdns'
#             #raise Exception(hints)
#             raise Exception( 'WRITE OBJ: ' + str(type(hints['instance'])) + str(hints) )
#         
#         if model._meta.app_label == 'powerdns_manager':
#             #raise Exception( 'WRITE OBJ: ' + str(type(hints['instance'])) + str(hints) )
#             return 'powerdns'
#         elif model._meta.app_label == 'auth':
#             return 'default'
#         elif model._meta.app_label == 'sessions':
#             return 'default'
#         elif model._meta.app_label == 'contenttypes':
#             return 'default'
# 
#         #raise Exception('WRITE app label: ' + model._meta.app_label)
# #         #raise Exception(type(hints['instance']))
# 
#         return None
# 
#     def allow_relation(self, obj1, obj2, **hints):
#         """Allow any relation if a model in powerdns_manager is involved"""
#         #raise Exception(obj1._meta.app_label + ' - ' + obj2._meta.app_label)
#         if obj1._meta.app_label == 'powerdns_manager' or obj2._meta.app_label == 'powerdns_manager':
#             return True
#         #return True
#         #raise Exception(obj1._meta.app_label + ' - ' + obj2._meta.app_label)
#         return None
# 
#     def allow_syncdb(self, db, model):
#         """Make sure the powerdns_manager app only appears on the 'powerdns' db"""
#         if db == 'powerdns':
#             return model._meta.app_label == 'powerdns_manager'
#         elif model._meta.app_label == 'powerdns_manager':
#             return False
#         return None
