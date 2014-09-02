import sys


def proxy(ak, sk, bucket_name, host='bcs.duapp.com'):

	from django.views.decorators.http import require_POST

	from pybcs.bcs import BCS
	from pybcs.bucket import Bucket
	from django_render_json import render_json

	CODE_NO_FILES = 3001
	CODE_FAILED = 3002
	CODE_OK = 0

	bcs = BCS(host, ak, sk)
	bucket = (bcs, bucket_name)
	
	def view(request):
		if len(request.FILES.keys()) == 0:
			return render_json({'ret_code': CODE_NO_FILES})
		
		uploadedFile = request.FILES[request.FILES.keys()[0]]
		if 'temporary_file_path' in dir(uploadedFile):
			result = bucket.post_file(uploadedFile.temporary_file_path())
		else:
			result = bucket.put(uploadFile.read())
		
		return render_json({'ret_code': CODE_OK \
			if result['status'] == 200 else CODE_FAILED})

	return view


sys.modules[__name__] = proxy

