# PathwayApi

All URIs are relative to *http://rest.rgd.mcw.edu/rgdws*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getPathwaysWithDiagramsForCategoryUsingGET**](PathwayApi.md#getPathwaysWithDiagramsForCategoryUsingGET) | **GET** /pathways/diagramsForCategory/{category} | Return a list of pathways based on category provided |
| [**searchPathwaysUsingGET**](PathwayApi.md#searchPathwaysUsingGET) | **GET** /pathways/diagrams/search/{searchString} | Return a list of pathways based on search term |


<a id="getPathwaysWithDiagramsForCategoryUsingGET"></a>
# **getPathwaysWithDiagramsForCategoryUsingGET**
> List&lt;Pathway&gt; getPathwaysWithDiagramsForCategoryUsingGET(category)

Return a list of pathways based on category provided

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PathwayApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    PathwayApi apiInstance = new PathwayApi(defaultClient);
    String category = "category_example"; // String | Pathway Category
    try {
      List<Pathway> result = apiInstance.getPathwaysWithDiagramsForCategoryUsingGET(category);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PathwayApi#getPathwaysWithDiagramsForCategoryUsingGET");
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
| **category** | **String**| Pathway Category | |

### Return type

[**List&lt;Pathway&gt;**](Pathway.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="searchPathwaysUsingGET"></a>
# **searchPathwaysUsingGET**
> List&lt;Pathway&gt; searchPathwaysUsingGET(searchString)

Return a list of pathways based on search term

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PathwayApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    PathwayApi apiInstance = new PathwayApi(defaultClient);
    String searchString = "searchString_example"; // String | Free text search string
    try {
      List<Pathway> result = apiInstance.searchPathwaysUsingGET(searchString);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PathwayApi#searchPathwaysUsingGET");
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
| **searchString** | **String**| Free text search string | |

### Return type

[**List&lt;Pathway&gt;**](Pathway.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

