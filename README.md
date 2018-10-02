# aee-saleor
Forked from https://github.com/mirumee/saleor and modified as needed

Original readme file from fork available at [[README-upstream.md]]

Moved to saleor from django-oscar after oscar's open issues
- [ Price won't update when selecting variants. #2139 ](https://github.com/django-oscar/django-oscar/issues/2139)
- [ Better variant product support #675 ](https://github.com/django-oscar/django-oscar/issues/675)
  - opened in 2013, and still open in 2018
  - [ ace-han comment on Jun 19](https://github.com/django-oscar/django-oscar/issues/675#issuecomment-398478730) pointed me in saleor's direction
  - sign of a bit of technical debt?

Fork was from master branch around commit ae91ff4 (i.e. after tag `v2018.08`)


## Installation

1. follow installation instructions in [[README-upstream.md]]

2. `cp manage.sh.dist manage.sh` and modify as needed

3. replace all usage of `./manage.py ...` with `./manage.sh ...`


## Changelog

Check [[CHANGELOG.md]]


## User management

One of the things that I changed in saleor in this fork is that
only a registered and logged in staff user can register another
staff user.

The initial one can be created with django's `createsuperuser` command.

The rest can be done via the `register` link at the top of the 
storefront (near `log out`)
