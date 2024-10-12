

# ErrorDetail


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | **Integer** | El código indica la familia del error. Por ejemplo, de 2000 a 2999 indican problemas en el login. Cada código de error debe tratarse de forma diferente. Por ejemplo, si el código indica \&quot;Login incorrecto\&quot;, no se debe reintentar la llamada; si el código indica \&quot;entidad en mantenimiento\&quot; sí se puede reintentar más tarde. Puedes obtener el listado completo en el método error-codes. |  |
|**contracts** |  | Solamente estará informado cuando el valor de code sea 2020 (usuario multicontrato) |  [optional] |
|**message** | **String** | Texto en el idioma de la entidad. Es seguro mostrárselo al usuario y en muchos casos le ayudará a corregir el error |  |



