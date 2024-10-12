# MerakiAuthUsersApi

All URIs are relative to *https://api.meraki.com/api/v0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getNetworkMerakiAuthUser**](MerakiAuthUsersApi.md#getNetworkMerakiAuthUser) | **GET** /networks/{networkId}/merakiAuthUsers/{merakiAuthUserId} | Return the Meraki Auth splash or RADIUS user |
| [**getNetworkMerakiAuthUsers**](MerakiAuthUsersApi.md#getNetworkMerakiAuthUsers) | **GET** /networks/{networkId}/merakiAuthUsers | List the splash or RADIUS users configured under Meraki Authentication for a network |


<a id="getNetworkMerakiAuthUser"></a>
# **getNetworkMerakiAuthUser**
> Object getNetworkMerakiAuthUser(networkId, merakiAuthUserId)

Return the Meraki Auth splash or RADIUS user

Return the Meraki Auth splash or RADIUS user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MerakiAuthUsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    MerakiAuthUsersApi apiInstance = new MerakiAuthUsersApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String merakiAuthUserId = "merakiAuthUserId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkMerakiAuthUser(networkId, merakiAuthUserId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MerakiAuthUsersApi#getNetworkMerakiAuthUser");
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
| **networkId** | **String**|  | |
| **merakiAuthUserId** | **String**|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkMerakiAuthUsers"></a>
# **getNetworkMerakiAuthUsers**
> List&lt;Object&gt; getNetworkMerakiAuthUsers(networkId)

List the splash or RADIUS users configured under Meraki Authentication for a network

List the splash or RADIUS users configured under Meraki Authentication for a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MerakiAuthUsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    MerakiAuthUsersApi apiInstance = new MerakiAuthUsersApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<Object> result = apiInstance.getNetworkMerakiAuthUsers(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MerakiAuthUsersApi#getNetworkMerakiAuthUsers");
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
| **networkId** | **String**|  | |

### Return type

**List&lt;Object&gt;**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

