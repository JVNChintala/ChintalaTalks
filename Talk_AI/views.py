import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from openai import OpenAI

# Create your views here.
def speech_to_text(request):
    return render(request, 'chatandtalk.html')

@csrf_exempt
def speaker(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_text = data.get("text", "")
            client = OpenAI(
                api_key="Put Your API Key here",
                base_url="Put your organization url or Open AI url",
            )

            chat_completion = client.chat.completions.create(
                model="UCCIX-v2-Llama3.1-70B-Instruct",
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
