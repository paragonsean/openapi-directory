# ArchivesApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**archiveImageAnalysis**](ArchivesApi.md#archiveImageAnalysis) | **POST** /archives/images |  |
| [**createAnalysisArchiveRule**](ArchivesApi.md#createAnalysisArchiveRule) | **POST** /archives/rules |  |
| [**deleteAnalysisArchiveRule**](ArchivesApi.md#deleteAnalysisArchiveRule) | **DELETE** /archives/rules/{ruleId} |  |
| [**deleteArchivedAnalysis**](ArchivesApi.md#deleteArchivedAnalysis) | **DELETE** /archives/images/{imageDigest} |  |
| [**getAnalysisArchiveRule**](ArchivesApi.md#getAnalysisArchiveRule) | **GET** /archives/rules/{ruleId} |  |
| [**getArchivedAnalysis**](ArchivesApi.md#getArchivedAnalysis) | **GET** /archives/images/{imageDigest} |  |
| [**listAnalysisArchive**](ArchivesApi.md#listAnalysisArchive) | **GET** /archives/images |  |
| [**listAnalysisArchiveRules**](ArchivesApi.md#listAnalysisArchiveRules) | **GET** /archives/rules |  |
| [**listArchives**](ArchivesApi.md#listArchives) | **GET** /archives |  |


<a id="archiveImageAnalysis"></a>
# **archiveImageAnalysis**
> List&lt;AnalysisArchiveAddResult&gt; archiveImageAnalysis(requestBody)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArchivesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ArchivesApi apiInstance = new ArchivesApi(defaultClient);
    List<String> requestBody = Arrays.asList(); // List<String> | 
    try {
      List<AnalysisArchiveAddResult> result = apiInstance.archiveImageAnalysis(requestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArchivesApi#archiveImageAnalysis");
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
| **requestBody** | [**List&lt;String&gt;**](String.md)|  | |

### Return type

[**List&lt;AnalysisArchiveAddResult&gt;**](AnalysisArchiveAddResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Archive statuses |  -  |
| **500** | Internal error |  -  |

<a id="createAnalysisArchiveRule"></a>
# **createAnalysisArchiveRule**
> AnalysisArchiveTransitionRule createAnalysisArchiveRule(analysisArchiveTransitionRule)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArchivesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ArchivesApi apiInstance = new ArchivesApi(defaultClient);
    AnalysisArchiveTransitionRule analysisArchiveTransitionRule = new AnalysisArchiveTransitionRule(); // AnalysisArchiveTransitionRule | 
    try {
      AnalysisArchiveTransitionRule result = apiInstance.createAnalysisArchiveRule(analysisArchiveTransitionRule);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArchivesApi#createAnalysisArchiveRule");
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
| **analysisArchiveTransitionRule** | [**AnalysisArchiveTransitionRule**](AnalysisArchiveTransitionRule.md)|  | |

### Return type

[**AnalysisArchiveTransitionRule**](AnalysisArchiveTransitionRule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Archive transition rule |  -  |
| **500** | Internal error |  -  |

<a id="deleteAnalysisArchiveRule"></a>
# **deleteAnalysisArchiveRule**
> deleteAnalysisArchiveRule(ruleId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArchivesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ArchivesApi apiInstance = new ArchivesApi(defaultClient);
    String ruleId = "ruleId_example"; // String | 
    try {
      apiInstance.deleteAnalysisArchiveRule(ruleId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArchivesApi#deleteAnalysisArchiveRule");
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
| **ruleId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Analysis archive rule succesfuly deleted |  -  |
| **500** | Internal error |  -  |

<a id="deleteArchivedAnalysis"></a>
# **deleteArchivedAnalysis**
> deleteArchivedAnalysis(imageDigest, force)



Performs a synchronous archive deletion

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArchivesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ArchivesApi apiInstance = new ArchivesApi(defaultClient);
    String imageDigest = "imageDigest_example"; // String | 
    Boolean force = true; // Boolean | 
    try {
      apiInstance.deleteArchivedAnalysis(imageDigest, force);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArchivesApi#deleteArchivedAnalysis");
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
| **imageDigest** | **String**|  | |
| **force** | **Boolean**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ArchivdImageAnalysis successfully deleted |  -  |
| **500** | Internal error |  -  |

<a id="getAnalysisArchiveRule"></a>
# **getAnalysisArchiveRule**
> AnalysisArchiveTransitionRule getAnalysisArchiveRule(ruleId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArchivesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ArchivesApi apiInstance = new ArchivesApi(defaultClient);
    String ruleId = "ruleId_example"; // String | 
    try {
      AnalysisArchiveTransitionRule result = apiInstance.getAnalysisArchiveRule(ruleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArchivesApi#getAnalysisArchiveRule");
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
| **ruleId** | **String**|  | |

### Return type

[**AnalysisArchiveTransitionRule**](AnalysisArchiveTransitionRule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Archive transition rule |  -  |
| **500** | Internal error |  -  |

<a id="getArchivedAnalysis"></a>
# **getArchivedAnalysis**
> ArchivedAnalysis getArchivedAnalysis(imageDigest)



Returns the archive metadata record identifying the image and tags for the analysis in the archive.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArchivesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ArchivesApi apiInstance = new ArchivesApi(defaultClient);
    String imageDigest = "imageDigest_example"; // String | The image digest to identify the image analysis
    try {
      ArchivedAnalysis result = apiInstance.getArchivedAnalysis(imageDigest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArchivesApi#getArchivedAnalysis");
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
| **imageDigest** | **String**| The image digest to identify the image analysis | |

### Return type

[**ArchivedAnalysis**](ArchivedAnalysis.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Archived Image |  -  |
| **500** | Internal error |  -  |

<a id="listAnalysisArchive"></a>
# **listAnalysisArchive**
> List&lt;ArchivedAnalysis&gt; listAnalysisArchive()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArchivesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ArchivesApi apiInstance = new ArchivesApi(defaultClient);
    try {
      List<ArchivedAnalysis> result = apiInstance.listAnalysisArchive();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArchivesApi#listAnalysisArchive");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;ArchivedAnalysis&gt;**](ArchivedAnalysis.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Image analysis archive listing for the requesting account (not the whole system) |  -  |
| **500** | Internal error |  -  |

<a id="listAnalysisArchiveRules"></a>
# **listAnalysisArchiveRules**
> List&lt;AnalysisArchiveTransitionRule&gt; listAnalysisArchiveRules(systemGlobal)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArchivesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ArchivesApi apiInstance = new ArchivesApi(defaultClient);
    Boolean systemGlobal = true; // Boolean | If true include system global rules (owned by admin) even for non-admin users. Defaults to true if not set. Can be set to false to exclude globals
    try {
      List<AnalysisArchiveTransitionRule> result = apiInstance.listAnalysisArchiveRules(systemGlobal);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArchivesApi#listAnalysisArchiveRules");
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
| **systemGlobal** | **Boolean**| If true include system global rules (owned by admin) even for non-admin users. Defaults to true if not set. Can be set to false to exclude globals | [optional] |

### Return type

[**List&lt;AnalysisArchiveTransitionRule&gt;**](AnalysisArchiveTransitionRule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Archive transition rules |  -  |
| **500** | Internal error |  -  |

<a id="listArchives"></a>
# **listArchives**
> ArchiveSummary listArchives()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArchivesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ArchivesApi apiInstance = new ArchivesApi(defaultClient);
    try {
      ArchiveSummary result = apiInstance.listArchives();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArchivesApi#listArchives");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Archive summary listing |  -  |
| **500** | Internal error |  -  |

