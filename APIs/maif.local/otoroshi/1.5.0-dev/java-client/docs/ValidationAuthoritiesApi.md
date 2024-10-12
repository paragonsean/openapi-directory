# ValidationAuthoritiesApi

All URIs are relative to *http://otoroshi-api.oto.tools*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createClientValidator**](ValidationAuthoritiesApi.md#createClientValidator) | **POST** /api/client-validators | Create one validation authorities |
| [**deleteClientValidator**](ValidationAuthoritiesApi.md#deleteClientValidator) | **DELETE** /api/client-validators/{id} | Delete one validation authorities by id |
| [**findAllClientValidators**](ValidationAuthoritiesApi.md#findAllClientValidators) | **GET** /api/client-validators | Get all validation authoritiess |
| [**findClientValidatorById**](ValidationAuthoritiesApi.md#findClientValidatorById) | **GET** /api/client-validators/{id} | Get one validation authorities by id |
| [**patchClientValidator**](ValidationAuthoritiesApi.md#patchClientValidator) | **PATCH** /api/client-validators/{id} | Update one validation authorities by id |
| [**updateClientValidator**](ValidationAuthoritiesApi.md#updateClientValidator) | **PUT** /api/client-validators/{id} | Update one validation authorities by id |


<a id="createClientValidator"></a>
# **createClientValidator**
> ValidationAuthority createClientValidator(validationAuthority)

Create one validation authorities

Create one validation authorities

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ValidationAuthoritiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    ValidationAuthoritiesApi apiInstance = new ValidationAuthoritiesApi(defaultClient);
    ValidationAuthority validationAuthority = new ValidationAuthority(); // ValidationAuthority | 
    try {
      ValidationAuthority result = apiInstance.createClientValidator(validationAuthority);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ValidationAuthoritiesApi#createClientValidator");
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
| **validationAuthority** | [**ValidationAuthority**](ValidationAuthority.md)|  | [optional] |

### Return type

[**ValidationAuthority**](ValidationAuthority.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **400** | Bad resource format. Take another look to the swagger, or open an issue :) |  -  |
| **401** | You have to provide an Api Key. Api Key can be passed with &#39;Otoroshi-Client-Id&#39; and &#39;Otoroshi-Client-Secret&#39; headers, or use basic http authentication |  -  |
| **404** | Resource not found or does not exist |  -  |

<a id="deleteClientValidator"></a>
# **deleteClientValidator**
> Deleted deleteClientValidator(id)

Delete one validation authorities by id

Delete one validation authorities by id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ValidationAuthoritiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    ValidationAuthoritiesApi apiInstance = new ValidationAuthoritiesApi(defaultClient);
    String id = "id_example"; // String | The validation authorities id
    try {
      Deleted result = apiInstance.deleteClientValidator(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ValidationAuthoritiesApi#deleteClientValidator");
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
| **id** | **String**| The validation authorities id | |

### Return type

[**Deleted**](Deleted.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **400** | Bad resource format. Take another look to the swagger, or open an issue :) |  -  |
| **401** | You have to provide an Api Key. Api Key can be passed with &#39;Otoroshi-Client-Id&#39; and &#39;Otoroshi-Client-Secret&#39; headers, or use basic http authentication |  -  |
| **404** | Resource not found or does not exist |  -  |

<a id="findAllClientValidators"></a>
# **findAllClientValidators**
> List&lt;ValidationAuthority&gt; findAllClientValidators()

Get all validation authoritiess

Get all validation authoritiess

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ValidationAuthoritiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    ValidationAuthoritiesApi apiInstance = new ValidationAuthoritiesApi(defaultClient);
    try {
      List<ValidationAuthority> result = apiInstance.findAllClientValidators();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ValidationAuthoritiesApi#findAllClientValidators");
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

[**List&lt;ValidationAuthority&gt;**](ValidationAuthority.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **400** | Bad resource format. Take another look to the swagger, or open an issue :) |  -  |
| **401** | You have to provide an Api Key. Api Key can be passed with &#39;Otoroshi-Client-Id&#39; and &#39;Otoroshi-Client-Secret&#39; headers, or use basic http authentication |  -  |
| **404** | Resource not found or does not exist |  -  |

<a id="findClientValidatorById"></a>
# **findClientValidatorById**
> ValidationAuthority findClientValidatorById(id)

Get one validation authorities by id

Get one validation authorities by id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ValidationAuthoritiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    ValidationAuthoritiesApi apiInstance = new ValidationAuthoritiesApi(defaultClient);
    String id = "id_example"; // String | The auth. config id
    try {
      ValidationAuthority result = apiInstance.findClientValidatorById(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ValidationAuthoritiesApi#findClientValidatorById");
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
| **id** | **String**| The auth. config id | |

### Return type

[**ValidationAuthority**](ValidationAuthority.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **400** | Bad resource format. Take another look to the swagger, or open an issue :) |  -  |
| **401** | You have to provide an Api Key. Api Key can be passed with &#39;Otoroshi-Client-Id&#39; and &#39;Otoroshi-Client-Secret&#39; headers, or use basic http authentication |  -  |
| **404** | Resource not found or does not exist |  -  |

<a id="patchClientValidator"></a>
# **patchClientValidator**
> ValidationAuthority patchClientValidator(id, patchInner)

Update one validation authorities by id

Update one validation authorities by id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ValidationAuthoritiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    ValidationAuthoritiesApi apiInstance = new ValidationAuthoritiesApi(defaultClient);
    String id = "id_example"; // String | The validation authorities id
    List<PatchInner> patchInner = Arrays.asList(); // List<PatchInner> | 
    try {
      ValidationAuthority result = apiInstance.patchClientValidator(id, patchInner);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ValidationAuthoritiesApi#patchClientValidator");
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
| **id** | **String**| The validation authorities id | |
| **patchInner** | [**List&lt;PatchInner&gt;**](PatchInner.md)|  | [optional] |

### Return type

[**ValidationAuthority**](ValidationAuthority.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **400** | Bad resource format. Take another look to the swagger, or open an issue :) |  -  |
| **401** | You have to provide an Api Key. Api Key can be passed with &#39;Otoroshi-Client-Id&#39; and &#39;Otoroshi-Client-Secret&#39; headers, or use basic http authentication |  -  |
| **404** | Resource not found or does not exist |  -  |

<a id="updateClientValidator"></a>
# **updateClientValidator**
> ValidationAuthority updateClientValidator(id, validationAuthority)

Update one validation authorities by id

Update one validation authorities by id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ValidationAuthoritiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    ValidationAuthoritiesApi apiInstance = new ValidationAuthoritiesApi(defaultClient);
    String id = "id_example"; // String | The validation authorities id
    ValidationAuthority validationAuthority = new ValidationAuthority(); // ValidationAuthority | 
    try {
      ValidationAuthority result = apiInstance.updateClientValidator(id, validationAuthority);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ValidationAuthoritiesApi#updateClientValidator");
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
| **id** | **String**| The validation authorities id | |
| **validationAuthority** | [**ValidationAuthority**](ValidationAuthority.md)|  | [optional] |

### Return type

[**ValidationAuthority**](ValidationAuthority.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **400** | Bad resource format. Take another look to the swagger, or open an issue :) |  -  |
| **401** | You have to provide an Api Key. Api Key can be passed with &#39;Otoroshi-Client-Id&#39; and &#39;Otoroshi-Client-Secret&#39; headers, or use basic http authentication |  -  |
| **404** | Resource not found or does not exist |  -  |

