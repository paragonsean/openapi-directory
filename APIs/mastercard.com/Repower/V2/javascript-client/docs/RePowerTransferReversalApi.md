# RePower.RePowerTransferReversalApi

All URIs are relative to *https://api.mastercard.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**repowerReversalPost2**](RePowerTransferReversalApi.md#repowerReversalPost2) | **POST** /repower/v2/repowerreversal | 



## repowerReversalPost2

> Repowerreversal11Wrapper repowerReversalPost2(opts)



A Transfer Reversal is a request to reverse a previously submitted Mastercard rePower Transfer, and is only available in extremely limited circumstances.  Reversal Processing : A rePower transaction reversal may be submitted in the event of a documented clerical error. The rePower transaction reversal must be submitted within 15 minutes of the time the original rePower transaction was authorized.  Use this resource to reverse a previously submitted rePower Transfer. 

### Example

```javascript
import RePower from 're_power';

let apiInstance = new RePower.RePowerTransferReversalApi();
let opts = {
  'repowerReversalRequest': new RePower.Repowerreversalrequest10Wrapper() // Repowerreversalrequest10Wrapper | Contains the details of the repower reversal request message.
};
apiInstance.repowerReversalPost2(opts, (error, data, response) => {
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
 **repowerReversalRequest** | [**Repowerreversalrequest10Wrapper**](Repowerreversalrequest10Wrapper.md)| Contains the details of the repower reversal request message. | [optional] 

### Return type

[**Repowerreversal11Wrapper**](Repowerreversal11Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/xml
- **Accept**: application/xml

