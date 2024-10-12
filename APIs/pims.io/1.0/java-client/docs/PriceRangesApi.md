# PriceRangesApi

All URIs are relative to *https://demo.pims.io/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchAllPriceRanges**](PriceRangesApi.md#fetchAllPriceRanges) | **GET** /price-ranges | Find all price ranges |
| [**fetchOnePriceRange**](PriceRangesApi.md#fetchOnePriceRange) | **GET** /price-ranges/{price_range_id} | Get one price range by ID |


<a id="fetchAllPriceRanges"></a>
# **fetchAllPriceRanges**
> List&lt;PriceRangesEntity&gt; fetchAllPriceRanges(label, showIgnored, sort, pageSize, acceptLanguage)

Find all price ranges

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PriceRangesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.pims.io/api/v1");
    
    // Configure HTTP basic authorization: Basic Auth
    HttpBasicAuth Basic Auth = (HttpBasicAuth) defaultClient.getAuthentication("Basic Auth");
    Basic Auth.setUsername("YOUR USERNAME");
    Basic Auth.setPassword("YOUR PASSWORD");

    PriceRangesApi apiInstance = new PriceRangesApi(defaultClient);
    String label = "label_example"; // String | Find only the price ranges whose label contains this value.
    Boolean showIgnored = false; // Boolean | If set to `false`, show only the price ranges which are not ignored. If set to `true`, show all price ranges.
    String sort = "label"; // String | Sort the price ranges in the corresponding order.
    Integer pageSize = 25; // Integer | Pagination size, i.e. maximum number of items to be displayed in the response.
    String acceptLanguage = "de"; // String | Language used for the translatable labels.
    try {
      List<PriceRangesEntity> result = apiInstance.fetchAllPriceRanges(label, showIgnored, sort, pageSize, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PriceRangesApi#fetchAllPriceRanges");
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
| **label** | **String**| Find only the price ranges whose label contains this value. | [optional] |
| **showIgnored** | **Boolean**| If set to &#x60;false&#x60;, show only the price ranges which are not ignored. If set to &#x60;true&#x60;, show all price ranges. | [optional] [default to false] |
| **sort** | **String**| Sort the price ranges in the corresponding order. | [optional] [default to label] [enum: label, -label, order, -order] |
| **pageSize** | **Integer**| Pagination size, i.e. maximum number of items to be displayed in the response. | [optional] [default to 25] |
| **acceptLanguage** | **String**| Language used for the translatable labels. | [optional] [default to en] [enum: de, en, fr] |

### Return type

[**List&lt;PriceRangesEntity&gt;**](PriceRangesEntity.md)

### Authorization

[Basic Auth](../README.md#Basic Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation, gives an array of price ranges |  -  |
| **401** | Unauthorized, no authentication was made |  -  |
| **403** | Forbidden, the authentication is wrong |  -  |
| **422** | Unprocessable Entity |  -  |
| **500** | Unexpected error |  -  |

<a id="fetchOnePriceRange"></a>
# **fetchOnePriceRange**
> VenuesEntity fetchOnePriceRange(priceRangeId, acceptLanguage)

Get one price range by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PriceRangesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.pims.io/api/v1");
    
    // Configure HTTP basic authorization: Basic Auth
    HttpBasicAuth Basic Auth = (HttpBasicAuth) defaultClient.getAuthentication("Basic Auth");
    Basic Auth.setUsername("YOUR USERNAME");
    Basic Auth.setPassword("YOUR PASSWORD");

    PriceRangesApi apiInstance = new PriceRangesApi(defaultClient);
    Integer priceRangeId = 56; // Integer | ID of the targeted price range.
    String acceptLanguage = "de"; // String | Language used for the translatable labels.
    try {
      VenuesEntity result = apiInstance.fetchOnePriceRange(priceRangeId, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PriceRangesApi#fetchOnePriceRange");
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
| **priceRangeId** | **Integer**| ID of the targeted price range. | |
| **acceptLanguage** | **String**| Language used for the translatable labels. | [optional] [default to en] [enum: de, en, fr] |

### Return type

[**VenuesEntity**](VenuesEntity.md)

### Authorization

[Basic Auth](../README.md#Basic Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation, gives one price range |  -  |
| **401** | Unauthorized, no authentication was made |  -  |
| **403** | Forbidden, the authentication is wrong |  -  |
| **404** | Not Found |  -  |
| **500** | Unexpected error |  -  |

