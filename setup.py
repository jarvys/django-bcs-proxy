from distutils.core import setup	

setup(
	name='django-bcs-proxy',
	version='0.0.1',
	description='proxy for bcs with django',
	author='yangchen',
	author_email='yuhan534@126.com',
	url='https://github.com/jarvys/django-bcs-proxy',
	install_requires=[
		'django-upload-path-generator',
		'django-render-json',
		'Django',
		'pybcs'
	],
	py_modules=['django_bcs_proxy'],
	scripts=[],
	keywords=[
		'baidu',
		'cloud',
		'service',
		'proxy',
		'django',
		'utilities'
	]
)

