# InfluxOssApiService.BucketsApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteBucketsID**](BucketsApi.md#deleteBucketsID) | **DELETE** /buckets/{bucketID} | Delete a bucket
[**deleteBucketsIDLabelsID**](BucketsApi.md#deleteBucketsIDLabelsID) | **DELETE** /buckets/{bucketID}/labels/{labelID} | Delete a label from a bucket
[**deleteBucketsIDMembersID**](BucketsApi.md#deleteBucketsIDMembersID) | **DELETE** /buckets/{bucketID}/members/{userID} | Remove a member from a bucket
[**deleteBucketsIDOwnersID**](BucketsApi.md#deleteBucketsIDOwnersID) | **DELETE** /buckets/{bucketID}/owners/{userID} | Remove an owner from a bucket
[**getBuckets**](BucketsApi.md#getBuckets) | **GET** /buckets | List all buckets
[**getBucketsID**](BucketsApi.md#getBucketsID) | **GET** /buckets/{bucketID} | Retrieve a bucket
[**getBucketsIDLabels**](BucketsApi.md#getBucketsIDLabels) | **GET** /buckets/{bucketID}/labels | List all labels for a bucket
[**getBucketsIDMembers**](BucketsApi.md#getBucketsIDMembers) | **GET** /buckets/{bucketID}/members | List all users with member privileges for a bucket
[**getBucketsIDOwners**](BucketsApi.md#getBucketsIDOwners) | **GET** /buckets/{bucketID}/owners | List all owners of a bucket
[**getSourcesIDBuckets_0**](BucketsApi.md#getSourcesIDBuckets_0) | **GET** /sources/{sourceID}/buckets | Get buckets in a source
[**patchBucketsID**](BucketsApi.md#patchBucketsID) | **PATCH** /buckets/{bucketID} | Update a bucket
[**postBuckets**](BucketsApi.md#postBuckets) | **POST** /buckets | Create a bucket
[**postBucketsIDLabels**](BucketsApi.md#postBucketsIDLabels) | **POST** /buckets/{bucketID}/labels | Add a label to a bucket
[**postBucketsIDMembers**](BucketsApi.md#postBucketsIDMembers) | **POST** /buckets/{bucketID}/members | Add a member to a bucket
[**postBucketsIDOwners**](BucketsApi.md#postBucketsIDOwners) | **POST** /buckets/{bucketID}/owners | Add an owner to a bucket



## deleteBucketsID

> deleteBucketsID(bucketID, opts)

Delete a bucket

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.BucketsApi();
let bucketID = "bucketID_example"; // String | The ID of the bucket to delete.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.deleteBucketsID(bucketID, opts, (error, data, response) => {
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
 **bucketID** | **String**| The ID of the bucket to delete. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteBucketsIDLabelsID

> deleteBucketsIDLabelsID(bucketID, labelID, opts)

Delete a label from a bucket

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.BucketsApi();
let bucketID = "bucketID_example"; // String | The bucket ID.
let labelID = "labelID_example"; // String | The ID of the label to delete.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.deleteBucketsIDLabelsID(bucketID, labelID, opts, (error, data, response) => {
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
 **bucketID** | **String**| The bucket ID. | 
 **labelID** | **String**| The ID of the label to delete. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteBucketsIDMembersID

> deleteBucketsIDMembersID(userID, bucketID, opts)

Remove a member from a bucket

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.BucketsApi();
let userID = "userID_example"; // String | The ID of the member to remove.
let bucketID = "bucketID_example"; // String | The bucket ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.deleteBucketsIDMembersID(userID, bucketID, opts, (error, data, response) => {
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
 **userID** | **String**| The ID of the member to remove. | 
 **bucketID** | **String**| The bucket ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteBucketsIDOwnersID

> deleteBucketsIDOwnersID(userID, bucketID, opts)

Remove an owner from a bucket

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.BucketsApi();
let userID = "userID_example"; // String | The ID of the owner to remove.
let bucketID = "bucketID_example"; // String | The bucket ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.deleteBucketsIDOwnersID(userID, bucketID, opts, (error, data, response) => {
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
 **userID** | **String**| The ID of the owner to remove. | 
 **bucketID** | **String**| The bucket ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBuckets

> Buckets getBuckets(opts)

List all buckets

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.BucketsApi();
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}", // String | OpenTracing span context
  'offset': 56, // Number | 
  'limit': 20, // Number | 
  'after': "after_example", // String | The last resource ID from which to seek from (but not including). This is to be used instead of `offset`. 
  'org': "org_example", // String | The name of the organization.
  'orgID': "orgID_example", // String | The organization ID.
  'name': "name_example", // String | Only returns buckets with a specific name.
  'id': "id_example" // String | Only returns buckets with a specific ID.
};
apiInstance.getBuckets(opts, (error, data, response) => {
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
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 
 **offset** | **Number**|  | [optional] 
 **limit** | **Number**|  | [optional] [default to 20]
 **after** | **String**| The last resource ID from which to seek from (but not including). This is to be used instead of &#x60;offset&#x60;.  | [optional] 
 **org** | **String**| The name of the organization. | [optional] 
 **orgID** | **String**| The organization ID. | [optional] 
 **name** | **String**| Only returns buckets with a specific name. | [optional] 
 **id** | **String**| Only returns buckets with a specific ID. | [optional] 

### Return type

[**Buckets**](Buckets.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBucketsID

> Bucket getBucketsID(bucketID, opts)

Retrieve a bucket

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.BucketsApi();
let bucketID = "bucketID_example"; // String | The bucket ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.getBucketsID(bucketID, opts, (error, data, response) => {
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
 **bucketID** | **String**| The bucket ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**Bucket**](Bucket.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBucketsIDLabels

> LabelsResponse getBucketsIDLabels(bucketID, opts)

List all labels for a bucket

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.BucketsApi();
let bucketID = "bucketID_example"; // String | The bucket ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.getBucketsIDLabels(bucketID, opts, (error, data, response) => {
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
 **bucketID** | **String**| The bucket ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**LabelsResponse**](LabelsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBucketsIDMembers

> ResourceMembers getBucketsIDMembers(bucketID, opts)

List all users with member privileges for a bucket

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.BucketsApi();
let bucketID = "bucketID_example"; // String | The bucket ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.getBucketsIDMembers(bucketID, opts, (error, data, response) => {
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
 **bucketID** | **String**| The bucket ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**ResourceMembers**](ResourceMembers.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBucketsIDOwners

> ResourceOwners getBucketsIDOwners(bucketID, opts)

List all owners of a bucket

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.BucketsApi();
let bucketID = "bucketID_example"; // String | The bucket ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.getBucketsIDOwners(bucketID, opts, (error, data, response) => {
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
 **bucketID** | **String**| The bucket ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**ResourceOwners**](ResourceOwners.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSourcesIDBuckets_0

> Buckets getSourcesIDBuckets_0(sourceID, opts)

Get buckets in a source

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.BucketsApi();
let sourceID = "sourceID_example"; // String | The source ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}", // String | OpenTracing span context
  'org': "org_example" // String | The name of the organization.
};
apiInstance.getSourcesIDBuckets_0(sourceID, opts, (error, data, response) => {
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
 **sourceID** | **String**| The source ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 
 **org** | **String**| The name of the organization. | [optional] 

### Return type

[**Buckets**](Buckets.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchBucketsID

> Bucket patchBucketsID(bucketID, patchBucketRequest, opts)

Update a bucket

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.BucketsApi();
let bucketID = "bucketID_example"; // String | The bucket ID.
let patchBucketRequest = new InfluxOssApiService.PatchBucketRequest(); // PatchBucketRequest | Bucket update to apply
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.patchBucketsID(bucketID, patchBucketRequest, opts, (error, data, response) => {
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
 **bucketID** | **String**| The bucket ID. | 
 **patchBucketRequest** | [**PatchBucketRequest**](PatchBucketRequest.md)| Bucket update to apply | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**Bucket**](Bucket.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postBuckets

> Bucket postBuckets(postBucketRequest, opts)

Create a bucket

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.BucketsApi();
let postBucketRequest = new InfluxOssApiService.PostBucketRequest(); // PostBucketRequest | Bucket to create
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.postBuckets(postBucketRequest, opts, (error, data, response) => {
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
 **postBucketRequest** | [**PostBucketRequest**](PostBucketRequest.md)| Bucket to create | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**Bucket**](Bucket.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postBucketsIDLabels

> LabelResponse postBucketsIDLabels(bucketID, labelMapping, opts)

Add a label to a bucket

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.BucketsApi();
let bucketID = "bucketID_example"; // String | The bucket ID.
let labelMapping = new InfluxOssApiService.LabelMapping(); // LabelMapping | Label to add
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.postBucketsIDLabels(bucketID, labelMapping, opts, (error, data, response) => {
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
 **bucketID** | **String**| The bucket ID. | 
 **labelMapping** | [**LabelMapping**](LabelMapping.md)| Label to add | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**LabelResponse**](LabelResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postBucketsIDMembers

> ResourceMember postBucketsIDMembers(bucketID, addResourceMemberRequestBody, opts)

Add a member to a bucket

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.BucketsApi();
let bucketID = "bucketID_example"; // String | The bucket ID.
let addResourceMemberRequestBody = new InfluxOssApiService.AddResourceMemberRequestBody(); // AddResourceMemberRequestBody | User to add as member
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.postBucketsIDMembers(bucketID, addResourceMemberRequestBody, opts, (error, data, response) => {
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
 **bucketID** | **String**| The bucket ID. | 
 **addResourceMemberRequestBody** | [**AddResourceMemberRequestBody**](AddResourceMemberRequestBody.md)| User to add as member | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**ResourceMember**](ResourceMember.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postBucketsIDOwners

> ResourceOwner postBucketsIDOwners(bucketID, addResourceMemberRequestBody, opts)

Add an owner to a bucket

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.BucketsApi();
let bucketID = "bucketID_example"; // String | The bucket ID.
let addResourceMemberRequestBody = new InfluxOssApiService.AddResourceMemberRequestBody(); // AddResourceMemberRequestBody | User to add as owner
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.postBucketsIDOwners(bucketID, addResourceMemberRequestBody, opts, (error, data, response) => {
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
 **bucketID** | **String**| The bucket ID. | 
 **addResourceMemberRequestBody** | [**AddResourceMemberRequestBody**](AddResourceMemberRequestBody.md)| User to add as owner | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**ResourceOwner**](ResourceOwner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

