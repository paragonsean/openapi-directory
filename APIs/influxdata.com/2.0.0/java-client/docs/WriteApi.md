# WriteApi

All URIs are relative to */api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**postWrite**](WriteApi.md#postWrite) | **POST** /write | Write time series data into InfluxDB |


<a id="postWrite"></a>
# **postWrite**
> postWrite(org, bucket, body, zapTraceSpan, contentEncoding, contentType, contentLength, accept, orgID, precision)

Write time series data into InfluxDB

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WriteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    WriteApi apiInstance = new WriteApi(defaultClient);
    String org = "org_example"; // String | Specifies the destination organization for writes. Takes either the ID or Name interchangeably. If both `orgID` and `org` are specified, `org` takes precedence.
    String bucket = "bucket_example"; // String | The destination bucket for writes.
    byte[] body = null; // byte[] | Line protocol body
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    String contentEncoding = "gzip"; // String | When present, its value indicates to the database that compression is applied to the line-protocol body.
    String contentType = "text/plain"; // String | Content-Type is used to indicate the format of the data sent to the server.
    Integer contentLength = 56; // Integer | Content-Length is an entity header is indicating the size of the entity-body, in bytes, sent to the database. If the length is greater than the database max body configuration option, a 413 response is sent.
    String accept = "application/json"; // String | Specifies the return content format.
    String orgID = "orgID_example"; // String | Specifies the ID of the destination organization for writes. If both `orgID` and `org` are specified, `org` takes precedence.
    WritePrecision precision = WritePrecision.fromValue("ms"); // WritePrecision | The precision for the unix timestamps within the body line-protocol.
    try {
      apiInstance.postWrite(org, bucket, body, zapTraceSpan, contentEncoding, contentType, contentLength, accept, orgID, precision);
    } catch (ApiException e) {
      System.err.println("Exception when calling WriteApi#postWrite");
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
| **org** | **String**| Specifies the destination organization for writes. Takes either the ID or Name interchangeably. If both &#x60;orgID&#x60; and &#x60;org&#x60; are specified, &#x60;org&#x60; takes precedence. | |
| **bucket** | **String**| The destination bucket for writes. | |
| **body** | **byte[]**| Line protocol body | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |
| **contentEncoding** | **String**| When present, its value indicates to the database that compression is applied to the line-protocol body. | [optional] [default to identity] [enum: gzip, identity] |
| **contentType** | **String**| Content-Type is used to indicate the format of the data sent to the server. | [optional] [default to text/plain; charset&#x3D;utf-8] [enum: text/plain, text/plain; charset=utf-8, application/vnd.influx.arrow] |
| **contentLength** | **Integer**| Content-Length is an entity header is indicating the size of the entity-body, in bytes, sent to the database. If the length is greater than the database max body configuration option, a 413 response is sent. | [optional] |
| **accept** | **String**| Specifies the return content format. | [optional] [default to application/json] [enum: application/json] |
| **orgID** | **String**| Specifies the ID of the destination organization for writes. If both &#x60;orgID&#x60; and &#x60;org&#x60; are specified, &#x60;org&#x60; takes precedence. | [optional] |
| **precision** | [**WritePrecision**](.md)| The precision for the unix timestamps within the body line-protocol. | [optional] [enum: ms, s, us, ns] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Write data is correctly formatted and accepted for writing to the bucket. |  -  |
| **400** | Line protocol poorly formed and no points were written.  Response can be used to determine the first malformed line in the body line-protocol. All data in body was rejected and not written. |  -  |
| **401** | Token does not have sufficient permissions to write to this organization and bucket or the organization and bucket do not exist. |  -  |
| **403** | No token was sent and they are required. |  -  |
| **413** | Write has been rejected because the payload is too large. Error message returns max size supported. All data in body was rejected and not written. |  -  |
| **429** | Token is temporarily over quota. The Retry-After header describes when to try the write again. |  * Retry-After - A non-negative decimal integer indicating the seconds to delay after the response is received. <br>  |
| **503** | Server is temporarily unavailable to accept writes.  The Retry-After header describes when to try the write again. |  * Retry-After - A non-negative decimal integer indicating the seconds to delay after the response is received. <br>  |
| **0** | Internal server error |  -  |

