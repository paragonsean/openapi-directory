# LookupApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV20LookupBarcodeGet**](LookupApi.md#apiV20LookupBarcodeGet) | **GET** /api/v2.0/lookup/{barcode} |  |
| [**apiV20LookupBarcodePost**](LookupApi.md#apiV20LookupBarcodePost) | **POST** /api/v2.0/lookup/{barcode} |  |
| [**apiV20LookupGet**](LookupApi.md#apiV20LookupGet) | **GET** /api/v2.0/lookup |  |


<a id="apiV20LookupBarcodeGet"></a>
# **apiV20LookupBarcodeGet**
> apiV20LookupBarcodeGet(barcode)



Generic endpoint for lookup of barcodes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LookupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    LookupApi apiInstance = new LookupApi(defaultClient);
    String barcode = "barcode_example"; // String | Unique barcode for Traces records, <database prefix>_<ID code>_<Table code> e.g. SAL_AA0001AA_ST
    try {
      apiInstance.apiV20LookupBarcodeGet(barcode);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookupApi#apiV20LookupBarcodeGet");
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
| **barcode** | **String**| Unique barcode for Traces records, &lt;database prefix&gt;_&lt;ID code&gt;_&lt;Table code&gt; e.g. SAL_AA0001AA_ST | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A lookup object |  -  |
| **403** | Unauthorised access for this specific resource or data |  -  |

<a id="apiV20LookupBarcodePost"></a>
# **apiV20LookupBarcodePost**
> apiV20LookupBarcodePost(barcode, apiV20LookupBarcodePostRequest)



Generic endpoint for lookup of barcodes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LookupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    LookupApi apiInstance = new LookupApi(defaultClient);
    String barcode = "barcode_example"; // String | Unique barcode for Traces records, <database prefix>_<ID code>_<Table code> e.g. SAL_AA0001AA_ST
    ApiV20LookupBarcodePostRequest apiV20LookupBarcodePostRequest = new ApiV20LookupBarcodePostRequest(); // ApiV20LookupBarcodePostRequest | 
    try {
      apiInstance.apiV20LookupBarcodePost(barcode, apiV20LookupBarcodePostRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookupApi#apiV20LookupBarcodePost");
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
| **barcode** | **String**| Unique barcode for Traces records, &lt;database prefix&gt;_&lt;ID code&gt;_&lt;Table code&gt; e.g. SAL_AA0001AA_ST | |
| **apiV20LookupBarcodePostRequest** | [**ApiV20LookupBarcodePostRequest**](ApiV20LookupBarcodePostRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A lookup object |  -  |
| **403** | Unauthorised access for this specific resource or data |  -  |

<a id="apiV20LookupGet"></a>
# **apiV20LookupGet**
> apiV20LookupGet(barcode)



Generic endpoint for lookup list of barcodes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LookupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    LookupApi apiInstance = new LookupApi(defaultClient);
    String barcode = "barcode_example"; // String | Unique barcode for Traces records, <database prefix>_<ID code>_<Table code> e.g. SAL_AA0001AA_ST
    try {
      apiInstance.apiV20LookupGet(barcode);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookupApi#apiV20LookupGet");
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
| **barcode** | **String**| Unique barcode for Traces records, &lt;database prefix&gt;_&lt;ID code&gt;_&lt;Table code&gt; e.g. SAL_AA0001AA_ST | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of lookup objects |  -  |
| **403** | Unauthorised access for this specific resource or data |  -  |
| **408** | Connection timeout, please try again later. |  -  |

