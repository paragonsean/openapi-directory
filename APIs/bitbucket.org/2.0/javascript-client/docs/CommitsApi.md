# BitbucketApi.CommitsApi

All URIs are relative to *https://api.bitbucket.org/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulkCreateOrUpdateAnnotations_0**](CommitsApi.md#bulkCreateOrUpdateAnnotations_0) | **POST** /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}/annotations | Bulk create or update annotations
[**createOrUpdateAnnotation_0**](CommitsApi.md#createOrUpdateAnnotation_0) | **PUT** /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}/annotations/{annotationId} | Create or update an annotation
[**createOrUpdateReport_0**](CommitsApi.md#createOrUpdateReport_0) | **PUT** /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId} | Create or update a report
[**deleteAnnotation_0**](CommitsApi.md#deleteAnnotation_0) | **DELETE** /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}/annotations/{annotationId} | Delete an annotation
[**deleteReport_0**](CommitsApi.md#deleteReport_0) | **DELETE** /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId} | Delete a report
[**getAnnotation_0**](CommitsApi.md#getAnnotation_0) | **GET** /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}/annotations/{annotationId} | Get an annotation
[**getAnnotationsForReport_0**](CommitsApi.md#getAnnotationsForReport_0) | **GET** /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}/annotations | List annotations
[**getReport_0**](CommitsApi.md#getReport_0) | **GET** /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId} | Get a report
[**getReportsForCommit_0**](CommitsApi.md#getReportsForCommit_0) | **GET** /repositories/{workspace}/{repo_slug}/commit/{commit}/reports | List reports
[**repositoriesWorkspaceRepoSlugCommitCommitApproveDelete**](CommitsApi.md#repositoriesWorkspaceRepoSlugCommitCommitApproveDelete) | **DELETE** /repositories/{workspace}/{repo_slug}/commit/{commit}/approve | Unapprove a commit
[**repositoriesWorkspaceRepoSlugCommitCommitApprovePost**](CommitsApi.md#repositoriesWorkspaceRepoSlugCommitCommitApprovePost) | **POST** /repositories/{workspace}/{repo_slug}/commit/{commit}/approve | Approve a commit
[**repositoriesWorkspaceRepoSlugCommitCommitCommentsCommentIdDelete**](CommitsApi.md#repositoriesWorkspaceRepoSlugCommitCommitCommentsCommentIdDelete) | **DELETE** /repositories/{workspace}/{repo_slug}/commit/{commit}/comments/{comment_id} | Delete a commit comment
[**repositoriesWorkspaceRepoSlugCommitCommitCommentsCommentIdGet**](CommitsApi.md#repositoriesWorkspaceRepoSlugCommitCommitCommentsCommentIdGet) | **GET** /repositories/{workspace}/{repo_slug}/commit/{commit}/comments/{comment_id} | Get a commit comment
[**repositoriesWorkspaceRepoSlugCommitCommitCommentsCommentIdPut**](CommitsApi.md#repositoriesWorkspaceRepoSlugCommitCommitCommentsCommentIdPut) | **PUT** /repositories/{workspace}/{repo_slug}/commit/{commit}/comments/{comment_id} | Update a commit comment
[**repositoriesWorkspaceRepoSlugCommitCommitCommentsGet**](CommitsApi.md#repositoriesWorkspaceRepoSlugCommitCommitCommentsGet) | **GET** /repositories/{workspace}/{repo_slug}/commit/{commit}/comments | List a commit&#39;s comments
[**repositoriesWorkspaceRepoSlugCommitCommitCommentsPost**](CommitsApi.md#repositoriesWorkspaceRepoSlugCommitCommitCommentsPost) | **POST** /repositories/{workspace}/{repo_slug}/commit/{commit}/comments | Create comment for a commit
[**repositoriesWorkspaceRepoSlugCommitCommitGet**](CommitsApi.md#repositoriesWorkspaceRepoSlugCommitCommitGet) | **GET** /repositories/{workspace}/{repo_slug}/commit/{commit} | Get a commit
[**repositoriesWorkspaceRepoSlugCommitsGet**](CommitsApi.md#repositoriesWorkspaceRepoSlugCommitsGet) | **GET** /repositories/{workspace}/{repo_slug}/commits | List commits
[**repositoriesWorkspaceRepoSlugCommitsPost**](CommitsApi.md#repositoriesWorkspaceRepoSlugCommitsPost) | **POST** /repositories/{workspace}/{repo_slug}/commits | List commits with include/exclude
[**repositoriesWorkspaceRepoSlugCommitsRevisionGet**](CommitsApi.md#repositoriesWorkspaceRepoSlugCommitsRevisionGet) | **GET** /repositories/{workspace}/{repo_slug}/commits/{revision} | List commits for revision
[**repositoriesWorkspaceRepoSlugCommitsRevisionPost**](CommitsApi.md#repositoriesWorkspaceRepoSlugCommitsRevisionPost) | **POST** /repositories/{workspace}/{repo_slug}/commits/{revision} | List commits for revision using include/exclude
[**repositoriesWorkspaceRepoSlugDiffSpecGet**](CommitsApi.md#repositoriesWorkspaceRepoSlugDiffSpecGet) | **GET** /repositories/{workspace}/{repo_slug}/diff/{spec} | Compare two commits
[**repositoriesWorkspaceRepoSlugDiffstatSpecGet**](CommitsApi.md#repositoriesWorkspaceRepoSlugDiffstatSpecGet) | **GET** /repositories/{workspace}/{repo_slug}/diffstat/{spec} | Compare two commit diff stats
[**repositoriesWorkspaceRepoSlugMergeBaseRevspecGet**](CommitsApi.md#repositoriesWorkspaceRepoSlugMergeBaseRevspecGet) | **GET** /repositories/{workspace}/{repo_slug}/merge-base/{revspec} | Get the common ancestor between two commits
[**repositoriesWorkspaceRepoSlugPatchSpecGet**](CommitsApi.md#repositoriesWorkspaceRepoSlugPatchSpecGet) | **GET** /repositories/{workspace}/{repo_slug}/patch/{spec} | Get a patch for two commits



## bulkCreateOrUpdateAnnotations_0

> [ReportAnnotation] bulkCreateOrUpdateAnnotations_0(workspace, repoSlug, commit, reportId, reportAnnotation)

Bulk create or update annotations

Bulk upload of annotations. Annotations are individual findings that have been identified as part of a report, for example, a line of code that represents a vulnerability. These annotations can be attached to a specific file and even a specific line in that file, however, that is optional. Annotations are not mandatory and a report can contain up to 1000 annotations.  Add the annotations you want to upload as objects in a JSON array and make sure each annotation has the external_id field set to a unique value. If you want to use an existing id from your own system, we recommend prefixing it with your system&#39;s name to avoid collisions, for example, mySystem-annotation001. The external id can later be used to identify the report as an alternative to the generated [UUID](https://developer.atlassian.com/bitbucket/api/2/reference/meta/uri-uuid#uuid). You can upload up to 100 annotations per POST request.  ### Sample cURL request: &#x60;&#x60;&#x60; curl --location &#39;https://api.bitbucket.org/2.0/repositories/&lt;username&gt;/&lt;reposity-name&gt;/commit/&lt;commit-hash&gt;/reports/mysystem-001/annotations&#39; \\ --header &#39;Content-Type: application/json&#39; \\ --data-raw &#39;[   {         \&quot;external_id\&quot;: \&quot;mysystem-annotation001\&quot;,         \&quot;title\&quot;: \&quot;Security scan report\&quot;,         \&quot;annotation_type\&quot;: \&quot;VULNERABILITY\&quot;,         \&quot;summary\&quot;: \&quot;This line represents a security threat.\&quot;,         \&quot;severity\&quot;: \&quot;HIGH\&quot;,       \&quot;path\&quot;: \&quot;my-service/src/main/java/com/myCompany/mysystem/logic/Main.java\&quot;,         \&quot;line\&quot;: 42   },   {         \&quot;external_id\&quot;: \&quot;mySystem-annotation002\&quot;,         \&quot;title\&quot;: \&quot;Bug report\&quot;,         \&quot;annotation_type\&quot;: \&quot;BUG\&quot;,         \&quot;result\&quot;: \&quot;FAILED\&quot;,         \&quot;summary\&quot;: \&quot;This line might introduce a bug.\&quot;,         \&quot;severity\&quot;: \&quot;MEDIUM\&quot;,       \&quot;path\&quot;: \&quot;my-service/src/main/java/com/myCompany/mysystem/logic/Helper.java\&quot;,         \&quot;line\&quot;: 13   } ]&#39; &#x60;&#x60;&#x60;  ### Possible field values: annotation_type: VULNERABILITY, CODE_SMELL, BUG result: PASSED, FAILED, IGNORED, SKIPPED severity: HIGH, MEDIUM, LOW, CRITICAL  Please refer to the [Code Insights documentation](https://confluence.atlassian.com/bitbucket/code-insights-994316785.html) for more information. 

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.CommitsApi();
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
let repoSlug = "repoSlug_example"; // String | The repository.
let commit = "commit_example"; // String | The commit for which to retrieve reports.
let reportId = "reportId_example"; // String | Uuid or external-if of the report for which to get annotations for.
let reportAnnotation = [new BitbucketApi.ReportAnnotation()]; // [ReportAnnotation] | The annotations to create or update
apiInstance.bulkCreateOrUpdateAnnotations_0(workspace, repoSlug, commit, reportId, reportAnnotation, (error, data, response) => {
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
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example &#x60;{workspace UUID}&#x60;. | 
 **repoSlug** | **String**| The repository. | 
 **commit** | **String**| The commit for which to retrieve reports. | 
 **reportId** | **String**| Uuid or external-if of the report for which to get annotations for. | 
 **reportAnnotation** | [**[ReportAnnotation]**](ReportAnnotation.md)| The annotations to create or update | 

### Return type

[**[ReportAnnotation]**](ReportAnnotation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createOrUpdateAnnotation_0

> ReportAnnotation createOrUpdateAnnotation_0(workspace, repoSlug, commit, reportId, annotationId, reportAnnotation)

Create or update an annotation

Creates or updates an individual annotation for the specified report. Annotations are individual findings that have been identified as part of a report, for example, a line of code that represents a vulnerability. These annotations can be attached to a specific file and even a specific line in that file, however, that is optional. Annotations are not mandatory and a report can contain up to 1000 annotations.  Just as reports, annotation needs to be uploaded with a unique ID that can later be used to identify the report as an alternative to the generated [UUID](https://developer.atlassian.com/bitbucket/api/2/reference/meta/uri-uuid#uuid). If you want to use an existing id from your own system, we recommend prefixing it with your system&#39;s name to avoid collisions, for example, mySystem-annotation001.  ### Sample cURL request: &#x60;&#x60;&#x60; curl --request PUT &#39;https://api.bitbucket.org/2.0/repositories/&lt;username&gt;/&lt;reposity-name&gt;/commit/&lt;commit-hash&gt;/reports/mySystem-001/annotations/mysystem-annotation001&#39; \\ --header &#39;Content-Type: application/json&#39; \\ --data-raw &#39;{     \&quot;title\&quot;: \&quot;Security scan report\&quot;,     \&quot;annotation_type\&quot;: \&quot;VULNERABILITY\&quot;,     \&quot;summary\&quot;: \&quot;This line represents a security thread.\&quot;,     \&quot;severity\&quot;: \&quot;HIGH\&quot;,     \&quot;path\&quot;: \&quot;my-service/src/main/java/com/myCompany/mysystem/logic/Main.java\&quot;,     \&quot;line\&quot;: 42 }&#39; &#x60;&#x60;&#x60;  ### Possible field values: annotation_type: VULNERABILITY, CODE_SMELL, BUG result: PASSED, FAILED, IGNORED, SKIPPED severity: HIGH, MEDIUM, LOW, CRITICAL  Please refer to the [Code Insights documentation](https://confluence.atlassian.com/bitbucket/code-insights-994316785.html) for more information. 

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.CommitsApi();
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
let repoSlug = "repoSlug_example"; // String | The repository.
let commit = "commit_example"; // String | The commit the report belongs to.
let reportId = "reportId_example"; // String | Either the uuid or external-id of the report.
let annotationId = "annotationId_example"; // String | Either the uuid or external-id of the annotation.
let reportAnnotation = new BitbucketApi.ReportAnnotation(); // ReportAnnotation | The annotation to create or update
apiInstance.createOrUpdateAnnotation_0(workspace, repoSlug, commit, reportId, annotationId, reportAnnotation, (error, data, response) => {
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
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example &#x60;{workspace UUID}&#x60;. | 
 **repoSlug** | **String**| The repository. | 
 **commit** | **String**| The commit the report belongs to. | 
 **reportId** | **String**| Either the uuid or external-id of the report. | 
 **annotationId** | **String**| Either the uuid or external-id of the annotation. | 
 **reportAnnotation** | [**ReportAnnotation**](ReportAnnotation.md)| The annotation to create or update | 

### Return type

[**ReportAnnotation**](ReportAnnotation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createOrUpdateReport_0

> Report createOrUpdateReport_0(workspace, repoSlug, commit, reportId, report)

Create or update a report

Creates or updates a report for the specified commit. To upload a report, make sure to generate an ID that is unique across all reports for that commit. If you want to use an existing id from your own system, we recommend prefixing it with your system&#39;s name to avoid collisions, for example, mySystem-001.  ### Sample cURL request: &#x60;&#x60;&#x60; curl --request PUT &#39;https://api.bitbucket.org/2.0/repositories/&lt;username&gt;/&lt;reposity-name&gt;/commit/&lt;commit-hash&gt;/reports/mysystem-001&#39; \\ --header &#39;Content-Type: application/json&#39; \\ --data-raw &#39;{     \&quot;title\&quot;: \&quot;Security scan report\&quot;,     \&quot;details\&quot;: \&quot;This pull request introduces 10 new dependency vulnerabilities.\&quot;,     \&quot;report_type\&quot;: \&quot;SECURITY\&quot;,     \&quot;reporter\&quot;: \&quot;mySystem\&quot;,     \&quot;link\&quot;: \&quot;http://www.mysystem.com/reports/001\&quot;,     \&quot;result\&quot;: \&quot;FAILED\&quot;,     \&quot;data\&quot;: [         {             \&quot;title\&quot;: \&quot;Duration (seconds)\&quot;,             \&quot;type\&quot;: \&quot;DURATION\&quot;,             \&quot;value\&quot;: 14         },         {             \&quot;title\&quot;: \&quot;Safe to merge?\&quot;,             \&quot;type\&quot;: \&quot;BOOLEAN\&quot;,             \&quot;value\&quot;: false         }     ] }&#39; &#x60;&#x60;&#x60;  ### Possible field values: report_type: SECURITY, COVERAGE, TEST, BUG result: PASSED, FAILED, PENDING data.type: BOOLEAN, DATE, DURATION, LINK, NUMBER, PERCENTAGE, TEXT  #### Data field formats | Type  Field   | Value Field Type  | Value Field Display | |:--------------|:------------------|:--------------------| | None/ Omitted | Number, String or Boolean (not an array or object) | Plain text | | BOOLEAN | Boolean | The value will be read as a JSON boolean and displayed as &#39;Yes&#39; or &#39;No&#39;. | | DATE  | Number | The value will be read as a JSON number in the form of a Unix timestamp (milliseconds) and will be displayed as a relative date if the date is less than one week ago, otherwise  it will be displayed as an absolute date. | | DURATION | Number | The value will be read as a JSON number in milliseconds and will be displayed in a human readable duration format. | | LINK | Object: &#x60;{\&quot;text\&quot;: \&quot;Link text here\&quot;, \&quot;href\&quot;: \&quot;https://link.to.annotation/in/external/tool\&quot;}&#x60; | The value will be read as a JSON object containing the fields \&quot;text\&quot; and \&quot;href\&quot; and will be displayed as a clickable link on the report. | | NUMBER | Number | The value will be read as a JSON number and large numbers will be  displayed in a human readable format (e.g. 14.3k). | | PERCENTAGE | Number (between 0 and 100) | The value will be read as a JSON number between 0 and 100 and will be displayed with a percentage sign. | | TEXT | String | The value will be read as a JSON string and will be displayed as-is |  Please refer to the [Code Insights documentation](https://confluence.atlassian.com/bitbucket/code-insights-994316785.html) for more information. 

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.CommitsApi();
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
let repoSlug = "repoSlug_example"; // String | The repository.
let commit = "commit_example"; // String | The commit the report belongs to.
let reportId = "reportId_example"; // String | Either the uuid or external-id of the report.
let report = new BitbucketApi.Report(); // Report | The report to create or update
apiInstance.createOrUpdateReport_0(workspace, repoSlug, commit, reportId, report, (error, data, response) => {
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
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example &#x60;{workspace UUID}&#x60;. | 
 **repoSlug** | **String**| The repository. | 
 **commit** | **String**| The commit the report belongs to. | 
 **reportId** | **String**| Either the uuid or external-id of the report. | 
 **report** | [**Report**](Report.md)| The report to create or update | 

### Return type

[**Report**](Report.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteAnnotation_0

> deleteAnnotation_0(workspace, repoSlug, commit, reportId, annotationId)

Delete an annotation

Deletes a single Annotation matching the provided ID.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.CommitsApi();
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
let repoSlug = "repoSlug_example"; // String | The repository.
let commit = "commit_example"; // String | The commit the annotation belongs to.
let reportId = "reportId_example"; // String | Either the uuid or external-id of the annotation.
let annotationId = "annotationId_example"; // String | Either the uuid or external-id of the annotation.
apiInstance.deleteAnnotation_0(workspace, repoSlug, commit, reportId, annotationId, (error, data, response) => {
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
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example &#x60;{workspace UUID}&#x60;. | 
 **repoSlug** | **String**| The repository. | 
 **commit** | **String**| The commit the annotation belongs to. | 
 **reportId** | **String**| Either the uuid or external-id of the annotation. | 
 **annotationId** | **String**| Either the uuid or external-id of the annotation. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteReport_0

> deleteReport_0(workspace, repoSlug, commit, reportId)

Delete a report

Deletes a single Report matching the provided ID.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.CommitsApi();
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
let repoSlug = "repoSlug_example"; // String | The repository.
let commit = "commit_example"; // String | The commit the report belongs to.
let reportId = "reportId_example"; // String | Either the uuid or external-id of the report.
apiInstance.deleteReport_0(workspace, repoSlug, commit, reportId, (error, data, response) => {
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
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example &#x60;{workspace UUID}&#x60;. | 
 **repoSlug** | **String**| The repository. | 
 **commit** | **String**| The commit the report belongs to. | 
 **reportId** | **String**| Either the uuid or external-id of the report. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getAnnotation_0

> ReportAnnotation getAnnotation_0(workspace, repoSlug, commit, reportId, annotationId)

Get an annotation

Returns a single Annotation matching the provided ID.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.CommitsApi();
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
let repoSlug = "repoSlug_example"; // String | The repository.
let commit = "commit_example"; // String | The commit the report belongs to.
let reportId = "reportId_example"; // String | Either the uuid or external-id of the report.
let annotationId = "annotationId_example"; // String | Either the uuid or external-id of the annotation.
apiInstance.getAnnotation_0(workspace, repoSlug, commit, reportId, annotationId, (error, data, response) => {
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
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example &#x60;{workspace UUID}&#x60;. | 
 **repoSlug** | **String**| The repository. | 
 **commit** | **String**| The commit the report belongs to. | 
 **reportId** | **String**| Either the uuid or external-id of the report. | 
 **annotationId** | **String**| Either the uuid or external-id of the annotation. | 

### Return type

[**ReportAnnotation**](ReportAnnotation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAnnotationsForReport_0

> PaginatedAnnotations getAnnotationsForReport_0(workspace, repoSlug, commit, reportId)

List annotations

Returns a paginated list of Annotations for a specified report.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.CommitsApi();
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
let repoSlug = "repoSlug_example"; // String | The repository.
let commit = "commit_example"; // String | The commit for which to retrieve reports.
let reportId = "reportId_example"; // String | Uuid or external-if of the report for which to get annotations for.
apiInstance.getAnnotationsForReport_0(workspace, repoSlug, commit, reportId, (error, data, response) => {
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
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example &#x60;{workspace UUID}&#x60;. | 
 **repoSlug** | **String**| The repository. | 
 **commit** | **String**| The commit for which to retrieve reports. | 
 **reportId** | **String**| Uuid or external-if of the report for which to get annotations for. | 

### Return type

[**PaginatedAnnotations**](PaginatedAnnotations.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getReport_0

> Report getReport_0(workspace, repoSlug, commit, reportId)

Get a report

Returns a single Report matching the provided ID.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.CommitsApi();
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
let repoSlug = "repoSlug_example"; // String | The repository.
let commit = "commit_example"; // String | The commit the report belongs to.
let reportId = "reportId_example"; // String | Either the uuid or external-id of the report.
apiInstance.getReport_0(workspace, repoSlug, commit, reportId, (error, data, response) => {
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
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example &#x60;{workspace UUID}&#x60;. | 
 **repoSlug** | **String**| The repository. | 
 **commit** | **String**| The commit the report belongs to. | 
 **reportId** | **String**| Either the uuid or external-id of the report. | 

### Return type

[**Report**](Report.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getReportsForCommit_0

> PaginatedReports getReportsForCommit_0(workspace, repoSlug, commit)

List reports

Returns a paginated list of Reports linked to this commit.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.CommitsApi();
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
let repoSlug = "repoSlug_example"; // String | The repository.
let commit = "commit_example"; // String | The commit for which to retrieve reports.
apiInstance.getReportsForCommit_0(workspace, repoSlug, commit, (error, data, response) => {
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
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example &#x60;{workspace UUID}&#x60;. | 
 **repoSlug** | **String**| The repository. | 
 **commit** | **String**| The commit for which to retrieve reports. | 

### Return type

[**PaginatedReports**](PaginatedReports.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## repositoriesWorkspaceRepoSlugCommitCommitApproveDelete

> repositoriesWorkspaceRepoSlugCommitCommitApproveDelete(commit, repoSlug, workspace)

Unapprove a commit

Redact the authenticated user&#39;s approval of the specified commit.  This operation is only available to users that have explicit access to the repository. In contrast, just the fact that a repository is publicly accessible to users does not give them the ability to approve commits.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.CommitsApi();
let commit = "commit_example"; // String | The commit's SHA1.
let repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
apiInstance.repositoriesWorkspaceRepoSlugCommitCommitApproveDelete(commit, repoSlug, workspace, (error, data, response) => {
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
 **commit** | **String**| The commit&#39;s SHA1. | 
 **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## repositoriesWorkspaceRepoSlugCommitCommitApprovePost

> Participant repositoriesWorkspaceRepoSlugCommitCommitApprovePost(commit, repoSlug, workspace)

Approve a commit

Approve the specified commit as the authenticated user.  This operation is only available to users that have explicit access to the repository. In contrast, just the fact that a repository is publicly accessible to users does not give them the ability to approve commits.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.CommitsApi();
let commit = "commit_example"; // String | The commit's SHA1.
let repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
apiInstance.repositoriesWorkspaceRepoSlugCommitCommitApprovePost(commit, repoSlug, workspace, (error, data, response) => {
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
 **commit** | **String**| The commit&#39;s SHA1. | 
 **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | 

### Return type

[**Participant**](Participant.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## repositoriesWorkspaceRepoSlugCommitCommitCommentsCommentIdDelete

> repositoriesWorkspaceRepoSlugCommitCommitCommentsCommentIdDelete(commentId, commit, repoSlug, workspace)

Delete a commit comment

Deletes the specified commit comment.  Note that deleting comments that have visible replies that point to them will not really delete the resource. This is to retain the integrity of the original comment tree. Instead, the &#x60;deleted&#x60; element is set to &#x60;true&#x60; and the content is blanked out. The comment will continue to be returned by the collections and self endpoints.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.CommitsApi();
let commentId = 56; // Number | The id of the comment.
let commit = "commit_example"; // String | The commit's SHA1.
let repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
apiInstance.repositoriesWorkspaceRepoSlugCommitCommitCommentsCommentIdDelete(commentId, commit, repoSlug, workspace, (error, data, response) => {
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
 **commentId** | **Number**| The id of the comment. | 
 **commit** | **String**| The commit&#39;s SHA1. | 
 **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## repositoriesWorkspaceRepoSlugCommitCommitCommentsCommentIdGet

> CommitComment repositoriesWorkspaceRepoSlugCommitCommitCommentsCommentIdGet(commentId, commit, repoSlug, workspace)

Get a commit comment

Returns the specified commit comment.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.CommitsApi();
let commentId = 56; // Number | The id of the comment.
let commit = "commit_example"; // String | The commit's SHA1.
let repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
apiInstance.repositoriesWorkspaceRepoSlugCommitCommitCommentsCommentIdGet(commentId, commit, repoSlug, workspace, (error, data, response) => {
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
 **commentId** | **Number**| The id of the comment. | 
 **commit** | **String**| The commit&#39;s SHA1. | 
 **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | 

### Return type

[**CommitComment**](CommitComment.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## repositoriesWorkspaceRepoSlugCommitCommitCommentsCommentIdPut

> repositoriesWorkspaceRepoSlugCommitCommitCommentsCommentIdPut(commentId, commit, repoSlug, workspace, commitComment)

Update a commit comment

Used to update the contents of a comment. Only the content of the comment can be updated.  &#x60;&#x60;&#x60; $ curl https://api.bitbucket.org/2.0/repositories/atlassian/prlinks/commit/7f71b5/comments/5728901 \\   -X PUT -u evzijst \\   -H &#39;Content-Type: application/json&#39; \\   -d &#39;{\&quot;content\&quot;: {\&quot;raw\&quot;: \&quot;One more thing!\&quot;}&#39; &#x60;&#x60;&#x60;

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.CommitsApi();
let commentId = 56; // Number | The id of the comment.
let commit = "commit_example"; // String | The commit's SHA1.
let repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
let commitComment = new BitbucketApi.CommitComment(); // CommitComment | The updated comment.
apiInstance.repositoriesWorkspaceRepoSlugCommitCommitCommentsCommentIdPut(commentId, commit, repoSlug, workspace, commitComment, (error, data, response) => {
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
 **commentId** | **Number**| The id of the comment. | 
 **commit** | **String**| The commit&#39;s SHA1. | 
 **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | 
 **commitComment** | [**CommitComment**](CommitComment.md)| The updated comment. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## repositoriesWorkspaceRepoSlugCommitCommitCommentsGet

> PaginatedCommitComments repositoriesWorkspaceRepoSlugCommitCommitCommentsGet(commit, repoSlug, workspace, opts)

List a commit&#39;s comments

Returns the commit&#39;s comments.  This includes both global and inline comments.  The default sorting is oldest to newest and can be overridden with the &#x60;sort&#x60; query parameter.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.CommitsApi();
let commit = "commit_example"; // String | The commit's SHA1.
let repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
let opts = {
  'q': "q_example", // String | Query string to narrow down the response as per [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering). 
  'sort': "sort_example" // String | Field by which the results should be sorted as per [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering). 
};
apiInstance.repositoriesWorkspaceRepoSlugCommitCommitCommentsGet(commit, repoSlug, workspace, opts, (error, data, response) => {
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
 **commit** | **String**| The commit&#39;s SHA1. | 
 **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | 
 **q** | **String**| Query string to narrow down the response as per [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering).  | [optional] 
 **sort** | **String**| Field by which the results should be sorted as per [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering).  | [optional] 

### Return type

[**PaginatedCommitComments**](PaginatedCommitComments.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## repositoriesWorkspaceRepoSlugCommitCommitCommentsPost

> repositoriesWorkspaceRepoSlugCommitCommitCommentsPost(commit, repoSlug, workspace, commitComment)

Create comment for a commit

Creates new comment on the specified commit.  To post a reply to an existing comment, include the &#x60;parent.id&#x60; field:  &#x60;&#x60;&#x60; $ curl https://api.bitbucket.org/2.0/repositories/atlassian/prlinks/commit/db9ba1e031d07a02603eae0e559a7adc010257fc/comments/ \\   -X POST -u evzijst \\   -H &#39;Content-Type: application/json&#39; \\   -d &#39;{\&quot;content\&quot;: {\&quot;raw\&quot;: \&quot;One more thing!\&quot;},        \&quot;parent\&quot;: {\&quot;id\&quot;: 5728901}}&#39; &#x60;&#x60;&#x60;

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.CommitsApi();
let commit = "commit_example"; // String | The commit's SHA1.
let repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
let commitComment = new BitbucketApi.CommitComment(); // CommitComment | The specified comment.
apiInstance.repositoriesWorkspaceRepoSlugCommitCommitCommentsPost(commit, repoSlug, workspace, commitComment, (error, data, response) => {
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
 **commit** | **String**| The commit&#39;s SHA1. | 
 **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | 
 **commitComment** | [**CommitComment**](CommitComment.md)| The specified comment. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## repositoriesWorkspaceRepoSlugCommitCommitGet

> Commit repositoriesWorkspaceRepoSlugCommitCommitGet(commit, repoSlug, workspace)

Get a commit

Returns the specified commit.  Example:  &#x60;&#x60;&#x60; $ curl https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/commit/f7591a1 {     \&quot;rendered\&quot;: {         \&quot;message\&quot;: {         \&quot;raw\&quot;: \&quot;Add a GEORDI_OUTPUT_DIR setting\&quot;,         \&quot;markup\&quot;: \&quot;markdown\&quot;,         \&quot;html\&quot;: \&quot;&lt;p&gt;Add a GEORDI_OUTPUT_DIR setting&lt;/p&gt;\&quot;,         \&quot;type\&quot;: \&quot;rendered\&quot;         }     },     \&quot;hash\&quot;: \&quot;f7591a13eda445d9a9167f98eb870319f4b6c2d8\&quot;,     \&quot;repository\&quot;: {         \&quot;name\&quot;: \&quot;geordi\&quot;,         \&quot;type\&quot;: \&quot;repository\&quot;,         \&quot;full_name\&quot;: \&quot;bitbucket/geordi\&quot;,         \&quot;links\&quot;: {             \&quot;self\&quot;: {                 \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/bitbucket/geordi\&quot;             },             \&quot;html\&quot;: {                 \&quot;href\&quot;: \&quot;https://bitbucket.org/bitbucket/geordi\&quot;             },             \&quot;avatar\&quot;: {                 \&quot;href\&quot;: \&quot;https://bytebucket.org/ravatar/%7B85d08b4e-571d-44e9-a507-fa476535aa98%7D?ts&#x3D;1730260\&quot;             }         },         \&quot;uuid\&quot;: \&quot;{85d08b4e-571d-44e9-a507-fa476535aa98}\&quot;     },     \&quot;links\&quot;: {         \&quot;self\&quot;: {             \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/commit/f7591a13eda445d9a9167f98eb870319f4b6c2d8\&quot;         },         \&quot;comments\&quot;: {             \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/commit/f7591a13eda445d9a9167f98eb870319f4b6c2d8/comments\&quot;         },         \&quot;patch\&quot;: {             \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/patch/f7591a13eda445d9a9167f98eb870319f4b6c2d8\&quot;         },         \&quot;html\&quot;: {             \&quot;href\&quot;: \&quot;https://bitbucket.org/bitbucket/geordi/commits/f7591a13eda445d9a9167f98eb870319f4b6c2d8\&quot;         },         \&quot;diff\&quot;: {             \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/diff/f7591a13eda445d9a9167f98eb870319f4b6c2d8\&quot;         },         \&quot;approve\&quot;: {             \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/commit/f7591a13eda445d9a9167f98eb870319f4b6c2d8/approve\&quot;         },         \&quot;statuses\&quot;: {             \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/commit/f7591a13eda445d9a9167f98eb870319f4b6c2d8/statuses\&quot;         }     },     \&quot;author\&quot;: {         \&quot;raw\&quot;: \&quot;Brodie Rao &lt;a@b.c&gt;\&quot;,         \&quot;type\&quot;: \&quot;author\&quot;,         \&quot;user\&quot;: {             \&quot;display_name\&quot;: \&quot;Brodie Rao\&quot;,             \&quot;uuid\&quot;: \&quot;{9484702e-c663-4afd-aefb-c93a8cd31c28}\&quot;,             \&quot;links\&quot;: {                 \&quot;self\&quot;: {                     \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/users/%7B9484702e-c663-4afd-aefb-c93a8cd31c28%7D\&quot;                 },                 \&quot;html\&quot;: {                     \&quot;href\&quot;: \&quot;https://bitbucket.org/%7B9484702e-c663-4afd-aefb-c93a8cd31c28%7D/\&quot;                 },                 \&quot;avatar\&quot;: {                     \&quot;href\&quot;: \&quot;https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/557058:3aae1e05-702a-41e5-81c8-f36f29afb6ca/613070db-28b0-421f-8dba-ae8a87e2a5c7/128\&quot;                 }             },             \&quot;type\&quot;: \&quot;user\&quot;,             \&quot;nickname\&quot;: \&quot;brodie\&quot;,             \&quot;account_id\&quot;: \&quot;557058:3aae1e05-702a-41e5-81c8-f36f29afb6ca\&quot;         }     },     \&quot;summary\&quot;: {         \&quot;raw\&quot;: \&quot;Add a GEORDI_OUTPUT_DIR setting\&quot;,         \&quot;markup\&quot;: \&quot;markdown\&quot;,         \&quot;html\&quot;: \&quot;&lt;p&gt;Add a GEORDI_OUTPUT_DIR setting&lt;/p&gt;\&quot;,         \&quot;type\&quot;: \&quot;rendered\&quot;     },     \&quot;participants\&quot;: [],     \&quot;parents\&quot;: [         {             \&quot;type\&quot;: \&quot;commit\&quot;,             \&quot;hash\&quot;: \&quot;f06941fec4ef6bcb0c2456927a0cf258fa4f899b\&quot;,             \&quot;links\&quot;: {                 \&quot;self\&quot;: {                     \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/commit/f06941fec4ef6bcb0c2456927a0cf258fa4f899b\&quot;                 },                 \&quot;html\&quot;: {                     \&quot;href\&quot;: \&quot;https://bitbucket.org/bitbucket/geordi/commits/f06941fec4ef6bcb0c2456927a0cf258fa4f899b\&quot;                 }             }         }     ],     \&quot;date\&quot;: \&quot;2012-07-16T19:37:54+00:00\&quot;,     \&quot;message\&quot;: \&quot;Add a GEORDI_OUTPUT_DIR setting\&quot;,     \&quot;type\&quot;: \&quot;commit\&quot; } &#x60;&#x60;&#x60;

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.CommitsApi();
let commit = "commit_example"; // String | The commit's SHA1.
let repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
apiInstance.repositoriesWorkspaceRepoSlugCommitCommitGet(commit, repoSlug, workspace, (error, data, response) => {
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
 **commit** | **String**| The commit&#39;s SHA1. | 
 **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | 

### Return type

[**Commit**](Commit.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## repositoriesWorkspaceRepoSlugCommitsGet

> PaginatedChangeset repositoriesWorkspaceRepoSlugCommitsGet(repoSlug, workspace)

List commits

These are the repository&#39;s commits. They are paginated and returned in reverse chronological order, similar to the output of &#x60;git log&#x60;. Like these tools, the DAG can be filtered.  #### GET /repositories/{workspace}/{repo_slug}/commits/  Returns all commits in the repo in topological order (newest commit first). All branches and tags are included (similar to &#x60;git log --all&#x60;).  #### GET /repositories/{workspace}/{repo_slug}/commits/?exclude&#x3D;master  Returns all commits in the repo that are not on master (similar to &#x60;git log --all ^master&#x60;).  #### GET /repositories/{workspace}/{repo_slug}/commits/?include&#x3D;foo&amp;include&#x3D;bar&amp;exclude&#x3D;fu&amp;exclude&#x3D;fubar  Returns all commits that are on refs &#x60;foo&#x60; or &#x60;bar&#x60;, but not on &#x60;fu&#x60; or &#x60;fubar&#x60; (similar to &#x60;git log foo bar ^fu ^fubar&#x60;).  An optional &#x60;path&#x60; parameter can be specified that will limit the results to commits that affect that path. &#x60;path&#x60; can either be a file or a directory. If a directory is specified, commits are returned that have modified any file in the directory tree rooted by &#x60;path&#x60;. It is important to note that if the &#x60;path&#x60; parameter is specified, the commits returned by this endpoint may no longer be a DAG, parent commits that do not modify the path will be omitted from the response.  #### GET /repositories/{workspace}/{repo_slug}/commits/?path&#x3D;README.md&amp;include&#x3D;foo&amp;include&#x3D;bar&amp;exclude&#x3D;master  Returns all commits that are on refs &#x60;foo&#x60; or &#x60;bar&#x60;, but not on &#x60;master&#x60; that changed the file README.md.  #### GET /repositories/{workspace}/{repo_slug}/commits/?path&#x3D;src/&amp;include&#x3D;foo&amp;include&#x3D;bar&amp;exclude&#x3D;master  Returns all commits that are on refs &#x60;foo&#x60; or &#x60;bar&#x60;, but not on &#x60;master&#x60; that changed to a file in any file in the directory src or its children.  Because the response could include a very large number of commits, it is paginated. Follow the &#39;next&#39; link in the response to navigate to the next page of commits. As with other paginated resources, do not construct your own links.  When the include and exclude parameters are more than can fit in a query string, clients can use a &#x60;x-www-form-urlencoded&#x60; POST instead.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.CommitsApi();
let repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
apiInstance.repositoriesWorkspaceRepoSlugCommitsGet(repoSlug, workspace, (error, data, response) => {
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
 **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | 

### Return type

[**PaginatedChangeset**](PaginatedChangeset.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## repositoriesWorkspaceRepoSlugCommitsPost

> PaginatedChangeset repositoriesWorkspaceRepoSlugCommitsPost(repoSlug, workspace)

List commits with include/exclude

Identical to &#x60;GET /repositories/{workspace}/{repo_slug}/commits&#x60;, except that POST allows clients to place the include and exclude parameters in the request body to avoid URL length issues.  **Note that this resource does NOT support new commit creation.**

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.CommitsApi();
let repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
apiInstance.repositoriesWorkspaceRepoSlugCommitsPost(repoSlug, workspace, (error, data, response) => {
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
 **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | 

### Return type

[**PaginatedChangeset**](PaginatedChangeset.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## repositoriesWorkspaceRepoSlugCommitsRevisionGet

> PaginatedChangeset repositoriesWorkspaceRepoSlugCommitsRevisionGet(repoSlug, revision, workspace)

List commits for revision

These are the repository&#39;s commits. They are paginated and returned in reverse chronological order, similar to the output of &#x60;git log&#x60;. Like these tools, the DAG can be filtered.  #### GET /repositories/{workspace}/{repo_slug}/commits/master  Returns all commits on ref &#x60;master&#x60; (similar to &#x60;git log master&#x60;).  #### GET /repositories/{workspace}/{repo_slug}/commits/dev?include&#x3D;foo&amp;exclude&#x3D;master  Returns all commits on ref &#x60;dev&#x60; or &#x60;foo&#x60;, except those that are reachable on &#x60;master&#x60; (similar to &#x60;git log dev foo ^master&#x60;).  An optional &#x60;path&#x60; parameter can be specified that will limit the results to commits that affect that path. &#x60;path&#x60; can either be a file or a directory. If a directory is specified, commits are returned that have modified any file in the directory tree rooted by &#x60;path&#x60;. It is important to note that if the &#x60;path&#x60; parameter is specified, the commits returned by this endpoint may no longer be a DAG, parent commits that do not modify the path will be omitted from the response.  #### GET /repositories/{workspace}/{repo_slug}/commits/dev?path&#x3D;README.md&amp;include&#x3D;foo&amp;include&#x3D;bar&amp;exclude&#x3D;master  Returns all commits that are on refs &#x60;dev&#x60; or &#x60;foo&#x60; or &#x60;bar&#x60;, but not on &#x60;master&#x60; that changed the file README.md.  #### GET /repositories/{workspace}/{repo_slug}/commits/dev?path&#x3D;src/&amp;include&#x3D;foo&amp;exclude&#x3D;master  Returns all commits that are on refs &#x60;dev&#x60; or &#x60;foo&#x60;, but not on &#x60;master&#x60; that changed to a file in any file in the directory src or its children.  Because the response could include a very large number of commits, it is paginated. Follow the &#39;next&#39; link in the response to navigate to the next page of commits. As with other paginated resources, do not construct your own links.  When the include and exclude parameters are more than can fit in a query string, clients can use a &#x60;x-www-form-urlencoded&#x60; POST instead.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.CommitsApi();
let repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
let revision = "revision_example"; // String | A commit SHA1 or ref name.
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
apiInstance.repositoriesWorkspaceRepoSlugCommitsRevisionGet(repoSlug, revision, workspace, (error, data, response) => {
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
 **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **revision** | **String**| A commit SHA1 or ref name. | 
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | 

### Return type

[**PaginatedChangeset**](PaginatedChangeset.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## repositoriesWorkspaceRepoSlugCommitsRevisionPost

> PaginatedChangeset repositoriesWorkspaceRepoSlugCommitsRevisionPost(repoSlug, revision, workspace)

List commits for revision using include/exclude

Identical to &#x60;GET /repositories/{workspace}/{repo_slug}/commits/{revision}&#x60;, except that POST allows clients to place the include and exclude parameters in the request body to avoid URL length issues.  **Note that this resource does NOT support new commit creation.**

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.CommitsApi();
let repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
let revision = "revision_example"; // String | A commit SHA1 or ref name.
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
apiInstance.repositoriesWorkspaceRepoSlugCommitsRevisionPost(repoSlug, revision, workspace, (error, data, response) => {
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
 **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **revision** | **String**| A commit SHA1 or ref name. | 
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | 

### Return type

[**PaginatedChangeset**](PaginatedChangeset.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## repositoriesWorkspaceRepoSlugDiffSpecGet

> repositoriesWorkspaceRepoSlugDiffSpecGet(repoSlug, spec, workspace, opts)

Compare two commits

Produces a raw git-style diff.  #### Single commit spec  If the &#x60;spec&#x60; argument to this API is a single commit, the diff is produced against the first parent of the specified commit.  #### Two commit spec  Two commits separated by &#x60;..&#x60; may be provided as the &#x60;spec&#x60;, e.g., &#x60;3a8b42..9ff173&#x60;. When two commits are provided and the &#x60;topic&#x60; query parameter is true or absent, this API produces a 2-way three dot diff. This is the diff between source commit and the merge base of the source commit and the destination commit. When the &#x60;topic&#x60; query param is false, a simple git-style diff is produced.  The two commits are interpreted as follows:  * First commit: the commit containing the changes we wish to preview * Second commit: the commit representing the state to which we want to   compare the first commit * **Note**: This is the opposite of the order used in &#x60;git diff&#x60;.  #### Comparison to patches  While similar to patches, diffs:  * Don&#39;t have a commit header (username, commit message, etc) * Support the optional &#x60;path&#x3D;foo/bar.py&#x60; query param to filter   the diff to just that one file diff  #### Response  The raw diff is returned as-is, in whatever encoding the files in the repository use. It is not decoded into unicode. As such, the content-type is &#x60;text/plain&#x60;.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.CommitsApi();
let repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
let spec = "spec_example"; // String | A commit SHA (e.g. `3a8b42`) or a commit range using double dot notation (e.g. `3a8b42..9ff173`). 
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
let opts = {
  'context': 56, // Number | Generate diffs with <n> lines of context instead of the usual three.
  'path': "path_example", // String | Limit the diff to a particular file (this parameter can be repeated for multiple paths).
  'ignoreWhitespace': true, // Boolean | Generate diffs that ignore whitespace.
  'binary': true, // Boolean | Generate diffs that include binary files, true if omitted.
  'renames': true, // Boolean | Whether to perform rename detection, true if omitted.
  'merge': true, // Boolean | This parameter is deprecated and will be removed at the end of 2022. The 'topic' parameter should be used instead. The 'merge' and 'topic' parameters cannot be both used at the same time.  If true, the source commit is merged into the destination commit, and then a diff from the destination to the merge result is returned. If false, a simple 'two dot' diff between the source and destination is returned. True if omitted.
  'topic': true // Boolean | If true, returns 2-way 'three-dot' diff. This is a diff between the source commit and the merge base of the source commit and the destination commit. If false, a simple 'two dot' diff between the source and destination is returned.
};
apiInstance.repositoriesWorkspaceRepoSlugDiffSpecGet(repoSlug, spec, workspace, opts, (error, data, response) => {
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
 **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **spec** | **String**| A commit SHA (e.g. &#x60;3a8b42&#x60;) or a commit range using double dot notation (e.g. &#x60;3a8b42..9ff173&#x60;).  | 
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | 
 **context** | **Number**| Generate diffs with &lt;n&gt; lines of context instead of the usual three. | [optional] 
 **path** | **String**| Limit the diff to a particular file (this parameter can be repeated for multiple paths). | [optional] 
 **ignoreWhitespace** | **Boolean**| Generate diffs that ignore whitespace. | [optional] 
 **binary** | **Boolean**| Generate diffs that include binary files, true if omitted. | [optional] 
 **renames** | **Boolean**| Whether to perform rename detection, true if omitted. | [optional] 
 **merge** | **Boolean**| This parameter is deprecated and will be removed at the end of 2022. The &#39;topic&#39; parameter should be used instead. The &#39;merge&#39; and &#39;topic&#39; parameters cannot be both used at the same time.  If true, the source commit is merged into the destination commit, and then a diff from the destination to the merge result is returned. If false, a simple &#39;two dot&#39; diff between the source and destination is returned. True if omitted. | [optional] 
 **topic** | **Boolean**| If true, returns 2-way &#39;three-dot&#39; diff. This is a diff between the source commit and the merge base of the source commit and the destination commit. If false, a simple &#39;two dot&#39; diff between the source and destination is returned. | [optional] 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## repositoriesWorkspaceRepoSlugDiffstatSpecGet

> PaginatedDiffstats repositoriesWorkspaceRepoSlugDiffstatSpecGet(repoSlug, spec, workspace, opts)

Compare two commit diff stats

Produces a response in JSON format with a record for every path modified, including information on the type of the change and the number of lines added and removed.  #### Single commit spec  If the &#x60;spec&#x60; argument to this API is a single commit, the diff is produced against the first parent of the specified commit.  #### Two commit spec  Two commits separated by &#x60;..&#x60; may be provided as the &#x60;spec&#x60;, e.g., &#x60;3a8b42..9ff173&#x60;. When two commits are provided and the &#x60;topic&#x60; query parameter is true or absent, this API produces a 2-way three dot diff. This is the diff between source commit and the merge base of the source commit and the destination commit. When the &#x60;topic&#x60; query param is false, a simple git-style diff is produced.  The two commits are interpreted as follows:  * First commit: the commit containing the changes we wish to preview * Second commit: the commit representing the state to which we want to   compare the first commit * **Note**: This is the opposite of the order used in &#x60;git diff&#x60;.  #### Sample output &#x60;&#x60;&#x60; curl https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/diffstat/d222fa2..e174964 {     \&quot;pagelen\&quot;: 500,     \&quot;values\&quot;: [         {             \&quot;type\&quot;: \&quot;diffstat\&quot;,             \&quot;status\&quot;: \&quot;modified\&quot;,             \&quot;lines_removed\&quot;: 1,             \&quot;lines_added\&quot;: 2,             \&quot;old\&quot;: {                 \&quot;path\&quot;: \&quot;setup.py\&quot;,                 \&quot;escaped_path\&quot;: \&quot;setup.py\&quot;,                 \&quot;type\&quot;: \&quot;commit_file\&quot;,                 \&quot;links\&quot;: {                     \&quot;self\&quot;: {                         \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/src/e1749643d655d7c7014001a6c0f58abaf42ad850/setup.py\&quot;                     }                 }             },             \&quot;new\&quot;: {                 \&quot;path\&quot;: \&quot;setup.py\&quot;,                 \&quot;escaped_path\&quot;: \&quot;setup.py\&quot;,                 \&quot;type\&quot;: \&quot;commit_file\&quot;,                 \&quot;links\&quot;: {                     \&quot;self\&quot;: {                         \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/src/d222fa235229c55dad20b190b0b571adf737d5a6/setup.py\&quot;                     }                 }             }         }     ],     \&quot;page\&quot;: 1,     \&quot;size\&quot;: 1 } &#x60;&#x60;&#x60;

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.CommitsApi();
let repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
let spec = "spec_example"; // String | A commit SHA (e.g. `3a8b42`) or a commit range using double dot notation (e.g. `3a8b42..9ff173`). 
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
let opts = {
  'ignoreWhitespace': true, // Boolean | Generate diffs that ignore whitespace
  'merge': true, // Boolean | This parameter is deprecated and will be removed at the end of 2022. The 'topic' parameter should be used instead. The 'merge' and 'topic' parameters cannot be both used at the same time.  If true, the source commit is merged into the destination commit, and then a diffstat from the destination to the merge result is returned. If false, a simple 'two dot' diffstat between the source and destination is returned. True if omitted.
  'path': "path_example", // String | Limit the diffstat to a particular file (this parameter can be repeated for multiple paths).
  'renames': true, // Boolean | Whether to perform rename detection, true if omitted.
  'topic': true // Boolean | If true, returns 2-way 'three-dot' diff. This is a diff between the source commit and the merge base of the source commit and the destination commit. If false, a simple 'two dot' diff between the source and destination is returned.
};
apiInstance.repositoriesWorkspaceRepoSlugDiffstatSpecGet(repoSlug, spec, workspace, opts, (error, data, response) => {
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
 **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **spec** | **String**| A commit SHA (e.g. &#x60;3a8b42&#x60;) or a commit range using double dot notation (e.g. &#x60;3a8b42..9ff173&#x60;).  | 
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | 
 **ignoreWhitespace** | **Boolean**| Generate diffs that ignore whitespace | [optional] 
 **merge** | **Boolean**| This parameter is deprecated and will be removed at the end of 2022. The &#39;topic&#39; parameter should be used instead. The &#39;merge&#39; and &#39;topic&#39; parameters cannot be both used at the same time.  If true, the source commit is merged into the destination commit, and then a diffstat from the destination to the merge result is returned. If false, a simple &#39;two dot&#39; diffstat between the source and destination is returned. True if omitted. | [optional] 
 **path** | **String**| Limit the diffstat to a particular file (this parameter can be repeated for multiple paths). | [optional] 
 **renames** | **Boolean**| Whether to perform rename detection, true if omitted. | [optional] 
 **topic** | **Boolean**| If true, returns 2-way &#39;three-dot&#39; diff. This is a diff between the source commit and the merge base of the source commit and the destination commit. If false, a simple &#39;two dot&#39; diff between the source and destination is returned. | [optional] 

### Return type

[**PaginatedDiffstats**](PaginatedDiffstats.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## repositoriesWorkspaceRepoSlugMergeBaseRevspecGet

> Commit repositoriesWorkspaceRepoSlugMergeBaseRevspecGet(repoSlug, revspec, workspace)

Get the common ancestor between two commits

Returns the best common ancestor between two commits, specified in a revspec of 2 commits (e.g. 3a8b42..9ff173).  If more than one best common ancestor exists, only one will be returned. It is unspecified which will be returned.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.CommitsApi();
let repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
let revspec = "revspec_example"; // String | A commit range using double dot notation (e.g. `3a8b42..9ff173`). 
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
apiInstance.repositoriesWorkspaceRepoSlugMergeBaseRevspecGet(repoSlug, revspec, workspace, (error, data, response) => {
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
 **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **revspec** | **String**| A commit range using double dot notation (e.g. &#x60;3a8b42..9ff173&#x60;).  | 
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | 

### Return type

[**Commit**](Commit.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## repositoriesWorkspaceRepoSlugPatchSpecGet

> repositoriesWorkspaceRepoSlugPatchSpecGet(repoSlug, spec, workspace)

Get a patch for two commits

Produces a raw patch for a single commit (diffed against its first parent), or a patch-series for a revspec of 2 commits (e.g. &#x60;3a8b42..9ff173&#x60; where the first commit represents the source and the second commit the destination).  In case of the latter (diffing a revspec), a patch series is returned for the commits on the source branch (&#x60;3a8b42&#x60; and its ancestors in our example).  While similar to diffs, patches:  * Have a commit header (username, commit message, etc) * Do not support the &#x60;path&#x3D;foo/bar.py&#x60; query parameter  The raw patch is returned as-is, in whatever encoding the files in the repository use. It is not decoded into unicode. As such, the content-type is &#x60;text/plain&#x60;.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.CommitsApi();
let repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
let spec = "spec_example"; // String | A commit SHA (e.g. `3a8b42`) or a commit range using double dot notation (e.g. `3a8b42..9ff173`). 
let workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
apiInstance.repositoriesWorkspaceRepoSlugPatchSpecGet(repoSlug, spec, workspace, (error, data, response) => {
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
 **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | 
 **spec** | **String**| A commit SHA (e.g. &#x60;3a8b42&#x60;) or a commit range using double dot notation (e.g. &#x60;3a8b42..9ff173&#x60;).  | 
 **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

