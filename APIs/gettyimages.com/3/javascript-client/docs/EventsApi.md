# GettyImages.EventsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v3EventsGet**](EventsApi.md#v3EventsGet) | **GET** /v3/events | Get metadata for multiple events
[**v3EventsIdGet**](EventsApi.md#v3EventsIdGet) | **GET** /v3/events/{id} | Get metadata for a single event



## v3EventsGet

> v3EventsGet(opts)

Get metadata for multiple events

This endpoint returns the detailed event metadata for all specified events. Getty Images news, sports and entertainment photographers and videographers cover editorially relevant events occurring around the world.  All images or video clips produced in association with  an event, are assigned the same EventID. EventIDs are part of the meta-data returned in SearchForImages Results. Only content  produced under a Getty Images brand name (Getty Images News, Getty Images Sports, Getty Images Entertainment, Film Magic, Wire Image)  will be consistently assigned an EventID. The Event framework may also be used to group similar content, such as  \&quot;Hats from the Royal Wedding\&quot; or \&quot;Odd-ballOffbeat images of the week\&quot;.   You&#39;ll need an API key and access token to use this resource. 

### Example

```javascript
import GettyImages from 'getty_images';
let defaultClient = GettyImages.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure API key authorization: Api-Key
let Api-Key = defaultClient.authentications['Api-Key'];
Api-Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Api-Key.apiKeyPrefix = 'Token';

let apiInstance = new GettyImages.EventsApi();
let opts = {
  'acceptLanguage': "acceptLanguage_example", // String | Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
  'ids': [null], // [Number] | A comma separated list of event ids.
  'fields': [new GettyImages.EventDetailFieldValues()] // [EventDetailFieldValues] | A comma separated list of fields to return in the response.
};
apiInstance.v3EventsGet(opts, (error, data, response) => {
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
 **acceptLanguage** | **String**| Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only). | [optional] 
 **ids** | [**[Number]**](Number.md)| A comma separated list of event ids. | [optional] 
 **fields** | [**[EventDetailFieldValues]**](EventDetailFieldValues.md)| A comma separated list of fields to return in the response. | [optional] 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [Api-Key](../README.md#Api-Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## v3EventsIdGet

> v3EventsIdGet(id, opts)

Get metadata for a single event

This endpoint returns the detailed event metadata for a specified event. Getty Images news, sports and entertainment  photographers and videographers cover editorially relevant events occurring around the world.   All images or video clips produced in association with an event, are assigned the same EventID.  EventIDs are part of the meta-data returned in SearchForImages Results. Only content produced under a Getty Images  brand name (Getty Images News, Getty Images Sports, Getty Images Entertainment, Film Magic, Wire Image) will be  consistently assigned an EventID. The Event framework may also be used to group similar content, such as  \&quot;Hats from the Royal Wedding\&quot; or \&quot;Odd-ballOffbeat images of the week\&quot;.   You&#39;ll need an API key and access token to use this resource. 

### Example

```javascript
import GettyImages from 'getty_images';
let defaultClient = GettyImages.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure API key authorization: Api-Key
let Api-Key = defaultClient.authentications['Api-Key'];
Api-Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Api-Key.apiKeyPrefix = 'Token';

let apiInstance = new GettyImages.EventsApi();
let id = 56; // Number | An event id.
let opts = {
  'acceptLanguage': "acceptLanguage_example", // String | Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
  'fields': [new GettyImages.EventDetailFieldValues()] // [EventDetailFieldValues] | A comma separated list of fields to return in the response.
};
apiInstance.v3EventsIdGet(id, opts, (error, data, response) => {
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
 **id** | **Number**| An event id. | 
 **acceptLanguage** | **String**| Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only). | [optional] 
 **fields** | [**[EventDetailFieldValues]**](EventDetailFieldValues.md)| A comma separated list of fields to return in the response. | [optional] 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [Api-Key](../README.md#Api-Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

