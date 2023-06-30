from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from database.crud import create_task, get_tasks
from database.models import Task, SchemaTask

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Вас приветствует TODO-bot!\nДля получения справки используйте команду /help')


@router.message(F.text == '/help')
async def cmd_help(message: Message):
    await message.answer('<b>Доступные команды:</b>\n\n'
                         '/add [текст задачи] - добавление задачи\n'
                         '/done [индекс задачи] - отметить задачу выполненной\n'
                         '/list - показать все\n'
                         '/delete [индекс задачи] удалить по индексу\n')


# ########################################## #
# ################ TASK #################### #
# ########################################## #


@router.message(F.text.startswith('/add '))
async def add_task(message: Message):
    task_text = message.text.split('/add')[-1]
    create_task(task_text, message.from_user.id)
    await message.answer('Задача добавлена')


@router.message(F.text.startswith('/done'))
async def done_task(message: Message):
    await message.answer('Задача отмечена выполненной')


@router.message(F.text == '/list')
async def list_tasks(message: Message):
    tasks = get_tasks()
    for task in tasks:
        delete_button = InlineKeyboardButton(text='Удалить ❌', callback_data=f'delete_task {task.id}')
        delete_task_kb = InlineKeyboardMarkup(inline_keyboard=[[delete_button]])
        await message.answer(f'ID: {task.id}\n'
                             f'TITLE: {task.title}\n'
                             f'DESCRIPTION: {task.description}\n'
                             f'STATUS: {task.status}',
                             reply_markup=delete_task_kb)


@router.callback_query(F.data.startswith('delete_task'))
async def delete_task_button_press(callback: CallbackQuery):
    task_id = callback.data.split(' ')[-1]
    print(task_id)
    await callback.message.answer(callback.message.text)


@router.message(F.text.startswith('/delete'))
async def delete_task(message: Message):
    await message.answer('Задача удалена')


# ################ END #########################
@router.message(F.text == '/add')
async def incorrect_add(message: Message):
    await message.answer('<b> ERROR </b>\n'
                         'Эта команда требует данные для обработки')


@router.message()
async def i_dont_know(message: Message):
    await message.answer('<b>Такой команды пока нет =(</b>')
