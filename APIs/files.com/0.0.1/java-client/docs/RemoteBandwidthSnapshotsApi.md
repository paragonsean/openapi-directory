# RemoteBandwidthSnapshotsApi

All URIs are relative to *http://app.files.com/api/rest/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getRemoteBandwidthSnapshots**](RemoteBandwidthSnapshotsApi.md#getRemoteBandwidthSnapshots) | **GET** /remote_bandwidth_snapshots | List Remote Bandwidth Snapshots |


<a id="getRemoteBandwidthSnapshots"></a>
# **getRemoteBandwidthSnapshots**
> List&lt;RemoteBandwidthSnapshotEntity&gt; getRemoteBandwidthSnapshots(cursor, perPage, sortBy, filter, filterGt, filterGteq, filterLt, filterLteq)

List Remote Bandwidth Snapshots

List Remote Bandwidth Snapshots

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RemoteBandwidthSnapshotsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    RemoteBandwidthSnapshotsApi apiInstance = new RemoteBandwidthSnapshotsApi(defaultClient);
    String cursor = "cursor_example"; // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    Integer perPage = 56; // Integer | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    Object sortBy = null; // Object | If set, sort records by the specified field in either `asc` or `desc` direction (e.g. `sort_by[logged_at]=desc`). Valid fields are `logged_at`.
    Object filter = null; // Object | If set, return records where the specified field is equal to the supplied value. Valid fields are `logged_at`.
    Object filterGt = null; // Object | If set, return records where the specified field is greater than the supplied value. Valid fields are `logged_at`.
    Object filterGteq = null; // Object | If set, return records where the specified field is greater than or equal the supplied value. Valid fields are `logged_at`.
    Object filterLt = null; // Object | If set, return records where the specified field is less than the supplied value. Valid fields are `logged_at`.
    Object filterLteq = null; // Object | If set, return records where the specified field is less than or equal the supplied value. Valid fields are `logged_at`.
    try {
      List<RemoteBandwidthSnapshotEntity> result = apiInstance.getRemoteBandwidthSnapshots(cursor, perPage, sortBy, filter, filterGt, filterGteq, filterLt, filterLteq);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RemoteBandwidthSnapshotsApi#getRemoteBandwidthSnapshots");
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
| **sortBy** | [**Object**](.md)| If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[logged_at]&#x3D;desc&#x60;). Valid fields are &#x60;logged_at&#x60;. | [optional] |
| **filter** | [**Object**](.md)| If set, return records where the specified field is equal to the supplied value. Valid fields are &#x60;logged_at&#x60;. | [optional] |
| **filterGt** | [**Object**](.md)| If set, return records where the specified field is greater than the supplied value. Valid fields are &#x60;logged_at&#x60;. | [optional] |
| **filterGteq** | [**Object**](.md)| If set, return records where the specified field is greater than or equal the supplied value. Valid fields are &#x60;logged_at&#x60;. | [optional] |
| **filterLt** | [**Object**](.md)| If set, return records where the specified field is less than the supplied value. Valid fields are &#x60;logged_at&#x60;. | [optional] |
| **filterLteq** | [**Object**](.md)| If set, return records where the specified field is less than or equal the supplied value. Valid fields are &#x60;logged_at&#x60;. | [optional] |

### Return type

[**List&lt;RemoteBandwidthSnapshotEntity&gt;**](RemoteBandwidthSnapshotEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of RemoteBandwidthSnapshots objects. |  -  |
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

