# GitHubV3RestApi.CodeScanningApi

All URIs are relative to *https://github.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**codeScanningDeleteAnalysis**](CodeScanningApi.md#codeScanningDeleteAnalysis) | **DELETE** /repos/{owner}/{repo}/code-scanning/analyses/{analysis_id} | Delete a code scanning analysis from a repository
[**codeScanningGetAlert**](CodeScanningApi.md#codeScanningGetAlert) | **GET** /repos/{owner}/{repo}/code-scanning/alerts/{alert_number} | Get a code scanning alert
[**codeScanningGetAnalysis**](CodeScanningApi.md#codeScanningGetAnalysis) | **GET** /repos/{owner}/{repo}/code-scanning/analyses/{analysis_id} | Get a code scanning analysis for a repository
[**codeScanningGetSarif**](CodeScanningApi.md#codeScanningGetSarif) | **GET** /repos/{owner}/{repo}/code-scanning/sarifs/{sarif_id} | Get information about a SARIF upload
[**codeScanningListAlertInstances**](CodeScanningApi.md#codeScanningListAlertInstances) | **GET** /repos/{owner}/{repo}/code-scanning/alerts/{alert_number}/instances | List instances of a code scanning alert
[**codeScanningListAlertsForRepo**](CodeScanningApi.md#codeScanningListAlertsForRepo) | **GET** /repos/{owner}/{repo}/code-scanning/alerts | List code scanning alerts for a repository
[**codeScanningListRecentAnalyses**](CodeScanningApi.md#codeScanningListRecentAnalyses) | **GET** /repos/{owner}/{repo}/code-scanning/analyses | List code scanning analyses for a repository
[**codeScanningUpdateAlert**](CodeScanningApi.md#codeScanningUpdateAlert) | **PATCH** /repos/{owner}/{repo}/code-scanning/alerts/{alert_number} | Update a code scanning alert
[**codeScanningUploadSarif**](CodeScanningApi.md#codeScanningUploadSarif) | **POST** /repos/{owner}/{repo}/code-scanning/sarifs | Upload an analysis as SARIF data



## codeScanningDeleteAnalysis

> CodeScanningAnalysisDeletion codeScanningDeleteAnalysis(owner, repo, analysisId, opts)

Delete a code scanning analysis from a repository

Deletes a specified code scanning analysis from a repository. For private repositories, you must use an access token with the &#x60;repo&#x60; scope. For public repositories, you must use an access token with &#x60;public_repo&#x60; and &#x60;repo:security_events&#x60; scopes. GitHub Apps must have the &#x60;security_events&#x60; write permission to use this endpoint.  You can delete one analysis at a time. To delete a series of analyses, start with the most recent analysis and work backwards. Conceptually, the process is similar to the undo function in a text editor.  **Note**: The ability to delete analyses was introduced in GitHub Enterprise Server 3.1. You can delete analyses that were generated prior to installing this release, however, if you do so, you will lose information about fixed alerts for all such analyses, for the relevant code scanning tool. We recommend that you only delete analyses that were generated with earlier releases if you don&#39;t need the details of fixed alerts from pre-3.1 releases.  When you list the analyses for a repository, one or more will be identified as deletable in the response:  &#x60;&#x60;&#x60; \&quot;deletable\&quot;: true &#x60;&#x60;&#x60;  An analysis is deletable when it&#39;s the most recent in a set of analyses. Typically, a repository will have multiple sets of analyses for each enabled code scanning tool, where a set is determined by a unique combination of analysis values:  * &#x60;ref&#x60; * &#x60;tool&#x60; * &#x60;analysis_key&#x60; * &#x60;environment&#x60;  If you attempt to delete an analysis that is not the most recent in a set, you&#39;ll get a 400 response with the message:  &#x60;&#x60;&#x60; Analysis specified is not deletable. &#x60;&#x60;&#x60;  The response from a successful &#x60;DELETE&#x60; operation provides you with two alternative URLs for deleting the next analysis in the set (see the example default response below). Use the &#x60;next_analysis_url&#x60; URL if you want to avoid accidentally deleting the final analysis in the set. This is a useful option if you want to preserve at least one analysis for the specified tool in your repository. Use the &#x60;confirm_delete_url&#x60; URL if you are content to remove all analyses for a tool. When you delete the last analysis in a set the value of &#x60;next_analysis_url&#x60; and &#x60;confirm_delete_url&#x60; in the 200 response is &#x60;null&#x60;.  As an example of the deletion process, let&#39;s imagine that you added a workflow that configured a particular code scanning tool to analyze the code in a repository. This tool has added 15 analyses: 10 on the default branch, and another 5 on a topic branch. You therefore have two separate sets of analyses for this tool. You&#39;ve now decided that you want to remove all of the analyses for the tool. To do this you must make 15 separate deletion requests. To start, you must find the deletable analysis for one of the sets, step through deleting the analyses in that set, and then repeat the process for the second set. The procedure therefore consists of a nested loop:  **Outer loop**: * List the analyses for the repository, filtered by tool. * Parse this list to find a deletable analysis. If found:    **Inner loop**:   * Delete the identified analysis.   * Parse the response for the value of &#x60;confirm_delete_url&#x60; and, if found, use this in the next iteration.  The above process assumes that you want to remove all trace of the tool&#39;s analyses from the GitHub user interface, for the specified repository, and it therefore uses the &#x60;confirm_delete_url&#x60; value. Alternatively, you could use the &#x60;next_analysis_url&#x60; value, which would leave the last analysis in each set undeleted to avoid removing a tool&#39;s analysis entirely.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.CodeScanningApi();
let owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
let repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
let analysisId = 56; // Number | The ID of the analysis, as returned from the `GET /repos/{owner}/{repo}/code-scanning/analyses` operation.
let opts = {
  'confirmDelete': "confirmDelete_example" // String | Allow deletion if the specified analysis is the last in a set. If you attempt to delete the final analysis in a set without setting this parameter to `true`, you'll get a 400 response with the message: `Analysis is last of its type and deletion may result in the loss of historical alert data. Please specify confirm_delete.`
};
apiInstance.codeScanningDeleteAnalysis(owner, repo, analysisId, opts, (error, data, response) => {
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
 **owner** | **String**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **String**| The name of the repository. The name is not case sensitive. | 
 **analysisId** | **Number**| The ID of the analysis, as returned from the &#x60;GET /repos/{owner}/{repo}/code-scanning/analyses&#x60; operation. | 
 **confirmDelete** | **String**| Allow deletion if the specified analysis is the last in a set. If you attempt to delete the final analysis in a set without setting this parameter to &#x60;true&#x60;, you&#39;ll get a 400 response with the message: &#x60;Analysis is last of its type and deletion may result in the loss of historical alert data. Please specify confirm_delete.&#x60; | [optional] 

### Return type

[**CodeScanningAnalysisDeletion**](CodeScanningAnalysisDeletion.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/scim+json


## codeScanningGetAlert

> CodeScanningAlert codeScanningGetAlert(owner, repo, alertNumber)

Get a code scanning alert

Gets a single code scanning alert. You must use an access token with the &#x60;security_events&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;security_events&#x60; read permission to use this endpoint.  **Deprecation notice**: The instances field is deprecated and will, in future, not be included in the response for this endpoint. The example response reflects this change. The same information can now be retrieved via a GET request to the URL specified by &#x60;instances_url&#x60;.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.CodeScanningApi();
let owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
let repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
let alertNumber = 56; // Number | The number that identifies an alert. You can find this at the end of the URL for a code scanning alert within GitHub, and in the `number` field in the response from the `GET /repos/{owner}/{repo}/code-scanning/alerts` operation.
apiInstance.codeScanningGetAlert(owner, repo, alertNumber, (error, data, response) => {
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
 **owner** | **String**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **String**| The name of the repository. The name is not case sensitive. | 
 **alertNumber** | **Number**| The number that identifies an alert. You can find this at the end of the URL for a code scanning alert within GitHub, and in the &#x60;number&#x60; field in the response from the &#x60;GET /repos/{owner}/{repo}/code-scanning/alerts&#x60; operation. | 

### Return type

[**CodeScanningAlert**](CodeScanningAlert.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## codeScanningGetAnalysis

> CodeScanningAnalysis codeScanningGetAnalysis(owner, repo, analysisId)

Get a code scanning analysis for a repository

Gets a specified code scanning analysis for a repository. You must use an access token with the &#x60;security_events&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;security_events&#x60; read permission to use this endpoint.  The default JSON response contains fields that describe the analysis. This includes the Git reference and commit SHA to which the analysis relates, the datetime of the analysis, the name of the code scanning tool, and the number of alerts.  The &#x60;rules_count&#x60; field in the default response give the number of rules that were run in the analysis. For very old analyses this data is not available, and &#x60;0&#x60; is returned in this field.  If you use the Accept header &#x60;application/sarif+json&#x60;, the response contains the analysis data that was uploaded. This is formatted as [SARIF version 2.1.0](https://docs.oasis-open.org/sarif/sarif/v2.1.0/cs01/sarif-v2.1.0-cs01.html).

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.CodeScanningApi();
let owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
let repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
let analysisId = 56; // Number | The ID of the analysis, as returned from the `GET /repos/{owner}/{repo}/code-scanning/analyses` operation.
apiInstance.codeScanningGetAnalysis(owner, repo, analysisId, (error, data, response) => {
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
 **owner** | **String**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **String**| The name of the repository. The name is not case sensitive. | 
 **analysisId** | **Number**| The ID of the analysis, as returned from the &#x60;GET /repos/{owner}/{repo}/code-scanning/analyses&#x60; operation. | 

### Return type

[**CodeScanningAnalysis**](CodeScanningAnalysis.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json+sarif


## codeScanningGetSarif

> CodeScanningSarifsStatus codeScanningGetSarif(owner, repo, sarifId)

Get information about a SARIF upload

Gets information about a SARIF upload, including the status and the URL of the analysis that was uploaded so that you can retrieve details of the analysis. For more information, see \&quot;[Get a code scanning analysis for a repository](/rest/reference/code-scanning#get-a-code-scanning-analysis-for-a-repository).\&quot; You must use an access token with the &#x60;security_events&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;security_events&#x60; read permission to use this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.CodeScanningApi();
let owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
let repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
let sarifId = "sarifId_example"; // String | The SARIF ID obtained after uploading.
apiInstance.codeScanningGetSarif(owner, repo, sarifId, (error, data, response) => {
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
 **owner** | **String**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **String**| The name of the repository. The name is not case sensitive. | 
 **sarifId** | **String**| The SARIF ID obtained after uploading. | 

### Return type

[**CodeScanningSarifsStatus**](CodeScanningSarifsStatus.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## codeScanningListAlertInstances

> [CodeScanningAlertInstance] codeScanningListAlertInstances(owner, repo, alertNumber, opts)

List instances of a code scanning alert

Lists all instances of the specified code scanning alert. You must use an access token with the &#x60;security_events&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;security_events&#x60; read permission to use this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.CodeScanningApi();
let owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
let repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
let alertNumber = 56; // Number | The number that identifies an alert. You can find this at the end of the URL for a code scanning alert within GitHub, and in the `number` field in the response from the `GET /repos/{owner}/{repo}/code-scanning/alerts` operation.
let opts = {
  'page': 1, // Number | Page number of the results to fetch.
  'perPage': 30, // Number | The number of results per page (max 100).
  'ref': "ref_example" // String | The Git reference for the results you want to list. The `ref` for a branch can be formatted either as `refs/heads/<branch name>` or simply `<branch name>`. To reference a pull request use `refs/pull/<number>/merge`.
};
apiInstance.codeScanningListAlertInstances(owner, repo, alertNumber, opts, (error, data, response) => {
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
 **owner** | **String**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **String**| The name of the repository. The name is not case sensitive. | 
 **alertNumber** | **Number**| The number that identifies an alert. You can find this at the end of the URL for a code scanning alert within GitHub, and in the &#x60;number&#x60; field in the response from the &#x60;GET /repos/{owner}/{repo}/code-scanning/alerts&#x60; operation. | 
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]
 **ref** | **String**| The Git reference for the results you want to list. The &#x60;ref&#x60; for a branch can be formatted either as &#x60;refs/heads/&lt;branch name&gt;&#x60; or simply &#x60;&lt;branch name&gt;&#x60;. To reference a pull request use &#x60;refs/pull/&lt;number&gt;/merge&#x60;. | [optional] 

### Return type

[**[CodeScanningAlertInstance]**](CodeScanningAlertInstance.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## codeScanningListAlertsForRepo

> [CodeScanningAlertItems] codeScanningListAlertsForRepo(owner, repo, opts)

List code scanning alerts for a repository

Lists all open code scanning alerts for the default branch (usually &#x60;main&#x60; or &#x60;master&#x60;). You must use an access token with the &#x60;security_events&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;security_events&#x60; read permission to use this endpoint.  The response includes a &#x60;most_recent_instance&#x60; object. This provides details of the most recent instance of this alert for the default branch or for the specified Git reference (if you used &#x60;ref&#x60; in the request).

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.CodeScanningApi();
let owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
let repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
let opts = {
  'toolName': "toolName_example", // String | The name of a code scanning tool. Only results by this tool will be listed. You can specify the tool by using either `tool_name` or `tool_guid`, but not both.
  'toolGuid': "toolGuid_example", // String | The GUID of a code scanning tool. Only results by this tool will be listed. Note that some code scanning tools may not include a GUID in their analysis data. You can specify the tool by using either `tool_guid` or `tool_name`, but not both.
  'page': 1, // Number | Page number of the results to fetch.
  'perPage': 30, // Number | The number of results per page (max 100).
  'ref': "ref_example", // String | The Git reference for the results you want to list. The `ref` for a branch can be formatted either as `refs/heads/<branch name>` or simply `<branch name>`. To reference a pull request use `refs/pull/<number>/merge`.
  'state': new GitHubV3RestApi.CodeScanningAlertState() // CodeScanningAlertState | Set to `open`, `fixed`, or `dismissed` to list code scanning alerts in a specific state.
};
apiInstance.codeScanningListAlertsForRepo(owner, repo, opts, (error, data, response) => {
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
 **owner** | **String**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **String**| The name of the repository. The name is not case sensitive. | 
 **toolName** | **String**| The name of a code scanning tool. Only results by this tool will be listed. You can specify the tool by using either &#x60;tool_name&#x60; or &#x60;tool_guid&#x60;, but not both. | [optional] 
 **toolGuid** | **String**| The GUID of a code scanning tool. Only results by this tool will be listed. Note that some code scanning tools may not include a GUID in their analysis data. You can specify the tool by using either &#x60;tool_guid&#x60; or &#x60;tool_name&#x60;, but not both. | [optional] 
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]
 **ref** | **String**| The Git reference for the results you want to list. The &#x60;ref&#x60; for a branch can be formatted either as &#x60;refs/heads/&lt;branch name&gt;&#x60; or simply &#x60;&lt;branch name&gt;&#x60;. To reference a pull request use &#x60;refs/pull/&lt;number&gt;/merge&#x60;. | [optional] 
 **state** | [**CodeScanningAlertState**](.md)| Set to &#x60;open&#x60;, &#x60;fixed&#x60;, or &#x60;dismissed&#x60; to list code scanning alerts in a specific state. | [optional] 

### Return type

[**[CodeScanningAlertItems]**](CodeScanningAlertItems.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## codeScanningListRecentAnalyses

> [CodeScanningAnalysis] codeScanningListRecentAnalyses(owner, repo, opts)

List code scanning analyses for a repository

Lists the details of all code scanning analyses for a repository, starting with the most recent. The response is paginated and you can use the &#x60;page&#x60; and &#x60;per_page&#x60; parameters to list the analyses you&#39;re interested in. By default 30 analyses are listed per page.  The &#x60;rules_count&#x60; field in the response give the number of rules that were run in the analysis. For very old analyses this data is not available, and &#x60;0&#x60; is returned in this field.  You must use an access token with the &#x60;security_events&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;security_events&#x60; read permission to use this endpoint.  **Deprecation notice**: The &#x60;tool_name&#x60; field is deprecated and will, in future, not be included in the response for this endpoint. The example response reflects this change. The tool name can now be found inside the &#x60;tool&#x60; field.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.CodeScanningApi();
let owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
let repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
let opts = {
  'toolName': "toolName_example", // String | The name of a code scanning tool. Only results by this tool will be listed. You can specify the tool by using either `tool_name` or `tool_guid`, but not both.
  'toolGuid': "toolGuid_example", // String | The GUID of a code scanning tool. Only results by this tool will be listed. Note that some code scanning tools may not include a GUID in their analysis data. You can specify the tool by using either `tool_guid` or `tool_name`, but not both.
  'page': 1, // Number | Page number of the results to fetch.
  'perPage': 30, // Number | The number of results per page (max 100).
  'ref': "ref_example", // String | The Git reference for the analyses you want to list. The `ref` for a branch can be formatted either as `refs/heads/<branch name>` or simply `<branch name>`. To reference a pull request use `refs/pull/<number>/merge`.
  'sarifId': "sarifId_example" // String | Filter analyses belonging to the same SARIF upload.
};
apiInstance.codeScanningListRecentAnalyses(owner, repo, opts, (error, data, response) => {
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
 **owner** | **String**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **String**| The name of the repository. The name is not case sensitive. | 
 **toolName** | **String**| The name of a code scanning tool. Only results by this tool will be listed. You can specify the tool by using either &#x60;tool_name&#x60; or &#x60;tool_guid&#x60;, but not both. | [optional] 
 **toolGuid** | **String**| The GUID of a code scanning tool. Only results by this tool will be listed. Note that some code scanning tools may not include a GUID in their analysis data. You can specify the tool by using either &#x60;tool_guid&#x60; or &#x60;tool_name&#x60;, but not both. | [optional] 
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]
 **ref** | **String**| The Git reference for the analyses you want to list. The &#x60;ref&#x60; for a branch can be formatted either as &#x60;refs/heads/&lt;branch name&gt;&#x60; or simply &#x60;&lt;branch name&gt;&#x60;. To reference a pull request use &#x60;refs/pull/&lt;number&gt;/merge&#x60;. | [optional] 
 **sarifId** | **String**| Filter analyses belonging to the same SARIF upload. | [optional] 

### Return type

[**[CodeScanningAnalysis]**](CodeScanningAnalysis.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## codeScanningUpdateAlert

> CodeScanningAlert codeScanningUpdateAlert(owner, repo, alertNumber, codeScanningUpdateAlertRequest)

Update a code scanning alert

Updates the status of a single code scanning alert. You must use an access token with the &#x60;security_events&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;security_events&#x60; write permission to use this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.CodeScanningApi();
let owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
let repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
let alertNumber = 56; // Number | The number that identifies an alert. You can find this at the end of the URL for a code scanning alert within GitHub, and in the `number` field in the response from the `GET /repos/{owner}/{repo}/code-scanning/alerts` operation.
let codeScanningUpdateAlertRequest = {"dismissed_comment":"This alert is not actually correct, because there's a sanitizer included in the library.","dismissed_reason":"false positive","state":"dismissed"}; // CodeScanningUpdateAlertRequest | 
apiInstance.codeScanningUpdateAlert(owner, repo, alertNumber, codeScanningUpdateAlertRequest, (error, data, response) => {
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
 **owner** | **String**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **String**| The name of the repository. The name is not case sensitive. | 
 **alertNumber** | **Number**| The number that identifies an alert. You can find this at the end of the URL for a code scanning alert within GitHub, and in the &#x60;number&#x60; field in the response from the &#x60;GET /repos/{owner}/{repo}/code-scanning/alerts&#x60; operation. | 
 **codeScanningUpdateAlertRequest** | [**CodeScanningUpdateAlertRequest**](CodeScanningUpdateAlertRequest.md)|  | 

### Return type

[**CodeScanningAlert**](CodeScanningAlert.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## codeScanningUploadSarif

> CodeScanningSarifsReceipt codeScanningUploadSarif(owner, repo, codeScanningUploadSarifRequest)

Upload an analysis as SARIF data

Uploads SARIF data containing the results of a code scanning analysis to make the results available in a repository. You must use an access token with the &#x60;security_events&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;security_events&#x60; write permission to use this endpoint.  There are two places where you can upload code scanning results.  - If you upload to a pull request, for example &#x60;--ref refs/pull/42/merge&#x60; or &#x60;--ref refs/pull/42/head&#x60;, then the results appear as alerts in a pull request check. For more information, see \&quot;[Triaging code scanning alerts in pull requests](/code-security/secure-coding/triaging-code-scanning-alerts-in-pull-requests).\&quot;  - If you upload to a branch, for example &#x60;--ref refs/heads/my-branch&#x60;, then the results appear in the **Security** tab for your repository. For more information, see \&quot;[Managing code scanning alerts for your repository](/code-security/secure-coding/managing-code-scanning-alerts-for-your-repository#viewing-the-alerts-for-a-repository).\&quot;  You must compress the SARIF-formatted analysis data that you want to upload, using &#x60;gzip&#x60;, and then encode it as a Base64 format string. For example: &#x60;&#x60;&#x60; gzip -c analysis-data.sarif | base64 -w0 &#x60;&#x60;&#x60;  &lt;br&gt; SARIF upload supports a maximum number of entries per the following data objects, and an analysis will be rejected if any of these objects is above its maximum value. For some objects, there are additional values over which the entries will be ignored while keeping the most important entries whenever applicable. To get the most out of your analysis when it includes data above the supported limits, try to optimize the analysis configuration. For example, for the CodeQL tool, identify and remove the most noisy queries.  | **SARIF data**                   | **Maximum values** | **Additional limits**                                                            | |----------------------------------|:------------------:|----------------------------------------------------------------------------------| | Runs per file                    |         15         |                                                                                  | | Results per run                  |       25,000       | Only the top 5,000 results will be included, prioritized by severity.            | | Rules per run                    |       25,000       |                                                                                  | | Thread Flow Locations per result |       10,000       | Only the top 1,000 Thread Flow Locations will be included, using prioritization. | | Location per result              |       1,000        | Only 100 locations will be included.                                             |  The &#x60;202 Accepted&#x60; response includes an &#x60;id&#x60; value. You can use this ID to check the status of the upload by using it in the &#x60;/sarifs/{sarif_id}&#x60; endpoint. For more information, see \&quot;[Get information about a SARIF upload](/rest/reference/code-scanning#get-information-about-a-sarif-upload).\&quot;

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.CodeScanningApi();
let owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
let repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
let codeScanningUploadSarifRequest = {"commit_sha":"4b6472266afd7b471e86085a6659e8c7f2b119da","ref":"refs/heads/master","sarif":"H4sICMLGdF4AA2V4YW1wbGUuc2FyaWYAvVjdbts2FL7PUxDCijaA/CM7iRNfLkPXYgHSNstumlzQ0pHFVCI1korjFgH2ONtr7Ul2KFmy/mOn6QIkjsjDw0/nfN85NL8dEGL9pNwAImqRObECrWM1H40kXQ2XTAfJIlEgXcE1cD10RTQSVDE10K4aKSqZP1AxuKOIKg1ydJU60jSfSh8Hk6EzHA/vlOCWbfa7B6kYPpj90rlsWCZcmbHP5Bs+4oAWIjQD2SMOeJLh2vIQDnIaQerqXHjw8YIgxohybxAyDsS4cAPKsp03K4RcUs6+Up2D+JXpd8mibKIQN9fM/aMCdbyBujGSSQgVxJtx5qX2d2qUcIweQhEuDQf3GBO6CKHkogx/N3MVCKl/AeVKFuf4y5ubsMGDTj1ep+5I7sgmLIpxtU38hLtmMRGSuCFVyip5eKzs5ydh+LztVL6f2m6oih1BkYiuyQIIJWodxVpERPj4sEiWBNNH8EWT0DMG8EAjzKVHXCrB4FkPu/F64NMk1OeC+2yZSNoBOoR7CC0EzYWGbm+xFDFIzbI011+cLjfZtyJkmMZfumAh02uL3NpV2y+MZ6RAjxibyKrNxxJcVjANSb4eBGwZ1M0KsuyR2poLr5rMl8vaDSeVn6eTWEO2j2xIEcmhwlTKNOi4GMOI8gfuZYkvJ7b4v5Tiumyz7RnHeodFzpS8ASIZCH/AYdWi2z3sG8JtFxJ6fF9yR9CdifBr9Pd6d5V2+zbJKjjCFGGmsHuYFy2ytJq9tUxcLSRSQecppOGKrpUxYfxefMEFK+wOGa4hudQByBVT0L+EKtyACxnRsABhEx1QjVDs1KNI9MbpnhqfE45B6FJvu3hRu5VRU9MhZLmK7fqkKyQSTHNoyMqUFMqXCV3CwAeqEwmVokraK8IuBaGvHjQ0gMYrKjnjyw7uk9uD8tgmsBbFMPnU1bV2ZhkJNkuolUiWys3UPWzs5aaIUz9TBe8zMb+6+nT+6fLy91dlE3xzeDDT4zYszb0bW6NjJd0Rvn2EnLvWLFSdKPpBzInzfRgu8ETyMcH8nIfMnJCeC2PyfTA+UKngcnGH7Hw2hGkVQs5YlIRCtdWZYQ4/73es2JlxkfViOEIhoWJq5Oo6UBBfiKIqFBWhiE3jJGbFwVoxBHTRSuIS67sMeplei24X20shLjG+8gqbKC/bESiNMC+wd5q5id0yeS7CJEqXzmrTWNq3k05l84P6f4/bEmXFJjI0fIt1BGQssUnUDkBYeVhE5TqPnMH3jqogDcP0zKcTgLPTMSzOjhbjuVOmW23l1fYNStulfo6sXlFsGLhbDy5RECPRYGCTgOj2bd4nUQEivEd0H7KKYxqnEhFohuur3a3UPskbH/+Yg0+M5P2MHRJu3ziHh3Z2NCrWt3XF1rWTw8Ne/pfbWYXnDSE0SNZQQt1i18q7te2vOhu7ehWuvVyeu0wbLZi24mhoo6aOOTltzG/lgdVvVoXQq5V+pewkFIzL8fjEcadT55jOjpzFzHuOTtDNrMkJPMVQDd7F09RID72O/UPZ0tmctqZ7kWX6EmSZnDpP8GU67SXM8XE3YSrxbKsx6UReZ4y6n/FVZfJjs9Z7stma75W5yQtkzjk5eSJxk1lv4o7+j8TlhaJ2lsKWZO6lruDPBLib3x5ZN/KGWzZ+pn///evv7OOf4iIBv3oY9L/l1wiJ9p0Tc+F1zZnOE9NxXWEus6IQhr5pMfoqxi8WPsuu0azsns4UC6WzNzHIzbeEx4P/AJ3SefgcFAAA"}; // CodeScanningUploadSarifRequest | 
apiInstance.codeScanningUploadSarif(owner, repo, codeScanningUploadSarifRequest, (error, data, response) => {
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
 **owner** | **String**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **String**| The name of the repository. The name is not case sensitive. | 
 **codeScanningUploadSarifRequest** | [**CodeScanningUploadSarifRequest**](CodeScanningUploadSarifRequest.md)|  | 

### Return type

[**CodeScanningSarifsReceipt**](CodeScanningSarifsReceipt.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

