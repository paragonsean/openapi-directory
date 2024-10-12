# ProjectsApi

All URIs are relative to *https://dialogflow.googleapis.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**dialogflowProjectsLocationsAgentsChangelogsList**](ProjectsApi.md#dialogflowProjectsLocationsAgentsChangelogsList) | **GET** /v3/{parent}/changelogs |  |
| [**dialogflowProjectsLocationsAgentsCreate**](ProjectsApi.md#dialogflowProjectsLocationsAgentsCreate) | **POST** /v3/{parent}/agents |  |
| [**dialogflowProjectsLocationsAgentsEntityTypesExport**](ProjectsApi.md#dialogflowProjectsLocationsAgentsEntityTypesExport) | **POST** /v3/{parent}/entityTypes:export |  |
| [**dialogflowProjectsLocationsAgentsEntityTypesImport**](ProjectsApi.md#dialogflowProjectsLocationsAgentsEntityTypesImport) | **POST** /v3/{parent}/entityTypes:import |  |
| [**dialogflowProjectsLocationsAgentsEnvironmentsContinuousTestResultsList**](ProjectsApi.md#dialogflowProjectsLocationsAgentsEnvironmentsContinuousTestResultsList) | **GET** /v3/{parent}/continuousTestResults |  |
| [**dialogflowProjectsLocationsAgentsEnvironmentsCreate**](ProjectsApi.md#dialogflowProjectsLocationsAgentsEnvironmentsCreate) | **POST** /v3/{parent}/environments |  |
| [**dialogflowProjectsLocationsAgentsEnvironmentsDeployFlow**](ProjectsApi.md#dialogflowProjectsLocationsAgentsEnvironmentsDeployFlow) | **POST** /v3/{environment}:deployFlow |  |
| [**dialogflowProjectsLocationsAgentsEnvironmentsDeploymentsList**](ProjectsApi.md#dialogflowProjectsLocationsAgentsEnvironmentsDeploymentsList) | **GET** /v3/{parent}/deployments |  |
| [**dialogflowProjectsLocationsAgentsEnvironmentsExperimentsCreate**](ProjectsApi.md#dialogflowProjectsLocationsAgentsEnvironmentsExperimentsCreate) | **POST** /v3/{parent}/experiments |  |
| [**dialogflowProjectsLocationsAgentsEnvironmentsExperimentsList**](ProjectsApi.md#dialogflowProjectsLocationsAgentsEnvironmentsExperimentsList) | **GET** /v3/{parent}/experiments |  |
| [**dialogflowProjectsLocationsAgentsEnvironmentsExperimentsStart**](ProjectsApi.md#dialogflowProjectsLocationsAgentsEnvironmentsExperimentsStart) | **POST** /v3/{name}:start |  |
| [**dialogflowProjectsLocationsAgentsEnvironmentsExperimentsStop**](ProjectsApi.md#dialogflowProjectsLocationsAgentsEnvironmentsExperimentsStop) | **POST** /v3/{name}:stop |  |
| [**dialogflowProjectsLocationsAgentsEnvironmentsList**](ProjectsApi.md#dialogflowProjectsLocationsAgentsEnvironmentsList) | **GET** /v3/{parent}/environments |  |
| [**dialogflowProjectsLocationsAgentsEnvironmentsLookupEnvironmentHistory**](ProjectsApi.md#dialogflowProjectsLocationsAgentsEnvironmentsLookupEnvironmentHistory) | **GET** /v3/{name}:lookupEnvironmentHistory |  |
| [**dialogflowProjectsLocationsAgentsEnvironmentsRunContinuousTest**](ProjectsApi.md#dialogflowProjectsLocationsAgentsEnvironmentsRunContinuousTest) | **POST** /v3/{environment}:runContinuousTest |  |
| [**dialogflowProjectsLocationsAgentsFlowsCreate**](ProjectsApi.md#dialogflowProjectsLocationsAgentsFlowsCreate) | **POST** /v3/{parent}/flows |  |
| [**dialogflowProjectsLocationsAgentsFlowsExport**](ProjectsApi.md#dialogflowProjectsLocationsAgentsFlowsExport) | **POST** /v3/{name}:export |  |
| [**dialogflowProjectsLocationsAgentsFlowsImport**](ProjectsApi.md#dialogflowProjectsLocationsAgentsFlowsImport) | **POST** /v3/{parent}/flows:import |  |
| [**dialogflowProjectsLocationsAgentsFlowsList**](ProjectsApi.md#dialogflowProjectsLocationsAgentsFlowsList) | **GET** /v3/{parent}/flows |  |
| [**dialogflowProjectsLocationsAgentsFlowsPagesCreate**](ProjectsApi.md#dialogflowProjectsLocationsAgentsFlowsPagesCreate) | **POST** /v3/{parent}/pages |  |
| [**dialogflowProjectsLocationsAgentsFlowsPagesList**](ProjectsApi.md#dialogflowProjectsLocationsAgentsFlowsPagesList) | **GET** /v3/{parent}/pages |  |
| [**dialogflowProjectsLocationsAgentsFlowsTrain**](ProjectsApi.md#dialogflowProjectsLocationsAgentsFlowsTrain) | **POST** /v3/{name}:train |  |
| [**dialogflowProjectsLocationsAgentsFlowsValidate**](ProjectsApi.md#dialogflowProjectsLocationsAgentsFlowsValidate) | **POST** /v3/{name}:validate |  |
| [**dialogflowProjectsLocationsAgentsFlowsVersionsCompareVersions**](ProjectsApi.md#dialogflowProjectsLocationsAgentsFlowsVersionsCompareVersions) | **POST** /v3/{baseVersion}:compareVersions |  |
| [**dialogflowProjectsLocationsAgentsFlowsVersionsCreate**](ProjectsApi.md#dialogflowProjectsLocationsAgentsFlowsVersionsCreate) | **POST** /v3/{parent}/versions |  |
| [**dialogflowProjectsLocationsAgentsFlowsVersionsList**](ProjectsApi.md#dialogflowProjectsLocationsAgentsFlowsVersionsList) | **GET** /v3/{parent}/versions |  |
| [**dialogflowProjectsLocationsAgentsFlowsVersionsLoad**](ProjectsApi.md#dialogflowProjectsLocationsAgentsFlowsVersionsLoad) | **POST** /v3/{name}:load |  |
| [**dialogflowProjectsLocationsAgentsGeneratorsCreate**](ProjectsApi.md#dialogflowProjectsLocationsAgentsGeneratorsCreate) | **POST** /v3/{parent}/generators |  |
| [**dialogflowProjectsLocationsAgentsGeneratorsList**](ProjectsApi.md#dialogflowProjectsLocationsAgentsGeneratorsList) | **GET** /v3/{parent}/generators |  |
| [**dialogflowProjectsLocationsAgentsIntentsCreate**](ProjectsApi.md#dialogflowProjectsLocationsAgentsIntentsCreate) | **POST** /v3/{parent}/intents |  |
| [**dialogflowProjectsLocationsAgentsIntentsExport**](ProjectsApi.md#dialogflowProjectsLocationsAgentsIntentsExport) | **POST** /v3/{parent}/intents:export |  |
| [**dialogflowProjectsLocationsAgentsIntentsImport**](ProjectsApi.md#dialogflowProjectsLocationsAgentsIntentsImport) | **POST** /v3/{parent}/intents:import |  |
| [**dialogflowProjectsLocationsAgentsIntentsList**](ProjectsApi.md#dialogflowProjectsLocationsAgentsIntentsList) | **GET** /v3/{parent}/intents |  |
| [**dialogflowProjectsLocationsAgentsList**](ProjectsApi.md#dialogflowProjectsLocationsAgentsList) | **GET** /v3/{parent}/agents |  |
| [**dialogflowProjectsLocationsAgentsRestore**](ProjectsApi.md#dialogflowProjectsLocationsAgentsRestore) | **POST** /v3/{name}:restore |  |
| [**dialogflowProjectsLocationsAgentsSessionsDetectIntent**](ProjectsApi.md#dialogflowProjectsLocationsAgentsSessionsDetectIntent) | **POST** /v3/{session}:detectIntent |  |
| [**dialogflowProjectsLocationsAgentsSessionsEntityTypesCreate**](ProjectsApi.md#dialogflowProjectsLocationsAgentsSessionsEntityTypesCreate) | **POST** /v3/{parent}/entityTypes |  |
| [**dialogflowProjectsLocationsAgentsSessionsEntityTypesList**](ProjectsApi.md#dialogflowProjectsLocationsAgentsSessionsEntityTypesList) | **GET** /v3/{parent}/entityTypes |  |
| [**dialogflowProjectsLocationsAgentsSessionsFulfillIntent**](ProjectsApi.md#dialogflowProjectsLocationsAgentsSessionsFulfillIntent) | **POST** /v3/{session}:fulfillIntent |  |
| [**dialogflowProjectsLocationsAgentsSessionsMatchIntent**](ProjectsApi.md#dialogflowProjectsLocationsAgentsSessionsMatchIntent) | **POST** /v3/{session}:matchIntent |  |
| [**dialogflowProjectsLocationsAgentsSessionsServerStreamingDetectIntent**](ProjectsApi.md#dialogflowProjectsLocationsAgentsSessionsServerStreamingDetectIntent) | **POST** /v3/{session}:serverStreamingDetectIntent |  |
| [**dialogflowProjectsLocationsAgentsSessionsSubmitAnswerFeedback**](ProjectsApi.md#dialogflowProjectsLocationsAgentsSessionsSubmitAnswerFeedback) | **POST** /v3/{session}:submitAnswerFeedback |  |
| [**dialogflowProjectsLocationsAgentsTestCasesBatchDelete**](ProjectsApi.md#dialogflowProjectsLocationsAgentsTestCasesBatchDelete) | **POST** /v3/{parent}/testCases:batchDelete |  |
| [**dialogflowProjectsLocationsAgentsTestCasesBatchRun**](ProjectsApi.md#dialogflowProjectsLocationsAgentsTestCasesBatchRun) | **POST** /v3/{parent}/testCases:batchRun |  |
| [**dialogflowProjectsLocationsAgentsTestCasesCalculateCoverage**](ProjectsApi.md#dialogflowProjectsLocationsAgentsTestCasesCalculateCoverage) | **GET** /v3/{agent}/testCases:calculateCoverage |  |
| [**dialogflowProjectsLocationsAgentsTestCasesCreate**](ProjectsApi.md#dialogflowProjectsLocationsAgentsTestCasesCreate) | **POST** /v3/{parent}/testCases |  |
| [**dialogflowProjectsLocationsAgentsTestCasesExport**](ProjectsApi.md#dialogflowProjectsLocationsAgentsTestCasesExport) | **POST** /v3/{parent}/testCases:export |  |
| [**dialogflowProjectsLocationsAgentsTestCasesImport**](ProjectsApi.md#dialogflowProjectsLocationsAgentsTestCasesImport) | **POST** /v3/{parent}/testCases:import |  |
| [**dialogflowProjectsLocationsAgentsTestCasesList**](ProjectsApi.md#dialogflowProjectsLocationsAgentsTestCasesList) | **GET** /v3/{parent}/testCases |  |
| [**dialogflowProjectsLocationsAgentsTestCasesResultsList**](ProjectsApi.md#dialogflowProjectsLocationsAgentsTestCasesResultsList) | **GET** /v3/{parent}/results |  |
| [**dialogflowProjectsLocationsAgentsTestCasesRun**](ProjectsApi.md#dialogflowProjectsLocationsAgentsTestCasesRun) | **POST** /v3/{name}:run |  |
| [**dialogflowProjectsLocationsAgentsTransitionRouteGroupsCreate**](ProjectsApi.md#dialogflowProjectsLocationsAgentsTransitionRouteGroupsCreate) | **POST** /v3/{parent}/transitionRouteGroups |  |
| [**dialogflowProjectsLocationsAgentsTransitionRouteGroupsList**](ProjectsApi.md#dialogflowProjectsLocationsAgentsTransitionRouteGroupsList) | **GET** /v3/{parent}/transitionRouteGroups |  |
| [**dialogflowProjectsLocationsAgentsWebhooksCreate**](ProjectsApi.md#dialogflowProjectsLocationsAgentsWebhooksCreate) | **POST** /v3/{parent}/webhooks |  |
| [**dialogflowProjectsLocationsAgentsWebhooksList**](ProjectsApi.md#dialogflowProjectsLocationsAgentsWebhooksList) | **GET** /v3/{parent}/webhooks |  |
| [**dialogflowProjectsLocationsList**](ProjectsApi.md#dialogflowProjectsLocationsList) | **GET** /v3/{name}/locations |  |
| [**dialogflowProjectsLocationsSecuritySettingsCreate**](ProjectsApi.md#dialogflowProjectsLocationsSecuritySettingsCreate) | **POST** /v3/{parent}/securitySettings |  |
| [**dialogflowProjectsLocationsSecuritySettingsDelete**](ProjectsApi.md#dialogflowProjectsLocationsSecuritySettingsDelete) | **DELETE** /v3/{name} |  |
| [**dialogflowProjectsLocationsSecuritySettingsList**](ProjectsApi.md#dialogflowProjectsLocationsSecuritySettingsList) | **GET** /v3/{parent}/securitySettings |  |
| [**dialogflowProjectsLocationsSecuritySettingsPatch**](ProjectsApi.md#dialogflowProjectsLocationsSecuritySettingsPatch) | **PATCH** /v3/{name} |  |
| [**dialogflowProjectsOperationsCancel**](ProjectsApi.md#dialogflowProjectsOperationsCancel) | **POST** /v3/{name}:cancel |  |
| [**dialogflowProjectsOperationsGet**](ProjectsApi.md#dialogflowProjectsOperationsGet) | **GET** /v3/{name} |  |
| [**dialogflowProjectsOperationsList**](ProjectsApi.md#dialogflowProjectsOperationsList) | **GET** /v3/{name}/operations |  |


<a id="dialogflowProjectsLocationsAgentsChangelogsList"></a>
# **dialogflowProjectsLocationsAgentsChangelogsList**
> GoogleCloudDialogflowCxV3ListChangelogsResponse dialogflowProjectsLocationsAgentsChangelogsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, filter, pageSize, pageToken)



Returns the list of Changelogs.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dialogflow.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The agent containing the changelogs. Format: `projects//locations//agents/`.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String filter = "filter_example"; // String | The filter string. Supports filter by user_email, resource, type and create_time. Some examples: 1. By user email: user_email = \"someone@google.com\" 2. By resource name: resource = \"projects/123/locations/global/agents/456/flows/789\" 3. By resource display name: display_name = \"my agent\" 4. By action: action = \"Create\" 5. By type: type = \"flows\" 6. By create time. Currently predicates on `create_time` and `create_time_epoch_seconds` are supported: create_time_epoch_seconds > 1551790877 AND create_time <= 2017-01-15T01:30:15.01Z 7. Combination of above filters: resource = \"projects/123/locations/global/agents/456/flows/789\" AND user_email = \"someone@google.com\" AND create_time <= 2017-01-15T01:30:15.01Z
    Integer pageSize = 56; // Integer | The maximum number of items to return in a single page. By default 100 and at most 1000.
    String pageToken = "pageToken_example"; // String | The next_page_token value returned from a previous list request.
    try {
      GoogleCloudDialogflowCxV3ListChangelogsResponse result = apiInstance.dialogflowProjectsLocationsAgentsChangelogsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, filter, pageSize, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#dialogflowProjectsLocationsAgentsChangelogsList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **parent** | **String**| Required. The agent containing the changelogs. Format: &#x60;projects//locations//agents/&#x60;. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **filter** | **String**| The filter string. Supports filter by user_email, resource, type and create_time. Some examples: 1. By user email: user_email &#x3D; \&quot;someone@google.com\&quot; 2. By resource name: resource &#x3D; \&quot;projects/123/locations/global/agents/456/flows/789\&quot; 3. By resource display name: display_name &#x3D; \&quot;my agent\&quot; 4. By action: action &#x3D; \&quot;Create\&quot; 5. By type: type &#x3D; \&quot;flows\&quot; 6. By create time. Currently predicates on &#x60;create_time&#x60; and &#x60;create_time_epoch_seconds&#x60; are supported: create_time_epoch_seconds &gt; 1551790877 AND create_time &lt;&#x3D; 2017-01-15T01:30:15.01Z 7. Combination of above filters: resource &#x3D; \&quot;projects/123/locations/global/agents/456/flows/789\&quot; AND user_email &#x3D; \&quot;someone@google.com\&quot; AND create_time &lt;&#x3D; 2017-01-15T01:30:15.01Z | [optional] |
| **pageSize** | **Integer**| The maximum number of items to return in a single page. By default 100 and at most 1000. | [optional] |
| **pageToken** | **String**| The next_page_token value returned from a previous list request. | [optional] |

### Return type

[**GoogleCloudDialogflowCxV3ListChangelogsResponse**](GoogleCloudDialogflowCxV3ListChangelogsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dialogflowProjectsLocationsAgentsCreate"></a>
# **dialogflowProjectsLocationsAgentsCreate**
> GoogleCloudDialogflowCxV3Agent dialogflowProjectsLocationsAgentsCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDialogflowCxV3Agent)



Creates an agent in the specified location. Note: You should always train flows prior to sending them queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dialogflow.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The location to create a agent for. Format: `projects//locations/`.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    GoogleCloudDialogflowCxV3Agent googleCloudDialogflowCxV3Agent = new GoogleCloudDialogflowCxV3Agent(); // GoogleCloudDialogflowCxV3Agent | 
    try {
      GoogleCloudDialogflowCxV3Agent result = apiInstance.dialogflowProjectsLocationsAgentsCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDialogflowCxV3Agent);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#dialogflowProjectsLocationsAgentsCreate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **parent** | **String**| Required. The location to create a agent for. Format: &#x60;projects//locations/&#x60;. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **googleCloudDialogflowCxV3Agent** | [**GoogleCloudDialogflowCxV3Agent**](GoogleCloudDialogflowCxV3Agent.md)|  | [optional] |

### Return type

[**GoogleCloudDialogflowCxV3Agent**](GoogleCloudDialogflowCxV3Agent.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dialogflowProjectsLocationsAgentsEntityTypesExport"></a>
# **dialogflowProjectsLocationsAgentsEntityTypesExport**
> GoogleLongrunningOperation dialogflowProjectsLocationsAgentsEntityTypesExport(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDialogflowCxV3ExportEntityTypesRequest)



Exports the selected entity types.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dialogflow.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The name of the parent agent to export entity types. Format: `projects//locations//agents/`.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    GoogleCloudDialogflowCxV3ExportEntityTypesRequest googleCloudDialogflowCxV3ExportEntityTypesRequest = new GoogleCloudDialogflowCxV3ExportEntityTypesRequest(); // GoogleCloudDialogflowCxV3ExportEntityTypesRequest | 
    try {
      GoogleLongrunningOperation result = apiInstance.dialogflowProjectsLocationsAgentsEntityTypesExport(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDialogflowCxV3ExportEntityTypesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#dialogflowProjectsLocationsAgentsEntityTypesExport");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **parent** | **String**| Required. The name of the parent agent to export entity types. Format: &#x60;projects//locations//agents/&#x60;. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **googleCloudDialogflowCxV3ExportEntityTypesRequest** | [**GoogleCloudDialogflowCxV3ExportEntityTypesRequest**](GoogleCloudDialogflowCxV3ExportEntityTypesRequest.md)|  | [optional] |

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dialogflowProjectsLocationsAgentsEntityTypesImport"></a>
# **dialogflowProjectsLocationsAgentsEntityTypesImport**
> GoogleLongrunningOperation dialogflowProjectsLocationsAgentsEntityTypesImport(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDialogflowCxV3ImportEntityTypesRequest)



Imports the specified entitytypes into the agent.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dialogflow.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The agent to import the entity types into. Format: `projects//locations//agents/`.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    GoogleCloudDialogflowCxV3ImportEntityTypesRequest googleCloudDialogflowCxV3ImportEntityTypesRequest = new GoogleCloudDialogflowCxV3ImportEntityTypesRequest(); // GoogleCloudDialogflowCxV3ImportEntityTypesRequest | 
    try {
      GoogleLongrunningOperation result = apiInstance.dialogflowProjectsLocationsAgentsEntityTypesImport(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDialogflowCxV3ImportEntityTypesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#dialogflowProjectsLocationsAgentsEntityTypesImport");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **parent** | **String**| Required. The agent to import the entity types into. Format: &#x60;projects//locations//agents/&#x60;. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **googleCloudDialogflowCxV3ImportEntityTypesRequest** | [**GoogleCloudDialogflowCxV3ImportEntityTypesRequest**](GoogleCloudDialogflowCxV3ImportEntityTypesRequest.md)|  | [optional] |

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dialogflowProjectsLocationsAgentsEnvironmentsContinuousTestResultsList"></a>
# **dialogflowProjectsLocationsAgentsEnvironmentsContinuousTestResultsList**
> GoogleCloudDialogflowCxV3ListContinuousTestResultsResponse dialogflowProjectsLocationsAgentsEnvironmentsContinuousTestResultsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, pageSize, pageToken)



Fetches a list of continuous test results for a given environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dialogflow.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The environment to list results for. Format: `projects//locations//agents// environments/`.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    Integer pageSize = 56; // Integer | The maximum number of items to return in a single page. By default 100 and at most 1000.
    String pageToken = "pageToken_example"; // String | The next_page_token value returned from a previous list request.
    try {
      GoogleCloudDialogflowCxV3ListContinuousTestResultsResponse result = apiInstance.dialogflowProjectsLocationsAgentsEnvironmentsContinuousTestResultsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, pageSize, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#dialogflowProjectsLocationsAgentsEnvironmentsContinuousTestResultsList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **parent** | **String**| Required. The environment to list results for. Format: &#x60;projects//locations//agents// environments/&#x60;. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **pageSize** | **Integer**| The maximum number of items to return in a single page. By default 100 and at most 1000. | [optional] |
| **pageToken** | **String**| The next_page_token value returned from a previous list request. | [optional] |

### Return type

[**GoogleCloudDialogflowCxV3ListContinuousTestResultsResponse**](GoogleCloudDialogflowCxV3ListContinuousTestResultsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dialogflowProjectsLocationsAgentsEnvironmentsCreate"></a>
# **dialogflowProjectsLocationsAgentsEnvironmentsCreate**
> GoogleLongrunningOperation dialogflowProjectsLocationsAgentsEnvironmentsCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDialogflowCxV3Environment)



Creates an Environment in the specified Agent. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned &#x60;Operation&#x60; type has the following method-specific fields: - &#x60;metadata&#x60;: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct) - &#x60;response&#x60;: Environment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dialogflow.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The Agent to create an Environment for. Format: `projects//locations//agents/`.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    GoogleCloudDialogflowCxV3Environment googleCloudDialogflowCxV3Environment = new GoogleCloudDialogflowCxV3Environment(); // GoogleCloudDialogflowCxV3Environment | 
    try {
      GoogleLongrunningOperation result = apiInstance.dialogflowProjectsLocationsAgentsEnvironmentsCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDialogflowCxV3Environment);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#dialogflowProjectsLocationsAgentsEnvironmentsCreate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **parent** | **String**| Required. The Agent to create an Environment for. Format: &#x60;projects//locations//agents/&#x60;. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **googleCloudDialogflowCxV3Environment** | [**GoogleCloudDialogflowCxV3Environment**](GoogleCloudDialogflowCxV3Environment.md)|  | [optional] |

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dialogflowProjectsLocationsAgentsEnvironmentsDeployFlow"></a>
# **dialogflowProjectsLocationsAgentsEnvironmentsDeployFlow**
> GoogleLongrunningOperation dialogflowProjectsLocationsAgentsEnvironmentsDeployFlow(environment, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDialogflowCxV3DeployFlowRequest)



Deploys a flow to the specified Environment. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned &#x60;Operation&#x60; type has the following method-specific fields: - &#x60;metadata&#x60;: DeployFlowMetadata - &#x60;response&#x60;: DeployFlowResponse

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dialogflow.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String environment = "environment_example"; // String | Required. The environment to deploy the flow to. Format: `projects//locations//agents// environments/`.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    GoogleCloudDialogflowCxV3DeployFlowRequest googleCloudDialogflowCxV3DeployFlowRequest = new GoogleCloudDialogflowCxV3DeployFlowRequest(); // GoogleCloudDialogflowCxV3DeployFlowRequest | 
    try {
      GoogleLongrunningOperation result = apiInstance.dialogflowProjectsLocationsAgentsEnvironmentsDeployFlow(environment, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDialogflowCxV3DeployFlowRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#dialogflowProjectsLocationsAgentsEnvironmentsDeployFlow");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **environment** | **String**| Required. The environment to deploy the flow to. Format: &#x60;projects//locations//agents// environments/&#x60;. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **googleCloudDialogflowCxV3DeployFlowRequest** | [**GoogleCloudDialogflowCxV3DeployFlowRequest**](GoogleCloudDialogflowCxV3DeployFlowRequest.md)|  | [optional] |

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dialogflowProjectsLocationsAgentsEnvironmentsDeploymentsList"></a>
# **dialogflowProjectsLocationsAgentsEnvironmentsDeploymentsList**
> GoogleCloudDialogflowCxV3ListDeploymentsResponse dialogflowProjectsLocationsAgentsEnvironmentsDeploymentsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, pageSize, pageToken)



Returns the list of all deployments in the specified Environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dialogflow.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The Environment to list all environments for. Format: `projects//locations//agents//environments/`.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    Integer pageSize = 56; // Integer | The maximum number of items to return in a single page. By default 20 and at most 100.
    String pageToken = "pageToken_example"; // String | The next_page_token value returned from a previous list request.
    try {
      GoogleCloudDialogflowCxV3ListDeploymentsResponse result = apiInstance.dialogflowProjectsLocationsAgentsEnvironmentsDeploymentsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, pageSize, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#dialogflowProjectsLocationsAgentsEnvironmentsDeploymentsList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **parent** | **String**| Required. The Environment to list all environments for. Format: &#x60;projects//locations//agents//environments/&#x60;. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **pageSize** | **Integer**| The maximum number of items to return in a single page. By default 20 and at most 100. | [optional] |
| **pageToken** | **String**| The next_page_token value returned from a previous list request. | [optional] |

### Return type

[**GoogleCloudDialogflowCxV3ListDeploymentsResponse**](GoogleCloudDialogflowCxV3ListDeploymentsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dialogflowProjectsLocationsAgentsEnvironmentsExperimentsCreate"></a>
# **dialogflowProjectsLocationsAgentsEnvironmentsExperimentsCreate**
> GoogleCloudDialogflowCxV3Experiment dialogflowProjectsLocationsAgentsEnvironmentsExperimentsCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDialogflowCxV3Experiment)



Creates an Experiment in the specified Environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dialogflow.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The Agent to create an Environment for. Format: `projects//locations//agents//environments/`.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    GoogleCloudDialogflowCxV3Experiment googleCloudDialogflowCxV3Experiment = new GoogleCloudDialogflowCxV3Experiment(); // GoogleCloudDialogflowCxV3Experiment | 
    try {
      GoogleCloudDialogflowCxV3Experiment result = apiInstance.dialogflowProjectsLocationsAgentsEnvironmentsExperimentsCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDialogflowCxV3Experiment);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#dialogflowProjectsLocationsAgentsEnvironmentsExperimentsCreate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **parent** | **String**| Required. The Agent to create an Environment for. Format: &#x60;projects//locations//agents//environments/&#x60;. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **googleCloudDialogflowCxV3Experiment** | [**GoogleCloudDialogflowCxV3Experiment**](GoogleCloudDialogflowCxV3Experiment.md)|  | [optional] |

### Return type

[**GoogleCloudDialogflowCxV3Experiment**](GoogleCloudDialogflowCxV3Experiment.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dialogflowProjectsLocationsAgentsEnvironmentsExperimentsList"></a>
# **dialogflowProjectsLocationsAgentsEnvironmentsExperimentsList**
> GoogleCloudDialogflowCxV3ListExperimentsResponse dialogflowProjectsLocationsAgentsEnvironmentsExperimentsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, pageSize, pageToken)



Returns the list of all experiments in the specified Environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dialogflow.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The Environment to list all environments for. Format: `projects//locations//agents//environments/`.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    Integer pageSize = 56; // Integer | The maximum number of items to return in a single page. By default 20 and at most 100.
    String pageToken = "pageToken_example"; // String | The next_page_token value returned from a previous list request.
    try {
      GoogleCloudDialogflowCxV3ListExperimentsResponse result = apiInstance.dialogflowProjectsLocationsAgentsEnvironmentsExperimentsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, pageSize, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#dialogflowProjectsLocationsAgentsEnvironmentsExperimentsList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **parent** | **String**| Required. The Environment to list all environments for. Format: &#x60;projects//locations//agents//environments/&#x60;. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **pageSize** | **Integer**| The maximum number of items to return in a single page. By default 20 and at most 100. | [optional] |
| **pageToken** | **String**| The next_page_token value returned from a previous list request. | [optional] |

### Return type

[**GoogleCloudDialogflowCxV3ListExperimentsResponse**](GoogleCloudDialogflowCxV3ListExperimentsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dialogflowProjectsLocationsAgentsEnvironmentsExperimentsStart"></a>
# **dialogflowProjectsLocationsAgentsEnvironmentsExperimentsStart**
> GoogleCloudDialogflowCxV3Experiment dialogflowProjectsLocationsAgentsEnvironmentsExperimentsStart(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, body)



Starts the specified Experiment. This rpc only changes the state of experiment from PENDING to RUNNING.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dialogflow.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String name = "name_example"; // String | Required. Resource name of the experiment to start. Format: `projects//locations//agents//environments//experiments/`.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    Object body = null; // Object | 
    try {
      GoogleCloudDialogflowCxV3Experiment result = apiInstance.dialogflowProjectsLocationsAgentsEnvironmentsExperimentsStart(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#dialogflowProjectsLocationsAgentsEnvironmentsExperimentsStart");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**| Required. Resource name of the experiment to start. Format: &#x60;projects//locations//agents//environments//experiments/&#x60;. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **body** | **Object**|  | [optional] |

### Return type

[**GoogleCloudDialogflowCxV3Experiment**](GoogleCloudDialogflowCxV3Experiment.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dialogflowProjectsLocationsAgentsEnvironmentsExperimentsStop"></a>
# **dialogflowProjectsLocationsAgentsEnvironmentsExperimentsStop**
> GoogleCloudDialogflowCxV3Experiment dialogflowProjectsLocationsAgentsEnvironmentsExperimentsStop(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, body)



Stops the specified Experiment. This rpc only changes the state of experiment from RUNNING to DONE.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dialogflow.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String name = "name_example"; // String | Required. Resource name of the experiment to stop. Format: `projects//locations//agents//environments//experiments/`.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    Object body = null; // Object | 
    try {
      GoogleCloudDialogflowCxV3Experiment result = apiInstance.dialogflowProjectsLocationsAgentsEnvironmentsExperimentsStop(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#dialogflowProjectsLocationsAgentsEnvironmentsExperimentsStop");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**| Required. Resource name of the experiment to stop. Format: &#x60;projects//locations//agents//environments//experiments/&#x60;. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **body** | **Object**|  | [optional] |

### Return type

[**GoogleCloudDialogflowCxV3Experiment**](GoogleCloudDialogflowCxV3Experiment.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dialogflowProjectsLocationsAgentsEnvironmentsList"></a>
# **dialogflowProjectsLocationsAgentsEnvironmentsList**
> GoogleCloudDialogflowCxV3ListEnvironmentsResponse dialogflowProjectsLocationsAgentsEnvironmentsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, pageSize, pageToken)



Returns the list of all environments in the specified Agent.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dialogflow.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The Agent to list all environments for. Format: `projects//locations//agents/`.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    Integer pageSize = 56; // Integer | The maximum number of items to return in a single page. By default 20 and at most 100.
    String pageToken = "pageToken_example"; // String | The next_page_token value returned from a previous list request.
    try {
      GoogleCloudDialogflowCxV3ListEnvironmentsResponse result = apiInstance.dialogflowProjectsLocationsAgentsEnvironmentsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, pageSize, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#dialogflowProjectsLocationsAgentsEnvironmentsList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **parent** | **String**| Required. The Agent to list all environments for. Format: &#x60;projects//locations//agents/&#x60;. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **pageSize** | **Integer**| The maximum number of items to return in a single page. By default 20 and at most 100. | [optional] |
| **pageToken** | **String**| The next_page_token value returned from a previous list request. | [optional] |

### Return type

[**GoogleCloudDialogflowCxV3ListEnvironmentsResponse**](GoogleCloudDialogflowCxV3ListEnvironmentsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dialogflowProjectsLocationsAgentsEnvironmentsLookupEnvironmentHistory"></a>
# **dialogflowProjectsLocationsAgentsEnvironmentsLookupEnvironmentHistory**
> GoogleCloudDialogflowCxV3LookupEnvironmentHistoryResponse dialogflowProjectsLocationsAgentsEnvironmentsLookupEnvironmentHistory(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, pageSize, pageToken)



Looks up the history of the specified Environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dialogflow.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String name = "name_example"; // String | Required. Resource name of the environment to look up the history for. Format: `projects//locations//agents//environments/`.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    Integer pageSize = 56; // Integer | The maximum number of items to return in a single page. By default 100 and at most 1000.
    String pageToken = "pageToken_example"; // String | The next_page_token value returned from a previous list request.
    try {
      GoogleCloudDialogflowCxV3LookupEnvironmentHistoryResponse result = apiInstance.dialogflowProjectsLocationsAgentsEnvironmentsLookupEnvironmentHistory(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, pageSize, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#dialogflowProjectsLocationsAgentsEnvironmentsLookupEnvironmentHistory");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**| Required. Resource name of the environment to look up the history for. Format: &#x60;projects//locations//agents//environments/&#x60;. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **pageSize** | **Integer**| The maximum number of items to return in a single page. By default 100 and at most 1000. | [optional] |
| **pageToken** | **String**| The next_page_token value returned from a previous list request. | [optional] |

### Return type

[**GoogleCloudDialogflowCxV3LookupEnvironmentHistoryResponse**](GoogleCloudDialogflowCxV3LookupEnvironmentHistoryResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dialogflowProjectsLocationsAgentsEnvironmentsRunContinuousTest"></a>
# **dialogflowProjectsLocationsAgentsEnvironmentsRunContinuousTest**
> GoogleLongrunningOperation dialogflowProjectsLocationsAgentsEnvironmentsRunContinuousTest(environment, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, body)



Kicks off a continuous test under the specified Environment. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned &#x60;Operation&#x60; type has the following method-specific fields: - &#x60;metadata&#x60;: RunContinuousTestMetadata - &#x60;response&#x60;: RunContinuousTestResponse

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dialogflow.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String environment = "environment_example"; // String | Required. Format: `projects//locations//agents//environments/`.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    Object body = null; // Object | 
    try {
      GoogleLongrunningOperation result = apiInstance.dialogflowProjectsLocationsAgentsEnvironmentsRunContinuousTest(environment, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#dialogflowProjectsLocationsAgentsEnvironmentsRunContinuousTest");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **environment** | **String**| Required. Format: &#x60;projects//locations//agents//environments/&#x60;. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **body** | **Object**|  | [optional] |

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dialogflowProjectsLocationsAgentsFlowsCreate"></a>
# **dialogflowProjectsLocationsAgentsFlowsCreate**
> GoogleCloudDialogflowCxV3Flow dialogflowProjectsLocationsAgentsFlowsCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, languageCode, googleCloudDialogflowCxV3Flow)



Creates a flow in the specified agent. Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dialogflow.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The agent to create a flow for. Format: `projects//locations//agents/`.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String languageCode = "languageCode_example"; // String | The language of the following fields in `flow`: * `Flow.event_handlers.trigger_fulfillment.messages` * `Flow.event_handlers.trigger_fulfillment.conditional_cases` * `Flow.transition_routes.trigger_fulfillment.messages` * `Flow.transition_routes.trigger_fulfillment.conditional_cases` If not specified, the agent's default language is used. [Many languages](https://cloud.google.com/dialogflow/cx/docs/reference/language) are supported. Note: languages must be enabled in the agent before they can be used.
    GoogleCloudDialogflowCxV3Flow googleCloudDialogflowCxV3Flow = new GoogleCloudDialogflowCxV3Flow(); // GoogleCloudDialogflowCxV3Flow | 
    try {
      GoogleCloudDialogflowCxV3Flow result = apiInstance.dialogflowProjectsLocationsAgentsFlowsCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, languageCode, googleCloudDialogflowCxV3Flow);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#dialogflowProjectsLocationsAgentsFlowsCreate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **parent** | **String**| Required. The agent to create a flow for. Format: &#x60;projects//locations//agents/&#x60;. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **languageCode** | **String**| The language of the following fields in &#x60;flow&#x60;: * &#x60;Flow.event_handlers.trigger_fulfillment.messages&#x60; * &#x60;Flow.event_handlers.trigger_fulfillment.conditional_cases&#x60; * &#x60;Flow.transition_routes.trigger_fulfillment.messages&#x60; * &#x60;Flow.transition_routes.trigger_fulfillment.conditional_cases&#x60; If not specified, the agent&#39;s default language is used. [Many languages](https://cloud.google.com/dialogflow/cx/docs/reference/language) are supported. Note: languages must be enabled in the agent before they can be used. | [optional] |
| **googleCloudDialogflowCxV3Flow** | [**GoogleCloudDialogflowCxV3Flow**](GoogleCloudDialogflowCxV3Flow.md)|  | [optional] |

### Return type

[**GoogleCloudDialogflowCxV3Flow**](GoogleCloudDialogflowCxV3Flow.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dialogflowProjectsLocationsAgentsFlowsExport"></a>
# **dialogflowProjectsLocationsAgentsFlowsExport**
> GoogleLongrunningOperation dialogflowProjectsLocationsAgentsFlowsExport(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDialogflowCxV3ExportFlowRequest)



Exports the specified flow to a binary file. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned &#x60;Operation&#x60; type has the following method-specific fields: - &#x60;metadata&#x60;: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct) - &#x60;response&#x60;: ExportFlowResponse Note that resources (e.g. intents, entities, webhooks) that the flow references will also be exported.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dialogflow.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String name = "name_example"; // String | Required. The name of the flow to export. Format: `projects//locations//agents//flows/`.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    GoogleCloudDialogflowCxV3ExportFlowRequest googleCloudDialogflowCxV3ExportFlowRequest = new GoogleCloudDialogflowCxV3ExportFlowRequest(); // GoogleCloudDialogflowCxV3ExportFlowRequest | 
    try {
      GoogleLongrunningOperation result = apiInstance.dialogflowProjectsLocationsAgentsFlowsExport(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDialogflowCxV3ExportFlowRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#dialogflowProjectsLocationsAgentsFlowsExport");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**| Required. The name of the flow to export. Format: &#x60;projects//locations//agents//flows/&#x60;. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **googleCloudDialogflowCxV3ExportFlowRequest** | [**GoogleCloudDialogflowCxV3ExportFlowRequest**](GoogleCloudDialogflowCxV3ExportFlowRequest.md)|  | [optional] |

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dialogflowProjectsLocationsAgentsFlowsImport"></a>
# **dialogflowProjectsLocationsAgentsFlowsImport**
> GoogleLongrunningOperation dialogflowProjectsLocationsAgentsFlowsImport(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDialogflowCxV3ImportFlowRequest)



Imports the specified flow to the specified agent from a binary file. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned &#x60;Operation&#x60; type has the following method-specific fields: - &#x60;metadata&#x60;: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct) - &#x60;response&#x60;: ImportFlowResponse Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dialogflow.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The agent to import the flow into. Format: `projects//locations//agents/`.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    GoogleCloudDialogflowCxV3ImportFlowRequest googleCloudDialogflowCxV3ImportFlowRequest = new GoogleCloudDialogflowCxV3ImportFlowRequest(); // GoogleCloudDialogflowCxV3ImportFlowRequest | 
    try {
      GoogleLongrunningOperation result = apiInstance.dialogflowProjectsLocationsAgentsFlowsImport(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDialogflowCxV3ImportFlowRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#dialogflowProjectsLocationsAgentsFlowsImport");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **parent** | **String**| Required. The agent to import the flow into. Format: &#x60;projects//locations//agents/&#x60;. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **googleCloudDialogflowCxV3ImportFlowRequest** | [**GoogleCloudDialogflowCxV3ImportFlowRequest**](GoogleCloudDialogflowCxV3ImportFlowRequest.md)|  | [optional] |

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dialogflowProjectsLocationsAgentsFlowsList"></a>
# **dialogflowProjectsLocationsAgentsFlowsList**
> GoogleCloudDialogflowCxV3ListFlowsResponse dialogflowProjectsLocationsAgentsFlowsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, languageCode, pageSize, pageToken)



Returns the list of all flows in the specified agent.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dialogflow.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The agent containing the flows. Format: `projects//locations//agents/`.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String languageCode = "languageCode_example"; // String | The language to list flows for. The following fields are language dependent: * `Flow.event_handlers.trigger_fulfillment.messages` * `Flow.event_handlers.trigger_fulfillment.conditional_cases` * `Flow.transition_routes.trigger_fulfillment.messages` * `Flow.transition_routes.trigger_fulfillment.conditional_cases` If not specified, the agent's default language is used. [Many languages](https://cloud.google.com/dialogflow/cx/docs/reference/language) are supported. Note: languages must be enabled in the agent before they can be used.
    Integer pageSize = 56; // Integer | The maximum number of items to return in a single page. By default 100 and at most 1000.
    String pageToken = "pageToken_example"; // String | The next_page_token value returned from a previous list request.
    try {
      GoogleCloudDialogflowCxV3ListFlowsResponse result = apiInstance.dialogflowProjectsLocationsAgentsFlowsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, languageCode, pageSize, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#dialogflowProjectsLocationsAgentsFlowsList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **parent** | **String**| Required. The agent containing the flows. Format: &#x60;projects//locations//agents/&#x60;. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **languageCode** | **String**| The language to list flows for. The following fields are language dependent: * &#x60;Flow.event_handlers.trigger_fulfillment.messages&#x60; * &#x60;Flow.event_handlers.trigger_fulfillment.conditional_cases&#x60; * &#x60;Flow.transition_routes.trigger_fulfillment.messages&#x60; * &#x60;Flow.transition_routes.trigger_fulfillment.conditional_cases&#x60; If not specified, the agent&#39;s default language is used. [Many languages](https://cloud.google.com/dialogflow/cx/docs/reference/language) are supported. Note: languages must be enabled in the agent before they can be used. | [optional] |
| **pageSize** | **Integer**| The maximum number of items to return in a single page. By default 100 and at most 1000. | [optional] |
| **pageToken** | **String**| The next_page_token value returned from a previous list request. | [optional] |

### Return type

[**GoogleCloudDialogflowCxV3ListFlowsResponse**](GoogleCloudDialogflowCxV3ListFlowsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dialogflowProjectsLocationsAgentsFlowsPagesCreate"></a>
# **dialogflowProjectsLocationsAgentsFlowsPagesCreate**
> GoogleCloudDialogflowCxV3Page dialogflowProjectsLocationsAgentsFlowsPagesCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, languageCode, googleCloudDialogflowCxV3Page)



Creates a page in the specified flow. Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dialogflow.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The flow to create a page for. Format: `projects//locations//agents//flows/`.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String languageCode = "languageCode_example"; // String | The language of the following fields in `page`: * `Page.entry_fulfillment.messages` * `Page.entry_fulfillment.conditional_cases` * `Page.event_handlers.trigger_fulfillment.messages` * `Page.event_handlers.trigger_fulfillment.conditional_cases` * `Page.form.parameters.fill_behavior.initial_prompt_fulfillment.messages` * `Page.form.parameters.fill_behavior.initial_prompt_fulfillment.conditional_cases` * `Page.form.parameters.fill_behavior.reprompt_event_handlers.messages` * `Page.form.parameters.fill_behavior.reprompt_event_handlers.conditional_cases` * `Page.transition_routes.trigger_fulfillment.messages` * `Page.transition_routes.trigger_fulfillment.conditional_cases` If not specified, the agent's default language is used. [Many languages](https://cloud.google.com/dialogflow/cx/docs/reference/language) are supported. Note: languages must be enabled in the agent before they can be used.
    GoogleCloudDialogflowCxV3Page googleCloudDialogflowCxV3Page = new GoogleCloudDialogflowCxV3Page(); // GoogleCloudDialogflowCxV3Page | 
    try {
      GoogleCloudDialogflowCxV3Page result = apiInstance.dialogflowProjectsLocationsAgentsFlowsPagesCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, languageCode, googleCloudDialogflowCxV3Page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#dialogflowProjectsLocationsAgentsFlowsPagesCreate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **parent** | **String**| Required. The flow to create a page for. Format: &#x60;projects//locations//agents//flows/&#x60;. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **languageCode** | **String**| The language of the following fields in &#x60;page&#x60;: * &#x60;Page.entry_fulfillment.messages&#x60; * &#x60;Page.entry_fulfillment.conditional_cases&#x60; * &#x60;Page.event_handlers.trigger_fulfillment.messages&#x60; * &#x60;Page.event_handlers.trigger_fulfillment.conditional_cases&#x60; * &#x60;Page.form.parameters.fill_behavior.initial_prompt_fulfillment.messages&#x60; * &#x60;Page.form.parameters.fill_behavior.initial_prompt_fulfillment.conditional_cases&#x60; * &#x60;Page.form.parameters.fill_behavior.reprompt_event_handlers.messages&#x60; * &#x60;Page.form.parameters.fill_behavior.reprompt_event_handlers.conditional_cases&#x60; * &#x60;Page.transition_routes.trigger_fulfillment.messages&#x60; * &#x60;Page.transition_routes.trigger_fulfillment.conditional_cases&#x60; If not specified, the agent&#39;s default language is used. [Many languages](https://cloud.google.com/dialogflow/cx/docs/reference/language) are supported. Note: languages must be enabled in the agent before they can be used. | [optional] |
| **googleCloudDialogflowCxV3Page** | [**GoogleCloudDialogflowCxV3Page**](GoogleCloudDialogflowCxV3Page.md)|  | [optional] |

### Return type

[**GoogleCloudDialogflowCxV3Page**](GoogleCloudDialogflowCxV3Page.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dialogflowProjectsLocationsAgentsFlowsPagesList"></a>
# **dialogflowProjectsLocationsAgentsFlowsPagesList**
> GoogleCloudDialogflowCxV3ListPagesResponse dialogflowProjectsLocationsAgentsFlowsPagesList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, languageCode, pageSize, pageToken)



Returns the list of all pages in the specified flow.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dialogflow.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The flow to list all pages for. Format: `projects//locations//agents//flows/`.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String languageCode = "languageCode_example"; // String | The language to list pages for. The following fields are language dependent: * `Page.entry_fulfillment.messages` * `Page.entry_fulfillment.conditional_cases` * `Page.event_handlers.trigger_fulfillment.messages` * `Page.event_handlers.trigger_fulfillment.conditional_cases` * `Page.form.parameters.fill_behavior.initial_prompt_fulfillment.messages` * `Page.form.parameters.fill_behavior.initial_prompt_fulfillment.conditional_cases` * `Page.form.parameters.fill_behavior.reprompt_event_handlers.messages` * `Page.form.parameters.fill_behavior.reprompt_event_handlers.conditional_cases` * `Page.transition_routes.trigger_fulfillment.messages` * `Page.transition_routes.trigger_fulfillment.conditional_cases` If not specified, the agent's default language is used. [Many languages](https://cloud.google.com/dialogflow/cx/docs/reference/language) are supported. Note: languages must be enabled in the agent before they can be used.
    Integer pageSize = 56; // Integer | The maximum number of items to return in a single page. By default 100 and at most 1000.
    String pageToken = "pageToken_example"; // String | The next_page_token value returned from a previous list request.
    try {
      GoogleCloudDialogflowCxV3ListPagesResponse result = apiInstance.dialogflowProjectsLocationsAgentsFlowsPagesList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, languageCode, pageSize, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#dialogflowProjectsLocationsAgentsFlowsPagesList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **parent** | **String**| Required. The flow to list all pages for. Format: &#x60;projects//locations//agents//flows/&#x60;. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **languageCode** | **String**| The language to list pages for. The following fields are language dependent: * &#x60;Page.entry_fulfillment.messages&#x60; * &#x60;Page.entry_fulfillment.conditional_cases&#x60; * &#x60;Page.event_handlers.trigger_fulfillment.messages&#x60; * &#x60;Page.event_handlers.trigger_fulfillment.conditional_cases&#x60; * &#x60;Page.form.parameters.fill_behavior.initial_prompt_fulfillment.messages&#x60; * &#x60;Page.form.parameters.fill_behavior.initial_prompt_fulfillment.conditional_cases&#x60; * &#x60;Page.form.parameters.fill_behavior.reprompt_event_handlers.messages&#x60; * &#x60;Page.form.parameters.fill_behavior.reprompt_event_handlers.conditional_cases&#x60; * &#x60;Page.transition_routes.trigger_fulfillment.messages&#x60; * &#x60;Page.transition_routes.trigger_fulfillment.conditional_cases&#x60; If not specified, the agent&#39;s default language is used. [Many languages](https://cloud.google.com/dialogflow/cx/docs/reference/language) are supported. Note: languages must be enabled in the agent before they can be used. | [optional] |
| **pageSize** | **Integer**| The maximum number of items to return in a single page. By default 100 and at most 1000. | [optional] |
| **pageToken** | **String**| The next_page_token value returned from a previous list request. | [optional] |

### Return type

[**GoogleCloudDialogflowCxV3ListPagesResponse**](GoogleCloudDialogflowCxV3ListPagesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dialogflowProjectsLocationsAgentsFlowsTrain"></a>
# **dialogflowProjectsLocationsAgentsFlowsTrain**
> GoogleLongrunningOperation dialogflowProjectsLocationsAgentsFlowsTrain(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, body)



Trains the specified flow. Note that only the flow in &#39;draft&#39; environment is trained. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned &#x60;Operation&#x60; type has the following method-specific fields: - &#x60;metadata&#x60;: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct) - &#x60;response&#x60;: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty) Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dialogflow.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String name = "name_example"; // String | Required. The flow to train. Format: `projects//locations//agents//flows/`.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    Object body = null; // Object | 
    try {
      GoogleLongrunningOperation result = apiInstance.dialogflowProjectsLocationsAgentsFlowsTrain(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#dialogflowProjectsLocationsAgentsFlowsTrain");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**| Required. The flow to train. Format: &#x60;projects//locations//agents//flows/&#x60;. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **body** | **Object**|  | [optional] |

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dialogflowProjectsLocationsAgentsFlowsValidate"></a>
# **dialogflowProjectsLocationsAgentsFlowsValidate**
> GoogleCloudDialogflowCxV3FlowValidationResult dialogflowProjectsLocationsAgentsFlowsValidate(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDialogflowCxV3ValidateFlowRequest)



Validates the specified flow and creates or updates validation results. Please call this API after the training is completed to get the complete validation results.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dialogflow.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String name = "name_example"; // String | Required. The flow to validate. Format: `projects//locations//agents//flows/`.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    GoogleCloudDialogflowCxV3ValidateFlowRequest googleCloudDialogflowCxV3ValidateFlowRequest = new GoogleCloudDialogflowCxV3ValidateFlowRequest(); // GoogleCloudDialogflowCxV3ValidateFlowRequest | 
    try {
      GoogleCloudDialogflowCxV3FlowValidationResult result = apiInstance.dialogflowProjectsLocationsAgentsFlowsValidate(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDialogflowCxV3ValidateFlowRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#dialogflowProjectsLocationsAgentsFlowsValidate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**| Required. The flow to validate. Format: &#x60;projects//locations//agents//flows/&#x60;. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **googleCloudDialogflowCxV3ValidateFlowRequest** | [**GoogleCloudDialogflowCxV3ValidateFlowRequest**](GoogleCloudDialogflowCxV3ValidateFlowRequest.md)|  | [optional] |

### Return type

[**GoogleCloudDialogflowCxV3FlowValidationResult**](GoogleCloudDialogflowCxV3FlowValidationResult.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dialogflowProjectsLocationsAgentsFlowsVersionsCompareVersions"></a>
# **dialogflowProjectsLocationsAgentsFlowsVersionsCompareVersions**
> GoogleCloudDialogflowCxV3CompareVersionsResponse dialogflowProjectsLocationsAgentsFlowsVersionsCompareVersions(baseVersion, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDialogflowCxV3CompareVersionsRequest)



Compares the specified base version with target version.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dialogflow.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String baseVersion = "baseVersion_example"; // String | Required. Name of the base flow version to compare with the target version. Use version ID `0` to indicate the draft version of the specified flow. Format: `projects//locations//agents/ /flows//versions/`.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    GoogleCloudDialogflowCxV3CompareVersionsRequest googleCloudDialogflowCxV3CompareVersionsRequest = new GoogleCloudDialogflowCxV3CompareVersionsRequest(); // GoogleCloudDialogflowCxV3CompareVersionsRequest | 
    try {
      GoogleCloudDialogflowCxV3CompareVersionsResponse result = apiInstance.dialogflowProjectsLocationsAgentsFlowsVersionsCompareVersions(baseVersion, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDialogflowCxV3CompareVersionsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#dialogflowProjectsLocationsAgentsFlowsVersionsCompareVersions");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **baseVersion** | **String**| Required. Name of the base flow version to compare with the target version. Use version ID &#x60;0&#x60; to indicate the draft version of the specified flow. Format: &#x60;projects//locations//agents/ /flows//versions/&#x60;. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **googleCloudDialogflowCxV3CompareVersionsRequest** | [**GoogleCloudDialogflowCxV3CompareVersionsRequest**](GoogleCloudDialogflowCxV3CompareVersionsRequest.md)|  | [optional] |

### Return type

[**GoogleCloudDialogflowCxV3CompareVersionsResponse**](GoogleCloudDialogflowCxV3CompareVersionsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dialogflowProjectsLocationsAgentsFlowsVersionsCreate"></a>
# **dialogflowProjectsLocationsAgentsFlowsVersionsCreate**
> GoogleLongrunningOperation dialogflowProjectsLocationsAgentsFlowsVersionsCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDialogflowCxV3Version)



Creates a Version in the specified Flow. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned &#x60;Operation&#x60; type has the following method-specific fields: - &#x60;metadata&#x60;: CreateVersionOperationMetadata - &#x60;response&#x60;: Version

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dialogflow.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The Flow to create an Version for. Format: `projects//locations//agents//flows/`.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    GoogleCloudDialogflowCxV3Version googleCloudDialogflowCxV3Version = new GoogleCloudDialogflowCxV3Version(); // GoogleCloudDialogflowCxV3Version | 
    try {
      GoogleLongrunningOperation result = apiInstance.dialogflowProjectsLocationsAgentsFlowsVersionsCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDialogflowCxV3Version);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#dialogflowProjectsLocationsAgentsFlowsVersionsCreate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **parent** | **String**| Required. The Flow to create an Version for. Format: &#x60;projects//locations//agents//flows/&#x60;. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **googleCloudDialogflowCxV3Version** | [**GoogleCloudDialogflowCxV3Version**](GoogleCloudDialogflowCxV3Version.md)|  | [optional] |

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dialogflowProjectsLocationsAgentsFlowsVersionsList"></a>
# **dialogflowProjectsLocationsAgentsFlowsVersionsList**
> GoogleCloudDialogflowCxV3ListVersionsResponse dialogflowProjectsLocationsAgentsFlowsVersionsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, pageSize, pageToken)



Returns the list of all versions in the specified Flow.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dialogflow.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The Flow to list all versions for. Format: `projects//locations//agents//flows/`.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    Integer pageSize = 56; // Integer | The maximum number of items to return in a single page. By default 20 and at most 100.
    String pageToken = "pageToken_example"; // String | The next_page_token value returned from a previous list request.
    try {
      GoogleCloudDialogflowCxV3ListVersionsResponse result = apiInstance.dialogflowProjectsLocationsAgentsFlowsVersionsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, pageSize, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#dialogflowProjectsLocationsAgentsFlowsVersionsList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **parent** | **String**| Required. The Flow to list all versions for. Format: &#x60;projects//locations//agents//flows/&#x60;. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **pageSize** | **Integer**| The maximum number of items to return in a single page. By default 20 and at most 100. | [optional] |
| **pageToken** | **String**| The next_page_token value returned from a previous list request. | [optional] |

### Return type

[**GoogleCloudDialogflowCxV3ListVersionsResponse**](GoogleCloudDialogflowCxV3ListVersionsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dialogflowProjectsLocationsAgentsFlowsVersionsLoad"></a>
# **dialogflowProjectsLocationsAgentsFlowsVersionsLoad**
> GoogleLongrunningOperation dialogflowProjectsLocationsAgentsFlowsVersionsLoad(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDialogflowCxV3LoadVersionRequest)



Loads resources in the specified version to the draft flow. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned &#x60;Operation&#x60; type has the following method-specific fields: - &#x60;metadata&#x60;: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct) - &#x60;response&#x60;: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dialogflow.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String name = "name_example"; // String | Required. The Version to be loaded to draft flow. Format: `projects//locations//agents//flows//versions/`.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    GoogleCloudDialogflowCxV3LoadVersionRequest googleCloudDialogflowCxV3LoadVersionRequest = new GoogleCloudDialogflowCxV3LoadVersionRequest(); // GoogleCloudDialogflowCxV3LoadVersionRequest | 
    try {
      GoogleLongrunningOperation result = apiInstance.dialogflowProjectsLocationsAgentsFlowsVersionsLoad(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDialogflowCxV3LoadVersionRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#dialogflowProjectsLocationsAgentsFlowsVersionsLoad");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**| Required. The Version to be loaded to draft flow. Format: &#x60;projects//locations//agents//flows//versions/&#x60;. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **googleCloudDialogflowCxV3LoadVersionRequest** | [**GoogleCloudDialogflowCxV3LoadVersionRequest**](GoogleCloudDialogflowCxV3LoadVersionRequest.md)|  | [optional] |

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dialogflowProjectsLocationsAgentsGeneratorsCreate"></a>
# **dialogflowProjectsLocationsAgentsGeneratorsCreate**
> GoogleCloudDialogflowCxV3Generator dialogflowProjectsLocationsAgentsGeneratorsCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, languageCode, googleCloudDialogflowCxV3Generator)



Creates a generator in the specified agent.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dialogflow.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The agent to create a generator for. Format: `projects//locations//agents/`.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String languageCode = "languageCode_example"; // String | The language to create generators for the following fields: * `Generator.prompt_text.text` If not specified, the agent's default language is used.
    GoogleCloudDialogflowCxV3Generator googleCloudDialogflowCxV3Generator = new GoogleCloudDialogflowCxV3Generator(); // GoogleCloudDialogflowCxV3Generator | 
    try {
      GoogleCloudDialogflowCxV3Generator result = apiInstance.dialogflowProjectsLocationsAgentsGeneratorsCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, languageCode, googleCloudDialogflowCxV3Generator);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#dialogflowProjectsLocationsAgentsGeneratorsCreate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **parent** | **String**| Required. The agent to create a generator for. Format: &#x60;projects//locations//agents/&#x60;. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **languageCode** | **String**| The language to create generators for the following fields: * &#x60;Generator.prompt_text.text&#x60; If not specified, the agent&#39;s default language is used. | [optional] |
| **googleCloudDialogflowCxV3Generator** | [**GoogleCloudDialogflowCxV3Generator**](GoogleCloudDialogflowCxV3Generator.md)|  | [optional] |

### Return type

[**GoogleCloudDialogflowCxV3Generator**](GoogleCloudDialogflowCxV3Generator.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dialogflowProjectsLocationsAgentsGeneratorsList"></a>
# **dialogflowProjectsLocationsAgentsGeneratorsList**
> GoogleCloudDialogflowCxV3ListGeneratorsResponse dialogflowProjectsLocationsAgentsGeneratorsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, languageCode, pageSize, pageToken)



Returns the list of all generators in the specified agent.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dialogflow.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The agent to list all generators for. Format: `projects//locations//agents/`.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String languageCode = "languageCode_example"; // String | The language to list generators for.
    Integer pageSize = 56; // Integer | The maximum number of items to return in a single page. By default 100 and at most 1000.
    String pageToken = "pageToken_example"; // String | The next_page_token value returned from a previous list request.
    try {
      GoogleCloudDialogflowCxV3ListGeneratorsResponse result = apiInstance.dialogflowProjectsLocationsAgentsGeneratorsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, languageCode, pageSize, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#dialogflowProjectsLocationsAgentsGeneratorsList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **parent** | **String**| Required. The agent to list all generators for. Format: &#x60;projects//locations//agents/&#x60;. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **languageCode** | **String**| The language to list generators for. | [optional] |
| **pageSize** | **Integer**| The maximum number of items to return in a single page. By default 100 and at most 1000. | [optional] |
| **pageToken** | **String**| The next_page_token value returned from a previous list request. | [optional] |

### Return type

[**GoogleCloudDialogflowCxV3ListGeneratorsResponse**](GoogleCloudDialogflowCxV3ListGeneratorsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dialogflowProjectsLocationsAgentsIntentsCreate"></a>
# **dialogflowProjectsLocationsAgentsIntentsCreate**
> GoogleCloudDialogflowCxV3Intent dialogflowProjectsLocationsAgentsIntentsCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, languageCode, googleCloudDialogflowCxV3Intent)



Creates an intent in the specified agent. Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dialogflow.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The agent to create an intent for. Format: `projects//locations//agents/`.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String languageCode = "languageCode_example"; // String | The language of the following fields in `intent`: * `Intent.training_phrases.parts.text` If not specified, the agent's default language is used. [Many languages](https://cloud.google.com/dialogflow/cx/docs/reference/language) are supported. Note: languages must be enabled in the agent before they can be used.
    GoogleCloudDialogflowCxV3Intent googleCloudDialogflowCxV3Intent = new GoogleCloudDialogflowCxV3Intent(); // GoogleCloudDialogflowCxV3Intent | 
    try {
      GoogleCloudDialogflowCxV3Intent result = apiInstance.dialogflowProjectsLocationsAgentsIntentsCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, languageCode, googleCloudDialogflowCxV3Intent);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#dialogflowProjectsLocationsAgentsIntentsCreate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **parent** | **String**| Required. The agent to create an intent for. Format: &#x60;projects//locations//agents/&#x60;. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **languageCode** | **String**| The language of the following fields in &#x60;intent&#x60;: * &#x60;Intent.training_phrases.parts.text&#x60; If not specified, the agent&#39;s default language is used. [Many languages](https://cloud.google.com/dialogflow/cx/docs/reference/language) are supported. Note: languages must be enabled in the agent before they can be used. | [optional] |
| **googleCloudDialogflowCxV3Intent** | [**GoogleCloudDialogflowCxV3Intent**](GoogleCloudDialogflowCxV3Intent.md)|  | [optional] |

### Return type

[**GoogleCloudDialogflowCxV3Intent**](GoogleCloudDialogflowCxV3Intent.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dialogflowProjectsLocationsAgentsIntentsExport"></a>
# **dialogflowProjectsLocationsAgentsIntentsExport**
> GoogleLongrunningOperation dialogflowProjectsLocationsAgentsIntentsExport(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDialogflowCxV3ExportIntentsRequest)



Exports the selected intents. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned &#x60;Operation&#x60; type has the following method-specific fields: - &#x60;metadata&#x60;: ExportIntentsMetadata - &#x60;response&#x60;: ExportIntentsResponse

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dialogflow.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The name of the parent agent to export intents. Format: `projects//locations//agents/`.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    GoogleCloudDialogflowCxV3ExportIntentsRequest googleCloudDialogflowCxV3ExportIntentsRequest = new GoogleCloudDialogflowCxV3ExportIntentsRequest(); // GoogleCloudDialogflowCxV3ExportIntentsRequest | 
    try {
      GoogleLongrunningOperation result = apiInstance.dialogflowProjectsLocationsAgentsIntentsExport(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDialogflowCxV3ExportIntentsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#dialogflowProjectsLocationsAgentsIntentsExport");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **parent** | **String**| Required. The name of the parent agent to export intents. Format: &#x60;projects//locations//agents/&#x60;. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **googleCloudDialogflowCxV3ExportIntentsRequest** | [**GoogleCloudDialogflowCxV3ExportIntentsRequest**](GoogleCloudDialogflowCxV3ExportIntentsRequest.md)|  | [optional] |

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dialogflowProjectsLocationsAgentsIntentsImport"></a>
# **dialogflowProjectsLocationsAgentsIntentsImport**
> GoogleLongrunningOperation dialogflowProjectsLocationsAgentsIntentsImport(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDialogflowCxV3ImportIntentsRequest)



Imports the specified intents into the agent. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned &#x60;Operation&#x60; type has the following method-specific fields: - &#x60;metadata&#x60;: ImportIntentsMetadata - &#x60;response&#x60;: ImportIntentsResponse

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dialogflow.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The agent to import the intents into. Format: `projects//locations//agents/`.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    GoogleCloudDialogflowCxV3ImportIntentsRequest googleCloudDialogflowCxV3ImportIntentsRequest = new GoogleCloudDialogflowCxV3ImportIntentsRequest(); // GoogleCloudDialogflowCxV3ImportIntentsRequest | 
    try {
      GoogleLongrunningOperation result = apiInstance.dialogflowProjectsLocationsAgentsIntentsImport(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDialogflowCxV3ImportIntentsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#dialogflowProjectsLocationsAgentsIntentsImport");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **parent** | **String**| Required. The agent to import the intents into. Format: &#x60;projects//locations//agents/&#x60;. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **googleCloudDialogflowCxV3ImportIntentsRequest** | [**GoogleCloudDialogflowCxV3ImportIntentsRequest**](GoogleCloudDialogflowCxV3ImportIntentsRequest.md)|  | [optional] |

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dialogflowProjectsLocationsAgentsIntentsList"></a>
# **dialogflowProjectsLocationsAgentsIntentsList**
> GoogleCloudDialogflowCxV3ListIntentsResponse dialogflowProjectsLocationsAgentsIntentsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, intentView, languageCode, pageSize, pageToken)



Returns the list of all intents in the specified agent.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dialogflow.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The agent to list all intents for. Format: `projects//locations//agents/`.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String intentView = "INTENT_VIEW_UNSPECIFIED"; // String | The resource view to apply to the returned intent.
    String languageCode = "languageCode_example"; // String | The language to list intents for. The following fields are language dependent: * `Intent.training_phrases.parts.text` If not specified, the agent's default language is used. [Many languages](https://cloud.google.com/dialogflow/cx/docs/reference/language) are supported. Note: languages must be enabled in the agent before they can be used.
    Integer pageSize = 56; // Integer | The maximum number of items to return in a single page. By default 100 and at most 1000.
    String pageToken = "pageToken_example"; // String | The next_page_token value returned from a previous list request.
    try {
      GoogleCloudDialogflowCxV3ListIntentsResponse result = apiInstance.dialogflowProjectsLocationsAgentsIntentsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, intentView, languageCode, pageSize, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#dialogflowProjectsLocationsAgentsIntentsList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **parent** | **String**| Required. The agent to list all intents for. Format: &#x60;projects//locations//agents/&#x60;. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **intentView** | **String**| The resource view to apply to the returned intent. | [optional] [enum: INTENT_VIEW_UNSPECIFIED, INTENT_VIEW_PARTIAL, INTENT_VIEW_FULL] |
| **languageCode** | **String**| The language to list intents for. The following fields are language dependent: * &#x60;Intent.training_phrases.parts.text&#x60; If not specified, the agent&#39;s default language is used. [Many languages](https://cloud.google.com/dialogflow/cx/docs/reference/language) are supported. Note: languages must be enabled in the agent before they can be used. | [optional] |
| **pageSize** | **Integer**| The maximum number of items to return in a single page. By default 100 and at most 1000. | [optional] |
| **pageToken** | **String**| The next_page_token value returned from a previous list request. | [optional] |

### Return type

[**GoogleCloudDialogflowCxV3ListIntentsResponse**](GoogleCloudDialogflowCxV3ListIntentsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dialogflowProjectsLocationsAgentsList"></a>
# **dialogflowProjectsLocationsAgentsList**
> GoogleCloudDialogflowCxV3ListAgentsResponse dialogflowProjectsLocationsAgentsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, pageSize, pageToken)



Returns the list of all agents in the specified location.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dialogflow.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The location to list all agents for. Format: `projects//locations/`.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    Integer pageSize = 56; // Integer | The maximum number of items to return in a single page. By default 100 and at most 1000.
    String pageToken = "pageToken_example"; // String | The next_page_token value returned from a previous list request.
    try {
      GoogleCloudDialogflowCxV3ListAgentsResponse result = apiInstance.dialogflowProjectsLocationsAgentsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, pageSize, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#dialogflowProjectsLocationsAgentsList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **parent** | **String**| Required. The location to list all agents for. Format: &#x60;projects//locations/&#x60;. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **pageSize** | **Integer**| The maximum number of items to return in a single page. By default 100 and at most 1000. | [optional] |
| **pageToken** | **String**| The next_page_token value returned from a previous list request. | [optional] |

### Return type

[**GoogleCloudDialogflowCxV3ListAgentsResponse**](GoogleCloudDialogflowCxV3ListAgentsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dialogflowProjectsLocationsAgentsRestore"></a>
# **dialogflowProjectsLocationsAgentsRestore**
> GoogleLongrunningOperation dialogflowProjectsLocationsAgentsRestore(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDialogflowCxV3RestoreAgentRequest)



Restores the specified agent from a binary file. Replaces the current agent with a new one. Note that all existing resources in agent (e.g. intents, entity types, flows) will be removed. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned &#x60;Operation&#x60; type has the following method-specific fields: - &#x60;metadata&#x60;: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct) - &#x60;response&#x60;: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty) Note: You should always train flows prior to sending them queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dialogflow.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String name = "name_example"; // String | Required. The name of the agent to restore into. Format: `projects//locations//agents/`.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    GoogleCloudDialogflowCxV3RestoreAgentRequest googleCloudDialogflowCxV3RestoreAgentRequest = new GoogleCloudDialogflowCxV3RestoreAgentRequest(); // GoogleCloudDialogflowCxV3RestoreAgentRequest | 
    try {
      GoogleLongrunningOperation result = apiInstance.dialogflowProjectsLocationsAgentsRestore(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDialogflowCxV3RestoreAgentRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#dialogflowProjectsLocationsAgentsRestore");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**| Required. The name of the agent to restore into. Format: &#x60;projects//locations//agents/&#x60;. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **googleCloudDialogflowCxV3RestoreAgentRequest** | [**GoogleCloudDialogflowCxV3RestoreAgentRequest**](GoogleCloudDialogflowCxV3RestoreAgentRequest.md)|  | [optional] |

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dialogflowProjectsLocationsAgentsSessionsDetectIntent"></a>
# **dialogflowProjectsLocationsAgentsSessionsDetectIntent**
> GoogleCloudDialogflowCxV3DetectIntentResponse dialogflowProjectsLocationsAgentsSessionsDetectIntent(session, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDialogflowCxV3DetectIntentRequest)



Processes a natural language query and returns structured, actionable data as a result. This method is not idempotent, because it may cause session entity types to be updated, which in turn might affect results of future queries. Note: Always use agent versions for production traffic. See [Versions and environments](https://cloud.google.com/dialogflow/cx/docs/concept/version).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dialogflow.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String session = "session_example"; // String | Required. The name of the session this query is sent to. Format: `projects//locations//agents//sessions/` or `projects//locations//agents//environments//sessions/`. If `Environment ID` is not specified, we assume default 'draft' environment. It's up to the API caller to choose an appropriate `Session ID`. It can be a random number or some type of session identifiers (preferably hashed). The length of the `Session ID` must not exceed 36 characters. For more information, see the [sessions guide](https://cloud.google.com/dialogflow/cx/docs/concept/session). Note: Always use agent versions for production traffic. See [Versions and environments](https://cloud.google.com/dialogflow/cx/docs/concept/version).
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    GoogleCloudDialogflowCxV3DetectIntentRequest googleCloudDialogflowCxV3DetectIntentRequest = new GoogleCloudDialogflowCxV3DetectIntentRequest(); // GoogleCloudDialogflowCxV3DetectIntentRequest | 
    try {
      GoogleCloudDialogflowCxV3DetectIntentResponse result = apiInstance.dialogflowProjectsLocationsAgentsSessionsDetectIntent(session, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDialogflowCxV3DetectIntentRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#dialogflowProjectsLocationsAgentsSessionsDetectIntent");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **session** | **String**| Required. The name of the session this query is sent to. Format: &#x60;projects//locations//agents//sessions/&#x60; or &#x60;projects//locations//agents//environments//sessions/&#x60;. If &#x60;Environment ID&#x60; is not specified, we assume default &#39;draft&#39; environment. It&#39;s up to the API caller to choose an appropriate &#x60;Session ID&#x60;. It can be a random number or some type of session identifiers (preferably hashed). The length of the &#x60;Session ID&#x60; must not exceed 36 characters. For more information, see the [sessions guide](https://cloud.google.com/dialogflow/cx/docs/concept/session). Note: Always use agent versions for production traffic. See [Versions and environments](https://cloud.google.com/dialogflow/cx/docs/concept/version). | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **googleCloudDialogflowCxV3DetectIntentRequest** | [**GoogleCloudDialogflowCxV3DetectIntentRequest**](GoogleCloudDialogflowCxV3DetectIntentRequest.md)|  | [optional] |

### Return type

[**GoogleCloudDialogflowCxV3DetectIntentResponse**](GoogleCloudDialogflowCxV3DetectIntentResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dialogflowProjectsLocationsAgentsSessionsEntityTypesCreate"></a>
# **dialogflowProjectsLocationsAgentsSessionsEntityTypesCreate**
> GoogleCloudDialogflowCxV3SessionEntityType dialogflowProjectsLocationsAgentsSessionsEntityTypesCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, languageCode, googleCloudDialogflowCxV3SessionEntityType)



Creates a session entity type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dialogflow.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The session to create a session entity type for. Format: `projects//locations//agents//sessions/` or `projects//locations//agents//environments//sessions/`. If `Environment ID` is not specified, we assume default 'draft' environment.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String languageCode = "languageCode_example"; // String | The language of the following fields in `entity_type`: * `EntityType.entities.value` * `EntityType.entities.synonyms` * `EntityType.excluded_phrases.value` If not specified, the agent's default language is used. [Many languages](https://cloud.google.com/dialogflow/cx/docs/reference/language) are supported. Note: languages must be enabled in the agent before they can be used.
    GoogleCloudDialogflowCxV3SessionEntityType googleCloudDialogflowCxV3SessionEntityType = new GoogleCloudDialogflowCxV3SessionEntityType(); // GoogleCloudDialogflowCxV3SessionEntityType | 
    try {
      GoogleCloudDialogflowCxV3SessionEntityType result = apiInstance.dialogflowProjectsLocationsAgentsSessionsEntityTypesCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, languageCode, googleCloudDialogflowCxV3SessionEntityType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#dialogflowProjectsLocationsAgentsSessionsEntityTypesCreate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **parent** | **String**| Required. The session to create a session entity type for. Format: &#x60;projects//locations//agents//sessions/&#x60; or &#x60;projects//locations//agents//environments//sessions/&#x60;. If &#x60;Environment ID&#x60; is not specified, we assume default &#39;draft&#39; environment. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **languageCode** | **String**| The language of the following fields in &#x60;entity_type&#x60;: * &#x60;EntityType.entities.value&#x60; * &#x60;EntityType.entities.synonyms&#x60; * &#x60;EntityType.excluded_phrases.value&#x60; If not specified, the agent&#39;s default language is used. [Many languages](https://cloud.google.com/dialogflow/cx/docs/reference/language) are supported. Note: languages must be enabled in the agent before they can be used. | [optional] |
| **googleCloudDialogflowCxV3SessionEntityType** | [**GoogleCloudDialogflowCxV3SessionEntityType**](GoogleCloudDialogflowCxV3SessionEntityType.md)|  | [optional] |

### Return type

[**GoogleCloudDialogflowCxV3SessionEntityType**](GoogleCloudDialogflowCxV3SessionEntityType.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dialogflowProjectsLocationsAgentsSessionsEntityTypesList"></a>
# **dialogflowProjectsLocationsAgentsSessionsEntityTypesList**
> GoogleCloudDialogflowCxV3ListSessionEntityTypesResponse dialogflowProjectsLocationsAgentsSessionsEntityTypesList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, pageSize, pageToken)



Returns the list of all session entity types in the specified session.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dialogflow.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The session to list all session entity types from. Format: `projects//locations//agents//sessions/` or `projects//locations//agents//environments//sessions/`. If `Environment ID` is not specified, we assume default 'draft' environment.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    Integer pageSize = 56; // Integer | The maximum number of items to return in a single page. By default 100 and at most 1000.
    String pageToken = "pageToken_example"; // String | The next_page_token value returned from a previous list request.
    try {
      GoogleCloudDialogflowCxV3ListSessionEntityTypesResponse result = apiInstance.dialogflowProjectsLocationsAgentsSessionsEntityTypesList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, pageSize, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#dialogflowProjectsLocationsAgentsSessionsEntityTypesList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **parent** | **String**| Required. The session to list all session entity types from. Format: &#x60;projects//locations//agents//sessions/&#x60; or &#x60;projects//locations//agents//environments//sessions/&#x60;. If &#x60;Environment ID&#x60; is not specified, we assume default &#39;draft&#39; environment. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **pageSize** | **Integer**| The maximum number of items to return in a single page. By default 100 and at most 1000. | [optional] |
| **pageToken** | **String**| The next_page_token value returned from a previous list request. | [optional] |

### Return type

[**GoogleCloudDialogflowCxV3ListSessionEntityTypesResponse**](GoogleCloudDialogflowCxV3ListSessionEntityTypesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dialogflowProjectsLocationsAgentsSessionsFulfillIntent"></a>
# **dialogflowProjectsLocationsAgentsSessionsFulfillIntent**
> GoogleCloudDialogflowCxV3FulfillIntentResponse dialogflowProjectsLocationsAgentsSessionsFulfillIntent(session, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDialogflowCxV3FulfillIntentRequest)



Fulfills a matched intent returned by MatchIntent. Must be called after MatchIntent, with input from MatchIntentResponse. Otherwise, the behavior is undefined.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dialogflow.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String session = "session_example"; // String | Required. The name of the session this query is sent to. Format: `projects//locations//agents//sessions/` or `projects//locations//agents//environments//sessions/`. If `Environment ID` is not specified, we assume default 'draft' environment. It's up to the API caller to choose an appropriate `Session ID`. It can be a random number or some type of session identifiers (preferably hashed). The length of the `Session ID` must not exceed 36 characters. For more information, see the [sessions guide](https://cloud.google.com/dialogflow/cx/docs/concept/session).
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    GoogleCloudDialogflowCxV3FulfillIntentRequest googleCloudDialogflowCxV3FulfillIntentRequest = new GoogleCloudDialogflowCxV3FulfillIntentRequest(); // GoogleCloudDialogflowCxV3FulfillIntentRequest | 
    try {
      GoogleCloudDialogflowCxV3FulfillIntentResponse result = apiInstance.dialogflowProjectsLocationsAgentsSessionsFulfillIntent(session, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDialogflowCxV3FulfillIntentRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#dialogflowProjectsLocationsAgentsSessionsFulfillIntent");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **session** | **String**| Required. The name of the session this query is sent to. Format: &#x60;projects//locations//agents//sessions/&#x60; or &#x60;projects//locations//agents//environments//sessions/&#x60;. If &#x60;Environment ID&#x60; is not specified, we assume default &#39;draft&#39; environment. It&#39;s up to the API caller to choose an appropriate &#x60;Session ID&#x60;. It can be a random number or some type of session identifiers (preferably hashed). The length of the &#x60;Session ID&#x60; must not exceed 36 characters. For more information, see the [sessions guide](https://cloud.google.com/dialogflow/cx/docs/concept/session). | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **googleCloudDialogflowCxV3FulfillIntentRequest** | [**GoogleCloudDialogflowCxV3FulfillIntentRequest**](GoogleCloudDialogflowCxV3FulfillIntentRequest.md)|  | [optional] |

### Return type

[**GoogleCloudDialogflowCxV3FulfillIntentResponse**](GoogleCloudDialogflowCxV3FulfillIntentResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dialogflowProjectsLocationsAgentsSessionsMatchIntent"></a>
# **dialogflowProjectsLocationsAgentsSessionsMatchIntent**
> GoogleCloudDialogflowCxV3MatchIntentResponse dialogflowProjectsLocationsAgentsSessionsMatchIntent(session, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDialogflowCxV3MatchIntentRequest)



Returns preliminary intent match results, doesn&#39;t change the session status.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dialogflow.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String session = "session_example"; // String | Required. The name of the session this query is sent to. Format: `projects//locations//agents//sessions/` or `projects//locations//agents//environments//sessions/`. If `Environment ID` is not specified, we assume default 'draft' environment. It's up to the API caller to choose an appropriate `Session ID`. It can be a random number or some type of session identifiers (preferably hashed). The length of the `Session ID` must not exceed 36 characters. For more information, see the [sessions guide](https://cloud.google.com/dialogflow/cx/docs/concept/session).
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    GoogleCloudDialogflowCxV3MatchIntentRequest googleCloudDialogflowCxV3MatchIntentRequest = new GoogleCloudDialogflowCxV3MatchIntentRequest(); // GoogleCloudDialogflowCxV3MatchIntentRequest | 
    try {
      GoogleCloudDialogflowCxV3MatchIntentResponse result = apiInstance.dialogflowProjectsLocationsAgentsSessionsMatchIntent(session, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDialogflowCxV3MatchIntentRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#dialogflowProjectsLocationsAgentsSessionsMatchIntent");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **session** | **String**| Required. The name of the session this query is sent to. Format: &#x60;projects//locations//agents//sessions/&#x60; or &#x60;projects//locations//agents//environments//sessions/&#x60;. If &#x60;Environment ID&#x60; is not specified, we assume default &#39;draft&#39; environment. It&#39;s up to the API caller to choose an appropriate &#x60;Session ID&#x60;. It can be a random number or some type of session identifiers (preferably hashed). The length of the &#x60;Session ID&#x60; must not exceed 36 characters. For more information, see the [sessions guide](https://cloud.google.com/dialogflow/cx/docs/concept/session). | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **googleCloudDialogflowCxV3MatchIntentRequest** | [**GoogleCloudDialogflowCxV3MatchIntentRequest**](GoogleCloudDialogflowCxV3MatchIntentRequest.md)|  | [optional] |

### Return type

[**GoogleCloudDialogflowCxV3MatchIntentResponse**](GoogleCloudDialogflowCxV3MatchIntentResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dialogflowProjectsLocationsAgentsSessionsServerStreamingDetectIntent"></a>
# **dialogflowProjectsLocationsAgentsSessionsServerStreamingDetectIntent**
> GoogleCloudDialogflowCxV3DetectIntentResponse dialogflowProjectsLocationsAgentsSessionsServerStreamingDetectIntent(session, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDialogflowCxV3DetectIntentRequest)



Processes a natural language query and returns structured, actionable data as a result through server-side streaming. Server-side streaming allows Dialogflow to send [partial responses](https://cloud.google.com/dialogflow/cx/docs/concept/fulfillment#partial-response) earlier in a single request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dialogflow.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String session = "session_example"; // String | Required. The name of the session this query is sent to. Format: `projects//locations//agents//sessions/` or `projects//locations//agents//environments//sessions/`. If `Environment ID` is not specified, we assume default 'draft' environment. It's up to the API caller to choose an appropriate `Session ID`. It can be a random number or some type of session identifiers (preferably hashed). The length of the `Session ID` must not exceed 36 characters. For more information, see the [sessions guide](https://cloud.google.com/dialogflow/cx/docs/concept/session). Note: Always use agent versions for production traffic. See [Versions and environments](https://cloud.google.com/dialogflow/cx/docs/concept/version).
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    GoogleCloudDialogflowCxV3DetectIntentRequest googleCloudDialogflowCxV3DetectIntentRequest = new GoogleCloudDialogflowCxV3DetectIntentRequest(); // GoogleCloudDialogflowCxV3DetectIntentRequest | 
    try {
      GoogleCloudDialogflowCxV3DetectIntentResponse result = apiInstance.dialogflowProjectsLocationsAgentsSessionsServerStreamingDetectIntent(session, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDialogflowCxV3DetectIntentRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#dialogflowProjectsLocationsAgentsSessionsServerStreamingDetectIntent");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **session** | **String**| Required. The name of the session this query is sent to. Format: &#x60;projects//locations//agents//sessions/&#x60; or &#x60;projects//locations//agents//environments//sessions/&#x60;. If &#x60;Environment ID&#x60; is not specified, we assume default &#39;draft&#39; environment. It&#39;s up to the API caller to choose an appropriate &#x60;Session ID&#x60;. It can be a random number or some type of session identifiers (preferably hashed). The length of the &#x60;Session ID&#x60; must not exceed 36 characters. For more information, see the [sessions guide](https://cloud.google.com/dialogflow/cx/docs/concept/session). Note: Always use agent versions for production traffic. See [Versions and environments](https://cloud.google.com/dialogflow/cx/docs/concept/version). | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **googleCloudDialogflowCxV3DetectIntentRequest** | [**GoogleCloudDialogflowCxV3DetectIntentRequest**](GoogleCloudDialogflowCxV3DetectIntentRequest.md)|  | [optional] |

### Return type

[**GoogleCloudDialogflowCxV3DetectIntentResponse**](GoogleCloudDialogflowCxV3DetectIntentResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dialogflowProjectsLocationsAgentsSessionsSubmitAnswerFeedback"></a>
# **dialogflowProjectsLocationsAgentsSessionsSubmitAnswerFeedback**
> GoogleCloudDialogflowCxV3AnswerFeedback dialogflowProjectsLocationsAgentsSessionsSubmitAnswerFeedback(session, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDialogflowCxV3SubmitAnswerFeedbackRequest)



Updates the feedback received from the user for a single turn of the bot response.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dialogflow.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String session = "session_example"; // String | Required. The name of the session the feedback was sent to.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    GoogleCloudDialogflowCxV3SubmitAnswerFeedbackRequest googleCloudDialogflowCxV3SubmitAnswerFeedbackRequest = new GoogleCloudDialogflowCxV3SubmitAnswerFeedbackRequest(); // GoogleCloudDialogflowCxV3SubmitAnswerFeedbackRequest | 
    try {
      GoogleCloudDialogflowCxV3AnswerFeedback result = apiInstance.dialogflowProjectsLocationsAgentsSessionsSubmitAnswerFeedback(session, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDialogflowCxV3SubmitAnswerFeedbackRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#dialogflowProjectsLocationsAgentsSessionsSubmitAnswerFeedback");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **session** | **String**| Required. The name of the session the feedback was sent to. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **googleCloudDialogflowCxV3SubmitAnswerFeedbackRequest** | [**GoogleCloudDialogflowCxV3SubmitAnswerFeedbackRequest**](GoogleCloudDialogflowCxV3SubmitAnswerFeedbackRequest.md)|  | [optional] |

### Return type

[**GoogleCloudDialogflowCxV3AnswerFeedback**](GoogleCloudDialogflowCxV3AnswerFeedback.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dialogflowProjectsLocationsAgentsTestCasesBatchDelete"></a>
# **dialogflowProjectsLocationsAgentsTestCasesBatchDelete**
> Object dialogflowProjectsLocationsAgentsTestCasesBatchDelete(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDialogflowCxV3BatchDeleteTestCasesRequest)



Batch deletes test cases.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dialogflow.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The agent to delete test cases from. Format: `projects//locations//agents/`.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    GoogleCloudDialogflowCxV3BatchDeleteTestCasesRequest googleCloudDialogflowCxV3BatchDeleteTestCasesRequest = new GoogleCloudDialogflowCxV3BatchDeleteTestCasesRequest(); // GoogleCloudDialogflowCxV3BatchDeleteTestCasesRequest | 
    try {
      Object result = apiInstance.dialogflowProjectsLocationsAgentsTestCasesBatchDelete(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDialogflowCxV3BatchDeleteTestCasesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#dialogflowProjectsLocationsAgentsTestCasesBatchDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **parent** | **String**| Required. The agent to delete test cases from. Format: &#x60;projects//locations//agents/&#x60;. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **googleCloudDialogflowCxV3BatchDeleteTestCasesRequest** | [**GoogleCloudDialogflowCxV3BatchDeleteTestCasesRequest**](GoogleCloudDialogflowCxV3BatchDeleteTestCasesRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dialogflowProjectsLocationsAgentsTestCasesBatchRun"></a>
# **dialogflowProjectsLocationsAgentsTestCasesBatchRun**
> GoogleLongrunningOperation dialogflowProjectsLocationsAgentsTestCasesBatchRun(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDialogflowCxV3BatchRunTestCasesRequest)



Kicks off a batch run of test cases. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned &#x60;Operation&#x60; type has the following method-specific fields: - &#x60;metadata&#x60;: BatchRunTestCasesMetadata - &#x60;response&#x60;: BatchRunTestCasesResponse

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dialogflow.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String parent = "parent_example"; // String | Required. Agent name. Format: `projects//locations//agents/ `.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    GoogleCloudDialogflowCxV3BatchRunTestCasesRequest googleCloudDialogflowCxV3BatchRunTestCasesRequest = new GoogleCloudDialogflowCxV3BatchRunTestCasesRequest(); // GoogleCloudDialogflowCxV3BatchRunTestCasesRequest | 
    try {
      GoogleLongrunningOperation result = apiInstance.dialogflowProjectsLocationsAgentsTestCasesBatchRun(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDialogflowCxV3BatchRunTestCasesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#dialogflowProjectsLocationsAgentsTestCasesBatchRun");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **parent** | **String**| Required. Agent name. Format: &#x60;projects//locations//agents/ &#x60;. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **googleCloudDialogflowCxV3BatchRunTestCasesRequest** | [**GoogleCloudDialogflowCxV3BatchRunTestCasesRequest**](GoogleCloudDialogflowCxV3BatchRunTestCasesRequest.md)|  | [optional] |

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dialogflowProjectsLocationsAgentsTestCasesCalculateCoverage"></a>
# **dialogflowProjectsLocationsAgentsTestCasesCalculateCoverage**
> GoogleCloudDialogflowCxV3CalculateCoverageResponse dialogflowProjectsLocationsAgentsTestCasesCalculateCoverage(agent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, type)



Calculates the test coverage for an agent.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dialogflow.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String agent = "agent_example"; // String | Required. The agent to calculate coverage for. Format: `projects//locations//agents/`.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String type = "COVERAGE_TYPE_UNSPECIFIED"; // String | Required. The type of coverage requested.
    try {
      GoogleCloudDialogflowCxV3CalculateCoverageResponse result = apiInstance.dialogflowProjectsLocationsAgentsTestCasesCalculateCoverage(agent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, type);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#dialogflowProjectsLocationsAgentsTestCasesCalculateCoverage");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agent** | **String**| Required. The agent to calculate coverage for. Format: &#x60;projects//locations//agents/&#x60;. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **type** | **String**| Required. The type of coverage requested. | [optional] [enum: COVERAGE_TYPE_UNSPECIFIED, INTENT, PAGE_TRANSITION, TRANSITION_ROUTE_GROUP] |

### Return type

[**GoogleCloudDialogflowCxV3CalculateCoverageResponse**](GoogleCloudDialogflowCxV3CalculateCoverageResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dialogflowProjectsLocationsAgentsTestCasesCreate"></a>
# **dialogflowProjectsLocationsAgentsTestCasesCreate**
> GoogleCloudDialogflowCxV3TestCase dialogflowProjectsLocationsAgentsTestCasesCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDialogflowCxV3TestCase)



Creates a test case for the given agent.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dialogflow.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The agent to create the test case for. Format: `projects//locations//agents/`.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    GoogleCloudDialogflowCxV3TestCase googleCloudDialogflowCxV3TestCase = new GoogleCloudDialogflowCxV3TestCase(); // GoogleCloudDialogflowCxV3TestCase | 
    try {
      GoogleCloudDialogflowCxV3TestCase result = apiInstance.dialogflowProjectsLocationsAgentsTestCasesCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDialogflowCxV3TestCase);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#dialogflowProjectsLocationsAgentsTestCasesCreate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **parent** | **String**| Required. The agent to create the test case for. Format: &#x60;projects//locations//agents/&#x60;. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **googleCloudDialogflowCxV3TestCase** | [**GoogleCloudDialogflowCxV3TestCase**](GoogleCloudDialogflowCxV3TestCase.md)|  | [optional] |

### Return type

[**GoogleCloudDialogflowCxV3TestCase**](GoogleCloudDialogflowCxV3TestCase.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dialogflowProjectsLocationsAgentsTestCasesExport"></a>
# **dialogflowProjectsLocationsAgentsTestCasesExport**
> GoogleLongrunningOperation dialogflowProjectsLocationsAgentsTestCasesExport(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDialogflowCxV3ExportTestCasesRequest)



Exports the test cases under the agent to a Cloud Storage bucket or a local file. Filter can be applied to export a subset of test cases. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned &#x60;Operation&#x60; type has the following method-specific fields: - &#x60;metadata&#x60;: ExportTestCasesMetadata - &#x60;response&#x60;: ExportTestCasesResponse

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dialogflow.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The agent where to export test cases from. Format: `projects//locations//agents/`.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    GoogleCloudDialogflowCxV3ExportTestCasesRequest googleCloudDialogflowCxV3ExportTestCasesRequest = new GoogleCloudDialogflowCxV3ExportTestCasesRequest(); // GoogleCloudDialogflowCxV3ExportTestCasesRequest | 
    try {
      GoogleLongrunningOperation result = apiInstance.dialogflowProjectsLocationsAgentsTestCasesExport(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDialogflowCxV3ExportTestCasesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#dialogflowProjectsLocationsAgentsTestCasesExport");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **parent** | **String**| Required. The agent where to export test cases from. Format: &#x60;projects//locations//agents/&#x60;. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **googleCloudDialogflowCxV3ExportTestCasesRequest** | [**GoogleCloudDialogflowCxV3ExportTestCasesRequest**](GoogleCloudDialogflowCxV3ExportTestCasesRequest.md)|  | [optional] |

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dialogflowProjectsLocationsAgentsTestCasesImport"></a>
# **dialogflowProjectsLocationsAgentsTestCasesImport**
> GoogleLongrunningOperation dialogflowProjectsLocationsAgentsTestCasesImport(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDialogflowCxV3ImportTestCasesRequest)



Imports the test cases from a Cloud Storage bucket or a local file. It always creates new test cases and won&#39;t overwrite any existing ones. The provided ID in the imported test case is neglected. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned &#x60;Operation&#x60; type has the following method-specific fields: - &#x60;metadata&#x60;: ImportTestCasesMetadata - &#x60;response&#x60;: ImportTestCasesResponse

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dialogflow.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The agent to import test cases to. Format: `projects//locations//agents/`.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    GoogleCloudDialogflowCxV3ImportTestCasesRequest googleCloudDialogflowCxV3ImportTestCasesRequest = new GoogleCloudDialogflowCxV3ImportTestCasesRequest(); // GoogleCloudDialogflowCxV3ImportTestCasesRequest | 
    try {
      GoogleLongrunningOperation result = apiInstance.dialogflowProjectsLocationsAgentsTestCasesImport(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDialogflowCxV3ImportTestCasesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#dialogflowProjectsLocationsAgentsTestCasesImport");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **parent** | **String**| Required. The agent to import test cases to. Format: &#x60;projects//locations//agents/&#x60;. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **googleCloudDialogflowCxV3ImportTestCasesRequest** | [**GoogleCloudDialogflowCxV3ImportTestCasesRequest**](GoogleCloudDialogflowCxV3ImportTestCasesRequest.md)|  | [optional] |

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dialogflowProjectsLocationsAgentsTestCasesList"></a>
# **dialogflowProjectsLocationsAgentsTestCasesList**
> GoogleCloudDialogflowCxV3ListTestCasesResponse dialogflowProjectsLocationsAgentsTestCasesList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, pageSize, pageToken, view)



Fetches a list of test cases for a given agent.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dialogflow.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The agent to list all pages for. Format: `projects//locations//agents/`.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    Integer pageSize = 56; // Integer | The maximum number of items to return in a single page. By default 20. Note that when TestCaseView = FULL, the maximum page size allowed is 20. When TestCaseView = BASIC, the maximum page size allowed is 500.
    String pageToken = "pageToken_example"; // String | The next_page_token value returned from a previous list request.
    String view = "TEST_CASE_VIEW_UNSPECIFIED"; // String | Specifies whether response should include all fields or just the metadata.
    try {
      GoogleCloudDialogflowCxV3ListTestCasesResponse result = apiInstance.dialogflowProjectsLocationsAgentsTestCasesList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, pageSize, pageToken, view);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#dialogflowProjectsLocationsAgentsTestCasesList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **parent** | **String**| Required. The agent to list all pages for. Format: &#x60;projects//locations//agents/&#x60;. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **pageSize** | **Integer**| The maximum number of items to return in a single page. By default 20. Note that when TestCaseView &#x3D; FULL, the maximum page size allowed is 20. When TestCaseView &#x3D; BASIC, the maximum page size allowed is 500. | [optional] |
| **pageToken** | **String**| The next_page_token value returned from a previous list request. | [optional] |
| **view** | **String**| Specifies whether response should include all fields or just the metadata. | [optional] [enum: TEST_CASE_VIEW_UNSPECIFIED, BASIC, FULL] |

### Return type

[**GoogleCloudDialogflowCxV3ListTestCasesResponse**](GoogleCloudDialogflowCxV3ListTestCasesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dialogflowProjectsLocationsAgentsTestCasesResultsList"></a>
# **dialogflowProjectsLocationsAgentsTestCasesResultsList**
> GoogleCloudDialogflowCxV3ListTestCaseResultsResponse dialogflowProjectsLocationsAgentsTestCasesResultsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, filter, pageSize, pageToken)



Fetches the list of run results for the given test case. A maximum of 100 results are kept for each test case.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dialogflow.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The test case to list results for. Format: `projects//locations//agents// testCases/`. Specify a `-` as a wildcard for TestCase ID to list results across multiple test cases.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String filter = "filter_example"; // String | The filter expression used to filter test case results. See [API Filtering](https://aip.dev/160). The expression is case insensitive. Only 'AND' is supported for logical operators. The supported syntax is listed below in detail: [AND ] ... [AND latest] The supported fields and operators are: field operator `environment` `=`, `IN` (Use value `draft` for draft environment) `test_time` `>`, `<` `latest` only returns the latest test result in all results for each test case. Examples: * \"environment=draft AND latest\" matches the latest test result for each test case in the draft environment. * \"environment IN (e1,e2)\" matches any test case results with an environment resource name of either \"e1\" or \"e2\". * \"test_time > 1602540713\" matches any test case results with test time later than a unix timestamp in seconds 1602540713.
    Integer pageSize = 56; // Integer | The maximum number of items to return in a single page. By default 100 and at most 1000.
    String pageToken = "pageToken_example"; // String | The next_page_token value returned from a previous list request.
    try {
      GoogleCloudDialogflowCxV3ListTestCaseResultsResponse result = apiInstance.dialogflowProjectsLocationsAgentsTestCasesResultsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, filter, pageSize, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#dialogflowProjectsLocationsAgentsTestCasesResultsList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **parent** | **String**| Required. The test case to list results for. Format: &#x60;projects//locations//agents// testCases/&#x60;. Specify a &#x60;-&#x60; as a wildcard for TestCase ID to list results across multiple test cases. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **filter** | **String**| The filter expression used to filter test case results. See [API Filtering](https://aip.dev/160). The expression is case insensitive. Only &#39;AND&#39; is supported for logical operators. The supported syntax is listed below in detail: [AND ] ... [AND latest] The supported fields and operators are: field operator &#x60;environment&#x60; &#x60;&#x3D;&#x60;, &#x60;IN&#x60; (Use value &#x60;draft&#x60; for draft environment) &#x60;test_time&#x60; &#x60;&gt;&#x60;, &#x60;&lt;&#x60; &#x60;latest&#x60; only returns the latest test result in all results for each test case. Examples: * \&quot;environment&#x3D;draft AND latest\&quot; matches the latest test result for each test case in the draft environment. * \&quot;environment IN (e1,e2)\&quot; matches any test case results with an environment resource name of either \&quot;e1\&quot; or \&quot;e2\&quot;. * \&quot;test_time &gt; 1602540713\&quot; matches any test case results with test time later than a unix timestamp in seconds 1602540713. | [optional] |
| **pageSize** | **Integer**| The maximum number of items to return in a single page. By default 100 and at most 1000. | [optional] |
| **pageToken** | **String**| The next_page_token value returned from a previous list request. | [optional] |

### Return type

[**GoogleCloudDialogflowCxV3ListTestCaseResultsResponse**](GoogleCloudDialogflowCxV3ListTestCaseResultsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dialogflowProjectsLocationsAgentsTestCasesRun"></a>
# **dialogflowProjectsLocationsAgentsTestCasesRun**
> GoogleLongrunningOperation dialogflowProjectsLocationsAgentsTestCasesRun(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDialogflowCxV3RunTestCaseRequest)



Kicks off a test case run. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned &#x60;Operation&#x60; type has the following method-specific fields: - &#x60;metadata&#x60;: RunTestCaseMetadata - &#x60;response&#x60;: RunTestCaseResponse

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dialogflow.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String name = "name_example"; // String | Required. Format of test case name to run: `projects//locations/ /agents//testCases/`.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    GoogleCloudDialogflowCxV3RunTestCaseRequest googleCloudDialogflowCxV3RunTestCaseRequest = new GoogleCloudDialogflowCxV3RunTestCaseRequest(); // GoogleCloudDialogflowCxV3RunTestCaseRequest | 
    try {
      GoogleLongrunningOperation result = apiInstance.dialogflowProjectsLocationsAgentsTestCasesRun(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDialogflowCxV3RunTestCaseRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#dialogflowProjectsLocationsAgentsTestCasesRun");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**| Required. Format of test case name to run: &#x60;projects//locations/ /agents//testCases/&#x60;. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **googleCloudDialogflowCxV3RunTestCaseRequest** | [**GoogleCloudDialogflowCxV3RunTestCaseRequest**](GoogleCloudDialogflowCxV3RunTestCaseRequest.md)|  | [optional] |

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dialogflowProjectsLocationsAgentsTransitionRouteGroupsCreate"></a>
# **dialogflowProjectsLocationsAgentsTransitionRouteGroupsCreate**
> GoogleCloudDialogflowCxV3TransitionRouteGroup dialogflowProjectsLocationsAgentsTransitionRouteGroupsCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, languageCode, googleCloudDialogflowCxV3TransitionRouteGroup)



Creates an TransitionRouteGroup in the specified flow. Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dialogflow.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The flow to create an TransitionRouteGroup for. Format: `projects//locations//agents//flows/` or `projects//locations//agents/` for agent-level groups.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String languageCode = "languageCode_example"; // String | The language of the following fields in `TransitionRouteGroup`: * `TransitionRouteGroup.transition_routes.trigger_fulfillment.messages` * `TransitionRouteGroup.transition_routes.trigger_fulfillment.conditional_cases` If not specified, the agent's default language is used. [Many languages](https://cloud.google.com/dialogflow/cx/docs/reference/language) are supported. Note: languages must be enabled in the agent before they can be used.
    GoogleCloudDialogflowCxV3TransitionRouteGroup googleCloudDialogflowCxV3TransitionRouteGroup = new GoogleCloudDialogflowCxV3TransitionRouteGroup(); // GoogleCloudDialogflowCxV3TransitionRouteGroup | 
    try {
      GoogleCloudDialogflowCxV3TransitionRouteGroup result = apiInstance.dialogflowProjectsLocationsAgentsTransitionRouteGroupsCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, languageCode, googleCloudDialogflowCxV3TransitionRouteGroup);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#dialogflowProjectsLocationsAgentsTransitionRouteGroupsCreate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **parent** | **String**| Required. The flow to create an TransitionRouteGroup for. Format: &#x60;projects//locations//agents//flows/&#x60; or &#x60;projects//locations//agents/&#x60; for agent-level groups. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **languageCode** | **String**| The language of the following fields in &#x60;TransitionRouteGroup&#x60;: * &#x60;TransitionRouteGroup.transition_routes.trigger_fulfillment.messages&#x60; * &#x60;TransitionRouteGroup.transition_routes.trigger_fulfillment.conditional_cases&#x60; If not specified, the agent&#39;s default language is used. [Many languages](https://cloud.google.com/dialogflow/cx/docs/reference/language) are supported. Note: languages must be enabled in the agent before they can be used. | [optional] |
| **googleCloudDialogflowCxV3TransitionRouteGroup** | [**GoogleCloudDialogflowCxV3TransitionRouteGroup**](GoogleCloudDialogflowCxV3TransitionRouteGroup.md)|  | [optional] |

### Return type

[**GoogleCloudDialogflowCxV3TransitionRouteGroup**](GoogleCloudDialogflowCxV3TransitionRouteGroup.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dialogflowProjectsLocationsAgentsTransitionRouteGroupsList"></a>
# **dialogflowProjectsLocationsAgentsTransitionRouteGroupsList**
> GoogleCloudDialogflowCxV3ListTransitionRouteGroupsResponse dialogflowProjectsLocationsAgentsTransitionRouteGroupsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, languageCode, pageSize, pageToken)



Returns the list of all transition route groups in the specified flow.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dialogflow.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The flow to list all transition route groups for. Format: `projects//locations//agents//flows/` or `projects//locations//agents/.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String languageCode = "languageCode_example"; // String | The language to list transition route groups for. The following fields are language dependent: * `TransitionRouteGroup.transition_routes.trigger_fulfillment.messages` * `TransitionRouteGroup.transition_routes.trigger_fulfillment.conditional_cases` If not specified, the agent's default language is used. [Many languages](https://cloud.google.com/dialogflow/cx/docs/reference/language) are supported. Note: languages must be enabled in the agent before they can be used.
    Integer pageSize = 56; // Integer | The maximum number of items to return in a single page. By default 100 and at most 1000.
    String pageToken = "pageToken_example"; // String | The next_page_token value returned from a previous list request.
    try {
      GoogleCloudDialogflowCxV3ListTransitionRouteGroupsResponse result = apiInstance.dialogflowProjectsLocationsAgentsTransitionRouteGroupsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, languageCode, pageSize, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#dialogflowProjectsLocationsAgentsTransitionRouteGroupsList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **parent** | **String**| Required. The flow to list all transition route groups for. Format: &#x60;projects//locations//agents//flows/&#x60; or &#x60;projects//locations//agents/. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **languageCode** | **String**| The language to list transition route groups for. The following fields are language dependent: * &#x60;TransitionRouteGroup.transition_routes.trigger_fulfillment.messages&#x60; * &#x60;TransitionRouteGroup.transition_routes.trigger_fulfillment.conditional_cases&#x60; If not specified, the agent&#39;s default language is used. [Many languages](https://cloud.google.com/dialogflow/cx/docs/reference/language) are supported. Note: languages must be enabled in the agent before they can be used. | [optional] |
| **pageSize** | **Integer**| The maximum number of items to return in a single page. By default 100 and at most 1000. | [optional] |
| **pageToken** | **String**| The next_page_token value returned from a previous list request. | [optional] |

### Return type

[**GoogleCloudDialogflowCxV3ListTransitionRouteGroupsResponse**](GoogleCloudDialogflowCxV3ListTransitionRouteGroupsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dialogflowProjectsLocationsAgentsWebhooksCreate"></a>
# **dialogflowProjectsLocationsAgentsWebhooksCreate**
> GoogleCloudDialogflowCxV3Webhook dialogflowProjectsLocationsAgentsWebhooksCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDialogflowCxV3Webhook)



Creates a webhook in the specified agent.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dialogflow.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The agent to create a webhook for. Format: `projects//locations//agents/`.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    GoogleCloudDialogflowCxV3Webhook googleCloudDialogflowCxV3Webhook = new GoogleCloudDialogflowCxV3Webhook(); // GoogleCloudDialogflowCxV3Webhook | 
    try {
      GoogleCloudDialogflowCxV3Webhook result = apiInstance.dialogflowProjectsLocationsAgentsWebhooksCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDialogflowCxV3Webhook);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#dialogflowProjectsLocationsAgentsWebhooksCreate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **parent** | **String**| Required. The agent to create a webhook for. Format: &#x60;projects//locations//agents/&#x60;. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **googleCloudDialogflowCxV3Webhook** | [**GoogleCloudDialogflowCxV3Webhook**](GoogleCloudDialogflowCxV3Webhook.md)|  | [optional] |

### Return type

[**GoogleCloudDialogflowCxV3Webhook**](GoogleCloudDialogflowCxV3Webhook.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dialogflowProjectsLocationsAgentsWebhooksList"></a>
# **dialogflowProjectsLocationsAgentsWebhooksList**
> GoogleCloudDialogflowCxV3ListWebhooksResponse dialogflowProjectsLocationsAgentsWebhooksList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, pageSize, pageToken)



Returns the list of all webhooks in the specified agent.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dialogflow.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The agent to list all webhooks for. Format: `projects//locations//agents/`.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    Integer pageSize = 56; // Integer | The maximum number of items to return in a single page. By default 100 and at most 1000.
    String pageToken = "pageToken_example"; // String | The next_page_token value returned from a previous list request.
    try {
      GoogleCloudDialogflowCxV3ListWebhooksResponse result = apiInstance.dialogflowProjectsLocationsAgentsWebhooksList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, pageSize, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#dialogflowProjectsLocationsAgentsWebhooksList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **parent** | **String**| Required. The agent to list all webhooks for. Format: &#x60;projects//locations//agents/&#x60;. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **pageSize** | **Integer**| The maximum number of items to return in a single page. By default 100 and at most 1000. | [optional] |
| **pageToken** | **String**| The next_page_token value returned from a previous list request. | [optional] |

### Return type

[**GoogleCloudDialogflowCxV3ListWebhooksResponse**](GoogleCloudDialogflowCxV3ListWebhooksResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dialogflowProjectsLocationsList"></a>
# **dialogflowProjectsLocationsList**
> GoogleCloudLocationListLocationsResponse dialogflowProjectsLocationsList(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, filter, pageSize, pageToken)



Lists information about the supported locations for this service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dialogflow.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String name = "name_example"; // String | The resource that owns the locations collection, if applicable.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String filter = "filter_example"; // String | A filter to narrow down results to a preferred subset. The filtering language accepts strings like `\"displayName=tokyo\"`, and is documented in more detail in [AIP-160](https://google.aip.dev/160).
    Integer pageSize = 56; // Integer | The maximum number of results to return. If not set, the service selects a default.
    String pageToken = "pageToken_example"; // String | A page token received from the `next_page_token` field in the response. Send that page token to receive the subsequent page.
    try {
      GoogleCloudLocationListLocationsResponse result = apiInstance.dialogflowProjectsLocationsList(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, filter, pageSize, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#dialogflowProjectsLocationsList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**| The resource that owns the locations collection, if applicable. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **filter** | **String**| A filter to narrow down results to a preferred subset. The filtering language accepts strings like &#x60;\&quot;displayName&#x3D;tokyo\&quot;&#x60;, and is documented in more detail in [AIP-160](https://google.aip.dev/160). | [optional] |
| **pageSize** | **Integer**| The maximum number of results to return. If not set, the service selects a default. | [optional] |
| **pageToken** | **String**| A page token received from the &#x60;next_page_token&#x60; field in the response. Send that page token to receive the subsequent page. | [optional] |

### Return type

[**GoogleCloudLocationListLocationsResponse**](GoogleCloudLocationListLocationsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dialogflowProjectsLocationsSecuritySettingsCreate"></a>
# **dialogflowProjectsLocationsSecuritySettingsCreate**
> GoogleCloudDialogflowCxV3SecuritySettings dialogflowProjectsLocationsSecuritySettingsCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDialogflowCxV3SecuritySettings)



Create security settings in the specified location.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dialogflow.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The location to create an SecuritySettings for. Format: `projects//locations/`.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    GoogleCloudDialogflowCxV3SecuritySettings googleCloudDialogflowCxV3SecuritySettings = new GoogleCloudDialogflowCxV3SecuritySettings(); // GoogleCloudDialogflowCxV3SecuritySettings | 
    try {
      GoogleCloudDialogflowCxV3SecuritySettings result = apiInstance.dialogflowProjectsLocationsSecuritySettingsCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDialogflowCxV3SecuritySettings);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#dialogflowProjectsLocationsSecuritySettingsCreate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **parent** | **String**| Required. The location to create an SecuritySettings for. Format: &#x60;projects//locations/&#x60;. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **googleCloudDialogflowCxV3SecuritySettings** | [**GoogleCloudDialogflowCxV3SecuritySettings**](GoogleCloudDialogflowCxV3SecuritySettings.md)|  | [optional] |

### Return type

[**GoogleCloudDialogflowCxV3SecuritySettings**](GoogleCloudDialogflowCxV3SecuritySettings.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dialogflowProjectsLocationsSecuritySettingsDelete"></a>
# **dialogflowProjectsLocationsSecuritySettingsDelete**
> Object dialogflowProjectsLocationsSecuritySettingsDelete(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, force)



Deletes the specified SecuritySettings.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dialogflow.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String name = "name_example"; // String | Required. The name of the SecuritySettings to delete. Format: `projects//locations//securitySettings/`.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    Boolean force = true; // Boolean | This field has no effect for webhook not being used. For webhooks that are used by pages/flows/transition route groups: * If `force` is set to false, an error will be returned with message indicating the referenced resources. * If `force` is set to true, Dialogflow will remove the webhook, as well as any references to the webhook (i.e. Webhook and tagin fulfillments that point to this webhook will be removed).
    try {
      Object result = apiInstance.dialogflowProjectsLocationsSecuritySettingsDelete(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, force);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#dialogflowProjectsLocationsSecuritySettingsDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**| Required. The name of the SecuritySettings to delete. Format: &#x60;projects//locations//securitySettings/&#x60;. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **force** | **Boolean**| This field has no effect for webhook not being used. For webhooks that are used by pages/flows/transition route groups: * If &#x60;force&#x60; is set to false, an error will be returned with message indicating the referenced resources. * If &#x60;force&#x60; is set to true, Dialogflow will remove the webhook, as well as any references to the webhook (i.e. Webhook and tagin fulfillments that point to this webhook will be removed). | [optional] |

### Return type

**Object**

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dialogflowProjectsLocationsSecuritySettingsList"></a>
# **dialogflowProjectsLocationsSecuritySettingsList**
> GoogleCloudDialogflowCxV3ListSecuritySettingsResponse dialogflowProjectsLocationsSecuritySettingsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, pageSize, pageToken)



Returns the list of all security settings in the specified location.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dialogflow.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The location to list all security settings for. Format: `projects//locations/`.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    Integer pageSize = 56; // Integer | The maximum number of items to return in a single page. By default 20 and at most 100.
    String pageToken = "pageToken_example"; // String | The next_page_token value returned from a previous list request.
    try {
      GoogleCloudDialogflowCxV3ListSecuritySettingsResponse result = apiInstance.dialogflowProjectsLocationsSecuritySettingsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, pageSize, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#dialogflowProjectsLocationsSecuritySettingsList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **parent** | **String**| Required. The location to list all security settings for. Format: &#x60;projects//locations/&#x60;. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **pageSize** | **Integer**| The maximum number of items to return in a single page. By default 20 and at most 100. | [optional] |
| **pageToken** | **String**| The next_page_token value returned from a previous list request. | [optional] |

### Return type

[**GoogleCloudDialogflowCxV3ListSecuritySettingsResponse**](GoogleCloudDialogflowCxV3ListSecuritySettingsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dialogflowProjectsLocationsSecuritySettingsPatch"></a>
# **dialogflowProjectsLocationsSecuritySettingsPatch**
> GoogleCloudDialogflowCxV3SecuritySettings dialogflowProjectsLocationsSecuritySettingsPatch(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, updateMask, googleCloudDialogflowCxV3SecuritySettings)



Updates the specified SecuritySettings.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dialogflow.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String name = "name_example"; // String | Resource name of the settings. Required for the SecuritySettingsService.UpdateSecuritySettings method. SecuritySettingsService.CreateSecuritySettings populates the name automatically. Format: `projects//locations//securitySettings/`.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String updateMask = "updateMask_example"; // String | Required. The mask to control which fields get updated. If the mask is not present, all fields will be updated.
    GoogleCloudDialogflowCxV3SecuritySettings googleCloudDialogflowCxV3SecuritySettings = new GoogleCloudDialogflowCxV3SecuritySettings(); // GoogleCloudDialogflowCxV3SecuritySettings | 
    try {
      GoogleCloudDialogflowCxV3SecuritySettings result = apiInstance.dialogflowProjectsLocationsSecuritySettingsPatch(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, updateMask, googleCloudDialogflowCxV3SecuritySettings);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#dialogflowProjectsLocationsSecuritySettingsPatch");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**| Resource name of the settings. Required for the SecuritySettingsService.UpdateSecuritySettings method. SecuritySettingsService.CreateSecuritySettings populates the name automatically. Format: &#x60;projects//locations//securitySettings/&#x60;. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **updateMask** | **String**| Required. The mask to control which fields get updated. If the mask is not present, all fields will be updated. | [optional] |
| **googleCloudDialogflowCxV3SecuritySettings** | [**GoogleCloudDialogflowCxV3SecuritySettings**](GoogleCloudDialogflowCxV3SecuritySettings.md)|  | [optional] |

### Return type

[**GoogleCloudDialogflowCxV3SecuritySettings**](GoogleCloudDialogflowCxV3SecuritySettings.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dialogflowProjectsOperationsCancel"></a>
# **dialogflowProjectsOperationsCancel**
> Object dialogflowProjectsOperationsCancel(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType)



Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn&#39;t support this method, it returns &#x60;google.rpc.Code.UNIMPLEMENTED&#x60;. Clients can use Operations.GetOperation or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an Operation.error value with a google.rpc.Status.code of 1, corresponding to &#x60;Code.CANCELLED&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dialogflow.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String name = "name_example"; // String | The name of the operation resource to be cancelled.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    try {
      Object result = apiInstance.dialogflowProjectsOperationsCancel(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#dialogflowProjectsOperationsCancel");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**| The name of the operation resource to be cancelled. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |

### Return type

**Object**

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dialogflowProjectsOperationsGet"></a>
# **dialogflowProjectsOperationsGet**
> GoogleLongrunningOperation dialogflowProjectsOperationsGet(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, languageCode)



Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dialogflow.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String name = "name_example"; // String | The name of the operation resource.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String languageCode = "languageCode_example"; // String | The language to retrieve the transition route group for. The following fields are language dependent: * `TransitionRouteGroup.transition_routes.trigger_fulfillment.messages` * `TransitionRouteGroup.transition_routes.trigger_fulfillment.conditional_cases` If not specified, the agent's default language is used. [Many languages](https://cloud.google.com/dialogflow/cx/docs/reference/language) are supported. Note: languages must be enabled in the agent before they can be used.
    try {
      GoogleLongrunningOperation result = apiInstance.dialogflowProjectsOperationsGet(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, languageCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#dialogflowProjectsOperationsGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**| The name of the operation resource. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **languageCode** | **String**| The language to retrieve the transition route group for. The following fields are language dependent: * &#x60;TransitionRouteGroup.transition_routes.trigger_fulfillment.messages&#x60; * &#x60;TransitionRouteGroup.transition_routes.trigger_fulfillment.conditional_cases&#x60; If not specified, the agent&#39;s default language is used. [Many languages](https://cloud.google.com/dialogflow/cx/docs/reference/language) are supported. Note: languages must be enabled in the agent before they can be used. | [optional] |

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dialogflowProjectsOperationsList"></a>
# **dialogflowProjectsOperationsList**
> GoogleLongrunningListOperationsResponse dialogflowProjectsOperationsList(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, filter, pageSize, pageToken)



Lists operations that match the specified filter in the request. If the server doesn&#39;t support this method, it returns &#x60;UNIMPLEMENTED&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dialogflow.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String name = "name_example"; // String | The name of the operation's parent resource.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String filter = "filter_example"; // String | The standard list filter.
    Integer pageSize = 56; // Integer | The standard list page size.
    String pageToken = "pageToken_example"; // String | The standard list page token.
    try {
      GoogleLongrunningListOperationsResponse result = apiInstance.dialogflowProjectsOperationsList(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, filter, pageSize, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#dialogflowProjectsOperationsList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**| The name of the operation&#39;s parent resource. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **filter** | **String**| The standard list filter. | [optional] |
| **pageSize** | **Integer**| The standard list page size. | [optional] |
| **pageToken** | **String**| The standard list page token. | [optional] |

### Return type

[**GoogleLongrunningListOperationsResponse**](GoogleLongrunningListOperationsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

