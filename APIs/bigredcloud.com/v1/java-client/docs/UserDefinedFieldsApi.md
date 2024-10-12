# UserDefinedFieldsApi

All URIs are relative to *https://app.bigredcloud.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**userDefinedFieldsGet**](UserDefinedFieldsApi.md#userDefinedFieldsGet) | **GET** /v1/userDefinedFields | Returns a list of company&#39;s User Defined Fields. Supports OData querying protocol.  Filtering is allowed by \&quot;categoryTypeId\&quot; field.  Ordering is allowed by \&quot;id\&quot; and \&quot;orderIndex\&quot; fields. |


<a id="userDefinedFieldsGet"></a>
# **userDefinedFieldsGet**
> PageResultUserDefinedFieldDto userDefinedFieldsGet()

Returns a list of company&#39;s User Defined Fields. Supports OData querying protocol.  Filtering is allowed by \&quot;categoryTypeId\&quot; field.  Ordering is allowed by \&quot;id\&quot; and \&quot;orderIndex\&quot; fields.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserDefinedFieldsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    UserDefinedFieldsApi apiInstance = new UserDefinedFieldsApi(defaultClient);
    try {
      PageResultUserDefinedFieldDto result = apiInstance.userDefinedFieldsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserDefinedFieldsApi#userDefinedFieldsGet");
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

[**PageResultUserDefinedFieldDto**](PageResultUserDefinedFieldDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

