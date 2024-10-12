# CategoryTypesApi

All URIs are relative to *https://app.bigredcloud.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**categoryTypesGet**](CategoryTypesApi.md#categoryTypesGet) | **GET** /v1/categoryTypes | Returns a list of company&#39;s Category Types. Supports OData querying protocol.  Filtering is forbidden.  Ordering is allowed by \&quot;id\&quot; field. |


<a id="categoryTypesGet"></a>
# **categoryTypesGet**
> PageResultCategoryTypeDto categoryTypesGet()

Returns a list of company&#39;s Category Types. Supports OData querying protocol.  Filtering is forbidden.  Ordering is allowed by \&quot;id\&quot; field.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoryTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    CategoryTypesApi apiInstance = new CategoryTypesApi(defaultClient);
    try {
      PageResultCategoryTypeDto result = apiInstance.categoryTypesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoryTypesApi#categoryTypesGet");
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

[**PageResultCategoryTypeDto**](PageResultCategoryTypeDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

