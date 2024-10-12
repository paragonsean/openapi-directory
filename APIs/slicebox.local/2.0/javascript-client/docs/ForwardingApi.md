# SliceboxApi.ForwardingApi

All URIs are relative to *http://slicebox.local/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**forwardingRuleIdDelete**](ForwardingApi.md#forwardingRuleIdDelete) | **DELETE** /forwarding/rule/{id} | 
[**forwardingRulesGet**](ForwardingApi.md#forwardingRulesGet) | **GET** /forwarding/rules | 
[**forwardingRulesPost**](ForwardingApi.md#forwardingRulesPost) | **POST** /forwarding/rules | 



## forwardingRuleIdDelete

> forwardingRuleIdDelete(id)



remove the forwarding rule corresponding to the supplied ID

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.ForwardingApi();
let id = 789; // Number | id of forwarding rule to remove
apiInstance.forwardingRuleIdDelete(id, (error, data, response) => {
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
 **id** | **Number**| id of forwarding rule to remove | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## forwardingRulesGet

> [Forwardingrule] forwardingRulesGet(opts)



get a list of all forwarding rules. A forwarding rule specifies the automatic forwarding of images from a source (SCP, BOX, etc.) to a destimation (BOX, SCU, etc.)

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.ForwardingApi();
let opts = {
  'startindex': 0, // Number | start index of returned slice of rules
  'count': 20 // Number | size of returned slice of rules
};
apiInstance.forwardingRulesGet(opts, (error, data, response) => {
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
 **startindex** | **Number**| start index of returned slice of rules | [optional] [default to 0]
 **count** | **Number**| size of returned slice of rules | [optional] [default to 20]

### Return type

[**[Forwardingrule]**](Forwardingrule.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/octet-stream


## forwardingRulesPost

> Forwardingrule forwardingRulesPost(opts)



add a new forwarding rule

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.ForwardingApi();
let opts = {
  'fowardingRule': new SliceboxApi.Forwardingrule() // Forwardingrule | The forwarding rule to add. The ID property is irrelevant, the ID of the inserted record is present in the returned data.
};
apiInstance.forwardingRulesPost(opts, (error, data, response) => {
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
 **fowardingRule** | [**Forwardingrule**](Forwardingrule.md)| The forwarding rule to add. The ID property is irrelevant, the ID of the inserted record is present in the returned data. | [optional] 

### Return type

[**Forwardingrule**](Forwardingrule.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/octet-stream, multipart/form-data
- **Accept**: application/json, application/octet-stream

