# CodeScanningApi

All URIs are relative to *http://HOSTNAME/api/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**codeScanningGetAlert**](CodeScanningApi.md#codeScanningGetAlert) | **GET** /repos/{owner}/{repo}/code-scanning/alerts/{alert_number} | Get a code scanning alert |
| [**codeScanningListAlertsForRepo**](CodeScanningApi.md#codeScanningListAlertsForRepo) | **GET** /repos/{owner}/{repo}/code-scanning/alerts | List code scanning alerts for a repository |
| [**codeScanningListRecentAnalyses**](CodeScanningApi.md#codeScanningListRecentAnalyses) | **GET** /repos/{owner}/{repo}/code-scanning/analyses | List code scanning analyses for a repository |
| [**codeScanningUpdateAlert**](CodeScanningApi.md#codeScanningUpdateAlert) | **PATCH** /repos/{owner}/{repo}/code-scanning/alerts/{alert_number} | Update a code scanning alert |
| [**codeScanningUploadSarif**](CodeScanningApi.md#codeScanningUploadSarif) | **POST** /repos/{owner}/{repo}/code-scanning/sarifs | Upload an analysis as SARIF data |


<a id="codeScanningGetAlert"></a>
# **codeScanningGetAlert**
> CodeScanningAlert codeScanningGetAlert(owner, repo, alertNumber)

Get a code scanning alert

Gets a single code scanning alert. You must use an access token with the &#x60;security_events&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;security_events&#x60; read permission to use this endpoint.  **Deprecation notice**: The instances field is deprecated and will, in future, not be included in the response for this endpoint. From GitHub Enterprise Server 3.0, the same information can be retrieved via a GET request to the URL specified by &#x60;instances_url&#x60;, added in that release.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CodeScanningApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    CodeScanningApi apiInstance = new CodeScanningApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer alertNumber = 56; // Integer | The number that identifies an alert. You can find this at the end of the URL for a code scanning alert within GitHub, and in the `number` field in the response from the `GET /repos/{owner}/{repo}/code-scanning/alerts` operation.
    try {
      CodeScanningAlert result = apiInstance.codeScanningGetAlert(owner, repo, alertNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CodeScanningApi#codeScanningGetAlert");
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
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **alertNumber** | **Integer**| The number that identifies an alert. You can find this at the end of the URL for a code scanning alert within GitHub, and in the &#x60;number&#x60; field in the response from the &#x60;GET /repos/{owner}/{repo}/code-scanning/alerts&#x60; operation. | |

### Return type

[**CodeScanningAlert**](CodeScanningAlert.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **503** | Service unavailable |  -  |

<a id="codeScanningListAlertsForRepo"></a>
# **codeScanningListAlertsForRepo**
> List&lt;CodeScanningAlertItems&gt; codeScanningListAlertsForRepo(owner, repo, toolName, toolGuid, page, perPage, ref, state)

List code scanning alerts for a repository

Lists all open code scanning alerts for the default branch (usually &#x60;main&#x60; or &#x60;master&#x60;). You must use an access token with the &#x60;security_events&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;security_events&#x60; read permission to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CodeScanningApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    CodeScanningApi apiInstance = new CodeScanningApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String toolName = "toolName_example"; // String | The name of a code scanning tool. Only results by this tool will be listed. You can specify the tool by using either `tool_name` or `tool_guid`, but not both.
    String toolGuid = "toolGuid_example"; // String | The GUID of a code scanning tool. Only results by this tool will be listed. Note that some code scanning tools may not include a GUID in their analysis data. You can specify the tool by using either `tool_guid` or `tool_name`, but not both.
    Integer page = 1; // Integer | Page number of the results to fetch.
    Integer perPage = 30; // Integer | Results per page (max 100)
    String ref = "ref_example"; // String | The Git reference for the results you want to list. The `ref` for a branch can be formatted either as `refs/heads/<branch name>` or simply `<branch name>`. To reference a pull request use `refs/pull/<number>/merge`.
    CodeScanningAlertState state = CodeScanningAlertState.fromValue("open"); // CodeScanningAlertState | Set to `open`, `fixed`, or `dismissed` to list code scanning alerts in a specific state.
    try {
      List<CodeScanningAlertItems> result = apiInstance.codeScanningListAlertsForRepo(owner, repo, toolName, toolGuid, page, perPage, ref, state);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CodeScanningApi#codeScanningListAlertsForRepo");
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
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **toolName** | **String**| The name of a code scanning tool. Only results by this tool will be listed. You can specify the tool by using either &#x60;tool_name&#x60; or &#x60;tool_guid&#x60;, but not both. | [optional] |
| **toolGuid** | **String**| The GUID of a code scanning tool. Only results by this tool will be listed. Note that some code scanning tools may not include a GUID in their analysis data. You can specify the tool by using either &#x60;tool_guid&#x60; or &#x60;tool_name&#x60;, but not both. | [optional] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **ref** | **String**| The Git reference for the results you want to list. The &#x60;ref&#x60; for a branch can be formatted either as &#x60;refs/heads/&lt;branch name&gt;&#x60; or simply &#x60;&lt;branch name&gt;&#x60;. To reference a pull request use &#x60;refs/pull/&lt;number&gt;/merge&#x60;. | [optional] |
| **state** | [**CodeScanningAlertState**](.md)| Set to &#x60;open&#x60;, &#x60;fixed&#x60;, or &#x60;dismissed&#x60; to list code scanning alerts in a specific state. | [optional] [enum: open, closed, dismissed, fixed] |

### Return type

[**List&lt;CodeScanningAlertItems&gt;**](CodeScanningAlertItems.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **503** | Service unavailable |  -  |

<a id="codeScanningListRecentAnalyses"></a>
# **codeScanningListRecentAnalyses**
> List&lt;CodeScanningAnalysis&gt; codeScanningListRecentAnalyses(owner, repo, toolName, toolGuid, page, perPage, ref, sarifId)

List code scanning analyses for a repository

Lists the details of all code scanning analyses for a repository, starting with the most recent. The response is paginated and you can use the &#x60;page&#x60; and &#x60;per_page&#x60; parameters to list the analyses you&#39;re interested in. By default 30 analyses are listed per page.  The &#x60;rules_count&#x60; field in the response give the number of rules that were run in the analysis. For very old analyses this data is not available, and &#x60;0&#x60; is returned in this field.  You must use an access token with the &#x60;security_events&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;security_events&#x60; read permission to use this endpoint.  **Deprecation notice**: The &#x60;tool_name&#x60; field is deprecated and will, in future, not be included in the response for this endpoint. The example response reflects this change. The tool name can now be found inside the &#x60;tool&#x60; field.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CodeScanningApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    CodeScanningApi apiInstance = new CodeScanningApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String toolName = "toolName_example"; // String | The name of a code scanning tool. Only results by this tool will be listed. You can specify the tool by using either `tool_name` or `tool_guid`, but not both.
    String toolGuid = "toolGuid_example"; // String | The GUID of a code scanning tool. Only results by this tool will be listed. Note that some code scanning tools may not include a GUID in their analysis data. You can specify the tool by using either `tool_guid` or `tool_name`, but not both.
    Integer page = 1; // Integer | Page number of the results to fetch.
    Integer perPage = 30; // Integer | Results per page (max 100)
    String ref = "ref_example"; // String | The Git reference for the analyses you want to list. The `ref` for a branch can be formatted either as `refs/heads/<branch name>` or simply `<branch name>`. To reference a pull request use `refs/pull/<number>/merge`.
    String sarifId = "sarifId_example"; // String | Filter analyses belonging to the same SARIF upload.
    try {
      List<CodeScanningAnalysis> result = apiInstance.codeScanningListRecentAnalyses(owner, repo, toolName, toolGuid, page, perPage, ref, sarifId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CodeScanningApi#codeScanningListRecentAnalyses");
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
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **toolName** | **String**| The name of a code scanning tool. Only results by this tool will be listed. You can specify the tool by using either &#x60;tool_name&#x60; or &#x60;tool_guid&#x60;, but not both. | [optional] |
| **toolGuid** | **String**| The GUID of a code scanning tool. Only results by this tool will be listed. Note that some code scanning tools may not include a GUID in their analysis data. You can specify the tool by using either &#x60;tool_guid&#x60; or &#x60;tool_name&#x60;, but not both. | [optional] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **ref** | **String**| The Git reference for the analyses you want to list. The &#x60;ref&#x60; for a branch can be formatted either as &#x60;refs/heads/&lt;branch name&gt;&#x60; or simply &#x60;&lt;branch name&gt;&#x60;. To reference a pull request use &#x60;refs/pull/&lt;number&gt;/merge&#x60;. | [optional] |
| **sarifId** | **String**| Filter analyses belonging to the same SARIF upload. | [optional] |

### Return type

[**List&lt;CodeScanningAnalysis&gt;**](CodeScanningAnalysis.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **503** | Service unavailable |  -  |

<a id="codeScanningUpdateAlert"></a>
# **codeScanningUpdateAlert**
> CodeScanningAlert codeScanningUpdateAlert(owner, repo, alertNumber, codeScanningUpdateAlertRequest)

Update a code scanning alert

Updates the status of a single code scanning alert. You must use an access token with the &#x60;security_events&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;security_events&#x60; write permission to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CodeScanningApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    CodeScanningApi apiInstance = new CodeScanningApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer alertNumber = 56; // Integer | The number that identifies an alert. You can find this at the end of the URL for a code scanning alert within GitHub, and in the `number` field in the response from the `GET /repos/{owner}/{repo}/code-scanning/alerts` operation.
    CodeScanningUpdateAlertRequest codeScanningUpdateAlertRequest = new CodeScanningUpdateAlertRequest(); // CodeScanningUpdateAlertRequest | 
    try {
      CodeScanningAlert result = apiInstance.codeScanningUpdateAlert(owner, repo, alertNumber, codeScanningUpdateAlertRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CodeScanningApi#codeScanningUpdateAlert");
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
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **alertNumber** | **Integer**| The number that identifies an alert. You can find this at the end of the URL for a code scanning alert within GitHub, and in the &#x60;number&#x60; field in the response from the &#x60;GET /repos/{owner}/{repo}/code-scanning/alerts&#x60; operation. | |
| **codeScanningUpdateAlertRequest** | [**CodeScanningUpdateAlertRequest**](CodeScanningUpdateAlertRequest.md)|  | |

### Return type

[**CodeScanningAlert**](CodeScanningAlert.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **503** | Service unavailable |  -  |

<a id="codeScanningUploadSarif"></a>
# **codeScanningUploadSarif**
> CodeScanningSarifsReceipt codeScanningUploadSarif(owner, repo, codeScanningUploadSarifRequest)

Upload an analysis as SARIF data

Uploads SARIF data containing the results of a code scanning analysis to make the results available in a repository. You must use an access token with the &#x60;security_events&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;security_events&#x60; write permission to use this endpoint.  There are two places where you can upload code scanning results.  - If you upload to a pull request, for example &#x60;--ref refs/pull/42/merge&#x60; or &#x60;--ref refs/pull/42/head&#x60;, then the results appear as alerts in a pull request check. For more information, see \&quot;[Triaging code scanning alerts in pull requests](/github/finding-security-vulnerabilities-and-errors-in-your-code/automatically-scanning-your-code-for-vulnerabilities-and-errors/triaging-code-scanning-alerts-in-pull-requests).\&quot;  - If you upload to a branch, for example &#x60;--ref refs/heads/my-branch&#x60;, then the results appear in the **Security** tab for your repository. For more information, see \&quot;[Managing code scanning alerts for your repository](/github/finding-security-vulnerabilities-and-errors-in-your-code/automatically-scanning-your-code-for-vulnerabilities-and-errors/managing-code-scanning-alerts-for-your-repository#viewing-the-alerts-for-a-repository).\&quot;  You must compress the SARIF-formatted analysis data that you want to upload, using &#x60;gzip&#x60;, and then encode it as a Base64 format string. For example:  &#x60;&#x60;&#x60; gzip -c analysis-data.sarif | base64 -w0 &#x60;&#x60;&#x60;  SARIF upload supports a maximum of 1000 results per analysis run. Any results over this limit are ignored. Typically, but not necessarily, a SARIF file contains a single run of a single tool. If a code scanning tool generates too many results, you should update the analysis configuration to run only the most important rules or queries.  The &#x60;202 Accepted&#x60;, response includes an &#x60;id&#x60; value. You can use this ID to check the status of the upload by using this for the &#x60;/sarifs/{sarif_id}&#x60; endpoint. For more information, see \&quot;[Get information about a SARIF upload](/rest/reference/code-scanning#get-information-about-a-sarif-upload).\&quot;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CodeScanningApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    CodeScanningApi apiInstance = new CodeScanningApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    CodeScanningUploadSarifRequest codeScanningUploadSarifRequest = new CodeScanningUploadSarifRequest(); // CodeScanningUploadSarifRequest | 
    try {
      CodeScanningSarifsReceipt result = apiInstance.codeScanningUploadSarif(owner, repo, codeScanningUploadSarifRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CodeScanningApi#codeScanningUploadSarif");
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
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **codeScanningUploadSarifRequest** | [**CodeScanningUploadSarifRequest**](CodeScanningUploadSarifRequest.md)|  | |

### Return type

[**CodeScanningSarifsReceipt**](CodeScanningSarifsReceipt.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Response |  -  |
| **400** | Bad Request if the sarif field is invalid |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **413** | Payload Too Large if the sarif field is too large |  -  |
| **503** | Service unavailable |  -  |

