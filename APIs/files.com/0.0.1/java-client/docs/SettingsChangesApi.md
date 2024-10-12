# SettingsChangesApi

All URIs are relative to *http://app.files.com/api/rest/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getSettingsChanges**](SettingsChangesApi.md#getSettingsChanges) | **GET** /settings_changes | List Settings Changes |


<a id="getSettingsChanges"></a>
# **getSettingsChanges**
> List&lt;SettingsChangeEntity&gt; getSettingsChanges(cursor, perPage, sortBy, apiKeyId, userId, filter)

List Settings Changes

List Settings Changes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsChangesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    SettingsChangesApi apiInstance = new SettingsChangesApi(defaultClient);
    String cursor = "cursor_example"; // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    Integer perPage = 56; // Integer | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    Object sortBy = null; // Object | If set, sort records by the specified field in either `asc` or `desc` direction (e.g. `sort_by[api_key_id]=desc`). Valid fields are `api_key_id`, `created_at` or `user_id`.
    String apiKeyId = "apiKeyId_example"; // String | If set, return records where the specified field is equal to the supplied value.
    String userId = "userId_example"; // String | If set, return records where the specified field is equal to the supplied value.
    Object filter = null; // Object | If set, return records where the specified field is equal to the supplied value. Valid fields are `api_key_id` and `user_id`.
    try {
      List<SettingsChangeEntity> result = apiInstance.getSettingsChanges(cursor, perPage, sortBy, apiKeyId, userId, filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsChangesApi#getSettingsChanges");
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
| **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] |
| **perPage** | **Integer**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] |
| **sortBy** | [**Object**](.md)| If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[api_key_id]&#x3D;desc&#x60;). Valid fields are &#x60;api_key_id&#x60;, &#x60;created_at&#x60; or &#x60;user_id&#x60;. | [optional] |
| **apiKeyId** | **String**| If set, return records where the specified field is equal to the supplied value. | [optional] |
| **userId** | **String**| If set, return records where the specified field is equal to the supplied value. | [optional] |
| **filter** | [**Object**](.md)| If set, return records where the specified field is equal to the supplied value. Valid fields are &#x60;api_key_id&#x60; and &#x60;user_id&#x60;. | [optional] |

### Return type

[**List&lt;SettingsChangeEntity&gt;**](SettingsChangeEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of SettingsChanges objects. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **409** | Conflict |  -  |
| **412** | Precondition Failed |  -  |
| **422** | Unprocessable Entity |  -  |
| **423** | Locked |  -  |
| **429** | Too Many Requests |  -  |

