from datetime import datetime, timedelta

from injector import inject
from slack_sender.application.service.system_runner import SystemRunner
from slack_sender.application.service.users_runner import UsersRunner
from slack_sender.infrastructure.repository.system_repository import SystemRepository
from slack_sender.infrastructure.repository.user_repository import UserRepository


class BaseballSystemRunner(SystemRunner):
    @inject
    def __init__(self, sys_repo: SystemRepository, user_repo: UserRepository, users_runner: UsersRunner):
        super(BaseballSystemRunner, self).__init__(sys_repo, users_runner)
        self.user_repo = user_repo

    def before_action(self):
        if self.has_changed_day():
            for user in self.user_repo.get_users():
                self.user_repo.update_need_send_slack(user.id, True)

    def has_changed_day(self):
        sys = self.system_table.get()
        before = sys.last_startup.replace(hour=0, minute=0, second=0, microsecond=0)
        now = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

        return (now - before) >= timedelta(days=1)
