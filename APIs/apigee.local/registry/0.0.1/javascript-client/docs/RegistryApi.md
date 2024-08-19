# RegistryApi.RegistryApi

All URIs are relative to *http://apigee.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**registryCreateApi**](RegistryApi.md#registryCreateApi) | **POST** /v1/projects/{project}/locations/{location}/apis | 
[**registryCreateApiDeployment**](RegistryApi.md#registryCreateApiDeployment) | **POST** /v1/projects/{project}/locations/{location}/apis/{api}/deployments | 
[**registryCreateApiSpec**](RegistryApi.md#registryCreateApiSpec) | **POST** /v1/projects/{project}/locations/{location}/apis/{api}/versions/{version}/specs | 
[**registryCreateApiVersion**](RegistryApi.md#registryCreateApiVersion) | **POST** /v1/projects/{project}/locations/{location}/apis/{api}/versions | 
[**registryCreateArtifact**](RegistryApi.md#registryCreateArtifact) | **POST** /v1/projects/{project}/locations/{location}/artifacts | 
[**registryDeleteApi**](RegistryApi.md#registryDeleteApi) | **DELETE** /v1/projects/{project}/locations/{location}/apis/{api} | 
[**registryDeleteApiDeployment**](RegistryApi.md#registryDeleteApiDeployment) | **DELETE** /v1/projects/{project}/locations/{location}/apis/{api}/deployments/{deployment} | 
[**registryDeleteApiDeploymentRevision**](RegistryApi.md#registryDeleteApiDeploymentRevision) | **DELETE** /v1/projects/{project}/locations/{location}/apis/{api}/deployments/{deployment}:deleteRevision | 
[**registryDeleteApiSpec**](RegistryApi.md#registryDeleteApiSpec) | **DELETE** /v1/projects/{project}/locations/{location}/apis/{api}/versions/{version}/specs/{spec} | 
[**registryDeleteApiSpecRevision**](RegistryApi.md#registryDeleteApiSpecRevision) | **DELETE** /v1/projects/{project}/locations/{location}/apis/{api}/versions/{version}/specs/{spec}:deleteRevision | 
[**registryDeleteApiVersion**](RegistryApi.md#registryDeleteApiVersion) | **DELETE** /v1/projects/{project}/locations/{location}/apis/{api}/versions/{version} | 
[**registryDeleteArtifact**](RegistryApi.md#registryDeleteArtifact) | **DELETE** /v1/projects/{project}/locations/{location}/artifacts/{artifact} | 
[**registryGetApi**](RegistryApi.md#registryGetApi) | **GET** /v1/projects/{project}/locations/{location}/apis/{api} | 
[**registryGetApiDeployment**](RegistryApi.md#registryGetApiDeployment) | **GET** /v1/projects/{project}/locations/{location}/apis/{api}/deployments/{deployment} | 
[**registryGetApiSpec**](RegistryApi.md#registryGetApiSpec) | **GET** /v1/projects/{project}/locations/{location}/apis/{api}/versions/{version}/specs/{spec} | 
[**registryGetApiSpecContents**](RegistryApi.md#registryGetApiSpecContents) | **GET** /v1/projects/{project}/locations/{location}/apis/{api}/versions/{version}/specs/{spec}:getContents | 
[**registryGetApiVersion**](RegistryApi.md#registryGetApiVersion) | **GET** /v1/projects/{project}/locations/{location}/apis/{api}/versions/{version} | 
[**registryGetArtifact**](RegistryApi.md#registryGetArtifact) | **GET** /v1/projects/{project}/locations/{location}/artifacts/{artifact} | 
[**registryGetArtifactContents**](RegistryApi.md#registryGetArtifactContents) | **GET** /v1/projects/{project}/locations/{location}/artifacts/{artifact}:getContents | 
[**registryListApiDeploymentRevisions**](RegistryApi.md#registryListApiDeploymentRevisions) | **GET** /v1/projects/{project}/locations/{location}/apis/{api}/deployments/{deployment}:listRevisions | 
[**registryListApiDeployments**](RegistryApi.md#registryListApiDeployments) | **GET** /v1/projects/{project}/locations/{location}/apis/{api}/deployments | 
[**registryListApiSpecRevisions**](RegistryApi.md#registryListApiSpecRevisions) | **GET** /v1/projects/{project}/locations/{location}/apis/{api}/versions/{version}/specs/{spec}:listRevisions | 
[**registryListApiSpecs**](RegistryApi.md#registryListApiSpecs) | **GET** /v1/projects/{project}/locations/{location}/apis/{api}/versions/{version}/specs | 
[**registryListApiVersions**](RegistryApi.md#registryListApiVersions) | **GET** /v1/projects/{project}/locations/{location}/apis/{api}/versions | 
[**registryListApis**](RegistryApi.md#registryListApis) | **GET** /v1/projects/{project}/locations/{location}/apis | 
[**registryListArtifacts**](RegistryApi.md#registryListArtifacts) | **GET** /v1/projects/{project}/locations/{location}/artifacts | 
[**registryReplaceArtifact**](RegistryApi.md#registryReplaceArtifact) | **PUT** /v1/projects/{project}/locations/{location}/artifacts/{artifact} | 
[**registryRollbackApiDeployment**](RegistryApi.md#registryRollbackApiDeployment) | **POST** /v1/projects/{project}/locations/{location}/apis/{api}/deployments/{deployment}:rollback | 
[**registryRollbackApiSpec**](RegistryApi.md#registryRollbackApiSpec) | **POST** /v1/projects/{project}/locations/{location}/apis/{api}/versions/{version}/specs/{spec}:rollback | 
[**registryTagApiDeploymentRevision**](RegistryApi.md#registryTagApiDeploymentRevision) | **POST** /v1/projects/{project}/locations/{location}/apis/{api}/deployments/{deployment}:tagRevision | 
[**registryTagApiSpecRevision**](RegistryApi.md#registryTagApiSpecRevision) | **POST** /v1/projects/{project}/locations/{location}/apis/{api}/versions/{version}/specs/{spec}:tagRevision | 
[**registryUpdateApi**](RegistryApi.md#registryUpdateApi) | **PATCH** /v1/projects/{project}/locations/{location}/apis/{api} | 
[**registryUpdateApiDeployment**](RegistryApi.md#registryUpdateApiDeployment) | **PATCH** /v1/projects/{project}/locations/{location}/apis/{api}/deployments/{deployment} | 
[**registryUpdateApiSpec**](RegistryApi.md#registryUpdateApiSpec) | **PATCH** /v1/projects/{project}/locations/{location}/apis/{api}/versions/{version}/specs/{spec} | 
[**registryUpdateApiVersion**](RegistryApi.md#registryUpdateApiVersion) | **PATCH** /v1/projects/{project}/locations/{location}/apis/{api}/versions/{version} | 



## registryCreateApi

> Api registryCreateApi(project, location, api, opts)



CreateApi creates a specified API.

### Example

```javascript
import RegistryApi from 'registry_api';

let apiInstance = new RegistryApi.RegistryApi();
let project = "project_example"; // String | The project id.
let location = "location_example"; // String | The location id.
let api = new RegistryApi.Api(); // Api | 
let opts = {
  'apiId': "apiId_example" // String | Required. The ID to use for the api, which will become the final component of the api's resource name. This value should be 4-63 characters, and valid characters are /[a-z][0-9]-/. Following AIP-162, IDs must not have the form of a UUID.
};
apiInstance.registryCreateApi(project, location, api, opts, (error, data, response) => {
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
 **project** | **String**| The project id. | 
 **location** | **String**| The location id. | 
 **api** | [**Api**](Api.md)|  | 
 **apiId** | **String**| Required. The ID to use for the api, which will become the final component of the api&#39;s resource name. This value should be 4-63 characters, and valid characters are /[a-z][0-9]-/. Following AIP-162, IDs must not have the form of a UUID. | [optional] 

### Return type

[**Api**](Api.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## registryCreateApiDeployment

> ApiDeployment registryCreateApiDeployment(project, location, api, apiDeployment, opts)



CreateApiDeployment creates a specified deployment.

### Example

```javascript
import RegistryApi from 'registry_api';

let apiInstance = new RegistryApi.RegistryApi();
let project = "project_example"; // String | The project id.
let location = "location_example"; // String | The location id.
let api = "api_example"; // String | The api id.
let apiDeployment = new RegistryApi.ApiDeployment(); // ApiDeployment | 
let opts = {
  'apiDeploymentId': "apiDeploymentId_example" // String | Required. The ID to use for the deployment, which will become the final component of the deployment's resource name. This value should be 4-63 characters, and valid characters are /[a-z][0-9]-/. Following AIP-162, IDs must not have the form of a UUID.
};
apiInstance.registryCreateApiDeployment(project, location, api, apiDeployment, opts, (error, data, response) => {
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
 **project** | **String**| The project id. | 
 **location** | **String**| The location id. | 
 **api** | **String**| The api id. | 
 **apiDeployment** | [**ApiDeployment**](ApiDeployment.md)|  | 
 **apiDeploymentId** | **String**| Required. The ID to use for the deployment, which will become the final component of the deployment&#39;s resource name. This value should be 4-63 characters, and valid characters are /[a-z][0-9]-/. Following AIP-162, IDs must not have the form of a UUID. | [optional] 

### Return type

[**ApiDeployment**](ApiDeployment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## registryCreateApiSpec

> ApiSpec registryCreateApiSpec(project, location, api, version, apiSpec, opts)



CreateApiSpec creates a specified spec.

### Example

```javascript
import RegistryApi from 'registry_api';

let apiInstance = new RegistryApi.RegistryApi();
let project = "project_example"; // String | The project id.
let location = "location_example"; // String | The location id.
let api = "api_example"; // String | The api id.
let version = "version_example"; // String | The version id.
let apiSpec = new RegistryApi.ApiSpec(); // ApiSpec | 
let opts = {
  'apiSpecId': "apiSpecId_example" // String | Required. The ID to use for the spec, which will become the final component of the spec's resource name. This value should be 4-63 characters, and valid characters are /[a-z][0-9]-/. Following AIP-162, IDs must not have the form of a UUID.
};
apiInstance.registryCreateApiSpec(project, location, api, version, apiSpec, opts, (error, data, response) => {
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
 **project** | **String**| The project id. | 
 **location** | **String**| The location id. | 
 **api** | **String**| The api id. | 
 **version** | **String**| The version id. | 
 **apiSpec** | [**ApiSpec**](ApiSpec.md)|  | 
 **apiSpecId** | **String**| Required. The ID to use for the spec, which will become the final component of the spec&#39;s resource name. This value should be 4-63 characters, and valid characters are /[a-z][0-9]-/. Following AIP-162, IDs must not have the form of a UUID. | [optional] 

### Return type

[**ApiSpec**](ApiSpec.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## registryCreateApiVersion

> ApiVersion registryCreateApiVersion(project, location, api, apiVersion, opts)



CreateApiVersion creates a specified version.

### Example

```javascript
import RegistryApi from 'registry_api';

let apiInstance = new RegistryApi.RegistryApi();
let project = "project_example"; // String | The project id.
let location = "location_example"; // String | The location id.
let api = "api_example"; // String | The api id.
let apiVersion = new RegistryApi.ApiVersion(); // ApiVersion | 
let opts = {
  'apiVersionId': "apiVersionId_example" // String | Required. The ID to use for the version, which will become the final component of the version's resource name. This value should be 4-63 characters, and valid characters are /[a-z][0-9]-/. Following AIP-162, IDs must not have the form of a UUID.
};
apiInstance.registryCreateApiVersion(project, location, api, apiVersion, opts, (error, data, response) => {
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
 **project** | **String**| The project id. | 
 **location** | **String**| The location id. | 
 **api** | **String**| The api id. | 
 **apiVersion** | [**ApiVersion**](ApiVersion.md)|  | 
 **apiVersionId** | **String**| Required. The ID to use for the version, which will become the final component of the version&#39;s resource name. This value should be 4-63 characters, and valid characters are /[a-z][0-9]-/. Following AIP-162, IDs must not have the form of a UUID. | [optional] 

### Return type

[**ApiVersion**](ApiVersion.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## registryCreateArtifact

> Artifact registryCreateArtifact(project, location, artifact, opts)



CreateArtifact creates a specified artifact.

### Example

```javascript
import RegistryApi from 'registry_api';

let apiInstance = new RegistryApi.RegistryApi();
let project = "project_example"; // String | The project id.
let location = "location_example"; // String | The location id.
let artifact = new RegistryApi.Artifact(); // Artifact | 
let opts = {
  'artifactId': "artifactId_example" // String | Required. The ID to use for the artifact, which will become the final component of the artifact's resource name. This value should be 4-63 characters, and valid characters are /[a-z][0-9]-/. Following AIP-162, IDs must not have the form of a UUID.
};
apiInstance.registryCreateArtifact(project, location, artifact, opts, (error, data, response) => {
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
 **project** | **String**| The project id. | 
 **location** | **String**| The location id. | 
 **artifact** | [**Artifact**](Artifact.md)|  | 
 **artifactId** | **String**| Required. The ID to use for the artifact, which will become the final component of the artifact&#39;s resource name. This value should be 4-63 characters, and valid characters are /[a-z][0-9]-/. Following AIP-162, IDs must not have the form of a UUID. | [optional] 

### Return type

[**Artifact**](Artifact.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## registryDeleteApi

> registryDeleteApi(project, location, api, opts)



DeleteApi removes a specified API and all of the resources that it  owns.

### Example

```javascript
import RegistryApi from 'registry_api';

let apiInstance = new RegistryApi.RegistryApi();
let project = "project_example"; // String | The project id.
let location = "location_example"; // String | The location id.
let api = "api_example"; // String | The api id.
let opts = {
  'force': true // Boolean | If set to true, any child resources will also be deleted. (Otherwise, the request will only work if there are no child resources.)
};
apiInstance.registryDeleteApi(project, location, api, opts, (error, data, response) => {
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
 **project** | **String**| The project id. | 
 **location** | **String**| The location id. | 
 **api** | **String**| The api id. | 
 **force** | **Boolean**| If set to true, any child resources will also be deleted. (Otherwise, the request will only work if there are no child resources.) | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## registryDeleteApiDeployment

> registryDeleteApiDeployment(project, location, api, deployment, opts)



DeleteApiDeployment removes a specified deployment, all revisions, and all  child resources (e.g. artifacts).

### Example

```javascript
import RegistryApi from 'registry_api';

let apiInstance = new RegistryApi.RegistryApi();
let project = "project_example"; // String | The project id.
let location = "location_example"; // String | The location id.
let api = "api_example"; // String | The api id.
let deployment = "deployment_example"; // String | The deployment id.
let opts = {
  'force': true // Boolean | If set to true, any child resources will also be deleted. (Otherwise, the request will only work if there are no child resources.)
};
apiInstance.registryDeleteApiDeployment(project, location, api, deployment, opts, (error, data, response) => {
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
 **project** | **String**| The project id. | 
 **location** | **String**| The location id. | 
 **api** | **String**| The api id. | 
 **deployment** | **String**| The deployment id. | 
 **force** | **Boolean**| If set to true, any child resources will also be deleted. (Otherwise, the request will only work if there are no child resources.) | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## registryDeleteApiDeploymentRevision

> ApiDeployment registryDeleteApiDeploymentRevision(project, location, api, deployment)



DeleteApiDeploymentRevision deletes a revision of a deployment.

### Example

```javascript
import RegistryApi from 'registry_api';

let apiInstance = new RegistryApi.RegistryApi();
let project = "project_example"; // String | The project id.
let location = "location_example"; // String | The location id.
let api = "api_example"; // String | The api id.
let deployment = "deployment_example"; // String | The deployment id.
apiInstance.registryDeleteApiDeploymentRevision(project, location, api, deployment, (error, data, response) => {
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
 **project** | **String**| The project id. | 
 **location** | **String**| The location id. | 
 **api** | **String**| The api id. | 
 **deployment** | **String**| The deployment id. | 

### Return type

[**ApiDeployment**](ApiDeployment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## registryDeleteApiSpec

> registryDeleteApiSpec(project, location, api, version, spec, opts)



DeleteApiSpec removes a specified spec, all revisions, and all child  resources (e.g. artifacts).

### Example

```javascript
import RegistryApi from 'registry_api';

let apiInstance = new RegistryApi.RegistryApi();
let project = "project_example"; // String | The project id.
let location = "location_example"; // String | The location id.
let api = "api_example"; // String | The api id.
let version = "version_example"; // String | The version id.
let spec = "spec_example"; // String | The spec id.
let opts = {
  'force': true // Boolean | If set to true, any child resources will also be deleted. (Otherwise, the request will only work if there are no child resources.)
};
apiInstance.registryDeleteApiSpec(project, location, api, version, spec, opts, (error, data, response) => {
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
 **project** | **String**| The project id. | 
 **location** | **String**| The location id. | 
 **api** | **String**| The api id. | 
 **version** | **String**| The version id. | 
 **spec** | **String**| The spec id. | 
 **force** | **Boolean**| If set to true, any child resources will also be deleted. (Otherwise, the request will only work if there are no child resources.) | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## registryDeleteApiSpecRevision

> ApiSpec registryDeleteApiSpecRevision(project, location, api, version, spec)



DeleteApiSpecRevision deletes a revision of a spec.

### Example

```javascript
import RegistryApi from 'registry_api';

let apiInstance = new RegistryApi.RegistryApi();
let project = "project_example"; // String | The project id.
let location = "location_example"; // String | The location id.
let api = "api_example"; // String | The api id.
let version = "version_example"; // String | The version id.
let spec = "spec_example"; // String | The spec id.
apiInstance.registryDeleteApiSpecRevision(project, location, api, version, spec, (error, data, response) => {
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
 **project** | **String**| The project id. | 
 **location** | **String**| The location id. | 
 **api** | **String**| The api id. | 
 **version** | **String**| The version id. | 
 **spec** | **String**| The spec id. | 

### Return type

[**ApiSpec**](ApiSpec.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## registryDeleteApiVersion

> registryDeleteApiVersion(project, location, api, version, opts)



DeleteApiVersion removes a specified version and all of the resources that  it owns.

### Example

```javascript
import RegistryApi from 'registry_api';

let apiInstance = new RegistryApi.RegistryApi();
let project = "project_example"; // String | The project id.
let location = "location_example"; // String | The location id.
let api = "api_example"; // String | The api id.
let version = "version_example"; // String | The version id.
let opts = {
  'force': true // Boolean | If set to true, any child resources will also be deleted. (Otherwise, the request will only work if there are no child resources.)
};
apiInstance.registryDeleteApiVersion(project, location, api, version, opts, (error, data, response) => {
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
 **project** | **String**| The project id. | 
 **location** | **String**| The location id. | 
 **api** | **String**| The api id. | 
 **version** | **String**| The version id. | 
 **force** | **Boolean**| If set to true, any child resources will also be deleted. (Otherwise, the request will only work if there are no child resources.) | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## registryDeleteArtifact

> registryDeleteArtifact(project, location, artifact)



DeleteArtifact removes a specified artifact.

### Example

```javascript
import RegistryApi from 'registry_api';

let apiInstance = new RegistryApi.RegistryApi();
let project = "project_example"; // String | The project id.
let location = "location_example"; // String | The location id.
let artifact = "artifact_example"; // String | The artifact id.
apiInstance.registryDeleteArtifact(project, location, artifact, (error, data, response) => {
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
 **project** | **String**| The project id. | 
 **location** | **String**| The location id. | 
 **artifact** | **String**| The artifact id. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## registryGetApi

> Api registryGetApi(project, location, api)



GetApi returns a specified API.

### Example

```javascript
import RegistryApi from 'registry_api';

let apiInstance = new RegistryApi.RegistryApi();
let project = "project_example"; // String | The project id.
let location = "location_example"; // String | The location id.
let api = "api_example"; // String | The api id.
apiInstance.registryGetApi(project, location, api, (error, data, response) => {
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
 **project** | **String**| The project id. | 
 **location** | **String**| The location id. | 
 **api** | **String**| The api id. | 

### Return type

[**Api**](Api.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## registryGetApiDeployment

> ApiDeployment registryGetApiDeployment(project, location, api, deployment)



GetApiDeployment returns a specified deployment.

### Example

```javascript
import RegistryApi from 'registry_api';

let apiInstance = new RegistryApi.RegistryApi();
let project = "project_example"; // String | The project id.
let location = "location_example"; // String | The location id.
let api = "api_example"; // String | The api id.
let deployment = "deployment_example"; // String | The deployment id.
apiInstance.registryGetApiDeployment(project, location, api, deployment, (error, data, response) => {
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
 **project** | **String**| The project id. | 
 **location** | **String**| The location id. | 
 **api** | **String**| The api id. | 
 **deployment** | **String**| The deployment id. | 

### Return type

[**ApiDeployment**](ApiDeployment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## registryGetApiSpec

> ApiSpec registryGetApiSpec(project, location, api, version, spec)



GetApiSpec returns a specified spec.

### Example

```javascript
import RegistryApi from 'registry_api';

let apiInstance = new RegistryApi.RegistryApi();
let project = "project_example"; // String | The project id.
let location = "location_example"; // String | The location id.
let api = "api_example"; // String | The api id.
let version = "version_example"; // String | The version id.
let spec = "spec_example"; // String | The spec id.
apiInstance.registryGetApiSpec(project, location, api, version, spec, (error, data, response) => {
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
 **project** | **String**| The project id. | 
 **location** | **String**| The location id. | 
 **api** | **String**| The api id. | 
 **version** | **String**| The version id. | 
 **spec** | **String**| The spec id. | 

### Return type

[**ApiSpec**](ApiSpec.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## registryGetApiSpecContents

> registryGetApiSpecContents(project, location, api, version, spec)



GetApiSpecContents returns the contents of a specified spec.  If specs are stored with GZip compression, the default behavior  is to return the spec uncompressed (the mime_type response field  indicates the exact format returned).

### Example

```javascript
import RegistryApi from 'registry_api';

let apiInstance = new RegistryApi.RegistryApi();
let project = "project_example"; // String | The project id.
let location = "location_example"; // String | The location id.
let api = "api_example"; // String | The api id.
let version = "version_example"; // String | The version id.
let spec = "spec_example"; // String | The spec id.
apiInstance.registryGetApiSpecContents(project, location, api, version, spec, (error, data, response) => {
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
 **project** | **String**| The project id. | 
 **location** | **String**| The location id. | 
 **api** | **String**| The api id. | 
 **version** | **String**| The version id. | 
 **spec** | **String**| The spec id. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json


## registryGetApiVersion

> ApiVersion registryGetApiVersion(project, location, api, version)



GetApiVersion returns a specified version.

### Example

```javascript
import RegistryApi from 'registry_api';

let apiInstance = new RegistryApi.RegistryApi();
let project = "project_example"; // String | The project id.
let location = "location_example"; // String | The location id.
let api = "api_example"; // String | The api id.
let version = "version_example"; // String | The version id.
apiInstance.registryGetApiVersion(project, location, api, version, (error, data, response) => {
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
 **project** | **String**| The project id. | 
 **location** | **String**| The location id. | 
 **api** | **String**| The api id. | 
 **version** | **String**| The version id. | 

### Return type

[**ApiVersion**](ApiVersion.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## registryGetArtifact

> Artifact registryGetArtifact(project, location, artifact)



GetArtifact returns a specified artifact.

### Example

```javascript
import RegistryApi from 'registry_api';

let apiInstance = new RegistryApi.RegistryApi();
let project = "project_example"; // String | The project id.
let location = "location_example"; // String | The location id.
let artifact = "artifact_example"; // String | The artifact id.
apiInstance.registryGetArtifact(project, location, artifact, (error, data, response) => {
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
 **project** | **String**| The project id. | 
 **location** | **String**| The location id. | 
 **artifact** | **String**| The artifact id. | 

### Return type

[**Artifact**](Artifact.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## registryGetArtifactContents

> registryGetArtifactContents(project, location, artifact)



GetArtifactContents returns the contents of a specified artifact.  If artifacts are stored with GZip compression, the default behavior  is to return the artifact uncompressed (the mime_type response field  indicates the exact format returned).

### Example

```javascript
import RegistryApi from 'registry_api';

let apiInstance = new RegistryApi.RegistryApi();
let project = "project_example"; // String | The project id.
let location = "location_example"; // String | The location id.
let artifact = "artifact_example"; // String | The artifact id.
apiInstance.registryGetArtifactContents(project, location, artifact, (error, data, response) => {
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
 **project** | **String**| The project id. | 
 **location** | **String**| The location id. | 
 **artifact** | **String**| The artifact id. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json


## registryListApiDeploymentRevisions

> ListApiDeploymentRevisionsResponse registryListApiDeploymentRevisions(project, location, api, deployment, opts)



ListApiDeploymentRevisions lists all revisions of a deployment.  Revisions are returned in descending order of revision creation time.

### Example

```javascript
import RegistryApi from 'registry_api';

let apiInstance = new RegistryApi.RegistryApi();
let project = "project_example"; // String | The project id.
let location = "location_example"; // String | The location id.
let api = "api_example"; // String | The api id.
let deployment = "deployment_example"; // String | The deployment id.
let opts = {
  'pageSize': 56, // Number | The maximum number of revisions to return per page.
  'pageToken': "pageToken_example" // String | The page token, received from a previous ListApiDeploymentRevisions call. Provide this to retrieve the subsequent page.
};
apiInstance.registryListApiDeploymentRevisions(project, location, api, deployment, opts, (error, data, response) => {
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
 **project** | **String**| The project id. | 
 **location** | **String**| The location id. | 
 **api** | **String**| The api id. | 
 **deployment** | **String**| The deployment id. | 
 **pageSize** | **Number**| The maximum number of revisions to return per page. | [optional] 
 **pageToken** | **String**| The page token, received from a previous ListApiDeploymentRevisions call. Provide this to retrieve the subsequent page. | [optional] 

### Return type

[**ListApiDeploymentRevisionsResponse**](ListApiDeploymentRevisionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## registryListApiDeployments

> ListApiDeploymentsResponse registryListApiDeployments(project, location, api, opts)



ListApiDeployments returns matching deployments.

### Example

```javascript
import RegistryApi from 'registry_api';

let apiInstance = new RegistryApi.RegistryApi();
let project = "project_example"; // String | The project id.
let location = "location_example"; // String | The location id.
let api = "api_example"; // String | The api id.
let opts = {
  'pageSize': 56, // Number | The maximum number of deployments to return. The service may return fewer than this value. If unspecified, at most 50 values will be returned. The maximum is 1000; values above 1000 will be coerced to 1000.
  'pageToken': "pageToken_example", // String | A page token, received from a previous `ListApiDeployments` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListApiDeployments` must match the call that provided the page token.
  'filter': "filter_example" // String | An expression that can be used to filter the list. Filters use the Common Expression Language and can refer to all message fields.
};
apiInstance.registryListApiDeployments(project, location, api, opts, (error, data, response) => {
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
 **project** | **String**| The project id. | 
 **location** | **String**| The location id. | 
 **api** | **String**| The api id. | 
 **pageSize** | **Number**| The maximum number of deployments to return. The service may return fewer than this value. If unspecified, at most 50 values will be returned. The maximum is 1000; values above 1000 will be coerced to 1000. | [optional] 
 **pageToken** | **String**| A page token, received from a previous &#x60;ListApiDeployments&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListApiDeployments&#x60; must match the call that provided the page token. | [optional] 
 **filter** | **String**| An expression that can be used to filter the list. Filters use the Common Expression Language and can refer to all message fields. | [optional] 

### Return type

[**ListApiDeploymentsResponse**](ListApiDeploymentsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## registryListApiSpecRevisions

> ListApiSpecRevisionsResponse registryListApiSpecRevisions(project, location, api, version, spec, opts)



ListApiSpecRevisions lists all revisions of a spec.  Revisions are returned in descending order of revision creation time.

### Example

```javascript
import RegistryApi from 'registry_api';

let apiInstance = new RegistryApi.RegistryApi();
let project = "project_example"; // String | The project id.
let location = "location_example"; // String | The location id.
let api = "api_example"; // String | The api id.
let version = "version_example"; // String | The version id.
let spec = "spec_example"; // String | The spec id.
let opts = {
  'pageSize': 56, // Number | The maximum number of revisions to return per page.
  'pageToken': "pageToken_example" // String | The page token, received from a previous ListApiSpecRevisions call. Provide this to retrieve the subsequent page.
};
apiInstance.registryListApiSpecRevisions(project, location, api, version, spec, opts, (error, data, response) => {
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
 **project** | **String**| The project id. | 
 **location** | **String**| The location id. | 
 **api** | **String**| The api id. | 
 **version** | **String**| The version id. | 
 **spec** | **String**| The spec id. | 
 **pageSize** | **Number**| The maximum number of revisions to return per page. | [optional] 
 **pageToken** | **String**| The page token, received from a previous ListApiSpecRevisions call. Provide this to retrieve the subsequent page. | [optional] 

### Return type

[**ListApiSpecRevisionsResponse**](ListApiSpecRevisionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## registryListApiSpecs

> ListApiSpecsResponse registryListApiSpecs(project, location, api, version, opts)



ListApiSpecs returns matching specs.

### Example

```javascript
import RegistryApi from 'registry_api';

let apiInstance = new RegistryApi.RegistryApi();
let project = "project_example"; // String | The project id.
let location = "location_example"; // String | The location id.
let api = "api_example"; // String | The api id.
let version = "version_example"; // String | The version id.
let opts = {
  'pageSize': 56, // Number | The maximum number of specs to return. The service may return fewer than this value. If unspecified, at most 50 values will be returned. The maximum is 1000; values above 1000 will be coerced to 1000.
  'pageToken': "pageToken_example", // String | A page token, received from a previous `ListApiSpecs` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListApiSpecs` must match the call that provided the page token.
  'filter': "filter_example" // String | An expression that can be used to filter the list. Filters use the Common Expression Language and can refer to all message fields except contents.
};
apiInstance.registryListApiSpecs(project, location, api, version, opts, (error, data, response) => {
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
 **project** | **String**| The project id. | 
 **location** | **String**| The location id. | 
 **api** | **String**| The api id. | 
 **version** | **String**| The version id. | 
 **pageSize** | **Number**| The maximum number of specs to return. The service may return fewer than this value. If unspecified, at most 50 values will be returned. The maximum is 1000; values above 1000 will be coerced to 1000. | [optional] 
 **pageToken** | **String**| A page token, received from a previous &#x60;ListApiSpecs&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListApiSpecs&#x60; must match the call that provided the page token. | [optional] 
 **filter** | **String**| An expression that can be used to filter the list. Filters use the Common Expression Language and can refer to all message fields except contents. | [optional] 

### Return type

[**ListApiSpecsResponse**](ListApiSpecsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## registryListApiVersions

> ListApiVersionsResponse registryListApiVersions(project, location, api, opts)



ListApiVersions returns matching versions.

### Example

```javascript
import RegistryApi from 'registry_api';

let apiInstance = new RegistryApi.RegistryApi();
let project = "project_example"; // String | The project id.
let location = "location_example"; // String | The location id.
let api = "api_example"; // String | The api id.
let opts = {
  'pageSize': 56, // Number | The maximum number of versions to return. The service may return fewer than this value. If unspecified, at most 50 values will be returned. The maximum is 1000; values above 1000 will be coerced to 1000.
  'pageToken': "pageToken_example", // String | A page token, received from a previous `ListApiVersions` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListApiVersions` must match the call that provided the page token.
  'filter': "filter_example" // String | An expression that can be used to filter the list. Filters use the Common Expression Language and can refer to all message fields.
};
apiInstance.registryListApiVersions(project, location, api, opts, (error, data, response) => {
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
 **project** | **String**| The project id. | 
 **location** | **String**| The location id. | 
 **api** | **String**| The api id. | 
 **pageSize** | **Number**| The maximum number of versions to return. The service may return fewer than this value. If unspecified, at most 50 values will be returned. The maximum is 1000; values above 1000 will be coerced to 1000. | [optional] 
 **pageToken** | **String**| A page token, received from a previous &#x60;ListApiVersions&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListApiVersions&#x60; must match the call that provided the page token. | [optional] 
 **filter** | **String**| An expression that can be used to filter the list. Filters use the Common Expression Language and can refer to all message fields. | [optional] 

### Return type

[**ListApiVersionsResponse**](ListApiVersionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## registryListApis

> ListApisResponse registryListApis(project, location, opts)



ListApis returns matching APIs.

### Example

```javascript
import RegistryApi from 'registry_api';

let apiInstance = new RegistryApi.RegistryApi();
let project = "project_example"; // String | The project id.
let location = "location_example"; // String | The location id.
let opts = {
  'pageSize': 56, // Number | The maximum number of APIs to return. The service may return fewer than this value. If unspecified, at most 50 values will be returned. The maximum is 1000; values above 1000 will be coerced to 1000.
  'pageToken': "pageToken_example", // String | A page token, received from a previous `ListApis` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListApis` must match the call that provided the page token.
  'filter': "filter_example" // String | An expression that can be used to filter the list. Filters use the Common Expression Language and can refer to all message fields.
};
apiInstance.registryListApis(project, location, opts, (error, data, response) => {
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
 **project** | **String**| The project id. | 
 **location** | **String**| The location id. | 
 **pageSize** | **Number**| The maximum number of APIs to return. The service may return fewer than this value. If unspecified, at most 50 values will be returned. The maximum is 1000; values above 1000 will be coerced to 1000. | [optional] 
 **pageToken** | **String**| A page token, received from a previous &#x60;ListApis&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListApis&#x60; must match the call that provided the page token. | [optional] 
 **filter** | **String**| An expression that can be used to filter the list. Filters use the Common Expression Language and can refer to all message fields. | [optional] 

### Return type

[**ListApisResponse**](ListApisResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## registryListArtifacts

> ListArtifactsResponse registryListArtifacts(project, location, opts)



ListArtifacts returns matching artifacts.

### Example

```javascript
import RegistryApi from 'registry_api';

let apiInstance = new RegistryApi.RegistryApi();
let project = "project_example"; // String | The project id.
let location = "location_example"; // String | The location id.
let opts = {
  'pageSize': 56, // Number | The maximum number of artifacts to return. The service may return fewer than this value. If unspecified, at most 50 values will be returned. The maximum is 1000; values above 1000 will be coerced to 1000.
  'pageToken': "pageToken_example", // String | A page token, received from a previous `ListArtifacts` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListArtifacts` must match the call that provided the page token.
  'filter': "filter_example" // String | An expression that can be used to filter the list. Filters use the Common Expression Language and can refer to all message fields except contents.
};
apiInstance.registryListArtifacts(project, location, opts, (error, data, response) => {
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
 **project** | **String**| The project id. | 
 **location** | **String**| The location id. | 
 **pageSize** | **Number**| The maximum number of artifacts to return. The service may return fewer than this value. If unspecified, at most 50 values will be returned. The maximum is 1000; values above 1000 will be coerced to 1000. | [optional] 
 **pageToken** | **String**| A page token, received from a previous &#x60;ListArtifacts&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListArtifacts&#x60; must match the call that provided the page token. | [optional] 
 **filter** | **String**| An expression that can be used to filter the list. Filters use the Common Expression Language and can refer to all message fields except contents. | [optional] 

### Return type

[**ListArtifactsResponse**](ListArtifactsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## registryReplaceArtifact

> Artifact registryReplaceArtifact(project, location, artifact, artifact2)



ReplaceArtifact can be used to replace a specified artifact.

### Example

```javascript
import RegistryApi from 'registry_api';

let apiInstance = new RegistryApi.RegistryApi();
let project = "project_example"; // String | The project id.
let location = "location_example"; // String | The location id.
let artifact = "artifact_example"; // String | The artifact id.
let artifact2 = new RegistryApi.Artifact(); // Artifact | 
apiInstance.registryReplaceArtifact(project, location, artifact, artifact2, (error, data, response) => {
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
 **project** | **String**| The project id. | 
 **location** | **String**| The location id. | 
 **artifact** | **String**| The artifact id. | 
 **artifact2** | [**Artifact**](Artifact.md)|  | 

### Return type

[**Artifact**](Artifact.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## registryRollbackApiDeployment

> ApiDeployment registryRollbackApiDeployment(project, location, api, deployment, rollbackApiDeploymentRequest)



RollbackApiDeployment sets the current revision to a specified prior  revision. Note that this creates a new revision with a new revision ID.

### Example

```javascript
import RegistryApi from 'registry_api';

let apiInstance = new RegistryApi.RegistryApi();
let project = "project_example"; // String | The project id.
let location = "location_example"; // String | The location id.
let api = "api_example"; // String | The api id.
let deployment = "deployment_example"; // String | The deployment id.
let rollbackApiDeploymentRequest = new RegistryApi.RollbackApiDeploymentRequest(); // RollbackApiDeploymentRequest | 
apiInstance.registryRollbackApiDeployment(project, location, api, deployment, rollbackApiDeploymentRequest, (error, data, response) => {
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
 **project** | **String**| The project id. | 
 **location** | **String**| The location id. | 
 **api** | **String**| The api id. | 
 **deployment** | **String**| The deployment id. | 
 **rollbackApiDeploymentRequest** | [**RollbackApiDeploymentRequest**](RollbackApiDeploymentRequest.md)|  | 

### Return type

[**ApiDeployment**](ApiDeployment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## registryRollbackApiSpec

> ApiSpec registryRollbackApiSpec(project, location, api, version, spec, rollbackApiSpecRequest)



RollbackApiSpec sets the current revision to a specified prior revision.  Note that this creates a new revision with a new revision ID.

### Example

```javascript
import RegistryApi from 'registry_api';

let apiInstance = new RegistryApi.RegistryApi();
let project = "project_example"; // String | The project id.
let location = "location_example"; // String | The location id.
let api = "api_example"; // String | The api id.
let version = "version_example"; // String | The version id.
let spec = "spec_example"; // String | The spec id.
let rollbackApiSpecRequest = new RegistryApi.RollbackApiSpecRequest(); // RollbackApiSpecRequest | 
apiInstance.registryRollbackApiSpec(project, location, api, version, spec, rollbackApiSpecRequest, (error, data, response) => {
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
 **project** | **String**| The project id. | 
 **location** | **String**| The location id. | 
 **api** | **String**| The api id. | 
 **version** | **String**| The version id. | 
 **spec** | **String**| The spec id. | 
 **rollbackApiSpecRequest** | [**RollbackApiSpecRequest**](RollbackApiSpecRequest.md)|  | 

### Return type

[**ApiSpec**](ApiSpec.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## registryTagApiDeploymentRevision

> ApiDeployment registryTagApiDeploymentRevision(project, location, api, deployment, tagApiDeploymentRevisionRequest)



TagApiDeploymentRevision adds a tag to a specified revision of a  deployment.

### Example

```javascript
import RegistryApi from 'registry_api';

let apiInstance = new RegistryApi.RegistryApi();
let project = "project_example"; // String | The project id.
let location = "location_example"; // String | The location id.
let api = "api_example"; // String | The api id.
let deployment = "deployment_example"; // String | The deployment id.
let tagApiDeploymentRevisionRequest = new RegistryApi.TagApiDeploymentRevisionRequest(); // TagApiDeploymentRevisionRequest | 
apiInstance.registryTagApiDeploymentRevision(project, location, api, deployment, tagApiDeploymentRevisionRequest, (error, data, response) => {
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
 **project** | **String**| The project id. | 
 **location** | **String**| The location id. | 
 **api** | **String**| The api id. | 
 **deployment** | **String**| The deployment id. | 
 **tagApiDeploymentRevisionRequest** | [**TagApiDeploymentRevisionRequest**](TagApiDeploymentRevisionRequest.md)|  | 

### Return type

[**ApiDeployment**](ApiDeployment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## registryTagApiSpecRevision

> ApiSpec registryTagApiSpecRevision(project, location, api, version, spec, tagApiSpecRevisionRequest)



TagApiSpecRevision adds a tag to a specified revision of a spec.

### Example

```javascript
import RegistryApi from 'registry_api';

let apiInstance = new RegistryApi.RegistryApi();
let project = "project_example"; // String | The project id.
let location = "location_example"; // String | The location id.
let api = "api_example"; // String | The api id.
let version = "version_example"; // String | The version id.
let spec = "spec_example"; // String | The spec id.
let tagApiSpecRevisionRequest = new RegistryApi.TagApiSpecRevisionRequest(); // TagApiSpecRevisionRequest | 
apiInstance.registryTagApiSpecRevision(project, location, api, version, spec, tagApiSpecRevisionRequest, (error, data, response) => {
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
 **project** | **String**| The project id. | 
 **location** | **String**| The location id. | 
 **api** | **String**| The api id. | 
 **version** | **String**| The version id. | 
 **spec** | **String**| The spec id. | 
 **tagApiSpecRevisionRequest** | [**TagApiSpecRevisionRequest**](TagApiSpecRevisionRequest.md)|  | 

### Return type

[**ApiSpec**](ApiSpec.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## registryUpdateApi

> Api registryUpdateApi(project, location, api, api2, opts)



UpdateApi can be used to modify a specified API.

### Example

```javascript
import RegistryApi from 'registry_api';

let apiInstance = new RegistryApi.RegistryApi();
let project = "project_example"; // String | The project id.
let location = "location_example"; // String | The location id.
let api = "api_example"; // String | The api id.
let api2 = new RegistryApi.Api(); // Api | 
let opts = {
  'updateMask': "updateMask_example", // String | The list of fields to be updated. If omitted, all fields are updated that are set in the request message (fields set to default values are ignored). If a \"*\" is specified, all fields are updated, including fields that are unspecified/default in the request.
  'allowMissing': true // Boolean | If set to true, and the api is not found, a new api_versions will be created. In this situation, `update_mask` is ignored.
};
apiInstance.registryUpdateApi(project, location, api, api2, opts, (error, data, response) => {
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
 **project** | **String**| The project id. | 
 **location** | **String**| The location id. | 
 **api** | **String**| The api id. | 
 **api2** | [**Api**](Api.md)|  | 
 **updateMask** | **String**| The list of fields to be updated. If omitted, all fields are updated that are set in the request message (fields set to default values are ignored). If a \&quot;*\&quot; is specified, all fields are updated, including fields that are unspecified/default in the request. | [optional] 
 **allowMissing** | **Boolean**| If set to true, and the api is not found, a new api_versions will be created. In this situation, &#x60;update_mask&#x60; is ignored. | [optional] 

### Return type

[**Api**](Api.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## registryUpdateApiDeployment

> ApiDeployment registryUpdateApiDeployment(project, location, api, deployment, apiDeployment, opts)



UpdateApiDeployment can be used to modify a specified deployment.

### Example

```javascript
import RegistryApi from 'registry_api';

let apiInstance = new RegistryApi.RegistryApi();
let project = "project_example"; // String | The project id.
let location = "location_example"; // String | The location id.
let api = "api_example"; // String | The api id.
let deployment = "deployment_example"; // String | The deployment id.
let apiDeployment = new RegistryApi.ApiDeployment(); // ApiDeployment | 
let opts = {
  'updateMask': "updateMask_example", // String | The list of fields to be updated. If omitted, all fields are updated that are set in the request message (fields set to default values are ignored). If a \"*\" is specified, all fields are updated, including fields that are unspecified/default in the request.
  'allowMissing': true // Boolean | If set to true, and the deployment is not found, a new deployment will be created. In this situation, `update_mask` is ignored.
};
apiInstance.registryUpdateApiDeployment(project, location, api, deployment, apiDeployment, opts, (error, data, response) => {
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
 **project** | **String**| The project id. | 
 **location** | **String**| The location id. | 
 **api** | **String**| The api id. | 
 **deployment** | **String**| The deployment id. | 
 **apiDeployment** | [**ApiDeployment**](ApiDeployment.md)|  | 
 **updateMask** | **String**| The list of fields to be updated. If omitted, all fields are updated that are set in the request message (fields set to default values are ignored). If a \&quot;*\&quot; is specified, all fields are updated, including fields that are unspecified/default in the request. | [optional] 
 **allowMissing** | **Boolean**| If set to true, and the deployment is not found, a new deployment will be created. In this situation, &#x60;update_mask&#x60; is ignored. | [optional] 

### Return type

[**ApiDeployment**](ApiDeployment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## registryUpdateApiSpec

> ApiSpec registryUpdateApiSpec(project, location, api, version, spec, apiSpec, opts)



UpdateApiSpec can be used to modify a specified spec.

### Example

```javascript
import RegistryApi from 'registry_api';

let apiInstance = new RegistryApi.RegistryApi();
let project = "project_example"; // String | The project id.
let location = "location_example"; // String | The location id.
let api = "api_example"; // String | The api id.
let version = "version_example"; // String | The version id.
let spec = "spec_example"; // String | The spec id.
let apiSpec = new RegistryApi.ApiSpec(); // ApiSpec | 
let opts = {
  'updateMask': "updateMask_example", // String | The list of fields to be updated. If omitted, all fields are updated that are set in the request message (fields set to default values are ignored). If a \"*\" is specified, all fields are updated, including fields that are unspecified/default in the request.
  'allowMissing': true // Boolean | If set to true, and the spec is not found, a new spec will be created. In this situation, `update_mask` is ignored.
};
apiInstance.registryUpdateApiSpec(project, location, api, version, spec, apiSpec, opts, (error, data, response) => {
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
 **project** | **String**| The project id. | 
 **location** | **String**| The location id. | 
 **api** | **String**| The api id. | 
 **version** | **String**| The version id. | 
 **spec** | **String**| The spec id. | 
 **apiSpec** | [**ApiSpec**](ApiSpec.md)|  | 
 **updateMask** | **String**| The list of fields to be updated. If omitted, all fields are updated that are set in the request message (fields set to default values are ignored). If a \&quot;*\&quot; is specified, all fields are updated, including fields that are unspecified/default in the request. | [optional] 
 **allowMissing** | **Boolean**| If set to true, and the spec is not found, a new spec will be created. In this situation, &#x60;update_mask&#x60; is ignored. | [optional] 

### Return type

[**ApiSpec**](ApiSpec.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## registryUpdateApiVersion

> ApiVersion registryUpdateApiVersion(project, location, api, version, apiVersion, opts)



UpdateApiVersion can be used to modify a specified version.

### Example

```javascript
import RegistryApi from 'registry_api';

let apiInstance = new RegistryApi.RegistryApi();
let project = "project_example"; // String | The project id.
let location = "location_example"; // String | The location id.
let api = "api_example"; // String | The api id.
let version = "version_example"; // String | The version id.
let apiVersion = new RegistryApi.ApiVersion(); // ApiVersion | 
let opts = {
  'updateMask': "updateMask_example", // String | The list of fields to be updated. If omitted, all fields are updated that are set in the request message (fields set to default values are ignored). If a \"*\" is specified, all fields are updated, including fields that are unspecified/default in the request.
  'allowMissing': true // Boolean | If set to true, and the version is not found, a new version will be created. In this situation, `update_mask` is ignored.
};
apiInstance.registryUpdateApiVersion(project, location, api, version, apiVersion, opts, (error, data, response) => {
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
 **project** | **String**| The project id. | 
 **location** | **String**| The location id. | 
 **api** | **String**| The api id. | 
 **version** | **String**| The version id. | 
 **apiVersion** | [**ApiVersion**](ApiVersion.md)|  | 
 **updateMask** | **String**| The list of fields to be updated. If omitted, all fields are updated that are set in the request message (fields set to default values are ignored). If a \&quot;*\&quot; is specified, all fields are updated, including fields that are unspecified/default in the request. | [optional] 
 **allowMissing** | **Boolean**| If set to true, and the version is not found, a new version will be created. In this situation, &#x60;update_mask&#x60; is ignored. | [optional] 

### Return type

[**ApiVersion**](ApiVersion.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

