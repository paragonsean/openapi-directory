# StatusApi

All URIs are relative to *https://tl-api.azurewebsites.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**statusGet**](StatusApi.md#statusGet) | **GET** /api/Status | Get the current status of message |


<a id="statusGet"></a>
# **statusGet**
> MessageStatus statusGet(messageId)

Get the current status of message

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatusApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tl-api.azurewebsites.net");
    
    // Configure OAuth2 access token for authorization: bearer
    OAuth bearer = (OAuth) defaultClient.getAuthentication("bearer");
    bearer.setAccessToken("YOUR ACCESS TOKEN");

    StatusApi apiInstance = new StatusApi(defaultClient);
    String messageId = "messageId_example"; // String | respose of POST request
    try {
      MessageStatus result = apiInstance.statusGet(messageId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatusApi#statusGet");
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
| **messageId** | **String**| respose of POST request | [optional] |

### Return type

[**MessageStatus**](MessageStatus.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | same response result will retrun with different status and messageText |  -  |
| **404** |  |  -  |

