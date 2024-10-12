# CustomerRightsApi

All URIs are relative to *https://api.beezup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getRights**](CustomerRightsApi.md#getRights) | **GET** /v2/user/customer/stores/{storeId}/rights | Get store&#39;s rights |


<a id="getRights"></a>
# **getRights**
> List&lt;FunctionalityRightInfo&gt; getRights(storeId)

Get store&#39;s rights

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerRightsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CustomerRightsApi apiInstance = new CustomerRightsApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    try {
      List<FunctionalityRightInfo> result = apiInstance.getRights(storeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerRightsApi#getRights");
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
| **storeId** | **String**| Your store identifier | |

### Return type

[**List&lt;FunctionalityRightInfo&gt;**](FunctionalityRightInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The store&#39;s rights |  -  |
| **404** | Store not found or not authorized |  -  |
| **0** | Occurs when something goes wrong |  -  |

