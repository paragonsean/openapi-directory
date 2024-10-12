# TablesRowsApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**tablesRowsGetId**](TablesRowsApi.md#tablesRowsGetId) | **GET** /Tables/Rows/{id} | Rows: Get by Id |


<a id="tablesRowsGetId"></a>
# **tablesRowsGetId**
> TableRows tablesRowsGetId(id)

Rows: Get by Id

Get by Id: Use this method to retrieve a Rows object by its primary key (id)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TablesRowsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    TablesRowsApi apiInstance = new TablesRowsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    try {
      TableRows result = apiInstance.tablesRowsGetId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TablesRowsApi#tablesRowsGetId");
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

[**TableRows**](TableRows.md)

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

