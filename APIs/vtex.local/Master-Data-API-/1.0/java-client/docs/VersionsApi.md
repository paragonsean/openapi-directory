# VersionsApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getversion**](VersionsApi.md#getversion) | **GET** /api/dataentities/{dataEntityName}/documents/{id}/versions/{versionId} | Get version |
| [**listversions**](VersionsApi.md#listversions) | **GET** /api/dataentities/{dataEntityName}/documents/{id}/versions | List versions |
| [**putversion**](VersionsApi.md#putversion) | **PUT** /api/dataentities/{dataEntityName}/documents/{id}/versions/{versionId} | Put version |


<a id="getversion"></a>
# **getversion**
> Getversion getversion(dataEntityName, contentType, accept, id, versionId)

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
    String dataEntityName = "Client"; // String | Name of the data entity. Defined by the api. Examples of native data entities you can use are `CL` for client profiles and `AD` for client addresses.
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String id = "Client-b818cbda-e489-11e6-94f4-0ac138d2d42e"; // String | ID of the Document.
    String versionId = "123456789abc"; // String | ID of the version to update.
    try {
      Getversion result = apiInstance.getversion(dataEntityName, contentType, accept, id, versionId);
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
| **dataEntityName** | **String**| Name of the data entity. Defined by the api. Examples of native data entities you can use are &#x60;CL&#x60; for client profiles and &#x60;AD&#x60; for client addresses. | |
| **contentType** | **String**| Type of the content being sent. | |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | |
| **id** | **String**| ID of the Document. | |
| **versionId** | **String**| ID of the version to update. | [default to 123456789abc] |

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
| **200** | OK |  -  |

<a id="listversions"></a>
# **listversions**
> List&lt;Listversion&gt; listversions(dataEntityName, contentType, accept, id, load, fields)

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
    String dataEntityName = "Client"; // String | Name of the data entity. Defined by the api. Examples of native data entities you can use are `CL` for client profiles and `AD` for client addresses.
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String id = "Client-b818cbda-e489-11e6-94f4-0ac138d2d42e"; // String | ID of the Document.
    Boolean load = true; // Boolean | If true, return all the fields in each version of the document
    String fields = "id,dataEntityId,isNewsletterOptIn,createdBy"; // String | If `load` is true, the response will return only these specific fields
    try {
      List<Listversion> result = apiInstance.listversions(dataEntityName, contentType, accept, id, load, fields);
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
| **dataEntityName** | **String**| Name of the data entity. Defined by the api. Examples of native data entities you can use are &#x60;CL&#x60; for client profiles and &#x60;AD&#x60; for client addresses. | |
| **contentType** | **String**| Type of the content being sent. | |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | |
| **id** | **String**| ID of the Document. | |
| **load** | **Boolean**| If true, return all the fields in each version of the document | [optional] [default to true] |
| **fields** | **String**| If &#x60;load&#x60; is true, the response will return only these specific fields | [optional] [default to id,dataEntityId,isNewsletterOptIn,createdBy] |

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
| **200** | OK |  -  |

<a id="putversion"></a>
# **putversion**
> DocumentResponse putversion(dataEntityName, contentType, accept, id, versionId)

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
    String dataEntityName = "Client"; // String | Name of the data entity. Defined by the api. Examples of native data entities you can use are `CL` for client profiles and `AD` for client addresses.
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String id = "Client-b818cbda-e489-11e6-94f4-0ac138d2d42e"; // String | ID of the Document.
    String versionId = "{{versionId}}"; // String | ID of the version to update
    try {
      DocumentResponse result = apiInstance.putversion(dataEntityName, contentType, accept, id, versionId);
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
| **dataEntityName** | **String**| Name of the data entity. Defined by the api. Examples of native data entities you can use are &#x60;CL&#x60; for client profiles and &#x60;AD&#x60; for client addresses. | |
| **contentType** | **String**| Type of the content being sent. | |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | |
| **id** | **String**| ID of the Document. | |
| **versionId** | **String**| ID of the version to update | [default to {{versionId}}] |

### Return type

[**DocumentResponse**](DocumentResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

