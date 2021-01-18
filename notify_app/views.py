from json import load

from django.shortcuts import render


from .forms import NotifyForm
from notifications import Notifications

with open('data.json') as f:
    api_key = load(f)['api_key']

notifications = Notifications(api_key)


def notify_new(request):
    sent = False
    if request.method == 'POST':
        form = NotifyForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            sent = True
            tokens_devices = cd['tokens_devices'].replace(' ', '').split(',')
            title = cd['title']
            message = cd['message']
            payload_title = cd['payload_title']
            payload_body = cd['payload_body']
            payload = {'payload_title': payload_title, 'payload_body': payload_body}
            if not payload_body or not payload_title:
                payload = None
            result = notifications.notify(tokens_devices, title, message, payload)
            cd['result'] = f'Done! Success: {result["success"]} | Failure: {result["failure"]}'
            form = NotifyForm()
            return render(request, 'notify_app/send_notify.html', {'form': form, 'sent': sent,
                                                                   'cd': cd, 'alert_flag': True})
    else:
        form = NotifyForm()
    return render(request, 'notify_app/send_notify.html', {'form': form, 'sent': sent})
