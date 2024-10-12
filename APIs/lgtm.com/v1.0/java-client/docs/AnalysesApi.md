# AnalysesApi

All URIs are relative to *https://lgtm.com/api/v1.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAlerts**](AnalysesApi.md#getAlerts) | **GET** /analyses/{analysis-id}/alerts | Get detailed alert information |
| [**getAnalysis**](AnalysesApi.md#getAnalysis) | **GET** /analyses/{analysis-id} | Get analysis summary |
| [**getAnalysisForCommit**](AnalysesApi.md#getAnalysisForCommit) | **GET** /analyses/{project-id}/commits/{commit-id} | Get analysis summary for a specific commit |
| [**requestAnalysis**](AnalysesApi.md#requestAnalysis) | **POST** /analyses/{project-id} | Run analysis of a specific commit |


<a id="getAlerts"></a>
# **getAlerts**
> Object getAlerts(analysisId, sarifVersion, excludedFiles)

Get detailed alert information

Download all the alerts found by an analysis. Use the &#x60;Accept:&#x60; request header to specify the output media type as either CSV or [SARIF](https://lgtm.com/help/lgtm/sarif-results-file):   - &#x60;application/sarif+json&#x60;: Alerts in SARIF format. If no version is specified the latest supported SARIF version is used. - &#x60;application/json&#x60;: Alerts in SARIF format (*deprecated*).    If no version is specified, [SARIF 2.0.0](http://docs.oasis-open.org/sarif/sarif/v2.0/sarif-v2.0.html)    is used for backwards compatibility.  - &#x60;text/csv&#x60;: Alerts in CSV format. The &#x60;text/csv&#x60; media type has two optional parameters:    - &#x60;charset&#x60;: determines the character encoding of the text, by default UTF-8.    - &#x60;header&#x60;: determines whether a header row with column names is &#x60;present&#x60; or &#x60;absent&#x60;.       The default value for this parameter is &#x60;present&#x60;.       For example, an Accept header with value &#x60;text/csv; header&#x3D;absent&#x60;        would result in CSV output without a header row.         To find the analysis identifier for a commit, use the &#x60;/analyses/{project-id}/commits/{commit-id}&#x60;  endpoint. For more information, see [Get analysis summary for a specific commit](https://lgtm.com/help/lgtm/api/api-v1#opIdgetAnalysisForCommit).  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalysesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://lgtm.com/api/v1.0");
    
    // Configure HTTP bearer authorization: access-token
    HttpBearerAuth access-token = (HttpBearerAuth) defaultClient.getAuthentication("access-token");
    access-token.setBearerToken("BEARER TOKEN");

    AnalysesApi apiInstance = new AnalysesApi(defaultClient);
    String analysisId = "analysisId_example"; // String | The analysis identifier.
    String sarifVersion = "sarifVersion_example"; // String | The desired version of the SARIF format. Currently supported versions are `1.0.0`, `2.0.0`, and `2.1.0`.
    Boolean excludedFiles = false; // Boolean | Set `true` to include results in files that are excluded from the output by default. This includes results in test code and generated files. For more information, see [File classification](https://lgtm.com/help/lgtm/file-classification).
    try {
      Object result = apiInstance.getAlerts(analysisId, sarifVersion, excludedFiles);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalysesApi#getAlerts");
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
| **analysisId** | **String**| The analysis identifier. | |
| **sarifVersion** | **String**| The desired version of the SARIF format. Currently supported versions are &#x60;1.0.0&#x60;, &#x60;2.0.0&#x60;, and &#x60;2.1.0&#x60;. | [optional] |
| **excludedFiles** | **Boolean**| Set &#x60;true&#x60; to include results in files that are excluded from the output by default. This includes results in test code and generated files. For more information, see [File classification](https://lgtm.com/help/lgtm/file-classification). | [optional] [default to false] |

### Return type

**Object**

### Authorization

[access-token](../README.md#access-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/sarif+json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success. Requested data returned. |  -  |

<a id="getAnalysis"></a>
# **getAnalysis**
> Analysis getAnalysis(analysisId)

Get analysis summary

Get a summary of the analysis results for a specific analysis identifier.  To find the analysis identifier for a commit, use the &#x60;/analyses/{project-id}/commits/{commit-id}&#x60; endpoint. For more information, see [Get analysis summary for a specific commit](https://lgtm.com/help/lgtm/api/api-v1#opIdgetAnalysisForCommit).  This endpoint reports the commit analyzed and a summary of the results for each language. Alternatively, you can use this identifier to download full details  of all the alerts found by the analysis. For more information, see [Get detailed alert information](https://lgtm.com/help/lgtm/api/api-v1#opIdgetAlerts). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalysesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://lgtm.com/api/v1.0");
    
    // Configure HTTP bearer authorization: access-token
    HttpBearerAuth access-token = (HttpBearerAuth) defaultClient.getAuthentication("access-token");
    access-token.setBearerToken("BEARER TOKEN");

    AnalysesApi apiInstance = new AnalysesApi(defaultClient);
    String analysisId = "analysisId_example"; // String | The analysis identifier.
    try {
      Analysis result = apiInstance.getAnalysis(analysisId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalysesApi#getAnalysis");
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
| **analysisId** | **String**| The analysis identifier. | |

### Return type

[**Analysis**](Analysis.md)

### Authorization

[access-token](../README.md#access-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success. Requested data returned. |  -  |

<a id="getAnalysisForCommit"></a>
# **getAnalysisForCommit**
> Analysis getAnalysisForCommit(projectId, commitId)

Get analysis summary for a specific commit

Get a summary of the analysis results for a specific commit, or the latest commit, to a project. (For projects configured for sparse or upload analysis, only &#x60;latest&#x60; is supported.)   This endpoint reports a summary of results for each language, and also the analysis identifier. You can use the analysis identifier to download full details of all the alerts  found by the analysis. For more information, see [Get detailed alert information](https://lgtm.com/help/lgtm/api/api-v1#opIdgetAlerts). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalysesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://lgtm.com/api/v1.0");
    
    // Configure HTTP bearer authorization: access-token
    HttpBearerAuth access-token = (HttpBearerAuth) defaultClient.getAuthentication("access-token");
    access-token.setBearerToken("BEARER TOKEN");

    AnalysesApi apiInstance = new AnalysesApi(defaultClient);
    Long projectId = 56L; // Long | The numeric project identifier.
    String commitId = "commitId_example"; // String | The identifier of a specific commit. Alternatively, use `latest` for the most recent analyzed commit.
    try {
      Analysis result = apiInstance.getAnalysisForCommit(projectId, commitId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalysesApi#getAnalysisForCommit");
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
| **projectId** | **Long**| The numeric project identifier. | |
| **commitId** | **String**| The identifier of a specific commit. Alternatively, use &#x60;latest&#x60; for the most recent analyzed commit. | |

### Return type

[**Analysis**](Analysis.md)

### Authorization

[access-token](../README.md#access-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success. Data returned. |  -  |

<a id="requestAnalysis"></a>
# **requestAnalysis**
> Operation requestAnalysis(projectId, commit, language)

Run analysis of a specific commit

Trigger the analysis of a specific commit to a project. If a previous attempt to analyze that commit failed, this triggers a fresh analysis.  This is supported for all LGTM projects, regardless of repository type or host. The commit must be available in the main repository, but can be on a branch that isn&#39;t tracked by LGTM. For both LGTM.com and LGTM Enterprise, you must include an access token with the &#x60;analyses:write&#x60; scope.  When you request the analysis of a commit, the API returns: - &#x60;operation-id&#x60;: used to track the status of the task using the &#x60;/operations&#x60; endpoint. For more information, see [Get operation status](https://lgtm.com/help/lgtm/api/api-v1#opIdgetOperation). - &#x60;status&#x60;: initially pending. - &#x60;task-result&#x60;: containing information about the progress and results of the analysis. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalysesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://lgtm.com/api/v1.0");
    
    // Configure HTTP bearer authorization: access-token
    HttpBearerAuth access-token = (HttpBearerAuth) defaultClient.getAuthentication("access-token");
    access-token.setBearerToken("BEARER TOKEN");

    AnalysesApi apiInstance = new AnalysesApi(defaultClient);
    Long projectId = 56L; // Long | The numeric project identifier.
    String commit = "commit_example"; // String | The identifier of the commit to analyze.
    List<String> language = Arrays.asList(); // List<String> | The language codes of the languages to analyze. For a list of available languages, see [Supported languages](https://lgtm.com/help/lgtm/analysis-faqs#which-languages-are-supported). To specify more than one language, this parameter can be repeated. If no language is specified, all the project's languages will be analyzed. 
    try {
      Operation result = apiInstance.requestAnalysis(projectId, commit, language);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalysesApi#requestAnalysis");
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
| **projectId** | **Long**| The numeric project identifier. | |
| **commit** | **String**| The identifier of the commit to analyze. | |
| **language** | [**List&lt;String&gt;**](String.md)| The language codes of the languages to analyze. For a list of available languages, see [Supported languages](https://lgtm.com/help/lgtm/analysis-faqs#which-languages-are-supported). To specify more than one language, this parameter can be repeated. If no language is specified, all the project&#39;s languages will be analyzed.  | [optional] |

### Return type

[**Operation**](Operation.md)

### Authorization

[access-token](../README.md#access-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Accepted. Analysis triggered. Tracking data returned. |  -  |

