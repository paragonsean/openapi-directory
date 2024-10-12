# MerchantIndustriesApi

All URIs are relative to *https://api.openfintech.io/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**merchantIndustriesGet**](MerchantIndustriesApi.md#merchantIndustriesGet) | **GET** /merchant-industries | List of merchant industries |
| [**merchantIndustriesIdGet**](MerchantIndustriesApi.md#merchantIndustriesIdGet) | **GET** /merchant-industries/{id} | Merchant industry by ID |


<a id="merchantIndustriesGet"></a>
# **merchantIndustriesGet**
> MerchantIndustriesResponse merchantIndustriesGet(pageNumber, pageSize, filterName)

List of merchant industries

Returns all available merchant fields of activity. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MerchantIndustriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.openfintech.io/v1");

    MerchantIndustriesApi apiInstance = new MerchantIndustriesApi(defaultClient);
    Integer pageNumber = 56; // Integer | Current page number.
    Integer pageSize = 56; // Integer | Page size.<br>*Default value: 100* 
    String filterName = "filterName_example"; // String | Filtering by name.
    try {
      MerchantIndustriesResponse result = apiInstance.merchantIndustriesGet(pageNumber, pageSize, filterName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MerchantIndustriesApi#merchantIndustriesGet");
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
| **pageNumber** | **Integer**| Current page number. | [optional] |
| **pageSize** | **Integer**| Page size.&lt;br&gt;*Default value: 100*  | [optional] |
| **filterName** | **String**| Filtering by name. | [optional] |

### Return type

[**MerchantIndustriesResponse**](MerchantIndustriesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of Merchant industries. |  -  |

<a id="merchantIndustriesIdGet"></a>
# **merchantIndustriesIdGet**
> MerchantIndustryResponse merchantIndustriesIdGet(id)

Merchant industry by ID

Returns merchant industry with specific ID. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MerchantIndustriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.openfintech.io/v1");

    MerchantIndustriesApi apiInstance = new MerchantIndustriesApi(defaultClient);
    String id = "id_example"; // String | Unique ID.
    try {
      MerchantIndustryResponse result = apiInstance.merchantIndustriesIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MerchantIndustriesApi#merchantIndustriesIdGet");
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
| **id** | **String**| Unique ID. | |

### Return type

[**MerchantIndustryResponse**](MerchantIndustryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Merchant industry. |  -  |
| **404** | Merchant industry ID is not valid. |  -  |

