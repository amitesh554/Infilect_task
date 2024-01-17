from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import sessionmaker,Session
from typing import List
from pydantic import BaseModel

from datab import get_db,RequestLog,ResponseLog


app = FastAPI()


def largest_rectangle(matrix: List[List[int]]) -> tuple:
    if not matrix or not matrix[0]:
        raise ValueError("Invalid matrix")

    rows, cols = len(matrix), len(matrix[0])
    max_area = 0
    max_number = None

    for top in range(rows):
        height = [0] * cols
        for bottom in range(top, rows):
            for col in range(cols):
                if matrix[bottom][col] == matrix[top][col]:
                    height[col] += 1
                else:
                    height[col] = 0

            stack = [-1]
            for col in range(cols + 1):
                while stack[-1] != -1 and (col == cols or height[col] < height[stack[-1]]):
                    h = height[stack.pop()]
                    w = col - stack[-1] - 1 if stack else col
                    if h * w > max_area:
                        max_area = h * w
                        max_number = matrix[top][col - 1]

                stack.append(col)

    return max_number, max_area




class MatrixInput(BaseModel):
    matrix: List[List[int]]

class MatrixResponse(BaseModel):
    number: int
    area: int

def log_request(matrix_input: MatrixInput, db: Session = Depends(get_db)):
    matrix_str = str(matrix_input.matrix)
    request_log = RequestLog(matrix=matrix_str)
    db.add(request_log)
    db.commit()


def log_response(response: MatrixResponse, db: Session = Depends(get_db)):
    response_log = ResponseLog(number=response.number, area=response.area)
    db.add(response_log)
    db.commit()

@app.post("/largest_rectangle", response_model=MatrixResponse)
def find_largest_rectangle(matrix_input: MatrixInput, db: Session = Depends(get_db)):
    try:
        log_request(matrix_input, db)
        result = largest_rectangle(matrix_input.matrix)
        log_response(MatrixResponse(number=result[0], area=result[1]), db)
        return {"number": result[0], "area": result[1]}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
