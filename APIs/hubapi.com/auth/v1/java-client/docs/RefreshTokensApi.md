# RefreshTokensApi

All URIs are relative to *https://api.hubapi.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteOauthV1RefreshTokensTokenArchive**](RefreshTokensApi.md#deleteOauthV1RefreshTokensTokenArchive) | **DELETE** /oauth/v1/refresh-tokens/{token} |  |
| [**getOauthV1RefreshTokensTokenGet**](RefreshTokensApi.md#getOauthV1RefreshTokensTokenGet) | **GET** /oauth/v1/refresh-tokens/{token} |  |


<a id="deleteOauthV1RefreshTokensTokenArchive"></a>
# **deleteOauthV1RefreshTokensTokenArchive**
> deleteOauthV1RefreshTokensTokenArchive(token)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RefreshTokensApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hubapi.com");

    RefreshTokensApi apiInstance = new RefreshTokensApi(defaultClient);
    String token = "token_example"; // String | 
    try {
      apiInstance.deleteOauthV1RefreshTokensTokenArchive(token);
    } catch (ApiException e) {
      System.err.println("Exception when calling RefreshTokensApi#deleteOauthV1RefreshTokensTokenArchive");
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
| **token** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No content |  -  |
| **0** | An error occurred. |  -  |

<a id="getOauthV1RefreshTokensTokenGet"></a>
# **getOauthV1RefreshTokensTokenGet**
> RefreshTokenInfoResponse getOauthV1RefreshTokensTokenGet(token)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RefreshTokensApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hubapi.com");

    RefreshTokensApi apiInstance = new RefreshTokensApi(defaultClient);
    String token = "token_example"; // String | 
    try {
      RefreshTokenInfoResponse result = apiInstance.getOauthV1RefreshTokensTokenGet(token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RefreshTokensApi#getOauthV1RefreshTokensTokenGet");
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
| **token** | **String**|  | |

### Return type

[**RefreshTokenInfoResponse**](RefreshTokenInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | An error occurred. |  -  |

