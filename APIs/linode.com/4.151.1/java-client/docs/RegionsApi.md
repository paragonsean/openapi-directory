# RegionsApi

All URIs are relative to *https://api.linode.com/v4*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getRegion**](RegionsApi.md#getRegion) | **GET** /regions/{regionId} | Region View |
| [**getRegions**](RegionsApi.md#getRegions) | **GET** /regions | Regions List |


<a id="getRegion"></a>
# **getRegion**
> Region getRegion(regionId)

Region View

Returns a single Region. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");

    RegionsApi apiInstance = new RegionsApi(defaultClient);
    String regionId = "regionId_example"; // String | ID of the Region to look up.
    try {
      Region result = apiInstance.getRegion(regionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegionsApi#getRegion");
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
| **regionId** | **String**| ID of the Region to look up. | |

### Return type

[**Region**](Region.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A single Region object. |  -  |
| **0** | Error |  -  |

<a id="getRegions"></a>
# **getRegions**
> GetRegions200Response getRegions()

Regions List

Lists the Regions available for Linode services. Not all services are guaranteed to be available in all Regions. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");

    RegionsApi apiInstance = new RegionsApi(defaultClient);
    try {
      GetRegions200Response result = apiInstance.getRegions();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegionsApi#getRegions");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetRegions200Response**](GetRegions200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns an array of Regions. |  -  |
| **0** | Error |  -  |

