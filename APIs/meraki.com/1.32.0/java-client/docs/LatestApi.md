# LatestApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getOrganizationSensorReadingsLatest_2**](LatestApi.md#getOrganizationSensorReadingsLatest_2) | **GET** /organizations/{organizationId}/sensor/readings/latest | Return the latest available reading for each metric from each sensor, sorted by sensor serial |


<a id="getOrganizationSensorReadingsLatest_2"></a>
# **getOrganizationSensorReadingsLatest_2**
> List&lt;GetOrganizationSensorReadingsLatest200ResponseInner&gt; getOrganizationSensorReadingsLatest_2(organizationId, perPage, startingAfter, endingBefore, networkIds, serials, metrics)

Return the latest available reading for each metric from each sensor, sorted by sensor serial

Return the latest available reading for each metric from each sensor, sorted by sensor serial

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LatestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    LatestApi apiInstance = new LatestApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 3 - 100. Default is 100.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    List<String> networkIds = Arrays.asList(); // List<String> | Optional parameter to filter readings by network.
    List<String> serials = Arrays.asList(); // List<String> | Optional parameter to filter readings by sensor.
    List<String> metrics = Arrays.asList(); // List<String> | Types of sensor readings to retrieve. If no metrics are supplied, all available types of readings will be retrieved. Allowed values are battery, button, door, humidity, indoorAirQuality, noise, pm25, temperature, tvoc, and water.
    try {
      List<GetOrganizationSensorReadingsLatest200ResponseInner> result = apiInstance.getOrganizationSensorReadingsLatest_2(organizationId, perPage, startingAfter, endingBefore, networkIds, serials, metrics);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LatestApi#getOrganizationSensorReadingsLatest_2");
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
| **organizationId** | **String**|  | |
| **perPage** | **Integer**| The number of entries per page returned. Acceptable range is 3 - 100. Default is 100. | [optional] |
| **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **networkIds** | [**List&lt;String&gt;**](String.md)| Optional parameter to filter readings by network. | [optional] |
| **serials** | [**List&lt;String&gt;**](String.md)| Optional parameter to filter readings by sensor. | [optional] |
| **metrics** | [**List&lt;String&gt;**](String.md)| Types of sensor readings to retrieve. If no metrics are supplied, all available types of readings will be retrieved. Allowed values are battery, button, door, humidity, indoorAirQuality, noise, pm25, temperature, tvoc, and water. | [optional] |

### Return type

[**List&lt;GetOrganizationSensorReadingsLatest200ResponseInner&gt;**](GetOrganizationSensorReadingsLatest200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  * Link - A comma-separated list of first, last, prev, and next relative links used for subsequent paginated requests. <br>  |

