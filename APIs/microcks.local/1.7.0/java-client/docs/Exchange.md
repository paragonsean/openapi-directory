

# Exchange

Abstract representation of a Service or API exchange type (request/response, event based, ...)

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**request** | [**Request**](Request.md) |  |  |
|**response** | [**Response**](Response.md) |  |  |
|**type** | [**TypeEnum**](#TypeEnum) | Discriminant type for identifying kind of exchange |  |
|**eventMessage** | [**EventMessage**](EventMessage.md) |  |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| REQ_RESP_PAIR | &quot;reqRespPair&quot; |
| UNIDIR_EVENT | &quot;unidirEvent&quot; |



