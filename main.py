import os

from injector import Injector, Module, singleton
from slack_sender.application.service.slack_sender import SlackSender
from slack_sender.application.service.user_runner import UserRunner
from slack_sender.application.slack_message_creator import SlackMessageCreator
from slack_sender.infrastructure.configuration import Configuration
from slack_sender.infrastructure.repository.user_repository import UserRepository

from baseball_news_send_slack.slack_message_creator import BaseballNewsCreator
from baseball_news_send_slack.system_runner import SystemRunner, BaseballSystemRunner
from baseball_news_send_slack.user_repository import BaseballUserRepository
from baseball_news_send_slack.user_runner import BaseballUserRunner


class BaseballInjectModule(Module):
    def configure(self, binder):
        binder.bind(SystemRunner, to=BaseballSystemRunner)
        binder.bind(UserRunner, to=BaseballUserRunner)
        binder.bind(SlackMessageCreator, to=BaseballNewsCreator)
        binder.bind(UserRepository, to=BaseballUserRepository)
        binder.bind(SlackSender, to=SlackSender(), scope=singleton)
        user_table_name = os.environ["USER_TABLE"]
        system_table_name = os.environ["SYSTEM_TABLE"]
        system_id = os.environ["SYSTEM_ID"]
        binder.bind(Configuration,
                    to=Configuration(system_table_name, user_table_name, int(system_id), "%Y%m%d %H%M%S"),
                    scope=singleton)


def handler(event, context):
    injector = Injector([BaseballInjectModule()])
    sysrunner = injector.get(SystemRunner)
    sysrunner.run()


if __name__ == '__main__':
    handler(None, None)
