# JwtVerifiersApi

All URIs are relative to *http://otoroshi-api.oto.tools*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createGlobalJwtVerifier**](JwtVerifiersApi.md#createGlobalJwtVerifier) | **POST** /api/verifiers | Create one global JWT verifiers |
| [**deleteGlobalJwtVerifier**](JwtVerifiersApi.md#deleteGlobalJwtVerifier) | **DELETE** /api/verifiers/{verifierId} | Delete one global JWT verifiers |
| [**findAllGlobalJwtVerifiers**](JwtVerifiersApi.md#findAllGlobalJwtVerifiers) | **GET** /api/verifiers | Get all global JWT verifiers |
| [**findGlobalJwtVerifiersById**](JwtVerifiersApi.md#findGlobalJwtVerifiersById) | **GET** /api/verifiers/{verifierId} | Get one global JWT verifiers |
| [**patchGlobalJwtVerifier**](JwtVerifiersApi.md#patchGlobalJwtVerifier) | **PATCH** /api/verifiers/{verifierId} | Update one global JWT verifiers |
| [**updateGlobalJwtVerifier**](JwtVerifiersApi.md#updateGlobalJwtVerifier) | **PUT** /api/verifiers/{verifierId} | Update one global JWT verifiers |


<a id="createGlobalJwtVerifier"></a>
# **createGlobalJwtVerifier**
> GlobalJwtVerifier createGlobalJwtVerifier(globalJwtVerifier)

Create one global JWT verifiers

Create one global JWT verifiers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JwtVerifiersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    JwtVerifiersApi apiInstance = new JwtVerifiersApi(defaultClient);
    GlobalJwtVerifier globalJwtVerifier = new GlobalJwtVerifier(); // GlobalJwtVerifier | 
    try {
      GlobalJwtVerifier result = apiInstance.createGlobalJwtVerifier(globalJwtVerifier);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JwtVerifiersApi#createGlobalJwtVerifier");
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
| **globalJwtVerifier** | [**GlobalJwtVerifier**](GlobalJwtVerifier.md)|  | [optional] |

### Return type

[**GlobalJwtVerifier**](GlobalJwtVerifier.md)

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

<a id="deleteGlobalJwtVerifier"></a>
# **deleteGlobalJwtVerifier**
> Deleted deleteGlobalJwtVerifier(verifierId)

Delete one global JWT verifiers

Delete one global JWT verifiers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JwtVerifiersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    JwtVerifiersApi apiInstance = new JwtVerifiersApi(defaultClient);
    String verifierId = "verifierId_example"; // String | The jwt verifier id
    try {
      Deleted result = apiInstance.deleteGlobalJwtVerifier(verifierId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JwtVerifiersApi#deleteGlobalJwtVerifier");
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
| **verifierId** | **String**| The jwt verifier id | |

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

<a id="findAllGlobalJwtVerifiers"></a>
# **findAllGlobalJwtVerifiers**
> List&lt;GlobalJwtVerifier&gt; findAllGlobalJwtVerifiers()

Get all global JWT verifiers

Get all global JWT verifiers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JwtVerifiersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    JwtVerifiersApi apiInstance = new JwtVerifiersApi(defaultClient);
    try {
      List<GlobalJwtVerifier> result = apiInstance.findAllGlobalJwtVerifiers();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JwtVerifiersApi#findAllGlobalJwtVerifiers");
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

[**List&lt;GlobalJwtVerifier&gt;**](GlobalJwtVerifier.md)

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

<a id="findGlobalJwtVerifiersById"></a>
# **findGlobalJwtVerifiersById**
> GlobalJwtVerifier findGlobalJwtVerifiersById(verifierId)

Get one global JWT verifiers

Get one global JWT verifiers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JwtVerifiersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    JwtVerifiersApi apiInstance = new JwtVerifiersApi(defaultClient);
    String verifierId = "verifierId_example"; // String | The jwt verifier id
    try {
      GlobalJwtVerifier result = apiInstance.findGlobalJwtVerifiersById(verifierId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JwtVerifiersApi#findGlobalJwtVerifiersById");
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
| **verifierId** | **String**| The jwt verifier id | |

### Return type

[**GlobalJwtVerifier**](GlobalJwtVerifier.md)

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

<a id="patchGlobalJwtVerifier"></a>
# **patchGlobalJwtVerifier**
> GlobalJwtVerifier patchGlobalJwtVerifier(verifierId, patchInner)

Update one global JWT verifiers

Update one global JWT verifiers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JwtVerifiersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    JwtVerifiersApi apiInstance = new JwtVerifiersApi(defaultClient);
    String verifierId = "verifierId_example"; // String | The jwt verifier id
    List<PatchInner> patchInner = Arrays.asList(); // List<PatchInner> | 
    try {
      GlobalJwtVerifier result = apiInstance.patchGlobalJwtVerifier(verifierId, patchInner);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JwtVerifiersApi#patchGlobalJwtVerifier");
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
| **verifierId** | **String**| The jwt verifier id | |
| **patchInner** | [**List&lt;PatchInner&gt;**](PatchInner.md)|  | [optional] |

### Return type

[**GlobalJwtVerifier**](GlobalJwtVerifier.md)

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

<a id="updateGlobalJwtVerifier"></a>
# **updateGlobalJwtVerifier**
> GlobalJwtVerifier updateGlobalJwtVerifier(verifierId, globalJwtVerifier)

Update one global JWT verifiers

Update one global JWT verifiers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JwtVerifiersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    JwtVerifiersApi apiInstance = new JwtVerifiersApi(defaultClient);
    String verifierId = "verifierId_example"; // String | The jwt verifier id
    GlobalJwtVerifier globalJwtVerifier = new GlobalJwtVerifier(); // GlobalJwtVerifier | 
    try {
      GlobalJwtVerifier result = apiInstance.updateGlobalJwtVerifier(verifierId, globalJwtVerifier);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JwtVerifiersApi#updateGlobalJwtVerifier");
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
| **verifierId** | **String**| The jwt verifier id | |
| **globalJwtVerifier** | [**GlobalJwtVerifier**](GlobalJwtVerifier.md)|  | [optional] |

### Return type

[**GlobalJwtVerifier**](GlobalJwtVerifier.md)

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

