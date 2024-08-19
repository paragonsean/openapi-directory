# IbmContainersApi.FileSharesApi

All URIs are relative to *https://containers-api.ng.bluemix.net/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**volumesFsCreatePost**](FileSharesApi.md#volumesFsCreatePost) | **POST** /volumes/fs/create | Create a file share in a space
[**volumesFsFlavorsJsonGet**](FileSharesApi.md#volumesFsFlavorsJsonGet) | **GET** /volumes/fs/flavors/json | List available file share sizes
[**volumesFsJsonGet**](FileSharesApi.md#volumesFsJsonGet) | **GET** /volumes/fs/json | List available file shares in a space
[**volumesFsNameDelete**](FileSharesApi.md#volumesFsNameDelete) | **DELETE** /volumes/fs/{name} | Delete a file share
[**volumesFsNameJsonGet**](FileSharesApi.md#volumesFsNameJsonGet) | **GET** /volumes/fs/{name}/json | Inspect a file share



## volumesFsCreatePost

> volumesFsCreatePost(xAuthToken, xAuthProjectId, fileshareParam)

Create a file share in a space

This endpoint creates a new file share in a space (corresponding IBM Containers command: &#x60;cf ic volume fs-create FSNAME FSSIZE FSIOPS&#x60;).    A file share is a persistent NFS-based (Network File System) storage system that hosts Docker volumes in a Bluemix space and allows a user to store and access container and app-related files. To store files in a file share, you must create a container volume and save the data into this volume.   As soon as you create your first volume in a space with the &#x60;cf ic volume create VOLNAME&#x60; command or the &#x60;POST /volumes/create&#x60; API endpoint, a default file share with 20 GB at 4 IOPS (Input Output operations Per Second) is created at no cost.   The organization manager can create file shares with specific storage size and IOPS to meet the storage needs of the space. File shares can be provisioned in sizes from 20 GB to 12 TB and at IOPS per GB of 0.25, 2 or 4. Run &#x60;cf ic volume fs-flavor-list&#x60; or call the &#x60;GET /volumes/fs/flavors/json&#x60; API endpoint to retrieve a list of available file share sizes. The file share size in relation to the number of IOPS impacts the speed that data can be read and written from and to the container volume.

### Example

```javascript
import IbmContainersApi from 'ibm_containers_api';

let apiInstance = new IbmContainersApi.FileSharesApi();
let xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
let xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
let fileshareParam = new IbmContainersApi.FileshareParam(); // FileshareParam | The input parameter to create a new file share in a space.
apiInstance.volumesFsCreatePost(xAuthToken, xAuthProjectId, fileshareParam, (error, data, response) => {
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
 **fileshareParam** | [**FileshareParam**](FileshareParam.md)| The input parameter to create a new file share in a space. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## volumesFsFlavorsJsonGet

> [Number] volumesFsFlavorsJsonGet(xAuthToken, xAuthProjectId)

List available file share sizes

This endpoint returns a list of available file shares in gigabyte (corresponding IBM Containers command: &#x60;cf ic volume fs-flavor-list&#x60;).

### Example

```javascript
import IbmContainersApi from 'ibm_containers_api';

let apiInstance = new IbmContainersApi.FileSharesApi();
let xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
let xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
apiInstance.volumesFsFlavorsJsonGet(xAuthToken, xAuthProjectId, (error, data, response) => {
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

**[Number]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## volumesFsJsonGet

> [Fileshare] volumesFsJsonGet(xAuthToken, xAuthProjectId)

List available file shares in a space

This endpoint returns a list of all file shares that are availble in a space (corresponding IBM Containers command: &#x60;cf ic volume fs-list&#x60;).

### Example

```javascript
import IbmContainersApi from 'ibm_containers_api';

let apiInstance = new IbmContainersApi.FileSharesApi();
let xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
let xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
apiInstance.volumesFsJsonGet(xAuthToken, xAuthProjectId, (error, data, response) => {
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

[**[Fileshare]**](Fileshare.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## volumesFsNameDelete

> volumesFsNameDelete(xAuthToken, xAuthProjectId, name)

Delete a file share

This endpoint deletes a file share from a space (corresponding IBM Containers command: &#x60;cf ic volume fs-rm FSNAME&#x60;).   Before you can delete a file share, all mounted volumes must be deleted first. To delete a volume, run &#x60;cf ic volume rm VOLNAME&#x60; or call the &#x60;DELETE /volumes/{name}&#x60; API endpoint.    **Note:** To delete a file share you must have been granted organization developer rights.

### Example

```javascript
import IbmContainersApi from 'ibm_containers_api';

let apiInstance = new IbmContainersApi.FileSharesApi();
let xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
let xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
let name = "name_example"; // String | The name of the file share that you want to delete. Run `cf ic volume fs-list` or call the `GET /volumes/fs/json` API endpoint to retrieve a list of available file shares in your space.
apiInstance.volumesFsNameDelete(xAuthToken, xAuthProjectId, name, (error, data, response) => {
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
 **name** | **String**| The name of the file share that you want to delete. Run &#x60;cf ic volume fs-list&#x60; or call the &#x60;GET /volumes/fs/json&#x60; API endpoint to retrieve a list of available file shares in your space. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## volumesFsNameJsonGet

> [GetFileshareDetails] volumesFsNameJsonGet(xAuthToken, xAuthProjectId, name)

Inspect a file share

This endpoint returns detailed information about a file share (corresponding IBM Containers command: &#x60;cf ic volume fs-inspect FSNAME&#x60;).

### Example

```javascript
import IbmContainersApi from 'ibm_containers_api';

let apiInstance = new IbmContainersApi.FileSharesApi();
let xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
let xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
let name = "name_example"; // String | The name of the file share that you want to inspect. Run `cf ic volume fs-list` or call the `GET /volumes/fs/json` endpoint to retrieve a list of available file shares in your space.
apiInstance.volumesFsNameJsonGet(xAuthToken, xAuthProjectId, name, (error, data, response) => {
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
 **name** | **String**| The name of the file share that you want to inspect. Run &#x60;cf ic volume fs-list&#x60; or call the &#x60;GET /volumes/fs/json&#x60; endpoint to retrieve a list of available file shares in your space. | 

### Return type

[**[GetFileshareDetails]**](GetFileshareDetails.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

