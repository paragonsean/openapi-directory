# ResourcesApi

All URIs are relative to *https://accountname.exavault.com/api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addFolder**](ResourcesApi.md#addFolder) | **POST** /resources | Create a folder |
| [**compressFiles**](ResourcesApi.md#compressFiles) | **POST** /resources/compress | Compress resources |
| [**copyResources**](ResourcesApi.md#copyResources) | **POST** /resources/copy | Copy resources |
| [**deleteResourceById**](ResourcesApi.md#deleteResourceById) | **DELETE** /resources/{id} | Delete a Resource |
| [**deleteResources**](ResourcesApi.md#deleteResources) | **DELETE** /resources | Delete Resources |
| [**download**](ResourcesApi.md#download) | **GET** /resources/download | Download a file |
| [**extractFiles**](ResourcesApi.md#extractFiles) | **POST** /resources/extract | Extract resources |
| [**getPreviewImage**](ResourcesApi.md#getPreviewImage) | **GET** /resources/preview | Preview a file |
| [**getResourceInfo**](ResourcesApi.md#getResourceInfo) | **GET** /resources | Get Resource Properties |
| [**getResourceInfoById**](ResourcesApi.md#getResourceInfoById) | **GET** /resources/{id} | Get resource metadata |
| [**listResourceContents**](ResourcesApi.md#listResourceContents) | **GET** /resources/list/{id} | List contents of folder |
| [**listResources**](ResourcesApi.md#listResources) | **GET** /resources/list | Get a list of all resources |
| [**moveResources**](ResourcesApi.md#moveResources) | **POST** /resources/move | Move resources |
| [**updateResourceById**](ResourcesApi.md#updateResourceById) | **PATCH** /resources/{id} | Rename a resource. |
| [**uploadFile**](ResourcesApi.md#uploadFile) | **POST** /resources/upload | Upload a file |


<a id="addFolder"></a>
# **addFolder**
> ResourceResponse addFolder(evApiKey, evAccessToken, addFolderRequestBody)

Create a folder

Create a new empty folder at the specified path. New files can be uploaded via the [/resources/upload](#operation/uploadFile) endpoint.  **Notes:** - Authenticated user should have modify permission. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://accountname.exavault.com/api/v2");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    String evApiKey = "evApiKey_example"; // String | API Key required to make the API call.
    String evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
    AddFolderRequestBody addFolderRequestBody = new AddFolderRequestBody(); // AddFolderRequestBody | 
    try {
      ResourceResponse result = apiInstance.addFolder(evApiKey, evAccessToken, addFolderRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#addFolder");
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
| **evApiKey** | **String**| API Key required to make the API call. | |
| **evAccessToken** | **String**| Access token required to make the API call. | |
| **addFolderRequestBody** | [**AddFolderRequestBody**](AddFolderRequestBody.md)|  | [optional] |

### Return type

[**ResourceResponse**](ResourceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful Operation |  -  |

<a id="compressFiles"></a>
# **compressFiles**
> ResourceResponse compressFiles(evApiKey, evAccessToken, compressFilesRequestBody)

Compress resources

Create a zip archive containing the files from given set of paths. Note that this can be a very slow operation if you have indicated many files should be included in the archive.  **Notes:** - Authenticated user should have modify permission. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://accountname.exavault.com/api/v2");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    String evApiKey = "evApiKey_example"; // String | API Key required to make the API call.
    String evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
    CompressFilesRequestBody compressFilesRequestBody = new CompressFilesRequestBody(); // CompressFilesRequestBody | 
    try {
      ResourceResponse result = apiInstance.compressFiles(evApiKey, evAccessToken, compressFilesRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#compressFiles");
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
| **evApiKey** | **String**| API Key required to make the API call. | |
| **evAccessToken** | **String**| Access token required to make the API call. | |
| **compressFilesRequestBody** | [**CompressFilesRequestBody**](CompressFilesRequestBody.md)|  | [optional] |

### Return type

[**ResourceResponse**](ResourceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful Operation |  -  |

<a id="copyResources"></a>
# **copyResources**
> ResourceCopyMove copyResources(evApiKey, evAccessToken, copyResourcesRequestBody)

Copy resources

Copies a set of exisiting files/folders (provided by an array &#x60;resources&#x60;) to the requested &#x60;parentResource&#x60; in your account. In the &#x60;resources&#x60; array, you may specify paths pointing files/folders throughout the account, but everything will be copied to the  root of the &#x60;parentResource&#x60;.  **Notes:** - Authenticated user should have modify permission. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://accountname.exavault.com/api/v2");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    String evApiKey = "evApiKey_example"; // String | API Key required to make the API call.
    String evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
    CopyResourcesRequestBody copyResourcesRequestBody = new CopyResourcesRequestBody(); // CopyResourcesRequestBody | 
    try {
      ResourceCopyMove result = apiInstance.copyResources(evApiKey, evAccessToken, copyResourcesRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#copyResources");
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
| **evApiKey** | **String**| API Key required to make the API call. | |
| **evAccessToken** | **String**| Access token required to make the API call. | |
| **copyResourcesRequestBody** | [**CopyResourcesRequestBody**](CopyResourcesRequestBody.md)|  | [optional] |

### Return type

[**ResourceCopyMove**](ResourceCopyMove.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Operation |  -  |
| **207** | Multi Response |  -  |

<a id="deleteResourceById"></a>
# **deleteResourceById**
> EmptyResponse deleteResourceById(id, evApiKey, evAccessToken)

Delete a Resource

Delete a single file or folder resource. Deleting a folder will also delete all of the contents.  **Notes:** - Authenticated user should have [delete permission](/docs/account/04-users/00-introduction#managing-user-roles-and-permissions). - There is no way to un-delete a deleted resource. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://accountname.exavault.com/api/v2");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    Long id = 56L; // Long | ID number of the resource
    String evApiKey = "evApiKey_example"; // String | API Key required to make the API call.
    String evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
    try {
      EmptyResponse result = apiInstance.deleteResourceById(id, evApiKey, evAccessToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#deleteResourceById");
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
| **id** | **Long**| ID number of the resource | |
| **evApiKey** | **String**| API Key required to make the API call. | |
| **evAccessToken** | **String**| Access token required to make the API call. | |

### Return type

[**EmptyResponse**](EmptyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Operation |  -  |

<a id="deleteResources"></a>
# **deleteResources**
> EmptyResponse deleteResources(evApiKey, evAccessToken, deleteResourcesRequestBody)

Delete Resources

Delete multiple file or folder resourcess. Deleting a folder resource will also delete any resources in that folder.  **Notes:** - Authenticated user should have [delete permission](/docs/account/04-users/00-introduction#managing-user-roles-and-permissions). - It is not possible to un-delete a deleted resource. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://accountname.exavault.com/api/v2");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    String evApiKey = "exampleaccount-zwSuWUZ8S38h33qPS8v0s"; // String | API Key
    String evAccessToken = "19853ef63a0bc348024a9e4cfd4a92520d2dfd04e88d8679fb1ed6bc551593d1"; // String | Access Token
    DeleteResourcesRequestBody deleteResourcesRequestBody = new DeleteResourcesRequestBody(); // DeleteResourcesRequestBody | 
    try {
      EmptyResponse result = apiInstance.deleteResources(evApiKey, evAccessToken, deleteResourcesRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#deleteResources");
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
| **evApiKey** | **String**| API Key | |
| **evAccessToken** | **String**| Access Token | |
| **deleteResourcesRequestBody** | [**DeleteResourcesRequestBody**](DeleteResourcesRequestBody.md)|  | [optional] |

### Return type

[**EmptyResponse**](EmptyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Operation |  -  |
| **207** | Multi Response |  -  |

<a id="download"></a>
# **download**
> File download(evApiKey, evAccessToken, resources, downloadArchiveName)

Download a file

Downloads a file from the server. Whenever more than one file is being downloaded, the file are first zipped into  a single file before the download starts, and the resulting zip file is named to match the &#x60;downloadArchiveName&#x60; parameter.  **NOTE**: Downloading many files at once  may result in a long delay before the API will return a response. You may need to override default timeout values in your API client, or download files individually.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://accountname.exavault.com/api/v2");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    String evApiKey = "evApiKey_example"; // String | API Key required to make the API call.
    String evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
    List<String> resources = Arrays.asList(); // List<String> | Path of file or folder to be downloaded, starting from the root. Can also be an array of paths.
    String downloadArchiveName = "downloadArchiveName_example"; // String | When downloading multiple files, this will be used as the name of the zip file that is created.
    try {
      File result = apiInstance.download(evApiKey, evAccessToken, resources, downloadArchiveName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#download");
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
| **evApiKey** | **String**| API Key required to make the API call. | |
| **evAccessToken** | **String**| Access token required to make the API call. | |
| **resources** | [**List&lt;String&gt;**](String.md)| Path of file or folder to be downloaded, starting from the root. Can also be an array of paths. | |
| **downloadArchiveName** | **String**| When downloading multiple files, this will be used as the name of the zip file that is created. | [optional] |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/zip

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Content of the file |  -  |

<a id="extractFiles"></a>
# **extractFiles**
> ResourceCollectionResponse extractFiles(evApiKey, evAccessToken, extractFilesRequestBody)

Extract resources

Extract the contents of a zip archive to a specified directory. Note that this can be a very slow operation.  **Notes:** - You must have  [modify permission](/docs/account/04-users/00-introduction#managing-user-roles-and-permissions) to do this. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://accountname.exavault.com/api/v2");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    String evApiKey = "evApiKey_example"; // String | API Key required to make the API call.
    String evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
    ExtractFilesRequestBody extractFilesRequestBody = new ExtractFilesRequestBody(); // ExtractFilesRequestBody | 
    try {
      ResourceCollectionResponse result = apiInstance.extractFiles(evApiKey, evAccessToken, extractFilesRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#extractFiles");
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
| **evApiKey** | **String**| API Key required to make the API call. | |
| **evAccessToken** | **String**| Access token required to make the API call. | |
| **extractFilesRequestBody** | [**ExtractFilesRequestBody**](ExtractFilesRequestBody.md)|  | [optional] |

### Return type

[**ResourceCollectionResponse**](ResourceCollectionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful Operation |  -  |

<a id="getPreviewImage"></a>
# **getPreviewImage**
> PreviewFileResponse getPreviewImage(evApiKey, evAccessToken, resource, size, width, height, page)

Preview a file

Returns a resized image of the specified document for supported file types.  Image data returned is encoded in base64 format and can be viewed using the &#x60;&lt;img&gt;&#x60; element.   &#x60;&#x60;&#x60;&lt;img src&#x3D;&#39;data:image/jpeg;base64&#39; + meta.image/&gt;&#x60;&#x60;&#x60;  **Notes:** - Supported files types are &#x60;&#39;jpg&#39;&#x60;, &#x60;&#39;jpeg&#39;&#x60;, &#x60;&#39;gif&#39;&#x60;, &#x60;&#39;png&#39;&#x60;, &#x60;&#39;bmp&#39;&#x60;, &#x60;&#39;pdf&#39;&#x60;, &#x60;&#39;psd&#39;&#x60;, &#x60;&#39;doc&#39;&#x60; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://accountname.exavault.com/api/v2");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    String evApiKey = "exampleaccount-zwSuWUZ8S38h33qPS8v0s"; // String | API Key
    String evAccessToken = "19853ef63a0bc348024a9e4cfd4a92520d2dfd04e88d8679fb1ed6bc551593d1"; // String | Access Token
    String resource = "resource_example"; // String | Resource identifier for the image file.
    String size = "small"; // String | The size of the image.
    Integer width = 56; // Integer | Overrides sizes. Sets to a specific width.
    Integer height = 56; // Integer | Overrides sizes. Sets to a specific height.
    Integer page = 0; // Integer | Page number to extract from a multi-page document (0 is the first page). Vaild for **.pdf** or **.doc** files.
    try {
      PreviewFileResponse result = apiInstance.getPreviewImage(evApiKey, evAccessToken, resource, size, width, height, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#getPreviewImage");
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
| **evApiKey** | **String**| API Key | |
| **evAccessToken** | **String**| Access Token | |
| **resource** | **String**| Resource identifier for the image file. | |
| **size** | **String**| The size of the image. | [enum: small, medium, large] |
| **width** | **Integer**| Overrides sizes. Sets to a specific width. | [optional] |
| **height** | **Integer**| Overrides sizes. Sets to a specific height. | [optional] |
| **page** | **Integer**| Page number to extract from a multi-page document (0 is the first page). Vaild for **.pdf** or **.doc** files. | [optional] [default to 0] |

### Return type

[**PreviewFileResponse**](PreviewFileResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Operation |  -  |

<a id="getResourceInfo"></a>
# **getResourceInfo**
> ResourceResponse getResourceInfo(evApiKey, evAccessToken, resource, include)

Get Resource Properties

Returns details for specified file/folder id or hash, including upload date, size and type. For the full list of returned properties, see the response syntax, below.  **Notes:** - Authenticated user should have list permission. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://accountname.exavault.com/api/v2");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    String evApiKey = "evApiKey_example"; // String | API Key required to make the API call.
    String evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
    String resource = "resource_example"; // String | Resource identifier of the file or folder to get metadata for.
    String include = "include_example"; // String | Comma separated list of relationships to include in response. Possible values are **share**, **notifications**, **directFile**, **parentResource**, **ownerUser**, **ownerUser**.
    try {
      ResourceResponse result = apiInstance.getResourceInfo(evApiKey, evAccessToken, resource, include);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#getResourceInfo");
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
| **evApiKey** | **String**| API Key required to make the API call. | |
| **evAccessToken** | **String**| Access token required to make the API call. | |
| **resource** | **String**| Resource identifier of the file or folder to get metadata for. | |
| **include** | **String**| Comma separated list of relationships to include in response. Possible values are **share**, **notifications**, **directFile**, **parentResource**, **ownerUser**, **ownerUser**. | [optional] |

### Return type

[**ResourceResponse**](ResourceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Operation |  -  |

<a id="getResourceInfoById"></a>
# **getResourceInfoById**
> ResourceResponse getResourceInfoById(id, evApiKey, evAccessToken, include)

Get resource metadata

Returns metadata for specified file/folder path, including upload date, size and type. For the full list of returned properties, see the response syntax, below.  **Notes:** - Authenticated user should have list permission. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://accountname.exavault.com/api/v2");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    Long id = 56L; // Long | ID number of the resource
    String evApiKey = "evApiKey_example"; // String | API Key required to make the API call.
    String evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
    String include = "include_example"; // String | Comma separated list of relationships to include in response. Possible values are **share**, **notifications**, **directFile**, **parentResource**, **ownerUser**, **ownerAccount**.
    try {
      ResourceResponse result = apiInstance.getResourceInfoById(id, evApiKey, evAccessToken, include);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#getResourceInfoById");
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
| **id** | **Long**| ID number of the resource | |
| **evApiKey** | **String**| API Key required to make the API call. | |
| **evAccessToken** | **String**| Access token required to make the API call. | |
| **include** | **String**| Comma separated list of relationships to include in response. Possible values are **share**, **notifications**, **directFile**, **parentResource**, **ownerUser**, **ownerAccount**. | [optional] |

### Return type

[**ResourceResponse**](ResourceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Operation |  -  |

<a id="listResourceContents"></a>
# **listResourceContents**
> ResourceCollectionResponse listResourceContents(evApiKey, evAccessToken, id, sort, offset, limit, type, include)

List contents of folder

Returns a list of files/folders for the parent resource ID.   You can use this API call to get information about all files and folders at a specified path. By default, the API returns basic metadata on each file/folder. An optional &#x60;include&#x60; parameter forces the return of additional metadata. As with all API calls, the path should be the full path relative to the user&#39;s home directory (e.g. **_/myfiles/some_folder**).  **Notes:** - Authenticated user should have list permission. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://accountname.exavault.com/api/v2");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    String evApiKey = "evApiKey_example"; // String | API Key required to make the API call. 
    String evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
    Long id = 56L; // Long | ID of the parent resource to get a list of resources for.
    String sort = "name"; // String | Endpoint support multiple sort fields by allowing array of sort params. Sort fields should be applied in the order specified. The sort order for each sort field is ascending unless it is prefixed with a minus (“-“), in which case it will be descending.
    Integer offset = 0; // Integer | Determines which item to start on for pagination. Use zero (0) to start at the beginning of the list.
    Integer limit = 56; // Integer | The number of files to limit the result. Cannot be set higher than 100. If you have more than one hundred files in your directory, make multiple calls, incrementing the `offset parameter, above.
    String type = "type_example"; // String | Limit types of resources returned to \"file\" or \"dir\" only.
    String include = "include_example"; // String | Comma separated list of relationships to include in response. Possible values are **share**, **notifications**, **directFile**, **parentResource**, **ownerUser**, **ownerUser**.
    try {
      ResourceCollectionResponse result = apiInstance.listResourceContents(evApiKey, evAccessToken, id, sort, offset, limit, type, include);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#listResourceContents");
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
| **evApiKey** | **String**| API Key required to make the API call.  | |
| **evAccessToken** | **String**| Access token required to make the API call. | |
| **id** | **Long**| ID of the parent resource to get a list of resources for. | |
| **sort** | **String**| Endpoint support multiple sort fields by allowing array of sort params. Sort fields should be applied in the order specified. The sort order for each sort field is ascending unless it is prefixed with a minus (“-“), in which case it will be descending. | [optional] |
| **offset** | **Integer**| Determines which item to start on for pagination. Use zero (0) to start at the beginning of the list. | [optional] [default to 0] |
| **limit** | **Integer**| The number of files to limit the result. Cannot be set higher than 100. If you have more than one hundred files in your directory, make multiple calls, incrementing the &#x60;offset parameter, above. | [optional] |
| **type** | **String**| Limit types of resources returned to \&quot;file\&quot; or \&quot;dir\&quot; only. | [optional] |
| **include** | **String**| Comma separated list of relationships to include in response. Possible values are **share**, **notifications**, **directFile**, **parentResource**, **ownerUser**, **ownerUser**. | [optional] |

### Return type

[**ResourceCollectionResponse**](ResourceCollectionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Operation |  -  |

<a id="listResources"></a>
# **listResources**
> ResourceCollectionResponse listResources(evApiKey, evAccessToken, resource, sort, offset, limit, type, name, include)

Get a list of all resources

Returns a list of files and folders in the account. Use the &#x60;resource&#x60; query parameter to indicate the folder you wish to search in (which can be /).   **Searching for Files and Folders**  Using the &#x60;name&#x60; parameter triggers search mode, which will search the entire directory structure under the provided &#x60;resource&#x60; for files or folders with names matching the provided &#x60;name&#x60;. This supports wildcard matching such as:  - \\*Report\\* would find any files or folders with \&quot;Report\&quot; in the name. - Data\\_202?-09-30.xlsx would match items such as \&quot;Data\\_2020-09-30.xlsx\&quot;, \&quot;DATA\\_2021-09-30.xlsx\&quot;, \&quot;data\\_2022-09-30.xlsx\&quot; etc. - sales\\* would find any files or folders starting with the word \&quot;Sales\&quot; - \\*.csv would locate any files ending in \&quot;.csv\&quot; - \\* matches everything within the directory tree starting at your given &#x60;resource&#x60;  The search is not case-sensitive. Searching for Clients\\* or clients\\* or CLIENTS\\*, etc. will provide identical results  If you are using the &#x60;name&#x60; parameter to run a search, the &#x60;type&#x60; parameter will be ignored by the server.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://accountname.exavault.com/api/v2");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    String evApiKey = "evApiKey_example"; // String | API Key required to make the API call.
    String evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
    String resource = "resource_example"; // String | Resource identifier to get resources for. Can be path/id/name.
    String sort = "name"; // String | Endpoint support multiple sort fields by allowing array of sort params. Sort fields should be applied in the order specified. The sort order for each sort field is ascending unless it is prefixed with a minus (“-“), in which case it will be descending.
    Integer offset = 0; // Integer | Determines which item to start on for pagination. Use zero (0) to start at the beginning of the list. e.g, setting `offset=200` would trigger the server to skip the first 200 matching entries when returning the results.
    Integer limit = 56; // Integer | The number of files to limit the result. If you have more files in your directory than this limit, make multiple calls, incrementing the `offset` parameter, above.
    String type = "type_example"; // String | Limit types of resources returned to \"file\" or \"dir\" only. This is ignored if you are using the `name` parameter to trigger a search.
    String name = "name_example"; // String | Text to match resource names. This allows you to filter the results returned. For example, to locate only zip archive files, you can enter `*zip` and only resources ending in \"zip\" will be included in the list of results.
    String include = "include_example"; // String | Comma separated list of relationships to include in response. Possible values are **share**, **notifications**, **directFile**, **parentResource**, **ownerUser**, **ownerAccount**.
    try {
      ResourceCollectionResponse result = apiInstance.listResources(evApiKey, evAccessToken, resource, sort, offset, limit, type, name, include);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#listResources");
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
| **evApiKey** | **String**| API Key required to make the API call. | |
| **evAccessToken** | **String**| Access token required to make the API call. | |
| **resource** | **String**| Resource identifier to get resources for. Can be path/id/name. | |
| **sort** | **String**| Endpoint support multiple sort fields by allowing array of sort params. Sort fields should be applied in the order specified. The sort order for each sort field is ascending unless it is prefixed with a minus (“-“), in which case it will be descending. | [optional] |
| **offset** | **Integer**| Determines which item to start on for pagination. Use zero (0) to start at the beginning of the list. e.g, setting &#x60;offset&#x3D;200&#x60; would trigger the server to skip the first 200 matching entries when returning the results. | [optional] [default to 0] |
| **limit** | **Integer**| The number of files to limit the result. If you have more files in your directory than this limit, make multiple calls, incrementing the &#x60;offset&#x60; parameter, above. | [optional] |
| **type** | **String**| Limit types of resources returned to \&quot;file\&quot; or \&quot;dir\&quot; only. This is ignored if you are using the &#x60;name&#x60; parameter to trigger a search. | [optional] |
| **name** | **String**| Text to match resource names. This allows you to filter the results returned. For example, to locate only zip archive files, you can enter &#x60;*zip&#x60; and only resources ending in \&quot;zip\&quot; will be included in the list of results. | [optional] |
| **include** | **String**| Comma separated list of relationships to include in response. Possible values are **share**, **notifications**, **directFile**, **parentResource**, **ownerUser**, **ownerAccount**. | [optional] |

### Return type

[**ResourceCollectionResponse**](ResourceCollectionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Operation |  -  |

<a id="moveResources"></a>
# **moveResources**
> ResourceCopyMove moveResources(evApiKey, evAccessToken, moveResourcesRequestBody)

Move resources

Moves a set of exisiting files/folders (provided by an array &#x60;resources&#x60;) to the requested &#x60;parentResource&#x60; in your account. In the &#x60;resources&#x60; array, you may specify paths pointing files/folders throughout the account, but everything will be moved to the root of the &#x60;parentResource&#x60;.  **Notes:** - Authenticated user should have modify permission. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://accountname.exavault.com/api/v2");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    String evApiKey = "evApiKey_example"; // String | API Key required to make the API call.
    String evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
    MoveResourcesRequestBody moveResourcesRequestBody = new MoveResourcesRequestBody(); // MoveResourcesRequestBody | 
    try {
      ResourceCopyMove result = apiInstance.moveResources(evApiKey, evAccessToken, moveResourcesRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#moveResources");
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
| **evApiKey** | **String**| API Key required to make the API call. | |
| **evAccessToken** | **String**| Access token required to make the API call. | |
| **moveResourcesRequestBody** | [**MoveResourcesRequestBody**](MoveResourcesRequestBody.md)|  | [optional] |

### Return type

[**ResourceCopyMove**](ResourceCopyMove.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Operation |  -  |
| **207** | Multi Response |  -  |

<a id="updateResourceById"></a>
# **updateResourceById**
> ResourceResponse updateResourceById(id, evAccessToken, evApiKey, updateResourceByIdRequestBody)

Rename a resource.

Update the specified file or folder resource record&#39;s \&quot;name\&quot; parameter. The resource is identified by the numeric resource ID that is passed in as the last segment of the URI. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://accountname.exavault.com/api/v2");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    Long id = 56L; // Long | ID number of the resource
    String evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
    String evApiKey = "evApiKey_example"; // String | API key required to make the API call.
    UpdateResourceByIdRequestBody updateResourceByIdRequestBody = new UpdateResourceByIdRequestBody(); // UpdateResourceByIdRequestBody | 
    try {
      ResourceResponse result = apiInstance.updateResourceById(id, evAccessToken, evApiKey, updateResourceByIdRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#updateResourceById");
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
| **id** | **Long**| ID number of the resource | |
| **evAccessToken** | **String**| Access token required to make the API call. | |
| **evApiKey** | **String**| API key required to make the API call. | |
| **updateResourceByIdRequestBody** | [**UpdateResourceByIdRequestBody**](UpdateResourceByIdRequestBody.md)|  | [optional] |

### Return type

[**ResourceResponse**](ResourceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="uploadFile"></a>
# **uploadFile**
> ResourceResponse uploadFile(evApiKey, evAccessToken, path, fileSize, offsetBytes, resume, allowOverwrite, _file)

Upload a file

Uploads a file to a specified path, with optional support for resuming a partially uploaded existing file. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://accountname.exavault.com/api/v2");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    String evApiKey = "evApiKey_example"; // String | API Key required to make the API call.
    String evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
    String path = "path_example"; // String | Destination path for the file being uploaded, including the file name.
    Integer fileSize = 2935; // Integer | File size, in bits, of the file being uploaded.
    Integer offsetBytes = 4852; // Integer | Allows a file upload to resume at a certain number of bytes.
    Boolean resume = true; // Boolean | True if upload resume is supported, false if it isn't. 
    Boolean allowOverwrite = false; // Boolean | True if a file with the same name is found in the designated path, should be overwritten. False if different file names should be generated. 
    File _file = new File("/path/to/file"); // File | 
    try {
      ResourceResponse result = apiInstance.uploadFile(evApiKey, evAccessToken, path, fileSize, offsetBytes, resume, allowOverwrite, _file);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#uploadFile");
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
| **evApiKey** | **String**| API Key required to make the API call. | |
| **evAccessToken** | **String**| Access token required to make the API call. | |
| **path** | **String**| Destination path for the file being uploaded, including the file name. | |
| **fileSize** | **Integer**| File size, in bits, of the file being uploaded. | |
| **offsetBytes** | **Integer**| Allows a file upload to resume at a certain number of bytes. | [optional] |
| **resume** | **Boolean**| True if upload resume is supported, false if it isn&#39;t.  | [optional] [default to true] |
| **allowOverwrite** | **Boolean**| True if a file with the same name is found in the designated path, should be overwritten. False if different file names should be generated.  | [optional] [default to false] |
| **_file** | **File**|  | [optional] |

### Return type

[**ResourceResponse**](ResourceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful Operation |  -  |

