# SendApi

All URIs are relative to *https://api.mailscript.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**send**](SendApi.md#send) | **POST** /send | Send an email |


<a id="send"></a>
# **send**
> send(sendRequest)

Send an email

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SendApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mailscript.com/v2");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    SendApi apiInstance = new SendApi(defaultClient);
    SendRequest sendRequest = new SendRequest(); // SendRequest | request body
    try {
      apiInstance.send(sendRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling SendApi#send");
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
| **sendRequest** | [**SendRequest**](SendRequest.md)| request body | |

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid input |  -  |
| **403** | Bad credentials |  -  |

