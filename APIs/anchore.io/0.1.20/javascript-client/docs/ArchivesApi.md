# AnchoreEngineApiServer.ArchivesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archiveImageAnalysis**](ArchivesApi.md#archiveImageAnalysis) | **POST** /archives/images | 
[**createAnalysisArchiveRule**](ArchivesApi.md#createAnalysisArchiveRule) | **POST** /archives/rules | 
[**deleteAnalysisArchiveRule**](ArchivesApi.md#deleteAnalysisArchiveRule) | **DELETE** /archives/rules/{ruleId} | 
[**deleteArchivedAnalysis**](ArchivesApi.md#deleteArchivedAnalysis) | **DELETE** /archives/images/{imageDigest} | 
[**getAnalysisArchiveRule**](ArchivesApi.md#getAnalysisArchiveRule) | **GET** /archives/rules/{ruleId} | 
[**getArchivedAnalysis**](ArchivesApi.md#getArchivedAnalysis) | **GET** /archives/images/{imageDigest} | 
[**listAnalysisArchive**](ArchivesApi.md#listAnalysisArchive) | **GET** /archives/images | 
[**listAnalysisArchiveRules**](ArchivesApi.md#listAnalysisArchiveRules) | **GET** /archives/rules | 
[**listArchives**](ArchivesApi.md#listArchives) | **GET** /archives | 



## archiveImageAnalysis

> [AnalysisArchiveAddResult] archiveImageAnalysis(requestBody)



### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.ArchivesApi();
let requestBody = ["null"]; // [String] | 
apiInstance.archiveImageAnalysis(requestBody, (error, data, response) => {
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
 **requestBody** | [**[String]**](String.md)|  | 

### Return type

[**[AnalysisArchiveAddResult]**](AnalysisArchiveAddResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createAnalysisArchiveRule

> AnalysisArchiveTransitionRule createAnalysisArchiveRule(analysisArchiveTransitionRule)



### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.ArchivesApi();
let analysisArchiveTransitionRule = new AnchoreEngineApiServer.AnalysisArchiveTransitionRule(); // AnalysisArchiveTransitionRule | 
apiInstance.createAnalysisArchiveRule(analysisArchiveTransitionRule, (error, data, response) => {
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
 **analysisArchiveTransitionRule** | [**AnalysisArchiveTransitionRule**](AnalysisArchiveTransitionRule.md)|  | 

### Return type

[**AnalysisArchiveTransitionRule**](AnalysisArchiveTransitionRule.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteAnalysisArchiveRule

> deleteAnalysisArchiveRule(ruleId)



### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.ArchivesApi();
let ruleId = "ruleId_example"; // String | 
apiInstance.deleteAnalysisArchiveRule(ruleId, (error, data, response) => {
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
 **ruleId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteArchivedAnalysis

> deleteArchivedAnalysis(imageDigest, opts)



Performs a synchronous archive deletion

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.ArchivesApi();
let imageDigest = "imageDigest_example"; // String | 
let opts = {
  'force': true // Boolean | 
};
apiInstance.deleteArchivedAnalysis(imageDigest, opts, (error, data, response) => {
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
 **imageDigest** | **String**|  | 
 **force** | **Boolean**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAnalysisArchiveRule

> AnalysisArchiveTransitionRule getAnalysisArchiveRule(ruleId)



### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.ArchivesApi();
let ruleId = "ruleId_example"; // String | 
apiInstance.getAnalysisArchiveRule(ruleId, (error, data, response) => {
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
 **ruleId** | **String**|  | 

### Return type

[**AnalysisArchiveTransitionRule**](AnalysisArchiveTransitionRule.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getArchivedAnalysis

> ArchivedAnalysis getArchivedAnalysis(imageDigest)



Returns the archive metadata record identifying the image and tags for the analysis in the archive.

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.ArchivesApi();
let imageDigest = "imageDigest_example"; // String | The image digest to identify the image analysis
apiInstance.getArchivedAnalysis(imageDigest, (error, data, response) => {
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
 **imageDigest** | **String**| The image digest to identify the image analysis | 

### Return type

[**ArchivedAnalysis**](ArchivedAnalysis.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAnalysisArchive

> [ArchivedAnalysis] listAnalysisArchive()



### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.ArchivesApi();
apiInstance.listAnalysisArchive((error, data, response) => {
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

[**[ArchivedAnalysis]**](ArchivedAnalysis.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAnalysisArchiveRules

> [AnalysisArchiveTransitionRule] listAnalysisArchiveRules(opts)



### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.ArchivesApi();
let opts = {
  'systemGlobal': true // Boolean | If true include system global rules (owned by admin) even for non-admin users. Defaults to true if not set. Can be set to false to exclude globals
};
apiInstance.listAnalysisArchiveRules(opts, (error, data, response) => {
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
 **systemGlobal** | **Boolean**| If true include system global rules (owned by admin) even for non-admin users. Defaults to true if not set. Can be set to false to exclude globals | [optional] 

### Return type

[**[AnalysisArchiveTransitionRule]**](AnalysisArchiveTransitionRule.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listArchives

> ArchiveSummary listArchives()



### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.ArchivesApi();
apiInstance.listArchives((error, data, response) => {
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

[**ArchiveSummary**](ArchiveSummary.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

