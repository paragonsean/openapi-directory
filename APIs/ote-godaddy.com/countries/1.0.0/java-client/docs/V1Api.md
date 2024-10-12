# V1Api

All URIs are relative to *http://api.ote-godaddy.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getCountries**](V1Api.md#getCountries) | **GET** /v1/countries | Retrieves summary country information for the provided marketId and filters |
| [**getCountry**](V1Api.md#getCountry) | **GET** /v1/countries/{countryKey} | Retrieves country and summary state information for provided countryKey |


<a id="getCountries"></a>
# **getCountries**
> List&lt;CountrySummary&gt; getCountries(marketId, regionTypeId, regionName, sort, order)

Retrieves summary country information for the provided marketId and filters

Authorization is not required

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.ote-godaddy.com");

    V1Api apiInstance = new V1Api(defaultClient);
    String marketId = "marketId_example"; // String | MarketId in which the request is being made, and for which responses should be localized
    Integer regionTypeId = 56; // Integer | Restrict countries to this region type; required if regionName is supplied
    String regionName = "regionName_example"; // String | Restrict countries to this region name; required if regionTypeId is supplied
    String sort = "key"; // String | The term to sort the result countries by.
    String order = "ascending"; // String | The direction to sort the result countries by.
    try {
      List<CountrySummary> result = apiInstance.getCountries(marketId, regionTypeId, regionName, sort, order);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#getCountries");
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
| **marketId** | **String**| MarketId in which the request is being made, and for which responses should be localized | |
| **regionTypeId** | **Integer**| Restrict countries to this region type; required if regionName is supplied | [optional] |
| **regionName** | **String**| Restrict countries to this region name; required if regionTypeId is supplied | [optional] |
| **sort** | **String**| The term to sort the result countries by. | [optional] [default to key] [enum: key, label] |
| **order** | **String**| The direction to sort the result countries by. | [optional] [default to ascending] [enum: ascending, descending] |

### Return type

[**List&lt;CountrySummary&gt;**](CountrySummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request was successful |  -  |
| **422** | marketId is required&lt;br&gt;regionTypeId is not a valid integer&lt;br&gt;regionName is required when regionTypeId is provided&lt;br&gt;regionTypeId is required when regionName is provided |  -  |
| **429** | Too many requests received within interval |  -  |
| **500** | Internal server error |  -  |

<a id="getCountry"></a>
# **getCountry**
> List&lt;Country&gt; getCountry(countryKey, marketId, sort, order)

Retrieves country and summary state information for provided countryKey

Authorization is not required

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.ote-godaddy.com");

    V1Api apiInstance = new V1Api(defaultClient);
    String countryKey = "countryKey_example"; // String | The country key
    String marketId = "marketId_example"; // String | MarketId in which the request is being made, and for which responses should be localized
    String sort = "key"; // String | The term to sort the result country states by.
    String order = "ascending"; // String | The direction to sort the result country states by.
    try {
      List<Country> result = apiInstance.getCountry(countryKey, marketId, sort, order);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#getCountry");
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
| **countryKey** | **String**| The country key | |
| **marketId** | **String**| MarketId in which the request is being made, and for which responses should be localized | |
| **sort** | **String**| The term to sort the result country states by. | [optional] [default to key] [enum: key, label] |
| **order** | **String**| The direction to sort the result country states by. | [optional] [default to ascending] [enum: ascending, descending] |

### Return type

[**List&lt;Country&gt;**](Country.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request was successful |  -  |
| **404** | Country not found |  -  |
| **422** | marketId is required |  -  |
| **429** | Too many requests received within interval |  -  |
| **500** | Internal server error |  -  |

