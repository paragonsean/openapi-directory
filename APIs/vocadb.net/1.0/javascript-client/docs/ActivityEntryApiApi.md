# VocaDbWeb.ActivityEntryApiApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiActivityEntriesGet**](ActivityEntryApiApi.md#apiActivityEntriesGet) | **GET** /api/activityEntries | 



## apiActivityEntriesGet

> ActivityEntryForApiContractPartialFindResult apiActivityEntriesGet(opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.ActivityEntryApiApi();
let opts = {
  'before': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'since': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'userId': 56, // Number | 
  'editEvent': new VocaDbWeb.EntryEditEvent(), // EntryEditEvent | 
  'entryType': new VocaDbWeb.EntryType(), // EntryType | 
  'maxResults': 50, // Number | 
  'getTotalCount': false, // Boolean | 
  'fields': new VocaDbWeb.ActivityEntryOptionalFields(), // ActivityEntryOptionalFields | 
  'entryFields': new VocaDbWeb.EntryOptionalFields(), // EntryOptionalFields | 
  'lang': new VocaDbWeb.ContentLanguagePreference(), // ContentLanguagePreference | 
  'sortRule': new VocaDbWeb.ActivityEntrySortRule() // ActivityEntrySortRule | 
};
apiInstance.apiActivityEntriesGet(opts, (error, data, response) => {
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
 **before** | **Date**|  | [optional] 
 **since** | **Date**|  | [optional] 
 **userId** | **Number**|  | [optional] 
 **editEvent** | [**EntryEditEvent**](.md)|  | [optional] 
 **entryType** | [**EntryType**](.md)|  | [optional] 
 **maxResults** | **Number**|  | [optional] [default to 50]
 **getTotalCount** | **Boolean**|  | [optional] [default to false]
 **fields** | [**ActivityEntryOptionalFields**](.md)|  | [optional] 
 **entryFields** | [**EntryOptionalFields**](.md)|  | [optional] 
 **lang** | [**ContentLanguagePreference**](.md)|  | [optional] 
 **sortRule** | [**ActivityEntrySortRule**](.md)|  | [optional] 

### Return type

[**ActivityEntryForApiContractPartialFindResult**](ActivityEntryForApiContractPartialFindResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

