# TrainingApi.ProjectApiApi

All URIs are relative to *https://southcentralus.api.cognitive.microsoft.com/customvision/v2.0/Training*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createProject**](ProjectApiApi.md#createProject) | **POST** /projects | Create a project
[**deleteIteration**](ProjectApiApi.md#deleteIteration) | **DELETE** /projects/{projectId}/iterations/{iterationId} | Delete a specific iteration of a project
[**deleteProject**](ProjectApiApi.md#deleteProject) | **DELETE** /projects/{projectId} | Delete a specific project
[**exportIteration**](ProjectApiApi.md#exportIteration) | **POST** /projects/{projectId}/iterations/{iterationId}/export | Export a trained iteration
[**getExports**](ProjectApiApi.md#getExports) | **GET** /projects/{projectId}/iterations/{iterationId}/export | Get the list of exports for a specific iteration
[**getImagePerformanceCount**](ProjectApiApi.md#getImagePerformanceCount) | **GET** /projects/{projectId}/iterations/{iterationId}/performance/images/count | Gets the number of images tagged with the provided {tagIds} that have prediction results from  training for the provided iteration {iterationId}
[**getImagePerformances**](ProjectApiApi.md#getImagePerformances) | **GET** /projects/{projectId}/iterations/{iterationId}/performance/images | Get image with its prediction for a given project iteration
[**getIteration**](ProjectApiApi.md#getIteration) | **GET** /projects/{projectId}/iterations/{iterationId} | Get a specific iteration
[**getIterationPerformance**](ProjectApiApi.md#getIterationPerformance) | **GET** /projects/{projectId}/iterations/{iterationId}/performance | Get detailed performance information about an iteration
[**getIterations**](ProjectApiApi.md#getIterations) | **GET** /projects/{projectId}/iterations | Get iterations for the project
[**getProject**](ProjectApiApi.md#getProject) | **GET** /projects/{projectId} | Get a specific project
[**getProjects**](ProjectApiApi.md#getProjects) | **GET** /projects | Get your projects
[**trainProject**](ProjectApiApi.md#trainProject) | **POST** /projects/{projectId}/train | Queues project for training
[**updateIteration**](ProjectApiApi.md#updateIteration) | **PATCH** /projects/{projectId}/iterations/{iterationId} | Update a specific iteration
[**updateProject**](ProjectApiApi.md#updateProject) | **PATCH** /projects/{projectId} | Update a specific project



## createProject

> Project createProject(name, trainingKey, opts)

Create a project

### Example

```javascript
import TrainingApi from 'training_api';

let apiInstance = new TrainingApi.ProjectApiApi();
let name = "My New Project"; // String | Name of the project
let trainingKey = "{API Key}"; // String | 
let opts = {
  'description': "A test project", // String | The description of the project
  'domainId': "ee85a74c-405e-4adc-bb47-ffa8ca0c9f31" // String | The id of the domain to use for this project. Defaults to General
};
apiInstance.createProject(name, trainingKey, opts, (error, data, response) => {
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
 **name** | **String**| Name of the project | 
 **trainingKey** | **String**|  | 
 **description** | **String**| The description of the project | [optional] 
 **domainId** | **String**| The id of the domain to use for this project. Defaults to General | [optional] 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## deleteIteration

> deleteIteration(projectId, iterationId, trainingKey)

Delete a specific iteration of a project

### Example

```javascript
import TrainingApi from 'training_api';

let apiInstance = new TrainingApi.ProjectApiApi();
let projectId = "64b822c5-8082-4b36-a426-27225f4aa18c"; // String | The project id
let iterationId = "e31a14ab-5d78-4f7b-a267-3a1e4fd8a758"; // String | The iteration id
let trainingKey = "{API Key}"; // String | 
apiInstance.deleteIteration(projectId, iterationId, trainingKey, (error, data, response) => {
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
 **projectId** | **String**| The project id | 
 **iterationId** | **String**| The iteration id | 
 **trainingKey** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteProject

> deleteProject(projectId, trainingKey)

Delete a specific project

### Example

```javascript
import TrainingApi from 'training_api';

let apiInstance = new TrainingApi.ProjectApiApi();
let projectId = "bc3f7dad-5544-468c-8573-3ef04d55463e"; // String | The project id
let trainingKey = "{API Key}"; // String | 
apiInstance.deleteProject(projectId, trainingKey, (error, data, response) => {
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
 **projectId** | **String**| The project id | 
 **trainingKey** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## exportIteration

> Export exportIteration(projectId, iterationId, platform, trainingKey, opts)

Export a trained iteration

### Example

```javascript
import TrainingApi from 'training_api';

let apiInstance = new TrainingApi.ProjectApiApi();
let projectId = "64b822c5-8082-4b36-a426-27225f4aa18c"; // String | The project id
let iterationId = "e31a14ab-5d78-4f7b-a267-3a1e4fd8a758"; // String | The iteration id
let platform = "tensorflow"; // String | The target platform (coreml or tensorflow)
let trainingKey = "{API Key}"; // String | 
let opts = {
  'flavor': "flavor_example" // String | The flavor of the target platform (Windows, Linux, ARM, or GPU)
};
apiInstance.exportIteration(projectId, iterationId, platform, trainingKey, opts, (error, data, response) => {
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
 **projectId** | **String**| The project id | 
 **iterationId** | **String**| The iteration id | 
 **platform** | **String**| The target platform (coreml or tensorflow) | 
 **trainingKey** | **String**|  | 
 **flavor** | **String**| The flavor of the target platform (Windows, Linux, ARM, or GPU) | [optional] 

### Return type

[**Export**](Export.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## getExports

> [Export] getExports(projectId, iterationId, trainingKey)

Get the list of exports for a specific iteration

### Example

```javascript
import TrainingApi from 'training_api';

let apiInstance = new TrainingApi.ProjectApiApi();
let projectId = "64b822c5-8082-4b36-a426-27225f4aa18c"; // String | The project id
let iterationId = "e31a14ab-5d78-4f7b-a267-3a1e4fd8a758"; // String | The iteration id
let trainingKey = "{API Key}"; // String | 
apiInstance.getExports(projectId, iterationId, trainingKey, (error, data, response) => {
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
 **projectId** | **String**| The project id | 
 **iterationId** | **String**| The iteration id | 
 **trainingKey** | **String**|  | 

### Return type

[**[Export]**](Export.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## getImagePerformanceCount

> Number getImagePerformanceCount(projectId, iterationId, trainingKey, opts)

Gets the number of images tagged with the provided {tagIds} that have prediction results from  training for the provided iteration {iterationId}

The filtering is on an and/or relationship. For example, if the provided tag ids are for the \&quot;Dog\&quot; and  \&quot;Cat\&quot; tags, then only images tagged with Dog and/or Cat will be returned

### Example

```javascript
import TrainingApi from 'training_api';

let apiInstance = new TrainingApi.ProjectApiApi();
let projectId = "bc3f7dad-5544-468c-8573-3ef04d55463e"; // String | The project id
let iterationId = "cf0f83fb-ebaa-4b25-8e34-613a6a0b8a12"; // String | The iteration id. Defaults to workspace
let trainingKey = "{API Key}"; // String | 
let opts = {
  'tagIds': ["null"] // [String] | A list of tags ids to filter the images to count. Defaults to all tags when null.
};
apiInstance.getImagePerformanceCount(projectId, iterationId, trainingKey, opts, (error, data, response) => {
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
 **projectId** | **String**| The project id | 
 **iterationId** | **String**| The iteration id. Defaults to workspace | 
 **trainingKey** | **String**|  | 
 **tagIds** | [**[String]**](String.md)| A list of tags ids to filter the images to count. Defaults to all tags when null. | [optional] 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## getImagePerformances

> [ImagePerformance] getImagePerformances(projectId, iterationId, trainingKey, opts)

Get image with its prediction for a given project iteration

This API supports batching and range selection. By default it will only return first 50 images matching images.  Use the {take} and {skip} parameters to control how many images to return in a given batch.  The filtering is on an and/or relationship. For example, if the provided tag ids are for the \&quot;Dog\&quot; and  \&quot;Cat\&quot; tags, then only images tagged with Dog and/or Cat will be returned

### Example

```javascript
import TrainingApi from 'training_api';

let apiInstance = new TrainingApi.ProjectApiApi();
let projectId = "bc3f7dad-5544-468c-8573-3ef04d55463e"; // String | The project id
let iterationId = "b7b9d99c-a2c6-4658-9900-a98d2ff5bc66"; // String | The iteration id. Defaults to workspace
let trainingKey = "{API Key}"; // String | 
let opts = {
  'tagIds': ["null"], // [String] | A list of tags ids to filter the images. Defaults to all tagged images when null. Limited to 20
  'orderBy': "Newest", // String | The ordering. Defaults to newest
  'take': 50, // Number | Maximum number of images to return. Defaults to 50, limited to 256
  'skip': 0 // Number | Number of images to skip before beginning the image batch. Defaults to 0
};
apiInstance.getImagePerformances(projectId, iterationId, trainingKey, opts, (error, data, response) => {
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
 **projectId** | **String**| The project id | 
 **iterationId** | **String**| The iteration id. Defaults to workspace | 
 **trainingKey** | **String**|  | 
 **tagIds** | [**[String]**](String.md)| A list of tags ids to filter the images. Defaults to all tagged images when null. Limited to 20 | [optional] 
 **orderBy** | **String**| The ordering. Defaults to newest | [optional] 
 **take** | **Number**| Maximum number of images to return. Defaults to 50, limited to 256 | [optional] [default to 50]
 **skip** | **Number**| Number of images to skip before beginning the image batch. Defaults to 0 | [optional] [default to 0]

### Return type

[**[ImagePerformance]**](ImagePerformance.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## getIteration

> Iteration getIteration(projectId, iterationId, trainingKey)

Get a specific iteration

### Example

```javascript
import TrainingApi from 'training_api';

let apiInstance = new TrainingApi.ProjectApiApi();
let projectId = "64b822c5-8082-4b36-a426-27225f4aa18c"; // String | The id of the project the iteration belongs to
let iterationId = "e31a14ab-5d78-4f7b-a267-3a1e4fd8a758"; // String | The id of the iteration to get
let trainingKey = "{API Key}"; // String | 
apiInstance.getIteration(projectId, iterationId, trainingKey, (error, data, response) => {
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
 **projectId** | **String**| The id of the project the iteration belongs to | 
 **iterationId** | **String**| The id of the iteration to get | 
 **trainingKey** | **String**|  | 

### Return type

[**Iteration**](Iteration.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## getIterationPerformance

> IterationPerformance getIterationPerformance(projectId, iterationId, trainingKey, opts)

Get detailed performance information about an iteration

### Example

```javascript
import TrainingApi from 'training_api';

let apiInstance = new TrainingApi.ProjectApiApi();
let projectId = "bc3f7dad-5544-468c-8573-3ef04d55463e"; // String | The id of the project the iteration belongs to
let iterationId = "fe1e83c4-6f50-4899-9544-6bb08cf0e15a"; // String | The id of the iteration to get
let trainingKey = "{API Key}"; // String | 
let opts = {
  'threshold': 0.9, // Number | The threshold used to determine true predictions
  'overlapThreshold': 3.4 // Number | If applicable, the bounding box overlap threshold used to determine true predictions
};
apiInstance.getIterationPerformance(projectId, iterationId, trainingKey, opts, (error, data, response) => {
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
 **projectId** | **String**| The id of the project the iteration belongs to | 
 **iterationId** | **String**| The id of the iteration to get | 
 **trainingKey** | **String**|  | 
 **threshold** | **Number**| The threshold used to determine true predictions | [optional] 
 **overlapThreshold** | **Number**| If applicable, the bounding box overlap threshold used to determine true predictions | [optional] 

### Return type

[**IterationPerformance**](IterationPerformance.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## getIterations

> [Iteration] getIterations(projectId, trainingKey)

Get iterations for the project

### Example

```javascript
import TrainingApi from 'training_api';

let apiInstance = new TrainingApi.ProjectApiApi();
let projectId = "64b822c5-8082-4b36-a426-27225f4aa18c"; // String | The project id
let trainingKey = "{API Key}"; // String | 
apiInstance.getIterations(projectId, trainingKey, (error, data, response) => {
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
 **projectId** | **String**| The project id | 
 **trainingKey** | **String**|  | 

### Return type

[**[Iteration]**](Iteration.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## getProject

> Project getProject(projectId, trainingKey)

Get a specific project

### Example

```javascript
import TrainingApi from 'training_api';

let apiInstance = new TrainingApi.ProjectApiApi();
let projectId = "bc3f7dad-5544-468c-8573-3ef04d55463e"; // String | The id of the project to get
let trainingKey = "{API Key}"; // String | 
apiInstance.getProject(projectId, trainingKey, (error, data, response) => {
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
 **projectId** | **String**| The id of the project to get | 
 **trainingKey** | **String**|  | 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## getProjects

> [Project] getProjects(trainingKey)

Get your projects

### Example

```javascript
import TrainingApi from 'training_api';

let apiInstance = new TrainingApi.ProjectApiApi();
let trainingKey = "{API Key}"; // String | 
apiInstance.getProjects(trainingKey, (error, data, response) => {
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
 **trainingKey** | **String**|  | 

### Return type

[**[Project]**](Project.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## trainProject

> Iteration trainProject(projectId, trainingKey)

Queues project for training

### Example

```javascript
import TrainingApi from 'training_api';

let apiInstance = new TrainingApi.ProjectApiApi();
let projectId = "64b822c5-8082-4b36-a426-27225f4aa18c"; // String | The project id
let trainingKey = "{API Key}"; // String | 
apiInstance.trainProject(projectId, trainingKey, (error, data, response) => {
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
 **projectId** | **String**| The project id | 
 **trainingKey** | **String**|  | 

### Return type

[**Iteration**](Iteration.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## updateIteration

> Iteration updateIteration(projectId, iterationId, trainingKey, iteration)

Update a specific iteration

### Example

```javascript
import TrainingApi from 'training_api';

let apiInstance = new TrainingApi.ProjectApiApi();
let projectId = "64b822c5-8082-4b36-a426-27225f4aa18c"; // String | Project id
let iterationId = "e31a14ab-5d78-4f7b-a267-3a1e4fd8a758"; // String | Iteration id
let trainingKey = "{API Key}"; // String | 
let iteration = new TrainingApi.Iteration(); // Iteration | The updated iteration model
apiInstance.updateIteration(projectId, iterationId, trainingKey, iteration, (error, data, response) => {
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
 **projectId** | **String**| Project id | 
 **iterationId** | **String**| Iteration id | 
 **trainingKey** | **String**|  | 
 **iteration** | [**Iteration**](Iteration.md)| The updated iteration model | 

### Return type

[**Iteration**](Iteration.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## updateProject

> Project updateProject(projectId, trainingKey, project)

Update a specific project

### Example

```javascript
import TrainingApi from 'training_api';

let apiInstance = new TrainingApi.ProjectApiApi();
let projectId = "bc3f7dad-5544-468c-8573-3ef04d55463e"; // String | The id of the project to update
let trainingKey = "{API Key}"; // String | 
let project = new TrainingApi.Project(); // Project | The updated project model
apiInstance.updateProject(projectId, trainingKey, project, (error, data, response) => {
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
 **projectId** | **String**| The id of the project to update | 
 **trainingKey** | **String**|  | 
 **project** | [**Project**](Project.md)| The updated project model | 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml

