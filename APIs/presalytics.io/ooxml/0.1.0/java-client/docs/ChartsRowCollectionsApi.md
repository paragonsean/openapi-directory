# ChartsRowCollectionsApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**chartRowcollectionsGetId**](ChartsRowCollectionsApi.md#chartRowcollectionsGetId) | **GET** /Charts/RowCollections/{id} | RowCollections: Get by Id |


<a id="chartRowcollectionsGetId"></a>
# **chartRowcollectionsGetId**
> ChartRowCollections chartRowcollectionsGetId(id)

RowCollections: Get by Id

Get by Id: Use this method to retrieve a RowCollections object by its primary key (id)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChartsRowCollectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    ChartsRowCollectionsApi apiInstance = new ChartsRowCollectionsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    try {
      ChartRowCollections result = apiInstance.chartRowcollectionsGetId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChartsRowCollectionsApi#chartRowcollectionsGetId");
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
| **id** | **UUID**|  | |

### Return type

[**ChartRowCollections**](ChartRowCollections.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |

