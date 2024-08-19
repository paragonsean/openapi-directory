# IntegrationApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createIntegrationApiV1AppAppIdIntegrationPost**](IntegrationApi.md#createIntegrationApiV1AppAppIdIntegrationPost) | **POST** /api/v1/app/{app_id}/integration/ | Create Integration |
| [**deleteIntegrationApiV1AppAppIdIntegrationIntegIdDelete**](IntegrationApi.md#deleteIntegrationApiV1AppAppIdIntegrationIntegIdDelete) | **DELETE** /api/v1/app/{app_id}/integration/{integ_id}/ | Delete Integration |
| [**getIntegrationApiV1AppAppIdIntegrationIntegIdGet**](IntegrationApi.md#getIntegrationApiV1AppAppIdIntegrationIntegIdGet) | **GET** /api/v1/app/{app_id}/integration/{integ_id}/ | Get Integration |
| [**getIntegrationKeyApiV1AppAppIdIntegrationIntegIdKeyGet**](IntegrationApi.md#getIntegrationKeyApiV1AppAppIdIntegrationIntegIdKeyGet) | **GET** /api/v1/app/{app_id}/integration/{integ_id}/key/ | Get Integration Key |
| [**listIntegrationsApiV1AppAppIdIntegrationGet**](IntegrationApi.md#listIntegrationsApiV1AppAppIdIntegrationGet) | **GET** /api/v1/app/{app_id}/integration/ | List Integrations |
| [**rotateIntegrationKeyApiV1AppAppIdIntegrationIntegIdKeyRotatePost**](IntegrationApi.md#rotateIntegrationKeyApiV1AppAppIdIntegrationIntegIdKeyRotatePost) | **POST** /api/v1/app/{app_id}/integration/{integ_id}/key/rotate/ | Rotate Integration Key |
| [**updateIntegrationApiV1AppAppIdIntegrationIntegIdPut**](IntegrationApi.md#updateIntegrationApiV1AppAppIdIntegrationIntegIdPut) | **PUT** /api/v1/app/{app_id}/integration/{integ_id}/ | Update Integration |


<a id="createIntegrationApiV1AppAppIdIntegrationPost"></a>
# **createIntegrationApiV1AppAppIdIntegrationPost**
> IntegrationOut createIntegrationApiV1AppAppIdIntegrationPost(appId, integrationIn, idempotencyKey)

Create Integration

Create an integration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    IntegrationApi apiInstance = new IntegrationApi(defaultClient);
    String appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
    IntegrationIn integrationIn = new IntegrationIn(); // IntegrationIn | 
    String idempotencyKey = "idempotencyKey_example"; // String | The request's idempotency key
    try {
      IntegrationOut result = apiInstance.createIntegrationApiV1AppAppIdIntegrationPost(appId, integrationIn, idempotencyKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationApi#createIntegrationApiV1AppAppIdIntegrationPost");
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
| **appId** | **String**|  | |
| **integrationIn** | [**IntegrationIn**](IntegrationIn.md)|  | |
| **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] |

### Return type

[**IntegrationOut**](IntegrationOut.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful Response |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **409** | Conflict |  -  |
| **422** | Validation Error |  -  |
| **429** | Too Many Requests |  -  |

<a id="deleteIntegrationApiV1AppAppIdIntegrationIntegIdDelete"></a>
# **deleteIntegrationApiV1AppAppIdIntegrationIntegIdDelete**
> deleteIntegrationApiV1AppAppIdIntegrationIntegIdDelete(integId, appId, idempotencyKey)

Delete Integration

Delete an integration and revoke it&#39;s key.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    IntegrationApi apiInstance = new IntegrationApi(defaultClient);
    String integId = "integ_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
    String appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
    String idempotencyKey = "idempotencyKey_example"; // String | The request's idempotency key
    try {
      apiInstance.deleteIntegrationApiV1AppAppIdIntegrationIntegIdDelete(integId, appId, idempotencyKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationApi#deleteIntegrationApiV1AppAppIdIntegrationIntegIdDelete");
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
| **integId** | **String**|  | |
| **appId** | **String**|  | |
| **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] |

### Return type

null (empty response body)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successful Response |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **409** | Conflict |  -  |
| **422** | Validation Error |  -  |
| **429** | Too Many Requests |  -  |

<a id="getIntegrationApiV1AppAppIdIntegrationIntegIdGet"></a>
# **getIntegrationApiV1AppAppIdIntegrationIntegIdGet**
> IntegrationOut getIntegrationApiV1AppAppIdIntegrationIntegIdGet(integId, appId, idempotencyKey)

Get Integration

Get an integration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    IntegrationApi apiInstance = new IntegrationApi(defaultClient);
    String integId = "integ_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
    String appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
    String idempotencyKey = "idempotencyKey_example"; // String | The request's idempotency key
    try {
      IntegrationOut result = apiInstance.getIntegrationApiV1AppAppIdIntegrationIntegIdGet(integId, appId, idempotencyKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationApi#getIntegrationApiV1AppAppIdIntegrationIntegIdGet");
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
| **integId** | **String**|  | |
| **appId** | **String**|  | |
| **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] |

### Return type

[**IntegrationOut**](IntegrationOut.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **409** | Conflict |  -  |
| **422** | Validation Error |  -  |
| **429** | Too Many Requests |  -  |

<a id="getIntegrationKeyApiV1AppAppIdIntegrationIntegIdKeyGet"></a>
# **getIntegrationKeyApiV1AppAppIdIntegrationIntegIdKeyGet**
> IntegrationKeyOut getIntegrationKeyApiV1AppAppIdIntegrationIntegIdKeyGet(integId, appId, idempotencyKey)

Get Integration Key

Get an integration&#39;s key.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    IntegrationApi apiInstance = new IntegrationApi(defaultClient);
    String integId = "integ_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
    String appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
    String idempotencyKey = "idempotencyKey_example"; // String | The request's idempotency key
    try {
      IntegrationKeyOut result = apiInstance.getIntegrationKeyApiV1AppAppIdIntegrationIntegIdKeyGet(integId, appId, idempotencyKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationApi#getIntegrationKeyApiV1AppAppIdIntegrationIntegIdKeyGet");
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
| **integId** | **String**|  | |
| **appId** | **String**|  | |
| **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] |

### Return type

[**IntegrationKeyOut**](IntegrationKeyOut.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **409** | Conflict |  -  |
| **422** | Validation Error |  -  |
| **429** | Too Many Requests |  -  |

<a id="listIntegrationsApiV1AppAppIdIntegrationGet"></a>
# **listIntegrationsApiV1AppAppIdIntegrationGet**
> ListResponseIntegrationOut listIntegrationsApiV1AppAppIdIntegrationGet(appId, iterator, limit, idempotencyKey)

List Integrations

List the application&#39;s integrations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    IntegrationApi apiInstance = new IntegrationApi(defaultClient);
    String appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
    String iterator = "integ_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
    Integer limit = 50; // Integer | 
    String idempotencyKey = "idempotencyKey_example"; // String | The request's idempotency key
    try {
      ListResponseIntegrationOut result = apiInstance.listIntegrationsApiV1AppAppIdIntegrationGet(appId, iterator, limit, idempotencyKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationApi#listIntegrationsApiV1AppAppIdIntegrationGet");
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
| **appId** | **String**|  | |
| **iterator** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] [default to 50] |
| **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] |

### Return type

[**ListResponseIntegrationOut**](ListResponseIntegrationOut.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **409** | Conflict |  -  |
| **422** | Validation Error |  -  |
| **429** | Too Many Requests |  -  |

<a id="rotateIntegrationKeyApiV1AppAppIdIntegrationIntegIdKeyRotatePost"></a>
# **rotateIntegrationKeyApiV1AppAppIdIntegrationIntegIdKeyRotatePost**
> IntegrationKeyOut rotateIntegrationKeyApiV1AppAppIdIntegrationIntegIdKeyRotatePost(integId, appId, idempotencyKey)

Rotate Integration Key

Rotate the integration&#39;s key. The previous key will be immediately revoked.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    IntegrationApi apiInstance = new IntegrationApi(defaultClient);
    String integId = "integ_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
    String appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
    String idempotencyKey = "idempotencyKey_example"; // String | The request's idempotency key
    try {
      IntegrationKeyOut result = apiInstance.rotateIntegrationKeyApiV1AppAppIdIntegrationIntegIdKeyRotatePost(integId, appId, idempotencyKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationApi#rotateIntegrationKeyApiV1AppAppIdIntegrationIntegIdKeyRotatePost");
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
| **integId** | **String**|  | |
| **appId** | **String**|  | |
| **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] |

### Return type

[**IntegrationKeyOut**](IntegrationKeyOut.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **409** | Conflict |  -  |
| **422** | Validation Error |  -  |
| **429** | Too Many Requests |  -  |

<a id="updateIntegrationApiV1AppAppIdIntegrationIntegIdPut"></a>
# **updateIntegrationApiV1AppAppIdIntegrationIntegIdPut**
> IntegrationOut updateIntegrationApiV1AppAppIdIntegrationIntegIdPut(integId, appId, integrationUpdate, idempotencyKey)

Update Integration

Update an integration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    IntegrationApi apiInstance = new IntegrationApi(defaultClient);
    String integId = "integ_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
    String appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
    IntegrationUpdate integrationUpdate = new IntegrationUpdate(); // IntegrationUpdate | 
    String idempotencyKey = "idempotencyKey_example"; // String | The request's idempotency key
    try {
      IntegrationOut result = apiInstance.updateIntegrationApiV1AppAppIdIntegrationIntegIdPut(integId, appId, integrationUpdate, idempotencyKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationApi#updateIntegrationApiV1AppAppIdIntegrationIntegIdPut");
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
| **integId** | **String**|  | |
| **appId** | **String**|  | |
| **integrationUpdate** | [**IntegrationUpdate**](IntegrationUpdate.md)|  | |
| **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] |

### Return type

[**IntegrationOut**](IntegrationOut.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **409** | Conflict |  -  |
| **422** | Validation Error |  -  |
| **429** | Too Many Requests |  -  |

