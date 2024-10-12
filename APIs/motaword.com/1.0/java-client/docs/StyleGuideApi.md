# StyleGuideApi

All URIs are relative to *https://api.motaword.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createStyleGuide**](StyleGuideApi.md#createStyleGuide) | **POST** /projects/{projectId}/styleguides | Upload a new style guide |
| [**deleteStyleGuide**](StyleGuideApi.md#deleteStyleGuide) | **DELETE** /projects/{projectId}/styleguides/{styleGuideId} | Delete a style guide |
| [**downloadGlobalStyleGuide**](StyleGuideApi.md#downloadGlobalStyleGuide) | **GET** /styleguide | Download account style guide |
| [**downloadStyleGuide**](StyleGuideApi.md#downloadStyleGuide) | **GET** /projects/{projectId}/styleguides/{styleGuideId}/download | Download a style guide |
| [**getStyleGuide**](StyleGuideApi.md#getStyleGuide) | **GET** /projects/{projectId}/styleguides/{styleGuideId} | View a style guide |
| [**getStyleGuides**](StyleGuideApi.md#getStyleGuides) | **GET** /projects/{projectId}/styleguides | View style guides |
| [**updateGlobalStyleGuide**](StyleGuideApi.md#updateGlobalStyleGuide) | **POST** /styleguide | Create or update the account style guide |
| [**updateStyleGuide**](StyleGuideApi.md#updateStyleGuide) | **PUT** /projects/{projectId}/styleguides/{styleGuideId} | Update a style guide |


<a id="createStyleGuide"></a>
# **createStyleGuide**
> StyleGuideList createStyleGuide(projectId, styleGuideUploadRequest)

Upload a new style guide

Upload a new style guide

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StyleGuideApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    StyleGuideApi apiInstance = new StyleGuideApi(defaultClient);
    Long projectId = 74L; // Long | Project ID
    StyleGuideUploadRequest styleGuideUploadRequest = new StyleGuideUploadRequest(); // StyleGuideUploadRequest | 
    try {
      StyleGuideList result = apiInstance.createStyleGuide(projectId, styleGuideUploadRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StyleGuideApi#createStyleGuide");
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
| **projectId** | **Long**| Project ID | |
| **styleGuideUploadRequest** | [**StyleGuideUploadRequest**](StyleGuideUploadRequest.md)|  | [optional] |

### Return type

[**StyleGuideList**](StyleGuideList.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Newly created style guide model or a list of new style guide models |  -  |
| **400** | FileTooLarge |  -  |
| **404** | ProjectNotFound |  -  |
| **405** | UnsupportedStyleGuideFormat |  -  |
| **409** | ProjectAlreadyStarted |  -  |

<a id="deleteStyleGuide"></a>
# **deleteStyleGuide**
> OperationStatus deleteStyleGuide(projectId, styleGuideId)

Delete a style guide

Delete the existing style guide from the project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StyleGuideApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    StyleGuideApi apiInstance = new StyleGuideApi(defaultClient);
    Long projectId = 74L; // Long | Project ID
    Long styleGuideId = 13959L; // Long | Style Guide ID
    try {
      OperationStatus result = apiInstance.deleteStyleGuide(projectId, styleGuideId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StyleGuideApi#deleteStyleGuide");
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
| **projectId** | **Long**| Project ID | |
| **styleGuideId** | **Long**| Style Guide ID | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Style guide deleted successfully |  -  |
| **404** | StyleGuideNotFound |  -  |
| **409** | ProjectAlreadyStarted |  -  |

<a id="downloadGlobalStyleGuide"></a>
# **downloadGlobalStyleGuide**
> String downloadGlobalStyleGuide()

Download account style guide

Download your account&#39;s global style guide. This endpoint is available only for corporate account customers. This style guide will be automatically attached to each new project under your account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StyleGuideApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    StyleGuideApi apiInstance = new StyleGuideApi(defaultClient);
    try {
      String result = apiInstance.downloadGlobalStyleGuide();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StyleGuideApi#downloadGlobalStyleGuide");
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

**String**

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Style guide file streamed. |  -  |
| **404** | StyleGuideNotFound |  -  |

<a id="downloadStyleGuide"></a>
# **downloadStyleGuide**
> String downloadStyleGuide(projectId, styleGuideId)

Download a style guide

Download a previously uploaded style guide file.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StyleGuideApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    StyleGuideApi apiInstance = new StyleGuideApi(defaultClient);
    Long projectId = 74L; // Long | Project ID
    Long styleGuideId = 13959L; // Long | Style Guide ID
    try {
      String result = apiInstance.downloadStyleGuide(projectId, styleGuideId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StyleGuideApi#downloadStyleGuide");
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
| **projectId** | **Long**| Project ID | |
| **styleGuideId** | **Long**| Style Guide ID | |

### Return type

**String**

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Style guide streamed |  -  |
| **404** | StyleGuideNotFound |  -  |

<a id="getStyleGuide"></a>
# **getStyleGuide**
> StyleGuide getStyleGuide(projectId, styleGuideId, with)

View a style guide

View the details of a style guide uploaded to a project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StyleGuideApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    StyleGuideApi apiInstance = new StyleGuideApi(defaultClient);
    Long projectId = 74L; // Long | Project ID
    Long styleGuideId = 13959L; // Long | Style Guide ID
    List<String> with = Arrays.asList(); // List<String> | Attach further information. Possible values 'preview' to fetch temporary preview URLs. This is NOT recommended to be used with list calls. Only use with[]=preview for single document/style guide calls.
    try {
      StyleGuide result = apiInstance.getStyleGuide(projectId, styleGuideId, with);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StyleGuideApi#getStyleGuide");
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
| **projectId** | **Long**| Project ID | |
| **styleGuideId** | **Long**| Style Guide ID | |
| **with** | [**List&lt;String&gt;**](String.md)| Attach further information. Possible values &#39;preview&#39; to fetch temporary preview URLs. This is NOT recommended to be used with list calls. Only use with[]&#x3D;preview for single document/style guide calls. | [optional] [enum: preview] |

### Return type

[**StyleGuide**](StyleGuide.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Style guide model |  -  |
| **404** | StyleGuideNotFound |  -  |

<a id="getStyleGuides"></a>
# **getStyleGuides**
> StyleGuideList getStyleGuides(projectId, with)

View style guides

View a list of style guides in your project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StyleGuideApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    StyleGuideApi apiInstance = new StyleGuideApi(defaultClient);
    Long projectId = 74L; // Long | Project ID
    List<String> with = Arrays.asList(); // List<String> | Attach further information. Possible values 'preview' to fetch temporary preview URLs. This is NOT recommended to be used with list calls. Only use with[]=preview for single document/style guide calls.
    try {
      StyleGuideList result = apiInstance.getStyleGuides(projectId, with);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StyleGuideApi#getStyleGuides");
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
| **projectId** | **Long**| Project ID | |
| **with** | [**List&lt;String&gt;**](String.md)| Attach further information. Possible values &#39;preview&#39; to fetch temporary preview URLs. This is NOT recommended to be used with list calls. Only use with[]&#x3D;preview for single document/style guide calls. | [optional] [enum: preview] |

### Return type

[**StyleGuideList**](StyleGuideList.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of style guide models |  -  |
| **404** | ProjectNotFound |  -  |

<a id="updateGlobalStyleGuide"></a>
# **updateGlobalStyleGuide**
> OperationStatus updateGlobalStyleGuide(accountStyleGuideUploadRequest)

Create or update the account style guide

Update your corporate account&#39;s global style guide. This endpoint is available only for corporate account customers. This style guide will be automatically attached to each new project under your account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StyleGuideApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    StyleGuideApi apiInstance = new StyleGuideApi(defaultClient);
    AccountStyleGuideUploadRequest accountStyleGuideUploadRequest = new AccountStyleGuideUploadRequest(); // AccountStyleGuideUploadRequest | 
    try {
      OperationStatus result = apiInstance.updateGlobalStyleGuide(accountStyleGuideUploadRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StyleGuideApi#updateGlobalStyleGuide");
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
| **accountStyleGuideUploadRequest** | [**AccountStyleGuideUploadRequest**](AccountStyleGuideUploadRequest.md)|  | [optional] |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **400** | FileTooLarge FileTooSmall NoFileUploaded MissingCorporateAccount |  -  |
| **405** | UnsupportedStyleGuideFormat |  -  |

<a id="updateStyleGuide"></a>
# **updateStyleGuide**
> StyleGuide updateStyleGuide(projectId, styleGuideId, styleGuideUploadRequest)

Update a style guide

Update the existing style guide in the project. Public users are allowed to have only 1 style guide per project and file name and contents will replaced with the new style guide that you are uploading via this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StyleGuideApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    StyleGuideApi apiInstance = new StyleGuideApi(defaultClient);
    Long projectId = 74L; // Long | Project ID
    Long styleGuideId = 13959L; // Long | Style guide ID
    StyleGuideUploadRequest styleGuideUploadRequest = new StyleGuideUploadRequest(); // StyleGuideUploadRequest | 
    try {
      StyleGuide result = apiInstance.updateStyleGuide(projectId, styleGuideId, styleGuideUploadRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StyleGuideApi#updateStyleGuide");
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
| **projectId** | **Long**| Project ID | |
| **styleGuideId** | **Long**| Style guide ID | |
| **styleGuideUploadRequest** | [**StyleGuideUploadRequest**](StyleGuideUploadRequest.md)|  | [optional] |

### Return type

[**StyleGuide**](StyleGuide.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated style guide model |  -  |
| **400** | FileTooLarge |  -  |
| **404** | StyleGuideNotFound |  -  |
| **405** | UnsupportedStyleGuideFormat |  -  |
| **409** | ProjectAlreadyStarted |  -  |

