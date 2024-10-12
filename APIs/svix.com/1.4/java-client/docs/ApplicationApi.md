# ApplicationApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createApplicationApiV1AppPost**](ApplicationApi.md#createApplicationApiV1AppPost) | **POST** /api/v1/app/ | Create Application |
| [**deleteApplicationApiV1AppAppIdDelete**](ApplicationApi.md#deleteApplicationApiV1AppAppIdDelete) | **DELETE** /api/v1/app/{app_id}/ | Delete Application |
| [**getApplicationApiV1AppAppIdGet**](ApplicationApi.md#getApplicationApiV1AppAppIdGet) | **GET** /api/v1/app/{app_id}/ | Get Application |
| [**listApplicationsApiV1AppGet**](ApplicationApi.md#listApplicationsApiV1AppGet) | **GET** /api/v1/app/ | List Applications |
| [**updateApplicationApiV1AppAppIdPut**](ApplicationApi.md#updateApplicationApiV1AppAppIdPut) | **PUT** /api/v1/app/{app_id}/ | Update Application |


<a id="createApplicationApiV1AppPost"></a>
# **createApplicationApiV1AppPost**
> ApplicationOut createApplicationApiV1AppPost(applicationIn, getIfExists, idempotencyKey)

Create Application

Create a new application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    ApplicationApi apiInstance = new ApplicationApi(defaultClient);
    ApplicationIn applicationIn = new ApplicationIn(); // ApplicationIn | 
    Boolean getIfExists = false; // Boolean | Get an existing application, or create a new one if doesn't exist. It's two separate functions in the libs.
    String idempotencyKey = "idempotencyKey_example"; // String | The request's idempotency key
    try {
      ApplicationOut result = apiInstance.createApplicationApiV1AppPost(applicationIn, getIfExists, idempotencyKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationApi#createApplicationApiV1AppPost");
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
| **applicationIn** | [**ApplicationIn**](ApplicationIn.md)|  | |
| **getIfExists** | **Boolean**| Get an existing application, or create a new one if doesn&#39;t exist. It&#39;s two separate functions in the libs. | [optional] [default to false] |
| **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] |

### Return type

[**ApplicationOut**](ApplicationOut.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Successful Response |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **409** | Conflict |  -  |
| **422** | Validation Error |  -  |
| **429** | Too Many Requests |  -  |

<a id="deleteApplicationApiV1AppAppIdDelete"></a>
# **deleteApplicationApiV1AppAppIdDelete**
> deleteApplicationApiV1AppAppIdDelete(appId, idempotencyKey)

Delete Application

Delete an application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    ApplicationApi apiInstance = new ApplicationApi(defaultClient);
    String appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
    String idempotencyKey = "idempotencyKey_example"; // String | The request's idempotency key
    try {
      apiInstance.deleteApplicationApiV1AppAppIdDelete(appId, idempotencyKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationApi#deleteApplicationApiV1AppAppIdDelete");
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

<a id="getApplicationApiV1AppAppIdGet"></a>
# **getApplicationApiV1AppAppIdGet**
> ApplicationOut getApplicationApiV1AppAppIdGet(appId, idempotencyKey)

Get Application

Get an application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    ApplicationApi apiInstance = new ApplicationApi(defaultClient);
    String appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
    String idempotencyKey = "idempotencyKey_example"; // String | The request's idempotency key
    try {
      ApplicationOut result = apiInstance.getApplicationApiV1AppAppIdGet(appId, idempotencyKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationApi#getApplicationApiV1AppAppIdGet");
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
| **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] |

### Return type

[**ApplicationOut**](ApplicationOut.md)

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

<a id="listApplicationsApiV1AppGet"></a>
# **listApplicationsApiV1AppGet**
> ListResponseApplicationOut listApplicationsApiV1AppGet(iterator, limit, order, idempotencyKey)

List Applications

List of all the organization&#39;s applications.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    ApplicationApi apiInstance = new ApplicationApi(defaultClient);
    String iterator = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
    Integer limit = 50; // Integer | 
    Ordering order = Ordering.fromValue("ascending"); // Ordering | 
    String idempotencyKey = "idempotencyKey_example"; // String | The request's idempotency key
    try {
      ListResponseApplicationOut result = apiInstance.listApplicationsApiV1AppGet(iterator, limit, order, idempotencyKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationApi#listApplicationsApiV1AppGet");
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
| **iterator** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] [default to 50] |
| **order** | [**Ordering**](.md)|  | [optional] [default to descending] [enum: ascending, descending] |
| **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] |

### Return type

[**ListResponseApplicationOut**](ListResponseApplicationOut.md)

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

<a id="updateApplicationApiV1AppAppIdPut"></a>
# **updateApplicationApiV1AppAppIdPut**
> ApplicationOut updateApplicationApiV1AppAppIdPut(appId, applicationIn, idempotencyKey)

Update Application

Update an application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    ApplicationApi apiInstance = new ApplicationApi(defaultClient);
    String appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
    ApplicationIn applicationIn = new ApplicationIn(); // ApplicationIn | 
    String idempotencyKey = "idempotencyKey_example"; // String | The request's idempotency key
    try {
      ApplicationOut result = apiInstance.updateApplicationApiV1AppAppIdPut(appId, applicationIn, idempotencyKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationApi#updateApplicationApiV1AppAppIdPut");
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
| **applicationIn** | [**ApplicationIn**](ApplicationIn.md)|  | |
| **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] |

### Return type

[**ApplicationOut**](ApplicationOut.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **409** | Conflict |  -  |
| **422** | Validation Error |  -  |
| **429** | Too Many Requests |  -  |

