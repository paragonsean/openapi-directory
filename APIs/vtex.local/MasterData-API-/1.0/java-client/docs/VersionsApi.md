# VersionsApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getversion**](VersionsApi.md#getversion) | **GET** /api/dataentities/{acronym}/documents/{id}/versions/{versionId} | Get version |
| [**listversions**](VersionsApi.md#listversions) | **GET** /api/dataentities/{acronym}/documents/{id}/versions | List versions |
| [**putversion**](VersionsApi.md#putversion) | **PUT** /api/dataentities/{acronym}/documents/{id}/versions/{versionId} | Put version |


<a id="getversion"></a>
# **getversion**
> Getversion getversion(contentType, accept, acronym, id, versionId)

Get version

Returns the version of a document.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VersionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    VersionsApi apiInstance = new VersionsApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent
    String accept = "application/vnd.vtex.ds.v10+json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
    String acronym = "{{acronym}}"; // String | Two letter word that identifies the data structure
    String id = "{{id}}"; // String | Id of the document
    String versionId = "{{versionId}}"; // String | Id of the version to get
    try {
      Getversion result = apiInstance.getversion(contentType, accept, acronym, id, versionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VersionsApi#getversion");
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
| **contentType** | **String**| Type of the content being sent | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand  | [default to application/vnd.vtex.ds.v10+json] |
| **acronym** | **String**| Two letter word that identifies the data structure | [default to {{acronym}}] |
| **id** | **String**| Id of the document | [default to {{id}}] |
| **versionId** | **String**| Id of the version to get | [default to {{versionId}}] |

### Return type

[**Getversion**](Getversion.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="listversions"></a>
# **listversions**
> List&lt;Listversion&gt; listversions(contentType, accept, acronym, id)

List versions

Allows to list the versions of a document.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VersionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    VersionsApi apiInstance = new VersionsApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent
    String accept = "application/vnd.vtex.ds.v10+json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
    String acronym = "{{acronym}}"; // String | Two letter word that identifies the data structure
    String id = "{{id}}"; // String | Id of the document
    try {
      List<Listversion> result = apiInstance.listversions(contentType, accept, acronym, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VersionsApi#listversions");
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
| **contentType** | **String**| Type of the content being sent | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand  | [default to application/vnd.vtex.ds.v10+json] |
| **acronym** | **String**| Two letter word that identifies the data structure | [default to {{acronym}}] |
| **id** | **String**| Id of the document | [default to {{id}}] |

### Return type

[**List&lt;Listversion&gt;**](Listversion.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="putversion"></a>
# **putversion**
> Putversion putversion(contentType, accept, acronym, id, versionId)

Put version

Updates document with version values.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VersionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    VersionsApi apiInstance = new VersionsApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent
    String accept = "application/vnd.vtex.ds.v10+json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
    String acronym = "{{acronym}}"; // String | Two letter word that identifies the data structure
    String id = "{{id}}"; // String | Id of the document
    String versionId = "{{versionId}}"; // String | Id of the version to update
    try {
      Putversion result = apiInstance.putversion(contentType, accept, acronym, id, versionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VersionsApi#putversion");
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
| **contentType** | **String**| Type of the content being sent | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand  | [default to application/vnd.vtex.ds.v10+json] |
| **acronym** | **String**| Two letter word that identifies the data structure | [default to {{acronym}}] |
| **id** | **String**| Id of the document | [default to {{id}}] |
| **versionId** | **String**| Id of the version to update | [default to {{versionId}}] |

### Return type

[**Putversion**](Putversion.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

