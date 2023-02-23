import asyncio    
from aiohttp import ClientSession    
 
cookies = {"arg1" : "test"}
params = {"param1" : "item1"}
 
async def DoURLGet(url) :    
    async with ClientSession() as session:    
        async with session.get(url, params = params, cookies = cookies) as res:    
            content = await res.read()        
            print(res.url)
            print(content)
            
async def DoURLPost(url, data) :    
    async with ClientSession() as session:    
        async with session.post(url, data=data, params = params, cookies = cookies) as res:    
            content = await res.read()    
            print(res.url)
            print(content)
    
    
loop = asyncio.get_event_loop()                                                 
JOBS = []                                        
url = 'http://182.227.191.199:1337/all?{0}' 

for i in range(5):                                                  
    job = asyncio.ensure_future(DoURLGet(url.format(i)))                                                                   
    JOBS.append(job)                                                                                                    
    loop.run_until_complete(asyncio.wait(JOBS))
           
for i in range(5):                                                  
    job = asyncio.ensure_future(DoURLPost('http://182.227.191.199:1337/all', str(i)))                                                                   
    JOBS.append(job)                                                                                                    
    loop.run_until_complete(asyncio.wait(JOBS))
    
    
#DeprecationWarning: There is no current event loop