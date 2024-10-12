# BioLinkApi.CamApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getActivityCollection**](CamApi.md#getActivityCollection) | **GET** /cam/activity | Returns list of models
[**getInstanceObject**](CamApi.md#getInstanceObject) | **GET** /cam/instance/{id} | Returns list of matches
[**getModelCollection**](CamApi.md#getModelCollection) | **GET** /cam/model | Returns list of ALL models
[**getModelContributors**](CamApi.md#getModelContributors) | **GET** /cam/model/contributors | Returns list of all contributors across all models
[**getModelInstances**](CamApi.md#getModelInstances) | **GET** /cam/instances | Returns list of all instances
[**getModelObject**](CamApi.md#getModelObject) | **GET** /cam/model/{id} | Returns a complete model
[**getModelProperties**](CamApi.md#getModelProperties) | **GET** /cam/model/properties | Returns list of all properties used across all models
[**getModelPropertyValues**](CamApi.md#getModelPropertyValues) | **GET** /cam/model/property_values | Returns list property-values for all models
[**getModelQuery**](CamApi.md#getModelQuery) | **GET** /cam/model/query | Returns list of models matching query
[**getPhysicalInteraction**](CamApi.md#getPhysicalInteraction) | **GET** /cam/physical_interaction | Returns list of models



## getActivityCollection

> getActivityCollection(opts)

Returns list of models

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.CamApi();
let opts = {
  'title': "title_example", // String | string to search for in title of model
  'contributor': "contributor_example" // String | string to search for in contributor of model
};
apiInstance.getActivityCollection(opts, (error, data, response) => {
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
 **title** | **String**| string to search for in title of model | [optional] 
 **contributor** | **String**| string to search for in contributor of model | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getInstanceObject

> [Association] getInstanceObject(id, opts)

Returns list of matches

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.CamApi();
let id = "id_example"; // String | 
let opts = {
  'title': "title_example", // String | string to search for in title of model
  'contributor': "contributor_example" // String | string to search for in contributor of model
};
apiInstance.getInstanceObject(id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **title** | **String**| string to search for in title of model | [optional] 
 **contributor** | **String**| string to search for in contributor of model | [optional] 

### Return type

[**[Association]**](Association.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getModelCollection

> getModelCollection()

Returns list of ALL models

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.CamApi();
apiInstance.getModelCollection((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getModelContributors

> getModelContributors()

Returns list of all contributors across all models

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.CamApi();
apiInstance.getModelContributors((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getModelInstances

> getModelInstances()

Returns list of all instances

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.CamApi();
apiInstance.getModelInstances((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getModelObject

> getModelObject(id)

Returns a complete model

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.CamApi();
let id = "id_example"; // String | 
apiInstance.getModelObject(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getModelProperties

> getModelProperties(opts)

Returns list of all properties used across all models

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.CamApi();
let opts = {
  'title': "title_example", // String | string to search for in title of model
  'contributor': "contributor_example" // String | string to search for in contributor of model
};
apiInstance.getModelProperties(opts, (error, data, response) => {
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
 **title** | **String**| string to search for in title of model | [optional] 
 **contributor** | **String**| string to search for in contributor of model | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getModelPropertyValues

> getModelPropertyValues(opts)

Returns list property-values for all models

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.CamApi();
let opts = {
  'title': "title_example", // String | string to search for in title of model
  'contributor': "contributor_example" // String | string to search for in contributor of model
};
apiInstance.getModelPropertyValues(opts, (error, data, response) => {
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
 **title** | **String**| string to search for in title of model | [optional] 
 **contributor** | **String**| string to search for in contributor of model | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getModelQuery

> getModelQuery(opts)

Returns list of models matching query

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.CamApi();
let opts = {
  'title': "title_example", // String | string to search for in title of model
  'contributor': "contributor_example" // String | string to search for in contributor of model
};
apiInstance.getModelQuery(opts, (error, data, response) => {
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
 **title** | **String**| string to search for in title of model | [optional] 
 **contributor** | **String**| string to search for in contributor of model | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getPhysicalInteraction

> getPhysicalInteraction(opts)

Returns list of models

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.CamApi();
let opts = {
  'title': "title_example", // String | string to search for in title of model
  'contributor': "contributor_example" // String | string to search for in contributor of model
};
apiInstance.getPhysicalInteraction(opts, (error, data, response) => {
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
 **title** | **String**| string to search for in title of model | [optional] 
 **contributor** | **String**| string to search for in contributor of model | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

