# ApplicationsApiApi

All URIs are relative to *http://meshery.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**idDeleteApplicationFile**](ApplicationsApiApi.md#idDeleteApplicationFile) | **DELETE** /api/application/deploy | Handle DELETE request for Application File Deploy |
| [**idDeleteMesheryApplicationFile**](ApplicationsApiApi.md#idDeleteMesheryApplicationFile) | **DELETE** /api/application/{id} | Handle Delete for a Meshery Application File |
| [**idGetApplicationFileRequest**](ApplicationsApiApi.md#idGetApplicationFileRequest) | **GET** /api/application/ | Handle GET request for Application Files |
| [**idGetMesheryApplication**](ApplicationsApiApi.md#idGetMesheryApplication) | **GET** /api/application/{id} | Handle GET request for Meshery Application with the given id |
| [**idPostApplicationFileRequest**](ApplicationsApiApi.md#idPostApplicationFileRequest) | **POST** /api/application/ | Handle POST request for Application Files |
| [**idPostDeployApplicationFile**](ApplicationsApiApi.md#idPostDeployApplicationFile) | **POST** /api/application/deploy | Handle POST request for Application File Deploy |


<a id="idDeleteApplicationFile"></a>
# **idDeleteApplicationFile**
> idDeleteApplicationFile()

Handle DELETE request for Application File Deploy

Delete a deployed application file with the request

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    ApplicationsApiApi apiInstance = new ApplicationsApiApi(defaultClient);
    try {
      apiInstance.idDeleteApplicationFile();
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationsApiApi#idDeleteApplicationFile");
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

null (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="idDeleteMesheryApplicationFile"></a>
# **idDeleteMesheryApplicationFile**
> idDeleteMesheryApplicationFile(id)

Handle Delete for a Meshery Application File

Deletes a meshery application file with ID: id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    ApplicationsApiApi apiInstance = new ApplicationsApiApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | id for a specific
    try {
      apiInstance.idDeleteMesheryApplicationFile(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationsApiApi#idDeleteMesheryApplicationFile");
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
| **id** | **UUID**| id for a specific | |

### Return type

null (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="idGetApplicationFileRequest"></a>
# **idGetApplicationFileRequest**
> ApplicationsAPIResponse idGetApplicationFileRequest()

Handle GET request for Application Files

Returns requests for all Meshery Applications

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    ApplicationsApiApi apiInstance = new ApplicationsApiApi(defaultClient);
    try {
      ApplicationsAPIResponse result = apiInstance.idGetApplicationFileRequest();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationsApiApi#idGetApplicationFileRequest");
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

[**ApplicationsAPIResponse**](ApplicationsAPIResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns all meshery applications |  -  |

<a id="idGetMesheryApplication"></a>
# **idGetMesheryApplication**
> MesheryApplication idGetMesheryApplication(id)

Handle GET request for Meshery Application with the given id

Fetches the list of all applications saved by the current user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    ApplicationsApiApi apiInstance = new ApplicationsApiApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | id for a specific
    try {
      MesheryApplication result = apiInstance.idGetMesheryApplication(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationsApiApi#idGetMesheryApplication");
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
| **id** | **UUID**| id for a specific | |

### Return type

[**MesheryApplication**](MesheryApplication.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Fetches a single Meshery Application |  -  |

<a id="idPostApplicationFileRequest"></a>
# **idPostApplicationFileRequest**
> MesheryApplication idPostApplicationFileRequest()

Handle POST request for Application Files

Save attached Meshery Application File

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    ApplicationsApiApi apiInstance = new ApplicationsApiApi(defaultClient);
    try {
      MesheryApplication result = apiInstance.idPostApplicationFileRequest();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationsApiApi#idPostApplicationFileRequest");
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

[**MesheryApplication**](MesheryApplication.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Fetches a single Meshery Application |  -  |

<a id="idPostDeployApplicationFile"></a>
# **idPostDeployApplicationFile**
> MesheryApplication idPostDeployApplicationFile(uploadYamlYmlFile)

Handle POST request for Application File Deploy

Deploy an attached application file with the request

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    ApplicationsApiApi apiInstance = new ApplicationsApiApi(defaultClient);
    File uploadYamlYmlFile = new File("/path/to/file"); // File | 
    try {
      MesheryApplication result = apiInstance.idPostDeployApplicationFile(uploadYamlYmlFile);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationsApiApi#idPostDeployApplicationFile");
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
| **uploadYamlYmlFile** | **File**|  | [optional] |

### Return type

[**MesheryApplication**](MesheryApplication.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the response of the application files |  -  |

