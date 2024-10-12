# UpApi.TagsApi

All URIs are relative to *https://api.up.com.au/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tagsGet**](TagsApi.md#tagsGet) | **GET** /tags | List tags
[**transactionsTransactionIdRelationshipsTagsDelete**](TagsApi.md#transactionsTransactionIdRelationshipsTagsDelete) | **DELETE** /transactions/{transactionId}/relationships/tags | Remove tags from transaction
[**transactionsTransactionIdRelationshipsTagsPost**](TagsApi.md#transactionsTransactionIdRelationshipsTagsPost) | **POST** /transactions/{transactionId}/relationships/tags | Add tags to transaction



## tagsGet

> ListTagsResponse tagsGet(opts)

List tags

Retrieve a list of all tags currently in use. The returned list is [paginated](#pagination) and can be scrolled by following the &#x60;next&#x60; and &#x60;prev&#x60; links where present. Results are ordered lexicographically. The &#x60;transactions&#x60; relationship for each tag exposes a link to get the transactions with the given tag. 

### Example

```javascript
import UpApi from 'up_api';
let defaultClient = UpApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new UpApi.TagsApi();
let opts = {
  'pageSize': 50 // Number | The number of records to return in each page. 
};
apiInstance.tagsGet(opts, (error, data, response) => {
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
 **pageSize** | **Number**| The number of records to return in each page.  | [optional] 

### Return type

[**ListTagsResponse**](ListTagsResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## transactionsTransactionIdRelationshipsTagsDelete

> transactionsTransactionIdRelationshipsTagsDelete(transactionId, opts)

Remove tags from transaction

Disassociates one or more tags from a specific transaction. Tags that are not associated are silently ignored. An HTTP &#x60;204&#x60; is returned on success. The associated tags, along with this request URL, are also exposed via the &#x60;tags&#x60; relationship on the transaction resource returned from &#x60;/transactions/{id}&#x60;. 

### Example

```javascript
import UpApi from 'up_api';
let defaultClient = UpApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new UpApi.TagsApi();
let transactionId = "c3feb4ba-829c-4482-b882-1b9bd23da82d"; // String | The unique identifier for the transaction. 
let opts = {
  'updateTransactionTagsRequest': new UpApi.UpdateTransactionTagsRequest() // UpdateTransactionTagsRequest | 
};
apiInstance.transactionsTransactionIdRelationshipsTagsDelete(transactionId, opts, (error, data, response) => {
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
 **transactionId** | **String**| The unique identifier for the transaction.  | 
 **updateTransactionTagsRequest** | [**UpdateTransactionTagsRequest**](UpdateTransactionTagsRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## transactionsTransactionIdRelationshipsTagsPost

> transactionsTransactionIdRelationshipsTagsPost(transactionId, opts)

Add tags to transaction

Associates one or more tags with a specific transaction. No more than 6 tags may be present on any single transaction. Duplicate tags are silently ignored. An HTTP &#x60;204&#x60; is returned on success. The associated tags, along with this request URL, are also exposed via the &#x60;tags&#x60; relationship on the transaction resource returned from &#x60;/transactions/{id}&#x60;. 

### Example

```javascript
import UpApi from 'up_api';
let defaultClient = UpApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new UpApi.TagsApi();
let transactionId = "acde4631-db56-49a6-aea3-4e2311ef1d6a"; // String | The unique identifier for the transaction. 
let opts = {
  'updateTransactionTagsRequest': new UpApi.UpdateTransactionTagsRequest() // UpdateTransactionTagsRequest | 
};
apiInstance.transactionsTransactionIdRelationshipsTagsPost(transactionId, opts, (error, data, response) => {
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
 **transactionId** | **String**| The unique identifier for the transaction.  | 
 **updateTransactionTagsRequest** | [**UpdateTransactionTagsRequest**](UpdateTransactionTagsRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

