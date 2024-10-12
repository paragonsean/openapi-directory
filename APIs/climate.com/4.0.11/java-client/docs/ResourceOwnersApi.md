# ResourceOwnersApi

All URIs are relative to *https://platform.climate.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getResourceOwner**](ResourceOwnersApi.md#getResourceOwner) | **GET** /v4/resourceOwners/{resourceOwnerId} | Retrieve a resource owner by ID |


<a id="getResourceOwner"></a>
# **getResourceOwner**
> ResourceOwner getResourceOwner(resourceOwnerId)

Retrieve a resource owner by ID

Retrieve a resource owner for the given &#x60;resourceOwnerId&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourceOwnersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://platform.climate.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2_authorization_code
    OAuth oauth2_authorization_code = (OAuth) defaultClient.getAuthentication("oauth2_authorization_code");
    oauth2_authorization_code.setAccessToken("YOUR ACCESS TOKEN");

    ResourceOwnersApi apiInstance = new ResourceOwnersApi(defaultClient);
    UUID resourceOwnerId = UUID.randomUUID(); // UUID | Unique identifier of the resource owner.
    try {
      ResourceOwner result = apiInstance.getResourceOwner(resourceOwnerId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceOwnersApi#getResourceOwner");
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
| **resourceOwnerId** | **UUID**| Unique identifier of the resource owner. | |

### Return type

[**ResourceOwner**](ResourceOwner.md)

### Authorization

[api_key](../README.md#api_key), [oauth2_authorization_code](../README.md#oauth2_authorization_code)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Input |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **404** | Not Found |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **500** | Internal Server Error |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |

