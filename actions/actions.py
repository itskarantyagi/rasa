# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


#
#
class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_speak"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        for blob in tracker.latest_message['entities']:
            print(tracker.latest_message)
            if blob['entity'] == "user_name":
                name = blob["value"]
                dispatcher.utter_message(text=f"Hello {name}, how can I help you today?")

        return []


class ActionReserveId(Action):
    def name(self) -> Text:
        return "action_reserve_id"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        for blob in tracker.latest_message['entities']:
            if blob['entity'] == "reservation_id":
                reservation_id = blob["value"]
                dispatcher.utter_message(text=f"reservation id is: {reservation_id}")

        return []
