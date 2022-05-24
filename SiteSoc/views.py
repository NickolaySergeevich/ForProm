import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from SiteSoc.forms import ChatForm
from SiteSoc.models import ChatHistory


def get_standard_context():
    return {
        "menu_data": [
            {"link": "/login", "text": "Авторизация"},
            {"link": "/logout", "text": "Выход из системы"},
            {"link": "/", "text": "Главная"},
            {"link": "/chat", "text": "Чат"}
        ]
    }


def main_page(request):
    context = get_standard_context()
    context.update(
        **{
            "username": request.user
        }
    )

    return render(request, "main_page.html", context)


@login_required
def chat_page(request):
    context = get_standard_context()

    if request.method == "POST":
        form = ChatForm(request.POST)
        message_text = form.data["message_text"]

        item = ChatHistory(
            message=message_text,
            username=request.user,
            date=datetime.datetime.now()
        )
        item.save()

        context.update(
            **{
                "form": form,
                "chat_data": ChatHistory.objects.all()
            }
        )
    else:
        context.update(
            **{
                "form": ChatForm(),
                "chat_data": ChatHistory.objects.all()
            }
        )

    return render(request, "chat_page.html", context)
