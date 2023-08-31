# Redmine-link Telegram bot
Простейший бот, чтобы постить в конференцию название задачи по ссылке на неё.
# Зачем
Потому что публичный доступ в *Redmine* может быть ограничен, соответственно для её урлов превью не генерится.
# Зависимости

- See *requirements.txt* for the list of dependencies.

# Запуск
1. Завести в *Telegram* через *BotFather* бота с отключенными настройками приватности.
2. Перед запуском бота в переменные окружения добавить:
    ```
    export REDMINE_URL="Урл Redmine, без / в конце"
    export REDMINE_USER="логин пользователя Redmine"
    export REDMINE_PASSWORD="пароль пользователя Redmine"
    export TELEGRAM_BOT_TOKEN="токен бота"
    ```

3. `python3 redmine_link_telegram_bot.py`
4. Добавить бота в конференцию.
5. Сделать его админом (так он сможет слушать сообщения в конференции).


