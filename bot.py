from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State,StatesGroup
from aiogram import Bot,executor,Dispatcher,types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from my_buttons import menu,admins_menu,zat_qosiw_menu,qoriw,reg_buttons, reg
from datas import start_db,add_to_db,show_foods,add_to_user_db, start_user_db



api = '7860150473:AAG9b8DT9F3VtLSDPxJ5C8HDW2nLrEe7V3w'
bot = Bot(api)
storage = MemoryStorage()
dp = Dispatcher(bot=bot,storage=storage)


class FoodState(StatesGroup):
    type_of_food = State()
    price = State()
    name = State()
    photo = State()
    ingridients = State()
class Regstate(StatesGroup):
    name = State()
    phone_num = State()
    id = State()



admin_id = 1305835810
@dp.message_handler(commands=['start'])
async def send_hi(sms:types.Message):
    
    if admin_id==sms.from_user.id:

        await sms.answer(text='Salem Admin',
                         reply_markup=admins_menu)
    else:

        await sms.answer(text='Assalamu aleykum registratsia qilim',
                         reply_markup=reg)
        

        

@dp.message_handler(text='Zat qosiw')
async def start_adding(sms:types.Message):
    if admin_id==sms.from_user.id:
        await start_db()
        await sms.answer(text='Qanday awqat',reply_markup=zat_qosiw_menu)
        await FoodState.type_of_food.set()

@dp.message_handler(state=FoodState.type_of_food)
async def start(sms:types.Message,state:FSMContext):
    if admin_id==sms.from_user.id:
        async with state.proxy() as food:
            food['type_of_food'] = sms.text
        await sms.answer(text='Neshe min')
        await FoodState.price.set()
@dp.message_handler(state=FoodState.price)
async def price(sms:types.Message,state:FSMContext):
    async with state.proxy() as food:
        food['price']=sms.text
    await sms.answer("Ati qanday")
    await FoodState.name.set()
@dp.message_handler(state=FoodState.name)
async def name(sms:types.Message,state:FSMContext):
    async with state.proxy() as food:
        food['name']=sms.text
    await sms.answer('Ingredient qanday')
    await FoodState.ingridients.set()

@dp.message_handler(state=FoodState.ingridients)
async def ingridients(sms:types.Message,state:FSMContext):
    async with state.proxy() as food:
        food['ingridients']=sms.text
    await sms.answer('photo')
    await FoodState.photo.set()
 
@dp.message_handler(state=FoodState.photo,content_types="photo")
async def photo(sms:types.Message,state:FSMContext):
    async with state.proxy() as food:

        food['photo']=sms.photo[0]['file_id']
    await sms.answer_photo(caption=f"Tagam Turi:{ food['type_of_food']}\nTagam Sena:{food['price']}\nAti : {food['name']}\n Ingredientlar : {food['ingridients']}",photo=food['photo'],reply_markup=admins_menu)
    await add_to_db(type=food['type_of_food'],price=food['price'],name=food['name'],
          photo=food['photo'],
          ingri=food['ingridients'])
    await state.finish()

@dp.message_handler(text='Menu')
async def show_all_foods(sms:types.Message):
    await sms.answer('qoriw awqat',reply_markup=qoriw)


@dp.message_handler(text='Fast food qoriw')
async def show_all_foods(sms:types.Message):
    datas = await show_foods()
    for data in datas:
        if data[0] == 'Fast food':
            await sms.answer_photo(caption=f'''
                type_of_food: {data[0]}
                price: {data[1]}
                name: {data[2]}
                ingridients": {data[4]}
''', photo=data[3])

@dp.message_handler(text='Hot food qoriw')
async def show_all_foods(sms:types.Message):
    datas = await show_foods()
    for data in datas:
        if data[0] == 'Hot food':
            await sms.answer_photo(caption=f'''
                type_of_food: {data[0]}
                price: {data[1]}
                name: {data[2]}
                ingridients": {data[4]}
''', photo=data[3])

@dp.message_handler(text='Drinks qoriw')
async def show_all_foods(sms:types.Message):
    datas = await show_foods()
    for data in datas:
        if data[0] == 'Drinks':
            await sms.answer_photo(caption=f'''
                type_of_food: {data[0]}
                price: {data[1]}
                name: {data[2]}
                ingridients": {data[4]}
''', photo=data[3])
            

@dp.message_handler(text='Registration')
async def registration(sms:types.Message):
    await sms.answer('Registration form', reply_markup=reg_buttons)

@dp.message_handler(text='start form')
async def start_user_adding(sms:types.Message):
    await start_user_db()
    await sms.answer("Atin kim")
    await Regstate.name.set()

@dp.message_handler(state=Regstate.name)
async def phone_number(sms: types.Message, state: FSMContext):
    async with state.proxy() as user:
        user['name'] = sms.text
    await sms.answer("Nomer jaz")
    await Regstate.phone_num.set()

@dp.message_handler(state=Regstate.phone_num)
async def aidi_num(sms:types.Message, state: FSMContext):
    async with state.proxy() as user:
        user['phone_num'] = sms.text
    await sms.answer('aidi jaz')
    await Regstate.id.set()

@dp.message_handler(state=Regstate.id)
async def finish_user_form(sms:types.Message, state: FSMContext):
    async with state.proxy() as user:
        user['id'] = sms.text
        
        if user['name'] is None or user['phone_num'] is None:
            await sms.answer("Вы не заполнили форму")
        await sms.answer(text=f'''
            ati: {user['name']},
            telefon: {user['phone_num']},
            id: {user['id']}
    ''')
        await add_to_user_db(name=user['name'],phone_num=user['phone_num'],id=user['id'])
        
    await state.finish()
    
if __name__=='__main__':
    executor.start_polling(dp,skip_updates=True)
