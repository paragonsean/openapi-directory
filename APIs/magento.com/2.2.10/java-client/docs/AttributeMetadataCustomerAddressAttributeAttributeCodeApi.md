# AttributeMetadataCustomerAddressAttributeAttributeCodeApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**customerAddressMetadataV1GetAttributeMetadataGet**](AttributeMetadataCustomerAddressAttributeAttributeCodeApi.md#customerAddressMetadataV1GetAttributeMetadataGet) | **GET** /V1/attributeMetadata/customerAddress/attribute/{attributeCode} | attributeMetadata/customerAddress/attribute/{attributeCode} |


<a id="customerAddressMetadataV1GetAttributeMetadataGet"></a>
# **customerAddressMetadataV1GetAttributeMetadataGet**
> CustomerDataAttributeMetadataInterface customerAddressMetadataV1GetAttributeMetadataGet(attributeCode)

attributeMetadata/customerAddress/attribute/{attributeCode}

Retrieve attribute metadata.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttributeMetadataCustomerAddressAttributeAttributeCodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    AttributeMetadataCustomerAddressAttributeAttributeCodeApi apiInstance = new AttributeMetadataCustomerAddressAttributeAttributeCodeApi(defaultClient);
    String attributeCode = "attributeCode_example"; // String | 
    try {
      CustomerDataAttributeMetadataInterface result = apiInstance.customerAddressMetadataV1GetAttributeMetadataGet(attributeCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttributeMetadataCustomerAddressAttributeAttributeCodeApi#customerAddressMetadataV1GetAttributeMetadataGet");
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

