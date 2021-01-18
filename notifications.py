from pyfcm import FCMNotification


class Notifications:
    def __init__(self, api_key: str):
        self.push_service = FCMNotification(api_key=api_key)

    def notify(self, registration_ids: list, message_title: str, message_body: str, data_message: dict) -> dict:
        result = self.push_service.notify_multiple_devices(registration_ids=registration_ids,
                                                           message_title=message_title,
                                                           message_body=message_body,
                                                           data_message=data_message)
        return result
