# OwnerTypeGroupsApi

All URIs are relative to *https://app.bigredcloud.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**ownerTypeGroupsGet**](OwnerTypeGroupsApi.md#ownerTypeGroupsGet) | **GET** /v1/ownerTypeGroups | Returns a list of global Owner Type Groups. Supports OData querying protocol.  Filtering is forbidden.  Ordering is allowed by \&quot;id\&quot; field. |


<a id="ownerTypeGroupsGet"></a>
# **ownerTypeGroupsGet**
> PageResultOwnerTypeGroupDto ownerTypeGroupsGet()

Returns a list of global Owner Type Groups. Supports OData querying protocol.  Filtering is forbidden.  Ordering is allowed by \&quot;id\&quot; field.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OwnerTypeGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    OwnerTypeGroupsApi apiInstance = new OwnerTypeGroupsApi(defaultClient);
    try {
      PageResultOwnerTypeGroupDto result = apiInstance.ownerTypeGroupsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OwnerTypeGroupsApi#ownerTypeGroupsGet");
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

[**PageResultOwnerTypeGroupDto**](PageResultOwnerTypeGroupDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

