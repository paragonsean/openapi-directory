# MigrationHubStrategyRecommendations.DefaultApi

All URIs are relative to *http://migrationhub-strategy.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getApplicationComponentDetails**](DefaultApi.md#getApplicationComponentDetails) | **GET** /get-applicationcomponent-details/{applicationComponentId} | 
[**getApplicationComponentStrategies**](DefaultApi.md#getApplicationComponentStrategies) | **GET** /get-applicationcomponent-strategies/{applicationComponentId} | 
[**getAssessment**](DefaultApi.md#getAssessment) | **GET** /get-assessment/{id} | 
[**getImportFileTask**](DefaultApi.md#getImportFileTask) | **GET** /get-import-file-task/{id} | 
[**getLatestAssessmentId**](DefaultApi.md#getLatestAssessmentId) | **GET** /get-latest-assessment-id | 
[**getPortfolioPreferences**](DefaultApi.md#getPortfolioPreferences) | **GET** /get-portfolio-preferences | 
[**getPortfolioSummary**](DefaultApi.md#getPortfolioSummary) | **GET** /get-portfolio-summary | 
[**getRecommendationReportDetails**](DefaultApi.md#getRecommendationReportDetails) | **GET** /get-recommendation-report-details/{id} | 
[**getServerDetails**](DefaultApi.md#getServerDetails) | **GET** /get-server-details/{serverId} | 
[**getServerStrategies**](DefaultApi.md#getServerStrategies) | **GET** /get-server-strategies/{serverId} | 
[**listApplicationComponents**](DefaultApi.md#listApplicationComponents) | **POST** /list-applicationcomponents | 
[**listCollectors**](DefaultApi.md#listCollectors) | **GET** /list-collectors | 
[**listImportFileTask**](DefaultApi.md#listImportFileTask) | **GET** /list-import-file-task | 
[**listServers**](DefaultApi.md#listServers) | **POST** /list-servers | 
[**putPortfolioPreferences**](DefaultApi.md#putPortfolioPreferences) | **POST** /put-portfolio-preferences | 
[**startAssessment**](DefaultApi.md#startAssessment) | **POST** /start-assessment | 
[**startImportFileTask**](DefaultApi.md#startImportFileTask) | **POST** /start-import-file-task | 
[**startRecommendationReportGeneration**](DefaultApi.md#startRecommendationReportGeneration) | **POST** /start-recommendation-report-generation | 
[**stopAssessment**](DefaultApi.md#stopAssessment) | **POST** /stop-assessment | 
[**updateApplicationComponentConfig**](DefaultApi.md#updateApplicationComponentConfig) | **POST** /update-applicationcomponent-config/ | 
[**updateServerConfig**](DefaultApi.md#updateServerConfig) | **POST** /update-server-config/ | 



## getApplicationComponentDetails

> GetApplicationComponentDetailsResponse getApplicationComponentDetails(applicationComponentId, opts)



 Retrieves details about an application component. 

### Example

```javascript
import MigrationHubStrategyRecommendations from 'migration_hub_strategy_recommendations';
let defaultClient = MigrationHubStrategyRecommendations.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new MigrationHubStrategyRecommendations.DefaultApi();
let applicationComponentId = "applicationComponentId_example"; // String |  The ID of the application component. The ID is unique within an AWS account.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getApplicationComponentDetails(applicationComponentId, opts, (error, data, response) => {
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
 **applicationComponentId** | **String**|  The ID of the application component. The ID is unique within an AWS account. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetApplicationComponentDetailsResponse**](GetApplicationComponentDetailsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getApplicationComponentStrategies

> GetApplicationComponentStrategiesResponse getApplicationComponentStrategies(applicationComponentId, opts)



 Retrieves a list of all the recommended strategies and tools for an application component running on a server. 

### Example

```javascript
import MigrationHubStrategyRecommendations from 'migration_hub_strategy_recommendations';
let defaultClient = MigrationHubStrategyRecommendations.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new MigrationHubStrategyRecommendations.DefaultApi();
let applicationComponentId = "applicationComponentId_example"; // String |  The ID of the application component. The ID is unique within an AWS account.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getApplicationComponentStrategies(applicationComponentId, opts, (error, data, response) => {
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
 **applicationComponentId** | **String**|  The ID of the application component. The ID is unique within an AWS account. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetApplicationComponentStrategiesResponse**](GetApplicationComponentStrategiesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAssessment

> GetAssessmentResponse getAssessment(id, opts)



 Retrieves the status of an on-going assessment. 

### Example

```javascript
import MigrationHubStrategyRecommendations from 'migration_hub_strategy_recommendations';
let defaultClient = MigrationHubStrategyRecommendations.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new MigrationHubStrategyRecommendations.DefaultApi();
let id = "id_example"; // String |  The <code>assessmentid</code> returned by <a>StartAssessment</a>.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getAssessment(id, opts, (error, data, response) => {
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
 **id** | **String**|  The &lt;code&gt;assessmentid&lt;/code&gt; returned by &lt;a&gt;StartAssessment&lt;/a&gt;. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetAssessmentResponse**](GetAssessmentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getImportFileTask

> GetImportFileTaskResponse getImportFileTask(id, opts)



 Retrieves the details about a specific import task. 

### Example

```javascript
import MigrationHubStrategyRecommendations from 'migration_hub_strategy_recommendations';
let defaultClient = MigrationHubStrategyRecommendations.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new MigrationHubStrategyRecommendations.DefaultApi();
let id = "id_example"; // String |  The ID of the import file task. This ID is returned in the response of <a>StartImportFileTask</a>. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getImportFileTask(id, opts, (error, data, response) => {
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
 **id** | **String**|  The ID of the import file task. This ID is returned in the response of &lt;a&gt;StartImportFileTask&lt;/a&gt;.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetImportFileTaskResponse**](GetImportFileTaskResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLatestAssessmentId

> GetLatestAssessmentIdResponse getLatestAssessmentId(opts)



Retrieve the latest ID of a specific assessment task.

### Example

```javascript
import MigrationHubStrategyRecommendations from 'migration_hub_strategy_recommendations';
let defaultClient = MigrationHubStrategyRecommendations.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new MigrationHubStrategyRecommendations.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getLatestAssessmentId(opts, (error, data, response) => {
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
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetLatestAssessmentIdResponse**](GetLatestAssessmentIdResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPortfolioPreferences

> GetPortfolioPreferencesResponse getPortfolioPreferences(opts)



 Retrieves your migration and modernization preferences. 

### Example

```javascript
import MigrationHubStrategyRecommendations from 'migration_hub_strategy_recommendations';
let defaultClient = MigrationHubStrategyRecommendations.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new MigrationHubStrategyRecommendations.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getPortfolioPreferences(opts, (error, data, response) => {
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
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetPortfolioPreferencesResponse**](GetPortfolioPreferencesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPortfolioSummary

> GetPortfolioSummaryResponse getPortfolioSummary(opts)



 Retrieves overall summary including the number of servers to rehost and the overall number of anti-patterns. 

### Example

```javascript
import MigrationHubStrategyRecommendations from 'migration_hub_strategy_recommendations';
let defaultClient = MigrationHubStrategyRecommendations.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new MigrationHubStrategyRecommendations.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getPortfolioSummary(opts, (error, data, response) => {
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
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetPortfolioSummaryResponse**](GetPortfolioSummaryResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRecommendationReportDetails

> GetRecommendationReportDetailsResponse getRecommendationReportDetails(id, opts)



 Retrieves detailed information about the specified recommendation report. 

### Example

```javascript
import MigrationHubStrategyRecommendations from 'migration_hub_strategy_recommendations';
let defaultClient = MigrationHubStrategyRecommendations.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new MigrationHubStrategyRecommendations.DefaultApi();
let id = "id_example"; // String |  The recommendation report generation task <code>id</code> returned by <a>StartRecommendationReportGeneration</a>. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getRecommendationReportDetails(id, opts, (error, data, response) => {
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
 **id** | **String**|  The recommendation report generation task &lt;code&gt;id&lt;/code&gt; returned by &lt;a&gt;StartRecommendationReportGeneration&lt;/a&gt;.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetRecommendationReportDetailsResponse**](GetRecommendationReportDetailsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getServerDetails

> GetServerDetailsResponse getServerDetails(serverId, opts)



 Retrieves detailed information about a specified server. 

### Example

```javascript
import MigrationHubStrategyRecommendations from 'migration_hub_strategy_recommendations';
let defaultClient = MigrationHubStrategyRecommendations.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new MigrationHubStrategyRecommendations.DefaultApi();
let serverId = "serverId_example"; // String |  The ID of the server. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number |  The maximum number of items to include in the response. The maximum value is 100. 
  'nextToken': "nextToken_example" // String |  The token from a previous call that you use to retrieve the next set of results. For example, if a previous call to this action returned 100 items, but you set <code>maxResults</code> to 10. You'll receive a set of 10 results along with a token. You then use the returned token to retrieve the next set of 10. 
};
apiInstance.getServerDetails(serverId, opts, (error, data, response) => {
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
 **serverId** | **String**|  The ID of the server.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**|  The maximum number of items to include in the response. The maximum value is 100.  | [optional] 
 **nextToken** | **String**|  The token from a previous call that you use to retrieve the next set of results. For example, if a previous call to this action returned 100 items, but you set &lt;code&gt;maxResults&lt;/code&gt; to 10. You&#39;ll receive a set of 10 results along with a token. You then use the returned token to retrieve the next set of 10.  | [optional] 

### Return type

[**GetServerDetailsResponse**](GetServerDetailsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getServerStrategies

> GetServerStrategiesResponse getServerStrategies(serverId, opts)



 Retrieves recommended strategies and tools for the specified server. 

### Example

```javascript
import MigrationHubStrategyRecommendations from 'migration_hub_strategy_recommendations';
let defaultClient = MigrationHubStrategyRecommendations.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new MigrationHubStrategyRecommendations.DefaultApi();
let serverId = "serverId_example"; // String |  The ID of the server. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getServerStrategies(serverId, opts, (error, data, response) => {
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
 **serverId** | **String**|  The ID of the server.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetServerStrategiesResponse**](GetServerStrategiesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listApplicationComponents

> ListApplicationComponentsResponse listApplicationComponents(listApplicationComponentsRequest, opts)



 Retrieves a list of all the application components (processes). 

### Example

```javascript
import MigrationHubStrategyRecommendations from 'migration_hub_strategy_recommendations';
let defaultClient = MigrationHubStrategyRecommendations.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new MigrationHubStrategyRecommendations.DefaultApi();
let listApplicationComponentsRequest = new MigrationHubStrategyRecommendations.ListApplicationComponentsRequest(); // ListApplicationComponentsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listApplicationComponents(listApplicationComponentsRequest, opts, (error, data, response) => {
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
 **listApplicationComponentsRequest** | [**ListApplicationComponentsRequest**](ListApplicationComponentsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListApplicationComponentsResponse**](ListApplicationComponentsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listCollectors

> ListCollectorsResponse listCollectors(opts)



 Retrieves a list of all the installed collectors. 

### Example

```javascript
import MigrationHubStrategyRecommendations from 'migration_hub_strategy_recommendations';
let defaultClient = MigrationHubStrategyRecommendations.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new MigrationHubStrategyRecommendations.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number |  The maximum number of items to include in the response. The maximum value is 100. 
  'nextToken': "nextToken_example" // String |  The token from a previous call that you use to retrieve the next set of results. For example, if a previous call to this action returned 100 items, but you set <code>maxResults</code> to 10. You'll receive a set of 10 results along with a token. You then use the returned token to retrieve the next set of 10. 
};
apiInstance.listCollectors(opts, (error, data, response) => {
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
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**|  The maximum number of items to include in the response. The maximum value is 100.  | [optional] 
 **nextToken** | **String**|  The token from a previous call that you use to retrieve the next set of results. For example, if a previous call to this action returned 100 items, but you set &lt;code&gt;maxResults&lt;/code&gt; to 10. You&#39;ll receive a set of 10 results along with a token. You then use the returned token to retrieve the next set of 10.  | [optional] 

### Return type

[**ListCollectorsResponse**](ListCollectorsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listImportFileTask

> ListImportFileTaskResponse listImportFileTask(opts)



 Retrieves a list of all the imports performed. 

### Example

```javascript
import MigrationHubStrategyRecommendations from 'migration_hub_strategy_recommendations';
let defaultClient = MigrationHubStrategyRecommendations.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new MigrationHubStrategyRecommendations.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number |  The total number of items to return. The maximum value is 100. 
  'nextToken': "nextToken_example" // String |  The token from a previous call that you use to retrieve the next set of results. For example, if a previous call to this action returned 100 items, but you set <code>maxResults</code> to 10. You'll receive a set of 10 results along with a token. You then use the returned token to retrieve the next set of 10. 
};
apiInstance.listImportFileTask(opts, (error, data, response) => {
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
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**|  The total number of items to return. The maximum value is 100.  | [optional] 
 **nextToken** | **String**|  The token from a previous call that you use to retrieve the next set of results. For example, if a previous call to this action returned 100 items, but you set &lt;code&gt;maxResults&lt;/code&gt; to 10. You&#39;ll receive a set of 10 results along with a token. You then use the returned token to retrieve the next set of 10.  | [optional] 

### Return type

[**ListImportFileTaskResponse**](ListImportFileTaskResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listServers

> ListServersResponse listServers(listServersRequest, opts)



 Returns a list of all the servers. 

### Example

```javascript
import MigrationHubStrategyRecommendations from 'migration_hub_strategy_recommendations';
let defaultClient = MigrationHubStrategyRecommendations.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new MigrationHubStrategyRecommendations.DefaultApi();
let listServersRequest = new MigrationHubStrategyRecommendations.ListServersRequest(); // ListServersRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listServers(listServersRequest, opts, (error, data, response) => {
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
 **listServersRequest** | [**ListServersRequest**](ListServersRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListServersResponse**](ListServersResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putPortfolioPreferences

> Object putPortfolioPreferences(putPortfolioPreferencesRequest, opts)



 Saves the specified migration and modernization preferences. 

### Example

```javascript
import MigrationHubStrategyRecommendations from 'migration_hub_strategy_recommendations';
let defaultClient = MigrationHubStrategyRecommendations.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new MigrationHubStrategyRecommendations.DefaultApi();
let putPortfolioPreferencesRequest = new MigrationHubStrategyRecommendations.PutPortfolioPreferencesRequest(); // PutPortfolioPreferencesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putPortfolioPreferences(putPortfolioPreferencesRequest, opts, (error, data, response) => {
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
 **putPortfolioPreferencesRequest** | [**PutPortfolioPreferencesRequest**](PutPortfolioPreferencesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startAssessment

> StartAssessmentResponse startAssessment(startAssessmentRequest, opts)



 Starts the assessment of an on-premises environment. 

### Example

```javascript
import MigrationHubStrategyRecommendations from 'migration_hub_strategy_recommendations';
let defaultClient = MigrationHubStrategyRecommendations.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new MigrationHubStrategyRecommendations.DefaultApi();
let startAssessmentRequest = new MigrationHubStrategyRecommendations.StartAssessmentRequest(); // StartAssessmentRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startAssessment(startAssessmentRequest, opts, (error, data, response) => {
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
 **startAssessmentRequest** | [**StartAssessmentRequest**](StartAssessmentRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartAssessmentResponse**](StartAssessmentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startImportFileTask

> StartImportFileTaskResponse startImportFileTask(startImportFileTaskRequest, opts)



 Starts a file import. 

### Example

```javascript
import MigrationHubStrategyRecommendations from 'migration_hub_strategy_recommendations';
let defaultClient = MigrationHubStrategyRecommendations.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new MigrationHubStrategyRecommendations.DefaultApi();
let startImportFileTaskRequest = new MigrationHubStrategyRecommendations.StartImportFileTaskRequest(); // StartImportFileTaskRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startImportFileTask(startImportFileTaskRequest, opts, (error, data, response) => {
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
 **startImportFileTaskRequest** | [**StartImportFileTaskRequest**](StartImportFileTaskRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartImportFileTaskResponse**](StartImportFileTaskResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startRecommendationReportGeneration

> StartRecommendationReportGenerationResponse startRecommendationReportGeneration(startRecommendationReportGenerationRequest, opts)



 Starts generating a recommendation report. 

### Example

```javascript
import MigrationHubStrategyRecommendations from 'migration_hub_strategy_recommendations';
let defaultClient = MigrationHubStrategyRecommendations.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new MigrationHubStrategyRecommendations.DefaultApi();
let startRecommendationReportGenerationRequest = new MigrationHubStrategyRecommendations.StartRecommendationReportGenerationRequest(); // StartRecommendationReportGenerationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startRecommendationReportGeneration(startRecommendationReportGenerationRequest, opts, (error, data, response) => {
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
 **startRecommendationReportGenerationRequest** | [**StartRecommendationReportGenerationRequest**](StartRecommendationReportGenerationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartRecommendationReportGenerationResponse**](StartRecommendationReportGenerationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## stopAssessment

> Object stopAssessment(stopAssessmentRequest, opts)



 Stops the assessment of an on-premises environment. 

### Example

```javascript
import MigrationHubStrategyRecommendations from 'migration_hub_strategy_recommendations';
let defaultClient = MigrationHubStrategyRecommendations.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new MigrationHubStrategyRecommendations.DefaultApi();
let stopAssessmentRequest = new MigrationHubStrategyRecommendations.StopAssessmentRequest(); // StopAssessmentRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.stopAssessment(stopAssessmentRequest, opts, (error, data, response) => {
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
 **stopAssessmentRequest** | [**StopAssessmentRequest**](StopAssessmentRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateApplicationComponentConfig

> Object updateApplicationComponentConfig(updateApplicationComponentConfigRequest, opts)



 Updates the configuration of an application component. 

### Example

```javascript
import MigrationHubStrategyRecommendations from 'migration_hub_strategy_recommendations';
let defaultClient = MigrationHubStrategyRecommendations.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new MigrationHubStrategyRecommendations.DefaultApi();
let updateApplicationComponentConfigRequest = new MigrationHubStrategyRecommendations.UpdateApplicationComponentConfigRequest(); // UpdateApplicationComponentConfigRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateApplicationComponentConfig(updateApplicationComponentConfigRequest, opts, (error, data, response) => {
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
 **updateApplicationComponentConfigRequest** | [**UpdateApplicationComponentConfigRequest**](UpdateApplicationComponentConfigRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateServerConfig

> Object updateServerConfig(updateServerConfigRequest, opts)



 Updates the configuration of the specified server. 

### Example

```javascript
import MigrationHubStrategyRecommendations from 'migration_hub_strategy_recommendations';
let defaultClient = MigrationHubStrategyRecommendations.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new MigrationHubStrategyRecommendations.DefaultApi();
let updateServerConfigRequest = new MigrationHubStrategyRecommendations.UpdateServerConfigRequest(); // UpdateServerConfigRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateServerConfig(updateServerConfigRequest, opts, (error, data, response) => {
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
 **updateServerConfigRequest** | [**UpdateServerConfigRequest**](UpdateServerConfigRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

