# AttributeMetadataCustomerAddressCustomApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**customerAddressMetadataV1GetCustomAttributesMetadataGet**](AttributeMetadataCustomerAddressCustomApi.md#customerAddressMetadataV1GetCustomAttributesMetadataGet) | **GET** /V1/attributeMetadata/customerAddress/custom | attributeMetadata/customerAddress/custom |


<a id="customerAddressMetadataV1GetCustomAttributesMetadataGet"></a>
# **customerAddressMetadataV1GetCustomAttributesMetadataGet**
> List&lt;CustomerDataAttributeMetadataInterface&gt; customerAddressMetadataV1GetCustomAttributesMetadataGet(dataInterfaceName)

attributeMetadata/customerAddress/custom

Get custom attributes metadata for the given data interface.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttributeMetadataCustomerAddressCustomApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    AttributeMetadataCustomerAddressCustomApi apiInstance = new AttributeMetadataCustomerAddressCustomApi(defaultClient);
    String dataInterfaceName = "dataInterfaceName_example"; // String | 
    try {
      List<CustomerDataAttributeMetadataInterface> result = apiInstance.customerAddressMetadataV1GetCustomAttributesMetadataGet(dataInterfaceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttributeMetadataCustomerAddressCustomApi#customerAddressMetadataV1GetCustomAttributesMetadataGet");
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
| **dataInterfaceName** | **String**|  | [optional] |

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
| **500** | Internal Server error |  -  |
| **0** | Unexpected error |  -  |

