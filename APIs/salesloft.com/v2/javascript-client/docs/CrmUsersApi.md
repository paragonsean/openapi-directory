# SalesLoftPlatform.CrmUsersApi

All URIs are relative to *https://api.salesloft.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2CrmUsersJsonGet**](CrmUsersApi.md#v2CrmUsersJsonGet) | **GET** /v2/crm_users.json | List crm users



## v2CrmUsersJsonGet

> [CrmUser] v2CrmUsersJsonGet(opts)

List crm users

Crm Users 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.CrmUsersApi();
let opts = {
  'ids': [null], // [Number] | IDs of crm users to fetch. If a record can't be found, that record won't be returned and your request will be successful
  'crmId': ["null"], // [String] | Filters crm users by crm_ids
  'userId': [null], // [Number] | Filters crm users by user_ids
  'userGuid': ["null"], // [String] | Filters crm users by user guids
  'perPage': 56, // Number | How many records to show per page in the range [1, 100]. Defaults to 25
  'page': 56, // Number | The current page to fetch results from. Defaults to 1
  'includePagingCounts': true, // Boolean | Whether to include total_pages and total_count in the metadata. Defaults to false
  'limitPagingCounts': true, // Boolean | Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data
  'sortBy': "sortBy_example", // String | Key to sort on, must be one of: id, updated_at. Defaults to id
  'sortDirection': "sortDirection_example" // String | Direction to sort in, must be one of: ASC, DESC. Defaults to DESC
};
apiInstance.v2CrmUsersJsonGet(opts, (error, data, response) => {
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
 **ids** | [**[Number]**](Number.md)| IDs of crm users to fetch. If a record can&#39;t be found, that record won&#39;t be returned and your request will be successful | [optional] 
 **crmId** | [**[String]**](String.md)| Filters crm users by crm_ids | [optional] 
 **userId** | [**[Number]**](Number.md)| Filters crm users by user_ids | [optional] 
 **userGuid** | [**[String]**](String.md)| Filters crm users by user guids | [optional] 
 **perPage** | **Number**| How many records to show per page in the range [1, 100]. Defaults to 25 | [optional] 
 **page** | **Number**| The current page to fetch results from. Defaults to 1 | [optional] 
 **includePagingCounts** | **Boolean**| Whether to include total_pages and total_count in the metadata. Defaults to false | [optional] 
 **limitPagingCounts** | **Boolean**| Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data | [optional] 
 **sortBy** | **String**| Key to sort on, must be one of: id, updated_at. Defaults to id | [optional] 
 **sortDirection** | **String**| Direction to sort in, must be one of: ASC, DESC. Defaults to DESC | [optional] 

### Return type

[**[CrmUser]**](CrmUser.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

