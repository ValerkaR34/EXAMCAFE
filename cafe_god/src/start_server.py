from  fastapi import  FastAPI
import uvicorn


from  server.routees import routersval

from fastapi.responses import RedirectResponse


app = FastAPI(title="Valerka-ezxem")

# [app.include_router(routees) for routees in routersval]


for router in routersval:
    app.include_router(router)




@app.get('/')
def root():
    return RedirectResponse('/docs')





if __name__ == '__main__':
    uvicorn.run(app="start_server:app", host="0.0.0.0", port=8000, reload=True)

