# ManufacturersApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getOrganizationSummaryTopClientsManufacturersByUsage_4**](ManufacturersApi.md#getOrganizationSummaryTopClientsManufacturersByUsage_4) | **GET** /organizations/{organizationId}/summary/top/clients/manufacturers/byUsage | Return metrics for organization&#39;s top clients by data usage (in mb) over given time range, grouped by manufacturer. |


<a id="getOrganizationSummaryTopClientsManufacturersByUsage_4"></a>
# **getOrganizationSummaryTopClientsManufacturersByUsage_4**
> List&lt;GetOrganizationSummaryTopClientsManufacturersByUsage200ResponseInner&gt; getOrganizationSummaryTopClientsManufacturersByUsage_4(organizationId, t0, t1, timespan)

Return metrics for organization&#39;s top clients by data usage (in mb) over given time range, grouped by manufacturer.

Return metrics for organization&#39;s top clients by data usage (in mb) over given time range, grouped by manufacturer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManufacturersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ManufacturersApi apiInstance = new ManufacturersApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    try {
      List<GetOrganizationSummaryTopClientsManufacturersByUsage200ResponseInner> result = apiInstance.getOrganizationSummaryTopClientsManufacturersByUsage_4(organizationId, t0, t1, timespan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManufacturersApi#getOrganizationSummaryTopClientsManufacturersByUsage_4");
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
| **t0** | **String**| The beginning of the timespan for the data. | [optional] |
| **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 31 days after t0. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day. | [optional] |

### Return type

[**List&lt;GetOrganizationSummaryTopClientsManufacturersByUsage200ResponseInner&gt;**](GetOrganizationSummaryTopClientsManufacturersByUsage200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

