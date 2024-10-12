# FilesComApi.BehaviorsApi

All URIs are relative to *http://app.files.com/api/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**behaviorListForPath**](BehaviorsApi.md#behaviorListForPath) | **GET** /behaviors/folders/{path} | List Behaviors by path
[**deleteBehaviorsId**](BehaviorsApi.md#deleteBehaviorsId) | **DELETE** /behaviors/{id} | Delete Behavior
[**getBehaviors**](BehaviorsApi.md#getBehaviors) | **GET** /behaviors | List Behaviors
[**getBehaviorsId**](BehaviorsApi.md#getBehaviorsId) | **GET** /behaviors/{id} | Show Behavior
[**patchBehaviorsId**](BehaviorsApi.md#patchBehaviorsId) | **PATCH** /behaviors/{id} | Update Behavior
[**postBehaviors**](BehaviorsApi.md#postBehaviors) | **POST** /behaviors | Create Behavior
[**postBehaviorsWebhookTest**](BehaviorsApi.md#postBehaviorsWebhookTest) | **POST** /behaviors/webhook/test | Test webhook.



## behaviorListForPath

> [BehaviorEntity] behaviorListForPath(path, opts)

List Behaviors by path

List Behaviors by path

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.BehaviorsApi();
let path = "path_example"; // String | Path to operate on.
let opts = {
  'cursor': "cursor_example", // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
  'perPage': 56, // Number | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
  'sortBy': {key: null}, // Object | If set, sort records by the specified field in either `asc` or `desc` direction (e.g. `sort_by[behavior]=desc`). Valid fields are `behavior`.
  'filter': {key: null}, // Object | If set, return records where the specified field is equal to the supplied value. Valid fields are `behavior`.
  'filterPrefix': {key: null}, // Object | If set, return records where the specified field is prefixed by the supplied value. Valid fields are `behavior`.
  'recursive': "recursive_example", // String | Show behaviors above this path?
  'behavior': "behavior_example" // String | DEPRECATED: If set only shows folder behaviors matching this behavior type. Use `filter[behavior]` instead.
};
apiInstance.behaviorListForPath(path, opts, (error, data, response) => {
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
 **path** | **String**| Path to operate on. | 
 **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] 
 **perPage** | **Number**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] 
 **sortBy** | [**Object**](.md)| If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[behavior]&#x3D;desc&#x60;). Valid fields are &#x60;behavior&#x60;. | [optional] 
 **filter** | [**Object**](.md)| If set, return records where the specified field is equal to the supplied value. Valid fields are &#x60;behavior&#x60;. | [optional] 
 **filterPrefix** | [**Object**](.md)| If set, return records where the specified field is prefixed by the supplied value. Valid fields are &#x60;behavior&#x60;. | [optional] 
 **recursive** | **String**| Show behaviors above this path? | [optional] 
 **behavior** | **String**| DEPRECATED: If set only shows folder behaviors matching this behavior type. Use &#x60;filter[behavior]&#x60; instead. | [optional] 

### Return type

[**[BehaviorEntity]**](BehaviorEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteBehaviorsId

> deleteBehaviorsId(id)

Delete Behavior

Delete Behavior

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.BehaviorsApi();
let id = 56; // Number | Behavior ID.
apiInstance.deleteBehaviorsId(id, (error, data, response) => {
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
 **id** | **Number**| Behavior ID. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getBehaviors

> [BehaviorEntity] getBehaviors(opts)

List Behaviors

List Behaviors

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.BehaviorsApi();
let opts = {
  'cursor': "cursor_example", // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
  'perPage': 56, // Number | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
  'sortBy': {key: null}, // Object | If set, sort records by the specified field in either `asc` or `desc` direction (e.g. `sort_by[behavior]=desc`). Valid fields are `behavior`.
  'behavior': "behavior_example", // String | If set, return records where the specified field is equal to the supplied value.
  'filter': {key: null}, // Object | If set, return records where the specified field is equal to the supplied value. Valid fields are `behavior`.
  'filterPrefix': {key: null} // Object | If set, return records where the specified field is prefixed by the supplied value. Valid fields are `behavior`.
};
apiInstance.getBehaviors(opts, (error, data, response) => {
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
 **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] 
 **perPage** | **Number**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] 
 **sortBy** | [**Object**](.md)| If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[behavior]&#x3D;desc&#x60;). Valid fields are &#x60;behavior&#x60;. | [optional] 
 **behavior** | **String**| If set, return records where the specified field is equal to the supplied value. | [optional] 
 **filter** | [**Object**](.md)| If set, return records where the specified field is equal to the supplied value. Valid fields are &#x60;behavior&#x60;. | [optional] 
 **filterPrefix** | [**Object**](.md)| If set, return records where the specified field is prefixed by the supplied value. Valid fields are &#x60;behavior&#x60;. | [optional] 

### Return type

[**[BehaviorEntity]**](BehaviorEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBehaviorsId

> BehaviorEntity getBehaviorsId(id)

Show Behavior

Show Behavior

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.BehaviorsApi();
let id = 56; // Number | Behavior ID.
apiInstance.getBehaviorsId(id, (error, data, response) => {
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
 **id** | **Number**| Behavior ID. | 

### Return type

[**BehaviorEntity**](BehaviorEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchBehaviorsId

> BehaviorEntity patchBehaviorsId(id, opts)

Update Behavior

Update Behavior

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.BehaviorsApi();
let id = 56; // Number | Behavior ID.
let opts = {
  'attachmentDelete': true, // Boolean | If true, will delete the file stored in attachment
  'attachmentFile': "/path/to/file", // File | Certain behaviors may require a file, for instance, the \\\"watermark\\\" behavior requires a watermark image
  'behavior': "behavior_example", // String | Behavior type.
  'description': "description_example", // String | Description for this behavior.
  'name': "name_example", // String | Name for this behavior.
  'path': "path_example", // String | Folder behaviors path.
  'value': "value_example" // String | The value of the folder behavior.  Can be a integer, array, or hash depending on the type of folder behavior. See The Behavior Types section for example values for each type of behavior.
};
apiInstance.patchBehaviorsId(id, opts, (error, data, response) => {
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
 **id** | **Number**| Behavior ID. | 
 **attachmentDelete** | **Boolean**| If true, will delete the file stored in attachment | [optional] 
 **attachmentFile** | **File**| Certain behaviors may require a file, for instance, the \\\&quot;watermark\\\&quot; behavior requires a watermark image | [optional] 
 **behavior** | **String**| Behavior type. | [optional] 
 **description** | **String**| Description for this behavior. | [optional] 
 **name** | **String**| Name for this behavior. | [optional] 
 **path** | **String**| Folder behaviors path. | [optional] 
 **value** | **String**| The value of the folder behavior.  Can be a integer, array, or hash depending on the type of folder behavior. See The Behavior Types section for example values for each type of behavior. | [optional] 

### Return type

[**BehaviorEntity**](BehaviorEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## postBehaviors

> BehaviorEntity postBehaviors(behavior, path, opts)

Create Behavior

Create Behavior

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.BehaviorsApi();
let behavior = "behavior_example"; // String | Behavior type.
let path = "path_example"; // String | Folder behaviors path.
let opts = {
  'attachmentFile': "/path/to/file", // File | Certain behaviors may require a file, for instance, the \\\"watermark\\\" behavior requires a watermark image
  'description': "description_example", // String | Description for this behavior.
  'name': "name_example", // String | Name for this behavior.
  'value': "value_example" // String | The value of the folder behavior.  Can be a integer, array, or hash depending on the type of folder behavior. See The Behavior Types section for example values for each type of behavior.
};
apiInstance.postBehaviors(behavior, path, opts, (error, data, response) => {
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
 **behavior** | **String**| Behavior type. | 
 **path** | **String**| Folder behaviors path. | 
 **attachmentFile** | **File**| Certain behaviors may require a file, for instance, the \\\&quot;watermark\\\&quot; behavior requires a watermark image | [optional] 
 **description** | **String**| Description for this behavior. | [optional] 
 **name** | **String**| Name for this behavior. | [optional] 
 **value** | **String**| The value of the folder behavior.  Can be a integer, array, or hash depending on the type of folder behavior. See The Behavior Types section for example values for each type of behavior. | [optional] 

### Return type

[**BehaviorEntity**](BehaviorEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## postBehaviorsWebhookTest

> StatusEntity postBehaviorsWebhookTest(url, opts)

Test webhook.

Test webhook.

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.BehaviorsApi();
let url = "url_example"; // String | URL for testing the webhook.
let opts = {
  'action': "action_example", // String | action for test body
  'body': {key: null}, // Object | Additional body parameters.
  'encoding': "encoding_example", // String | HTTP encoding method.  Can be JSON, XML, or RAW (form data).
  'headers': {key: null}, // Object | Additional request headers.
  'method': "method_example" // String | HTTP method(GET or POST).
};
apiInstance.postBehaviorsWebhookTest(url, opts, (error, data, response) => {
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
 **url** | **String**| URL for testing the webhook. | 
 **action** | **String**| action for test body | [optional] 
 **body** | [**Object**](Object.md)| Additional body parameters. | [optional] 
 **encoding** | **String**| HTTP encoding method.  Can be JSON, XML, or RAW (form data). | [optional] 
 **headers** | [**Object**](Object.md)| Additional request headers. | [optional] 
 **method** | **String**| HTTP method(GET or POST). | [optional] 

### Return type

[**StatusEntity**](StatusEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

