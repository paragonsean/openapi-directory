# SalesLoftPlatform.CadencesApi

All URIs are relative to *https://api.salesloft.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2CadencesIdJsonGet**](CadencesApi.md#v2CadencesIdJsonGet) | **GET** /v2/cadences/{id}.json | Fetch a cadence
[**v2CadencesJsonGet**](CadencesApi.md#v2CadencesJsonGet) | **GET** /v2/cadences.json | List cadences



## v2CadencesIdJsonGet

> Cadence v2CadencesIdJsonGet(id)

Fetch a cadence

Fetches a cadence, by ID only. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.CadencesApi();
let id = "id_example"; // String | Cadence ID
apiInstance.v2CadencesIdJsonGet(id, (error, data, response) => {
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
 **id** | **String**| Cadence ID | 

### Return type

[**Cadence**](Cadence.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## v2CadencesJsonGet

> [Cadence] v2CadencesJsonGet(opts)

List cadences

Fetches multiple cadence records. The records can be filtered, paged, and sorted according to the respective parameters. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.CadencesApi();
let opts = {
  'ids': [null], // [Number] | IDs of cadences to fetch. If a record can't be found, that record won't be returned and your request will be successful
  'updatedAt': ["null"], // [String] | Equality filters that are applied to the updated_at field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\"type\":\"object\",\"keys\":[{\"name\":\"gt\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"gte\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"lt\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"lte\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\"}]} 
  'teamCadence': true, // Boolean | Filters cadences by whether they are a team cadence or not
  'shared': true, // Boolean | Filters cadences by whether they are shared
  'ownedByGuid': ["null"], // [String] | Filters cadences by the owner's guid. Multiple owner guids can be applied
  'peopleAddable': true, // Boolean | Filters cadences by whether they are able to have people added to them
  'name': ["null"], // [String] | Filters cadences by name
  'groupIds': "groupIds_example", // String | Filters by group ids. Also supports group ids passed in as a JSON array string
  'archived': true, // Boolean | Filters by whether the Cadences have been archived. Excluding this field will result in both archived and unarchived Cadences to return.
  'sortBy': "sortBy_example", // String | Key to sort on, must be one of: created_at, updated_at, name. Defaults to updated_at
  'sortDirection': "sortDirection_example", // String | Direction to sort in, must be one of: ASC, DESC. Defaults to DESC
  'perPage': 56, // Number | How many records to show per page in the range [1, 100]. Defaults to 25
  'page': 56, // Number | The current page to fetch results from. Defaults to 1
  'includePagingCounts': true, // Boolean | Whether to include total_pages and total_count in the metadata. Defaults to false
  'limitPagingCounts': true // Boolean | Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data
};
apiInstance.v2CadencesJsonGet(opts, (error, data, response) => {
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
 **ids** | [**[Number]**](Number.md)| IDs of cadences to fetch. If a record can&#39;t be found, that record won&#39;t be returned and your request will be successful | [optional] 
 **updatedAt** | [**[String]**](String.md)| Equality filters that are applied to the updated_at field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\&quot;type\&quot;:\&quot;object\&quot;,\&quot;keys\&quot;:[{\&quot;name\&quot;:\&quot;gt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;gte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;}]}  | [optional] 
 **teamCadence** | **Boolean**| Filters cadences by whether they are a team cadence or not | [optional] 
 **shared** | **Boolean**| Filters cadences by whether they are shared | [optional] 
 **ownedByGuid** | [**[String]**](String.md)| Filters cadences by the owner&#39;s guid. Multiple owner guids can be applied | [optional] 
 **peopleAddable** | **Boolean**| Filters cadences by whether they are able to have people added to them | [optional] 
 **name** | [**[String]**](String.md)| Filters cadences by name | [optional] 
 **groupIds** | **String**| Filters by group ids. Also supports group ids passed in as a JSON array string | [optional] 
 **archived** | **Boolean**| Filters by whether the Cadences have been archived. Excluding this field will result in both archived and unarchived Cadences to return. | [optional] 
 **sortBy** | **String**| Key to sort on, must be one of: created_at, updated_at, name. Defaults to updated_at | [optional] 
 **sortDirection** | **String**| Direction to sort in, must be one of: ASC, DESC. Defaults to DESC | [optional] 
 **perPage** | **Number**| How many records to show per page in the range [1, 100]. Defaults to 25 | [optional] 
 **page** | **Number**| The current page to fetch results from. Defaults to 1 | [optional] 
 **includePagingCounts** | **Boolean**| Whether to include total_pages and total_count in the metadata. Defaults to false | [optional] 
 **limitPagingCounts** | **Boolean**| Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data | [optional] 

### Return type

[**[Cadence]**](Cadence.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

