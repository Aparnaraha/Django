# Django
With the basics of Python, HTML and CSS knowledge you need to start this tutorial. I'll be following this Django documentation mentioned in the below link

https://docs.djangoproject.com/en/4.2/contents/

You could check the codes with proper folder and its requirements here in my codespace mentioned below link

https://glorious-spork-v59xpxrgvp5h6ggq.github.dev/

Django documentation contents¶

    Getting started
        Django at a glance
            Design your model
            Install it
            Enjoy the free API
            A dynamic admin interface: it’s not just scaffolding – it’s the whole house
            Design your URLs
            Write your views
            Design your templates
            This is just the surface
        Quick install guide
            Install Python
            Set up a database
            Install Django
            Verifying
            That’s it!
        Writing your first Django app, part 1
            Creating a project
            The development server
            Creating the Polls app
            Write your first view
        Writing your first Django app, part 2
            Database setup
            Creating models
            Activating models
            Playing with the API
            Introducing the Django Admin
        Writing your first Django app, part 3
            Overview
            Writing more views
            Write views that actually do something
            Raising a 404 error
            Use the template system
            Removing hardcoded URLs in templates
            Namespacing URL names
        Writing your first Django app, part 4
            Write a minimal form
            Use generic views: Less code is better
        Writing your first Django app, part 5
            Introducing automated testing
            Basic testing strategies
            Writing our first test
            Test a view
            When testing, more is better
            Further testing
            What’s next?
        Writing your first Django app, part 6
            Customize your app’s look and feel
            Adding a background-image
        Writing your first Django app, part 7
            Customize the admin form
            Adding related objects
            Customize the admin change list
            Customize the admin look and feel
            Customize the admin index page
        Writing your first Django app, part 8
            Installing Django Debug Toolbar
            Getting help from others
            Installing other third-party packages
            What’s next?
        Advanced tutorial: How to write reusable apps
            Reusability matters
            Your project and your reusable app
            Installing some prerequisites
            Packaging your app
            Using your own package
            Publishing your app
            Installing Python packages with a virtual environment
        What to read next
            Finding documentation
            How the documentation is organized
            How documentation is updated
            Where to get it
            Differences between versions
        Writing your first patch for Django
            Introduction
            Code of Conduct
            Installing Git
            Getting a copy of Django’s development version
            Running Django’s test suite for the first time
            Working on a feature
            Creating a branch for your patch
            Writing some tests for your ticket
            Writing the code for your ticket
            Running Django’s test suite for the second time
            Writing Documentation
            Previewing your changes
            Committing the changes in the patch
            Pushing the commit and making a pull request
            Next steps
    Using Django
        How to install Django
            Install Python
            Install Apache and mod_wsgi
            Get your database running
            Install the Django code
        Models and databases
            Models
            Making queries
            Aggregation
            Search
            Managers
            Performing raw SQL queries
            Database transactions
            Multiple databases
            Tablespaces
            Database access optimization
            Database instrumentation
            Fixtures
            Examples of model relationship API usage
        Handling HTTP requests
            URL dispatcher
            Writing views
            View decorators
            File Uploads
            Django shortcut functions
            Generic views
            Middleware
            How to use sessions
        Working with forms
            HTML forms
            Django’s role in forms
            Forms in Django
            Building a form
            More about Django Form classes
            Working with form templates
            Further topics
        Templates
            The Django template language
            Support for template engines
        Class-based views
            Introduction to class-based views
            Built-in class-based generic views
            Form handling with class-based views
            Using mixins with class-based views
            Basic examples
            Usage in your URLconf
            Subclassing generic views
            Asynchronous class-based views
        Migrations
            The Commands
            Backend Support
            Workflow
            Transactions
            Dependencies
            Migration files
            Adding migrations to apps
            Reversing migrations
            Historical models
            Considerations when removing model fields
            Data Migrations
            Squashing migrations
            Serializing values
            Supporting multiple Django versions
        Managing files
            Using files in models
            The File object
            File storage
        Testing in Django
            Writing and running tests
            Testing tools
            Advanced testing topics
        User authentication in Django
            Overview
            Installation
            Usage
        Django’s cache framework
            Setting up the cache
            The per-site cache
            The per-view cache
            Template fragment caching
            The low-level cache API
            Asynchronous support
            Downstream caches
            Using Vary headers
            Controlling cache: Using other headers
            Order of MIDDLEWARE
        Conditional View Processing
            The condition decorator
            Shortcuts for only computing one value
            Using the decorators with other HTTP methods
            Comparison with middleware conditional processing
        Cryptographic signing
            Protecting SECRET_KEY and SECRET_KEY_FALLBACKS
            Using the low-level API
        Sending email
            Quick example
            send_mail()
            send_mass_mail()
            mail_admins()
            mail_managers()
            Examples
            Preventing header injection
            The EmailMessage class
            Email backends
            Configuring email for development
        Internationalization and localization
            Overview
            Definitions
        Logging
            Overview
            Security implications
            Configuring logging
        Pagination
            The Paginator class
            Example
            Paginating a ListView
            Using Paginator in a view function
        Security in Django
            Cross site scripting (XSS) protection
            Cross site request forgery (CSRF) protection
            SQL injection protection
            Clickjacking protection
            SSL/HTTPS
            Host header validation
            Referrer policy
            Cross-origin opener policy
            Session security
            User-uploaded content
            Additional security topics
        Performance and optimization
            Introduction
            General approaches
            Caching
            Understanding laziness
            Databases
            HTTP performance
            Template performance
            Using different versions of available software
        Serializing Django objects
            Serializing data
            Deserializing data
            Serialization formats
            Natural keys
        Django settings
            The basics
            Designating the settings
            Default settings
            Using settings in Python code
            Altering settings at runtime
            Security
            Available settings
            Creating your own settings
            Using settings without setting DJANGO_SETTINGS_MODULE
        Signals
            Listening to signals
            Defining and sending signals
            Disconnecting signals
        System check framework
            Writing your own checks
        External packages
            Localflavor
            Comments
            Formtools
        Asynchronous support
            Async views
            Async safety
            Async adapter functions
    “How-to” guides
        How to authenticate using REMOTE_USER
            Configuration
            Using REMOTE_USER on login pages only
        How to use Django’s CSRF protection
            Using CSRF protection with AJAX
            Using CSRF protection in Jinja2 templates
            Using the decorator method
            Handling rejected requests
            Using CSRF protection with caching
            Testing and CSRF protection
            Edge cases
            CSRF protection in reusable applications
        How to create custom django-admin commands
            Accepting optional arguments
            Management commands and locales
            Testing
            Overriding commands
            Command objects
        How to create custom model fields
            Introduction
            Background theory
            Writing a field subclass
            Writing a FileField subclass
        How to write custom lookups
            A lookup example
            A transformer example
            Writing an efficient abs__lt lookup
            A bilateral transformer example
            Writing alternative implementations for existing lookups
            How Django determines the lookups and transforms which are used
        How to implement a custom template backend
            Custom backends
            Debug integration for custom engines
        How to create custom template tags and filters
            Code layout
            Writing custom template filters
            Writing custom template tags
        How to write a custom storage class
            Use your custom storage engine
        How to deploy Django
            How to deploy with WSGI
            How to deploy with ASGI
            Deployment checklist
        How to upgrade Django to a newer version
            Required Reading
            Dependencies
            Resolving deprecation warnings
            Installation
            Testing
            Deployment
        How to manage error reporting
            Email reports
            Filtering error reports
        How to provide initial data for models
            Provide initial data with migrations
            Provide data with fixtures
        How to integrate Django with a legacy database
            Give Django your database parameters
            Auto-generate the models
            Install the core Django tables
            Test and tweak
        How to configure and use logging
            Make a basic logging call
            Customize logging configuration
        How to create CSV output
            Using the Python CSV library
            Using the template system
            Other text-based formats
        How to create PDF files
            Install ReportLab
            Write your view
            Other formats
        How to override templates
            Overriding from the project’s templates directory
            Overriding from an app’s template directory
            Extending an overridden template
        How to manage static files (e.g. images, JavaScript, CSS)
            Configuring static files
            Serving static files during development
            Serving files uploaded by a user during development
            Testing
            Deployment
            Learn more
        How to deploy static files
            Serving static files in production
            Learn more
        How to install Django on Windows
            Install Python
            About pip
            Setting up a virtual environment
            Install Django
            Colored terminal output
            Common pitfalls
        How to create database migrations
            Data migrations and multiple databases
            Migrations that add unique fields
            Controlling the order of migrations
            Migrating data between third-party apps
            Changing a ManyToManyField to use a through model
            Changing an unmanaged model to managed
        How to delete a Django application
    Django FAQ
        FAQ: General
            Why does this project exist?
            What does “Django” mean, and how do you pronounce it?
            Is Django stable?
            Does Django scale?
            Who’s behind this?
            How is Django licensed?
            Why does Django include Python’s license file?
            Which sites use Django?
            Django appears to be a MVC framework, but you call the Controller the “view”, and the View the “template”. How come you don’t use the standard names?
            <Framework X> does <feature Y> – why doesn’t Django?
            Why did you write all of Django from scratch, instead of using other Python libraries?
            Is Django a content-management-system (CMS)?
            How can I download the Django documentation to read it offline?
            How do I cite Django?
        FAQ: Installation
            How do I get started?
            What are Django’s prerequisites?
            What Python version can I use with Django?
            What Python version should I use with Django?
            Should I use the stable version or development version?
        FAQ: Using Django
            Why do I get an error about importing DJANGO_SETTINGS_MODULE?
            I can’t stand your template language. Do I have to use it?
            Do I have to use your model/database layer?
            How do I use image and file fields?
            How do I make a variable available to all my templates?
        FAQ: Getting Help
            How do I do X? Why doesn’t Y work? Where can I go to get help?
            Why hasn’t my message appeared on django-users?
            Nobody answered my question! What should I do?
            I think I’ve found a bug! What should I do?
            I think I’ve found a security problem! What should I do?
        FAQ: Databases and models
            How can I see the raw SQL queries Django is running?
            Can I use Django with a preexisting database?
            If I make changes to a model, how do I update the database?
            Do Django models support multiple-column primary keys?
            Does Django support NoSQL databases?
            How do I add database-specific options to my CREATE TABLE statements, such as specifying MyISAM as the table type?
        FAQ: The admin
            I can’t log in. When I enter a valid username and password, it just brings up the login page again, with no error messages.
            I can’t log in. When I enter a valid username and password, it brings up the login page again, with a “Please enter a correct username and password” error.
            How do I automatically set a field’s value to the user who last edited the object in the admin?
            How do I limit admin access so that objects can only be edited by the users who created them?
            My admin-site CSS and images showed up fine using the development server, but they’re not displaying when using mod_wsgi.
            My “list_filter” contains a ManyToManyField, but the filter doesn’t display.
            Some objects aren’t appearing in the admin.
            How can I customize the functionality of the admin interface?
            The dynamically-generated admin site is ugly! How can I change it?
            What browsers are supported for using the admin?
        FAQ: Contributing code
            How can I get started contributing code to Django?
            I submitted a bug fix in the ticket system several weeks ago. Why are you ignoring my patch?
            When and how might I remind the team of a patch I care about?
            But I’ve reminded you several times and you keep ignoring my patch!
            I’m sure my ticket is absolutely 100% perfect, can I mark it as “Ready For Checkin” myself?
        Troubleshooting
            Problems running django-admin
            Miscellaneous
    API Reference
        Applications
            Projects and applications
            Configuring applications
            Application configuration
            Application registry
            Initialization process
        System check framework
            API reference
            Builtin tags
            Core system checks
            contrib app checks
        Built-in class-based views API
            Base views
            Generic display views
            Generic editing views
            Generic date views
            Class-based views mixins
            Class-based generic views - flattened index
            Specification
            Base vs Generic views
        Clickjacking Protection
            An example of clickjacking
            Preventing clickjacking
            How to use it
            Limitations
        contrib packages
            The Django admin site
            django.contrib.auth
            The contenttypes framework
            The flatpages app
            GeoDjango
            django.contrib.humanize
            The messages framework
            django.contrib.postgres
            The redirects app
            The sitemap framework
            The “sites” framework
            The staticfiles app
            The syndication feed framework
            admin
            auth
            contenttypes
            flatpages
            gis
            humanize
            messages
            postgres
            redirects
            sessions
            sites
            sitemaps
            syndication
            Other add-ons
        Cross Site Request Forgery protection
            How it works
            Limitations
            Utilities
            Settings
            Frequently Asked Questions
        Databases
            General notes
            PostgreSQL notes
            MariaDB notes
            MySQL notes
            SQLite notes
            Oracle notes
            Subclassing the built-in database backends
            Using a 3rd-party database backend
        django-admin and manage.py
            Usage
            Available commands
            Commands provided by applications
            Default options
            Extra niceties
        Running management commands from your code
            Output redirection
        Django Exceptions
            Django Core Exceptions
            URL Resolver exceptions
            Database Exceptions
            HTTP Exceptions
            Sessions Exceptions
            Transaction Exceptions
            Testing Framework Exceptions
            Python Exceptions
        File handling
            The File object
            File storage API
            Uploaded Files and Upload Handlers
        Forms
            The Forms API
            Form fields
            Model Form Functions
            Formset Functions
            The form rendering API
            Widgets
            Form and field validation
        Logging
            Django’s default logging configuration
            Django logging extensions
        Middleware
            Available middleware
            Middleware ordering
        Migration Operations
            Schema Operations
            Special Operations
            Writing your own
        Models
            Model field reference
            Field attribute reference
            Model index reference
            Constraints reference
            Model _meta API
            Related objects reference
            Model class reference
            Model Meta options
            Model instance reference
            QuerySet API reference
            Lookup API reference
            Query Expressions
            Conditional Expressions
            Database Functions
        Paginator
            Paginator class
            Page class
            Exceptions
        Request and response objects
            Quick overview
            HttpRequest objects
            QueryDict objects
            HttpResponse objects
            JsonResponse objects
            StreamingHttpResponse objects
            FileResponse objects
            HttpResponseBase class
        SchemaEditor
            Methods
            Attributes
        Settings
            Core Settings
            Auth
            Messages
            Sessions
            Sites
            Static Files
            Core Settings Topical Index
        Signals
            Model signals
            Management signals
            Request/response signals
            Test signals
            Database Wrappers
        Templates
            The Django template language
            Built-in template tags and filters
            The Django template language: for Python programmers
        TemplateResponse and SimpleTemplateResponse
            SimpleTemplateResponse objects
            TemplateResponse objects
            The rendering process
            Using TemplateResponse and SimpleTemplateResponse
        Unicode data
            Creating the database
            General string handling
            Models
            Templates
            Files
            Form submission
        django.urls utility functions
            reverse()
            reverse_lazy()
            resolve()
            get_script_prefix()
        django.urls functions for use in URLconfs
            path()
            re_path()
            include()
            register_converter()
        django.conf.urls functions for use in URLconfs
            static()
            handler400
            handler403
            handler404
            handler500
        Django Utils
            django.utils.cache
            django.utils.dateparse
            django.utils.decorators
            django.utils.encoding
            django.utils.feedgenerator
            django.utils.functional
            django.utils.html
            django.utils.http
            django.utils.module_loading
            django.utils.safestring
            django.utils.text
            django.utils.timezone
            django.utils.translation
        Validators
            Writing validators
            How validators are run
            Built-in validators
        Built-in Views
            Serving files in development
            Error views
    Meta-documentation and miscellany
        API stability
            What “stable” means
            Stable APIs
            Exceptions
        Design philosophies
            Overall
            Models
            Database API
            URL design
            Template system
            Views
            Cache Framework
        Third-party distributions of Django
            For distributors
    Glossary
    Release notes
        Final releases
            4.2 release
            4.1 release
            4.0 release
            3.2 release
            3.1 release
            3.0 release
            2.2 release
            2.1 release
            2.0 release
            1.11 release
            1.10 release
            1.9 release
            1.8 release
            1.7 release
            1.6 release
            1.5 release
            1.4 release
            1.3 release
            1.2 release
            1.1 release
            1.0 release
            Pre-1.0 releases
        Security releases
    Django internals
        Contributing to Django
            Work on the Django framework
            Join the Django community ❤️
        Mailing lists and Forum
            Django Forum
            django-users
            django-developers
            django-announce
            django-updates
        Organization of the Django Project
            Principles
            Mergers
            Releasers
            Steering council
            Changing the organization
        Django’s security policies
            Reporting security issues
            Supported versions
            How Django discloses security issues
            Who receives advance notification
            Requesting notifications
        Django’s release process
            Official releases
            Release cadence
            Deprecation policy
            Supported versions
            Release process
        Django Deprecation Timeline
            5.1
            5.0
            4.1
            4.0
            3.1
            3.0
            2.1
            2.0
            1.10
            1.9
            1.8
            1.7
            1.6
            1.5
            1.4
            1.3
        The Django source code repository
            High-level overview
            The main branch
            Stable branches
            Tags
        How is Django Formed?
            Overview
            Prerequisites
            Pre-release tasks
            Preparing for release
            Actually rolling the release
            Making the release(s) available to the public
            Post-release
            New stable branch tasks
            Notes on setting the VERSION tuple

