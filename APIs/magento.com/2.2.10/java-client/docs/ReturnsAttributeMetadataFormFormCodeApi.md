# ReturnsAttributeMetadataFormFormCodeApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**rmaRmaAttributesManagementV1GetAttributesGet**](ReturnsAttributeMetadataFormFormCodeApi.md#rmaRmaAttributesManagementV1GetAttributesGet) | **GET** /V1/returnsAttributeMetadata/form/{formCode} | returnsAttributeMetadata/form/{formCode} |


<a id="rmaRmaAttributesManagementV1GetAttributesGet"></a>
# **rmaRmaAttributesManagementV1GetAttributesGet**
> List&lt;CustomerDataAttributeMetadataInterface&gt; rmaRmaAttributesManagementV1GetAttributesGet(formCode)

returnsAttributeMetadata/form/{formCode}

Retrieve all attributes filtered by form code

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReturnsAttributeMetadataFormFormCodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ReturnsAttributeMetadataFormFormCodeApi apiInstance = new ReturnsAttributeMetadataFormFormCodeApi(defaultClient);
    String formCode = "formCode_example"; // String | 
    try {
      List<CustomerDataAttributeMetadataInterface> result = apiInstance.rmaRmaAttributesManagementV1GetAttributesGet(formCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReturnsAttributeMetadataFormFormCodeApi#rmaRmaAttributesManagementV1GetAttributesGet");
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
| **formCode** | **String**|  | |

### Return type

[**List&lt;CustomerDataAttributeMetadataInterface&gt;**](CustomerDataAttributeMetadataInterface.md)

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

