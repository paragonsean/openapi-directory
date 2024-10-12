# AuthConfigApi

All URIs are relative to *http://otoroshi-api.oto.tools*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createGlobalAuthModule**](AuthConfigApi.md#createGlobalAuthModule) | **POST** /api/auths | Create one global auth. module config |
| [**deleteGlobalAuthModule**](AuthConfigApi.md#deleteGlobalAuthModule) | **DELETE** /api/auths/{id} | Delete one global auth. module config |
| [**findAllGlobalAuthModules**](AuthConfigApi.md#findAllGlobalAuthModules) | **GET** /api/auths | Get all global auth. module configs |
| [**findGlobalAuthModuleById**](AuthConfigApi.md#findGlobalAuthModuleById) | **GET** /api/auths/{id} | Get one global auth. module configs |
| [**patchGlobalAuthModule**](AuthConfigApi.md#patchGlobalAuthModule) | **PATCH** /api/auths/{id} | Update one global auth. module config |
| [**updateGlobalAuthModule**](AuthConfigApi.md#updateGlobalAuthModule) | **PUT** /api/auths/{id} | Update one global auth. module config |


<a id="createGlobalAuthModule"></a>
# **createGlobalAuthModule**
> FindAllGlobalAuthModules200ResponseInner createGlobalAuthModule(findAllGlobalAuthModules200ResponseInner)

Create one global auth. module config

Create one global auth. module config

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    AuthConfigApi apiInstance = new AuthConfigApi(defaultClient);
    FindAllGlobalAuthModules200ResponseInner findAllGlobalAuthModules200ResponseInner = new FindAllGlobalAuthModules200ResponseInner(); // FindAllGlobalAuthModules200ResponseInner | 
    try {
      FindAllGlobalAuthModules200ResponseInner result = apiInstance.createGlobalAuthModule(findAllGlobalAuthModules200ResponseInner);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthConfigApi#createGlobalAuthModule");
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
| **findAllGlobalAuthModules200ResponseInner** | [**FindAllGlobalAuthModules200ResponseInner**](FindAllGlobalAuthModules200ResponseInner.md)|  | [optional] |

### Return type

[**FindAllGlobalAuthModules200ResponseInner**](FindAllGlobalAuthModules200ResponseInner.md)

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

<a id="deleteGlobalAuthModule"></a>
# **deleteGlobalAuthModule**
> Deleted deleteGlobalAuthModule(id)

Delete one global auth. module config

Delete one global auth. module config

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    AuthConfigApi apiInstance = new AuthConfigApi(defaultClient);
    String id = "id_example"; // String | The auth. config id id
    try {
      Deleted result = apiInstance.deleteGlobalAuthModule(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthConfigApi#deleteGlobalAuthModule");
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
| **id** | **String**| The auth. config id id | |

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

<a id="findAllGlobalAuthModules"></a>
# **findAllGlobalAuthModules**
> List&lt;FindAllGlobalAuthModules200ResponseInner&gt; findAllGlobalAuthModules()

Get all global auth. module configs

Get all global auth. module configs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    AuthConfigApi apiInstance = new AuthConfigApi(defaultClient);
    try {
      List<FindAllGlobalAuthModules200ResponseInner> result = apiInstance.findAllGlobalAuthModules();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthConfigApi#findAllGlobalAuthModules");
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

[**List&lt;FindAllGlobalAuthModules200ResponseInner&gt;**](FindAllGlobalAuthModules200ResponseInner.md)

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

<a id="findGlobalAuthModuleById"></a>
# **findGlobalAuthModuleById**
> FindAllGlobalAuthModules200ResponseInner findGlobalAuthModuleById(id)

Get one global auth. module configs

Get one global auth. module configs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    AuthConfigApi apiInstance = new AuthConfigApi(defaultClient);
    String id = "id_example"; // String | The auth. config id
    try {
      FindAllGlobalAuthModules200ResponseInner result = apiInstance.findGlobalAuthModuleById(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthConfigApi#findGlobalAuthModuleById");
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

[**FindAllGlobalAuthModules200ResponseInner**](FindAllGlobalAuthModules200ResponseInner.md)

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

<a id="patchGlobalAuthModule"></a>
# **patchGlobalAuthModule**
> FindAllGlobalAuthModules200ResponseInner patchGlobalAuthModule(id, patchInner)

Update one global auth. module config

Update one global auth. module config

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    AuthConfigApi apiInstance = new AuthConfigApi(defaultClient);
    String id = "id_example"; // String | The auth. config id
    List<PatchInner> patchInner = Arrays.asList(); // List<PatchInner> | 
    try {
      FindAllGlobalAuthModules200ResponseInner result = apiInstance.patchGlobalAuthModule(id, patchInner);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthConfigApi#patchGlobalAuthModule");
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
| **patchInner** | [**List&lt;PatchInner&gt;**](PatchInner.md)|  | [optional] |

### Return type

[**FindAllGlobalAuthModules200ResponseInner**](FindAllGlobalAuthModules200ResponseInner.md)

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

<a id="updateGlobalAuthModule"></a>
# **updateGlobalAuthModule**
> FindAllGlobalAuthModules200ResponseInner updateGlobalAuthModule(id, findAllGlobalAuthModules200ResponseInner)

Update one global auth. module config

Update one global auth. module config

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    AuthConfigApi apiInstance = new AuthConfigApi(defaultClient);
    String id = "id_example"; // String | The auth. config id
    FindAllGlobalAuthModules200ResponseInner findAllGlobalAuthModules200ResponseInner = new FindAllGlobalAuthModules200ResponseInner(); // FindAllGlobalAuthModules200ResponseInner | 
    try {
      FindAllGlobalAuthModules200ResponseInner result = apiInstance.updateGlobalAuthModule(id, findAllGlobalAuthModules200ResponseInner);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthConfigApi#updateGlobalAuthModule");
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
| **findAllGlobalAuthModules200ResponseInner** | [**FindAllGlobalAuthModules200ResponseInner**](FindAllGlobalAuthModules200ResponseInner.md)|  | [optional] |

### Return type

[**FindAllGlobalAuthModules200ResponseInner**](FindAllGlobalAuthModules200ResponseInner.md)

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

