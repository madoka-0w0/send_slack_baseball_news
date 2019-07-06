from baseball_news_picker.model.game_status import GameStatus

from baseball_news_send_slack.model.user import BaseballNewsUser
from baseball_news_send_slack.slack_message import SlackBaseballMessage
from slack_sender.application.service.user_runner import UserRunner


class BaseballUserRunner(UserRunner):
    def need_send_slack(self, user: BaseballNewsUser, message: SlackBaseballMessage):
        status = user.status
        if status == GameStatus.RESULT or self.no_game(status) or message.is_empty():
            return False
        return user.need_send_slack and message.status == GameStatus.RESULT

    def change_need_send_slack_status(self, user: BaseballNewsUser, message: SlackBaseballMessage):
        if self.no_game(message.status) or message.status == GameStatus.RESULT:
            if user.need_send_slack:
                self.user_repo.update_need_send_slack(user.id, False)

    @staticmethod
    def no_game(status):
        return status == GameStatus.CALLED_OFF or status == GameStatus.NO_GAME
