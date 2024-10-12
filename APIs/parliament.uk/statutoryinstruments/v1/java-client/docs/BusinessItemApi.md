# BusinessItemApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getBusinessItemById**](BusinessItemApi.md#getBusinessItemById) | **GET** /api/v1/BusinessItem/{id} | Returns business item by ID. |


<a id="getBusinessItemById"></a>
# **getBusinessItemById**
> BusinessItemResource getBusinessItemById(id, laidPaper)

Returns business item by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BusinessItemApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    BusinessItemApi apiInstance = new BusinessItemApi(defaultClient);
    String id = "id_example"; // String | Business item with the ID specified
    LaidPaperType laidPaper = LaidPaperType.fromValue("StatutoryInstrument"); // LaidPaperType | Business item by laid paper type
    try {
      BusinessItemResource result = apiInstance.getBusinessItemById(id, laidPaper);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BusinessItemApi#getBusinessItemById");
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
| **id** | **String**| Business item with the ID specified | |
| **laidPaper** | [**LaidPaperType**](.md)| Business item by laid paper type | [optional] [enum: StatutoryInstrument, ProposedNegative] |

### Return type

[**BusinessItemResource**](BusinessItemResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested business item |  -  |
| **400** | Bad Request |  -  |
| **404** | If the item doesn&#39;t exist |  -  |

