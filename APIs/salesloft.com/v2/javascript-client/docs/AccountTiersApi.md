# SalesLoftPlatform.AccountTiersApi

All URIs are relative to *https://api.salesloft.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2AccountTiersIdJsonGet**](AccountTiersApi.md#v2AccountTiersIdJsonGet) | **GET** /v2/account_tiers/{id}.json | Fetch an account tier
[**v2AccountTiersJsonGet**](AccountTiersApi.md#v2AccountTiersJsonGet) | **GET** /v2/account_tiers.json | List Account Tiers



## v2AccountTiersIdJsonGet

> AccountTier v2AccountTiersIdJsonGet(id)

Fetch an account tier

Fetches an account tier, by ID only. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.AccountTiersApi();
let id = "id_example"; // String | Account Tier ID
apiInstance.v2AccountTiersIdJsonGet(id, (error, data, response) => {
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
 **id** | **String**| Account Tier ID | 

### Return type

[**AccountTier**](AccountTier.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## v2AccountTiersJsonGet

> [AccountTier] v2AccountTiersJsonGet(opts)

List Account Tiers

Fetches multiple account tier records. The records can be filtered, paged, and sorted according to the respective parameters. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.AccountTiersApi();
let opts = {
  'ids': [null], // [Number] | IDs of Account Tiers to fetch. If a record can't be found, that record won't be returned and your request will be successful
  'name': ["null"], // [String] | Filters Account Tiers by name. Multiple names can be applied
  'sortBy': "sortBy_example", // String | Key to sort on, must be one of: created_at, updated_at, order. Defaults to updated_at
  'sortDirection': "sortDirection_example", // String | Direction to sort in, must be one of: ASC, DESC. Defaults to DESC
  'perPage': 56, // Number | How many records to show per page in the range [1, 100]. Defaults to 25
  'page': 56, // Number | The current page to fetch results from. Defaults to 1
  'includePagingCounts': true, // Boolean | Whether to include total_pages and total_count in the metadata. Defaults to false
  'limitPagingCounts': true // Boolean | Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data
};
apiInstance.v2AccountTiersJsonGet(opts, (error, data, response) => {
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
 **ids** | [**[Number]**](Number.md)| IDs of Account Tiers to fetch. If a record can&#39;t be found, that record won&#39;t be returned and your request will be successful | [optional] 
 **name** | [**[String]**](String.md)| Filters Account Tiers by name. Multiple names can be applied | [optional] 
 **sortBy** | **String**| Key to sort on, must be one of: created_at, updated_at, order. Defaults to updated_at | [optional] 
 **sortDirection** | **String**| Direction to sort in, must be one of: ASC, DESC. Defaults to DESC | [optional] 
 **perPage** | **Number**| How many records to show per page in the range [1, 100]. Defaults to 25 | [optional] 
 **page** | **Number**| The current page to fetch results from. Defaults to 1 | [optional] 
 **includePagingCounts** | **Boolean**| Whether to include total_pages and total_count in the metadata. Defaults to false | [optional] 
 **limitPagingCounts** | **Boolean**| Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data | [optional] 

### Return type

[**[AccountTier]**](AccountTier.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

