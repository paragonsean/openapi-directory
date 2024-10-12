# VocaDbWeb.EntryApiApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiEntriesGet**](EntryApiApi.md#apiEntriesGet) | **GET** /api/entries | 
[**apiEntriesNamesGet**](EntryApiApi.md#apiEntriesNamesGet) | **GET** /api/entries/names | 



## apiEntriesGet

> EntryForApiContractPartialFindResult apiEntriesGet(opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.EntryApiApi();
let opts = {
  'query': "''", // String | 
  'tagName': ["null"], // [String] | 
  'tagId': [null], // [Number] | 
  'childTags': false, // Boolean | 
  'entryTypes': new VocaDbWeb.EntryTypes(), // EntryTypes | 
  'status': new VocaDbWeb.EntryStatus(), // EntryStatus | 
  'start': 0, // Number | 
  'maxResults': 10, // Number | 
  'getTotalCount': false, // Boolean | 
  'sort': new VocaDbWeb.EntrySortRule(), // EntrySortRule | 
  'nameMatchMode': new VocaDbWeb.NameMatchMode(), // NameMatchMode | 
  'fields': new VocaDbWeb.EntryOptionalFields(), // EntryOptionalFields | 
  'lang': new VocaDbWeb.ContentLanguagePreference() // ContentLanguagePreference | 
};
apiInstance.apiEntriesGet(opts, (error, data, response) => {
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
 **query** | **String**|  | [optional] [default to &#39;&#39;]
 **tagName** | [**[String]**](String.md)|  | [optional] 
 **tagId** | [**[Number]**](Number.md)|  | [optional] 
 **childTags** | **Boolean**|  | [optional] [default to false]
 **entryTypes** | [**EntryTypes**](.md)|  | [optional] 
 **status** | [**EntryStatus**](.md)|  | [optional] 
 **start** | **Number**|  | [optional] [default to 0]
 **maxResults** | **Number**|  | [optional] [default to 10]
 **getTotalCount** | **Boolean**|  | [optional] [default to false]
 **sort** | [**EntrySortRule**](.md)|  | [optional] 
 **nameMatchMode** | [**NameMatchMode**](.md)|  | [optional] 
 **fields** | [**EntryOptionalFields**](.md)|  | [optional] 
 **lang** | [**ContentLanguagePreference**](.md)|  | [optional] 

### Return type

[**EntryForApiContractPartialFindResult**](EntryForApiContractPartialFindResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiEntriesNamesGet

> [String] apiEntriesNamesGet(opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.EntryApiApi();
let opts = {
  'query': "''", // String | 
  'nameMatchMode': new VocaDbWeb.NameMatchMode(), // NameMatchMode | 
  'maxResults': 10 // Number | 
};
apiInstance.apiEntriesNamesGet(opts, (error, data, response) => {
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
 **query** | **String**|  | [optional] [default to &#39;&#39;]
 **nameMatchMode** | [**NameMatchMode**](.md)|  | [optional] 
 **maxResults** | **Number**|  | [optional] [default to 10]

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

