# GitHubV3RestApi.ChecksApi

All URIs are relative to *http://HOSTNAME/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checksCreate**](ChecksApi.md#checksCreate) | **POST** /repos/{owner}/{repo}/check-runs | Create a check run
[**checksCreateSuite**](ChecksApi.md#checksCreateSuite) | **POST** /repos/{owner}/{repo}/check-suites | Create a check suite
[**checksGet**](ChecksApi.md#checksGet) | **GET** /repos/{owner}/{repo}/check-runs/{check_run_id} | Get a check run
[**checksGetSuite**](ChecksApi.md#checksGetSuite) | **GET** /repos/{owner}/{repo}/check-suites/{check_suite_id} | Get a check suite
[**checksListAnnotations**](ChecksApi.md#checksListAnnotations) | **GET** /repos/{owner}/{repo}/check-runs/{check_run_id}/annotations | List check run annotations
[**checksListForRef**](ChecksApi.md#checksListForRef) | **GET** /repos/{owner}/{repo}/commits/{ref}/check-runs | List check runs for a Git reference
[**checksListForSuite**](ChecksApi.md#checksListForSuite) | **GET** /repos/{owner}/{repo}/check-suites/{check_suite_id}/check-runs | List check runs in a check suite
[**checksListSuitesForRef**](ChecksApi.md#checksListSuitesForRef) | **GET** /repos/{owner}/{repo}/commits/{ref}/check-suites | List check suites for a Git reference
[**checksRerequestSuite**](ChecksApi.md#checksRerequestSuite) | **POST** /repos/{owner}/{repo}/check-suites/{check_suite_id}/rerequest | Rerequest a check suite
[**checksSetSuitesPreferences**](ChecksApi.md#checksSetSuitesPreferences) | **PATCH** /repos/{owner}/{repo}/check-suites/preferences | Update repository preferences for check suites
[**checksUpdate**](ChecksApi.md#checksUpdate) | **PATCH** /repos/{owner}/{repo}/check-runs/{check_run_id} | Update a check run



## checksCreate

> CheckRun checksCreate(owner, repo, checksCreateRequest)

Create a check run

**Note:** The Checks API only looks for pushes in the repository where the check suite or check run were created. Pushes to a branch in a forked repository are not detected and return an empty &#x60;pull_requests&#x60; array.  Creates a new check run for a specific commit in a repository. Your GitHub App must have the &#x60;checks:write&#x60; permission to create check runs.  In a check suite, GitHub limits the number of check runs with the same name to 1000. Once these check runs exceed 1000, GitHub will start to automatically delete older check runs.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.ChecksApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let checksCreateRequest = {"actions":[{"description":"Allow us to fix these errors for you","identifier":"fix_errors","label":"Fix"}],"completed_at":"2017-11-30T19:49:10Z","conclusion":"success","head_sha":"ce587453ced02b1526dfb4cb910479d431683101","name":"mighty_readme","output":{"annotations":[{"annotation_level":"warning","end_line":2,"message":"Check your spelling for 'banaas'.","path":"README.md","raw_details":"Do you mean 'bananas' or 'banana'?","start_line":2,"title":"Spell Checker"},{"annotation_level":"warning","end_line":4,"message":"Check your spelling for 'aples'","path":"README.md","raw_details":"Do you mean 'apples' or 'Naples'","start_line":4,"title":"Spell Checker"}],"images":[{"alt":"Super bananas","image_url":"http://example.com/images/42"}],"summary":"There are 0 failures, 2 warnings, and 1 notices.","text":"You may have some misspelled words on lines 2 and 4. You also may want to add a section in your README about how to install your app.","title":"Mighty Readme report"},"started_at":"2017-11-30T19:39:10Z","status":"completed"}; // ChecksCreateRequest | 
apiInstance.checksCreate(owner, repo, checksCreateRequest, (error, data, response) => {
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
 **owner** | **String**|  | 
 **repo** | **String**|  | 
 **checksCreateRequest** | [**ChecksCreateRequest**](ChecksCreateRequest.md)|  | 

### Return type

[**CheckRun**](CheckRun.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## checksCreateSuite

> CheckSuite checksCreateSuite(owner, repo, opts)

Create a check suite

**Note:** The Checks API only looks for pushes in the repository where the check suite or check run were created. Pushes to a branch in a forked repository are not detected and return an empty &#x60;pull_requests&#x60; array and a &#x60;null&#x60; value for &#x60;head_branch&#x60;.  By default, check suites are automatically created when you create a [check run](https://docs.github.com/enterprise-server@2.20/rest/reference/checks#check-runs). You only need to use this endpoint for manually creating check suites when you&#39;ve disabled automatic creation using \&quot;[Update repository preferences for check suites](https://docs.github.com/enterprise-server@2.20/rest/reference/checks#update-repository-preferences-for-check-suites)\&quot;. Your GitHub App must have the &#x60;checks:write&#x60; permission to create check suites.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.ChecksApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let opts = {
  'checksCreateSuiteRequest': {"head_sha":"d6fde92930d4715a2b49857d24b940956b26d2d3"} // ChecksCreateSuiteRequest | 
};
apiInstance.checksCreateSuite(owner, repo, opts, (error, data, response) => {
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
 **owner** | **String**|  | 
 **repo** | **String**|  | 
 **checksCreateSuiteRequest** | [**ChecksCreateSuiteRequest**](ChecksCreateSuiteRequest.md)|  | [optional] 

### Return type

[**CheckSuite**](CheckSuite.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## checksGet

> CheckRun checksGet(owner, repo, checkRunId)

Get a check run

**Note:** The Checks API only looks for pushes in the repository where the check suite or check run were created. Pushes to a branch in a forked repository are not detected and return an empty &#x60;pull_requests&#x60; array.  Gets a single check run using its &#x60;id&#x60;. GitHub Apps must have the &#x60;checks:read&#x60; permission on a private repository or pull access to a public repository to get check runs. OAuth Apps and authenticated users must have the &#x60;repo&#x60; scope to get check runs in a private repository.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.ChecksApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let checkRunId = 56; // Number | check_run_id parameter
apiInstance.checksGet(owner, repo, checkRunId, (error, data, response) => {
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
 **owner** | **String**|  | 
 **repo** | **String**|  | 
 **checkRunId** | **Number**| check_run_id parameter | 

### Return type

[**CheckRun**](CheckRun.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## checksGetSuite

> CheckSuite checksGetSuite(owner, repo, checkSuiteId)

Get a check suite

**Note:** The Checks API only looks for pushes in the repository where the check suite or check run were created. Pushes to a branch in a forked repository are not detected and return an empty &#x60;pull_requests&#x60; array and a &#x60;null&#x60; value for &#x60;head_branch&#x60;.  Gets a single check suite using its &#x60;id&#x60;. GitHub Apps must have the &#x60;checks:read&#x60; permission on a private repository or pull access to a public repository to get check suites. OAuth Apps and authenticated users must have the &#x60;repo&#x60; scope to get check suites in a private repository.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.ChecksApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let checkSuiteId = 56; // Number | check_suite_id parameter
apiInstance.checksGetSuite(owner, repo, checkSuiteId, (error, data, response) => {
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
 **owner** | **String**|  | 
 **repo** | **String**|  | 
 **checkSuiteId** | **Number**| check_suite_id parameter | 

### Return type

[**CheckSuite**](CheckSuite.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## checksListAnnotations

> [CheckAnnotation] checksListAnnotations(owner, repo, checkRunId, opts)

List check run annotations

Lists annotations for a check run using the annotation &#x60;id&#x60;. GitHub Apps must have the &#x60;checks:read&#x60; permission on a private repository or pull access to a public repository to get annotations for a check run. OAuth Apps and authenticated users must have the &#x60;repo&#x60; scope to get annotations for a check run in a private repository.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.ChecksApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let checkRunId = 56; // Number | check_run_id parameter
let opts = {
  'perPage': 30, // Number | Results per page (max 100)
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.checksListAnnotations(owner, repo, checkRunId, opts, (error, data, response) => {
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
 **owner** | **String**|  | 
 **repo** | **String**|  | 
 **checkRunId** | **Number**| check_run_id parameter | 
 **perPage** | **Number**| Results per page (max 100) | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[CheckAnnotation]**](CheckAnnotation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## checksListForRef

> ChecksListForSuite200Response checksListForRef(owner, repo, ref, opts)

List check runs for a Git reference

**Note:** The Checks API only looks for pushes in the repository where the check suite or check run were created. Pushes to a branch in a forked repository are not detected and return an empty &#x60;pull_requests&#x60; array.  Lists check runs for a commit ref. The &#x60;ref&#x60; can be a SHA, branch name, or a tag name. GitHub Apps must have the &#x60;checks:read&#x60; permission on a private repository or pull access to a public repository to get check runs. OAuth Apps and authenticated users must have the &#x60;repo&#x60; scope to get check runs in a private repository.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.ChecksApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let ref = "ref_example"; // String | ref parameter
let opts = {
  'checkName': "checkName_example", // String | Returns check runs with the specified `name`.
  'status': "status_example", // String | Returns check runs with the specified `status`. Can be one of `queued`, `in_progress`, or `completed`.
  'filter': "'latest'", // String | Filters check runs by their `completed_at` timestamp. Can be one of `latest` (returning the most recent check runs) or `all`.
  'perPage': 30, // Number | Results per page (max 100)
  'page': 1, // Number | Page number of the results to fetch.
  'appId': 56 // Number | 
};
apiInstance.checksListForRef(owner, repo, ref, opts, (error, data, response) => {
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
 **owner** | **String**|  | 
 **repo** | **String**|  | 
 **ref** | **String**| ref parameter | 
 **checkName** | **String**| Returns check runs with the specified &#x60;name&#x60;. | [optional] 
 **status** | **String**| Returns check runs with the specified &#x60;status&#x60;. Can be one of &#x60;queued&#x60;, &#x60;in_progress&#x60;, or &#x60;completed&#x60;. | [optional] 
 **filter** | **String**| Filters check runs by their &#x60;completed_at&#x60; timestamp. Can be one of &#x60;latest&#x60; (returning the most recent check runs) or &#x60;all&#x60;. | [optional] [default to &#39;latest&#39;]
 **perPage** | **Number**| Results per page (max 100) | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]
 **appId** | **Number**|  | [optional] 

### Return type

[**ChecksListForSuite200Response**](ChecksListForSuite200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## checksListForSuite

> ChecksListForSuite200Response checksListForSuite(owner, repo, checkSuiteId, opts)

List check runs in a check suite

**Note:** The Checks API only looks for pushes in the repository where the check suite or check run were created. Pushes to a branch in a forked repository are not detected and return an empty &#x60;pull_requests&#x60; array.  Lists check runs for a check suite using its &#x60;id&#x60;. GitHub Apps must have the &#x60;checks:read&#x60; permission on a private repository or pull access to a public repository to get check runs. OAuth Apps and authenticated users must have the &#x60;repo&#x60; scope to get check runs in a private repository.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.ChecksApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let checkSuiteId = 56; // Number | check_suite_id parameter
let opts = {
  'checkName': "checkName_example", // String | Returns check runs with the specified `name`.
  'status': "status_example", // String | Returns check runs with the specified `status`. Can be one of `queued`, `in_progress`, or `completed`.
  'filter': "'latest'", // String | Filters check runs by their `completed_at` timestamp. Can be one of `latest` (returning the most recent check runs) or `all`.
  'perPage': 30, // Number | Results per page (max 100)
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.checksListForSuite(owner, repo, checkSuiteId, opts, (error, data, response) => {
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
 **owner** | **String**|  | 
 **repo** | **String**|  | 
 **checkSuiteId** | **Number**| check_suite_id parameter | 
 **checkName** | **String**| Returns check runs with the specified &#x60;name&#x60;. | [optional] 
 **status** | **String**| Returns check runs with the specified &#x60;status&#x60;. Can be one of &#x60;queued&#x60;, &#x60;in_progress&#x60;, or &#x60;completed&#x60;. | [optional] 
 **filter** | **String**| Filters check runs by their &#x60;completed_at&#x60; timestamp. Can be one of &#x60;latest&#x60; (returning the most recent check runs) or &#x60;all&#x60;. | [optional] [default to &#39;latest&#39;]
 **perPage** | **Number**| Results per page (max 100) | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**ChecksListForSuite200Response**](ChecksListForSuite200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## checksListSuitesForRef

> ChecksListSuitesForRef200Response checksListSuitesForRef(owner, repo, ref, opts)

List check suites for a Git reference

**Note:** The Checks API only looks for pushes in the repository where the check suite or check run were created. Pushes to a branch in a forked repository are not detected and return an empty &#x60;pull_requests&#x60; array and a &#x60;null&#x60; value for &#x60;head_branch&#x60;.  Lists check suites for a commit &#x60;ref&#x60;. The &#x60;ref&#x60; can be a SHA, branch name, or a tag name. GitHub Apps must have the &#x60;checks:read&#x60; permission on a private repository or pull access to a public repository to list check suites. OAuth Apps and authenticated users must have the &#x60;repo&#x60; scope to get check suites in a private repository.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.ChecksApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let ref = "ref_example"; // String | ref parameter
let opts = {
  'appId': 1, // Number | Filters check suites by GitHub App `id`.
  'checkName': "checkName_example", // String | Returns check runs with the specified `name`.
  'perPage': 30, // Number | Results per page (max 100)
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.checksListSuitesForRef(owner, repo, ref, opts, (error, data, response) => {
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
 **owner** | **String**|  | 
 **repo** | **String**|  | 
 **ref** | **String**| ref parameter | 
 **appId** | **Number**| Filters check suites by GitHub App &#x60;id&#x60;. | [optional] 
 **checkName** | **String**| Returns check runs with the specified &#x60;name&#x60;. | [optional] 
 **perPage** | **Number**| Results per page (max 100) | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**ChecksListSuitesForRef200Response**](ChecksListSuitesForRef200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## checksRerequestSuite

> Object checksRerequestSuite(owner, repo, checkSuiteId)

Rerequest a check suite

Triggers GitHub to rerequest an existing check suite, without pushing new code to a repository. This endpoint will trigger the [&#x60;check_suite&#x60; webhook](https://docs.github.com/enterprise-server@2.20/webhooks/event-payloads/#check_suite) event with the action &#x60;rerequested&#x60;. When a check suite is &#x60;rerequested&#x60;, its &#x60;status&#x60; is reset to &#x60;queued&#x60; and the &#x60;conclusion&#x60; is cleared.  To rerequest a check suite, your GitHub App must have the &#x60;checks:read&#x60; permission on a private repository or pull access to a public repository.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.ChecksApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let checkSuiteId = 56; // Number | check_suite_id parameter
apiInstance.checksRerequestSuite(owner, repo, checkSuiteId, (error, data, response) => {
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
 **owner** | **String**|  | 
 **repo** | **String**|  | 
 **checkSuiteId** | **Number**| check_suite_id parameter | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## checksSetSuitesPreferences

> CheckSuitePreference checksSetSuitesPreferences(owner, repo, checksSetSuitesPreferencesRequest)

Update repository preferences for check suites

Changes the default automatic flow when creating check suites. By default, a check suite is automatically created each time code is pushed to a repository. When you disable the automatic creation of check suites, you can manually [Create a check suite](https://docs.github.com/enterprise-server@2.20/rest/reference/checks#create-a-check-suite). You must have admin permissions in the repository to set preferences for check suites.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.ChecksApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let checksSetSuitesPreferencesRequest = {"auto_trigger_checks":[{"app_id":4,"setting":false}]}; // ChecksSetSuitesPreferencesRequest | 
apiInstance.checksSetSuitesPreferences(owner, repo, checksSetSuitesPreferencesRequest, (error, data, response) => {
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
 **owner** | **String**|  | 
 **repo** | **String**|  | 
 **checksSetSuitesPreferencesRequest** | [**ChecksSetSuitesPreferencesRequest**](ChecksSetSuitesPreferencesRequest.md)|  | 

### Return type

[**CheckSuitePreference**](CheckSuitePreference.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## checksUpdate

> CheckRun checksUpdate(owner, repo, checkRunId, opts)

Update a check run

**Note:** The Checks API only looks for pushes in the repository where the check suite or check run were created. Pushes to a branch in a forked repository are not detected and return an empty &#x60;pull_requests&#x60; array.  Updates a check run for a specific commit in a repository. Your GitHub App must have the &#x60;checks:write&#x60; permission to edit check runs.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.ChecksApi();
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let checkRunId = 56; // Number | check_run_id parameter
let opts = {
  'checksUpdateRequest': {"completed_at":"2018-05-04T01:14:52Z","conclusion":"success","name":"mighty_readme","output":{"annotations":[{"annotation_level":"warning","end_line":2,"message":"Check your spelling for 'banaas'.","path":"README.md","raw_details":"Do you mean 'bananas' or 'banana'?","start_line":2,"title":"Spell Checker"},{"annotation_level":"warning","end_line":4,"message":"Check your spelling for 'aples'","path":"README.md","raw_details":"Do you mean 'apples' or 'Naples'","start_line":4,"title":"Spell Checker"}],"images":[{"alt":"Super bananas","image_url":"http://example.com/images/42"}],"summary":"There are 0 failures, 2 warnings, and 1 notices.","text":"You may have some misspelled words on lines 2 and 4. You also may want to add a section in your README about how to install your app.","title":"Mighty Readme report"},"started_at":"2018-05-04T01:14:52Z","status":"completed"} // ChecksUpdateRequest | 
};
apiInstance.checksUpdate(owner, repo, checkRunId, opts, (error, data, response) => {
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
 **owner** | **String**|  | 
 **repo** | **String**|  | 
 **checkRunId** | **Number**| check_run_id parameter | 
 **checksUpdateRequest** | [**ChecksUpdateRequest**](ChecksUpdateRequest.md)|  | [optional] 

### Return type

[**CheckRun**](CheckRun.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

