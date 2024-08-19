# MdesCustomerService.SearchApi

All URIs are relative to *https://api.mastercard.com/mdes/csapi/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**searchPost**](SearchApi.md#searchPost) | **POST** /search | 



## searchPost

> SearchResponseSchema searchPost(opts)



Provides the ability to search for tokens based on Account PAN, Alternate Account Identifier, Token Unique Reference, Token, Payment App Instance Id or Comment Id. Returns all of the tokens associated with an account according to the scope of the indicated search request criteria. The response includes key state and informational data for each token, including the Token Unique Reference which is needed for subsequent token lifecycle management activities.&lt;br&gt;&lt;br&gt;_Notes:_ The Search API request MUST include only one of the available search methods Account PAN, Token Unique Reference, Token, Payment App Instance Id, Comment Id, or Alternate Account Identifier. They cannot be used together in a single request.&lt;br&gt; Moreover, this function only retrieves results if the search criteria matches a current value from the token vault. In other words, if the search criteria is a PAN that has been replaced, the system will not retrieve any data.  

### Example

```javascript
import MdesCustomerService from 'mdes_customer_service';

let apiInstance = new MdesCustomerService.SearchApi();
let opts = {
  'searchRequestSchema': new MdesCustomerService.SearchRequestSchema() // SearchRequestSchema | Contains the details of the request message.
};
apiInstance.searchPost(opts, (error, data, response) => {
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
 **searchRequestSchema** | [**SearchRequestSchema**](SearchRequestSchema.md)| Contains the details of the request message. | [optional] 

### Return type

[**SearchResponseSchema**](SearchResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

