# IbmContainersApi.SingleContainersApi

All URIs are relative to *https://containers-api.ng.bluemix.net/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**containersCreatePost**](SingleContainersApi.md#containersCreatePost) | **POST** /containers/create | Create and start a single container
[**containersIdStatusGet**](SingleContainersApi.md#containersIdStatusGet) | **GET** /containers/{id}/status | List the current state of a container.
[**containersJsonGet**](SingleContainersApi.md#containersJsonGet) | **GET** /containers/json | List single containers in a space.
[**containersNameOrIdDelete**](SingleContainersApi.md#containersNameOrIdDelete) | **DELETE** /containers/{name_or_id} | Remove a single container
[**containersNameOrIdJsonGet**](SingleContainersApi.md#containersNameOrIdJsonGet) | **GET** /containers/{name_or_id}/json | Inspect a single container
[**containersNameOrIdPausePost**](SingleContainersApi.md#containersNameOrIdPausePost) | **POST** /containers/{name_or_id}/pause | Pause a single container
[**containersNameOrIdRenamePost**](SingleContainersApi.md#containersNameOrIdRenamePost) | **POST** /containers/{name_or_id}/rename | Rename a single container
[**containersNameOrIdRestartPost**](SingleContainersApi.md#containersNameOrIdRestartPost) | **POST** /containers/{name_or_id}/restart | Restart a single container
[**containersNameOrIdStartPost**](SingleContainersApi.md#containersNameOrIdStartPost) | **POST** /containers/{name_or_id}/start | Start a single container
[**containersNameOrIdStopPost**](SingleContainersApi.md#containersNameOrIdStopPost) | **POST** /containers/{name_or_id}/stop | Stop a single container
[**containersNameOrIdUnpausePost**](SingleContainersApi.md#containersNameOrIdUnpausePost) | **POST** /containers/{name_or_id}/unpause | Unpause a single container



## containersCreatePost

> ContainerId containersCreatePost(xAuthToken, xAuthProjectId, createContainer, opts)

Create and start a single container

This endpoint creates and starts a single container in your space based on the Docker image that is specified in the Image field of the request json. A single container in IBM Containers is similar to a container that you create in your local Docker environment. Single containers are a good way to start with IBM Containers and to learn about how containers work in the IBM Cloud and the features that IBM Containers provides. They are also recommended when you want to run simple app tests or during the development process of an app.    In the Docker API there are two separate APIs to create and start a container. However in IBM Containers a container is created and started in a single API call. Therefore, this API merges parameters from the Docker API to create and start container.    To create a container with IBM Containers, you must at least define the image that the container is based on.  - Image: You must include the full path to the image in your private Bluemix registry in the format: &#x60;registry.ng.bluemix.net/&lt;namespace&gt;/&lt;image&gt;&#x60;.

### Example

```javascript
import IbmContainersApi from 'ibm_containers_api';

let apiInstance = new IbmContainersApi.SingleContainersApi();
let xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
let xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
let createContainer = new IbmContainersApi.CreateContainer(); // CreateContainer | Summary of input parameter to create a container in IBM Containers.
let opts = {
  'name': "name_example" // String | Choose a name for your container. The characters in the name can include uppercase letters, lowercase letters, numbers, periods (.), underscores (_), or hyphens (-), but the name must start with a letter.
};
apiInstance.containersCreatePost(xAuthToken, xAuthProjectId, createContainer, opts, (error, data, response) => {
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
 **createContainer** | [**CreateContainer**](CreateContainer.md)| Summary of input parameter to create a container in IBM Containers. | 
 **name** | **String**| Choose a name for your container. The characters in the name can include uppercase letters, lowercase letters, numbers, periods (.), underscores (_), or hyphens (-), but the name must start with a letter. | [optional] 

### Return type

[**ContainerId**](ContainerId.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## containersIdStatusGet

> GetContainerStatus containersIdStatusGet(xAuthToken, xAuthProjectId, id)

List the current state of a container.

This endpoint returns the current state of a container. This state can either be a transient state, such as BUILDING and NETWORKING, or a non-transient state, such as RUNNING, SHUTDOWN, CRASHED, or SUSPENDED.

### Example

```javascript
import IbmContainersApi from 'ibm_containers_api';

let apiInstance = new IbmContainersApi.SingleContainersApi();
let xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
let xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
let id = "id_example"; // String | The unique identifier that represents the container. Run `cf ic ps`, or call the `GET /containers/json` endpoint to retrieve the ID of the container.
apiInstance.containersIdStatusGet(xAuthToken, xAuthProjectId, id, (error, data, response) => {
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
 **id** | **String**| The unique identifier that represents the container. Run &#x60;cf ic ps&#x60;, or call the &#x60;GET /containers/json&#x60; endpoint to retrieve the ID of the container. | 

### Return type

[**GetContainerStatus**](GetContainerStatus.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## containersJsonGet

> [Container] containersJsonGet(xAuthToken, xAuthProjectId, opts)

List single containers in a space.

This endpoint returns a list of all single containers in a space that are currently in a running state (corresponding IBM Containers command: &#x60;cf ic ps&#x60;). To list all single containers independent of their current state, set the &#x60;all&#x60; query parameter to true.

### Example

```javascript
import IbmContainersApi from 'ibm_containers_api';

let apiInstance = new IbmContainersApi.SingleContainersApi();
let xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
let xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
let opts = {
  'all': "all_example", // String | By default, the `GET /containers/json` endpoint returns a list of all single containers in a space that are in a running state. To request a list of all containers independent of their current state, set the `all` query parameter to true. Allowed values are: `all=true`, `all=True`, and `all=1`. 
  'filters': "filters_example" // String | You can filter your containers by any environment variable key or value that is listed in the `Env` section of your CLI/ API response when you run the `cf ic inspect <container>` command, or call the `GET /containers/{id}/json` endpoint. Your search criteria does not need to be an exact match. It can also be a part of the key or value you are looking for. For example, to filter all containers with an environment variable that contains `id` in one of their environment variables, use `filter=id`.
};
apiInstance.containersJsonGet(xAuthToken, xAuthProjectId, opts, (error, data, response) => {
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
 **all** | **String**| By default, the &#x60;GET /containers/json&#x60; endpoint returns a list of all single containers in a space that are in a running state. To request a list of all containers independent of their current state, set the &#x60;all&#x60; query parameter to true. Allowed values are: &#x60;all&#x3D;true&#x60;, &#x60;all&#x3D;True&#x60;, and &#x60;all&#x3D;1&#x60;.  | [optional] 
 **filters** | **String**| You can filter your containers by any environment variable key or value that is listed in the &#x60;Env&#x60; section of your CLI/ API response when you run the &#x60;cf ic inspect &lt;container&gt;&#x60; command, or call the &#x60;GET /containers/{id}/json&#x60; endpoint. Your search criteria does not need to be an exact match. It can also be a part of the key or value you are looking for. For example, to filter all containers with an environment variable that contains &#x60;id&#x60; in one of their environment variables, use &#x60;filter&#x3D;id&#x60;. | [optional] 

### Return type

[**[Container]**](Container.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## containersNameOrIdDelete

> containersNameOrIdDelete(xAuthToken, xAuthProjectId, nameOrId, opts)

Remove a single container

Remove a single container that is identified by container ID or name from a space (corresponding IBM Containers command: &#x60;cf ic delete &lt;container&gt;&#x60;). The container must be stopped before it can be deleted, unless the &#x60;force&#x60; query parameter is set to true.

### Example

```javascript
import IbmContainersApi from 'ibm_containers_api';

let apiInstance = new IbmContainersApi.SingleContainersApi();
let xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
let xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
let nameOrId = "nameOrId_example"; // String | The unique identifier or name of the container that you want to delete. Run `cf ic ps -a` or call the `GET /containers/json?all=true` endpoint to review all containers in your space.
let opts = {
  'force': true // Boolean | Use the `force` query parameter if you want to delete the container independent of their current state. The container does not need to be stopped first. To force the deletion of a container, enter `force=true`, `force=True`, or `force=1`. If you want to delete containers that are in a non-running state only, do either not set this query parameter, or enter `force=false`, `force=False`, or `force=0`.
};
apiInstance.containersNameOrIdDelete(xAuthToken, xAuthProjectId, nameOrId, opts, (error, data, response) => {
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
 **nameOrId** | **String**| The unique identifier or name of the container that you want to delete. Run &#x60;cf ic ps -a&#x60; or call the &#x60;GET /containers/json?all&#x3D;true&#x60; endpoint to review all containers in your space. | 
 **force** | **Boolean**| Use the &#x60;force&#x60; query parameter if you want to delete the container independent of their current state. The container does not need to be stopped first. To force the deletion of a container, enter &#x60;force&#x3D;true&#x60;, &#x60;force&#x3D;True&#x60;, or &#x60;force&#x3D;1&#x60;. If you want to delete containers that are in a non-running state only, do either not set this query parameter, or enter &#x60;force&#x3D;false&#x60;, &#x60;force&#x3D;False&#x60;, or &#x60;force&#x3D;0&#x60;. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## containersNameOrIdJsonGet

> ContainerInfo containersNameOrIdJsonGet(xAuthToken, xAuthProjectId, nameOrId)

Inspect a single container

This endpoint retrieves detailed information about a single container (corresponding IBM Containers command: &#x60;cf ic inspect &lt;container&gt;&#x60;).

### Example

```javascript
import IbmContainersApi from 'ibm_containers_api';

let apiInstance = new IbmContainersApi.SingleContainersApi();
let xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
let xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
let nameOrId = "nameOrId_example"; // String | The name or ID of the container that you want to inspect. Run the `cf ic ps` command or call the `GET /containers/json` endpoint to retrieve a list of containers in your space.
apiInstance.containersNameOrIdJsonGet(xAuthToken, xAuthProjectId, nameOrId, (error, data, response) => {
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
 **nameOrId** | **String**| The name or ID of the container that you want to inspect. Run the &#x60;cf ic ps&#x60; command or call the &#x60;GET /containers/json&#x60; endpoint to retrieve a list of containers in your space. | 

### Return type

[**ContainerInfo**](ContainerInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## containersNameOrIdPausePost

> containersNameOrIdPausePost(xAuthToken, xAuthProjectId, nameOrId)

Pause a single container

Pause all processes in a running single container with a given container ID or name (corresponding IBM Containers command: &#x60;cf ic pause &lt;container&gt;&#x60;).

### Example

```javascript
import IbmContainersApi from 'ibm_containers_api';

let apiInstance = new IbmContainersApi.SingleContainersApi();
let xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
let xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
let nameOrId = "nameOrId_example"; // String | The unique identifier or name of the container that you want to pause. Run `cf ic ps` or call the `GET /containers/json` endpoint to review all containers in your space that are currently in a running state.
apiInstance.containersNameOrIdPausePost(xAuthToken, xAuthProjectId, nameOrId, (error, data, response) => {
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
 **nameOrId** | **String**| The unique identifier or name of the container that you want to pause. Run &#x60;cf ic ps&#x60; or call the &#x60;GET /containers/json&#x60; endpoint to review all containers in your space that are currently in a running state. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## containersNameOrIdRenamePost

> containersNameOrIdRenamePost(xAuthToken, xAuthProjectId, nameOrId, name)

Rename a single container

Change the current name of an existing single container that is identified by the container ID or name (corresponding IBM Containers command: &#x60;cf ic rename &lt;old_name&gt; &lt;new_name&gt;&#x60;). 

### Example

```javascript
import IbmContainersApi from 'ibm_containers_api';

let apiInstance = new IbmContainersApi.SingleContainersApi();
let xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
let xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
let nameOrId = "nameOrId_example"; // String | The unique identifier or name of the container that you want to rename. Run `cf ic ps -a` or call the `GET /containers/json?all=true` endpoint to review all containers in your space.
let name = "name_example"; // String | The new name for the container. The characters in the name can include uppercase letters, lowercase letters, numbers, periods (.), underscores (_), or hyphens (-), but the name must start with a letter.
apiInstance.containersNameOrIdRenamePost(xAuthToken, xAuthProjectId, nameOrId, name, (error, data, response) => {
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
 **nameOrId** | **String**| The unique identifier or name of the container that you want to rename. Run &#x60;cf ic ps -a&#x60; or call the &#x60;GET /containers/json?all&#x3D;true&#x60; endpoint to review all containers in your space. | 
 **name** | **String**| The new name for the container. The characters in the name can include uppercase letters, lowercase letters, numbers, periods (.), underscores (_), or hyphens (-), but the name must start with a letter. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## containersNameOrIdRestartPost

> containersNameOrIdRestartPost(xAuthToken, xAuthProjectId, nameOrId, opts)

Restart a single container

Restart a container with a given container ID or name (corresponding IBM Containers command: &#x60;cf ic restart &lt;container&gt;&#x60;).

### Example

```javascript
import IbmContainersApi from 'ibm_containers_api';

let apiInstance = new IbmContainersApi.SingleContainersApi();
let xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
let xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
let nameOrId = "nameOrId_example"; // String | The unique identifier or name of the container that you want to restart. Run `cf ic ps` or call the `GET /containers/json` endpoint to review all containers in your space.
let opts = {
  't': 56 // Number | The number of seconds to wait before the container is restarted. For example, if you want a container to restart after 10 seconds, enter `t=10`.
};
apiInstance.containersNameOrIdRestartPost(xAuthToken, xAuthProjectId, nameOrId, opts, (error, data, response) => {
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
 **nameOrId** | **String**| The unique identifier or name of the container that you want to restart. Run &#x60;cf ic ps&#x60; or call the &#x60;GET /containers/json&#x60; endpoint to review all containers in your space. | 
 **t** | **Number**| The number of seconds to wait before the container is restarted. For example, if you want a container to restart after 10 seconds, enter &#x60;t&#x3D;10&#x60;. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## containersNameOrIdStartPost

> containersNameOrIdStartPost(xAuthToken, xAuthProjectId, nameOrId)

Start a single container

Start a single container with a given container name or ID (corresponding IBM Containers command: &#x60;cf ic start &lt;container&gt;&#x60;).

### Example

```javascript
import IbmContainersApi from 'ibm_containers_api';

let apiInstance = new IbmContainersApi.SingleContainersApi();
let xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
let xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
let nameOrId = "nameOrId_example"; // String | The unique identifier or name of the container that you want to start. Run `cf ic ps -a` or call the `GET /containers/json?all=true` endpoint to review the containers in your space that are currently not in a running state.
apiInstance.containersNameOrIdStartPost(xAuthToken, xAuthProjectId, nameOrId, (error, data, response) => {
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
 **nameOrId** | **String**| The unique identifier or name of the container that you want to start. Run &#x60;cf ic ps -a&#x60; or call the &#x60;GET /containers/json?all&#x3D;true&#x60; endpoint to review the containers in your space that are currently not in a running state. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## containersNameOrIdStopPost

> containersNameOrIdStopPost(xAuthToken, xAuthProjectId, nameOrId, opts)

Stop a single container

Stop a single container with a given container name or ID (corresponding IBM Containers command: &#x60;cf ic stop &lt;container&gt;&#x60;).

### Example

```javascript
import IbmContainersApi from 'ibm_containers_api';

let apiInstance = new IbmContainersApi.SingleContainersApi();
let xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
let xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
let nameOrId = "nameOrId_example"; // String | The unique identifier or name of the container that you want to stop. Run `cf ic ps` or call the `GET /containers/json` endpoint to review the containers in your space that are currently in a running state.
let opts = {
  't': 56 // Number | The number of seconds to wait before the container is stopped. For example, if you want a container to stop after 10 seconds, enter `t=10`.
};
apiInstance.containersNameOrIdStopPost(xAuthToken, xAuthProjectId, nameOrId, opts, (error, data, response) => {
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
 **nameOrId** | **String**| The unique identifier or name of the container that you want to stop. Run &#x60;cf ic ps&#x60; or call the &#x60;GET /containers/json&#x60; endpoint to review the containers in your space that are currently in a running state. | 
 **t** | **Number**| The number of seconds to wait before the container is stopped. For example, if you want a container to stop after 10 seconds, enter &#x60;t&#x3D;10&#x60;. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## containersNameOrIdUnpausePost

> containersNameOrIdUnpausePost(xAuthToken, xAuthProjectId, nameOrId)

Unpause a single container

Unpause all processes that are currently stopped inside a single containers with a given container ID or name (corresponding IBM Containers command: &#x60;cf ic unpause &lt;container&gt;&#x60;).

### Example

```javascript
import IbmContainersApi from 'ibm_containers_api';

let apiInstance = new IbmContainersApi.SingleContainersApi();
let xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
let xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
let nameOrId = "nameOrId_example"; // String | The unique identifier or name of the container that you want to unpause. Run `cf ic ps -a` or call the `GET /containers/json?all=true` endpoint to review all containers in your space.
apiInstance.containersNameOrIdUnpausePost(xAuthToken, xAuthProjectId, nameOrId, (error, data, response) => {
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
 **nameOrId** | **String**| The unique identifier or name of the container that you want to unpause. Run &#x60;cf ic ps -a&#x60; or call the &#x60;GET /containers/json?all&#x3D;true&#x60; endpoint to review all containers in your space. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

