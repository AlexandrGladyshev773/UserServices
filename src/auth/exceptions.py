from fastapi import HTTPException, status



UserAlreadyExistsException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Пользователь уже существует",
)

IncorrectEmailOrPasswordExeption = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Неверная почта или пароль",
    )


ExpiredTokenExeption = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Токеи истек",
    )

TokenExistFaliedException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Токеи отсутствует",
    )

IncorrectTokenFormatException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Неверный формат токена",
    )

UserFaliedException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Пользователя нет без JWT",
    )

UserFaliedException2 = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Пользователя нет",
    )
