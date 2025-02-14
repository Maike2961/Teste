import asyncio
import time


async def chamadas(delay, name):
    print(f"Iniciando {name}")
    await asyncio.sleep(delay)
    
async def main():
    start = time.time()
    
    await chamadas(1, "Hello")
    await chamadas(2, "Hello World")
    await chamadas(3, "Hello Brave World")
    
    total = time.time() - start
    
    print(f"Tempo de execução {total:.2f}")

asyncio.run(main())
    
    
    