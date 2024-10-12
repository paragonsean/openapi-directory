# CreditmemoRefundApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**salesCreditmemoManagementV1RefundPost**](CreditmemoRefundApi.md#salesCreditmemoManagementV1RefundPost) | **POST** /V1/creditmemo/refund | creditmemo/refund |


<a id="salesCreditmemoManagementV1RefundPost"></a>
# **salesCreditmemoManagementV1RefundPost**
> SalesDataCreditmemoInterface salesCreditmemoManagementV1RefundPost(salesCreditmemoManagementV1RefundPostRequest)

creditmemo/refund

Prepare creditmemo to refund and save it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CreditmemoRefundApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CreditmemoRefundApi apiInstance = new CreditmemoRefundApi(defaultClient);
    SalesCreditmemoManagementV1RefundPostRequest salesCreditmemoManagementV1RefundPostRequest = new SalesCreditmemoManagementV1RefundPostRequest(); // SalesCreditmemoManagementV1RefundPostRequest | 
    try {
      SalesDataCreditmemoInterface result = apiInstance.salesCreditmemoManagementV1RefundPost(salesCreditmemoManagementV1RefundPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CreditmemoRefundApi#salesCreditmemoManagementV1RefundPost");
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
| **salesCreditmemoManagementV1RefundPostRequest** | [**SalesCreditmemoManagementV1RefundPostRequest**](SalesCreditmemoManagementV1RefundPostRequest.md)|  | [optional] |

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

