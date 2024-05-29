from django.http import HttpRequest, JsonResponse
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from celery.result import AsyncResult

from tasks.sample_tasks import create_task


def home(request: HttpRequest) -> HttpResponse:
    return render(request, "home.html")


@csrf_exempt
def run_task(request: HttpRequest) -> JsonResponse:
    if request.method == "POST":
        print()
        print(request.POST)
        print()
        task_type = request.POST.get("type")
        task = create_task.delay(int(task_type))
        return JsonResponse({"task_id": task.id}, status=202)
    return JsonResponse({"error": "invalid request"}, status=400)


@csrf_exempt
def get_status(request: HttpRequest, task_id) -> JsonResponse:
    task_result = AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result
    }
    return JsonResponse(result, status=200)
