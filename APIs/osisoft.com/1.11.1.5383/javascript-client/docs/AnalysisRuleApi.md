# PiWebApi2018Sp1SwaggerSpec.AnalysisRuleApi

All URIs are relative to *https://devdata.osisoft.com/piwebapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analysisRuleCreateAnalysisRule**](AnalysisRuleApi.md#analysisRuleCreateAnalysisRule) | **POST** /analysisrules/{webId}/analysisrules | Create a new Analysis Rule as a child of an existing Analysis Rule.
[**analysisRuleDelete**](AnalysisRuleApi.md#analysisRuleDelete) | **DELETE** /analysisrules/{webId} | Delete an Analysis Rule.
[**analysisRuleGet**](AnalysisRuleApi.md#analysisRuleGet) | **GET** /analysisrules/{webId} | Retrieve an Analysis Rule.
[**analysisRuleGetAnalysisRules**](AnalysisRuleApi.md#analysisRuleGetAnalysisRules) | **GET** /analysisrules/{webId}/analysisrules | Get the child Analysis Rules of the Analysis Rule.
[**analysisRuleGetByPath**](AnalysisRuleApi.md#analysisRuleGetByPath) | **GET** /analysisrules | Retrieve an Analysis Rule by path.
[**analysisRuleUpdate**](AnalysisRuleApi.md#analysisRuleUpdate) | **PATCH** /analysisrules/{webId} | Update an Analysis Rule by replacing items in its definition.



## analysisRuleCreateAnalysisRule

> analysisRuleCreateAnalysisRule(webId, analysisRule, opts)

Create a new Analysis Rule as a child of an existing Analysis Rule.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AnalysisRuleApi();
let webId = "webId_example"; // String | The ID of the parent Analysis Rule, on which to create the child Analysis Rule.
let analysisRule = new PiWebApi2018Sp1SwaggerSpec.AnalysisRule(); // AnalysisRule | The definition of the new Analysis Rule.
let opts = {
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.analysisRuleCreateAnalysisRule(webId, analysisRule, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the parent Analysis Rule, on which to create the child Analysis Rule. | 
 **analysisRule** | [**AnalysisRule**](AnalysisRule.md)| The definition of the new Analysis Rule. | 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: Not defined


## analysisRuleDelete

> analysisRuleDelete(webId)

Delete an Analysis Rule.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AnalysisRuleApi();
let webId = "webId_example"; // String | The ID of the Analysis Rule.
apiInstance.analysisRuleDelete(webId, (error, data, response) => {
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
 **webId** | **String**| The ID of the Analysis Rule. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## analysisRuleGet

> AnalysisRule analysisRuleGet(webId, opts)

Retrieve an Analysis Rule.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AnalysisRuleApi();
let webId = "webId_example"; // String | The ID of the Analysis Rule.
let opts = {
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.analysisRuleGet(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the Analysis Rule. | 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**AnalysisRule**](AnalysisRule.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## analysisRuleGetAnalysisRules

> ItemsAnalysisRule analysisRuleGetAnalysisRules(webId, opts)

Get the child Analysis Rules of the Analysis Rule.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AnalysisRuleApi();
let webId = "webId_example"; // String | The ID of the parent Analysis Rule.
let opts = {
  'maxCount': 56, // Number | The maximum number of objects to be returned per call (page size). The default is 1000.
  'nameFilter': "nameFilter_example", // String | The name query string used for finding Analysis Rules. The default is no filter.
  'searchFullHierarchy': true, // Boolean | Specifies if the search should include Analysis Rules nested further than the immediate children of the searchRoot. The default is 'false'.
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'sortField': "sortField_example", // String | The field or property of the object used to sort the returned collection. The default is 'Name'.
  'sortOrder': "sortOrder_example", // String | The order that the returned collection is sorted. The default is 'Ascending'.
  'startIndex': 56, // Number | The starting index (zero based) of the items to be returned. The default is 0.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.analysisRuleGetAnalysisRules(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the parent Analysis Rule. | 
 **maxCount** | **Number**| The maximum number of objects to be returned per call (page size). The default is 1000. | [optional] 
 **nameFilter** | **String**| The name query string used for finding Analysis Rules. The default is no filter. | [optional] 
 **searchFullHierarchy** | **Boolean**| Specifies if the search should include Analysis Rules nested further than the immediate children of the searchRoot. The default is &#39;false&#39;. | [optional] 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **sortField** | **String**| The field or property of the object used to sort the returned collection. The default is &#39;Name&#39;. | [optional] 
 **sortOrder** | **String**| The order that the returned collection is sorted. The default is &#39;Ascending&#39;. | [optional] 
 **startIndex** | **Number**| The starting index (zero based) of the items to be returned. The default is 0. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsAnalysisRule**](ItemsAnalysisRule.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## analysisRuleGetByPath

> AnalysisRule analysisRuleGetByPath(path, opts)

Retrieve an Analysis Rule by path.

This method returns an Analysis Rule based on the hierarchical path associated with it, and should be used when a path has been received from a separate part of the PI System for use in the PI Web API. Users should primarily search with the WebID when available.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AnalysisRuleApi();
let path = "path_example"; // String | The path to the Analysis Rule.
let opts = {
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.analysisRuleGetByPath(path, opts, (error, data, response) => {
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
 **path** | **String**| The path to the Analysis Rule. | 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**AnalysisRule**](AnalysisRule.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## analysisRuleUpdate

> analysisRuleUpdate(webId, analysisRule)

Update an Analysis Rule by replacing items in its definition.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AnalysisRuleApi();
let webId = "webId_example"; // String | The ID of the Analysis Rule.
let analysisRule = new PiWebApi2018Sp1SwaggerSpec.AnalysisRule(); // AnalysisRule | A partial Analysis Rule containing the desired changes.
apiInstance.analysisRuleUpdate(webId, analysisRule, (error, data, response) => {
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
 **webId** | **String**| The ID of the Analysis Rule. | 
 **analysisRule** | [**AnalysisRule**](AnalysisRule.md)| A partial Analysis Rule containing the desired changes. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: Not defined

