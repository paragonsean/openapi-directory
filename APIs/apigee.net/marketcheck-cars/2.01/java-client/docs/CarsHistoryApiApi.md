# CarsHistoryApiApi

All URIs are relative to *https://marketcheck-prod.apigee.net/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getCarHistory**](CarsHistoryApiApi.md#getCarHistory) | **GET** /history/car/{vin} | Get a cars online listing history |
| [**historyCarUkVrmGet**](CarsHistoryApiApi.md#historyCarUkVrmGet) | **GET** /history/car/uk/{vrm} | Get a cars online listing history |


<a id="getCarHistory"></a>
# **getCarHistory**
> List&lt;HistoricalListing&gt; getCarHistory(vin, apiKey, fields, page, includeDuplicates, sortOrder)

Get a cars online listing history

The history API returns online listing history for a car identified by its VIN. History listings are sorted in the descending order of the listing date / last seen date

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CarsHistoryApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    CarsHistoryApiApi apiInstance = new CarsHistoryApiApi(defaultClient);
    String vin = "vin_example"; // String | The VIN to identify the car. Must be a valid 17 char VIN
    String apiKey = "apiKey_example"; // String | The API Authentication Key. Mandatory with all API calls.
    String fields = "fields_example"; // String | List of fields to fetch, in case the default fields list in the response is to be trimmed down
    BigDecimal page = new BigDecimal(78); // BigDecimal | Page number to fetch the results for the given criteria. Default is 1.
    Boolean includeDuplicates = true; // Boolean | Flag to indicate whether to include duplicate historical records as well in the response
    String sortOrder = "asc"; // String | Sort order - asc or desc. Default sort order is asc
    try {
      List<HistoricalListing> result = apiInstance.getCarHistory(vin, apiKey, fields, page, includeDuplicates, sortOrder);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CarsHistoryApiApi#getCarHistory");
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
| **vin** | **String**| The VIN to identify the car. Must be a valid 17 char VIN | |
| **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] |
| **fields** | **String**| List of fields to fetch, in case the default fields list in the response is to be trimmed down | [optional] |
| **page** | **BigDecimal**| Page number to fetch the results for the given criteria. Default is 1. | [optional] |
| **includeDuplicates** | **Boolean**| Flag to indicate whether to include duplicate historical records as well in the response | [optional] |
| **sortOrder** | **String**| Sort order - asc or desc. Default sort order is asc | [optional] [enum: asc, desc, ASC, DESC] |

### Return type

[**List&lt;HistoricalListing&gt;**](HistoricalListing.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Online listing history for the given vin |  -  |
| **0** | Error |  -  |

<a id="historyCarUkVrmGet"></a>
# **historyCarUkVrmGet**
> List&lt;HistoricalListing&gt; historyCarUkVrmGet(vrm, apiKey, page, includeDuplicates, sortOrder)

Get a cars online listing history

The history API returns online listing history for a car identified by its VRM. History listings are sorted in the descending order of the listing date / last seen date

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CarsHistoryApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    CarsHistoryApiApi apiInstance = new CarsHistoryApiApi(defaultClient);
    String vrm = "vrm_example"; // String | The VRM to identify the car.
    String apiKey = "apiKey_example"; // String | The API Authentication Key. Mandatory with all API calls.
    BigDecimal page = new BigDecimal(78); // BigDecimal | Page number to fetch the results for the given criteria. Default is 1.
    Boolean includeDuplicates = true; // Boolean | Flag to indicate whether to include duplicate historical records as well in the response
    String sortOrder = "asc"; // String | Sort order - asc or desc. Default sort order is asc
    try {
      List<HistoricalListing> result = apiInstance.historyCarUkVrmGet(vrm, apiKey, page, includeDuplicates, sortOrder);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CarsHistoryApiApi#historyCarUkVrmGet");
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
| **vrm** | **String**| The VRM to identify the car. | |
| **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] |
| **page** | **BigDecimal**| Page number to fetch the results for the given criteria. Default is 1. | [optional] |
| **includeDuplicates** | **Boolean**| Flag to indicate whether to include duplicate historical records as well in the response | [optional] |
| **sortOrder** | **String**| Sort order - asc or desc. Default sort order is asc | [optional] [enum: asc, desc, ASC, DESC] |

### Return type

[**List&lt;HistoricalListing&gt;**](HistoricalListing.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Online listing history for the given vrm |  -  |
| **0** | Error |  -  |

