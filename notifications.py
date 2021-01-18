from pyfcm import FCMNotification


class Notifications:
    def __init__(self, api_key: str):
        self.push_service = FCMNotification(api_key=api_key)

    def notify(self, registration_ids: list, data_message: dict) -> dict:
        result = self.push_service.notify_multiple_devices(registration_ids=registration_ids,
                                                           data_message=data_message)
        return result
