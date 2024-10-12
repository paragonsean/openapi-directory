# CustomerGroupsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**customerGroupRepositoryV1SavePost**](CustomerGroupsApi.md#customerGroupRepositoryV1SavePost) | **POST** /V1/customerGroups | customerGroups |


<a id="customerGroupRepositoryV1SavePost"></a>
# **customerGroupRepositoryV1SavePost**
> CustomerDataGroupInterface customerGroupRepositoryV1SavePost(customerGroupRepositoryV1SavePostRequest)

customerGroups

Save customer group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CustomerGroupsApi apiInstance = new CustomerGroupsApi(defaultClient);
    CustomerGroupRepositoryV1SavePostRequest customerGroupRepositoryV1SavePostRequest = new CustomerGroupRepositoryV1SavePostRequest(); // CustomerGroupRepositoryV1SavePostRequest | 
    try {
      CustomerDataGroupInterface result = apiInstance.customerGroupRepositoryV1SavePost(customerGroupRepositoryV1SavePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerGroupsApi#customerGroupRepositoryV1SavePost");
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
| **customerGroupRepositoryV1SavePostRequest** | [**CustomerGroupRepositoryV1SavePostRequest**](CustomerGroupRepositoryV1SavePostRequest.md)|  | [optional] |

### Return type

[**CustomerDataGroupInterface**](CustomerDataGroupInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **400** | 400 Bad Request |  -  |
| **401** | 401 Unauthorized |  -  |
| **500** | Internal Server error |  -  |
| **0** | Unexpected error |  -  |

