# WealthReaderApi.EntityDataApi

All URIs are relative to *https://virtserver.swaggerhub.com/Wealth-Reader/api/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**entitiesGet**](EntityDataApi.md#entitiesGet) | **GET** /entities | Obtiene el listado de entidades soportadas
[**entitiesPost**](EntityDataApi.md#entitiesPost) | **POST** /entities | Obtiene los activos financieros y el detalle de su composición
[**errorCodesGet**](EntityDataApi.md#errorCodesGet) | **GET** /error-codes | Listado de códigos de error



## entitiesGet

> [Array] entitiesGet()

Obtiene el listado de entidades soportadas

Obtiene el listado de entidades soportadas y la información necesaria para dibujar el formulario de login de la entidad. 

### Example

```javascript
import WealthReaderApi from 'wealth_reader_api';

let apiInstance = new WealthReaderApi.EntityDataApi();
apiInstance.entitiesGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**[Array]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## entitiesPost

> [EntityData] entitiesPost(opts)

Obtiene los activos financieros y el detalle de su composición

Obtiene los activos financieros y el detalle de su composición de carteras de inversión compuestas por acciones o fondos, tarjetas de crédito, seguros y préstamos. Incluye información de titularidad de cada uno de los activos así como identificadores únicos que facilitan el tratamiento del dato. Es posible obtener datos Mock. Consulte con el equipo técnico cómo hacerlo. 

### Example

```javascript
import WealthReaderApi from 'wealth_reader_api';

let apiInstance = new WealthReaderApi.EntityDataApi();
let opts = {
  'OTP': "OTP_example", // String | Solo necesario cuando se esté completando la seguda petición de un login con 2 factores de autenticación, si el tipo de desafío es OTP. Requiere la clave que la entidad le ha enviado al usario final
  'SESSION': "SESSION_example", // String | Solo necesario cuando se esté completando la seguda petición de un login con 2 factores de autenticación. Requiere el valor de SESSION obtenido en la primera petición
  'apiKey': "apiKey_example", // String | Identifica al cliente en el servicio
  'code': "code_example", // String | Nombre de la entidad. El listado completo está disponible con GET
  'contractCode': "contractCode_example", // String | Solo necesario cuando el usuario puede acceder a más de un contrato. El listado de contratos disponibles se obtiene al realizar una conexión con un usuario con opción a trabajar con varios contratos en su entidad (que al hacer login en su banca online ve como primera opción una pantalla de selección de contratos) y cuya llamada a la API no se le ha especificado un valor a contract_code
  'documentType': "documentType_example", // String | Tipo de documento, requerido según la entidad. Si es requerido o no, está indicado en el listado de entidades. Ver definición.
  'password': "password_example", // String | Contraseña
  'secondPassword': "secondPassword_example", // String | Segunda contraseña, requerida según la entidad.
  'token': "token_example", // String | Valor para credenciales custodiadas, tokenizadas previamente mediante una llamada a este método con el valor de tokenize=true. Están disponibles los siguientes usuarios Mock: MOCKDATA, respuesta OK; MOCKOTP, respuesta con desafío OTP; MOCKLOGINKO, respuesta con error de login
  'tokenize': false, // Boolean | Indica si Wealth Reader debe custodiar los credenciales, de tal manera que incluído en el body de respuesta estará un token que permite conectar con la entidad sin necesidad de conocer los credenciales: document_type, user, password, second_password, contract_code
  'user': "user_example" // String | Usuario. Están disponibles los siguientes usuarios Mock: MOCKDATA, respuesta OK; MOCKOTP, respuesta con desafío OTP; MOCKLOGINKO, respuesta con error de login
};
apiInstance.entitiesPost(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **OTP** | **String**| Solo necesario cuando se esté completando la seguda petición de un login con 2 factores de autenticación, si el tipo de desafío es OTP. Requiere la clave que la entidad le ha enviado al usario final | [optional] 
 **SESSION** | **String**| Solo necesario cuando se esté completando la seguda petición de un login con 2 factores de autenticación. Requiere el valor de SESSION obtenido en la primera petición | [optional] 
 **apiKey** | **String**| Identifica al cliente en el servicio | [optional] 
 **code** | **String**| Nombre de la entidad. El listado completo está disponible con GET | [optional] 
 **contractCode** | **String**| Solo necesario cuando el usuario puede acceder a más de un contrato. El listado de contratos disponibles se obtiene al realizar una conexión con un usuario con opción a trabajar con varios contratos en su entidad (que al hacer login en su banca online ve como primera opción una pantalla de selección de contratos) y cuya llamada a la API no se le ha especificado un valor a contract_code | [optional] 
 **documentType** | **String**| Tipo de documento, requerido según la entidad. Si es requerido o no, está indicado en el listado de entidades. Ver definición. | [optional] 
 **password** | **String**| Contraseña | [optional] 
 **secondPassword** | **String**| Segunda contraseña, requerida según la entidad. | [optional] 
 **token** | **String**| Valor para credenciales custodiadas, tokenizadas previamente mediante una llamada a este método con el valor de tokenize&#x3D;true. Están disponibles los siguientes usuarios Mock: MOCKDATA, respuesta OK; MOCKOTP, respuesta con desafío OTP; MOCKLOGINKO, respuesta con error de login | [optional] 
 **tokenize** | **Boolean**| Indica si Wealth Reader debe custodiar los credenciales, de tal manera que incluído en el body de respuesta estará un token que permite conectar con la entidad sin necesidad de conocer los credenciales: document_type, user, password, second_password, contract_code | [optional] [default to false]
 **user** | **String**| Usuario. Están disponibles los siguientes usuarios Mock: MOCKDATA, respuesta OK; MOCKOTP, respuesta con desafío OTP; MOCKLOGINKO, respuesta con error de login | [optional] 

### Return type

[**[EntityData]**](EntityData.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## errorCodesGet

> [Array] errorCodesGet(opts)

Listado de códigos de error

Listado de códigos de error. Presta especial atención a que no todos los códigos de error deben recibir el mismo tratamiento por parte de tu aplicación. Ante un error de password incorrecto no debes reintentar la llamada con los mismos parámetros, pero ante un error que te indique que la entidad está en mantenimiento sí puedes reintentarlo. Pide una sesión técnica con nuestro equipo para resolver cualquier duda sobre la gestión de errores. 

### Example

```javascript
import WealthReaderApi from 'wealth_reader_api';

let apiInstance = new WealthReaderApi.EntityDataApi();
let opts = {
  'lang': "'es'" // String | Idioma de la respuesta
};
apiInstance.errorCodesGet(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lang** | **String**| Idioma de la respuesta | [optional] [default to &#39;es&#39;]

### Return type

**[Array]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

