# CreditmemoApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**salesCreditmemoRepositoryV1SavePost**](CreditmemoApi.md#salesCreditmemoRepositoryV1SavePost) | **POST** /V1/creditmemo | creditmemo |


<a id="salesCreditmemoRepositoryV1SavePost"></a>
# **salesCreditmemoRepositoryV1SavePost**
> SalesDataCreditmemoInterface salesCreditmemoRepositoryV1SavePost(salesCreditmemoRepositoryV1SavePostRequest)

creditmemo

Performs persist operations for a specified credit memo.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CreditmemoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CreditmemoApi apiInstance = new CreditmemoApi(defaultClient);
    SalesCreditmemoRepositoryV1SavePostRequest salesCreditmemoRepositoryV1SavePostRequest = new SalesCreditmemoRepositoryV1SavePostRequest(); // SalesCreditmemoRepositoryV1SavePostRequest | 
    try {
      SalesDataCreditmemoInterface result = apiInstance.salesCreditmemoRepositoryV1SavePost(salesCreditmemoRepositoryV1SavePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CreditmemoApi#salesCreditmemoRepositoryV1SavePost");
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
| **salesCreditmemoRepositoryV1SavePostRequest** | [**SalesCreditmemoRepositoryV1SavePostRequest**](SalesCreditmemoRepositoryV1SavePostRequest.md)|  | [optional] |

### Return type

[**SalesDataCreditmemoInterface**](SalesDataCreditmemoInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

