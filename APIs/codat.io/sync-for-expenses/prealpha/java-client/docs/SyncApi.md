# SyncApi

All URIs are relative to *https://api.codat.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**intiateSync**](SyncApi.md#intiateSync) | **POST** /companies/{companyId}/sync/expenses/syncs | Initiate sync |


<a id="intiateSync"></a>
# **intiateSync**
> SyncInitiated intiateSync(companyId, postSync)

Initiate sync

Initiate sync of pending transactions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.codat.io");
    
    // Configure API key authorization: auth_header
    ApiKeyAuth auth_header = (ApiKeyAuth) defaultClient.getAuthentication("auth_header");
    auth_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //auth_header.setApiKeyPrefix("Token");

    SyncApi apiInstance = new SyncApi(defaultClient);
    UUID companyId = UUID.fromString("8a210b68-6988-11ed-a1eb-0242ac120002"); // UUID | 
    PostSync postSync = new PostSync(); // PostSync | 
    try {
      SyncInitiated result = apiInstance.intiateSync(companyId, postSync);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncApi#intiateSync");
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
| **companyId** | **UUID**|  | |
| **postSync** | [**PostSync**](PostSync.md)|  | [optional] |

### Return type

[**SyncInitiated**](SyncInitiated.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Returns the newly created SyncId |  -  |
| **400** | If model is incorrect |  -  |
| **404** | If company not found |  -  |
| **422** | If the specified company does not have a valid set of DataConnections setup |  -  |

