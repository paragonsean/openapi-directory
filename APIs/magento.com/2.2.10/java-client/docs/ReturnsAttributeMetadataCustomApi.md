# ReturnsAttributeMetadataCustomApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**rmaRmaAttributesManagementV1GetCustomAttributesMetadataGet**](ReturnsAttributeMetadataCustomApi.md#rmaRmaAttributesManagementV1GetCustomAttributesMetadataGet) | **GET** /V1/returnsAttributeMetadata/custom | returnsAttributeMetadata/custom |


<a id="rmaRmaAttributesManagementV1GetCustomAttributesMetadataGet"></a>
# **rmaRmaAttributesManagementV1GetCustomAttributesMetadataGet**
> List&lt;FrameworkMetadataObjectInterface&gt; rmaRmaAttributesManagementV1GetCustomAttributesMetadataGet(dataObjectClassName)

returnsAttributeMetadata/custom

Get custom attribute metadata for the given Data object&#39;s attribute set

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReturnsAttributeMetadataCustomApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ReturnsAttributeMetadataCustomApi apiInstance = new ReturnsAttributeMetadataCustomApi(defaultClient);
    String dataObjectClassName = "dataObjectClassName_example"; // String | Data object class name
    try {
      List<FrameworkMetadataObjectInterface> result = apiInstance.rmaRmaAttributesManagementV1GetCustomAttributesMetadataGet(dataObjectClassName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReturnsAttributeMetadataCustomApi#rmaRmaAttributesManagementV1GetCustomAttributesMetadataGet");
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
| **dataObjectClassName** | **String**| Data object class name | [optional] |

### Return type

[**List&lt;FrameworkMetadataObjectInterface&gt;**](FrameworkMetadataObjectInterface.md)

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

