django-bcs-proxy
================

> proxy for baidu cloud service with django


Install
-------

```Bash
$ pip install django-bcs-proxy
```

Usage
-----

```Python
# in urls.py
import django_bcs_proxy

urlpatterns += (
	#...
	(r'URL', django_bcs_proxy(AK, SK, HOST)),
	#...
)
```

