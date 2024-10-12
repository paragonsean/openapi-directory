# CustomVisionTrainingClient.ProjectApiApi

All URIs are relative to *https://southcentralus.api.cognitive.microsoft.com/customvision/v3.2/training*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createProject**](ProjectApiApi.md#createProject) | **POST** /projects | Create a project.
[**deleteIteration**](ProjectApiApi.md#deleteIteration) | **DELETE** /projects/{projectId}/iterations/{iterationId} | Delete a specific iteration of a project.
[**deleteProject**](ProjectApiApi.md#deleteProject) | **DELETE** /projects/{projectId} | Delete a specific project.
[**exportIteration**](ProjectApiApi.md#exportIteration) | **POST** /projects/{projectId}/iterations/{iterationId}/export | Export a trained iteration.
[**exportProject**](ProjectApiApi.md#exportProject) | **GET** /projects/{projectId}/export | Exports a project.
[**getExports**](ProjectApiApi.md#getExports) | **GET** /projects/{projectId}/iterations/{iterationId}/export | Get the list of exports for a specific iteration.
[**getImagePerformanceCount**](ProjectApiApi.md#getImagePerformanceCount) | **GET** /projects/{projectId}/iterations/{iterationId}/performance/images/count | Gets the number of images tagged with the provided {tagIds} that have prediction results from  training for the provided iteration {iterationId}.
[**getImagePerformances**](ProjectApiApi.md#getImagePerformances) | **GET** /projects/{projectId}/iterations/{iterationId}/performance/images | Get image with its prediction for a given project iteration.
[**getIteration**](ProjectApiApi.md#getIteration) | **GET** /projects/{projectId}/iterations/{iterationId} | Get a specific iteration.
[**getIterationPerformance**](ProjectApiApi.md#getIterationPerformance) | **GET** /projects/{projectId}/iterations/{iterationId}/performance | Get detailed performance information about an iteration.
[**getIterations**](ProjectApiApi.md#getIterations) | **GET** /projects/{projectId}/iterations | Get iterations for the project.
[**getProject**](ProjectApiApi.md#getProject) | **GET** /projects/{projectId} | Get a specific project.
[**getProjects**](ProjectApiApi.md#getProjects) | **GET** /projects | Get your projects.
[**importProject**](ProjectApiApi.md#importProject) | **POST** /projects/import | Imports a project.
[**publishIteration**](ProjectApiApi.md#publishIteration) | **POST** /projects/{projectId}/iterations/{iterationId}/publish | Publish a specific iteration.
[**trainProject**](ProjectApiApi.md#trainProject) | **POST** /projects/{projectId}/train | Queues project for training.
[**unpublishIteration**](ProjectApiApi.md#unpublishIteration) | **DELETE** /projects/{projectId}/iterations/{iterationId}/publish | Unpublish a specific iteration.
[**updateIteration**](ProjectApiApi.md#updateIteration) | **PATCH** /projects/{projectId}/iterations/{iterationId} | Update a specific iteration.
[**updateProject**](ProjectApiApi.md#updateProject) | **PATCH** /projects/{projectId} | Update a specific project.



## createProject

> Project createProject(name, opts)

Create a project.

### Example

```javascript
import CustomVisionTrainingClient from 'custom_vision_training_client';
let defaultClient = CustomVisionTrainingClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new CustomVisionTrainingClient.ProjectApiApi();
let name = "My New Project"; // String | Name of the project.
let opts = {
  'description': "A test project", // String | The description of the project.
  'domainId': "ee85a74c-405e-4adc-bb47-ffa8ca0c9f31", // String | The id of the domain to use for this project. Defaults to General.
  'classificationType': "classificationType_example", // String | The type of classifier to create for this project.
  'targetExportPlatforms': ["null"] // [String] | List of platforms the trained model is intending exporting to.
};
apiInstance.createProject(name, opts, (error, data, response) => {
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
 **name** | **String**| Name of the project. | 
 **description** | **String**| The description of the project. | [optional] 
 **domainId** | **String**| The id of the domain to use for this project. Defaults to General. | [optional] 
 **classificationType** | **String**| The type of classifier to create for this project. | [optional] 
 **targetExportPlatforms** | [**[String]**](String.md)| List of platforms the trained model is intending exporting to. | [optional] 

### Return type

[**Project**](Project.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/xml


## deleteIteration

> deleteIteration(projectId, iterationId)

Delete a specific iteration of a project.

### Example

```javascript
import CustomVisionTrainingClient from 'custom_vision_training_client';
let defaultClient = CustomVisionTrainingClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new CustomVisionTrainingClient.ProjectApiApi();
let projectId = "64b822c5-8082-4b36-a426-27225f4aa18c"; // String | The project id.
let iterationId = "e31a14ab-5d78-4f7b-a267-3a1e4fd8a758"; // String | The iteration id.
apiInstance.deleteIteration(projectId, iterationId, (error, data, response) => {
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
 **projectId** | **String**| The project id. | 
 **iterationId** | **String**| The iteration id. | 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## deleteProject

> deleteProject(projectId)

Delete a specific project.

### Example

```javascript
import CustomVisionTrainingClient from 'custom_vision_training_client';
let defaultClient = CustomVisionTrainingClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new CustomVisionTrainingClient.ProjectApiApi();
let projectId = "bc3f7dad-5544-468c-8573-3ef04d55463e"; // String | The project id.
apiInstance.deleteProject(projectId, (error, data, response) => {
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
 **projectId** | **String**| The project id. | 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## exportIteration

> Export exportIteration(projectId, iterationId, platform, opts)

Export a trained iteration.

### Example

```javascript
import CustomVisionTrainingClient from 'custom_vision_training_client';
let defaultClient = CustomVisionTrainingClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new CustomVisionTrainingClient.ProjectApiApi();
let projectId = "64b822c5-8082-4b36-a426-27225f4aa18c"; // String | The project id.
let iterationId = "e31a14ab-5d78-4f7b-a267-3a1e4fd8a758"; // String | The iteration id.
let platform = "TensorFlow"; // String | The target platform.
let opts = {
  'flavor': "flavor_example" // String | The flavor of the target platform.
};
apiInstance.exportIteration(projectId, iterationId, platform, opts, (error, data, response) => {
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
 **projectId** | **String**| The project id. | 
 **iterationId** | **String**| The iteration id. | 
 **platform** | **String**| The target platform. | 
 **flavor** | **String**| The flavor of the target platform. | [optional] 

### Return type

[**Export**](Export.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/xml


## exportProject

> ProjectExport exportProject(projectId)

Exports a project.

### Example

```javascript
import CustomVisionTrainingClient from 'custom_vision_training_client';
let defaultClient = CustomVisionTrainingClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new CustomVisionTrainingClient.ProjectApiApi();
let projectId = "bc3f7dad-5544-468c-8573-3ef04d55463e"; // String | The project id of the project to export.
apiInstance.exportProject(projectId, (error, data, response) => {
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
 **projectId** | **String**| The project id of the project to export. | 

### Return type

[**ProjectExport**](ProjectExport.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/xml


## getExports

> [Export] getExports(projectId, iterationId)

Get the list of exports for a specific iteration.

### Example

```javascript
import CustomVisionTrainingClient from 'custom_vision_training_client';
let defaultClient = CustomVisionTrainingClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new CustomVisionTrainingClient.ProjectApiApi();
let projectId = "64b822c5-8082-4b36-a426-27225f4aa18c"; // String | The project id.
let iterationId = "e31a14ab-5d78-4f7b-a267-3a1e4fd8a758"; // String | The iteration id.
apiInstance.getExports(projectId, iterationId, (error, data, response) => {
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
 **projectId** | **String**| The project id. | 
 **iterationId** | **String**| The iteration id. | 

### Return type

[**[Export]**](Export.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/xml


## getImagePerformanceCount

> Number getImagePerformanceCount(projectId, iterationId, opts)

Gets the number of images tagged with the provided {tagIds} that have prediction results from  training for the provided iteration {iterationId}.

The filtering is on an and/or relationship. For example, if the provided tag ids are for the \&quot;Dog\&quot; and  \&quot;Cat\&quot; tags, then only images tagged with Dog and/or Cat will be returned

### Example

```javascript
import CustomVisionTrainingClient from 'custom_vision_training_client';
let defaultClient = CustomVisionTrainingClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new CustomVisionTrainingClient.ProjectApiApi();
let projectId = "bc3f7dad-5544-468c-8573-3ef04d55463e"; // String | The project id.
let iterationId = "cf0f83fb-ebaa-4b25-8e34-613a6a0b8a12"; // String | The iteration id. Defaults to workspace.
let opts = {
  'tagIds': ["null"] // [String] | A list of tags ids to filter the images to count. Defaults to all tags when null.
};
apiInstance.getImagePerformanceCount(projectId, iterationId, opts, (error, data, response) => {
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
 **projectId** | **String**| The project id. | 
 **iterationId** | **String**| The iteration id. Defaults to workspace. | 
 **tagIds** | [**[String]**](String.md)| A list of tags ids to filter the images to count. Defaults to all tags when null. | [optional] 

### Return type

**Number**

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/xml


## getImagePerformances

> [ImagePerformance] getImagePerformances(projectId, iterationId, opts)

Get image with its prediction for a given project iteration.

This API supports batching and range selection. By default it will only return first 50 images matching images.  Use the {take} and {skip} parameters to control how many images to return in a given batch.  The filtering is on an and/or relationship. For example, if the provided tag ids are for the \&quot;Dog\&quot; and  \&quot;Cat\&quot; tags, then only images tagged with Dog and/or Cat will be returned

### Example

```javascript
import CustomVisionTrainingClient from 'custom_vision_training_client';
let defaultClient = CustomVisionTrainingClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new CustomVisionTrainingClient.ProjectApiApi();
let projectId = "bc3f7dad-5544-468c-8573-3ef04d55463e"; // String | The project id.
let iterationId = "b7b9d99c-a2c6-4658-9900-a98d2ff5bc66"; // String | The iteration id. Defaults to workspace.
let opts = {
  'tagIds': ["null"], // [String] | A list of tags ids to filter the images. Defaults to all tagged images when null. Limited to 20.
  'orderBy': "Newest", // String | The ordering. Defaults to newest.
  'take': 50, // Number | Maximum number of images to return. Defaults to 50, limited to 256.
  'skip': 0 // Number | Number of images to skip before beginning the image batch. Defaults to 0.
};
apiInstance.getImagePerformances(projectId, iterationId, opts, (error, data, response) => {
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
 **projectId** | **String**| The project id. | 
 **iterationId** | **String**| The iteration id. Defaults to workspace. | 
 **tagIds** | [**[String]**](String.md)| A list of tags ids to filter the images. Defaults to all tagged images when null. Limited to 20. | [optional] 
 **orderBy** | **String**| The ordering. Defaults to newest. | [optional] 
 **take** | **Number**| Maximum number of images to return. Defaults to 50, limited to 256. | [optional] [default to 50]
 **skip** | **Number**| Number of images to skip before beginning the image batch. Defaults to 0. | [optional] [default to 0]

### Return type

[**[ImagePerformance]**](ImagePerformance.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/xml


## getIteration

> Iteration getIteration(projectId, iterationId)

Get a specific iteration.

### Example

```javascript
import CustomVisionTrainingClient from 'custom_vision_training_client';
let defaultClient = CustomVisionTrainingClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new CustomVisionTrainingClient.ProjectApiApi();
let projectId = "64b822c5-8082-4b36-a426-27225f4aa18c"; // String | The id of the project the iteration belongs to.
let iterationId = "e31a14ab-5d78-4f7b-a267-3a1e4fd8a758"; // String | The id of the iteration to get.
apiInstance.getIteration(projectId, iterationId, (error, data, response) => {
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
 **projectId** | **String**| The id of the project the iteration belongs to. | 
 **iterationId** | **String**| The id of the iteration to get. | 

### Return type

[**Iteration**](Iteration.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/xml


## getIterationPerformance

> IterationPerformance getIterationPerformance(projectId, iterationId, opts)

Get detailed performance information about an iteration.

### Example

```javascript
import CustomVisionTrainingClient from 'custom_vision_training_client';
let defaultClient = CustomVisionTrainingClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new CustomVisionTrainingClient.ProjectApiApi();
let projectId = "bc3f7dad-5544-468c-8573-3ef04d55463e"; // String | The id of the project the iteration belongs to.
let iterationId = "fe1e83c4-6f50-4899-9544-6bb08cf0e15a"; // String | The id of the iteration to get.
let opts = {
  'threshold': 0.9, // Number | The threshold used to determine true predictions.
  'overlapThreshold': 3.4 // Number | If applicable, the bounding box overlap threshold used to determine true predictions.
};
apiInstance.getIterationPerformance(projectId, iterationId, opts, (error, data, response) => {
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
 **projectId** | **String**| The id of the project the iteration belongs to. | 
 **iterationId** | **String**| The id of the iteration to get. | 
 **threshold** | **Number**| The threshold used to determine true predictions. | [optional] 
 **overlapThreshold** | **Number**| If applicable, the bounding box overlap threshold used to determine true predictions. | [optional] 

### Return type

[**IterationPerformance**](IterationPerformance.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/xml


## getIterations

> [Iteration] getIterations(projectId)

Get iterations for the project.

### Example

```javascript
import CustomVisionTrainingClient from 'custom_vision_training_client';
let defaultClient = CustomVisionTrainingClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new CustomVisionTrainingClient.ProjectApiApi();
let projectId = "64b822c5-8082-4b36-a426-27225f4aa18c"; // String | The project id.
apiInstance.getIterations(projectId, (error, data, response) => {
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
 **projectId** | **String**| The project id. | 

### Return type

[**[Iteration]**](Iteration.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/xml


## getProject

> Project getProject(projectId)

Get a specific project.

### Example

```javascript
import CustomVisionTrainingClient from 'custom_vision_training_client';
let defaultClient = CustomVisionTrainingClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new CustomVisionTrainingClient.ProjectApiApi();
let projectId = "bc3f7dad-5544-468c-8573-3ef04d55463e"; // String | The id of the project to get.
apiInstance.getProject(projectId, (error, data, response) => {
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
 **projectId** | **String**| The id of the project to get. | 

### Return type

[**Project**](Project.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/xml


## getProjects

> [Project] getProjects()

Get your projects.

### Example

```javascript
import CustomVisionTrainingClient from 'custom_vision_training_client';
let defaultClient = CustomVisionTrainingClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new CustomVisionTrainingClient.ProjectApiApi();
apiInstance.getProjects((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[Project]**](Project.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/xml


## importProject

> Project importProject(token)

Imports a project.

### Example

```javascript
import CustomVisionTrainingClient from 'custom_vision_training_client';
let defaultClient = CustomVisionTrainingClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new CustomVisionTrainingClient.ProjectApiApi();
let token = "token"; // String | Token generated from the export project call.
apiInstance.importProject(token, (error, data, response) => {
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
 **token** | **String**| Token generated from the export project call. | 

### Return type

[**Project**](Project.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/xml


## publishIteration

> Boolean publishIteration(projectId, iterationId, publishName, predictionId)

Publish a specific iteration.

### Example

```javascript
import CustomVisionTrainingClient from 'custom_vision_training_client';
let defaultClient = CustomVisionTrainingClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new CustomVisionTrainingClient.ProjectApiApi();
let projectId = "64b822c5-8082-4b36-a426-27225f4aa18c"; // String | The project id.
let iterationId = "e31a14ab-5d78-4f7b-a267-3a1e4fd8a758"; // String | The iteration id.
let publishName = "Model1"; // String | The name to give the published iteration.
let predictionId = "/subscriptions/{subscription}/resourceGroups/{resource group name}/providers/Microsoft.CognitiveServices/accounts/{resource name}"; // String | The id of the prediction resource to publish to.
apiInstance.publishIteration(projectId, iterationId, publishName, predictionId, (error, data, response) => {
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
 **projectId** | **String**| The project id. | 
 **iterationId** | **String**| The iteration id. | 
 **publishName** | **String**| The name to give the published iteration. | 
 **predictionId** | **String**| The id of the prediction resource to publish to. | 

### Return type

**Boolean**

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/xml


## trainProject

> Iteration trainProject(projectId, opts)

Queues project for training.

### Example

```javascript
import CustomVisionTrainingClient from 'custom_vision_training_client';
let defaultClient = CustomVisionTrainingClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new CustomVisionTrainingClient.ProjectApiApi();
let projectId = "64b822c5-8082-4b36-a426-27225f4aa18c"; // String | The project id.
let opts = {
  'trainingType': "trainingType_example", // String | The type of training to use to train the project (default: Regular).
  'reservedBudgetInHours': 0, // Number | The number of hours reserved as budget for training (if applicable).
  'forceTrain': false, // Boolean | Whether to force train even if dataset and configuration does not change (default: false).
  'notificationEmailAddress': "notificationEmailAddress_example", // String | The email address to send notification to when training finishes (default: null).
  'trainingParameters': new CustomVisionTrainingClient.TrainingParameters() // TrainingParameters | Additional training parameters passed in to control how the project is trained.
};
apiInstance.trainProject(projectId, opts, (error, data, response) => {
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
 **projectId** | **String**| The project id. | 
 **trainingType** | **String**| The type of training to use to train the project (default: Regular). | [optional] 
 **reservedBudgetInHours** | **Number**| The number of hours reserved as budget for training (if applicable). | [optional] [default to 0]
 **forceTrain** | **Boolean**| Whether to force train even if dataset and configuration does not change (default: false). | [optional] [default to false]
 **notificationEmailAddress** | **String**| The email address to send notification to when training finishes (default: null). | [optional] 
 **trainingParameters** | [**TrainingParameters**](TrainingParameters.md)| Additional training parameters passed in to control how the project is trained. | [optional] 

### Return type

[**Iteration**](Iteration.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
- **Accept**: application/json, application/xml, text/xml


## unpublishIteration

> unpublishIteration(projectId, iterationId)

Unpublish a specific iteration.

### Example

```javascript
import CustomVisionTrainingClient from 'custom_vision_training_client';
let defaultClient = CustomVisionTrainingClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new CustomVisionTrainingClient.ProjectApiApi();
let projectId = "64b822c5-8082-4b36-a426-27225f4aa18c"; // String | The project id.
let iterationId = "e31a14ab-5d78-4f7b-a267-3a1e4fd8a758"; // String | The iteration id.
apiInstance.unpublishIteration(projectId, iterationId, (error, data, response) => {
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
 **projectId** | **String**| The project id. | 
 **iterationId** | **String**| The iteration id. | 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## updateIteration

> Iteration updateIteration(projectId, iterationId, iteration)

Update a specific iteration.

### Example

```javascript
import CustomVisionTrainingClient from 'custom_vision_training_client';
let defaultClient = CustomVisionTrainingClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new CustomVisionTrainingClient.ProjectApiApi();
let projectId = "64b822c5-8082-4b36-a426-27225f4aa18c"; // String | Project id.
let iterationId = "e31a14ab-5d78-4f7b-a267-3a1e4fd8a758"; // String | Iteration id.
let iteration = new CustomVisionTrainingClient.Iteration(); // Iteration | The updated iteration model.
apiInstance.updateIteration(projectId, iterationId, iteration, (error, data, response) => {
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
 **projectId** | **String**| Project id. | 
 **iterationId** | **String**| Iteration id. | 
 **iteration** | [**Iteration**](Iteration.md)| The updated iteration model. | 

### Return type

[**Iteration**](Iteration.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
- **Accept**: application/json, application/xml, text/xml


## updateProject

> Project updateProject(projectId, project)

Update a specific project.

### Example

```javascript
import CustomVisionTrainingClient from 'custom_vision_training_client';
let defaultClient = CustomVisionTrainingClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new CustomVisionTrainingClient.ProjectApiApi();
let projectId = "bc3f7dad-5544-468c-8573-3ef04d55463e"; // String | The id of the project to update.
let project = new CustomVisionTrainingClient.Project(); // Project | The updated project model.
apiInstance.updateProject(projectId, project, (error, data, response) => {
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
 **projectId** | **String**| The id of the project to update. | 
 **project** | [**Project**](Project.md)| The updated project model. | 

### Return type

[**Project**](Project.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
- **Accept**: application/json, application/xml, text/xml

