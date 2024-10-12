# AccessTokensApi

All URIs are relative to *https://hub.docker.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v2AccessTokensGet**](AccessTokensApi.md#v2AccessTokensGet) | **GET** /v2/access-tokens | Get a list of personal access tokens |
| [**v2AccessTokensPost**](AccessTokensApi.md#v2AccessTokensPost) | **POST** /v2/access-tokens | Create a personal access token |
| [**v2AccessTokensUuidDelete**](AccessTokensApi.md#v2AccessTokensUuidDelete) | **DELETE** /v2/access-tokens/{uuid} | Delete a personal access token |
| [**v2AccessTokensUuidGet**](AccessTokensApi.md#v2AccessTokensUuidGet) | **GET** /v2/access-tokens/{uuid} | Get a personal access token |
| [**v2AccessTokensUuidPatch**](AccessTokensApi.md#v2AccessTokensUuidPatch) | **PATCH** /v2/access-tokens/{uuid} | Update a personal access token |


<a id="v2AccessTokensGet"></a>
# **v2AccessTokensGet**
> GetAccessTokensResponse v2AccessTokensGet(page, pageSize)

Get a list of personal access tokens

Returns a paginated list of personal access tokens.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccessTokensApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://hub.docker.com");

    AccessTokensApi apiInstance = new AccessTokensApi(defaultClient);
    BigDecimal page = new BigDecimal("1"); // BigDecimal | 
    BigDecimal pageSize = new BigDecimal("10"); // BigDecimal | 
    try {
      GetAccessTokensResponse result = apiInstance.v2AccessTokensGet(page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccessTokensApi#v2AccessTokensGet");
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
| **page** | **BigDecimal**|  | [optional] [default to 1] |
| **pageSize** | **BigDecimal**|  | [optional] [default to 10] |

### Return type

[**GetAccessTokensResponse**](GetAccessTokensResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |

<a id="v2AccessTokensPost"></a>
# **v2AccessTokensPost**
> AccessToken v2AccessTokensPost(createAccessTokenRequest)

Create a personal access token

Creates and returns a personal access token.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccessTokensApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://hub.docker.com");

    AccessTokensApi apiInstance = new AccessTokensApi(defaultClient);
    CreateAccessTokenRequest createAccessTokenRequest = new CreateAccessTokenRequest(); // CreateAccessTokenRequest | 
    try {
      AccessToken result = apiInstance.v2AccessTokensPost(createAccessTokenRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccessTokensApi#v2AccessTokensPost");
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
| **createAccessTokenRequest** | [**CreateAccessTokenRequest**](CreateAccessTokenRequest.md)|  | |

### Return type

[**AccessToken**](AccessToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |

<a id="v2AccessTokensUuidDelete"></a>
# **v2AccessTokensUuidDelete**
> v2AccessTokensUuidDelete(uuid)

Delete a personal access token

Deletes a personal access token permanently. This cannot be undone. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccessTokensApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://hub.docker.com");

    AccessTokensApi apiInstance = new AccessTokensApi(defaultClient);
    String uuid = "uuid_example"; // String | 
    try {
      apiInstance.v2AccessTokensUuidDelete(uuid);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccessTokensApi#v2AccessTokensUuidDelete");
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
| **uuid** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | A successful response. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

<a id="v2AccessTokensUuidGet"></a>
# **v2AccessTokensUuidGet**
> V2AccessTokensUuidGet200Response v2AccessTokensUuidGet(uuid)

Get a personal access token

Returns a personal access token by UUID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccessTokensApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://hub.docker.com");

    AccessTokensApi apiInstance = new AccessTokensApi(defaultClient);
    String uuid = "uuid_example"; // String | 
    try {
      V2AccessTokensUuidGet200Response result = apiInstance.v2AccessTokensUuidGet(uuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccessTokensApi#v2AccessTokensUuidGet");
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
| **uuid** | **String**|  | |

### Return type

[**V2AccessTokensUuidGet200Response**](V2AccessTokensUuidGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

<a id="v2AccessTokensUuidPatch"></a>
# **v2AccessTokensUuidPatch**
> AccessToken v2AccessTokensUuidPatch(uuid, patchAccessTokenRequest)

Update a personal access token

Updates a personal access token partially. You can either update the token&#39;s label or enable/disable it. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccessTokensApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://hub.docker.com");

    AccessTokensApi apiInstance = new AccessTokensApi(defaultClient);
    String uuid = "uuid_example"; // String | 
    PatchAccessTokenRequest patchAccessTokenRequest = new PatchAccessTokenRequest(); // PatchAccessTokenRequest | 
    try {
      AccessToken result = apiInstance.v2AccessTokensUuidPatch(uuid, patchAccessTokenRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccessTokensApi#v2AccessTokensUuidPatch");
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
| **uuid** | **String**|  | |
| **patchAccessTokenRequest** | [**PatchAccessTokenRequest**](PatchAccessTokenRequest.md)|  | |

### Return type

[**AccessToken**](AccessToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |

