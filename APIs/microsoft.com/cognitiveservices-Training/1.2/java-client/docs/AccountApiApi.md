# AccountApiApi

All URIs are relative to *https://southcentralus.api.cognitive.microsoft.com/customvision/v1.2/Training*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAccountInfo**](AccountApiApi.md#getAccountInfo) | **GET** /account | Get basic information about your account |


<a id="getAccountInfo"></a>
# **getAccountInfo**
> Account getAccountInfo(trainingKey)

Get basic information about your account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v1.2/Training");

    AccountApiApi apiInstance = new AccountApiApi(defaultClient);
    String trainingKey = "{API Key}"; // String | 
    try {
      Account result = apiInstance.getAccountInfo(trainingKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApiApi#getAccountInfo");
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
| **trainingKey** | **String**|  | |

### Return type

[**Account**](Account.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

