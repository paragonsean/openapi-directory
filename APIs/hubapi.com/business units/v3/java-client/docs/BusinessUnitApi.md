# BusinessUnitApi

All URIs are relative to *https://api.hubapi.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getBusinessUnitsV3BusinessUnitsUserUserIdGetByUserID**](BusinessUnitApi.md#getBusinessUnitsV3BusinessUnitsUserUserIdGetByUserID) | **GET** /business-units/v3/business-units/user/{userId} | Get Business Units for a user |


<a id="getBusinessUnitsV3BusinessUnitsUserUserIdGetByUserID"></a>
# **getBusinessUnitsV3BusinessUnitsUserUserIdGetByUserID**
> CollectionResponsePublicBusinessUnitNoPaging getBusinessUnitsV3BusinessUnitsUserUserIdGetByUserID(userId, properties, name)

Get Business Units for a user

Get Business Units identified by &#x60;userId&#x60;. The &#x60;userId&#x60; refers to the user’s ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BusinessUnitApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hubapi.com");
    
    // Configure OAuth2 access token for authorization: oauth2_legacy
    OAuth oauth2_legacy = (OAuth) defaultClient.getAuthentication("oauth2_legacy");
    oauth2_legacy.setAccessToken("YOUR ACCESS TOKEN");

    // Configure API key authorization: private_apps_legacy
    ApiKeyAuth private_apps_legacy = (ApiKeyAuth) defaultClient.getAuthentication("private_apps_legacy");
    private_apps_legacy.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_apps_legacy.setApiKeyPrefix("Token");

    BusinessUnitApi apiInstance = new BusinessUnitApi(defaultClient);
    String userId = "userId_example"; // String | Identifier of user to retrieve.
    List<String> properties = Arrays.asList(); // List<String> | The names of properties to optionally include in the response body. The only valid value is `logoMetadata`.
    List<String> name = Arrays.asList(); // List<String> | The names of Business Units to retrieve. If empty or not provided, then all associated Business Units will be returned.
    try {
      CollectionResponsePublicBusinessUnitNoPaging result = apiInstance.getBusinessUnitsV3BusinessUnitsUserUserIdGetByUserID(userId, properties, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BusinessUnitApi#getBusinessUnitsV3BusinessUnitsUserUserIdGetByUserID");
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
| **userId** | **String**| Identifier of user to retrieve. | |
| **properties** | [**List&lt;String&gt;**](String.md)| The names of properties to optionally include in the response body. The only valid value is &#x60;logoMetadata&#x60;. | [optional] |
| **name** | [**List&lt;String&gt;**](String.md)| The names of Business Units to retrieve. If empty or not provided, then all associated Business Units will be returned. | [optional] |

### Return type

[**CollectionResponsePublicBusinessUnitNoPaging**](CollectionResponsePublicBusinessUnitNoPaging.md)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | An error occurred. |  -  |

