# ReportsApi

All URIs are relative to *https://api.bitbucket.org/2.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**bulkCreateOrUpdateAnnotations**](ReportsApi.md#bulkCreateOrUpdateAnnotations) | **POST** /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}/annotations | Bulk create or update annotations |
| [**createOrUpdateAnnotation**](ReportsApi.md#createOrUpdateAnnotation) | **PUT** /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}/annotations/{annotationId} | Create or update an annotation |
| [**createOrUpdateReport**](ReportsApi.md#createOrUpdateReport) | **PUT** /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId} | Create or update a report |
| [**deleteAnnotation**](ReportsApi.md#deleteAnnotation) | **DELETE** /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}/annotations/{annotationId} | Delete an annotation |
| [**deleteReport**](ReportsApi.md#deleteReport) | **DELETE** /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId} | Delete a report |
| [**getAnnotation**](ReportsApi.md#getAnnotation) | **GET** /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}/annotations/{annotationId} | Get an annotation |
| [**getAnnotationsForReport**](ReportsApi.md#getAnnotationsForReport) | **GET** /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}/annotations | List annotations |
| [**getReport**](ReportsApi.md#getReport) | **GET** /repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId} | Get a report |
| [**getReportsForCommit**](ReportsApi.md#getReportsForCommit) | **GET** /repositories/{workspace}/{repo_slug}/commit/{commit}/reports | List reports |


<a id="bulkCreateOrUpdateAnnotations"></a>
# **bulkCreateOrUpdateAnnotations**
> List&lt;ReportAnnotation&gt; bulkCreateOrUpdateAnnotations(workspace, repoSlug, commit, reportId, reportAnnotation)

Bulk create or update annotations

Bulk upload of annotations. Annotations are individual findings that have been identified as part of a report, for example, a line of code that represents a vulnerability. These annotations can be attached to a specific file and even a specific line in that file, however, that is optional. Annotations are not mandatory and a report can contain up to 1000 annotations.  Add the annotations you want to upload as objects in a JSON array and make sure each annotation has the external_id field set to a unique value. If you want to use an existing id from your own system, we recommend prefixing it with your system&#39;s name to avoid collisions, for example, mySystem-annotation001. The external id can later be used to identify the report as an alternative to the generated [UUID](https://developer.atlassian.com/bitbucket/api/2/reference/meta/uri-uuid#uuid). You can upload up to 100 annotations per POST request.  ### Sample cURL request: &#x60;&#x60;&#x60; curl --location &#39;https://api.bitbucket.org/2.0/repositories/&lt;username&gt;/&lt;reposity-name&gt;/commit/&lt;commit-hash&gt;/reports/mysystem-001/annotations&#39; \\ --header &#39;Content-Type: application/json&#39; \\ --data-raw &#39;[   {         \&quot;external_id\&quot;: \&quot;mysystem-annotation001\&quot;,         \&quot;title\&quot;: \&quot;Security scan report\&quot;,         \&quot;annotation_type\&quot;: \&quot;VULNERABILITY\&quot;,         \&quot;summary\&quot;: \&quot;This line represents a security threat.\&quot;,         \&quot;severity\&quot;: \&quot;HIGH\&quot;,       \&quot;path\&quot;: \&quot;my-service/src/main/java/com/myCompany/mysystem/logic/Main.java\&quot;,         \&quot;line\&quot;: 42   },   {         \&quot;external_id\&quot;: \&quot;mySystem-annotation002\&quot;,         \&quot;title\&quot;: \&quot;Bug report\&quot;,         \&quot;annotation_type\&quot;: \&quot;BUG\&quot;,         \&quot;result\&quot;: \&quot;FAILED\&quot;,         \&quot;summary\&quot;: \&quot;This line might introduce a bug.\&quot;,         \&quot;severity\&quot;: \&quot;MEDIUM\&quot;,       \&quot;path\&quot;: \&quot;my-service/src/main/java/com/myCompany/mysystem/logic/Helper.java\&quot;,         \&quot;line\&quot;: 13   } ]&#39; &#x60;&#x60;&#x60;  ### Possible field values: annotation_type: VULNERABILITY, CODE_SMELL, BUG result: PASSED, FAILED, IGNORED, SKIPPED severity: HIGH, MEDIUM, LOW, CRITICAL  Please refer to the [Code Insights documentation](https://confluence.atlassian.com/bitbucket/code-insights-994316785.html) for more information. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
    String repoSlug = "repoSlug_example"; // String | The repository.
    String commit = "commit_example"; // String | The commit for which to retrieve reports.
    String reportId = "reportId_example"; // String | Uuid or external-if of the report for which to get annotations for.
    List<ReportAnnotation> reportAnnotation = Arrays.asList(); // List<ReportAnnotation> | The annotations to create or update
    try {
      List<ReportAnnotation> result = apiInstance.bulkCreateOrUpdateAnnotations(workspace, repoSlug, commit, reportId, reportAnnotation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#bulkCreateOrUpdateAnnotations");
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
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example &#x60;{workspace UUID}&#x60;. | |
| **repoSlug** | **String**| The repository. | |
| **commit** | **String**| The commit for which to retrieve reports. | |
| **reportId** | **String**| Uuid or external-if of the report for which to get annotations for. | |
| **reportAnnotation** | [**List&lt;ReportAnnotation&gt;**](ReportAnnotation.md)| The annotations to create or update | |

### Return type

[**List&lt;ReportAnnotation&gt;**](ReportAnnotation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="createOrUpdateAnnotation"></a>
# **createOrUpdateAnnotation**
> ReportAnnotation createOrUpdateAnnotation(workspace, repoSlug, commit, reportId, annotationId, reportAnnotation)

Create or update an annotation

Creates or updates an individual annotation for the specified report. Annotations are individual findings that have been identified as part of a report, for example, a line of code that represents a vulnerability. These annotations can be attached to a specific file and even a specific line in that file, however, that is optional. Annotations are not mandatory and a report can contain up to 1000 annotations.  Just as reports, annotation needs to be uploaded with a unique ID that can later be used to identify the report as an alternative to the generated [UUID](https://developer.atlassian.com/bitbucket/api/2/reference/meta/uri-uuid#uuid). If you want to use an existing id from your own system, we recommend prefixing it with your system&#39;s name to avoid collisions, for example, mySystem-annotation001.  ### Sample cURL request: &#x60;&#x60;&#x60; curl --request PUT &#39;https://api.bitbucket.org/2.0/repositories/&lt;username&gt;/&lt;reposity-name&gt;/commit/&lt;commit-hash&gt;/reports/mySystem-001/annotations/mysystem-annotation001&#39; \\ --header &#39;Content-Type: application/json&#39; \\ --data-raw &#39;{     \&quot;title\&quot;: \&quot;Security scan report\&quot;,     \&quot;annotation_type\&quot;: \&quot;VULNERABILITY\&quot;,     \&quot;summary\&quot;: \&quot;This line represents a security thread.\&quot;,     \&quot;severity\&quot;: \&quot;HIGH\&quot;,     \&quot;path\&quot;: \&quot;my-service/src/main/java/com/myCompany/mysystem/logic/Main.java\&quot;,     \&quot;line\&quot;: 42 }&#39; &#x60;&#x60;&#x60;  ### Possible field values: annotation_type: VULNERABILITY, CODE_SMELL, BUG result: PASSED, FAILED, IGNORED, SKIPPED severity: HIGH, MEDIUM, LOW, CRITICAL  Please refer to the [Code Insights documentation](https://confluence.atlassian.com/bitbucket/code-insights-994316785.html) for more information. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
    String repoSlug = "repoSlug_example"; // String | The repository.
    String commit = "commit_example"; // String | The commit the report belongs to.
    String reportId = "reportId_example"; // String | Either the uuid or external-id of the report.
    String annotationId = "annotationId_example"; // String | Either the uuid or external-id of the annotation.
    ReportAnnotation reportAnnotation = new ReportAnnotation(); // ReportAnnotation | The annotation to create or update
    try {
      ReportAnnotation result = apiInstance.createOrUpdateAnnotation(workspace, repoSlug, commit, reportId, annotationId, reportAnnotation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#createOrUpdateAnnotation");
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
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example &#x60;{workspace UUID}&#x60;. | |
| **repoSlug** | **String**| The repository. | |
| **commit** | **String**| The commit the report belongs to. | |
| **reportId** | **String**| Either the uuid or external-id of the report. | |
| **annotationId** | **String**| Either the uuid or external-id of the annotation. | |
| **reportAnnotation** | [**ReportAnnotation**](ReportAnnotation.md)| The annotation to create or update | |

### Return type

[**ReportAnnotation**](ReportAnnotation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | The provided Annotation object is malformed or incomplete. |  -  |

<a id="createOrUpdateReport"></a>
# **createOrUpdateReport**
> Report createOrUpdateReport(workspace, repoSlug, commit, reportId, report)

Create or update a report

Creates or updates a report for the specified commit. To upload a report, make sure to generate an ID that is unique across all reports for that commit. If you want to use an existing id from your own system, we recommend prefixing it with your system&#39;s name to avoid collisions, for example, mySystem-001.  ### Sample cURL request: &#x60;&#x60;&#x60; curl --request PUT &#39;https://api.bitbucket.org/2.0/repositories/&lt;username&gt;/&lt;reposity-name&gt;/commit/&lt;commit-hash&gt;/reports/mysystem-001&#39; \\ --header &#39;Content-Type: application/json&#39; \\ --data-raw &#39;{     \&quot;title\&quot;: \&quot;Security scan report\&quot;,     \&quot;details\&quot;: \&quot;This pull request introduces 10 new dependency vulnerabilities.\&quot;,     \&quot;report_type\&quot;: \&quot;SECURITY\&quot;,     \&quot;reporter\&quot;: \&quot;mySystem\&quot;,     \&quot;link\&quot;: \&quot;http://www.mysystem.com/reports/001\&quot;,     \&quot;result\&quot;: \&quot;FAILED\&quot;,     \&quot;data\&quot;: [         {             \&quot;title\&quot;: \&quot;Duration (seconds)\&quot;,             \&quot;type\&quot;: \&quot;DURATION\&quot;,             \&quot;value\&quot;: 14         },         {             \&quot;title\&quot;: \&quot;Safe to merge?\&quot;,             \&quot;type\&quot;: \&quot;BOOLEAN\&quot;,             \&quot;value\&quot;: false         }     ] }&#39; &#x60;&#x60;&#x60;  ### Possible field values: report_type: SECURITY, COVERAGE, TEST, BUG result: PASSED, FAILED, PENDING data.type: BOOLEAN, DATE, DURATION, LINK, NUMBER, PERCENTAGE, TEXT  #### Data field formats | Type  Field   | Value Field Type  | Value Field Display | |:--------------|:------------------|:--------------------| | None/ Omitted | Number, String or Boolean (not an array or object) | Plain text | | BOOLEAN | Boolean | The value will be read as a JSON boolean and displayed as &#39;Yes&#39; or &#39;No&#39;. | | DATE  | Number | The value will be read as a JSON number in the form of a Unix timestamp (milliseconds) and will be displayed as a relative date if the date is less than one week ago, otherwise  it will be displayed as an absolute date. | | DURATION | Number | The value will be read as a JSON number in milliseconds and will be displayed in a human readable duration format. | | LINK | Object: &#x60;{\&quot;text\&quot;: \&quot;Link text here\&quot;, \&quot;href\&quot;: \&quot;https://link.to.annotation/in/external/tool\&quot;}&#x60; | The value will be read as a JSON object containing the fields \&quot;text\&quot; and \&quot;href\&quot; and will be displayed as a clickable link on the report. | | NUMBER | Number | The value will be read as a JSON number and large numbers will be  displayed in a human readable format (e.g. 14.3k). | | PERCENTAGE | Number (between 0 and 100) | The value will be read as a JSON number between 0 and 100 and will be displayed with a percentage sign. | | TEXT | String | The value will be read as a JSON string and will be displayed as-is |  Please refer to the [Code Insights documentation](https://confluence.atlassian.com/bitbucket/code-insights-994316785.html) for more information. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
    String repoSlug = "repoSlug_example"; // String | The repository.
    String commit = "commit_example"; // String | The commit the report belongs to.
    String reportId = "reportId_example"; // String | Either the uuid or external-id of the report.
    Report report = new Report(); // Report | The report to create or update
    try {
      Report result = apiInstance.createOrUpdateReport(workspace, repoSlug, commit, reportId, report);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#createOrUpdateReport");
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
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example &#x60;{workspace UUID}&#x60;. | |
| **repoSlug** | **String**| The repository. | |
| **commit** | **String**| The commit the report belongs to. | |
| **reportId** | **String**| Either the uuid or external-id of the report. | |
| **report** | [**Report**](Report.md)| The report to create or update | |

### Return type

[**Report**](Report.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | The provided Report object is malformed or incomplete. |  -  |

<a id="deleteAnnotation"></a>
# **deleteAnnotation**
> deleteAnnotation(workspace, repoSlug, commit, reportId, annotationId)

Delete an annotation

Deletes a single Annotation matching the provided ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
    String repoSlug = "repoSlug_example"; // String | The repository.
    String commit = "commit_example"; // String | The commit the annotation belongs to.
    String reportId = "reportId_example"; // String | Either the uuid or external-id of the annotation.
    String annotationId = "annotationId_example"; // String | Either the uuid or external-id of the annotation.
    try {
      apiInstance.deleteAnnotation(workspace, repoSlug, commit, reportId, annotationId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#deleteAnnotation");
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
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example &#x60;{workspace UUID}&#x60;. | |
| **repoSlug** | **String**| The repository. | |
| **commit** | **String**| The commit the annotation belongs to. | |
| **reportId** | **String**| Either the uuid or external-id of the annotation. | |
| **annotationId** | **String**| Either the uuid or external-id of the annotation. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No content |  -  |

<a id="deleteReport"></a>
# **deleteReport**
> deleteReport(workspace, repoSlug, commit, reportId)

Delete a report

Deletes a single Report matching the provided ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
    String repoSlug = "repoSlug_example"; // String | The repository.
    String commit = "commit_example"; // String | The commit the report belongs to.
    String reportId = "reportId_example"; // String | Either the uuid or external-id of the report.
    try {
      apiInstance.deleteReport(workspace, repoSlug, commit, reportId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#deleteReport");
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
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example &#x60;{workspace UUID}&#x60;. | |
| **repoSlug** | **String**| The repository. | |
| **commit** | **String**| The commit the report belongs to. | |
| **reportId** | **String**| Either the uuid or external-id of the report. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No content |  -  |

<a id="getAnnotation"></a>
# **getAnnotation**
> ReportAnnotation getAnnotation(workspace, repoSlug, commit, reportId, annotationId)

Get an annotation

Returns a single Annotation matching the provided ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
    String repoSlug = "repoSlug_example"; // String | The repository.
    String commit = "commit_example"; // String | The commit the report belongs to.
    String reportId = "reportId_example"; // String | Either the uuid or external-id of the report.
    String annotationId = "annotationId_example"; // String | Either the uuid or external-id of the annotation.
    try {
      ReportAnnotation result = apiInstance.getAnnotation(workspace, repoSlug, commit, reportId, annotationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#getAnnotation");
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
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example &#x60;{workspace UUID}&#x60;. | |
| **repoSlug** | **String**| The repository. | |
| **commit** | **String**| The commit the report belongs to. | |
| **reportId** | **String**| Either the uuid or external-id of the report. | |
| **annotationId** | **String**| Either the uuid or external-id of the annotation. | |

### Return type

[**ReportAnnotation**](ReportAnnotation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | The annotation with the given ID was not found. |  -  |

<a id="getAnnotationsForReport"></a>
# **getAnnotationsForReport**
> PaginatedAnnotations getAnnotationsForReport(workspace, repoSlug, commit, reportId)

List annotations

Returns a paginated list of Annotations for a specified report.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
    String repoSlug = "repoSlug_example"; // String | The repository.
    String commit = "commit_example"; // String | The commit for which to retrieve reports.
    String reportId = "reportId_example"; // String | Uuid or external-if of the report for which to get annotations for.
    try {
      PaginatedAnnotations result = apiInstance.getAnnotationsForReport(workspace, repoSlug, commit, reportId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#getAnnotationsForReport");
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
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example &#x60;{workspace UUID}&#x60;. | |
| **repoSlug** | **String**| The repository. | |
| **commit** | **String**| The commit for which to retrieve reports. | |
| **reportId** | **String**| Uuid or external-if of the report for which to get annotations for. | |

### Return type

[**PaginatedAnnotations**](PaginatedAnnotations.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getReport"></a>
# **getReport**
> Report getReport(workspace, repoSlug, commit, reportId)

Get a report

Returns a single Report matching the provided ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
    String repoSlug = "repoSlug_example"; // String | The repository.
    String commit = "commit_example"; // String | The commit the report belongs to.
    String reportId = "reportId_example"; // String | Either the uuid or external-id of the report.
    try {
      Report result = apiInstance.getReport(workspace, repoSlug, commit, reportId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#getReport");
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
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example &#x60;{workspace UUID}&#x60;. | |
| **repoSlug** | **String**| The repository. | |
| **commit** | **String**| The commit the report belongs to. | |
| **reportId** | **String**| Either the uuid or external-id of the report. | |

### Return type

[**Report**](Report.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | The report with the given ID was not found. |  -  |

<a id="getReportsForCommit"></a>
# **getReportsForCommit**
> PaginatedReports getReportsForCommit(workspace, repoSlug, commit)

List reports

Returns a paginated list of Reports linked to this commit.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example `{workspace UUID}`.
    String repoSlug = "repoSlug_example"; // String | The repository.
    String commit = "commit_example"; // String | The commit for which to retrieve reports.
    try {
      PaginatedReports result = apiInstance.getReportsForCommit(workspace, repoSlug, commit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#getReportsForCommit");
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
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example &#x60;{workspace UUID}&#x60;. | |
| **repoSlug** | **String**| The repository. | |
| **commit** | **String**| The commit for which to retrieve reports. | |

### Return type

[**PaginatedReports**](PaginatedReports.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

