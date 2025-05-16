import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from openai import OpenAI
from .env_loader import base_url, api_key, model

# Create your views here.
def speech_to_text(request):
    if api_key is None:
        return render(request, 'error.html')
    return render(request, 'chatandtalk.html')

@csrf_exempt
def speaker(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_text = data.get("text", "")

            openai_payload = {api_key=api_key}
            if base_url is not None:
                openai_payload['base_url'] = base_url
            client = OpenAI(**openai_payload)

            chat_completion = client.chat.completions.create(
                model=model,
                messages=[
                    {
                        "role": "user",
                        "content": user_text,
                    }
                ],
                max_tokens=1000,
                temperature=0.7,
            )
            response_text = chat_completion.choices[0].message.content
            
            return JsonResponse({"response": response_text})
        except Exception as e:
            print(e)
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Invalid request method"}, status=405)
