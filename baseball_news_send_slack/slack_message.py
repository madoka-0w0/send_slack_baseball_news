from baseball_news_picker.model.game_status import GameStatus

from slack_sender.application.model.slack_message import SlackMessage


class SlackBaseballMessage(SlackMessage):
    def __init__(self, message):
        super(SlackBaseballMessage, self).__init__(message)
        self.status = GameStatus.BEFORE
