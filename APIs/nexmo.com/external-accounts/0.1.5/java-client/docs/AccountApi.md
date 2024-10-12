# AccountApi

All URIs are relative to *https://api.nexmo.com/beta/chatapp-accounts*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAllAccounts**](AccountApi.md#getAllAccounts) | **GET** / | Retrieve all accounts you own |


<a id="getAllAccounts"></a>
# **getAllAccounts**
> GetAllAccounts200Response getAllAccounts(provider, pageNumber, pageSize)

Retrieve all accounts you own

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nexmo.com/beta/chatapp-accounts");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String provider = "messenger"; // String | Filter by provider
    Integer pageNumber = 1; // Integer | Page number of the results
    Integer pageSize = 20; // Integer | Page size of the results
    try {
      GetAllAccounts200Response result = apiInstance.getAllAccounts(provider, pageNumber, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#getAllAccounts");
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
| **provider** | **String**| Filter by provider | [optional] [enum: messenger, viber_service_msg, whatsapp] |
| **pageNumber** | **Integer**| Page number of the results | [optional] [default to 1] |
| **pageSize** | **Integer**| Page size of the results | [optional] [default to 20] |

### Return type

[**GetAllAccounts200Response**](GetAllAccounts200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |
| **401** | Unauthorized. |  -  |

