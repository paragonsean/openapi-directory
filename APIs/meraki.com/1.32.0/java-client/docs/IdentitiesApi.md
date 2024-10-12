# IdentitiesApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAdministeredIdentitiesMe_1**](IdentitiesApi.md#getAdministeredIdentitiesMe_1) | **GET** /administered/identities/me | Returns the identity of the current user. |


<a id="getAdministeredIdentitiesMe_1"></a>
# **getAdministeredIdentitiesMe_1**
> GetAdministeredIdentitiesMe200Response getAdministeredIdentitiesMe_1()

Returns the identity of the current user.

Returns the identity of the current user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdentitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    IdentitiesApi apiInstance = new IdentitiesApi(defaultClient);
    try {
      GetAdministeredIdentitiesMe200Response result = apiInstance.getAdministeredIdentitiesMe_1();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdentitiesApi#getAdministeredIdentitiesMe_1");
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

[**GetAdministeredIdentitiesMe200Response**](GetAdministeredIdentitiesMe200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

