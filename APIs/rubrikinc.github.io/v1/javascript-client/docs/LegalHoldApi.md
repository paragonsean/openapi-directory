# RubrikRestApi.LegalHoldApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**applyLegalHold**](LegalHoldApi.md#applyLegalHold) | **POST** /legal_hold/snapshot | Apply a Legal Hold
[**dissolveLegalHoldSnapshots**](LegalHoldApi.md#dissolveLegalHoldSnapshots) | **POST** /legal_hold/object/{id}/dissolve | Dissolve a collection of snapshots of specified data source from Legal Hold
[**getLegalHoldObjects**](LegalHoldApi.md#getLegalHoldObjects) | **GET** /legal_hold/object | Get objects part of Legal Hold
[**queryLegalHold**](LegalHoldApi.md#queryLegalHold) | **GET** /legal_hold/snapshot | Get snasphots held under legal hold



## applyLegalHold

> LegalHoldSummary applyLegalHold(applyLegalHoldDefinition)

Apply a Legal Hold

Places a snapshot on legal hold by specifying the hold requirements.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.LegalHoldApi();
let applyLegalHoldDefinition = new RubrikRestApi.ApplyLegalHoldDefinition(); // ApplyLegalHoldDefinition | 
apiInstance.applyLegalHold(applyLegalHoldDefinition, (error, data, response) => {
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
 **applyLegalHoldDefinition** | [**ApplyLegalHoldDefinition**](ApplyLegalHoldDefinition.md)|  | 

### Return type

[**LegalHoldSummary**](LegalHoldSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dissolveLegalHoldSnapshots

> DissolveLegalHoldResponse dissolveLegalHoldSnapshots(id, dissolveLegalHoldDefinition)

Dissolve a collection of snapshots of specified data source from Legal Hold

Dissolve a collection of snapshots of specified data source from Legal Hold.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.LegalHoldApi();
let id = "id_example"; // String | ID of the data source.
let dissolveLegalHoldDefinition = new RubrikRestApi.DissolveLegalHoldDefinition(); // DissolveLegalHoldDefinition | An object that contains the IDs of the snapshots to remove from legal hold status.
apiInstance.dissolveLegalHoldSnapshots(id, dissolveLegalHoldDefinition, (error, data, response) => {
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
 **id** | **String**| ID of the data source. | 
 **dissolveLegalHoldDefinition** | [**DissolveLegalHoldDefinition**](DissolveLegalHoldDefinition.md)| An object that contains the IDs of the snapshots to remove from legal hold status. | 

### Return type

[**DissolveLegalHoldResponse**](DissolveLegalHoldResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getLegalHoldObjects

> ObjectHoldSummaryListResponse getLegalHoldObjects(opts)

Get objects part of Legal Hold

Returns the object details for object with snapshots under legal hold.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.LegalHoldApi();
let opts = {
  'objectId': "objectId_example", // String | Limit the list to a particular object.
  'limit': 56, // Number | Limit the number of matches returned.
  'offset': 56, // Number | Specifies a number of initial matches to ignore.
  'objectName': "objectName_example", // String | Limits the list to objects that match a specified value for the object name.
  'objectType': "objectType_example", // String | Limits the list to objects that match a specified type.
  'sortBy': "sortBy_example", // String | The attribute used to sort summary information. The optional parameter _sort_order_ specifies ascending or descending sort order.
  'sortOrder': "'asc'" // String | Specifies ascending or descending sort order. Summary results are sorted in ascending order when this parameter is not specified.
};
apiInstance.getLegalHoldObjects(opts, (error, data, response) => {
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
 **objectId** | **String**| Limit the list to a particular object. | [optional] 
 **limit** | **Number**| Limit the number of matches returned. | [optional] 
 **offset** | **Number**| Specifies a number of initial matches to ignore. | [optional] 
 **objectName** | **String**| Limits the list to objects that match a specified value for the object name. | [optional] 
 **objectType** | **String**| Limits the list to objects that match a specified type. | [optional] 
 **sortBy** | **String**| The attribute used to sort summary information. The optional parameter _sort_order_ specifies ascending or descending sort order. | [optional] 
 **sortOrder** | **String**| Specifies ascending or descending sort order. Summary results are sorted in ascending order when this parameter is not specified. | [optional] [default to &#39;asc&#39;]

### Return type

[**ObjectHoldSummaryListResponse**](ObjectHoldSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryLegalHold

> LegalHoldSummaryListResponse queryLegalHold(opts)

Get snasphots held under legal hold

Get summary for snapshots under legal hold. If object_id is passed, return summary information only for snapshots of the object under legal hold else return summary for all snapshots under legal hold.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.LegalHoldApi();
let opts = {
  'objectId': "objectId_example", // String | Limit the list to snapshot for the particular object.
  'limit': 56, // Number | Limit the number of matches returned.
  'offset': 56, // Number | An integer that specifies a number of initial matches to ignore.
  'objectName': "objectName_example", // String | Limits the list to objects that match a specified value for the object name.
  'objectType': "objectType_example", // String | Limits the list to objects that match a specified type.
  'beforeDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Limits the list to snapshots with holds created before a specified date.
  'afterDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Limits the list to snapshots with holds created after a specified date.
  'placedOnHoldBeforeDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Limits the list to snapshots which were placed on legal hold before a specified date.
  'placedOnHoldAfterDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Limits the list to snapshots which were placed on legal hold after a specified date.
  'sortBy': "sortBy_example", // String | The attribute used to sort summary information. The optional parameter **_sort_order_** specifies ascending or descending sort order.
  'sortOrder': "'asc'", // String | Specifies ascending or descending sort order. Summary results are sorted in ascending order when this parameter is not specified.
  'snapshotType': "snapshotType_example" // String | Specifies the type of snapshots to be returned.
};
apiInstance.queryLegalHold(opts, (error, data, response) => {
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
 **objectId** | **String**| Limit the list to snapshot for the particular object. | [optional] 
 **limit** | **Number**| Limit the number of matches returned. | [optional] 
 **offset** | **Number**| An integer that specifies a number of initial matches to ignore. | [optional] 
 **objectName** | **String**| Limits the list to objects that match a specified value for the object name. | [optional] 
 **objectType** | **String**| Limits the list to objects that match a specified type. | [optional] 
 **beforeDate** | **Date**| Limits the list to snapshots with holds created before a specified date. | [optional] 
 **afterDate** | **Date**| Limits the list to snapshots with holds created after a specified date. | [optional] 
 **placedOnHoldBeforeDate** | **Date**| Limits the list to snapshots which were placed on legal hold before a specified date. | [optional] 
 **placedOnHoldAfterDate** | **Date**| Limits the list to snapshots which were placed on legal hold after a specified date. | [optional] 
 **sortBy** | **String**| The attribute used to sort summary information. The optional parameter **_sort_order_** specifies ascending or descending sort order. | [optional] 
 **sortOrder** | **String**| Specifies ascending or descending sort order. Summary results are sorted in ascending order when this parameter is not specified. | [optional] [default to &#39;asc&#39;]
 **snapshotType** | **String**| Specifies the type of snapshots to be returned. | [optional] 

### Return type

[**LegalHoldSummaryListResponse**](LegalHoldSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

