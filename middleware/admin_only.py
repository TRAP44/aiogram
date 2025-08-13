from aiogram import BaseMiddleware

ADMINS = [1813351866]

class AdminOnlyMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        if event.from_user.id not in ADMINS:
            await event.answer("У вас нет прав доступа")
            return
        return await handler(event, data)
    