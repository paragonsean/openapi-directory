# AppsApi

All URIs are relative to *http://mastodon.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV1AppsPost**](AppsApi.md#apiV1AppsPost) | **POST** /api/v1/apps |  |
| [**apiV1AppsVerifyCredentialsGet**](AppsApi.md#apiV1AppsVerifyCredentialsGet) | **GET** /api/v1/apps/verify_credentials |  |


<a id="apiV1AppsPost"></a>
# **apiV1AppsPost**
> ApiV1AppsPost200Response apiV1AppsPost(apiV1AppsPostRequest)



Create a new application to obtain OAuth2 credentials.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");

    AppsApi apiInstance = new AppsApi(defaultClient);
    ApiV1AppsPostRequest apiV1AppsPostRequest = new ApiV1AppsPostRequest(); // ApiV1AppsPostRequest | 
    try {
      ApiV1AppsPost200Response result = apiInstance.apiV1AppsPost(apiV1AppsPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#apiV1AppsPost");
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
| **apiV1AppsPostRequest** | [**ApiV1AppsPostRequest**](ApiV1AppsPostRequest.md)|  | [optional] |

### Return type

[**ApiV1AppsPost200Response**](ApiV1AppsPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **422** | If a required parameter is missing or improperly formatted, the request will fail. |  -  |

<a id="apiV1AppsVerifyCredentialsGet"></a>
# **apiV1AppsVerifyCredentialsGet**
> Application apiV1AppsVerifyCredentialsGet()



Confirm that the app&#39;s OAuth2 credentials work.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    AppsApi apiInstance = new AppsApi(defaultClient);
    try {
      Application result = apiInstance.apiV1AppsVerifyCredentialsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#apiV1AppsVerifyCredentialsGet");
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

[**Application**](Application.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | If the Authorization header was provided with a valid token, you should see your app returned as an Application entity. |  -  |
| **401** | If the Authorization header contains an invalid token, is malformed, or is not present, an error will be returned indicating an authorization failure. |  -  |

