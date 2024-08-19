# Ecwid.PingApi

All URIs are relative to *https://api.cloud-elements.com/elements/api-v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getPing**](PingApi.md#getPing) | **GET** /ping | Ping the Element to confirm that the Hub Element has a heartbeat.  If the Element does not have a heartbeat, an error message will be returned.



## getPing

> Pong getPing(authorization)

Ping the Element to confirm that the Hub Element has a heartbeat.  If the Element does not have a heartbeat, an error message will be returned.

### Example

```javascript
import Ecwid from 'ecwid';

let apiInstance = new Ecwid.PingApi();
let authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
apiInstance.getPing(authorization, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | 

### Return type

[**Pong**](Pong.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

