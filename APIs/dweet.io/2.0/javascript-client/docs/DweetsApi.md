# DweetIo.DweetsApi

All URIs are relative to *https://dweet.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dweetForThingPost**](DweetsApi.md#dweetForThingPost) | **POST** /dweet/for/{thing} | Create a dweet for a thing.
[**dweetQuietlyForThingPost**](DweetsApi.md#dweetQuietlyForThingPost) | **POST** /dweet/quietly/for/{thing} | Create a dweet for a thing.  This method differs from /dweet/for/{thing} only in that successful dweets result in an HTTP 204 response rather than the typical verbose response.
[**getDweetsForThingGet**](DweetsApi.md#getDweetsForThingGet) | **GET** /get/dweets/for/{thing} | Read the last 5 cached dweets for a thing.
[**getLatestDweet**](DweetsApi.md#getLatestDweet) | **GET** /get/latest/dweet/for/{thing} | Read the latest dweet for a thing.
[**listenForDweets**](DweetsApi.md#listenForDweets) | **GET** /listen/for/dweets/from/{thing} | Listen for dweets from a thing.



## dweetForThingPost

> dweetForThingPost(thing, content, opts)

Create a dweet for a thing.

### Example

```javascript
import DweetIo from 'dweet_io';

let apiInstance = new DweetIo.DweetsApi();
let thing = "thing_example"; // String | A unique name of a thing. It is recommended that you use a GUID as to avoid name collisions.
let content = "content_example"; // String | The actual content of the string. Can be any valid JSON string.
let opts = {
  'key': "key_example" // String | A valid key for a locked thing. If the thing is not locked, this can be ignored.
};
apiInstance.dweetForThingPost(thing, content, opts, (error, data, response) => {
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
 **thing** | **String**| A unique name of a thing. It is recommended that you use a GUID as to avoid name collisions. | 
 **content** | **String**| The actual content of the string. Can be any valid JSON string. | 
 **key** | **String**| A valid key for a locked thing. If the thing is not locked, this can be ignored. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## dweetQuietlyForThingPost

> dweetQuietlyForThingPost(thing, content, opts)

Create a dweet for a thing.  This method differs from /dweet/for/{thing} only in that successful dweets result in an HTTP 204 response rather than the typical verbose response.

### Example

```javascript
import DweetIo from 'dweet_io';

let apiInstance = new DweetIo.DweetsApi();
let thing = "thing_example"; // String | A unique name of a thing. It is recommended that you use a GUID as to avoid name collisions.
let content = "content_example"; // String | The actual content of the string. Can be any valid JSON string.
let opts = {
  'key': "key_example" // String | A valid key for a locked thing. If the thing is not locked, this can be ignored.
};
apiInstance.dweetQuietlyForThingPost(thing, content, opts, (error, data, response) => {
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
 **thing** | **String**| A unique name of a thing. It is recommended that you use a GUID as to avoid name collisions. | 
 **content** | **String**| The actual content of the string. Can be any valid JSON string. | 
 **key** | **String**| A valid key for a locked thing. If the thing is not locked, this can be ignored. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getDweetsForThingGet

> getDweetsForThingGet(thing, opts)

Read the last 5 cached dweets for a thing.

### Example

```javascript
import DweetIo from 'dweet_io';

let apiInstance = new DweetIo.DweetsApi();
let thing = "thing_example"; // String | A unique name of a thing.
let opts = {
  'key': "key_example" // String | A valid key for a locked thing. If the thing is not locked, this can be ignored.
};
apiInstance.getDweetsForThingGet(thing, opts, (error, data, response) => {
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
 **thing** | **String**| A unique name of a thing. | 
 **key** | **String**| A valid key for a locked thing. If the thing is not locked, this can be ignored. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getLatestDweet

> getLatestDweet(thing, opts)

Read the latest dweet for a thing.

### Example

```javascript
import DweetIo from 'dweet_io';

let apiInstance = new DweetIo.DweetsApi();
let thing = "thing_example"; // String | A unique name of a thing.
let opts = {
  'key': "key_example" // String | A valid key for a locked thing. If the thing is not locked, this can be ignored.
};
apiInstance.getLatestDweet(thing, opts, (error, data, response) => {
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
 **thing** | **String**| A unique name of a thing. | 
 **key** | **String**| A valid key for a locked thing. If the thing is not locked, this can be ignored. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## listenForDweets

> listenForDweets(thing)

Listen for dweets from a thing.

Sorry, this function uses HTTP chunked responses and cannot be tested here. Try something like: &lt;pre&gt;curl --raw https://dweet.io/listen/for/dweets/from/{thing}&lt;/pre&gt;

### Example

```javascript
import DweetIo from 'dweet_io';

let apiInstance = new DweetIo.DweetsApi();
let thing = "thing_example"; // String | 
apiInstance.listenForDweets(thing, (error, data, response) => {
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
 **thing** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

