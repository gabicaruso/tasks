from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")

@api_view(["GET"])
def get_tasks(request):
    all_tasks = Task.objects.all()
    tasks_json = serializers.serialize("json", all_tasks)
    return HttpResponse(tasks_json ,content_type="application/json")

@api_view(["POST"])
def add_task(request):
    dataJson = JSONParser().parse(request)
    serializer = TaskSerializer(data=dataJson)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

@api_view(["DELETE"])
def del_tasks(request):
    Task.objects.all().delete()
    return Response({"message": "All tasks deleted!"})
