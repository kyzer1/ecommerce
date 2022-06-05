from bucket import bucket
from celery import shared_task


# TODO: can be async?
def all_bucket_objects_tasks():
    result = bucket.get_objects()
    return result


@shared_task
def delete_object_task(Key):
    bucket.delete_object(Key)


@shared_task
def download_oject_task(Key):
    bucket.download_object(Key)