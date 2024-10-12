# FileApi

All URIs are relative to *https://api.netlify.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getSiteFileByPathName**](FileApi.md#getSiteFileByPathName) | **GET** /sites/{site_id}/files/{file_path} |  |
| [**listSiteFiles**](FileApi.md#listSiteFiles) | **GET** /sites/{site_id}/files |  |
| [**uploadDeployFile**](FileApi.md#uploadDeployFile) | **PUT** /deploys/{deploy_id}/files/{path} |  |


<a id="getSiteFileByPathName"></a>
# **getSiteFileByPathName**
> File getSiteFileByPathName(siteId, filePath)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    FileApi apiInstance = new FileApi(defaultClient);
    String siteId = "siteId_example"; // String | 
    String filePath = "filePath_example"; // String | 
    try {
      File result = apiInstance.getSiteFileByPathName(siteId, filePath);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FileApi#getSiteFileByPathName");
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
| **siteId** | **String**|  | |
| **filePath** | **String**|  | |

### Return type

[**File**](File.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | error |  -  |

<a id="listSiteFiles"></a>
# **listSiteFiles**
> List&lt;File&gt; listSiteFiles(siteId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    FileApi apiInstance = new FileApi(defaultClient);
    String siteId = "siteId_example"; // String | 
    try {
      List<File> result = apiInstance.listSiteFiles(siteId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FileApi#listSiteFiles");
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
| **siteId** | **String**|  | |

### Return type

[**List&lt;File&gt;**](File.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | error |  -  |

<a id="uploadDeployFile"></a>
# **uploadDeployFile**
> File uploadDeployFile(deployId, path, fileBody, size)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    FileApi apiInstance = new FileApi(defaultClient);
    String deployId = "deployId_example"; // String | 
    String path = "path_example"; // String | 
    File fileBody = new File("/path/to/file"); // File | 
    Integer size = 56; // Integer | 
    try {
      File result = apiInstance.uploadDeployFile(deployId, path, fileBody, size);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FileApi#uploadDeployFile");
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
| **deployId** | **String**|  | |
| **path** | **String**|  | |
| **fileBody** | **File**|  | |
| **size** | **Integer**|  | [optional] |

### Return type

[**File**](File.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | error |  -  |

