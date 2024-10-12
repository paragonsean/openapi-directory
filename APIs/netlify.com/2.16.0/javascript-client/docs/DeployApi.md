# NetlifysApiDocumentation.DeployApi

All URIs are relative to *https://api.netlify.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancelSiteDeploy**](DeployApi.md#cancelSiteDeploy) | **POST** /deploys/{deploy_id}/cancel | 
[**createSiteDeploy**](DeployApi.md#createSiteDeploy) | **POST** /sites/{site_id}/deploys | 
[**deleteDeploy**](DeployApi.md#deleteDeploy) | **DELETE** /deploys/{deploy_id} | 
[**deleteSiteDeploy**](DeployApi.md#deleteSiteDeploy) | **DELETE** /sites/{site_id}/deploys/{deploy_id} | 
[**getDeploy**](DeployApi.md#getDeploy) | **GET** /deploys/{deploy_id} | 
[**getSiteDeploy**](DeployApi.md#getSiteDeploy) | **GET** /sites/{site_id}/deploys/{deploy_id} | 
[**listSiteDeploys**](DeployApi.md#listSiteDeploys) | **GET** /sites/{site_id}/deploys | 
[**lockDeploy**](DeployApi.md#lockDeploy) | **POST** /deploys/{deploy_id}/lock | 
[**restoreSiteDeploy**](DeployApi.md#restoreSiteDeploy) | **POST** /sites/{site_id}/deploys/{deploy_id}/restore | 
[**rollbackSiteDeploy**](DeployApi.md#rollbackSiteDeploy) | **PUT** /sites/{site_id}/rollback | 
[**unlockDeploy**](DeployApi.md#unlockDeploy) | **POST** /deploys/{deploy_id}/unlock | 
[**updateSiteDeploy**](DeployApi.md#updateSiteDeploy) | **PUT** /sites/{site_id}/deploys/{deploy_id} | 



## cancelSiteDeploy

> Deploy cancelSiteDeploy(deployId)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.DeployApi();
let deployId = "deployId_example"; // String | 
apiInstance.cancelSiteDeploy(deployId, (error, data, response) => {
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
 **deployId** | **String**|  | 

### Return type

[**Deploy**](Deploy.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createSiteDeploy

> Deploy createSiteDeploy(siteId, deploy, opts)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.DeployApi();
let siteId = "siteId_example"; // String | 
let deploy = new NetlifysApiDocumentation.DeployFiles(); // DeployFiles | 
let opts = {
  'deployPreviews': true, // Boolean | 
  'production': true, // Boolean | 
  'state': "state_example", // String | 
  'branch': "branch_example", // String | 
  'latestPublished': true, // Boolean | 
  'title': "title_example" // String | 
};
apiInstance.createSiteDeploy(siteId, deploy, opts, (error, data, response) => {
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
 **siteId** | **String**|  | 
 **deploy** | [**DeployFiles**](DeployFiles.md)|  | 
 **deployPreviews** | **Boolean**|  | [optional] 
 **production** | **Boolean**|  | [optional] 
 **state** | **String**|  | [optional] 
 **branch** | **String**|  | [optional] 
 **latestPublished** | **Boolean**|  | [optional] 
 **title** | **String**|  | [optional] 

### Return type

[**Deploy**](Deploy.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteDeploy

> deleteDeploy(deployId)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.DeployApi();
let deployId = "deployId_example"; // String | 
apiInstance.deleteDeploy(deployId, (error, data, response) => {
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
 **deployId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteSiteDeploy

> deleteSiteDeploy(deployId, siteId)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.DeployApi();
let deployId = "deployId_example"; // String | 
let siteId = "siteId_example"; // String | 
apiInstance.deleteSiteDeploy(deployId, siteId, (error, data, response) => {
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
 **deployId** | **String**|  | 
 **siteId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDeploy

> Deploy getDeploy(deployId)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.DeployApi();
let deployId = "deployId_example"; // String | 
apiInstance.getDeploy(deployId, (error, data, response) => {
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
 **deployId** | **String**|  | 

### Return type

[**Deploy**](Deploy.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSiteDeploy

> Deploy getSiteDeploy(siteId, deployId)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.DeployApi();
let siteId = "siteId_example"; // String | 
let deployId = "deployId_example"; // String | 
apiInstance.getSiteDeploy(siteId, deployId, (error, data, response) => {
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
 **siteId** | **String**|  | 
 **deployId** | **String**|  | 

### Return type

[**Deploy**](Deploy.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSiteDeploys

> [Deploy] listSiteDeploys(siteId, opts)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.DeployApi();
let siteId = "siteId_example"; // String | 
let opts = {
  'deployPreviews': true, // Boolean | 
  'production': true, // Boolean | 
  'state': "state_example", // String | 
  'branch': "branch_example", // String | 
  'latestPublished': true, // Boolean | 
  'page': 56, // Number | 
  'perPage': 56 // Number | 
};
apiInstance.listSiteDeploys(siteId, opts, (error, data, response) => {
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
 **siteId** | **String**|  | 
 **deployPreviews** | **Boolean**|  | [optional] 
 **production** | **Boolean**|  | [optional] 
 **state** | **String**|  | [optional] 
 **branch** | **String**|  | [optional] 
 **latestPublished** | **Boolean**|  | [optional] 
 **page** | **Number**|  | [optional] 
 **perPage** | **Number**|  | [optional] 

### Return type

[**[Deploy]**](Deploy.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## lockDeploy

> Deploy lockDeploy(deployId)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.DeployApi();
let deployId = "deployId_example"; // String | 
apiInstance.lockDeploy(deployId, (error, data, response) => {
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
 **deployId** | **String**|  | 

### Return type

[**Deploy**](Deploy.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## restoreSiteDeploy

> Deploy restoreSiteDeploy(siteId, deployId)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.DeployApi();
let siteId = "siteId_example"; // String | 
let deployId = "deployId_example"; // String | 
apiInstance.restoreSiteDeploy(siteId, deployId, (error, data, response) => {
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
 **siteId** | **String**|  | 
 **deployId** | **String**|  | 

### Return type

[**Deploy**](Deploy.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## rollbackSiteDeploy

> rollbackSiteDeploy(siteId)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.DeployApi();
let siteId = "siteId_example"; // String | 
apiInstance.rollbackSiteDeploy(siteId, (error, data, response) => {
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
 **siteId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## unlockDeploy

> Deploy unlockDeploy(deployId)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.DeployApi();
let deployId = "deployId_example"; // String | 
apiInstance.unlockDeploy(deployId, (error, data, response) => {
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
 **deployId** | **String**|  | 

### Return type

[**Deploy**](Deploy.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateSiteDeploy

> Deploy updateSiteDeploy(siteId, deployId, deploy)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.DeployApi();
let siteId = "siteId_example"; // String | 
let deployId = "deployId_example"; // String | 
let deploy = new NetlifysApiDocumentation.DeployFiles(); // DeployFiles | 
apiInstance.updateSiteDeploy(siteId, deployId, deploy, (error, data, response) => {
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
 **siteId** | **String**|  | 
 **deployId** | **String**|  | 
 **deploy** | [**DeployFiles**](DeployFiles.md)|  | 

### Return type

[**Deploy**](Deploy.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

