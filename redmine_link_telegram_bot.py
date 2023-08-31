import re
import telebot
import logging
from redminelib import Redmine
from redminelib.exceptions import ForbiddenError
import settings

redmine_issue_regex = re.compile('(%s/issues/([0-9]+))' % settings.REDMINE_URL.replace('/', '\\/').replace('.', '\\.'), re.IGNORECASE | re.MULTILINE)

redmine = None
bot = None

def extract_issue_urls(message):
    links = redmine_issue_regex.findall(message)
    ids = []
    for link in links:
        ids.append(link)
    return links


def compose_message(issue_urls):
    message = ''
    for issue_url in issue_urls:
        try:
            issue = redmine.issue.get(issue_url[1])
            message += '[%s](%s) - %s\n' % (issue_url[1], issue_url[0], issue.subject)
        except ForbiddenError:
            message += 'Sorry, task "%s" is either forbidden to me or not found at all.' % issue_url[1] 
    return message


def handle_messages(messages):
    for message in messages:
        handle_message(message)


def handle_message(message):
    issue_urls = extract_issue_urls(message.text)
    if not issue_urls:
        return
    reply_text = compose_message(issue_urls)
    if not reply_text:
        return
    bot.send_message(chat_id=message.chat.id, text=reply_text, parse_mode="MARKDOWN")


if __name__ == '__main__':
    redmine = Redmine(settings.REDMINE_URL, username=settings.REDMINE_USER, password=settings.REDMINE_PASSWORD)
    telebot.apihelper.SESSION_TIME_TO_LIVE = 5 * 60
    bot = telebot.TeleBot(settings.TELEGRAM_BOT_TOKEN)
    telebot.logger.setLevel(logging.INFO)
    print('Started.')
    print(bot.get_me())
    print('Polling...')
    bot.set_update_listener(handle_messages)
    bot.infinity_polling()
