# GlossaryApi

All URIs are relative to *https://api.motaword.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createGlossary**](GlossaryApi.md#createGlossary) | **POST** /projects/{projectId}/glossaries | Upload a glossary file |
| [**deleteGlossary**](GlossaryApi.md#deleteGlossary) | **DELETE** /projects/{projectId}/glossaries/{glossaryId} | Delete a glossary |
| [**downloadGlobalGlossary**](GlossaryApi.md#downloadGlobalGlossary) | **GET** /glossary | Download account glossary. |
| [**downloadGlossary**](GlossaryApi.md#downloadGlossary) | **GET** /projects/{projectId}/glossaries/{glossaryId}/download | Download a glossary |
| [**getGlossaries**](GlossaryApi.md#getGlossaries) | **GET** /projects/{projectId}/glossaries | View glossaries |
| [**getGlossary**](GlossaryApi.md#getGlossary) | **GET** /projects/{projectId}/glossaries/{glossaryId} | View a glossary |
| [**updateGlobalGlossary**](GlossaryApi.md#updateGlobalGlossary) | **POST** /glossary | Create or update the account glossary |
| [**updateGlossary**](GlossaryApi.md#updateGlossary) | **PUT** /projects/{projectId}/glossaries/{glossaryId} | Update a glossary |


<a id="createGlossary"></a>
# **createGlossary**
> Glossary createGlossary(projectId, glossaryUploadRequest)

Upload a glossary file

Upload a new glossary file to your project to be used during translation. Glossaries can be CSV or TBX files.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GlossaryApi;

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

    GlossaryApi apiInstance = new GlossaryApi(defaultClient);
    Long projectId = 74L; // Long | Project ID
    GlossaryUploadRequest glossaryUploadRequest = new GlossaryUploadRequest(); // GlossaryUploadRequest | 
    try {
      Glossary result = apiInstance.createGlossary(projectId, glossaryUploadRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GlossaryApi#createGlossary");
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
| **glossaryUploadRequest** | [**GlossaryUploadRequest**](GlossaryUploadRequest.md)|  | [optional] |

### Return type

[**Glossary**](Glossary.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Newly created glossary model. |  -  |
| **400** | FileTooLarge |  -  |
| **404** | ProjectNotFound |  -  |
| **405** | UnsupportedGlossaryFormat |  -  |
| **406** | ProjectAlreadyHasGlossary |  -  |
| **409** | ProjectAlreadyStarted |  -  |

<a id="deleteGlossary"></a>
# **deleteGlossary**
> OperationStatus deleteGlossary(projectId, glossaryId)

Delete a glossary

Delete the existing glossary from the project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GlossaryApi;

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

    GlossaryApi apiInstance = new GlossaryApi(defaultClient);
    Long projectId = 74L; // Long | Project ID
    Long glossaryId = 1411L; // Long | Glossary ID
    try {
      OperationStatus result = apiInstance.deleteGlossary(projectId, glossaryId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GlossaryApi#deleteGlossary");
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
| **glossaryId** | **Long**| Glossary ID | |

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
| **200** | Glossary deleted successfully |  -  |
| **404** | GlossaryNotFound |  -  |
| **409** | ProjectAlreadyStarted |  -  |

<a id="downloadGlobalGlossary"></a>
# **downloadGlobalGlossary**
> String downloadGlobalGlossary()

Download account glossary.

Download your corporate account&#39;s global glossary. This endpoint is available only for corporate account customers. This glossary will be automatically attached to each new project under your account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GlossaryApi;

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

    GlossaryApi apiInstance = new GlossaryApi(defaultClient);
    try {
      String result = apiInstance.downloadGlobalGlossary();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GlossaryApi#downloadGlobalGlossary");
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
| **200** | Glossary file streamed. |  -  |
| **404** | GlossaryNotFound |  -  |

<a id="downloadGlossary"></a>
# **downloadGlossary**
> String downloadGlossary(projectId, glossaryId)

Download a glossary

Download a previously uploaded glossary file.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GlossaryApi;

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

    GlossaryApi apiInstance = new GlossaryApi(defaultClient);
    Long projectId = 74L; // Long | Project ID
    Long glossaryId = 1411L; // Long | Glossary ID
    try {
      String result = apiInstance.downloadGlossary(projectId, glossaryId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GlossaryApi#downloadGlossary");
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
| **glossaryId** | **Long**| Glossary ID | |

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
| **200** | Glossary streamed |  -  |
| **404** | GlossaryNotFound |  -  |

<a id="getGlossaries"></a>
# **getGlossaries**
> GlossaryList getGlossaries(projectId)

View glossaries

View a list of glossaries previously uploaded to the project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GlossaryApi;

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

    GlossaryApi apiInstance = new GlossaryApi(defaultClient);
    Long projectId = 74L; // Long | Project ID
    try {
      GlossaryList result = apiInstance.getGlossaries(projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GlossaryApi#getGlossaries");
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

### Return type

[**GlossaryList**](GlossaryList.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of glossary models |  -  |
| **404** | ProjectNotFound |  -  |

<a id="getGlossary"></a>
# **getGlossary**
> Glossary getGlossary(projectId, glossaryId)

View a glossary

View the details of a glossary file uploaded to a project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GlossaryApi;

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

    GlossaryApi apiInstance = new GlossaryApi(defaultClient);
    Long projectId = 74L; // Long | Project ID
    Long glossaryId = 1411L; // Long | Glossary ID
    try {
      Glossary result = apiInstance.getGlossary(projectId, glossaryId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GlossaryApi#getGlossary");
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
| **glossaryId** | **Long**| Glossary ID | |

### Return type

[**Glossary**](Glossary.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Glossary model |  -  |
| **404** | GlossaryNotFound |  -  |

<a id="updateGlobalGlossary"></a>
# **updateGlobalGlossary**
> OperationStatus updateGlobalGlossary(accountGlossaryUploadRequest)

Create or update the account glossary

Update your corporate account&#39;s global glossary. This endpoint is available only for corporate account customers. This glossary will be automatically attached to each new project under your account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GlossaryApi;

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

    GlossaryApi apiInstance = new GlossaryApi(defaultClient);
    AccountGlossaryUploadRequest accountGlossaryUploadRequest = new AccountGlossaryUploadRequest(); // AccountGlossaryUploadRequest | 
    try {
      OperationStatus result = apiInstance.updateGlobalGlossary(accountGlossaryUploadRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GlossaryApi#updateGlobalGlossary");
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
| **accountGlossaryUploadRequest** | [**AccountGlossaryUploadRequest**](AccountGlossaryUploadRequest.md)|  | [optional] |

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
| **400** | FileTooLarge FileTooSmall NoFileUploaded |  -  |
| **405** | UnsupportedGlossaryFormat |  -  |

<a id="updateGlossary"></a>
# **updateGlossary**
> Glossary updateGlossary(projectId, glossaryId, glossaryUploadRequest)

Update a glossary

Update the existing glossary file in the project. Public users are allowed to have only 1 glossary per project and file name and contents will replaced with the new glossary file that you are uploading via this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GlossaryApi;

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

    GlossaryApi apiInstance = new GlossaryApi(defaultClient);
    Long projectId = 74L; // Long | Project ID
    Long glossaryId = 1411L; // Long | Glossary ID
    GlossaryUploadRequest glossaryUploadRequest = new GlossaryUploadRequest(); // GlossaryUploadRequest | 
    try {
      Glossary result = apiInstance.updateGlossary(projectId, glossaryId, glossaryUploadRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GlossaryApi#updateGlossary");
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
| **glossaryId** | **Long**| Glossary ID | |
| **glossaryUploadRequest** | [**GlossaryUploadRequest**](GlossaryUploadRequest.md)|  | [optional] |

### Return type

[**Glossary**](Glossary.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated glossary model |  -  |
| **400** | FileTooLarge |  -  |
| **404** | GlossaryNotFound |  -  |
| **405** | UnsupportedGlossaryFormat |  -  |
| **409** | ProjectAlreadyStarted |  -  |

