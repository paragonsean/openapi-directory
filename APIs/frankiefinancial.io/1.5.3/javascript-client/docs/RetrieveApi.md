# FrankieFinancialApi.RetrieveApi

All URIs are relative to *https://api.demo.frankiefinancial.io/compliance/v1.2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieveResult**](RetrieveApi.md#retrieveResult) | **GET** /retrieve/response/{requestId} | (Re)retrieve Response Result.



## retrieveResult

> RetrievedResponseObject retrieveResult(xFrankieCustomerID, requestId, opts)

(Re)retrieve Response Result.

If you&#39;ve received a notification that you previously backgrounded transaction has completed, or you wish to re-retrive a result from an earlier transaction, then you can simply request the result from our encrypted cache  The response will return the original HTTP code, along with the payload that would have been returned in the original request. 

### Example

```javascript
import FrankieFinancialApi from 'frankie_financial_api';
let defaultClient = FrankieFinancialApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new FrankieFinancialApi.RetrieveApi();
let xFrankieCustomerID = "xFrankieCustomerID_example"; // String | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
let requestId = "requestId_example"; // String | This will be the same RequestId that was sent in the 202 acceptance response. 
let opts = {
  'xFrankieCustomerChildID': "xFrankieCustomerChildID_example", // String | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
  'payload': "payload_example" // String | Specifies the type of the payload field in the retrieved response. Default is 'string'. 
};
apiInstance.retrieveResult(xFrankieCustomerID, requestId, opts, (error, data, response) => {
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
 **xFrankieCustomerID** | **String**| Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time.  | 
 **requestId** | **String**| This will be the same RequestId that was sent in the 202 acceptance response.  | 
 **xFrankieCustomerChildID** | **String**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] 
 **payload** | **String**| Specifies the type of the payload field in the retrieved response. Default is &#39;string&#39;.  | [optional] 

### Return type

[**RetrievedResponseObject**](RetrievedResponseObject.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

