from slack_sender.infrastructure.model.user import User


class BaseballNewsUser(User):
    STATUS_NAME = "status"
    TEAM_NAME = "team"

    @property
    def status(self):
        return self._item.get(BaseballNewsUser.STATUS_NAME)

    @property
    def team(self):
        return self._item[BaseballNewsUser.TEAM_NAME]
