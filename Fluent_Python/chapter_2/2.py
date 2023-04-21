import asyncio
import multiprocessing as mp
import time

queue = mp.Queue()


def difficult_process(data: mp.Queue):
    time.sleep(5)
    data.put(1)


async def main_process(data: mp.Queue):
    flag = True
    print(f'Привет дружище, мы тебе напишем когда обработка закончится')
    while flag:
        if data.empty():
            await asyncio.sleep(1)
            print('бззз, комп нагружен, жизнь боль')
        else:
            print('Всё выполнено!')
            flag = False


async def main(data: mp.Queue):
    task = [
        main_process(data)
    ]
    await asyncio.gather(*task)


if __name__ == '__main__':
    second_process = mp.Process(target=difficult_process, args=(queue,))
    second_process.start()
    asyncio.run(main(queue))
    second_process.join()
