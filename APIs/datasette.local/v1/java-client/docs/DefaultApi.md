# DefaultApi

All URIs are relative to *http://datasette.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**query**](DefaultApi.md#query) | **GET** /content.json | Execute a SQLite SQL query against the content database |


<a id="query"></a>
# **query**
> List&lt;Object&gt; query(sql, shape)

Execute a SQLite SQL query against the content database

Accepts SQLite SQL query, returns JSON. Does not allow PRAGMA statements.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://datasette.local");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String sql = "sql_example"; // String | The SQL query to be executed
    String shape = "array"; // String | The shape of the response data. Must be \"array\"
    try {
      List<Object> result = apiInstance.query(sql, shape);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#query");
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
| **sql** | **String**| The SQL query to be executed | |
| **shape** | **String**| The shape of the response data. Must be \&quot;array\&quot; | [enum: array] |

### Return type

**List&lt;Object&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful SQL results |  -  |
| **400** | Bad request |  -  |
| **500** | Internal server error |  -  |

