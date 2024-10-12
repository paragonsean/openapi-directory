# EntityDataApi

All URIs are relative to *https://virtserver.swaggerhub.com/Wealth-Reader/api/1.0.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**entitiesGet**](EntityDataApi.md#entitiesGet) | **GET** /entities | Obtiene el listado de entidades soportadas |
| [**entitiesPost**](EntityDataApi.md#entitiesPost) | **POST** /entities | Obtiene los activos financieros y el detalle de su composición |
| [**errorCodesGet**](EntityDataApi.md#errorCodesGet) | **GET** /error-codes | Listado de códigos de error |


<a id="entitiesGet"></a>
# **entitiesGet**
> List&lt;List&lt;Object&gt;&gt; entitiesGet()

Obtiene el listado de entidades soportadas

Obtiene el listado de entidades soportadas y la información necesaria para dibujar el formulario de login de la entidad. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntityDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://virtserver.swaggerhub.com/Wealth-Reader/api/1.0.0");

    EntityDataApi apiInstance = new EntityDataApi(defaultClient);
    try {
      List<List<Object>> result = apiInstance.entitiesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntityDataApi#entitiesGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;List&lt;Object&gt;&gt;**](List.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | listado de entidades |  -  |
| **400** | error |  -  |

<a id="entitiesPost"></a>
# **entitiesPost**
> List&lt;EntityData&gt; entitiesPost(OTP, SESSION, apiKey, code, contractCode, documentType, password, secondPassword, token, tokenize, user)

Obtiene los activos financieros y el detalle de su composición

Obtiene los activos financieros y el detalle de su composición de carteras de inversión compuestas por acciones o fondos, tarjetas de crédito, seguros y préstamos. Incluye información de titularidad de cada uno de los activos así como identificadores únicos que facilitan el tratamiento del dato. Es posible obtener datos Mock. Consulte con el equipo técnico cómo hacerlo. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntityDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://virtserver.swaggerhub.com/Wealth-Reader/api/1.0.0");

    EntityDataApi apiInstance = new EntityDataApi(defaultClient);
    String OTP = "OTP_example"; // String | Solo necesario cuando se esté completando la seguda petición de un login con 2 factores de autenticación, si el tipo de desafío es OTP. Requiere la clave que la entidad le ha enviado al usario final
    String SESSION = "SESSION_example"; // String | Solo necesario cuando se esté completando la seguda petición de un login con 2 factores de autenticación. Requiere el valor de SESSION obtenido en la primera petición
    String apiKey = "apiKey_example"; // String | Identifica al cliente en el servicio
    String code = "code_example"; // String | Nombre de la entidad. El listado completo está disponible con GET
    String contractCode = "contractCode_example"; // String | Solo necesario cuando el usuario puede acceder a más de un contrato. El listado de contratos disponibles se obtiene al realizar una conexión con un usuario con opción a trabajar con varios contratos en su entidad (que al hacer login en su banca online ve como primera opción una pantalla de selección de contratos) y cuya llamada a la API no se le ha especificado un valor a contract_code
    String documentType = "NIF"; // String | Tipo de documento, requerido según la entidad. Si es requerido o no, está indicado en el listado de entidades. Ver definición.
    String password = "password_example"; // String | Contraseña
    String secondPassword = "secondPassword_example"; // String | Segunda contraseña, requerida según la entidad.
    String token = "token_example"; // String | Valor para credenciales custodiadas, tokenizadas previamente mediante una llamada a este método con el valor de tokenize=true. Están disponibles los siguientes usuarios Mock: MOCKDATA, respuesta OK; MOCKOTP, respuesta con desafío OTP; MOCKLOGINKO, respuesta con error de login
    Boolean tokenize = false; // Boolean | Indica si Wealth Reader debe custodiar los credenciales, de tal manera que incluído en el body de respuesta estará un token que permite conectar con la entidad sin necesidad de conocer los credenciales: document_type, user, password, second_password, contract_code
    String user = "user_example"; // String | Usuario. Están disponibles los siguientes usuarios Mock: MOCKDATA, respuesta OK; MOCKOTP, respuesta con desafío OTP; MOCKLOGINKO, respuesta con error de login
    try {
      List<EntityData> result = apiInstance.entitiesPost(OTP, SESSION, apiKey, code, contractCode, documentType, password, secondPassword, token, tokenize, user);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntityDataApi#entitiesPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **OTP** | **String**| Solo necesario cuando se esté completando la seguda petición de un login con 2 factores de autenticación, si el tipo de desafío es OTP. Requiere la clave que la entidad le ha enviado al usario final | [optional] |
| **SESSION** | **String**| Solo necesario cuando se esté completando la seguda petición de un login con 2 factores de autenticación. Requiere el valor de SESSION obtenido en la primera petición | [optional] |
| **apiKey** | **String**| Identifica al cliente en el servicio | [optional] |
| **code** | **String**| Nombre de la entidad. El listado completo está disponible con GET | [optional] |
| **contractCode** | **String**| Solo necesario cuando el usuario puede acceder a más de un contrato. El listado de contratos disponibles se obtiene al realizar una conexión con un usuario con opción a trabajar con varios contratos en su entidad (que al hacer login en su banca online ve como primera opción una pantalla de selección de contratos) y cuya llamada a la API no se le ha especificado un valor a contract_code | [optional] |
| **documentType** | **String**| Tipo de documento, requerido según la entidad. Si es requerido o no, está indicado en el listado de entidades. Ver definición. | [optional] [enum: NIF, Pasaporte, Tarjeta de residencia] |
| **password** | **String**| Contraseña | [optional] |
| **secondPassword** | **String**| Segunda contraseña, requerida según la entidad. | [optional] |
| **token** | **String**| Valor para credenciales custodiadas, tokenizadas previamente mediante una llamada a este método con el valor de tokenize&#x3D;true. Están disponibles los siguientes usuarios Mock: MOCKDATA, respuesta OK; MOCKOTP, respuesta con desafío OTP; MOCKLOGINKO, respuesta con error de login | [optional] |
| **tokenize** | **Boolean**| Indica si Wealth Reader debe custodiar los credenciales, de tal manera que incluído en el body de respuesta estará un token que permite conectar con la entidad sin necesidad de conocer los credenciales: document_type, user, password, second_password, contract_code | [optional] [default to false] |
| **user** | **String**| Usuario. Están disponibles los siguientes usuarios Mock: MOCKDATA, respuesta OK; MOCKOTP, respuesta con desafío OTP; MOCKLOGINKO, respuesta con error de login | [optional] |

### Return type

[**List&lt;EntityData&gt;**](EntityData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | datos obtenidos de la entidad |  -  |
| **400** | error |  -  |

<a id="errorCodesGet"></a>
# **errorCodesGet**
> List&lt;List&lt;List&lt;Object&gt;&gt;&gt; errorCodesGet(lang)

Listado de códigos de error

Listado de códigos de error. Presta especial atención a que no todos los códigos de error deben recibir el mismo tratamiento por parte de tu aplicación. Ante un error de password incorrecto no debes reintentar la llamada con los mismos parámetros, pero ante un error que te indique que la entidad está en mantenimiento sí puedes reintentarlo. Pide una sesión técnica con nuestro equipo para resolver cualquier duda sobre la gestión de errores. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntityDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://virtserver.swaggerhub.com/Wealth-Reader/api/1.0.0");

    EntityDataApi apiInstance = new EntityDataApi(defaultClient);
    String lang = "es"; // String | Idioma de la respuesta
    try {
      List<List<List<Object>>> result = apiInstance.errorCodesGet(lang);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntityDataApi#errorCodesGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **lang** | **String**| Idioma de la respuesta | [optional] [default to es] [enum: es, en] |

### Return type

[**List&lt;List&lt;List&lt;Object&gt;&gt;&gt;**](List.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Códigos de error junto con su descripción, posible motivo y cómo proceder |  -  |
| **400** | error |  -  |

