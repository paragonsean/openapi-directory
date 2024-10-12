# OwnerTypesApi

All URIs are relative to *https://app.bigredcloud.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**ownerTypesGet**](OwnerTypesApi.md#ownerTypesGet) | **GET** /v1/ownerTypes | Returns a list of global Owner Types. Supports OData querying protocol.  Filtering is forbidden.  Ordering is allowed by \&quot;id\&quot; field. |


<a id="ownerTypesGet"></a>
# **ownerTypesGet**
> PageResultOwnerTypeDto ownerTypesGet()

Returns a list of global Owner Types. Supports OData querying protocol.  Filtering is forbidden.  Ordering is allowed by \&quot;id\&quot; field.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OwnerTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    OwnerTypesApi apiInstance = new OwnerTypesApi(defaultClient);
    try {
      PageResultOwnerTypeDto result = apiInstance.ownerTypesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OwnerTypesApi#ownerTypesGet");
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

[**PageResultOwnerTypeDto**](PageResultOwnerTypeDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

