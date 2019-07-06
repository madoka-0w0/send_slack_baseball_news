from baseball_news_picker import baseball_news_picker, baseball_news_factory

from baseball_news_send_slack.model.user import BaseballNewsUser
from baseball_news_send_slack.slack_message import SlackBaseballMessage
from slack_sender.application.slack_message_creator import SlackMessageCreator


class BaseballNewsCreator(SlackMessageCreator):
    def __init__(self):
        pass

    def create(cls, user: BaseballNewsUser) -> SlackBaseballMessage:
        picker = baseball_news_picker.BaseballNewsPicker(user.team)
        factory = baseball_news_factory.BaseballNewsFactory(user.team, picker)
        news = factory.create_news()

        text = ""
        if news.have_game():
            text += "{} {} - {} {}".format(news.my_team, news.my_team_point, news.battle_team_point, news.battle_team)
            text += news.news_text
        message = SlackBaseballMessage(text)
        message.status = news.status
        return message
