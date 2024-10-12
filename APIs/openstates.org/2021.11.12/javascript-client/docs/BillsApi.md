# OpenStatesApiV3.BillsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**billDetailBillsJurisdictionSessionBillIdGet**](BillsApi.md#billDetailBillsJurisdictionSessionBillIdGet) | **GET** /bills/{jurisdiction}/{session}/{bill_id} | Bill Detail
[**billDetailByIdBillsOcdBillOpenstatesBillIdGet**](BillsApi.md#billDetailByIdBillsOcdBillOpenstatesBillIdGet) | **GET** /bills/ocd-bill/{openstates_bill_id} | Bill Detail By Id
[**billsSearchBillsGet**](BillsApi.md#billsSearchBillsGet) | **GET** /bills | Bills Search



## billDetailBillsJurisdictionSessionBillIdGet

> Bill billDetailBillsJurisdictionSessionBillIdGet(jurisdiction, session, billId, opts)

Bill Detail

Obtain bill information based on (state, session, bill_id).

### Example

```javascript
import OpenStatesApiV3 from 'open_states_api_v3';

let apiInstance = new OpenStatesApiV3.BillsApi();
let jurisdiction = "jurisdiction_example"; // String | 
let session = "session_example"; // String | 
let billId = "billId_example"; // String | 
let opts = {
  'include': [new OpenStatesApiV3.BillInclude()], // [BillInclude] | 
  'apikey': "apikey_example", // String | 
  'xApiKey': "xApiKey_example" // String | 
};
apiInstance.billDetailBillsJurisdictionSessionBillIdGet(jurisdiction, session, billId, opts, (error, data, response) => {
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
 **jurisdiction** | **String**|  | 
 **session** | **String**|  | 
 **billId** | **String**|  | 
 **include** | [**[BillInclude]**](BillInclude.md)|  | [optional] 
 **apikey** | **String**|  | [optional] 
 **xApiKey** | **String**|  | [optional] 

### Return type

[**Bill**](Bill.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## billDetailByIdBillsOcdBillOpenstatesBillIdGet

> Bill billDetailByIdBillsOcdBillOpenstatesBillIdGet(openstatesBillId, opts)

Bill Detail By Id

Obtain bill information by internal ID in the format ocd-bill/_*uuid*.

### Example

```javascript
import OpenStatesApiV3 from 'open_states_api_v3';

let apiInstance = new OpenStatesApiV3.BillsApi();
let openstatesBillId = "openstatesBillId_example"; // String | 
let opts = {
  'include': [new OpenStatesApiV3.BillInclude()], // [BillInclude] | 
  'apikey': "apikey_example", // String | 
  'xApiKey': "xApiKey_example" // String | 
};
apiInstance.billDetailByIdBillsOcdBillOpenstatesBillIdGet(openstatesBillId, opts, (error, data, response) => {
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
 **openstatesBillId** | **String**|  | 
 **include** | [**[BillInclude]**](BillInclude.md)|  | [optional] 
 **apikey** | **String**|  | [optional] 
 **xApiKey** | **String**|  | [optional] 

### Return type

[**Bill**](Bill.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## billsSearchBillsGet

> BillList billsSearchBillsGet(opts)

Bills Search

Search for bills matching given criteria.  Must either specify a jurisdiction or a full text query (q).  Additional parameters will futher restrict bills returned.

### Example

```javascript
import OpenStatesApiV3 from 'open_states_api_v3';

let apiInstance = new OpenStatesApiV3.BillsApi();
let opts = {
  'jurisdiction': "jurisdiction_example", // String | Filter by jurisdiction name or ID.
  'session': "session_example", // String | Filter by session identifier.
  'chamber': "chamber_example", // String | Filter by chamber of origination.
  'identifier': ["null"], // [String] | Filter to only include bills with this identifier.
  'classification': "classification_example", // String | Filter by classification, e.g. bill or resolution
  'subject': ["null"], // [String] | Filter by one or more subjects.
  'updatedSince': "updatedSince_example", // String | Filter to only include bills with updates since a given date.
  'createdSince': "createdSince_example", // String | Filter to only include bills created since a given date.
  'actionSince': "actionSince_example", // String | Filter to only include bills with an action since a given date.
  'sort': new OpenStatesApiV3.BillSortOption(), // BillSortOption | Desired sort order for bill results.
  'sponsor': "sponsor_example", // String | Filter to only include bills sponsored by a given name or person ID.
  'sponsorClassification': "sponsorClassification_example", // String | Filter matched sponsors to only include particular types of sponsorships.
  'q': "q_example", // String | Filter by full text search term.
  'include': [new OpenStatesApiV3.BillInclude()], // [BillInclude] | Additional information to include in response.
  'page': 1, // Number | 
  'perPage': 10, // Number | 
  'apikey': "apikey_example", // String | 
  'xApiKey': "xApiKey_example" // String | 
};
apiInstance.billsSearchBillsGet(opts, (error, data, response) => {
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
 **session** | **String**| Filter by session identifier. | [optional] 
 **chamber** | **String**| Filter by chamber of origination. | [optional] 
 **identifier** | [**[String]**](String.md)| Filter to only include bills with this identifier. | [optional] 
 **classification** | **String**| Filter by classification, e.g. bill or resolution | [optional] 
 **subject** | [**[String]**](String.md)| Filter by one or more subjects. | [optional] 
 **updatedSince** | **String**| Filter to only include bills with updates since a given date. | [optional] 
 **createdSince** | **String**| Filter to only include bills created since a given date. | [optional] 
 **actionSince** | **String**| Filter to only include bills with an action since a given date. | [optional] 
 **sort** | [**BillSortOption**](.md)| Desired sort order for bill results. | [optional] 
 **sponsor** | **String**| Filter to only include bills sponsored by a given name or person ID. | [optional] 
 **sponsorClassification** | **String**| Filter matched sponsors to only include particular types of sponsorships. | [optional] 
 **q** | **String**| Filter by full text search term. | [optional] 
 **include** | [**[BillInclude]**](BillInclude.md)| Additional information to include in response. | [optional] 
 **page** | **Number**|  | [optional] [default to 1]
 **perPage** | **Number**|  | [optional] [default to 10]
 **apikey** | **String**|  | [optional] 
 **xApiKey** | **String**|  | [optional] 

### Return type

[**BillList**](BillList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

