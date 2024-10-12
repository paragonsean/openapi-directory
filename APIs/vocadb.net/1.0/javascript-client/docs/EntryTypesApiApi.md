# VocaDbWeb.EntryTypesApiApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiEntryTypesEntryTypeSubTypeTagGet**](EntryTypesApiApi.md#apiEntryTypesEntryTypeSubTypeTagGet) | **GET** /api/entry-types/{entryType}/{subType}/tag | 



## apiEntryTypesEntryTypeSubTypeTagGet

> TagForApiContract apiEntryTypesEntryTypeSubTypeTagGet(entryType, subType, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.EntryTypesApiApi();
let entryType = new VocaDbWeb.EntryType(); // EntryType | 
let subType = "subType_example"; // String | 
let opts = {
  'fields': new VocaDbWeb.TagOptionalFields() // TagOptionalFields | 
};
apiInstance.apiEntryTypesEntryTypeSubTypeTagGet(entryType, subType, opts, (error, data, response) => {
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
 **entryType** | [**EntryType**](.md)|  | 
 **subType** | **String**|  | 
 **fields** | [**TagOptionalFields**](.md)|  | [optional] 

### Return type

[**TagForApiContract**](TagForApiContract.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

