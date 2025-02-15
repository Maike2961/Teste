import asyncio
import time

""" função assincrona que tem como parametros a duração dentre as chamadas e o nome  """
async def chamadas(delay, name):
    print(f"Iniciando {name}")
    
    """ enquando a duração não estiver completa não prosseguira para a proxima chamada  """
    await asyncio.sleep(delay)
    
""" função principal que chamará a função chamadas tres vezes """
async def main():
    start = time.time()
    
    """ enquando a chamada não estiver completa, a outra ficara em espera de forma sequencial """
    await chamadas(1, "Hello")
    await chamadas(2, "Hello World")
    await chamadas(3, "Hello Brave World")
    
    """ calculando o tempo que todoas as funções levaram para concluir """
    total = time.time() - start
    
    print(f"Tempo de execução {total:.2f}")

""" executando a função main """
asyncio.run(main())
    
    
    