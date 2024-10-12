# BioLinkApi.IdentifierPrefixesApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getPrefixCollection**](IdentifierPrefixesApi.md#getPrefixCollection) | **GET** /identifier/prefixes/ | Returns list of prefixes
[**getPrefixContract**](IdentifierPrefixesApi.md#getPrefixContract) | **GET** /identifier/prefixes/contract/{uri} | Returns contracted URI
[**getPrefixExpand**](IdentifierPrefixesApi.md#getPrefixExpand) | **GET** /identifier/prefixes/expand/{id} | Returns expanded URI



## getPrefixCollection

> getPrefixCollection()

Returns list of prefixes

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.IdentifierPrefixesApi();
apiInstance.getPrefixCollection((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getPrefixContract

> getPrefixContract(uri)

Returns contracted URI

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.IdentifierPrefixesApi();
let uri = "uri_example"; // String | URI of entity to be contracted to identifier/CURIE, e.g \"http://www.informatics.jax.org/accession/MGI:1\"
apiInstance.getPrefixContract(uri, (error, data, response) => {
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
 **uri** | **String**| URI of entity to be contracted to identifier/CURIE, e.g \&quot;http://www.informatics.jax.org/accession/MGI:1\&quot; | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getPrefixExpand

> getPrefixExpand(id)

Returns expanded URI

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.IdentifierPrefixesApi();
let id = "id_example"; // String | ID of entity to be contracted to URI, e.g \"MGI:1\"
apiInstance.getPrefixExpand(id, (error, data, response) => {
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
 **id** | **String**| ID of entity to be contracted to URI, e.g \&quot;MGI:1\&quot; | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

