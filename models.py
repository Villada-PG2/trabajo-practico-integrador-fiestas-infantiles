from pydantic import BaseModel, Field

class TipoDocumento(BaseModel):
    nombre: str = Field(...)
    descripcion: str = Field(...)

class Chico(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=30)
    apellido: str = Field(..., min_length=3, max_length=30)
    edad: int = Field(..., gt=0)
    tipoDocumento: TipoDocumento = Field(...)
    numeroDocumento: int = Field(..., ge=1000000, le=99999999)

class Cliente(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=30)
    apellido: str = Field(..., min_length=3, max_length=30)
    tipoDocumento: TipoDocumento = Field(...)
    numeroDocumento: int = Field(..., ge=1000000, le=99999999)
    domicilio: str = Field(...)
    telefono: str = Field(..., min_length=8, max_length=15)
    celular: str = Field(..., min_length=8, max_length=15)
    email: str = Field(...)
    hijos: list[Chico] = []
