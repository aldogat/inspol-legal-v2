async def get_current_user(token: str = Depends(oauth2_scheme_optional)):
    if token is None or token == "demo":
        # Usuario demo fijo para pruebas
        return User(
            id=1,
            email="demo@inspol.com",
            nombre="Demo",
            apellido="User",
            rol="admin"
        )
    # Si hay token, intenta decodificarlo (tu lógica original)
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    # Busca el usuario en BD
    user = await get_user_by_id(user_id)
    if user is None:
        raise credentials_exception
    return user
