# VendorApi

All URIs are relative to *https://discovery.gsa.gov*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getVendorGET**](VendorApi.md#getVendorGET) | **GET** /api/vendor/{duns} | This endpoint returns a single vendor by their 9 digit DUNS number |


<a id="getVendorGET"></a>
# **getVendorGET**
> Object getVendorGET(duns)

This endpoint returns a single vendor by their 9 digit DUNS number

&lt;p&gt;This endpoint returns a single vendor by their 9 digit DUNS number. DUNS numbers can be looked up in the &lt;a href&#x3D;\&quot;https://www.sam.gov\&quot;&gt;System for Award Management&lt;/a&gt; by vendor name.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VendorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://discovery.gsa.gov");

    VendorApi apiInstance = new VendorApi(defaultClient);
    String duns = "duns_example"; // String | a nine digit DUNS number that uniquely identifies the vendor (required)
    try {
      Object result = apiInstance.getVendorGET(duns);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VendorApi#getVendorGET");
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
| **duns** | **String**| a nine digit DUNS number that uniquely identifies the vendor (required) | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

