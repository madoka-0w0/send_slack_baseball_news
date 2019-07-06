from slack_sender.infrastructure.repository.user_repository import UserRepository

from baseball_news_send_slack.model.user import BaseballNewsUser


class BaseballUserRepository(UserRepository):
    def get_users(self):
        users = super(BaseballUserRepository, self).get_users()
        return [BaseballNewsUser(user._item) for user in users]

    def get_user(self, user_id: int):
        user = super(BaseballUserRepository, self).get_user(user_id)
        return BaseballNewsUser(user._item)
