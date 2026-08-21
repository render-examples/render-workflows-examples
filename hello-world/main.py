from render import TaskContext, Workflows, Retry
import asyncio
import random

app = Workflows()


@app.task
def calculate_square(ctx: TaskContext, a: int) -> int:
    return a * a


@app.task
async def sum_squares(ctx: TaskContext, a: int, b: int) -> int:
    # ctx.run runs a task on its own compute and returns its result
    result1, result2 = await asyncio.gather(
        ctx.run(calculate_square, a),
        ctx.run(calculate_square, b),
    )
    return result1 + result2


@app.task(
    retry=Retry(
        max_retries=3,
        wait_duration_ms=1000,
        backoff_scaling=1.5,
    )
)
def flip_coin(ctx: TaskContext) -> str:
    if random.random() < 0.5:
        raise Exception("Flipped tails! Retrying.")
    return "Flipped heads!"


if __name__ == "__main__":
    app.start()
