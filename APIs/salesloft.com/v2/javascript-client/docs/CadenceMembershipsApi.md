# SalesLoftPlatform.CadenceMembershipsApi

All URIs are relative to *https://api.salesloft.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2CadenceMembershipsIdJsonDelete**](CadenceMembershipsApi.md#v2CadenceMembershipsIdJsonDelete) | **DELETE** /v2/cadence_memberships/{id}.json | Delete a cadence membership
[**v2CadenceMembershipsIdJsonGet**](CadenceMembershipsApi.md#v2CadenceMembershipsIdJsonGet) | **GET** /v2/cadence_memberships/{id}.json | Fetch a cadence membership
[**v2CadenceMembershipsJsonGet**](CadenceMembershipsApi.md#v2CadenceMembershipsJsonGet) | **GET** /v2/cadence_memberships.json | List cadence memberships
[**v2CadenceMembershipsJsonPost**](CadenceMembershipsApi.md#v2CadenceMembershipsJsonPost) | **POST** /v2/cadence_memberships.json | Create a cadence membership



## v2CadenceMembershipsIdJsonDelete

> v2CadenceMembershipsIdJsonDelete(id)

Delete a cadence membership

Cadence Membership 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.CadenceMembershipsApi();
let id = "id_example"; // String | CadenceMembership ID
apiInstance.v2CadenceMembershipsIdJsonDelete(id, (error, data, response) => {
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
 **id** | **String**| CadenceMembership ID | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## v2CadenceMembershipsIdJsonGet

> CadenceMembership v2CadenceMembershipsIdJsonGet(id)

Fetch a cadence membership

Fetches a cadence membership, by ID only. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.CadenceMembershipsApi();
let id = "id_example"; // String | CadenceMembership ID
apiInstance.v2CadenceMembershipsIdJsonGet(id, (error, data, response) => {
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
 **id** | **String**| CadenceMembership ID | 

### Return type

[**CadenceMembership**](CadenceMembership.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## v2CadenceMembershipsJsonGet

> [CadenceMembership] v2CadenceMembershipsJsonGet(opts)

List cadence memberships

Fetches multiple cadence membership records. The records can be filtered, paged, and sorted according to the respective parameters. A cadence membership is the association between a person and their current and historical time on a cadence. Cadence membership records are mutable and change over time. If a person is added to a cadence and re-added to the same cadence in the future, there is a single membership record. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.CadenceMembershipsApi();
let opts = {
  'ids': [null], // [Number] | IDs of cadence memberships to fetch. If a record can't be found, that record won't be returned and your request will be successful
  'personId': 56, // Number | ID of the person to find cadence memberships for
  'cadenceId': 56, // Number | ID of the cadence to find cadence memberships for
  'updatedAt': ["null"], // [String] | Equality filters that are applied to the updated_at field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\"type\":\"object\",\"keys\":[{\"name\":\"gt\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"gte\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"lt\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"lte\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\"}]} 
  'currentlyOnCadence': true, // Boolean | If true, return only cadence memberships for people currently on cadences.  If false, return cadence memberships for people who have been removed from or have completed a cadence.
  'sortBy': "sortBy_example", // String | Key to sort on, must be one of: added_at, updated_at. Defaults to updated_at
  'sortDirection': "sortDirection_example", // String | Direction to sort in, must be one of: ASC, DESC. Defaults to DESC
  'perPage': 56, // Number | How many records to show per page in the range [1, 100]. Defaults to 25
  'page': 56, // Number | The current page to fetch results from. Defaults to 1
  'includePagingCounts': true, // Boolean | Whether to include total_pages and total_count in the metadata. Defaults to false
  'limitPagingCounts': true // Boolean | Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data
};
apiInstance.v2CadenceMembershipsJsonGet(opts, (error, data, response) => {
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
 **ids** | [**[Number]**](Number.md)| IDs of cadence memberships to fetch. If a record can&#39;t be found, that record won&#39;t be returned and your request will be successful | [optional] 
 **personId** | **Number**| ID of the person to find cadence memberships for | [optional] 
 **cadenceId** | **Number**| ID of the cadence to find cadence memberships for | [optional] 
 **updatedAt** | [**[String]**](String.md)| Equality filters that are applied to the updated_at field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\&quot;type\&quot;:\&quot;object\&quot;,\&quot;keys\&quot;:[{\&quot;name\&quot;:\&quot;gt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;gte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;}]}  | [optional] 
 **currentlyOnCadence** | **Boolean**| If true, return only cadence memberships for people currently on cadences.  If false, return cadence memberships for people who have been removed from or have completed a cadence. | [optional] 
 **sortBy** | **String**| Key to sort on, must be one of: added_at, updated_at. Defaults to updated_at | [optional] 
 **sortDirection** | **String**| Direction to sort in, must be one of: ASC, DESC. Defaults to DESC | [optional] 
 **perPage** | **Number**| How many records to show per page in the range [1, 100]. Defaults to 25 | [optional] 
 **page** | **Number**| The current page to fetch results from. Defaults to 1 | [optional] 
 **includePagingCounts** | **Boolean**| Whether to include total_pages and total_count in the metadata. Defaults to false | [optional] 
 **limitPagingCounts** | **Boolean**| Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data | [optional] 

### Return type

[**[CadenceMembership]**](CadenceMembership.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## v2CadenceMembershipsJsonPost

> CadenceMembership v2CadenceMembershipsJsonPost(personId, cadenceId, opts)

Create a cadence membership

Adds a person to a cadence. person_id and cadence_id are required, and must be visible to the authenticated user. user_id will default to the authenticated user, but can be set to any visible user on the authenticated team.  A person cannot be added to a cadence on behalf of a teammate unless the cadence is a team cadence, the cadence is owned by the teammate, or the teammate has the Personal Cadence Admin permission. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.CadenceMembershipsApi();
let personId = 56; // Number | ID of the person to create a cadence membership for
let cadenceId = 56; // Number | ID of the cadence to create a cadence membership for
let opts = {
  'userId': 56, // Number | ID of the user to create a cadence membership for. The associated cadence must be owned by the user, or it must be a team cadence
  'stepId': 56 // Number | ID of the step on which the person should start the cadence. Start on first step is the default behavior without this parameter.
};
apiInstance.v2CadenceMembershipsJsonPost(personId, cadenceId, opts, (error, data, response) => {
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
 **personId** | **Number**| ID of the person to create a cadence membership for | 
 **cadenceId** | **Number**| ID of the cadence to create a cadence membership for | 
 **userId** | **Number**| ID of the user to create a cadence membership for. The associated cadence must be owned by the user, or it must be a team cadence | [optional] 
 **stepId** | **Number**| ID of the step on which the person should start the cadence. Start on first step is the default behavior without this parameter. | [optional] 

### Return type

[**CadenceMembership**](CadenceMembership.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

