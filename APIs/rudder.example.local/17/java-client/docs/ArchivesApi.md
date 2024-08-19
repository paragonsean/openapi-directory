# ArchivesApi

All URIs are relative to *https://rudder.example.local/rudder/api/latest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**callImport**](ArchivesApi.md#callImport) | **POST** /archives/import | Import a ZIP archive of policies into Rudder |
| [**export**](ArchivesApi.md#export) | **GET** /archives/export | Get a ZIP archive of the requested items and their dependencies |


<a id="callImport"></a>
# **callImport**
> Import200Response callImport(archive, merge)

Import a ZIP archive of policies into Rudder

Import a ZIP archive of techniques, directives, groups and rules in a saved in a normalized format into Rudder

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArchivesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    ArchivesApi apiInstance = new ArchivesApi(defaultClient);
    File archive = new File("/path/to/file"); // File | The ZIP archive file containing policies in a conventional layout and serialization format
    String merge = "override-all"; // String | Optional merge algo of the import. Default `override-all` means what is in the archive is the new reality. `keep-rule-groups` will keep existing target definition for existing rules (ignore archive value).
    try {
      Import200Response result = apiInstance.callImport(archive, merge);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArchivesApi#callImport");
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
| **archive** | **File**| The ZIP archive file containing policies in a conventional layout and serialization format | [optional] |
| **merge** | **String**| Optional merge algo of the import. Default &#x60;override-all&#x60; means what is in the archive is the new reality. &#x60;keep-rule-groups&#x60; will keep existing target definition for existing rules (ignore archive value). | [optional] [enum: override-all, keep-rule-groups] |

### Return type

[**Import200Response**](Import200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Archive imported |  -  |

<a id="export"></a>
# **export**
> File export(rules, directives, techniques, groups, include)

Get a ZIP archive of the requested items and their dependencies

Get a ZIP archive or rules, directives, techniques and groups with optionally their dependencies

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArchivesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    ArchivesApi apiInstance = new ArchivesApi(defaultClient);
    List<String> rules = Arrays.asList(); // List<String> | IDs (optionally with revision, '+' need to be escaped as '%2B') of rules to include
    List<String> directives = Arrays.asList(); // List<String> | IDs (optionally with revision, '+' need to be escaped as '%2B') of directives to include
    List<String> techniques = Arrays.asList(); // List<String> | IDs, ie technique name/technique version (optionally with revision, '+' need to be escaped as '%2B') of techniques to include
    List<String> groups = Arrays.asList(); // List<String> | IDs (optionally with revision, '+' need to be escaped as '%2B') of groups to include
    List<String> include = Arrays.asList(); // List<String> | Scope of dependencies to include in archive, where rule as directives and groups dependencies, directives have techniques dependencies, and techniques and groups don't have dependencies. 'none' means no dependencies will be include, 'all' means that the whole tree will,  'directives' and 'groups' means to include them specifically, 'techniques' means to include both directives and techniques.
    try {
      File result = apiInstance.export(rules, directives, techniques, groups, include);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArchivesApi#export");
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
| **rules** | [**List&lt;String&gt;**](String.md)| IDs (optionally with revision, &#39;+&#39; need to be escaped as &#39;%2B&#39;) of rules to include | [optional] |
| **directives** | [**List&lt;String&gt;**](String.md)| IDs (optionally with revision, &#39;+&#39; need to be escaped as &#39;%2B&#39;) of directives to include | [optional] |
| **techniques** | [**List&lt;String&gt;**](String.md)| IDs, ie technique name/technique version (optionally with revision, &#39;+&#39; need to be escaped as &#39;%2B&#39;) of techniques to include | [optional] |
| **groups** | [**List&lt;String&gt;**](String.md)| IDs (optionally with revision, &#39;+&#39; need to be escaped as &#39;%2B&#39;) of groups to include | [optional] |
| **include** | [**List&lt;String&gt;**](String.md)| Scope of dependencies to include in archive, where rule as directives and groups dependencies, directives have techniques dependencies, and techniques and groups don&#39;t have dependencies. &#39;none&#39; means no dependencies will be include, &#39;all&#39; means that the whole tree will,  &#39;directives&#39; and &#39;groups&#39; means to include them specifically, &#39;techniques&#39; means to include both directives and techniques. | [optional] [enum: all (default), none, directives, techniques, groups] |

### Return type

[**File**](File.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A zip archive with the queried content. |  -  |

