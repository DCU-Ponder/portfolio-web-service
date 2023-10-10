from src.write import add, update
from src.read import info
from src import delete

from fastapi import FastAPI

api = FastAPI()


@api.get("/")
async def userInfo(nickname:str = None):
    """
    info:
        해당 함수는 URL에서 Nickname이라는 변수에서 받은 데이터를 불러와 닉네임에있는 정보 Read해주는 함수입니다.

        해당 함수에서 필요한 변수는 아래와 같습니다.
    
    age:
        nickname: 사용자 닉네임
    """

    # 해당 함수에 있는 내용은 전부 예시입니다.
    return {"어?": "에프다."}

@api.post("/")
async def userAdd(nickname:str = None):
    """
    info:
        해당 함수는 URL에서 Nickname이라는 변수에서 받은 데이터를 사용자 이름으로 지정하고 JSON으로 받은 데이터대로 사용자 정보를 저장해주는 해주는 함수입니다.

        해당 함수에서 필요한 변수는 아래와 같습니다.
    
    age:
        nickname: 사용자 닉네임
    """

    # 해당 함수에 있는 내용은 전부 예시입니다.
    return {"어?": "에프다."}

@api.put("/")
async def userUpdate(nickname:str = None):
    """
    info:
        해당 함수는 JSON으로 데이터를 받아 사용자의 데이터를 수정하는 함수입니다.

        해당 함수에서 필요한 변수는 아래와 같습니다.
    
    age:
        nickname: 사용자 닉네임
    """

    # 해당 함수에 있는 내용은 전부 예시입니다.
    return {"어?": "에프다."}

@api.delete("/")
async def userRemove(nickname:str = None):
    """
    info:
        해당 함수는 사용자에 대한 정보를 제거하는 함수입니다.

        해당 함수에서 필요한 변수는 아래와 같습니다.
    
    age:
        nickname: 사용자 닉네임
    """

    # 해당 함수에 있는 내용은 전부 예시입니다.
    return {"어?": "에프다."}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(api, host="0.0.0.0", port=8080)