# PostmarkApi.InboundRulesAPIApi

All URIs are relative to *http://api.postmarkapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createInboundRule**](InboundRulesAPIApi.md#createInboundRule) | **POST** /triggers/inboundrules | Create an inbound rule trigger
[**deleteInboundRule**](InboundRulesAPIApi.md#deleteInboundRule) | **DELETE** /triggers/inboundrules/{triggerid} | Delete a single trigger
[**listInboundRules**](InboundRulesAPIApi.md#listInboundRules) | **GET** /triggers/inboundrules | List inbound rule triggers



## createInboundRule

> CreateInboundRule200Response createInboundRule(xPostmarkServerToken, opts)

Create an inbound rule trigger

### Example

```javascript
import PostmarkApi from 'postmark_api';

let apiInstance = new PostmarkApi.InboundRulesAPIApi();
let xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
let opts = {
  'body': new PostmarkApi.CreateInboundRuleRequest() // CreateInboundRuleRequest | 
};
apiInstance.createInboundRule(xPostmarkServerToken, opts, (error, data, response) => {
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
 **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | 
 **body** | [**CreateInboundRuleRequest**](CreateInboundRuleRequest.md)|  | [optional] 

### Return type

[**CreateInboundRule200Response**](CreateInboundRule200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteInboundRule

> StandardPostmarkResponse deleteInboundRule(xPostmarkServerToken, triggerid)

Delete a single trigger

### Example

```javascript
import PostmarkApi from 'postmark_api';

let apiInstance = new PostmarkApi.InboundRulesAPIApi();
let xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
let triggerid = 56; // Number | The ID of the Inbound Rule that should be deleted.
apiInstance.deleteInboundRule(xPostmarkServerToken, triggerid, (error, data, response) => {
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
 **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | 
 **triggerid** | **Number**| The ID of the Inbound Rule that should be deleted. | 

### Return type

[**StandardPostmarkResponse**](StandardPostmarkResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listInboundRules

> ListInboundRules200Response listInboundRules(xPostmarkServerToken, count, offset)

List inbound rule triggers

### Example

```javascript
import PostmarkApi from 'postmark_api';

let apiInstance = new PostmarkApi.InboundRulesAPIApi();
let xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
let count = 56; // Number | Number of records to return per request.
let offset = 56; // Number | Number of records to skip.
apiInstance.listInboundRules(xPostmarkServerToken, count, offset, (error, data, response) => {
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
 **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | 
 **count** | **Number**| Number of records to return per request. | 
 **offset** | **Number**| Number of records to skip. | 

### Return type

[**ListInboundRules200Response**](ListInboundRules200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

