from typing import List

class EndorsementsValidator():
    @staticmethod
    def validate(channel_id: str, endorsements: List[str]):
        # If the Activity came in and doesn't have a Channel ID then it's making no 
        # assertions as to who endorses it. This means it should pass. 
        if not channel_id:
            return True

        if endorsements is None:
            raise ValueError('Argument endorsements is null.')

        return channel_id in endorsements
