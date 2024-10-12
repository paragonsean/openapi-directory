# TheJiraCloudPlatformRestApi.ProjectFeaturesApi

All URIs are relative to *https://your-domain.atlassian.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getFeaturesForProject**](ProjectFeaturesApi.md#getFeaturesForProject) | **GET** /rest/api/3/project/{projectIdOrKey}/features | Get project features
[**toggleFeatureForProject**](ProjectFeaturesApi.md#toggleFeatureForProject) | **PUT** /rest/api/3/project/{projectIdOrKey}/features/{featureKey} | Set project feature state



## getFeaturesForProject

> ContainerForProjectFeatures getFeaturesForProject(projectIdOrKey)

Get project features

Returns the list of features for a project.

### Example

```javascript
import TheJiraCloudPlatformRestApi from 'the_jira_cloud_platform_rest_api';
let defaultClient = TheJiraCloudPlatformRestApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new TheJiraCloudPlatformRestApi.ProjectFeaturesApi();
let projectIdOrKey = "projectIdOrKey_example"; // String | The ID or (case-sensitive) key of the project.
apiInstance.getFeaturesForProject(projectIdOrKey, (error, data, response) => {
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
 **projectIdOrKey** | **String**| The ID or (case-sensitive) key of the project. | 

### Return type

[**ContainerForProjectFeatures**](ContainerForProjectFeatures.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## toggleFeatureForProject

> ContainerForProjectFeatures toggleFeatureForProject(projectIdOrKey, featureKey, projectFeatureState)

Set project feature state

Sets the state of a project feature.

### Example

```javascript
import TheJiraCloudPlatformRestApi from 'the_jira_cloud_platform_rest_api';
let defaultClient = TheJiraCloudPlatformRestApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new TheJiraCloudPlatformRestApi.ProjectFeaturesApi();
let projectIdOrKey = "projectIdOrKey_example"; // String | The ID or (case-sensitive) key of the project.
let featureKey = "featureKey_example"; // String | The key of the feature.
let projectFeatureState = {"state":"ENABLED"}; // ProjectFeatureState | Details of the feature state change.
apiInstance.toggleFeatureForProject(projectIdOrKey, featureKey, projectFeatureState, (error, data, response) => {
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
 **projectIdOrKey** | **String**| The ID or (case-sensitive) key of the project. | 
 **featureKey** | **String**| The key of the feature. | 
 **projectFeatureState** | [**ProjectFeatureState**](ProjectFeatureState.md)| Details of the feature state change. | 

### Return type

[**ContainerForProjectFeatures**](ContainerForProjectFeatures.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

