# DeleteApi

All URIs are relative to */api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**postDelete**](DeleteApi.md#postDelete) | **POST** /delete | Delete time series data from InfluxDB |


<a id="postDelete"></a>
# **postDelete**
> postDelete(deletePredicateRequest, zapTraceSpan, org, bucket, orgID, bucketID)

Delete time series data from InfluxDB

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeleteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    DeleteApi apiInstance = new DeleteApi(defaultClient);
    DeletePredicateRequest deletePredicateRequest = new DeletePredicateRequest(); // DeletePredicateRequest | Predicate delete request
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    String org = "org_example"; // String | Specifies the organization to delete data from.
    String bucket = "bucket_example"; // String | Specifies the bucket to delete data from.
    String orgID = "orgID_example"; // String | Specifies the organization ID of the resource.
    String bucketID = "bucketID_example"; // String | Specifies the bucket ID to delete data from.
    try {
      apiInstance.postDelete(deletePredicateRequest, zapTraceSpan, org, bucket, orgID, bucketID);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeleteApi#postDelete");
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
| **deletePredicateRequest** | [**DeletePredicateRequest**](DeletePredicateRequest.md)| Predicate delete request | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |
| **org** | **String**| Specifies the organization to delete data from. | [optional] |
| **bucket** | **String**| Specifies the bucket to delete data from. | [optional] |
| **orgID** | **String**| Specifies the organization ID of the resource. | [optional] |
| **bucketID** | **String**| Specifies the bucket ID to delete data from. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | delete has been accepted |  -  |
| **400** | Invalid request. |  -  |
| **403** | no token was sent or does not have sufficient permissions. |  -  |
| **404** | the bucket or organization is not found. |  -  |
| **0** | internal server error |  -  |

