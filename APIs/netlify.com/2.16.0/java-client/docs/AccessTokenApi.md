# AccessTokenApi

All URIs are relative to *https://api.netlify.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**exchangeTicket**](AccessTokenApi.md#exchangeTicket) | **POST** /oauth/tickets/{ticket_id}/exchange |  |


<a id="exchangeTicket"></a>
# **exchangeTicket**
> AccessToken exchangeTicket(ticketId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccessTokenApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    AccessTokenApi apiInstance = new AccessTokenApi(defaultClient);
    String ticketId = "ticketId_example"; // String | 
    try {
      AccessToken result = apiInstance.exchangeTicket(ticketId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccessTokenApi#exchangeTicket");
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
| **ticketId** | **String**|  | |

### Return type

[**AccessToken**](AccessToken.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | ok |  -  |
| **0** | error |  -  |

