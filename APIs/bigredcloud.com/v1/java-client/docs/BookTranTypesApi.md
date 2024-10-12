# BookTranTypesApi

All URIs are relative to *https://app.bigredcloud.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**bookTranTypesGet**](BookTranTypesApi.md#bookTranTypesGet) | **GET** /v1/bookTranTypes | Returns a list of global Book Transactions&#39; Types. Supports OData querying protocol.  Filtering is forbidden.  Ordering is allowed by \&quot;id\&quot; field. |


<a id="bookTranTypesGet"></a>
# **bookTranTypesGet**
> PageResultBookTranTypeDto bookTranTypesGet()

Returns a list of global Book Transactions&#39; Types. Supports OData querying protocol.  Filtering is forbidden.  Ordering is allowed by \&quot;id\&quot; field.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BookTranTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    BookTranTypesApi apiInstance = new BookTranTypesApi(defaultClient);
    try {
      PageResultBookTranTypeDto result = apiInstance.bookTranTypesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BookTranTypesApi#bookTranTypesGet");
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

[**PageResultBookTranTypeDto**](PageResultBookTranTypeDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

