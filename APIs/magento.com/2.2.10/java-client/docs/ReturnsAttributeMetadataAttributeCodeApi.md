# ReturnsAttributeMetadataAttributeCodeApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**rmaRmaAttributesManagementV1GetAttributeMetadataGet**](ReturnsAttributeMetadataAttributeCodeApi.md#rmaRmaAttributesManagementV1GetAttributeMetadataGet) | **GET** /V1/returnsAttributeMetadata/{attributeCode} | returnsAttributeMetadata/{attributeCode} |


<a id="rmaRmaAttributesManagementV1GetAttributeMetadataGet"></a>
# **rmaRmaAttributesManagementV1GetAttributeMetadataGet**
> CustomerDataAttributeMetadataInterface rmaRmaAttributesManagementV1GetAttributeMetadataGet(attributeCode)

returnsAttributeMetadata/{attributeCode}

Retrieve attribute metadata.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReturnsAttributeMetadataAttributeCodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ReturnsAttributeMetadataAttributeCodeApi apiInstance = new ReturnsAttributeMetadataAttributeCodeApi(defaultClient);
    String attributeCode = "attributeCode_example"; // String | 
    try {
      CustomerDataAttributeMetadataInterface result = apiInstance.rmaRmaAttributesManagementV1GetAttributeMetadataGet(attributeCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReturnsAttributeMetadataAttributeCodeApi#rmaRmaAttributesManagementV1GetAttributeMetadataGet");
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
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

