# IbmContainersApi.VolumesApi

All URIs are relative to *https://containers-api.ng.bluemix.net/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**volumesCreatePost**](VolumesApi.md#volumesCreatePost) | **POST** /volumes/create | Create a volume in a space
[**volumesJsonGet**](VolumesApi.md#volumesJsonGet) | **GET** /volumes/json | List all volumes for a space
[**volumesNameDelete**](VolumesApi.md#volumesNameDelete) | **DELETE** /volumes/{name} | Delete a volume
[**volumesNameJsonGet**](VolumesApi.md#volumesNameJsonGet) | **GET** /volumes/{name}/json | Retrieve detailed information about a volume. 
[**volumesNamePost**](VolumesApi.md#volumesNamePost) | **POST** /volumes/{name} | Share a volume with another space



## volumesCreatePost

> Volume volumesCreatePost(xAuthToken, xAuthProjectId, name, opts)

Create a volume in a space

This endpoints creates a new volume in your space (corresponding IBM Containers command: &#x60;cf ic volume create VOLNAME&#x60;). A volume is used to persist and access app data between container restarts. Volumes are hosted on file shares that define the available actual storage in Bluemix and the number of input and output transactions per second (IOPS).    After you have created a volume, you must mount it to a container by using the &#x60;--volume&#x60; option in the &#x60;cf ic run&#x60; (single containers) or &#x60;cf ic group create&#x60; (container groups) command. You can also define the volume as part of the HTTP body and send a request to the &#x60;POST /containers/create&#x60; (single containers) or &#x60;POST /containers/groups&#x60; (container groups) endpoints.    Note: If you mount multiple containers in a space to the same volume, they share the data in the volume and can access them anytime. When a container is deleted, the associated volume is not removed.

### Example

```javascript
import IbmContainersApi from 'ibm_containers_api';

let apiInstance = new IbmContainersApi.VolumesApi();
let xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
let xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
let name = "name_example"; // String | The name of the volume. The name must be unique for a space and can contain uppercase letters, lowercase letters, numbers, underscores (_), and hyphens (-).
let opts = {
  'fsName': "fsName_example" // String | The name of the file share that the volume is hosted on. File shares can have different storage sizes and IOPS based on the required workload. If this field is left blank, the volume is hosted on the default file share.
};
apiInstance.volumesCreatePost(xAuthToken, xAuthProjectId, name, opts, (error, data, response) => {
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
 **xAuthToken** | **String**| The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token. | 
 **xAuthProjectId** | **String**| The unique ID of your organization space where you want to create or work with your containers. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID. | 
 **name** | **String**| The name of the volume. The name must be unique for a space and can contain uppercase letters, lowercase letters, numbers, underscores (_), and hyphens (-). | 
 **fsName** | **String**| The name of the file share that the volume is hosted on. File shares can have different storage sizes and IOPS based on the required workload. If this field is left blank, the volume is hosted on the default file share. | [optional] 

### Return type

[**Volume**](Volume.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## volumesJsonGet

> [Volume] volumesJsonGet(xAuthToken, xAuthProjectId)

List all volumes for a space

This endpoint returns a list of all volumes that are available in the given space (corresponding IBM Containers command: &#x60;cf ic volume list&#x60;).

### Example

```javascript
import IbmContainersApi from 'ibm_containers_api';

let apiInstance = new IbmContainersApi.VolumesApi();
let xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
let xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
apiInstance.volumesJsonGet(xAuthToken, xAuthProjectId, (error, data, response) => {
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
 **xAuthToken** | **String**| The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token. | 
 **xAuthProjectId** | **String**| The unique ID of your organization space where you want to create or work with your containers. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID. | 

### Return type

[**[Volume]**](Volume.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## volumesNameDelete

> volumesNameDelete(xAuthToken, xAuthProjectId, name)

Delete a volume

Delete a volume with a given name from a space (corresponding IBM Containers command: &#x60;cf ic volume rm VOLNAME&#x60;). To delete a volume, all mounted containers must be unmounted first. After the volume is deleted, the data that are stored in the volume are lost. 

### Example

```javascript
import IbmContainersApi from 'ibm_containers_api';

let apiInstance = new IbmContainersApi.VolumesApi();
let xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
let xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
let name = "name_example"; // String | The name of the volume that you want to delete. Run `cf ic volume list` or call the `GET /volumes/json` endpoint to retrieve a list of all volumes that are available in your space.
apiInstance.volumesNameDelete(xAuthToken, xAuthProjectId, name, (error, data, response) => {
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
 **xAuthToken** | **String**| The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token. | 
 **xAuthProjectId** | **String**| The unique ID of your organization space where you want to create or work with your containers. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID. | 
 **name** | **String**| The name of the volume that you want to delete. Run &#x60;cf ic volume list&#x60; or call the &#x60;GET /volumes/json&#x60; endpoint to retrieve a list of all volumes that are available in your space. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## volumesNameJsonGet

> Volume volumesNameJsonGet(xAuthToken, xAuthProjectId, name)

Retrieve detailed information about a volume. 

Retrieve a detailed list of information about a volume that is identified by the volume name (corresponding IBM Containers command: &#x60;cf ic volume inspect VOLNAME&#x60;).

### Example

```javascript
import IbmContainersApi from 'ibm_containers_api';

let apiInstance = new IbmContainersApi.VolumesApi();
let xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
let xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
let name = "name_example"; // String | The name of the volume, for which you want to retrieve detailed information. Run `cf ic volume list` or call the `GET /volumes/json` endpoint to retrieve a list of all volumes that are available in your space.
apiInstance.volumesNameJsonGet(xAuthToken, xAuthProjectId, name, (error, data, response) => {
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
 **xAuthToken** | **String**| The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token. | 
 **xAuthProjectId** | **String**| The unique ID of your organization space where you want to create or work with your containers. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID. | 
 **name** | **String**| The name of the volume, for which you want to retrieve detailed information. Run &#x60;cf ic volume list&#x60; or call the &#x60;GET /volumes/json&#x60; endpoint to retrieve a list of all volumes that are available in your space. | 

### Return type

[**Volume**](Volume.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## volumesNamePost

> Volume volumesNamePost(xAuthToken, xAuthProjectId, name, updateVolume)

Share a volume with another space

This endpoint provisions an existing volume that was created in one space to another space within the same organization. Single containers and container groups in each space can read and write to the shared volume. The volume remains owned by the original space it was created in, including management and billing. For example, the volume can be deleted from the original space only.

### Example

```javascript
import IbmContainersApi from 'ibm_containers_api';

let apiInstance = new IbmContainersApi.VolumesApi();
let xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
let xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
let name = "name_example"; // String | The name of the volume that you want to share with another space in your organization.
let updateVolume = new IbmContainersApi.UpdateVolume(); // UpdateVolume | Input parameter that are required to provision an existing volume to a new space and to unprovision it from a space.
apiInstance.volumesNamePost(xAuthToken, xAuthProjectId, name, updateVolume, (error, data, response) => {
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
 **xAuthToken** | **String**| The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token. | 
 **xAuthProjectId** | **String**| The unique ID of your organization space where you want to create or work with your containers. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID. | 
 **name** | **String**| The name of the volume that you want to share with another space in your organization. | 
 **updateVolume** | [**UpdateVolume**](UpdateVolume.md)| Input parameter that are required to provision an existing volume to a new space and to unprovision it from a space. | 

### Return type

[**Volume**](Volume.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

