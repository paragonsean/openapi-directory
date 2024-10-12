# GitignoreApi

All URIs are relative to *http://HOSTNAME/api/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**gitignoreGetAllTemplates**](GitignoreApi.md#gitignoreGetAllTemplates) | **GET** /gitignore/templates | Get all gitignore templates |
| [**gitignoreGetTemplate**](GitignoreApi.md#gitignoreGetTemplate) | **GET** /gitignore/templates/{name} | Get a gitignore template |


<a id="gitignoreGetAllTemplates"></a>
# **gitignoreGetAllTemplates**
> List&lt;String&gt; gitignoreGetAllTemplates()

Get all gitignore templates

List all templates available to pass as an option when [creating a repository](https://docs.github.com/enterprise-server@2.19/rest/reference/repos#create-a-repository-for-the-authenticated-user).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GitignoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    GitignoreApi apiInstance = new GitignoreApi(defaultClient);
    try {
      List<String> result = apiInstance.gitignoreGetAllTemplates();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GitignoreApi#gitignoreGetAllTemplates");
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

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **304** | Not modified |  -  |

<a id="gitignoreGetTemplate"></a>
# **gitignoreGetTemplate**
> GitignoreTemplate gitignoreGetTemplate(name)

Get a gitignore template

The API also allows fetching the source of a single template. Use the raw [media type](https://docs.github.com/enterprise-server@2.19/rest/overview/media-types/) to get the raw contents.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GitignoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    GitignoreApi apiInstance = new GitignoreApi(defaultClient);
    String name = "name_example"; // String | 
    try {
      GitignoreTemplate result = apiInstance.gitignoreGetTemplate(name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GitignoreApi#gitignoreGetTemplate");
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
| **name** | **String**|  | |

### Return type

[**GitignoreTemplate**](GitignoreTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **304** | Not modified |  -  |

