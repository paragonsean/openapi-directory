# InfluxOssApiService.WriteApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postWrite**](WriteApi.md#postWrite) | **POST** /write | Write time series data into InfluxDB



## postWrite

> postWrite(org, bucket, body, opts)

Write time series data into InfluxDB

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.WriteApi();
let org = "org_example"; // String | Specifies the destination organization for writes. Takes either the ID or Name interchangeably. If both `orgID` and `org` are specified, `org` takes precedence.
let bucket = "bucket_example"; // String | The destination bucket for writes.
let body = null; // Blob | Line protocol body
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}", // String | OpenTracing span context
  'contentEncoding': "'identity'", // String | When present, its value indicates to the database that compression is applied to the line-protocol body.
  'contentType': "'text/plain; charset=utf-8'", // String | Content-Type is used to indicate the format of the data sent to the server.
  'contentLength': 56, // Number | Content-Length is an entity header is indicating the size of the entity-body, in bytes, sent to the database. If the length is greater than the database max body configuration option, a 413 response is sent.
  'accept': "'application/json'", // String | Specifies the return content format.
  'orgID': "orgID_example", // String | Specifies the ID of the destination organization for writes. If both `orgID` and `org` are specified, `org` takes precedence.
  'precision': new InfluxOssApiService.WritePrecision() // WritePrecision | The precision for the unix timestamps within the body line-protocol.
};
apiInstance.postWrite(org, bucket, body, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **String**| Specifies the destination organization for writes. Takes either the ID or Name interchangeably. If both &#x60;orgID&#x60; and &#x60;org&#x60; are specified, &#x60;org&#x60; takes precedence. | 
 **bucket** | **String**| The destination bucket for writes. | 
 **body** | **Blob**| Line protocol body | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 
 **contentEncoding** | **String**| When present, its value indicates to the database that compression is applied to the line-protocol body. | [optional] [default to &#39;identity&#39;]
 **contentType** | **String**| Content-Type is used to indicate the format of the data sent to the server. | [optional] [default to &#39;text/plain; charset&#x3D;utf-8&#39;]
 **contentLength** | **Number**| Content-Length is an entity header is indicating the size of the entity-body, in bytes, sent to the database. If the length is greater than the database max body configuration option, a 413 response is sent. | [optional] 
 **accept** | **String**| Specifies the return content format. | [optional] [default to &#39;application/json&#39;]
 **orgID** | **String**| Specifies the ID of the destination organization for writes. If both &#x60;orgID&#x60; and &#x60;org&#x60; are specified, &#x60;org&#x60; takes precedence. | [optional] 
 **precision** | [**WritePrecision**](.md)| The precision for the unix timestamps within the body line-protocol. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: text/plain
- **Accept**: application/json

