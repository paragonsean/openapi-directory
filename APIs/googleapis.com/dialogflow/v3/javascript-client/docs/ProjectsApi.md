# DialogflowApi.ProjectsApi

All URIs are relative to *https://dialogflow.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dialogflowProjectsLocationsAgentsChangelogsList**](ProjectsApi.md#dialogflowProjectsLocationsAgentsChangelogsList) | **GET** /v3/{parent}/changelogs | 
[**dialogflowProjectsLocationsAgentsCreate**](ProjectsApi.md#dialogflowProjectsLocationsAgentsCreate) | **POST** /v3/{parent}/agents | 
[**dialogflowProjectsLocationsAgentsEntityTypesExport**](ProjectsApi.md#dialogflowProjectsLocationsAgentsEntityTypesExport) | **POST** /v3/{parent}/entityTypes:export | 
[**dialogflowProjectsLocationsAgentsEntityTypesImport**](ProjectsApi.md#dialogflowProjectsLocationsAgentsEntityTypesImport) | **POST** /v3/{parent}/entityTypes:import | 
[**dialogflowProjectsLocationsAgentsEnvironmentsContinuousTestResultsList**](ProjectsApi.md#dialogflowProjectsLocationsAgentsEnvironmentsContinuousTestResultsList) | **GET** /v3/{parent}/continuousTestResults | 
[**dialogflowProjectsLocationsAgentsEnvironmentsCreate**](ProjectsApi.md#dialogflowProjectsLocationsAgentsEnvironmentsCreate) | **POST** /v3/{parent}/environments | 
[**dialogflowProjectsLocationsAgentsEnvironmentsDeployFlow**](ProjectsApi.md#dialogflowProjectsLocationsAgentsEnvironmentsDeployFlow) | **POST** /v3/{environment}:deployFlow | 
[**dialogflowProjectsLocationsAgentsEnvironmentsDeploymentsList**](ProjectsApi.md#dialogflowProjectsLocationsAgentsEnvironmentsDeploymentsList) | **GET** /v3/{parent}/deployments | 
[**dialogflowProjectsLocationsAgentsEnvironmentsExperimentsCreate**](ProjectsApi.md#dialogflowProjectsLocationsAgentsEnvironmentsExperimentsCreate) | **POST** /v3/{parent}/experiments | 
[**dialogflowProjectsLocationsAgentsEnvironmentsExperimentsList**](ProjectsApi.md#dialogflowProjectsLocationsAgentsEnvironmentsExperimentsList) | **GET** /v3/{parent}/experiments | 
[**dialogflowProjectsLocationsAgentsEnvironmentsExperimentsStart**](ProjectsApi.md#dialogflowProjectsLocationsAgentsEnvironmentsExperimentsStart) | **POST** /v3/{name}:start | 
[**dialogflowProjectsLocationsAgentsEnvironmentsExperimentsStop**](ProjectsApi.md#dialogflowProjectsLocationsAgentsEnvironmentsExperimentsStop) | **POST** /v3/{name}:stop | 
[**dialogflowProjectsLocationsAgentsEnvironmentsList**](ProjectsApi.md#dialogflowProjectsLocationsAgentsEnvironmentsList) | **GET** /v3/{parent}/environments | 
[**dialogflowProjectsLocationsAgentsEnvironmentsLookupEnvironmentHistory**](ProjectsApi.md#dialogflowProjectsLocationsAgentsEnvironmentsLookupEnvironmentHistory) | **GET** /v3/{name}:lookupEnvironmentHistory | 
[**dialogflowProjectsLocationsAgentsEnvironmentsRunContinuousTest**](ProjectsApi.md#dialogflowProjectsLocationsAgentsEnvironmentsRunContinuousTest) | **POST** /v3/{environment}:runContinuousTest | 
[**dialogflowProjectsLocationsAgentsFlowsCreate**](ProjectsApi.md#dialogflowProjectsLocationsAgentsFlowsCreate) | **POST** /v3/{parent}/flows | 
[**dialogflowProjectsLocationsAgentsFlowsExport**](ProjectsApi.md#dialogflowProjectsLocationsAgentsFlowsExport) | **POST** /v3/{name}:export | 
[**dialogflowProjectsLocationsAgentsFlowsImport**](ProjectsApi.md#dialogflowProjectsLocationsAgentsFlowsImport) | **POST** /v3/{parent}/flows:import | 
[**dialogflowProjectsLocationsAgentsFlowsList**](ProjectsApi.md#dialogflowProjectsLocationsAgentsFlowsList) | **GET** /v3/{parent}/flows | 
[**dialogflowProjectsLocationsAgentsFlowsPagesCreate**](ProjectsApi.md#dialogflowProjectsLocationsAgentsFlowsPagesCreate) | **POST** /v3/{parent}/pages | 
[**dialogflowProjectsLocationsAgentsFlowsPagesList**](ProjectsApi.md#dialogflowProjectsLocationsAgentsFlowsPagesList) | **GET** /v3/{parent}/pages | 
[**dialogflowProjectsLocationsAgentsFlowsTrain**](ProjectsApi.md#dialogflowProjectsLocationsAgentsFlowsTrain) | **POST** /v3/{name}:train | 
[**dialogflowProjectsLocationsAgentsFlowsValidate**](ProjectsApi.md#dialogflowProjectsLocationsAgentsFlowsValidate) | **POST** /v3/{name}:validate | 
[**dialogflowProjectsLocationsAgentsFlowsVersionsCompareVersions**](ProjectsApi.md#dialogflowProjectsLocationsAgentsFlowsVersionsCompareVersions) | **POST** /v3/{baseVersion}:compareVersions | 
[**dialogflowProjectsLocationsAgentsFlowsVersionsCreate**](ProjectsApi.md#dialogflowProjectsLocationsAgentsFlowsVersionsCreate) | **POST** /v3/{parent}/versions | 
[**dialogflowProjectsLocationsAgentsFlowsVersionsList**](ProjectsApi.md#dialogflowProjectsLocationsAgentsFlowsVersionsList) | **GET** /v3/{parent}/versions | 
[**dialogflowProjectsLocationsAgentsFlowsVersionsLoad**](ProjectsApi.md#dialogflowProjectsLocationsAgentsFlowsVersionsLoad) | **POST** /v3/{name}:load | 
[**dialogflowProjectsLocationsAgentsGeneratorsCreate**](ProjectsApi.md#dialogflowProjectsLocationsAgentsGeneratorsCreate) | **POST** /v3/{parent}/generators | 
[**dialogflowProjectsLocationsAgentsGeneratorsList**](ProjectsApi.md#dialogflowProjectsLocationsAgentsGeneratorsList) | **GET** /v3/{parent}/generators | 
[**dialogflowProjectsLocationsAgentsIntentsCreate**](ProjectsApi.md#dialogflowProjectsLocationsAgentsIntentsCreate) | **POST** /v3/{parent}/intents | 
[**dialogflowProjectsLocationsAgentsIntentsExport**](ProjectsApi.md#dialogflowProjectsLocationsAgentsIntentsExport) | **POST** /v3/{parent}/intents:export | 
[**dialogflowProjectsLocationsAgentsIntentsImport**](ProjectsApi.md#dialogflowProjectsLocationsAgentsIntentsImport) | **POST** /v3/{parent}/intents:import | 
[**dialogflowProjectsLocationsAgentsIntentsList**](ProjectsApi.md#dialogflowProjectsLocationsAgentsIntentsList) | **GET** /v3/{parent}/intents | 
[**dialogflowProjectsLocationsAgentsList**](ProjectsApi.md#dialogflowProjectsLocationsAgentsList) | **GET** /v3/{parent}/agents | 
[**dialogflowProjectsLocationsAgentsRestore**](ProjectsApi.md#dialogflowProjectsLocationsAgentsRestore) | **POST** /v3/{name}:restore | 
[**dialogflowProjectsLocationsAgentsSessionsDetectIntent**](ProjectsApi.md#dialogflowProjectsLocationsAgentsSessionsDetectIntent) | **POST** /v3/{session}:detectIntent | 
[**dialogflowProjectsLocationsAgentsSessionsEntityTypesCreate**](ProjectsApi.md#dialogflowProjectsLocationsAgentsSessionsEntityTypesCreate) | **POST** /v3/{parent}/entityTypes | 
[**dialogflowProjectsLocationsAgentsSessionsEntityTypesList**](ProjectsApi.md#dialogflowProjectsLocationsAgentsSessionsEntityTypesList) | **GET** /v3/{parent}/entityTypes | 
[**dialogflowProjectsLocationsAgentsSessionsFulfillIntent**](ProjectsApi.md#dialogflowProjectsLocationsAgentsSessionsFulfillIntent) | **POST** /v3/{session}:fulfillIntent | 
[**dialogflowProjectsLocationsAgentsSessionsMatchIntent**](ProjectsApi.md#dialogflowProjectsLocationsAgentsSessionsMatchIntent) | **POST** /v3/{session}:matchIntent | 
[**dialogflowProjectsLocationsAgentsSessionsServerStreamingDetectIntent**](ProjectsApi.md#dialogflowProjectsLocationsAgentsSessionsServerStreamingDetectIntent) | **POST** /v3/{session}:serverStreamingDetectIntent | 
[**dialogflowProjectsLocationsAgentsSessionsSubmitAnswerFeedback**](ProjectsApi.md#dialogflowProjectsLocationsAgentsSessionsSubmitAnswerFeedback) | **POST** /v3/{session}:submitAnswerFeedback | 
[**dialogflowProjectsLocationsAgentsTestCasesBatchDelete**](ProjectsApi.md#dialogflowProjectsLocationsAgentsTestCasesBatchDelete) | **POST** /v3/{parent}/testCases:batchDelete | 
[**dialogflowProjectsLocationsAgentsTestCasesBatchRun**](ProjectsApi.md#dialogflowProjectsLocationsAgentsTestCasesBatchRun) | **POST** /v3/{parent}/testCases:batchRun | 
[**dialogflowProjectsLocationsAgentsTestCasesCalculateCoverage**](ProjectsApi.md#dialogflowProjectsLocationsAgentsTestCasesCalculateCoverage) | **GET** /v3/{agent}/testCases:calculateCoverage | 
[**dialogflowProjectsLocationsAgentsTestCasesCreate**](ProjectsApi.md#dialogflowProjectsLocationsAgentsTestCasesCreate) | **POST** /v3/{parent}/testCases | 
[**dialogflowProjectsLocationsAgentsTestCasesExport**](ProjectsApi.md#dialogflowProjectsLocationsAgentsTestCasesExport) | **POST** /v3/{parent}/testCases:export | 
[**dialogflowProjectsLocationsAgentsTestCasesImport**](ProjectsApi.md#dialogflowProjectsLocationsAgentsTestCasesImport) | **POST** /v3/{parent}/testCases:import | 
[**dialogflowProjectsLocationsAgentsTestCasesList**](ProjectsApi.md#dialogflowProjectsLocationsAgentsTestCasesList) | **GET** /v3/{parent}/testCases | 
[**dialogflowProjectsLocationsAgentsTestCasesResultsList**](ProjectsApi.md#dialogflowProjectsLocationsAgentsTestCasesResultsList) | **GET** /v3/{parent}/results | 
[**dialogflowProjectsLocationsAgentsTestCasesRun**](ProjectsApi.md#dialogflowProjectsLocationsAgentsTestCasesRun) | **POST** /v3/{name}:run | 
[**dialogflowProjectsLocationsAgentsTransitionRouteGroupsCreate**](ProjectsApi.md#dialogflowProjectsLocationsAgentsTransitionRouteGroupsCreate) | **POST** /v3/{parent}/transitionRouteGroups | 
[**dialogflowProjectsLocationsAgentsTransitionRouteGroupsList**](ProjectsApi.md#dialogflowProjectsLocationsAgentsTransitionRouteGroupsList) | **GET** /v3/{parent}/transitionRouteGroups | 
[**dialogflowProjectsLocationsAgentsWebhooksCreate**](ProjectsApi.md#dialogflowProjectsLocationsAgentsWebhooksCreate) | **POST** /v3/{parent}/webhooks | 
[**dialogflowProjectsLocationsAgentsWebhooksList**](ProjectsApi.md#dialogflowProjectsLocationsAgentsWebhooksList) | **GET** /v3/{parent}/webhooks | 
[**dialogflowProjectsLocationsList**](ProjectsApi.md#dialogflowProjectsLocationsList) | **GET** /v3/{name}/locations | 
[**dialogflowProjectsLocationsSecuritySettingsCreate**](ProjectsApi.md#dialogflowProjectsLocationsSecuritySettingsCreate) | **POST** /v3/{parent}/securitySettings | 
[**dialogflowProjectsLocationsSecuritySettingsDelete**](ProjectsApi.md#dialogflowProjectsLocationsSecuritySettingsDelete) | **DELETE** /v3/{name} | 
[**dialogflowProjectsLocationsSecuritySettingsList**](ProjectsApi.md#dialogflowProjectsLocationsSecuritySettingsList) | **GET** /v3/{parent}/securitySettings | 
[**dialogflowProjectsLocationsSecuritySettingsPatch**](ProjectsApi.md#dialogflowProjectsLocationsSecuritySettingsPatch) | **PATCH** /v3/{name} | 
[**dialogflowProjectsOperationsCancel**](ProjectsApi.md#dialogflowProjectsOperationsCancel) | **POST** /v3/{name}:cancel | 
[**dialogflowProjectsOperationsGet**](ProjectsApi.md#dialogflowProjectsOperationsGet) | **GET** /v3/{name} | 
[**dialogflowProjectsOperationsList**](ProjectsApi.md#dialogflowProjectsOperationsList) | **GET** /v3/{name}/operations | 



## dialogflowProjectsLocationsAgentsChangelogsList

> GoogleCloudDialogflowCxV3ListChangelogsResponse dialogflowProjectsLocationsAgentsChangelogsList(parent, opts)



Returns the list of Changelogs.

### Example

```javascript
import DialogflowApi from 'dialogflow_api';
let defaultClient = DialogflowApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DialogflowApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The agent containing the changelogs. Format: `projects//locations//agents/`.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | The filter string. Supports filter by user_email, resource, type and create_time. Some examples: 1. By user email: user_email = \"someone@google.com\" 2. By resource name: resource = \"projects/123/locations/global/agents/456/flows/789\" 3. By resource display name: display_name = \"my agent\" 4. By action: action = \"Create\" 5. By type: type = \"flows\" 6. By create time. Currently predicates on `create_time` and `create_time_epoch_seconds` are supported: create_time_epoch_seconds > 1551790877 AND create_time <= 2017-01-15T01:30:15.01Z 7. Combination of above filters: resource = \"projects/123/locations/global/agents/456/flows/789\" AND user_email = \"someone@google.com\" AND create_time <= 2017-01-15T01:30:15.01Z
  'pageSize': 56, // Number | The maximum number of items to return in a single page. By default 100 and at most 1000.
  'pageToken': "pageToken_example" // String | The next_page_token value returned from a previous list request.
};
apiInstance.dialogflowProjectsLocationsAgentsChangelogsList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The agent containing the changelogs. Format: &#x60;projects//locations//agents/&#x60;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| The filter string. Supports filter by user_email, resource, type and create_time. Some examples: 1. By user email: user_email &#x3D; \&quot;someone@google.com\&quot; 2. By resource name: resource &#x3D; \&quot;projects/123/locations/global/agents/456/flows/789\&quot; 3. By resource display name: display_name &#x3D; \&quot;my agent\&quot; 4. By action: action &#x3D; \&quot;Create\&quot; 5. By type: type &#x3D; \&quot;flows\&quot; 6. By create time. Currently predicates on &#x60;create_time&#x60; and &#x60;create_time_epoch_seconds&#x60; are supported: create_time_epoch_seconds &gt; 1551790877 AND create_time &lt;&#x3D; 2017-01-15T01:30:15.01Z 7. Combination of above filters: resource &#x3D; \&quot;projects/123/locations/global/agents/456/flows/789\&quot; AND user_email &#x3D; \&quot;someone@google.com\&quot; AND create_time &lt;&#x3D; 2017-01-15T01:30:15.01Z | [optional] 
 **pageSize** | **Number**| The maximum number of items to return in a single page. By default 100 and at most 1000. | [optional] 
 **pageToken** | **String**| The next_page_token value returned from a previous list request. | [optional] 

### Return type

[**GoogleCloudDialogflowCxV3ListChangelogsResponse**](GoogleCloudDialogflowCxV3ListChangelogsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dialogflowProjectsLocationsAgentsCreate

> GoogleCloudDialogflowCxV3Agent dialogflowProjectsLocationsAgentsCreate(parent, opts)



Creates an agent in the specified location. Note: You should always train flows prior to sending them queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

### Example

```javascript
import DialogflowApi from 'dialogflow_api';
let defaultClient = DialogflowApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DialogflowApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The location to create a agent for. Format: `projects//locations/`.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudDialogflowCxV3Agent': new DialogflowApi.GoogleCloudDialogflowCxV3Agent() // GoogleCloudDialogflowCxV3Agent | 
};
apiInstance.dialogflowProjectsLocationsAgentsCreate(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The location to create a agent for. Format: &#x60;projects//locations/&#x60;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudDialogflowCxV3Agent** | [**GoogleCloudDialogflowCxV3Agent**](GoogleCloudDialogflowCxV3Agent.md)|  | [optional] 

### Return type

[**GoogleCloudDialogflowCxV3Agent**](GoogleCloudDialogflowCxV3Agent.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dialogflowProjectsLocationsAgentsEntityTypesExport

> GoogleLongrunningOperation dialogflowProjectsLocationsAgentsEntityTypesExport(parent, opts)



Exports the selected entity types.

### Example

```javascript
import DialogflowApi from 'dialogflow_api';
let defaultClient = DialogflowApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DialogflowApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The name of the parent agent to export entity types. Format: `projects//locations//agents/`.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudDialogflowCxV3ExportEntityTypesRequest': new DialogflowApi.GoogleCloudDialogflowCxV3ExportEntityTypesRequest() // GoogleCloudDialogflowCxV3ExportEntityTypesRequest | 
};
apiInstance.dialogflowProjectsLocationsAgentsEntityTypesExport(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The name of the parent agent to export entity types. Format: &#x60;projects//locations//agents/&#x60;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudDialogflowCxV3ExportEntityTypesRequest** | [**GoogleCloudDialogflowCxV3ExportEntityTypesRequest**](GoogleCloudDialogflowCxV3ExportEntityTypesRequest.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dialogflowProjectsLocationsAgentsEntityTypesImport

> GoogleLongrunningOperation dialogflowProjectsLocationsAgentsEntityTypesImport(parent, opts)



Imports the specified entitytypes into the agent.

### Example

```javascript
import DialogflowApi from 'dialogflow_api';
let defaultClient = DialogflowApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DialogflowApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The agent to import the entity types into. Format: `projects//locations//agents/`.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudDialogflowCxV3ImportEntityTypesRequest': new DialogflowApi.GoogleCloudDialogflowCxV3ImportEntityTypesRequest() // GoogleCloudDialogflowCxV3ImportEntityTypesRequest | 
};
apiInstance.dialogflowProjectsLocationsAgentsEntityTypesImport(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The agent to import the entity types into. Format: &#x60;projects//locations//agents/&#x60;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudDialogflowCxV3ImportEntityTypesRequest** | [**GoogleCloudDialogflowCxV3ImportEntityTypesRequest**](GoogleCloudDialogflowCxV3ImportEntityTypesRequest.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dialogflowProjectsLocationsAgentsEnvironmentsContinuousTestResultsList

> GoogleCloudDialogflowCxV3ListContinuousTestResultsResponse dialogflowProjectsLocationsAgentsEnvironmentsContinuousTestResultsList(parent, opts)



Fetches a list of continuous test results for a given environment.

### Example

```javascript
import DialogflowApi from 'dialogflow_api';
let defaultClient = DialogflowApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DialogflowApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The environment to list results for. Format: `projects//locations//agents// environments/`.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'pageSize': 56, // Number | The maximum number of items to return in a single page. By default 100 and at most 1000.
  'pageToken': "pageToken_example" // String | The next_page_token value returned from a previous list request.
};
apiInstance.dialogflowProjectsLocationsAgentsEnvironmentsContinuousTestResultsList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The environment to list results for. Format: &#x60;projects//locations//agents// environments/&#x60;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **pageSize** | **Number**| The maximum number of items to return in a single page. By default 100 and at most 1000. | [optional] 
 **pageToken** | **String**| The next_page_token value returned from a previous list request. | [optional] 

### Return type

[**GoogleCloudDialogflowCxV3ListContinuousTestResultsResponse**](GoogleCloudDialogflowCxV3ListContinuousTestResultsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dialogflowProjectsLocationsAgentsEnvironmentsCreate

> GoogleLongrunningOperation dialogflowProjectsLocationsAgentsEnvironmentsCreate(parent, opts)



Creates an Environment in the specified Agent. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned &#x60;Operation&#x60; type has the following method-specific fields: - &#x60;metadata&#x60;: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct) - &#x60;response&#x60;: Environment

### Example

```javascript
import DialogflowApi from 'dialogflow_api';
let defaultClient = DialogflowApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DialogflowApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The Agent to create an Environment for. Format: `projects//locations//agents/`.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudDialogflowCxV3Environment': new DialogflowApi.GoogleCloudDialogflowCxV3Environment() // GoogleCloudDialogflowCxV3Environment | 
};
apiInstance.dialogflowProjectsLocationsAgentsEnvironmentsCreate(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The Agent to create an Environment for. Format: &#x60;projects//locations//agents/&#x60;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudDialogflowCxV3Environment** | [**GoogleCloudDialogflowCxV3Environment**](GoogleCloudDialogflowCxV3Environment.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dialogflowProjectsLocationsAgentsEnvironmentsDeployFlow

> GoogleLongrunningOperation dialogflowProjectsLocationsAgentsEnvironmentsDeployFlow(environment, opts)



Deploys a flow to the specified Environment. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned &#x60;Operation&#x60; type has the following method-specific fields: - &#x60;metadata&#x60;: DeployFlowMetadata - &#x60;response&#x60;: DeployFlowResponse

### Example

```javascript
import DialogflowApi from 'dialogflow_api';
let defaultClient = DialogflowApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DialogflowApi.ProjectsApi();
let environment = "environment_example"; // String | Required. The environment to deploy the flow to. Format: `projects//locations//agents// environments/`.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudDialogflowCxV3DeployFlowRequest': new DialogflowApi.GoogleCloudDialogflowCxV3DeployFlowRequest() // GoogleCloudDialogflowCxV3DeployFlowRequest | 
};
apiInstance.dialogflowProjectsLocationsAgentsEnvironmentsDeployFlow(environment, opts, (error, data, response) => {
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
 **environment** | **String**| Required. The environment to deploy the flow to. Format: &#x60;projects//locations//agents// environments/&#x60;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudDialogflowCxV3DeployFlowRequest** | [**GoogleCloudDialogflowCxV3DeployFlowRequest**](GoogleCloudDialogflowCxV3DeployFlowRequest.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dialogflowProjectsLocationsAgentsEnvironmentsDeploymentsList

> GoogleCloudDialogflowCxV3ListDeploymentsResponse dialogflowProjectsLocationsAgentsEnvironmentsDeploymentsList(parent, opts)



Returns the list of all deployments in the specified Environment.

### Example

```javascript
import DialogflowApi from 'dialogflow_api';
let defaultClient = DialogflowApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DialogflowApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The Environment to list all environments for. Format: `projects//locations//agents//environments/`.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'pageSize': 56, // Number | The maximum number of items to return in a single page. By default 20 and at most 100.
  'pageToken': "pageToken_example" // String | The next_page_token value returned from a previous list request.
};
apiInstance.dialogflowProjectsLocationsAgentsEnvironmentsDeploymentsList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The Environment to list all environments for. Format: &#x60;projects//locations//agents//environments/&#x60;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **pageSize** | **Number**| The maximum number of items to return in a single page. By default 20 and at most 100. | [optional] 
 **pageToken** | **String**| The next_page_token value returned from a previous list request. | [optional] 

### Return type

[**GoogleCloudDialogflowCxV3ListDeploymentsResponse**](GoogleCloudDialogflowCxV3ListDeploymentsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dialogflowProjectsLocationsAgentsEnvironmentsExperimentsCreate

> GoogleCloudDialogflowCxV3Experiment dialogflowProjectsLocationsAgentsEnvironmentsExperimentsCreate(parent, opts)



Creates an Experiment in the specified Environment.

### Example

```javascript
import DialogflowApi from 'dialogflow_api';
let defaultClient = DialogflowApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DialogflowApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The Agent to create an Environment for. Format: `projects//locations//agents//environments/`.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudDialogflowCxV3Experiment': new DialogflowApi.GoogleCloudDialogflowCxV3Experiment() // GoogleCloudDialogflowCxV3Experiment | 
};
apiInstance.dialogflowProjectsLocationsAgentsEnvironmentsExperimentsCreate(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The Agent to create an Environment for. Format: &#x60;projects//locations//agents//environments/&#x60;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudDialogflowCxV3Experiment** | [**GoogleCloudDialogflowCxV3Experiment**](GoogleCloudDialogflowCxV3Experiment.md)|  | [optional] 

### Return type

[**GoogleCloudDialogflowCxV3Experiment**](GoogleCloudDialogflowCxV3Experiment.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dialogflowProjectsLocationsAgentsEnvironmentsExperimentsList

> GoogleCloudDialogflowCxV3ListExperimentsResponse dialogflowProjectsLocationsAgentsEnvironmentsExperimentsList(parent, opts)



Returns the list of all experiments in the specified Environment.

### Example

```javascript
import DialogflowApi from 'dialogflow_api';
let defaultClient = DialogflowApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DialogflowApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The Environment to list all environments for. Format: `projects//locations//agents//environments/`.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'pageSize': 56, // Number | The maximum number of items to return in a single page. By default 20 and at most 100.
  'pageToken': "pageToken_example" // String | The next_page_token value returned from a previous list request.
};
apiInstance.dialogflowProjectsLocationsAgentsEnvironmentsExperimentsList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The Environment to list all environments for. Format: &#x60;projects//locations//agents//environments/&#x60;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **pageSize** | **Number**| The maximum number of items to return in a single page. By default 20 and at most 100. | [optional] 
 **pageToken** | **String**| The next_page_token value returned from a previous list request. | [optional] 

### Return type

[**GoogleCloudDialogflowCxV3ListExperimentsResponse**](GoogleCloudDialogflowCxV3ListExperimentsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dialogflowProjectsLocationsAgentsEnvironmentsExperimentsStart

> GoogleCloudDialogflowCxV3Experiment dialogflowProjectsLocationsAgentsEnvironmentsExperimentsStart(name, opts)



Starts the specified Experiment. This rpc only changes the state of experiment from PENDING to RUNNING.

### Example

```javascript
import DialogflowApi from 'dialogflow_api';
let defaultClient = DialogflowApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DialogflowApi.ProjectsApi();
let name = "name_example"; // String | Required. Resource name of the experiment to start. Format: `projects//locations//agents//environments//experiments/`.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'body': {key: null} // Object | 
};
apiInstance.dialogflowProjectsLocationsAgentsEnvironmentsExperimentsStart(name, opts, (error, data, response) => {
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
 **name** | **String**| Required. Resource name of the experiment to start. Format: &#x60;projects//locations//agents//environments//experiments/&#x60;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **body** | **Object**|  | [optional] 

### Return type

[**GoogleCloudDialogflowCxV3Experiment**](GoogleCloudDialogflowCxV3Experiment.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dialogflowProjectsLocationsAgentsEnvironmentsExperimentsStop

> GoogleCloudDialogflowCxV3Experiment dialogflowProjectsLocationsAgentsEnvironmentsExperimentsStop(name, opts)



Stops the specified Experiment. This rpc only changes the state of experiment from RUNNING to DONE.

### Example

```javascript
import DialogflowApi from 'dialogflow_api';
let defaultClient = DialogflowApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DialogflowApi.ProjectsApi();
let name = "name_example"; // String | Required. Resource name of the experiment to stop. Format: `projects//locations//agents//environments//experiments/`.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'body': {key: null} // Object | 
};
apiInstance.dialogflowProjectsLocationsAgentsEnvironmentsExperimentsStop(name, opts, (error, data, response) => {
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
 **name** | **String**| Required. Resource name of the experiment to stop. Format: &#x60;projects//locations//agents//environments//experiments/&#x60;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **body** | **Object**|  | [optional] 

### Return type

[**GoogleCloudDialogflowCxV3Experiment**](GoogleCloudDialogflowCxV3Experiment.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dialogflowProjectsLocationsAgentsEnvironmentsList

> GoogleCloudDialogflowCxV3ListEnvironmentsResponse dialogflowProjectsLocationsAgentsEnvironmentsList(parent, opts)



Returns the list of all environments in the specified Agent.

### Example

```javascript
import DialogflowApi from 'dialogflow_api';
let defaultClient = DialogflowApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DialogflowApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The Agent to list all environments for. Format: `projects//locations//agents/`.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'pageSize': 56, // Number | The maximum number of items to return in a single page. By default 20 and at most 100.
  'pageToken': "pageToken_example" // String | The next_page_token value returned from a previous list request.
};
apiInstance.dialogflowProjectsLocationsAgentsEnvironmentsList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The Agent to list all environments for. Format: &#x60;projects//locations//agents/&#x60;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **pageSize** | **Number**| The maximum number of items to return in a single page. By default 20 and at most 100. | [optional] 
 **pageToken** | **String**| The next_page_token value returned from a previous list request. | [optional] 

### Return type

[**GoogleCloudDialogflowCxV3ListEnvironmentsResponse**](GoogleCloudDialogflowCxV3ListEnvironmentsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dialogflowProjectsLocationsAgentsEnvironmentsLookupEnvironmentHistory

> GoogleCloudDialogflowCxV3LookupEnvironmentHistoryResponse dialogflowProjectsLocationsAgentsEnvironmentsLookupEnvironmentHistory(name, opts)



Looks up the history of the specified Environment.

### Example

```javascript
import DialogflowApi from 'dialogflow_api';
let defaultClient = DialogflowApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DialogflowApi.ProjectsApi();
let name = "name_example"; // String | Required. Resource name of the environment to look up the history for. Format: `projects//locations//agents//environments/`.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'pageSize': 56, // Number | The maximum number of items to return in a single page. By default 100 and at most 1000.
  'pageToken': "pageToken_example" // String | The next_page_token value returned from a previous list request.
};
apiInstance.dialogflowProjectsLocationsAgentsEnvironmentsLookupEnvironmentHistory(name, opts, (error, data, response) => {
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
 **name** | **String**| Required. Resource name of the environment to look up the history for. Format: &#x60;projects//locations//agents//environments/&#x60;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **pageSize** | **Number**| The maximum number of items to return in a single page. By default 100 and at most 1000. | [optional] 
 **pageToken** | **String**| The next_page_token value returned from a previous list request. | [optional] 

### Return type

[**GoogleCloudDialogflowCxV3LookupEnvironmentHistoryResponse**](GoogleCloudDialogflowCxV3LookupEnvironmentHistoryResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dialogflowProjectsLocationsAgentsEnvironmentsRunContinuousTest

> GoogleLongrunningOperation dialogflowProjectsLocationsAgentsEnvironmentsRunContinuousTest(environment, opts)



Kicks off a continuous test under the specified Environment. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned &#x60;Operation&#x60; type has the following method-specific fields: - &#x60;metadata&#x60;: RunContinuousTestMetadata - &#x60;response&#x60;: RunContinuousTestResponse

### Example

```javascript
import DialogflowApi from 'dialogflow_api';
let defaultClient = DialogflowApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DialogflowApi.ProjectsApi();
let environment = "environment_example"; // String | Required. Format: `projects//locations//agents//environments/`.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'body': {key: null} // Object | 
};
apiInstance.dialogflowProjectsLocationsAgentsEnvironmentsRunContinuousTest(environment, opts, (error, data, response) => {
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
 **environment** | **String**| Required. Format: &#x60;projects//locations//agents//environments/&#x60;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **body** | **Object**|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dialogflowProjectsLocationsAgentsFlowsCreate

> GoogleCloudDialogflowCxV3Flow dialogflowProjectsLocationsAgentsFlowsCreate(parent, opts)



Creates a flow in the specified agent. Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

### Example

```javascript
import DialogflowApi from 'dialogflow_api';
let defaultClient = DialogflowApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DialogflowApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The agent to create a flow for. Format: `projects//locations//agents/`.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'languageCode': "languageCode_example", // String | The language of the following fields in `flow`: * `Flow.event_handlers.trigger_fulfillment.messages` * `Flow.event_handlers.trigger_fulfillment.conditional_cases` * `Flow.transition_routes.trigger_fulfillment.messages` * `Flow.transition_routes.trigger_fulfillment.conditional_cases` If not specified, the agent's default language is used. [Many languages](https://cloud.google.com/dialogflow/cx/docs/reference/language) are supported. Note: languages must be enabled in the agent before they can be used.
  'googleCloudDialogflowCxV3Flow': new DialogflowApi.GoogleCloudDialogflowCxV3Flow() // GoogleCloudDialogflowCxV3Flow | 
};
apiInstance.dialogflowProjectsLocationsAgentsFlowsCreate(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The agent to create a flow for. Format: &#x60;projects//locations//agents/&#x60;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **languageCode** | **String**| The language of the following fields in &#x60;flow&#x60;: * &#x60;Flow.event_handlers.trigger_fulfillment.messages&#x60; * &#x60;Flow.event_handlers.trigger_fulfillment.conditional_cases&#x60; * &#x60;Flow.transition_routes.trigger_fulfillment.messages&#x60; * &#x60;Flow.transition_routes.trigger_fulfillment.conditional_cases&#x60; If not specified, the agent&#39;s default language is used. [Many languages](https://cloud.google.com/dialogflow/cx/docs/reference/language) are supported. Note: languages must be enabled in the agent before they can be used. | [optional] 
 **googleCloudDialogflowCxV3Flow** | [**GoogleCloudDialogflowCxV3Flow**](GoogleCloudDialogflowCxV3Flow.md)|  | [optional] 

### Return type

[**GoogleCloudDialogflowCxV3Flow**](GoogleCloudDialogflowCxV3Flow.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dialogflowProjectsLocationsAgentsFlowsExport

> GoogleLongrunningOperation dialogflowProjectsLocationsAgentsFlowsExport(name, opts)



Exports the specified flow to a binary file. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned &#x60;Operation&#x60; type has the following method-specific fields: - &#x60;metadata&#x60;: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct) - &#x60;response&#x60;: ExportFlowResponse Note that resources (e.g. intents, entities, webhooks) that the flow references will also be exported.

### Example

```javascript
import DialogflowApi from 'dialogflow_api';
let defaultClient = DialogflowApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DialogflowApi.ProjectsApi();
let name = "name_example"; // String | Required. The name of the flow to export. Format: `projects//locations//agents//flows/`.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudDialogflowCxV3ExportFlowRequest': new DialogflowApi.GoogleCloudDialogflowCxV3ExportFlowRequest() // GoogleCloudDialogflowCxV3ExportFlowRequest | 
};
apiInstance.dialogflowProjectsLocationsAgentsFlowsExport(name, opts, (error, data, response) => {
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
 **name** | **String**| Required. The name of the flow to export. Format: &#x60;projects//locations//agents//flows/&#x60;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudDialogflowCxV3ExportFlowRequest** | [**GoogleCloudDialogflowCxV3ExportFlowRequest**](GoogleCloudDialogflowCxV3ExportFlowRequest.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dialogflowProjectsLocationsAgentsFlowsImport

> GoogleLongrunningOperation dialogflowProjectsLocationsAgentsFlowsImport(parent, opts)



Imports the specified flow to the specified agent from a binary file. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned &#x60;Operation&#x60; type has the following method-specific fields: - &#x60;metadata&#x60;: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct) - &#x60;response&#x60;: ImportFlowResponse Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

### Example

```javascript
import DialogflowApi from 'dialogflow_api';
let defaultClient = DialogflowApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DialogflowApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The agent to import the flow into. Format: `projects//locations//agents/`.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudDialogflowCxV3ImportFlowRequest': new DialogflowApi.GoogleCloudDialogflowCxV3ImportFlowRequest() // GoogleCloudDialogflowCxV3ImportFlowRequest | 
};
apiInstance.dialogflowProjectsLocationsAgentsFlowsImport(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The agent to import the flow into. Format: &#x60;projects//locations//agents/&#x60;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudDialogflowCxV3ImportFlowRequest** | [**GoogleCloudDialogflowCxV3ImportFlowRequest**](GoogleCloudDialogflowCxV3ImportFlowRequest.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dialogflowProjectsLocationsAgentsFlowsList

> GoogleCloudDialogflowCxV3ListFlowsResponse dialogflowProjectsLocationsAgentsFlowsList(parent, opts)



Returns the list of all flows in the specified agent.

### Example

```javascript
import DialogflowApi from 'dialogflow_api';
let defaultClient = DialogflowApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DialogflowApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The agent containing the flows. Format: `projects//locations//agents/`.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'languageCode': "languageCode_example", // String | The language to list flows for. The following fields are language dependent: * `Flow.event_handlers.trigger_fulfillment.messages` * `Flow.event_handlers.trigger_fulfillment.conditional_cases` * `Flow.transition_routes.trigger_fulfillment.messages` * `Flow.transition_routes.trigger_fulfillment.conditional_cases` If not specified, the agent's default language is used. [Many languages](https://cloud.google.com/dialogflow/cx/docs/reference/language) are supported. Note: languages must be enabled in the agent before they can be used.
  'pageSize': 56, // Number | The maximum number of items to return in a single page. By default 100 and at most 1000.
  'pageToken': "pageToken_example" // String | The next_page_token value returned from a previous list request.
};
apiInstance.dialogflowProjectsLocationsAgentsFlowsList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The agent containing the flows. Format: &#x60;projects//locations//agents/&#x60;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **languageCode** | **String**| The language to list flows for. The following fields are language dependent: * &#x60;Flow.event_handlers.trigger_fulfillment.messages&#x60; * &#x60;Flow.event_handlers.trigger_fulfillment.conditional_cases&#x60; * &#x60;Flow.transition_routes.trigger_fulfillment.messages&#x60; * &#x60;Flow.transition_routes.trigger_fulfillment.conditional_cases&#x60; If not specified, the agent&#39;s default language is used. [Many languages](https://cloud.google.com/dialogflow/cx/docs/reference/language) are supported. Note: languages must be enabled in the agent before they can be used. | [optional] 
 **pageSize** | **Number**| The maximum number of items to return in a single page. By default 100 and at most 1000. | [optional] 
 **pageToken** | **String**| The next_page_token value returned from a previous list request. | [optional] 

### Return type

[**GoogleCloudDialogflowCxV3ListFlowsResponse**](GoogleCloudDialogflowCxV3ListFlowsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dialogflowProjectsLocationsAgentsFlowsPagesCreate

> GoogleCloudDialogflowCxV3Page dialogflowProjectsLocationsAgentsFlowsPagesCreate(parent, opts)



Creates a page in the specified flow. Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

### Example

```javascript
import DialogflowApi from 'dialogflow_api';
let defaultClient = DialogflowApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DialogflowApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The flow to create a page for. Format: `projects//locations//agents//flows/`.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'languageCode': "languageCode_example", // String | The language of the following fields in `page`: * `Page.entry_fulfillment.messages` * `Page.entry_fulfillment.conditional_cases` * `Page.event_handlers.trigger_fulfillment.messages` * `Page.event_handlers.trigger_fulfillment.conditional_cases` * `Page.form.parameters.fill_behavior.initial_prompt_fulfillment.messages` * `Page.form.parameters.fill_behavior.initial_prompt_fulfillment.conditional_cases` * `Page.form.parameters.fill_behavior.reprompt_event_handlers.messages` * `Page.form.parameters.fill_behavior.reprompt_event_handlers.conditional_cases` * `Page.transition_routes.trigger_fulfillment.messages` * `Page.transition_routes.trigger_fulfillment.conditional_cases` If not specified, the agent's default language is used. [Many languages](https://cloud.google.com/dialogflow/cx/docs/reference/language) are supported. Note: languages must be enabled in the agent before they can be used.
  'googleCloudDialogflowCxV3Page': new DialogflowApi.GoogleCloudDialogflowCxV3Page() // GoogleCloudDialogflowCxV3Page | 
};
apiInstance.dialogflowProjectsLocationsAgentsFlowsPagesCreate(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The flow to create a page for. Format: &#x60;projects//locations//agents//flows/&#x60;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **languageCode** | **String**| The language of the following fields in &#x60;page&#x60;: * &#x60;Page.entry_fulfillment.messages&#x60; * &#x60;Page.entry_fulfillment.conditional_cases&#x60; * &#x60;Page.event_handlers.trigger_fulfillment.messages&#x60; * &#x60;Page.event_handlers.trigger_fulfillment.conditional_cases&#x60; * &#x60;Page.form.parameters.fill_behavior.initial_prompt_fulfillment.messages&#x60; * &#x60;Page.form.parameters.fill_behavior.initial_prompt_fulfillment.conditional_cases&#x60; * &#x60;Page.form.parameters.fill_behavior.reprompt_event_handlers.messages&#x60; * &#x60;Page.form.parameters.fill_behavior.reprompt_event_handlers.conditional_cases&#x60; * &#x60;Page.transition_routes.trigger_fulfillment.messages&#x60; * &#x60;Page.transition_routes.trigger_fulfillment.conditional_cases&#x60; If not specified, the agent&#39;s default language is used. [Many languages](https://cloud.google.com/dialogflow/cx/docs/reference/language) are supported. Note: languages must be enabled in the agent before they can be used. | [optional] 
 **googleCloudDialogflowCxV3Page** | [**GoogleCloudDialogflowCxV3Page**](GoogleCloudDialogflowCxV3Page.md)|  | [optional] 

### Return type

[**GoogleCloudDialogflowCxV3Page**](GoogleCloudDialogflowCxV3Page.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dialogflowProjectsLocationsAgentsFlowsPagesList

> GoogleCloudDialogflowCxV3ListPagesResponse dialogflowProjectsLocationsAgentsFlowsPagesList(parent, opts)



Returns the list of all pages in the specified flow.

### Example

```javascript
import DialogflowApi from 'dialogflow_api';
let defaultClient = DialogflowApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DialogflowApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The flow to list all pages for. Format: `projects//locations//agents//flows/`.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'languageCode': "languageCode_example", // String | The language to list pages for. The following fields are language dependent: * `Page.entry_fulfillment.messages` * `Page.entry_fulfillment.conditional_cases` * `Page.event_handlers.trigger_fulfillment.messages` * `Page.event_handlers.trigger_fulfillment.conditional_cases` * `Page.form.parameters.fill_behavior.initial_prompt_fulfillment.messages` * `Page.form.parameters.fill_behavior.initial_prompt_fulfillment.conditional_cases` * `Page.form.parameters.fill_behavior.reprompt_event_handlers.messages` * `Page.form.parameters.fill_behavior.reprompt_event_handlers.conditional_cases` * `Page.transition_routes.trigger_fulfillment.messages` * `Page.transition_routes.trigger_fulfillment.conditional_cases` If not specified, the agent's default language is used. [Many languages](https://cloud.google.com/dialogflow/cx/docs/reference/language) are supported. Note: languages must be enabled in the agent before they can be used.
  'pageSize': 56, // Number | The maximum number of items to return in a single page. By default 100 and at most 1000.
  'pageToken': "pageToken_example" // String | The next_page_token value returned from a previous list request.
};
apiInstance.dialogflowProjectsLocationsAgentsFlowsPagesList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The flow to list all pages for. Format: &#x60;projects//locations//agents//flows/&#x60;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **languageCode** | **String**| The language to list pages for. The following fields are language dependent: * &#x60;Page.entry_fulfillment.messages&#x60; * &#x60;Page.entry_fulfillment.conditional_cases&#x60; * &#x60;Page.event_handlers.trigger_fulfillment.messages&#x60; * &#x60;Page.event_handlers.trigger_fulfillment.conditional_cases&#x60; * &#x60;Page.form.parameters.fill_behavior.initial_prompt_fulfillment.messages&#x60; * &#x60;Page.form.parameters.fill_behavior.initial_prompt_fulfillment.conditional_cases&#x60; * &#x60;Page.form.parameters.fill_behavior.reprompt_event_handlers.messages&#x60; * &#x60;Page.form.parameters.fill_behavior.reprompt_event_handlers.conditional_cases&#x60; * &#x60;Page.transition_routes.trigger_fulfillment.messages&#x60; * &#x60;Page.transition_routes.trigger_fulfillment.conditional_cases&#x60; If not specified, the agent&#39;s default language is used. [Many languages](https://cloud.google.com/dialogflow/cx/docs/reference/language) are supported. Note: languages must be enabled in the agent before they can be used. | [optional] 
 **pageSize** | **Number**| The maximum number of items to return in a single page. By default 100 and at most 1000. | [optional] 
 **pageToken** | **String**| The next_page_token value returned from a previous list request. | [optional] 

### Return type

[**GoogleCloudDialogflowCxV3ListPagesResponse**](GoogleCloudDialogflowCxV3ListPagesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dialogflowProjectsLocationsAgentsFlowsTrain

> GoogleLongrunningOperation dialogflowProjectsLocationsAgentsFlowsTrain(name, opts)



Trains the specified flow. Note that only the flow in &#39;draft&#39; environment is trained. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned &#x60;Operation&#x60; type has the following method-specific fields: - &#x60;metadata&#x60;: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct) - &#x60;response&#x60;: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty) Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

### Example

```javascript
import DialogflowApi from 'dialogflow_api';
let defaultClient = DialogflowApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DialogflowApi.ProjectsApi();
let name = "name_example"; // String | Required. The flow to train. Format: `projects//locations//agents//flows/`.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'body': {key: null} // Object | 
};
apiInstance.dialogflowProjectsLocationsAgentsFlowsTrain(name, opts, (error, data, response) => {
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
 **name** | **String**| Required. The flow to train. Format: &#x60;projects//locations//agents//flows/&#x60;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **body** | **Object**|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dialogflowProjectsLocationsAgentsFlowsValidate

> GoogleCloudDialogflowCxV3FlowValidationResult dialogflowProjectsLocationsAgentsFlowsValidate(name, opts)



Validates the specified flow and creates or updates validation results. Please call this API after the training is completed to get the complete validation results.

### Example

```javascript
import DialogflowApi from 'dialogflow_api';
let defaultClient = DialogflowApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DialogflowApi.ProjectsApi();
let name = "name_example"; // String | Required. The flow to validate. Format: `projects//locations//agents//flows/`.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudDialogflowCxV3ValidateFlowRequest': new DialogflowApi.GoogleCloudDialogflowCxV3ValidateFlowRequest() // GoogleCloudDialogflowCxV3ValidateFlowRequest | 
};
apiInstance.dialogflowProjectsLocationsAgentsFlowsValidate(name, opts, (error, data, response) => {
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
 **name** | **String**| Required. The flow to validate. Format: &#x60;projects//locations//agents//flows/&#x60;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudDialogflowCxV3ValidateFlowRequest** | [**GoogleCloudDialogflowCxV3ValidateFlowRequest**](GoogleCloudDialogflowCxV3ValidateFlowRequest.md)|  | [optional] 

### Return type

[**GoogleCloudDialogflowCxV3FlowValidationResult**](GoogleCloudDialogflowCxV3FlowValidationResult.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dialogflowProjectsLocationsAgentsFlowsVersionsCompareVersions

> GoogleCloudDialogflowCxV3CompareVersionsResponse dialogflowProjectsLocationsAgentsFlowsVersionsCompareVersions(baseVersion, opts)



Compares the specified base version with target version.

### Example

```javascript
import DialogflowApi from 'dialogflow_api';
let defaultClient = DialogflowApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DialogflowApi.ProjectsApi();
let baseVersion = "baseVersion_example"; // String | Required. Name of the base flow version to compare with the target version. Use version ID `0` to indicate the draft version of the specified flow. Format: `projects//locations//agents/ /flows//versions/`.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudDialogflowCxV3CompareVersionsRequest': new DialogflowApi.GoogleCloudDialogflowCxV3CompareVersionsRequest() // GoogleCloudDialogflowCxV3CompareVersionsRequest | 
};
apiInstance.dialogflowProjectsLocationsAgentsFlowsVersionsCompareVersions(baseVersion, opts, (error, data, response) => {
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
 **baseVersion** | **String**| Required. Name of the base flow version to compare with the target version. Use version ID &#x60;0&#x60; to indicate the draft version of the specified flow. Format: &#x60;projects//locations//agents/ /flows//versions/&#x60;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudDialogflowCxV3CompareVersionsRequest** | [**GoogleCloudDialogflowCxV3CompareVersionsRequest**](GoogleCloudDialogflowCxV3CompareVersionsRequest.md)|  | [optional] 

### Return type

[**GoogleCloudDialogflowCxV3CompareVersionsResponse**](GoogleCloudDialogflowCxV3CompareVersionsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dialogflowProjectsLocationsAgentsFlowsVersionsCreate

> GoogleLongrunningOperation dialogflowProjectsLocationsAgentsFlowsVersionsCreate(parent, opts)



Creates a Version in the specified Flow. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned &#x60;Operation&#x60; type has the following method-specific fields: - &#x60;metadata&#x60;: CreateVersionOperationMetadata - &#x60;response&#x60;: Version

### Example

```javascript
import DialogflowApi from 'dialogflow_api';
let defaultClient = DialogflowApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DialogflowApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The Flow to create an Version for. Format: `projects//locations//agents//flows/`.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudDialogflowCxV3Version': new DialogflowApi.GoogleCloudDialogflowCxV3Version() // GoogleCloudDialogflowCxV3Version | 
};
apiInstance.dialogflowProjectsLocationsAgentsFlowsVersionsCreate(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The Flow to create an Version for. Format: &#x60;projects//locations//agents//flows/&#x60;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudDialogflowCxV3Version** | [**GoogleCloudDialogflowCxV3Version**](GoogleCloudDialogflowCxV3Version.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dialogflowProjectsLocationsAgentsFlowsVersionsList

> GoogleCloudDialogflowCxV3ListVersionsResponse dialogflowProjectsLocationsAgentsFlowsVersionsList(parent, opts)



Returns the list of all versions in the specified Flow.

### Example

```javascript
import DialogflowApi from 'dialogflow_api';
let defaultClient = DialogflowApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DialogflowApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The Flow to list all versions for. Format: `projects//locations//agents//flows/`.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'pageSize': 56, // Number | The maximum number of items to return in a single page. By default 20 and at most 100.
  'pageToken': "pageToken_example" // String | The next_page_token value returned from a previous list request.
};
apiInstance.dialogflowProjectsLocationsAgentsFlowsVersionsList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The Flow to list all versions for. Format: &#x60;projects//locations//agents//flows/&#x60;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **pageSize** | **Number**| The maximum number of items to return in a single page. By default 20 and at most 100. | [optional] 
 **pageToken** | **String**| The next_page_token value returned from a previous list request. | [optional] 

### Return type

[**GoogleCloudDialogflowCxV3ListVersionsResponse**](GoogleCloudDialogflowCxV3ListVersionsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dialogflowProjectsLocationsAgentsFlowsVersionsLoad

> GoogleLongrunningOperation dialogflowProjectsLocationsAgentsFlowsVersionsLoad(name, opts)



Loads resources in the specified version to the draft flow. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned &#x60;Operation&#x60; type has the following method-specific fields: - &#x60;metadata&#x60;: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct) - &#x60;response&#x60;: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)

### Example

```javascript
import DialogflowApi from 'dialogflow_api';
let defaultClient = DialogflowApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DialogflowApi.ProjectsApi();
let name = "name_example"; // String | Required. The Version to be loaded to draft flow. Format: `projects//locations//agents//flows//versions/`.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudDialogflowCxV3LoadVersionRequest': new DialogflowApi.GoogleCloudDialogflowCxV3LoadVersionRequest() // GoogleCloudDialogflowCxV3LoadVersionRequest | 
};
apiInstance.dialogflowProjectsLocationsAgentsFlowsVersionsLoad(name, opts, (error, data, response) => {
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
 **name** | **String**| Required. The Version to be loaded to draft flow. Format: &#x60;projects//locations//agents//flows//versions/&#x60;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudDialogflowCxV3LoadVersionRequest** | [**GoogleCloudDialogflowCxV3LoadVersionRequest**](GoogleCloudDialogflowCxV3LoadVersionRequest.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dialogflowProjectsLocationsAgentsGeneratorsCreate

> GoogleCloudDialogflowCxV3Generator dialogflowProjectsLocationsAgentsGeneratorsCreate(parent, opts)



Creates a generator in the specified agent.

### Example

```javascript
import DialogflowApi from 'dialogflow_api';
let defaultClient = DialogflowApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DialogflowApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The agent to create a generator for. Format: `projects//locations//agents/`.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'languageCode': "languageCode_example", // String | The language to create generators for the following fields: * `Generator.prompt_text.text` If not specified, the agent's default language is used.
  'googleCloudDialogflowCxV3Generator': new DialogflowApi.GoogleCloudDialogflowCxV3Generator() // GoogleCloudDialogflowCxV3Generator | 
};
apiInstance.dialogflowProjectsLocationsAgentsGeneratorsCreate(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The agent to create a generator for. Format: &#x60;projects//locations//agents/&#x60;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **languageCode** | **String**| The language to create generators for the following fields: * &#x60;Generator.prompt_text.text&#x60; If not specified, the agent&#39;s default language is used. | [optional] 
 **googleCloudDialogflowCxV3Generator** | [**GoogleCloudDialogflowCxV3Generator**](GoogleCloudDialogflowCxV3Generator.md)|  | [optional] 

### Return type

[**GoogleCloudDialogflowCxV3Generator**](GoogleCloudDialogflowCxV3Generator.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dialogflowProjectsLocationsAgentsGeneratorsList

> GoogleCloudDialogflowCxV3ListGeneratorsResponse dialogflowProjectsLocationsAgentsGeneratorsList(parent, opts)



Returns the list of all generators in the specified agent.

### Example

```javascript
import DialogflowApi from 'dialogflow_api';
let defaultClient = DialogflowApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DialogflowApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The agent to list all generators for. Format: `projects//locations//agents/`.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'languageCode': "languageCode_example", // String | The language to list generators for.
  'pageSize': 56, // Number | The maximum number of items to return in a single page. By default 100 and at most 1000.
  'pageToken': "pageToken_example" // String | The next_page_token value returned from a previous list request.
};
apiInstance.dialogflowProjectsLocationsAgentsGeneratorsList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The agent to list all generators for. Format: &#x60;projects//locations//agents/&#x60;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **languageCode** | **String**| The language to list generators for. | [optional] 
 **pageSize** | **Number**| The maximum number of items to return in a single page. By default 100 and at most 1000. | [optional] 
 **pageToken** | **String**| The next_page_token value returned from a previous list request. | [optional] 

### Return type

[**GoogleCloudDialogflowCxV3ListGeneratorsResponse**](GoogleCloudDialogflowCxV3ListGeneratorsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dialogflowProjectsLocationsAgentsIntentsCreate

> GoogleCloudDialogflowCxV3Intent dialogflowProjectsLocationsAgentsIntentsCreate(parent, opts)



Creates an intent in the specified agent. Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

### Example

```javascript
import DialogflowApi from 'dialogflow_api';
let defaultClient = DialogflowApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DialogflowApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The agent to create an intent for. Format: `projects//locations//agents/`.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'languageCode': "languageCode_example", // String | The language of the following fields in `intent`: * `Intent.training_phrases.parts.text` If not specified, the agent's default language is used. [Many languages](https://cloud.google.com/dialogflow/cx/docs/reference/language) are supported. Note: languages must be enabled in the agent before they can be used.
  'googleCloudDialogflowCxV3Intent': new DialogflowApi.GoogleCloudDialogflowCxV3Intent() // GoogleCloudDialogflowCxV3Intent | 
};
apiInstance.dialogflowProjectsLocationsAgentsIntentsCreate(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The agent to create an intent for. Format: &#x60;projects//locations//agents/&#x60;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **languageCode** | **String**| The language of the following fields in &#x60;intent&#x60;: * &#x60;Intent.training_phrases.parts.text&#x60; If not specified, the agent&#39;s default language is used. [Many languages](https://cloud.google.com/dialogflow/cx/docs/reference/language) are supported. Note: languages must be enabled in the agent before they can be used. | [optional] 
 **googleCloudDialogflowCxV3Intent** | [**GoogleCloudDialogflowCxV3Intent**](GoogleCloudDialogflowCxV3Intent.md)|  | [optional] 

### Return type

[**GoogleCloudDialogflowCxV3Intent**](GoogleCloudDialogflowCxV3Intent.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dialogflowProjectsLocationsAgentsIntentsExport

> GoogleLongrunningOperation dialogflowProjectsLocationsAgentsIntentsExport(parent, opts)



Exports the selected intents. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned &#x60;Operation&#x60; type has the following method-specific fields: - &#x60;metadata&#x60;: ExportIntentsMetadata - &#x60;response&#x60;: ExportIntentsResponse

### Example

```javascript
import DialogflowApi from 'dialogflow_api';
let defaultClient = DialogflowApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DialogflowApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The name of the parent agent to export intents. Format: `projects//locations//agents/`.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudDialogflowCxV3ExportIntentsRequest': new DialogflowApi.GoogleCloudDialogflowCxV3ExportIntentsRequest() // GoogleCloudDialogflowCxV3ExportIntentsRequest | 
};
apiInstance.dialogflowProjectsLocationsAgentsIntentsExport(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The name of the parent agent to export intents. Format: &#x60;projects//locations//agents/&#x60;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudDialogflowCxV3ExportIntentsRequest** | [**GoogleCloudDialogflowCxV3ExportIntentsRequest**](GoogleCloudDialogflowCxV3ExportIntentsRequest.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dialogflowProjectsLocationsAgentsIntentsImport

> GoogleLongrunningOperation dialogflowProjectsLocationsAgentsIntentsImport(parent, opts)



Imports the specified intents into the agent. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned &#x60;Operation&#x60; type has the following method-specific fields: - &#x60;metadata&#x60;: ImportIntentsMetadata - &#x60;response&#x60;: ImportIntentsResponse

### Example

```javascript
import DialogflowApi from 'dialogflow_api';
let defaultClient = DialogflowApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DialogflowApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The agent to import the intents into. Format: `projects//locations//agents/`.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudDialogflowCxV3ImportIntentsRequest': new DialogflowApi.GoogleCloudDialogflowCxV3ImportIntentsRequest() // GoogleCloudDialogflowCxV3ImportIntentsRequest | 
};
apiInstance.dialogflowProjectsLocationsAgentsIntentsImport(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The agent to import the intents into. Format: &#x60;projects//locations//agents/&#x60;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudDialogflowCxV3ImportIntentsRequest** | [**GoogleCloudDialogflowCxV3ImportIntentsRequest**](GoogleCloudDialogflowCxV3ImportIntentsRequest.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dialogflowProjectsLocationsAgentsIntentsList

> GoogleCloudDialogflowCxV3ListIntentsResponse dialogflowProjectsLocationsAgentsIntentsList(parent, opts)



Returns the list of all intents in the specified agent.

### Example

```javascript
import DialogflowApi from 'dialogflow_api';
let defaultClient = DialogflowApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DialogflowApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The agent to list all intents for. Format: `projects//locations//agents/`.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'intentView': "intentView_example", // String | The resource view to apply to the returned intent.
  'languageCode': "languageCode_example", // String | The language to list intents for. The following fields are language dependent: * `Intent.training_phrases.parts.text` If not specified, the agent's default language is used. [Many languages](https://cloud.google.com/dialogflow/cx/docs/reference/language) are supported. Note: languages must be enabled in the agent before they can be used.
  'pageSize': 56, // Number | The maximum number of items to return in a single page. By default 100 and at most 1000.
  'pageToken': "pageToken_example" // String | The next_page_token value returned from a previous list request.
};
apiInstance.dialogflowProjectsLocationsAgentsIntentsList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The agent to list all intents for. Format: &#x60;projects//locations//agents/&#x60;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **intentView** | **String**| The resource view to apply to the returned intent. | [optional] 
 **languageCode** | **String**| The language to list intents for. The following fields are language dependent: * &#x60;Intent.training_phrases.parts.text&#x60; If not specified, the agent&#39;s default language is used. [Many languages](https://cloud.google.com/dialogflow/cx/docs/reference/language) are supported. Note: languages must be enabled in the agent before they can be used. | [optional] 
 **pageSize** | **Number**| The maximum number of items to return in a single page. By default 100 and at most 1000. | [optional] 
 **pageToken** | **String**| The next_page_token value returned from a previous list request. | [optional] 

### Return type

[**GoogleCloudDialogflowCxV3ListIntentsResponse**](GoogleCloudDialogflowCxV3ListIntentsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dialogflowProjectsLocationsAgentsList

> GoogleCloudDialogflowCxV3ListAgentsResponse dialogflowProjectsLocationsAgentsList(parent, opts)



Returns the list of all agents in the specified location.

### Example

```javascript
import DialogflowApi from 'dialogflow_api';
let defaultClient = DialogflowApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DialogflowApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The location to list all agents for. Format: `projects//locations/`.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'pageSize': 56, // Number | The maximum number of items to return in a single page. By default 100 and at most 1000.
  'pageToken': "pageToken_example" // String | The next_page_token value returned from a previous list request.
};
apiInstance.dialogflowProjectsLocationsAgentsList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The location to list all agents for. Format: &#x60;projects//locations/&#x60;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **pageSize** | **Number**| The maximum number of items to return in a single page. By default 100 and at most 1000. | [optional] 
 **pageToken** | **String**| The next_page_token value returned from a previous list request. | [optional] 

### Return type

[**GoogleCloudDialogflowCxV3ListAgentsResponse**](GoogleCloudDialogflowCxV3ListAgentsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dialogflowProjectsLocationsAgentsRestore

> GoogleLongrunningOperation dialogflowProjectsLocationsAgentsRestore(name, opts)



Restores the specified agent from a binary file. Replaces the current agent with a new one. Note that all existing resources in agent (e.g. intents, entity types, flows) will be removed. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned &#x60;Operation&#x60; type has the following method-specific fields: - &#x60;metadata&#x60;: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct) - &#x60;response&#x60;: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty) Note: You should always train flows prior to sending them queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

### Example

```javascript
import DialogflowApi from 'dialogflow_api';
let defaultClient = DialogflowApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DialogflowApi.ProjectsApi();
let name = "name_example"; // String | Required. The name of the agent to restore into. Format: `projects//locations//agents/`.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudDialogflowCxV3RestoreAgentRequest': new DialogflowApi.GoogleCloudDialogflowCxV3RestoreAgentRequest() // GoogleCloudDialogflowCxV3RestoreAgentRequest | 
};
apiInstance.dialogflowProjectsLocationsAgentsRestore(name, opts, (error, data, response) => {
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
 **name** | **String**| Required. The name of the agent to restore into. Format: &#x60;projects//locations//agents/&#x60;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudDialogflowCxV3RestoreAgentRequest** | [**GoogleCloudDialogflowCxV3RestoreAgentRequest**](GoogleCloudDialogflowCxV3RestoreAgentRequest.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dialogflowProjectsLocationsAgentsSessionsDetectIntent

> GoogleCloudDialogflowCxV3DetectIntentResponse dialogflowProjectsLocationsAgentsSessionsDetectIntent(session, opts)



Processes a natural language query and returns structured, actionable data as a result. This method is not idempotent, because it may cause session entity types to be updated, which in turn might affect results of future queries. Note: Always use agent versions for production traffic. See [Versions and environments](https://cloud.google.com/dialogflow/cx/docs/concept/version).

### Example

```javascript
import DialogflowApi from 'dialogflow_api';
let defaultClient = DialogflowApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DialogflowApi.ProjectsApi();
let session = "session_example"; // String | Required. The name of the session this query is sent to. Format: `projects//locations//agents//sessions/` or `projects//locations//agents//environments//sessions/`. If `Environment ID` is not specified, we assume default 'draft' environment. It's up to the API caller to choose an appropriate `Session ID`. It can be a random number or some type of session identifiers (preferably hashed). The length of the `Session ID` must not exceed 36 characters. For more information, see the [sessions guide](https://cloud.google.com/dialogflow/cx/docs/concept/session). Note: Always use agent versions for production traffic. See [Versions and environments](https://cloud.google.com/dialogflow/cx/docs/concept/version).
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudDialogflowCxV3DetectIntentRequest': new DialogflowApi.GoogleCloudDialogflowCxV3DetectIntentRequest() // GoogleCloudDialogflowCxV3DetectIntentRequest | 
};
apiInstance.dialogflowProjectsLocationsAgentsSessionsDetectIntent(session, opts, (error, data, response) => {
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
 **session** | **String**| Required. The name of the session this query is sent to. Format: &#x60;projects//locations//agents//sessions/&#x60; or &#x60;projects//locations//agents//environments//sessions/&#x60;. If &#x60;Environment ID&#x60; is not specified, we assume default &#39;draft&#39; environment. It&#39;s up to the API caller to choose an appropriate &#x60;Session ID&#x60;. It can be a random number or some type of session identifiers (preferably hashed). The length of the &#x60;Session ID&#x60; must not exceed 36 characters. For more information, see the [sessions guide](https://cloud.google.com/dialogflow/cx/docs/concept/session). Note: Always use agent versions for production traffic. See [Versions and environments](https://cloud.google.com/dialogflow/cx/docs/concept/version). | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudDialogflowCxV3DetectIntentRequest** | [**GoogleCloudDialogflowCxV3DetectIntentRequest**](GoogleCloudDialogflowCxV3DetectIntentRequest.md)|  | [optional] 

### Return type

[**GoogleCloudDialogflowCxV3DetectIntentResponse**](GoogleCloudDialogflowCxV3DetectIntentResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dialogflowProjectsLocationsAgentsSessionsEntityTypesCreate

> GoogleCloudDialogflowCxV3SessionEntityType dialogflowProjectsLocationsAgentsSessionsEntityTypesCreate(parent, opts)



Creates a session entity type.

### Example

```javascript
import DialogflowApi from 'dialogflow_api';
let defaultClient = DialogflowApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DialogflowApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The session to create a session entity type for. Format: `projects//locations//agents//sessions/` or `projects//locations//agents//environments//sessions/`. If `Environment ID` is not specified, we assume default 'draft' environment.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'languageCode': "languageCode_example", // String | The language of the following fields in `entity_type`: * `EntityType.entities.value` * `EntityType.entities.synonyms` * `EntityType.excluded_phrases.value` If not specified, the agent's default language is used. [Many languages](https://cloud.google.com/dialogflow/cx/docs/reference/language) are supported. Note: languages must be enabled in the agent before they can be used.
  'googleCloudDialogflowCxV3SessionEntityType': new DialogflowApi.GoogleCloudDialogflowCxV3SessionEntityType() // GoogleCloudDialogflowCxV3SessionEntityType | 
};
apiInstance.dialogflowProjectsLocationsAgentsSessionsEntityTypesCreate(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The session to create a session entity type for. Format: &#x60;projects//locations//agents//sessions/&#x60; or &#x60;projects//locations//agents//environments//sessions/&#x60;. If &#x60;Environment ID&#x60; is not specified, we assume default &#39;draft&#39; environment. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **languageCode** | **String**| The language of the following fields in &#x60;entity_type&#x60;: * &#x60;EntityType.entities.value&#x60; * &#x60;EntityType.entities.synonyms&#x60; * &#x60;EntityType.excluded_phrases.value&#x60; If not specified, the agent&#39;s default language is used. [Many languages](https://cloud.google.com/dialogflow/cx/docs/reference/language) are supported. Note: languages must be enabled in the agent before they can be used. | [optional] 
 **googleCloudDialogflowCxV3SessionEntityType** | [**GoogleCloudDialogflowCxV3SessionEntityType**](GoogleCloudDialogflowCxV3SessionEntityType.md)|  | [optional] 

### Return type

[**GoogleCloudDialogflowCxV3SessionEntityType**](GoogleCloudDialogflowCxV3SessionEntityType.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dialogflowProjectsLocationsAgentsSessionsEntityTypesList

> GoogleCloudDialogflowCxV3ListSessionEntityTypesResponse dialogflowProjectsLocationsAgentsSessionsEntityTypesList(parent, opts)



Returns the list of all session entity types in the specified session.

### Example

```javascript
import DialogflowApi from 'dialogflow_api';
let defaultClient = DialogflowApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DialogflowApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The session to list all session entity types from. Format: `projects//locations//agents//sessions/` or `projects//locations//agents//environments//sessions/`. If `Environment ID` is not specified, we assume default 'draft' environment.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'pageSize': 56, // Number | The maximum number of items to return in a single page. By default 100 and at most 1000.
  'pageToken': "pageToken_example" // String | The next_page_token value returned from a previous list request.
};
apiInstance.dialogflowProjectsLocationsAgentsSessionsEntityTypesList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The session to list all session entity types from. Format: &#x60;projects//locations//agents//sessions/&#x60; or &#x60;projects//locations//agents//environments//sessions/&#x60;. If &#x60;Environment ID&#x60; is not specified, we assume default &#39;draft&#39; environment. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **pageSize** | **Number**| The maximum number of items to return in a single page. By default 100 and at most 1000. | [optional] 
 **pageToken** | **String**| The next_page_token value returned from a previous list request. | [optional] 

### Return type

[**GoogleCloudDialogflowCxV3ListSessionEntityTypesResponse**](GoogleCloudDialogflowCxV3ListSessionEntityTypesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dialogflowProjectsLocationsAgentsSessionsFulfillIntent

> GoogleCloudDialogflowCxV3FulfillIntentResponse dialogflowProjectsLocationsAgentsSessionsFulfillIntent(session, opts)



Fulfills a matched intent returned by MatchIntent. Must be called after MatchIntent, with input from MatchIntentResponse. Otherwise, the behavior is undefined.

### Example

```javascript
import DialogflowApi from 'dialogflow_api';
let defaultClient = DialogflowApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DialogflowApi.ProjectsApi();
let session = "session_example"; // String | Required. The name of the session this query is sent to. Format: `projects//locations//agents//sessions/` or `projects//locations//agents//environments//sessions/`. If `Environment ID` is not specified, we assume default 'draft' environment. It's up to the API caller to choose an appropriate `Session ID`. It can be a random number or some type of session identifiers (preferably hashed). The length of the `Session ID` must not exceed 36 characters. For more information, see the [sessions guide](https://cloud.google.com/dialogflow/cx/docs/concept/session).
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudDialogflowCxV3FulfillIntentRequest': new DialogflowApi.GoogleCloudDialogflowCxV3FulfillIntentRequest() // GoogleCloudDialogflowCxV3FulfillIntentRequest | 
};
apiInstance.dialogflowProjectsLocationsAgentsSessionsFulfillIntent(session, opts, (error, data, response) => {
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
 **session** | **String**| Required. The name of the session this query is sent to. Format: &#x60;projects//locations//agents//sessions/&#x60; or &#x60;projects//locations//agents//environments//sessions/&#x60;. If &#x60;Environment ID&#x60; is not specified, we assume default &#39;draft&#39; environment. It&#39;s up to the API caller to choose an appropriate &#x60;Session ID&#x60;. It can be a random number or some type of session identifiers (preferably hashed). The length of the &#x60;Session ID&#x60; must not exceed 36 characters. For more information, see the [sessions guide](https://cloud.google.com/dialogflow/cx/docs/concept/session). | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudDialogflowCxV3FulfillIntentRequest** | [**GoogleCloudDialogflowCxV3FulfillIntentRequest**](GoogleCloudDialogflowCxV3FulfillIntentRequest.md)|  | [optional] 

### Return type

[**GoogleCloudDialogflowCxV3FulfillIntentResponse**](GoogleCloudDialogflowCxV3FulfillIntentResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dialogflowProjectsLocationsAgentsSessionsMatchIntent

> GoogleCloudDialogflowCxV3MatchIntentResponse dialogflowProjectsLocationsAgentsSessionsMatchIntent(session, opts)



Returns preliminary intent match results, doesn&#39;t change the session status.

### Example

```javascript
import DialogflowApi from 'dialogflow_api';
let defaultClient = DialogflowApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DialogflowApi.ProjectsApi();
let session = "session_example"; // String | Required. The name of the session this query is sent to. Format: `projects//locations//agents//sessions/` or `projects//locations//agents//environments//sessions/`. If `Environment ID` is not specified, we assume default 'draft' environment. It's up to the API caller to choose an appropriate `Session ID`. It can be a random number or some type of session identifiers (preferably hashed). The length of the `Session ID` must not exceed 36 characters. For more information, see the [sessions guide](https://cloud.google.com/dialogflow/cx/docs/concept/session).
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudDialogflowCxV3MatchIntentRequest': new DialogflowApi.GoogleCloudDialogflowCxV3MatchIntentRequest() // GoogleCloudDialogflowCxV3MatchIntentRequest | 
};
apiInstance.dialogflowProjectsLocationsAgentsSessionsMatchIntent(session, opts, (error, data, response) => {
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
 **session** | **String**| Required. The name of the session this query is sent to. Format: &#x60;projects//locations//agents//sessions/&#x60; or &#x60;projects//locations//agents//environments//sessions/&#x60;. If &#x60;Environment ID&#x60; is not specified, we assume default &#39;draft&#39; environment. It&#39;s up to the API caller to choose an appropriate &#x60;Session ID&#x60;. It can be a random number or some type of session identifiers (preferably hashed). The length of the &#x60;Session ID&#x60; must not exceed 36 characters. For more information, see the [sessions guide](https://cloud.google.com/dialogflow/cx/docs/concept/session). | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudDialogflowCxV3MatchIntentRequest** | [**GoogleCloudDialogflowCxV3MatchIntentRequest**](GoogleCloudDialogflowCxV3MatchIntentRequest.md)|  | [optional] 

### Return type

[**GoogleCloudDialogflowCxV3MatchIntentResponse**](GoogleCloudDialogflowCxV3MatchIntentResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dialogflowProjectsLocationsAgentsSessionsServerStreamingDetectIntent

> GoogleCloudDialogflowCxV3DetectIntentResponse dialogflowProjectsLocationsAgentsSessionsServerStreamingDetectIntent(session, opts)



Processes a natural language query and returns structured, actionable data as a result through server-side streaming. Server-side streaming allows Dialogflow to send [partial responses](https://cloud.google.com/dialogflow/cx/docs/concept/fulfillment#partial-response) earlier in a single request.

### Example

```javascript
import DialogflowApi from 'dialogflow_api';
let defaultClient = DialogflowApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DialogflowApi.ProjectsApi();
let session = "session_example"; // String | Required. The name of the session this query is sent to. Format: `projects//locations//agents//sessions/` or `projects//locations//agents//environments//sessions/`. If `Environment ID` is not specified, we assume default 'draft' environment. It's up to the API caller to choose an appropriate `Session ID`. It can be a random number or some type of session identifiers (preferably hashed). The length of the `Session ID` must not exceed 36 characters. For more information, see the [sessions guide](https://cloud.google.com/dialogflow/cx/docs/concept/session). Note: Always use agent versions for production traffic. See [Versions and environments](https://cloud.google.com/dialogflow/cx/docs/concept/version).
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudDialogflowCxV3DetectIntentRequest': new DialogflowApi.GoogleCloudDialogflowCxV3DetectIntentRequest() // GoogleCloudDialogflowCxV3DetectIntentRequest | 
};
apiInstance.dialogflowProjectsLocationsAgentsSessionsServerStreamingDetectIntent(session, opts, (error, data, response) => {
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
 **session** | **String**| Required. The name of the session this query is sent to. Format: &#x60;projects//locations//agents//sessions/&#x60; or &#x60;projects//locations//agents//environments//sessions/&#x60;. If &#x60;Environment ID&#x60; is not specified, we assume default &#39;draft&#39; environment. It&#39;s up to the API caller to choose an appropriate &#x60;Session ID&#x60;. It can be a random number or some type of session identifiers (preferably hashed). The length of the &#x60;Session ID&#x60; must not exceed 36 characters. For more information, see the [sessions guide](https://cloud.google.com/dialogflow/cx/docs/concept/session). Note: Always use agent versions for production traffic. See [Versions and environments](https://cloud.google.com/dialogflow/cx/docs/concept/version). | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudDialogflowCxV3DetectIntentRequest** | [**GoogleCloudDialogflowCxV3DetectIntentRequest**](GoogleCloudDialogflowCxV3DetectIntentRequest.md)|  | [optional] 

### Return type

[**GoogleCloudDialogflowCxV3DetectIntentResponse**](GoogleCloudDialogflowCxV3DetectIntentResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dialogflowProjectsLocationsAgentsSessionsSubmitAnswerFeedback

> GoogleCloudDialogflowCxV3AnswerFeedback dialogflowProjectsLocationsAgentsSessionsSubmitAnswerFeedback(session, opts)



Updates the feedback received from the user for a single turn of the bot response.

### Example

```javascript
import DialogflowApi from 'dialogflow_api';
let defaultClient = DialogflowApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DialogflowApi.ProjectsApi();
let session = "session_example"; // String | Required. The name of the session the feedback was sent to.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudDialogflowCxV3SubmitAnswerFeedbackRequest': new DialogflowApi.GoogleCloudDialogflowCxV3SubmitAnswerFeedbackRequest() // GoogleCloudDialogflowCxV3SubmitAnswerFeedbackRequest | 
};
apiInstance.dialogflowProjectsLocationsAgentsSessionsSubmitAnswerFeedback(session, opts, (error, data, response) => {
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
 **session** | **String**| Required. The name of the session the feedback was sent to. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudDialogflowCxV3SubmitAnswerFeedbackRequest** | [**GoogleCloudDialogflowCxV3SubmitAnswerFeedbackRequest**](GoogleCloudDialogflowCxV3SubmitAnswerFeedbackRequest.md)|  | [optional] 

### Return type

[**GoogleCloudDialogflowCxV3AnswerFeedback**](GoogleCloudDialogflowCxV3AnswerFeedback.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dialogflowProjectsLocationsAgentsTestCasesBatchDelete

> Object dialogflowProjectsLocationsAgentsTestCasesBatchDelete(parent, opts)



Batch deletes test cases.

### Example

```javascript
import DialogflowApi from 'dialogflow_api';
let defaultClient = DialogflowApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DialogflowApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The agent to delete test cases from. Format: `projects//locations//agents/`.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudDialogflowCxV3BatchDeleteTestCasesRequest': new DialogflowApi.GoogleCloudDialogflowCxV3BatchDeleteTestCasesRequest() // GoogleCloudDialogflowCxV3BatchDeleteTestCasesRequest | 
};
apiInstance.dialogflowProjectsLocationsAgentsTestCasesBatchDelete(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The agent to delete test cases from. Format: &#x60;projects//locations//agents/&#x60;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudDialogflowCxV3BatchDeleteTestCasesRequest** | [**GoogleCloudDialogflowCxV3BatchDeleteTestCasesRequest**](GoogleCloudDialogflowCxV3BatchDeleteTestCasesRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dialogflowProjectsLocationsAgentsTestCasesBatchRun

> GoogleLongrunningOperation dialogflowProjectsLocationsAgentsTestCasesBatchRun(parent, opts)



Kicks off a batch run of test cases. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned &#x60;Operation&#x60; type has the following method-specific fields: - &#x60;metadata&#x60;: BatchRunTestCasesMetadata - &#x60;response&#x60;: BatchRunTestCasesResponse

### Example

```javascript
import DialogflowApi from 'dialogflow_api';
let defaultClient = DialogflowApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DialogflowApi.ProjectsApi();
let parent = "parent_example"; // String | Required. Agent name. Format: `projects//locations//agents/ `.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudDialogflowCxV3BatchRunTestCasesRequest': new DialogflowApi.GoogleCloudDialogflowCxV3BatchRunTestCasesRequest() // GoogleCloudDialogflowCxV3BatchRunTestCasesRequest | 
};
apiInstance.dialogflowProjectsLocationsAgentsTestCasesBatchRun(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. Agent name. Format: &#x60;projects//locations//agents/ &#x60;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudDialogflowCxV3BatchRunTestCasesRequest** | [**GoogleCloudDialogflowCxV3BatchRunTestCasesRequest**](GoogleCloudDialogflowCxV3BatchRunTestCasesRequest.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dialogflowProjectsLocationsAgentsTestCasesCalculateCoverage

> GoogleCloudDialogflowCxV3CalculateCoverageResponse dialogflowProjectsLocationsAgentsTestCasesCalculateCoverage(agent, opts)



Calculates the test coverage for an agent.

### Example

```javascript
import DialogflowApi from 'dialogflow_api';
let defaultClient = DialogflowApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DialogflowApi.ProjectsApi();
let agent = "agent_example"; // String | Required. The agent to calculate coverage for. Format: `projects//locations//agents/`.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'type': "type_example" // String | Required. The type of coverage requested.
};
apiInstance.dialogflowProjectsLocationsAgentsTestCasesCalculateCoverage(agent, opts, (error, data, response) => {
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
 **agent** | **String**| Required. The agent to calculate coverage for. Format: &#x60;projects//locations//agents/&#x60;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **type** | **String**| Required. The type of coverage requested. | [optional] 

### Return type

[**GoogleCloudDialogflowCxV3CalculateCoverageResponse**](GoogleCloudDialogflowCxV3CalculateCoverageResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dialogflowProjectsLocationsAgentsTestCasesCreate

> GoogleCloudDialogflowCxV3TestCase dialogflowProjectsLocationsAgentsTestCasesCreate(parent, opts)



Creates a test case for the given agent.

### Example

```javascript
import DialogflowApi from 'dialogflow_api';
let defaultClient = DialogflowApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DialogflowApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The agent to create the test case for. Format: `projects//locations//agents/`.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudDialogflowCxV3TestCase': new DialogflowApi.GoogleCloudDialogflowCxV3TestCase() // GoogleCloudDialogflowCxV3TestCase | 
};
apiInstance.dialogflowProjectsLocationsAgentsTestCasesCreate(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The agent to create the test case for. Format: &#x60;projects//locations//agents/&#x60;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudDialogflowCxV3TestCase** | [**GoogleCloudDialogflowCxV3TestCase**](GoogleCloudDialogflowCxV3TestCase.md)|  | [optional] 

### Return type

[**GoogleCloudDialogflowCxV3TestCase**](GoogleCloudDialogflowCxV3TestCase.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dialogflowProjectsLocationsAgentsTestCasesExport

> GoogleLongrunningOperation dialogflowProjectsLocationsAgentsTestCasesExport(parent, opts)



Exports the test cases under the agent to a Cloud Storage bucket or a local file. Filter can be applied to export a subset of test cases. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned &#x60;Operation&#x60; type has the following method-specific fields: - &#x60;metadata&#x60;: ExportTestCasesMetadata - &#x60;response&#x60;: ExportTestCasesResponse

### Example

```javascript
import DialogflowApi from 'dialogflow_api';
let defaultClient = DialogflowApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DialogflowApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The agent where to export test cases from. Format: `projects//locations//agents/`.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudDialogflowCxV3ExportTestCasesRequest': new DialogflowApi.GoogleCloudDialogflowCxV3ExportTestCasesRequest() // GoogleCloudDialogflowCxV3ExportTestCasesRequest | 
};
apiInstance.dialogflowProjectsLocationsAgentsTestCasesExport(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The agent where to export test cases from. Format: &#x60;projects//locations//agents/&#x60;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudDialogflowCxV3ExportTestCasesRequest** | [**GoogleCloudDialogflowCxV3ExportTestCasesRequest**](GoogleCloudDialogflowCxV3ExportTestCasesRequest.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dialogflowProjectsLocationsAgentsTestCasesImport

> GoogleLongrunningOperation dialogflowProjectsLocationsAgentsTestCasesImport(parent, opts)



Imports the test cases from a Cloud Storage bucket or a local file. It always creates new test cases and won&#39;t overwrite any existing ones. The provided ID in the imported test case is neglected. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned &#x60;Operation&#x60; type has the following method-specific fields: - &#x60;metadata&#x60;: ImportTestCasesMetadata - &#x60;response&#x60;: ImportTestCasesResponse

### Example

```javascript
import DialogflowApi from 'dialogflow_api';
let defaultClient = DialogflowApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DialogflowApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The agent to import test cases to. Format: `projects//locations//agents/`.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudDialogflowCxV3ImportTestCasesRequest': new DialogflowApi.GoogleCloudDialogflowCxV3ImportTestCasesRequest() // GoogleCloudDialogflowCxV3ImportTestCasesRequest | 
};
apiInstance.dialogflowProjectsLocationsAgentsTestCasesImport(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The agent to import test cases to. Format: &#x60;projects//locations//agents/&#x60;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudDialogflowCxV3ImportTestCasesRequest** | [**GoogleCloudDialogflowCxV3ImportTestCasesRequest**](GoogleCloudDialogflowCxV3ImportTestCasesRequest.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dialogflowProjectsLocationsAgentsTestCasesList

> GoogleCloudDialogflowCxV3ListTestCasesResponse dialogflowProjectsLocationsAgentsTestCasesList(parent, opts)



Fetches a list of test cases for a given agent.

### Example

```javascript
import DialogflowApi from 'dialogflow_api';
let defaultClient = DialogflowApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DialogflowApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The agent to list all pages for. Format: `projects//locations//agents/`.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'pageSize': 56, // Number | The maximum number of items to return in a single page. By default 20. Note that when TestCaseView = FULL, the maximum page size allowed is 20. When TestCaseView = BASIC, the maximum page size allowed is 500.
  'pageToken': "pageToken_example", // String | The next_page_token value returned from a previous list request.
  'view': "view_example" // String | Specifies whether response should include all fields or just the metadata.
};
apiInstance.dialogflowProjectsLocationsAgentsTestCasesList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The agent to list all pages for. Format: &#x60;projects//locations//agents/&#x60;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **pageSize** | **Number**| The maximum number of items to return in a single page. By default 20. Note that when TestCaseView &#x3D; FULL, the maximum page size allowed is 20. When TestCaseView &#x3D; BASIC, the maximum page size allowed is 500. | [optional] 
 **pageToken** | **String**| The next_page_token value returned from a previous list request. | [optional] 
 **view** | **String**| Specifies whether response should include all fields or just the metadata. | [optional] 

### Return type

[**GoogleCloudDialogflowCxV3ListTestCasesResponse**](GoogleCloudDialogflowCxV3ListTestCasesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dialogflowProjectsLocationsAgentsTestCasesResultsList

> GoogleCloudDialogflowCxV3ListTestCaseResultsResponse dialogflowProjectsLocationsAgentsTestCasesResultsList(parent, opts)



Fetches the list of run results for the given test case. A maximum of 100 results are kept for each test case.

### Example

```javascript
import DialogflowApi from 'dialogflow_api';
let defaultClient = DialogflowApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DialogflowApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The test case to list results for. Format: `projects//locations//agents// testCases/`. Specify a `-` as a wildcard for TestCase ID to list results across multiple test cases.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | The filter expression used to filter test case results. See [API Filtering](https://aip.dev/160). The expression is case insensitive. Only 'AND' is supported for logical operators. The supported syntax is listed below in detail: [AND ] ... [AND latest] The supported fields and operators are: field operator `environment` `=`, `IN` (Use value `draft` for draft environment) `test_time` `>`, `<` `latest` only returns the latest test result in all results for each test case. Examples: * \"environment=draft AND latest\" matches the latest test result for each test case in the draft environment. * \"environment IN (e1,e2)\" matches any test case results with an environment resource name of either \"e1\" or \"e2\". * \"test_time > 1602540713\" matches any test case results with test time later than a unix timestamp in seconds 1602540713.
  'pageSize': 56, // Number | The maximum number of items to return in a single page. By default 100 and at most 1000.
  'pageToken': "pageToken_example" // String | The next_page_token value returned from a previous list request.
};
apiInstance.dialogflowProjectsLocationsAgentsTestCasesResultsList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The test case to list results for. Format: &#x60;projects//locations//agents// testCases/&#x60;. Specify a &#x60;-&#x60; as a wildcard for TestCase ID to list results across multiple test cases. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| The filter expression used to filter test case results. See [API Filtering](https://aip.dev/160). The expression is case insensitive. Only &#39;AND&#39; is supported for logical operators. The supported syntax is listed below in detail: [AND ] ... [AND latest] The supported fields and operators are: field operator &#x60;environment&#x60; &#x60;&#x3D;&#x60;, &#x60;IN&#x60; (Use value &#x60;draft&#x60; for draft environment) &#x60;test_time&#x60; &#x60;&gt;&#x60;, &#x60;&lt;&#x60; &#x60;latest&#x60; only returns the latest test result in all results for each test case. Examples: * \&quot;environment&#x3D;draft AND latest\&quot; matches the latest test result for each test case in the draft environment. * \&quot;environment IN (e1,e2)\&quot; matches any test case results with an environment resource name of either \&quot;e1\&quot; or \&quot;e2\&quot;. * \&quot;test_time &gt; 1602540713\&quot; matches any test case results with test time later than a unix timestamp in seconds 1602540713. | [optional] 
 **pageSize** | **Number**| The maximum number of items to return in a single page. By default 100 and at most 1000. | [optional] 
 **pageToken** | **String**| The next_page_token value returned from a previous list request. | [optional] 

### Return type

[**GoogleCloudDialogflowCxV3ListTestCaseResultsResponse**](GoogleCloudDialogflowCxV3ListTestCaseResultsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dialogflowProjectsLocationsAgentsTestCasesRun

> GoogleLongrunningOperation dialogflowProjectsLocationsAgentsTestCasesRun(name, opts)



Kicks off a test case run. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned &#x60;Operation&#x60; type has the following method-specific fields: - &#x60;metadata&#x60;: RunTestCaseMetadata - &#x60;response&#x60;: RunTestCaseResponse

### Example

```javascript
import DialogflowApi from 'dialogflow_api';
let defaultClient = DialogflowApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DialogflowApi.ProjectsApi();
let name = "name_example"; // String | Required. Format of test case name to run: `projects//locations/ /agents//testCases/`.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudDialogflowCxV3RunTestCaseRequest': new DialogflowApi.GoogleCloudDialogflowCxV3RunTestCaseRequest() // GoogleCloudDialogflowCxV3RunTestCaseRequest | 
};
apiInstance.dialogflowProjectsLocationsAgentsTestCasesRun(name, opts, (error, data, response) => {
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
 **name** | **String**| Required. Format of test case name to run: &#x60;projects//locations/ /agents//testCases/&#x60;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudDialogflowCxV3RunTestCaseRequest** | [**GoogleCloudDialogflowCxV3RunTestCaseRequest**](GoogleCloudDialogflowCxV3RunTestCaseRequest.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dialogflowProjectsLocationsAgentsTransitionRouteGroupsCreate

> GoogleCloudDialogflowCxV3TransitionRouteGroup dialogflowProjectsLocationsAgentsTransitionRouteGroupsCreate(parent, opts)



Creates an TransitionRouteGroup in the specified flow. Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

### Example

```javascript
import DialogflowApi from 'dialogflow_api';
let defaultClient = DialogflowApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DialogflowApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The flow to create an TransitionRouteGroup for. Format: `projects//locations//agents//flows/` or `projects//locations//agents/` for agent-level groups.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'languageCode': "languageCode_example", // String | The language of the following fields in `TransitionRouteGroup`: * `TransitionRouteGroup.transition_routes.trigger_fulfillment.messages` * `TransitionRouteGroup.transition_routes.trigger_fulfillment.conditional_cases` If not specified, the agent's default language is used. [Many languages](https://cloud.google.com/dialogflow/cx/docs/reference/language) are supported. Note: languages must be enabled in the agent before they can be used.
  'googleCloudDialogflowCxV3TransitionRouteGroup': new DialogflowApi.GoogleCloudDialogflowCxV3TransitionRouteGroup() // GoogleCloudDialogflowCxV3TransitionRouteGroup | 
};
apiInstance.dialogflowProjectsLocationsAgentsTransitionRouteGroupsCreate(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The flow to create an TransitionRouteGroup for. Format: &#x60;projects//locations//agents//flows/&#x60; or &#x60;projects//locations//agents/&#x60; for agent-level groups. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **languageCode** | **String**| The language of the following fields in &#x60;TransitionRouteGroup&#x60;: * &#x60;TransitionRouteGroup.transition_routes.trigger_fulfillment.messages&#x60; * &#x60;TransitionRouteGroup.transition_routes.trigger_fulfillment.conditional_cases&#x60; If not specified, the agent&#39;s default language is used. [Many languages](https://cloud.google.com/dialogflow/cx/docs/reference/language) are supported. Note: languages must be enabled in the agent before they can be used. | [optional] 
 **googleCloudDialogflowCxV3TransitionRouteGroup** | [**GoogleCloudDialogflowCxV3TransitionRouteGroup**](GoogleCloudDialogflowCxV3TransitionRouteGroup.md)|  | [optional] 

### Return type

[**GoogleCloudDialogflowCxV3TransitionRouteGroup**](GoogleCloudDialogflowCxV3TransitionRouteGroup.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dialogflowProjectsLocationsAgentsTransitionRouteGroupsList

> GoogleCloudDialogflowCxV3ListTransitionRouteGroupsResponse dialogflowProjectsLocationsAgentsTransitionRouteGroupsList(parent, opts)



Returns the list of all transition route groups in the specified flow.

### Example

```javascript
import DialogflowApi from 'dialogflow_api';
let defaultClient = DialogflowApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DialogflowApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The flow to list all transition route groups for. Format: `projects//locations//agents//flows/` or `projects//locations//agents/.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'languageCode': "languageCode_example", // String | The language to list transition route groups for. The following fields are language dependent: * `TransitionRouteGroup.transition_routes.trigger_fulfillment.messages` * `TransitionRouteGroup.transition_routes.trigger_fulfillment.conditional_cases` If not specified, the agent's default language is used. [Many languages](https://cloud.google.com/dialogflow/cx/docs/reference/language) are supported. Note: languages must be enabled in the agent before they can be used.
  'pageSize': 56, // Number | The maximum number of items to return in a single page. By default 100 and at most 1000.
  'pageToken': "pageToken_example" // String | The next_page_token value returned from a previous list request.
};
apiInstance.dialogflowProjectsLocationsAgentsTransitionRouteGroupsList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The flow to list all transition route groups for. Format: &#x60;projects//locations//agents//flows/&#x60; or &#x60;projects//locations//agents/. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **languageCode** | **String**| The language to list transition route groups for. The following fields are language dependent: * &#x60;TransitionRouteGroup.transition_routes.trigger_fulfillment.messages&#x60; * &#x60;TransitionRouteGroup.transition_routes.trigger_fulfillment.conditional_cases&#x60; If not specified, the agent&#39;s default language is used. [Many languages](https://cloud.google.com/dialogflow/cx/docs/reference/language) are supported. Note: languages must be enabled in the agent before they can be used. | [optional] 
 **pageSize** | **Number**| The maximum number of items to return in a single page. By default 100 and at most 1000. | [optional] 
 **pageToken** | **String**| The next_page_token value returned from a previous list request. | [optional] 

### Return type

[**GoogleCloudDialogflowCxV3ListTransitionRouteGroupsResponse**](GoogleCloudDialogflowCxV3ListTransitionRouteGroupsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dialogflowProjectsLocationsAgentsWebhooksCreate

> GoogleCloudDialogflowCxV3Webhook dialogflowProjectsLocationsAgentsWebhooksCreate(parent, opts)



Creates a webhook in the specified agent.

### Example

```javascript
import DialogflowApi from 'dialogflow_api';
let defaultClient = DialogflowApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DialogflowApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The agent to create a webhook for. Format: `projects//locations//agents/`.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudDialogflowCxV3Webhook': new DialogflowApi.GoogleCloudDialogflowCxV3Webhook() // GoogleCloudDialogflowCxV3Webhook | 
};
apiInstance.dialogflowProjectsLocationsAgentsWebhooksCreate(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The agent to create a webhook for. Format: &#x60;projects//locations//agents/&#x60;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudDialogflowCxV3Webhook** | [**GoogleCloudDialogflowCxV3Webhook**](GoogleCloudDialogflowCxV3Webhook.md)|  | [optional] 

### Return type

[**GoogleCloudDialogflowCxV3Webhook**](GoogleCloudDialogflowCxV3Webhook.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dialogflowProjectsLocationsAgentsWebhooksList

> GoogleCloudDialogflowCxV3ListWebhooksResponse dialogflowProjectsLocationsAgentsWebhooksList(parent, opts)



Returns the list of all webhooks in the specified agent.

### Example

```javascript
import DialogflowApi from 'dialogflow_api';
let defaultClient = DialogflowApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DialogflowApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The agent to list all webhooks for. Format: `projects//locations//agents/`.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'pageSize': 56, // Number | The maximum number of items to return in a single page. By default 100 and at most 1000.
  'pageToken': "pageToken_example" // String | The next_page_token value returned from a previous list request.
};
apiInstance.dialogflowProjectsLocationsAgentsWebhooksList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The agent to list all webhooks for. Format: &#x60;projects//locations//agents/&#x60;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **pageSize** | **Number**| The maximum number of items to return in a single page. By default 100 and at most 1000. | [optional] 
 **pageToken** | **String**| The next_page_token value returned from a previous list request. | [optional] 

### Return type

[**GoogleCloudDialogflowCxV3ListWebhooksResponse**](GoogleCloudDialogflowCxV3ListWebhooksResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dialogflowProjectsLocationsList

> GoogleCloudLocationListLocationsResponse dialogflowProjectsLocationsList(name, opts)



Lists information about the supported locations for this service.

### Example

```javascript
import DialogflowApi from 'dialogflow_api';
let defaultClient = DialogflowApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DialogflowApi.ProjectsApi();
let name = "name_example"; // String | The resource that owns the locations collection, if applicable.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | A filter to narrow down results to a preferred subset. The filtering language accepts strings like `\"displayName=tokyo\"`, and is documented in more detail in [AIP-160](https://google.aip.dev/160).
  'pageSize': 56, // Number | The maximum number of results to return. If not set, the service selects a default.
  'pageToken': "pageToken_example" // String | A page token received from the `next_page_token` field in the response. Send that page token to receive the subsequent page.
};
apiInstance.dialogflowProjectsLocationsList(name, opts, (error, data, response) => {
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
 **name** | **String**| The resource that owns the locations collection, if applicable. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| A filter to narrow down results to a preferred subset. The filtering language accepts strings like &#x60;\&quot;displayName&#x3D;tokyo\&quot;&#x60;, and is documented in more detail in [AIP-160](https://google.aip.dev/160). | [optional] 
 **pageSize** | **Number**| The maximum number of results to return. If not set, the service selects a default. | [optional] 
 **pageToken** | **String**| A page token received from the &#x60;next_page_token&#x60; field in the response. Send that page token to receive the subsequent page. | [optional] 

### Return type

[**GoogleCloudLocationListLocationsResponse**](GoogleCloudLocationListLocationsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dialogflowProjectsLocationsSecuritySettingsCreate

> GoogleCloudDialogflowCxV3SecuritySettings dialogflowProjectsLocationsSecuritySettingsCreate(parent, opts)



Create security settings in the specified location.

### Example

```javascript
import DialogflowApi from 'dialogflow_api';
let defaultClient = DialogflowApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DialogflowApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The location to create an SecuritySettings for. Format: `projects//locations/`.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleCloudDialogflowCxV3SecuritySettings': new DialogflowApi.GoogleCloudDialogflowCxV3SecuritySettings() // GoogleCloudDialogflowCxV3SecuritySettings | 
};
apiInstance.dialogflowProjectsLocationsSecuritySettingsCreate(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The location to create an SecuritySettings for. Format: &#x60;projects//locations/&#x60;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleCloudDialogflowCxV3SecuritySettings** | [**GoogleCloudDialogflowCxV3SecuritySettings**](GoogleCloudDialogflowCxV3SecuritySettings.md)|  | [optional] 

### Return type

[**GoogleCloudDialogflowCxV3SecuritySettings**](GoogleCloudDialogflowCxV3SecuritySettings.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dialogflowProjectsLocationsSecuritySettingsDelete

> Object dialogflowProjectsLocationsSecuritySettingsDelete(name, opts)



Deletes the specified SecuritySettings.

### Example

```javascript
import DialogflowApi from 'dialogflow_api';
let defaultClient = DialogflowApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DialogflowApi.ProjectsApi();
let name = "name_example"; // String | Required. The name of the SecuritySettings to delete. Format: `projects//locations//securitySettings/`.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'force': true // Boolean | This field has no effect for webhook not being used. For webhooks that are used by pages/flows/transition route groups: * If `force` is set to false, an error will be returned with message indicating the referenced resources. * If `force` is set to true, Dialogflow will remove the webhook, as well as any references to the webhook (i.e. Webhook and tagin fulfillments that point to this webhook will be removed).
};
apiInstance.dialogflowProjectsLocationsSecuritySettingsDelete(name, opts, (error, data, response) => {
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
 **name** | **String**| Required. The name of the SecuritySettings to delete. Format: &#x60;projects//locations//securitySettings/&#x60;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **force** | **Boolean**| This field has no effect for webhook not being used. For webhooks that are used by pages/flows/transition route groups: * If &#x60;force&#x60; is set to false, an error will be returned with message indicating the referenced resources. * If &#x60;force&#x60; is set to true, Dialogflow will remove the webhook, as well as any references to the webhook (i.e. Webhook and tagin fulfillments that point to this webhook will be removed). | [optional] 

### Return type

**Object**

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dialogflowProjectsLocationsSecuritySettingsList

> GoogleCloudDialogflowCxV3ListSecuritySettingsResponse dialogflowProjectsLocationsSecuritySettingsList(parent, opts)



Returns the list of all security settings in the specified location.

### Example

```javascript
import DialogflowApi from 'dialogflow_api';
let defaultClient = DialogflowApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DialogflowApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The location to list all security settings for. Format: `projects//locations/`.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'pageSize': 56, // Number | The maximum number of items to return in a single page. By default 20 and at most 100.
  'pageToken': "pageToken_example" // String | The next_page_token value returned from a previous list request.
};
apiInstance.dialogflowProjectsLocationsSecuritySettingsList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The location to list all security settings for. Format: &#x60;projects//locations/&#x60;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **pageSize** | **Number**| The maximum number of items to return in a single page. By default 20 and at most 100. | [optional] 
 **pageToken** | **String**| The next_page_token value returned from a previous list request. | [optional] 

### Return type

[**GoogleCloudDialogflowCxV3ListSecuritySettingsResponse**](GoogleCloudDialogflowCxV3ListSecuritySettingsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dialogflowProjectsLocationsSecuritySettingsPatch

> GoogleCloudDialogflowCxV3SecuritySettings dialogflowProjectsLocationsSecuritySettingsPatch(name, opts)



Updates the specified SecuritySettings.

### Example

```javascript
import DialogflowApi from 'dialogflow_api';
let defaultClient = DialogflowApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DialogflowApi.ProjectsApi();
let name = "name_example"; // String | Resource name of the settings. Required for the SecuritySettingsService.UpdateSecuritySettings method. SecuritySettingsService.CreateSecuritySettings populates the name automatically. Format: `projects//locations//securitySettings/`.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'updateMask': "updateMask_example", // String | Required. The mask to control which fields get updated. If the mask is not present, all fields will be updated.
  'googleCloudDialogflowCxV3SecuritySettings': new DialogflowApi.GoogleCloudDialogflowCxV3SecuritySettings() // GoogleCloudDialogflowCxV3SecuritySettings | 
};
apiInstance.dialogflowProjectsLocationsSecuritySettingsPatch(name, opts, (error, data, response) => {
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
 **name** | **String**| Resource name of the settings. Required for the SecuritySettingsService.UpdateSecuritySettings method. SecuritySettingsService.CreateSecuritySettings populates the name automatically. Format: &#x60;projects//locations//securitySettings/&#x60;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **updateMask** | **String**| Required. The mask to control which fields get updated. If the mask is not present, all fields will be updated. | [optional] 
 **googleCloudDialogflowCxV3SecuritySettings** | [**GoogleCloudDialogflowCxV3SecuritySettings**](GoogleCloudDialogflowCxV3SecuritySettings.md)|  | [optional] 

### Return type

[**GoogleCloudDialogflowCxV3SecuritySettings**](GoogleCloudDialogflowCxV3SecuritySettings.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dialogflowProjectsOperationsCancel

> Object dialogflowProjectsOperationsCancel(name, opts)



Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn&#39;t support this method, it returns &#x60;google.rpc.Code.UNIMPLEMENTED&#x60;. Clients can use Operations.GetOperation or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an Operation.error value with a google.rpc.Status.code of 1, corresponding to &#x60;Code.CANCELLED&#x60;.

### Example

```javascript
import DialogflowApi from 'dialogflow_api';
let defaultClient = DialogflowApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DialogflowApi.ProjectsApi();
let name = "name_example"; // String | The name of the operation resource to be cancelled.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example" // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
};
apiInstance.dialogflowProjectsOperationsCancel(name, opts, (error, data, response) => {
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
 **name** | **String**| The name of the operation resource to be cancelled. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 

### Return type

**Object**

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dialogflowProjectsOperationsGet

> GoogleLongrunningOperation dialogflowProjectsOperationsGet(name, opts)



Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

### Example

```javascript
import DialogflowApi from 'dialogflow_api';
let defaultClient = DialogflowApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DialogflowApi.ProjectsApi();
let name = "name_example"; // String | The name of the operation resource.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'languageCode': "languageCode_example" // String | The language to retrieve the transition route group for. The following fields are language dependent: * `TransitionRouteGroup.transition_routes.trigger_fulfillment.messages` * `TransitionRouteGroup.transition_routes.trigger_fulfillment.conditional_cases` If not specified, the agent's default language is used. [Many languages](https://cloud.google.com/dialogflow/cx/docs/reference/language) are supported. Note: languages must be enabled in the agent before they can be used.
};
apiInstance.dialogflowProjectsOperationsGet(name, opts, (error, data, response) => {
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
 **name** | **String**| The name of the operation resource. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **languageCode** | **String**| The language to retrieve the transition route group for. The following fields are language dependent: * &#x60;TransitionRouteGroup.transition_routes.trigger_fulfillment.messages&#x60; * &#x60;TransitionRouteGroup.transition_routes.trigger_fulfillment.conditional_cases&#x60; If not specified, the agent&#39;s default language is used. [Many languages](https://cloud.google.com/dialogflow/cx/docs/reference/language) are supported. Note: languages must be enabled in the agent before they can be used. | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dialogflowProjectsOperationsList

> GoogleLongrunningListOperationsResponse dialogflowProjectsOperationsList(name, opts)



Lists operations that match the specified filter in the request. If the server doesn&#39;t support this method, it returns &#x60;UNIMPLEMENTED&#x60;.

### Example

```javascript
import DialogflowApi from 'dialogflow_api';
let defaultClient = DialogflowApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DialogflowApi.ProjectsApi();
let name = "name_example"; // String | The name of the operation's parent resource.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | The standard list filter.
  'pageSize': 56, // Number | The standard list page size.
  'pageToken': "pageToken_example" // String | The standard list page token.
};
apiInstance.dialogflowProjectsOperationsList(name, opts, (error, data, response) => {
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
 **name** | **String**| The name of the operation&#39;s parent resource. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| The standard list filter. | [optional] 
 **pageSize** | **Number**| The standard list page size. | [optional] 
 **pageToken** | **String**| The standard list page token. | [optional] 

### Return type

[**GoogleLongrunningListOperationsResponse**](GoogleLongrunningListOperationsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

