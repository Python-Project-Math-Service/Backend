import asyncio
from app.services import calculator

math_task_queue = asyncio.Queue()


async def process_math_tasks():
    while True:
        task = await math_task_queue.get()
        task_type, data, result_future = task

        try:
            if task_type == "factorial":
                result = calculator.calculate_factorial(data["number"])
            elif task_type == "fibonacci":
                result = calculator.calculate_fibonacci(data["index"])
            else:
                raise ValueError("Unknown task type")

            result_future.set_result(result)
        except Exception as e:
            result_future.set_exception(e)

        math_task_queue.task_done()
