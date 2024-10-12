# AttributeMetadataCustomerAttributeAttributeCodeApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**customerCustomerMetadataV1GetAttributeMetadataGet**](AttributeMetadataCustomerAttributeAttributeCodeApi.md#customerCustomerMetadataV1GetAttributeMetadataGet) | **GET** /V1/attributeMetadata/customer/attribute/{attributeCode} | attributeMetadata/customer/attribute/{attributeCode} |


<a id="customerCustomerMetadataV1GetAttributeMetadataGet"></a>
# **customerCustomerMetadataV1GetAttributeMetadataGet**
> CustomerDataAttributeMetadataInterface customerCustomerMetadataV1GetAttributeMetadataGet(attributeCode)

attributeMetadata/customer/attribute/{attributeCode}

Retrieve attribute metadata.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttributeMetadataCustomerAttributeAttributeCodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    AttributeMetadataCustomerAttributeAttributeCodeApi apiInstance = new AttributeMetadataCustomerAttributeAttributeCodeApi(defaultClient);
    String attributeCode = "attributeCode_example"; // String | 
    try {
      CustomerDataAttributeMetadataInterface result = apiInstance.customerCustomerMetadataV1GetAttributeMetadataGet(attributeCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttributeMetadataCustomerAttributeAttributeCodeApi#customerCustomerMetadataV1GetAttributeMetadataGet");
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
| **attributeCode** | **String**|  | |

### Return type

[**CustomerDataAttributeMetadataInterface**](CustomerDataAttributeMetadataInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **400** | 400 Bad Request |  -  |
| **401** | 401 Unauthorized |  -  |
| **500** | Internal Server error |  -  |
| **0** | Unexpected error |  -  |

