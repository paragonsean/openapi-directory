# AnchoreEngineApiServer.RepositoryCredentialsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addRepository**](RepositoryCredentialsApi.md#addRepository) | **POST** /repositories | Add repository to watch



## addRepository

> [Subscription] addRepository(repository, opts)

Add repository to watch



### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.RepositoryCredentialsApi();
let repository = "repository_example"; // String | full repository to add e.g. docker.io/library/alpine
let opts = {
  'autosubscribe': true, // Boolean | flag to enable/disable auto tag_update activation when new images from a repo are added
  'dryrun': true, // Boolean | flag to return tags in the repository without actually watching the repository, default is false
  'xAnchoreAccount': "xAnchoreAccount_example" // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
};
apiInstance.addRepository(repository, opts, (error, data, response) => {
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
 **repository** | **String**| full repository to add e.g. docker.io/library/alpine | 
 **autosubscribe** | **Boolean**| flag to enable/disable auto tag_update activation when new images from a repo are added | [optional] 
 **dryrun** | **Boolean**| flag to return tags in the repository without actually watching the repository, default is false | [optional] 
 **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] 

### Return type

[**[Subscription]**](Subscription.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

