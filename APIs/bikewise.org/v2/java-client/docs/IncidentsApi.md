# IncidentsApi

All URIs are relative to *https://bikewise.org/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**gETVersionIncidentsFormat**](IncidentsApi.md#gETVersionIncidentsFormat) | **GET** /v2/incidents | Paginated incidents matching parameters |
| [**gETVersionIncidentsIdFormat**](IncidentsApi.md#gETVersionIncidentsIdFormat) | **GET** /v2/incidents/{id} |  |


<a id="gETVersionIncidentsFormat"></a>
# **gETVersionIncidentsFormat**
> gETVersionIncidentsFormat(page, perPage, occurredBefore, occurredAfter, incidentType, proximity, proximitySquare, query)

Paginated incidents matching parameters

 &lt;p&gt;If you’d like more detailed information about bike incidents, use this endpoint. For mapping, &lt;code&gt;locations&lt;/code&gt; is probably a better bet.&lt;/p&gt;  &lt;p&gt;&lt;strong&gt;Notes on location searching&lt;/strong&gt;: &lt;br /&gt; - &lt;code&gt;proximity&lt;/code&gt; accepts an ip address, an address, zipcode, city, or latitude,longitude - i.e. &lt;code&gt;70.210.133.87&lt;/code&gt;, &lt;code&gt;210 NW 11th Ave, Portland, OR&lt;/code&gt;, &lt;code&gt;60647&lt;/code&gt;, &lt;code&gt;Chicago, IL&lt;/code&gt;, and &lt;code&gt;45.521728,-122.67326&lt;/code&gt; are all acceptable&lt;br /&gt; - &lt;code&gt;proximity_square&lt;/code&gt; sets the length of the sides of the square to find matches inside of. The square is centered on the location specified by &lt;code&gt;proximity&lt;/code&gt;. It defaults to 100.&lt;/p&gt; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IncidentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://bikewise.org/api");

    IncidentsApi apiInstance = new IncidentsApi(defaultClient);
    Integer page = 1; // Integer | <p>Page of results to fetch.</p> 
    Integer perPage = 56; // Integer | <p>Number of results to return per page.</p> 
    Integer occurredBefore = 56; // Integer | <p>End of period</p> 
    Integer occurredAfter = 56; // Integer | <p>Start of period</p> 
    String incidentType = "crash"; // String | <p>Only incidents of specific type</p> 
    String proximity = "proximity_example"; // String | <p>Center of location for proximity search</p> 
    Integer proximitySquare = 100; // Integer | <p>Size of the proximity search</p> 
    String query = "query_example"; // String | <p>Full text search of incidents</p> 
    try {
      apiInstance.gETVersionIncidentsFormat(page, perPage, occurredBefore, occurredAfter, incidentType, proximity, proximitySquare, query);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncidentsApi#gETVersionIncidentsFormat");
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
| **page** | **Integer**| &lt;p&gt;Page of results to fetch.&lt;/p&gt;  | [optional] [default to 1] |
| **perPage** | **Integer**| &lt;p&gt;Number of results to return per page.&lt;/p&gt;  | [optional] |
| **occurredBefore** | **Integer**| &lt;p&gt;End of period&lt;/p&gt;  | [optional] |
| **occurredAfter** | **Integer**| &lt;p&gt;Start of period&lt;/p&gt;  | [optional] |
| **incidentType** | **String**| &lt;p&gt;Only incidents of specific type&lt;/p&gt;  | [optional] [enum: crash, hazard, theft, unconfirmed, infrastructure_issue, chop_shop] |
| **proximity** | **String**| &lt;p&gt;Center of location for proximity search&lt;/p&gt;  | [optional] |
| **proximitySquare** | **Integer**| &lt;p&gt;Size of the proximity search&lt;/p&gt;  | [optional] [default to 100] |
| **query** | **String**| &lt;p&gt;Full text search of incidents&lt;/p&gt;  | [optional] |

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
| **200** | No response was specified |  -  |

<a id="gETVersionIncidentsIdFormat"></a>
# **gETVersionIncidentsIdFormat**
> gETVersionIncidentsIdFormat(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IncidentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://bikewise.org/api");

    IncidentsApi apiInstance = new IncidentsApi(defaultClient);
    Integer id = 56; // Integer | <p>Incident ID</p> 
    try {
      apiInstance.gETVersionIncidentsIdFormat(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncidentsApi#gETVersionIncidentsIdFormat");
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
| **id** | **Integer**| &lt;p&gt;Incident ID&lt;/p&gt;  | |

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
| **200** | No response was specified |  -  |

