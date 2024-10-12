# HetznerCloudApi.PlacementGroupsApi

All URIs are relative to *https://api.hetzner.cloud/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**placementGroupsGet**](PlacementGroupsApi.md#placementGroupsGet) | **GET** /placement_groups | Get all PlacementGroups
[**placementGroupsIdDelete**](PlacementGroupsApi.md#placementGroupsIdDelete) | **DELETE** /placement_groups/{id} | Delete a PlacementGroup
[**placementGroupsIdGet**](PlacementGroupsApi.md#placementGroupsIdGet) | **GET** /placement_groups/{id} | Get a PlacementGroup
[**placementGroupsIdPut**](PlacementGroupsApi.md#placementGroupsIdPut) | **PUT** /placement_groups/{id} | Update a PlacementGroup
[**placementGroupsPost**](PlacementGroupsApi.md#placementGroupsPost) | **POST** /placement_groups | Create a PlacementGroup



## placementGroupsGet

> PlacementGroupsResponse placementGroupsGet(opts)

Get all PlacementGroups

Returns all PlacementGroup objects.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.PlacementGroupsApi();
let opts = {
  'sort': "sort_example", // String | Can be used multiple times.
  'name': "name_example", // String | Can be used to filter resources by their name. The response will only contain the resources matching the specified name
  'labelSelector': "labelSelector_example", // String | Can be used to filter resources by labels. The response will only contain resources matching the label selector.
  'type': "type_example" // String | Can be used multiple times. The response will only contain PlacementGroups matching the type.
};
apiInstance.placementGroupsGet(opts, (error, data, response) => {
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
 **sort** | **String**| Can be used multiple times. | [optional] 
 **name** | **String**| Can be used to filter resources by their name. The response will only contain the resources matching the specified name | [optional] 
 **labelSelector** | **String**| Can be used to filter resources by labels. The response will only contain resources matching the label selector. | [optional] 
 **type** | **String**| Can be used multiple times. The response will only contain PlacementGroups matching the type. | [optional] 

### Return type

[**PlacementGroupsResponse**](PlacementGroupsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## placementGroupsIdDelete

> placementGroupsIdDelete(id)

Delete a PlacementGroup

Deletes a PlacementGroup.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.PlacementGroupsApi();
let id = 56; // Number | ID of the resource
apiInstance.placementGroupsIdDelete(id, (error, data, response) => {
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
 **id** | **Number**| ID of the resource | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## placementGroupsIdGet

> PlacementGroupResponse placementGroupsIdGet(id)

Get a PlacementGroup

Gets a specific PlacementGroup object.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.PlacementGroupsApi();
let id = 56; // Number | ID of the resource
apiInstance.placementGroupsIdGet(id, (error, data, response) => {
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
 **id** | **Number**| ID of the resource | 

### Return type

[**PlacementGroupResponse**](PlacementGroupResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## placementGroupsIdPut

> PlacementGroupResponse placementGroupsIdPut(id, opts)

Update a PlacementGroup

Updates the PlacementGroup properties.  Note that when updating labels, the PlacementGroup’s current set of labels will be replaced with the labels provided in the request body. So, for example, if you want to add a new label, you have to provide all existing labels plus the new label in the request body.  Note: if the PlacementGroup object changes during the request, the response will be a “conflict” error. 

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.PlacementGroupsApi();
let id = 56; // Number | ID of the resource
let opts = {
  'updatePlacementGroupRequest': new HetznerCloudApi.UpdatePlacementGroupRequest() // UpdatePlacementGroupRequest | 
};
apiInstance.placementGroupsIdPut(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID of the resource | 
 **updatePlacementGroupRequest** | [**UpdatePlacementGroupRequest**](UpdatePlacementGroupRequest.md)|  | [optional] 

### Return type

[**PlacementGroupResponse**](PlacementGroupResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## placementGroupsPost

> CreatePlacementGroupResponse placementGroupsPost(opts)

Create a PlacementGroup

Creates a new PlacementGroup. 

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.PlacementGroupsApi();
let opts = {
  'createPlacementGroupRequest': {"name":"my Placement Group","type":"spread"} // CreatePlacementGroupRequest | 
};
apiInstance.placementGroupsPost(opts, (error, data, response) => {
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
 **createPlacementGroupRequest** | [**CreatePlacementGroupRequest**](CreatePlacementGroupRequest.md)|  | [optional] 

### Return type

[**CreatePlacementGroupResponse**](CreatePlacementGroupResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

