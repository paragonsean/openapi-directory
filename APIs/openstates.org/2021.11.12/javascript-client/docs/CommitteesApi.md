# OpenStatesApiV3.CommitteesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**committeeDetailCommitteesCommitteeIdGet**](CommitteesApi.md#committeeDetailCommitteesCommitteeIdGet) | **GET** /committees/{committee_id} | Committee Detail
[**committeeListCommitteesGet**](CommitteesApi.md#committeeListCommitteesGet) | **GET** /committees | Committee List



## committeeDetailCommitteesCommitteeIdGet

> Committee committeeDetailCommitteesCommitteeIdGet(committeeId, opts)

Committee Detail

Get details on a single committee by ID.

### Example

```javascript
import OpenStatesApiV3 from 'open_states_api_v3';

let apiInstance = new OpenStatesApiV3.CommitteesApi();
let committeeId = "committeeId_example"; // String | 
let opts = {
  'include': [new OpenStatesApiV3.CommitteeInclude()], // [CommitteeInclude] | Additional includes for the Committee response.
  'apikey': "apikey_example", // String | 
  'xApiKey': "xApiKey_example" // String | 
};
apiInstance.committeeDetailCommitteesCommitteeIdGet(committeeId, opts, (error, data, response) => {
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
 **committeeId** | **String**|  | 
 **include** | [**[CommitteeInclude]**](CommitteeInclude.md)| Additional includes for the Committee response. | [optional] 
 **apikey** | **String**|  | [optional] 
 **xApiKey** | **String**|  | [optional] 

### Return type

[**Committee**](Committee.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## committeeListCommitteesGet

> CommitteeList committeeListCommitteesGet(opts)

Committee List

### Example

```javascript
import OpenStatesApiV3 from 'open_states_api_v3';

let apiInstance = new OpenStatesApiV3.CommitteesApi();
let opts = {
  'jurisdiction': "jurisdiction_example", // String | Filter by jurisdiction name or ID.
  'classification': new OpenStatesApiV3.CommitteeClassification(), // CommitteeClassification | 
  'parent': "parent_example", // String | ocd-organization ID of parent committee.
  'chamber': new OpenStatesApiV3.OrgClassification(), // OrgClassification | Chamber of committee, generally upper or lower.
  'include': [new OpenStatesApiV3.CommitteeInclude()], // [CommitteeInclude] | Additional includes for the Committee response.
  'apikey': "apikey_example", // String | 
  'page': 1, // Number | 
  'perPage': 20, // Number | 
  'xApiKey': "xApiKey_example" // String | 
};
apiInstance.committeeListCommitteesGet(opts, (error, data, response) => {
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
 **jurisdiction** | **String**| Filter by jurisdiction name or ID. | [optional] 
 **classification** | [**CommitteeClassification**](.md)|  | [optional] 
 **parent** | **String**| ocd-organization ID of parent committee. | [optional] 
 **chamber** | [**OrgClassification**](.md)| Chamber of committee, generally upper or lower. | [optional] 
 **include** | [**[CommitteeInclude]**](CommitteeInclude.md)| Additional includes for the Committee response. | [optional] 
 **apikey** | **String**|  | [optional] 
 **page** | **Number**|  | [optional] [default to 1]
 **perPage** | **Number**|  | [optional] [default to 20]
 **xApiKey** | **String**|  | [optional] 

### Return type

[**CommitteeList**](CommitteeList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

