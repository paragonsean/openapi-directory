# Class3TransferApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**trasnfer**](Class3TransferApi.md#trasnfer) | **POST** /transfer |  |


<a id="trasnfer"></a>
# **trasnfer**
> trasnfer(authorization, body)



Transfer money between two accounts

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Class3TransferApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    Class3TransferApi apiInstance = new Class3TransferApi(defaultClient);
    String authorization = "authorization_example"; // String | Authorization token (provided upon successful login)
    Transfer body = new Transfer(); // Transfer | Transfer details including ammount, sender and receiver
    try {
      apiInstance.trasnfer(authorization, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling Class3TransferApi#trasnfer");
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
| **authorization** | **String**| Authorization token (provided upon successful login) | |
| **body** | [**Transfer**](Transfer.md)| Transfer details including ammount, sender and receiver | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **400** | Bad parameters: Please check provided values |  -  |
| **501** | Internal server error |  -  |

