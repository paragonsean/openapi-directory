# AuthorApi

All URIs are relative to *http://etherpad.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createAuthorIfNotExistsForUsingGET**](AuthorApi.md#createAuthorIfNotExistsForUsingGET) | **GET** /createAuthorIfNotExistsFor | this functions helps you to map your application author ids to Etherpad author ids |
| [**createAuthorIfNotExistsForUsingPOST**](AuthorApi.md#createAuthorIfNotExistsForUsingPOST) | **POST** /createAuthorIfNotExistsFor | this functions helps you to map your application author ids to Etherpad author ids |
| [**createAuthorUsingGET**](AuthorApi.md#createAuthorUsingGET) | **GET** /createAuthor | creates a new author |
| [**createAuthorUsingPOST**](AuthorApi.md#createAuthorUsingPOST) | **POST** /createAuthor | creates a new author |
| [**getAuthorNameUsingGET**](AuthorApi.md#getAuthorNameUsingGET) | **GET** /getAuthorName | Returns the Author Name of the author |
| [**getAuthorNameUsingPOST**](AuthorApi.md#getAuthorNameUsingPOST) | **POST** /getAuthorName | Returns the Author Name of the author |
| [**listPadsOfAuthorUsingGET**](AuthorApi.md#listPadsOfAuthorUsingGET) | **GET** /listPadsOfAuthor | returns an array of all pads this author contributed to |
| [**listPadsOfAuthorUsingPOST**](AuthorApi.md#listPadsOfAuthorUsingPOST) | **POST** /listPadsOfAuthor | returns an array of all pads this author contributed to |
| [**listSessionsOfAuthorUsingGET**](AuthorApi.md#listSessionsOfAuthorUsingGET) | **GET** /listSessionsOfAuthor | returns all sessions of an author |
| [**listSessionsOfAuthorUsingPOST**](AuthorApi.md#listSessionsOfAuthorUsingPOST) | **POST** /listSessionsOfAuthor | returns all sessions of an author |


<a id="createAuthorIfNotExistsForUsingGET"></a>
# **createAuthorIfNotExistsForUsingGET**
> CreateAuthorUsingGET200Response createAuthorIfNotExistsForUsingGET(authorMapper, name)

this functions helps you to map your application author ids to Etherpad author ids

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    AuthorApi apiInstance = new AuthorApi(defaultClient);
    String authorMapper = "authorMapper_example"; // String | 
    String name = "name_example"; // String | 
    try {
      CreateAuthorUsingGET200Response result = apiInstance.createAuthorIfNotExistsForUsingGET(authorMapper, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthorApi#createAuthorIfNotExistsForUsingGET");
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
| **authorMapper** | **String**|  | [optional] |
| **name** | **String**|  | [optional] |

### Return type

[**CreateAuthorUsingGET200Response**](CreateAuthorUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ok (code 0) |  -  |
| **400** | generic api error (code 1) |  -  |
| **401** | no or wrong API key (code 4) |  -  |
| **500** | internal api error (code 2) |  -  |

<a id="createAuthorIfNotExistsForUsingPOST"></a>
# **createAuthorIfNotExistsForUsingPOST**
> CreateAuthorUsingGET200Response createAuthorIfNotExistsForUsingPOST(authorMapper, name)

this functions helps you to map your application author ids to Etherpad author ids

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    AuthorApi apiInstance = new AuthorApi(defaultClient);
    String authorMapper = "authorMapper_example"; // String | 
    String name = "name_example"; // String | 
    try {
      CreateAuthorUsingGET200Response result = apiInstance.createAuthorIfNotExistsForUsingPOST(authorMapper, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthorApi#createAuthorIfNotExistsForUsingPOST");
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
| **authorMapper** | **String**|  | [optional] |
| **name** | **String**|  | [optional] |

### Return type

[**CreateAuthorUsingGET200Response**](CreateAuthorUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ok (code 0) |  -  |
| **400** | generic api error (code 1) |  -  |
| **401** | no or wrong API key (code 4) |  -  |
| **500** | internal api error (code 2) |  -  |

<a id="createAuthorUsingGET"></a>
# **createAuthorUsingGET**
> CreateAuthorUsingGET200Response createAuthorUsingGET(name)

creates a new author

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    AuthorApi apiInstance = new AuthorApi(defaultClient);
    String name = "name_example"; // String | 
    try {
      CreateAuthorUsingGET200Response result = apiInstance.createAuthorUsingGET(name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthorApi#createAuthorUsingGET");
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
| **name** | **String**|  | [optional] |

### Return type

[**CreateAuthorUsingGET200Response**](CreateAuthorUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ok (code 0) |  -  |
| **400** | generic api error (code 1) |  -  |
| **401** | no or wrong API key (code 4) |  -  |
| **500** | internal api error (code 2) |  -  |

<a id="createAuthorUsingPOST"></a>
# **createAuthorUsingPOST**
> CreateAuthorUsingGET200Response createAuthorUsingPOST(name)

creates a new author

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    AuthorApi apiInstance = new AuthorApi(defaultClient);
    String name = "name_example"; // String | 
    try {
      CreateAuthorUsingGET200Response result = apiInstance.createAuthorUsingPOST(name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthorApi#createAuthorUsingPOST");
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
| **name** | **String**|  | [optional] |

### Return type

[**CreateAuthorUsingGET200Response**](CreateAuthorUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ok (code 0) |  -  |
| **400** | generic api error (code 1) |  -  |
| **401** | no or wrong API key (code 4) |  -  |
| **500** | internal api error (code 2) |  -  |

<a id="getAuthorNameUsingGET"></a>
# **getAuthorNameUsingGET**
> GetAuthorNameUsingGET200Response getAuthorNameUsingGET(authorID)

Returns the Author Name of the author

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    AuthorApi apiInstance = new AuthorApi(defaultClient);
    String authorID = "authorID_example"; // String | 
    try {
      GetAuthorNameUsingGET200Response result = apiInstance.getAuthorNameUsingGET(authorID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthorApi#getAuthorNameUsingGET");
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
| **authorID** | **String**|  | [optional] |

### Return type

[**GetAuthorNameUsingGET200Response**](GetAuthorNameUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ok (code 0) |  -  |
| **400** | generic api error (code 1) |  -  |
| **401** | no or wrong API key (code 4) |  -  |
| **500** | internal api error (code 2) |  -  |

<a id="getAuthorNameUsingPOST"></a>
# **getAuthorNameUsingPOST**
> GetAuthorNameUsingGET200Response getAuthorNameUsingPOST(authorID)

Returns the Author Name of the author

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    AuthorApi apiInstance = new AuthorApi(defaultClient);
    String authorID = "authorID_example"; // String | 
    try {
      GetAuthorNameUsingGET200Response result = apiInstance.getAuthorNameUsingPOST(authorID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthorApi#getAuthorNameUsingPOST");
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
| **authorID** | **String**|  | [optional] |

### Return type

[**GetAuthorNameUsingGET200Response**](GetAuthorNameUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ok (code 0) |  -  |
| **400** | generic api error (code 1) |  -  |
| **401** | no or wrong API key (code 4) |  -  |
| **500** | internal api error (code 2) |  -  |

<a id="listPadsOfAuthorUsingGET"></a>
# **listPadsOfAuthorUsingGET**
> ListAllPadsUsingGET200Response listPadsOfAuthorUsingGET(authorID)

returns an array of all pads this author contributed to

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    AuthorApi apiInstance = new AuthorApi(defaultClient);
    String authorID = "authorID_example"; // String | 
    try {
      ListAllPadsUsingGET200Response result = apiInstance.listPadsOfAuthorUsingGET(authorID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthorApi#listPadsOfAuthorUsingGET");
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
| **authorID** | **String**|  | [optional] |

### Return type

[**ListAllPadsUsingGET200Response**](ListAllPadsUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ok (code 0) |  -  |
| **400** | generic api error (code 1) |  -  |
| **401** | no or wrong API key (code 4) |  -  |
| **500** | internal api error (code 2) |  -  |

<a id="listPadsOfAuthorUsingPOST"></a>
# **listPadsOfAuthorUsingPOST**
> ListAllPadsUsingGET200Response listPadsOfAuthorUsingPOST(authorID)

returns an array of all pads this author contributed to

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    AuthorApi apiInstance = new AuthorApi(defaultClient);
    String authorID = "authorID_example"; // String | 
    try {
      ListAllPadsUsingGET200Response result = apiInstance.listPadsOfAuthorUsingPOST(authorID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthorApi#listPadsOfAuthorUsingPOST");
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
| **authorID** | **String**|  | [optional] |

### Return type

[**ListAllPadsUsingGET200Response**](ListAllPadsUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ok (code 0) |  -  |
| **400** | generic api error (code 1) |  -  |
| **401** | no or wrong API key (code 4) |  -  |
| **500** | internal api error (code 2) |  -  |

<a id="listSessionsOfAuthorUsingGET"></a>
# **listSessionsOfAuthorUsingGET**
> ListSessionsOfAuthorUsingGET200Response listSessionsOfAuthorUsingGET(authorID)

returns all sessions of an author

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    AuthorApi apiInstance = new AuthorApi(defaultClient);
    String authorID = "authorID_example"; // String | 
    try {
      ListSessionsOfAuthorUsingGET200Response result = apiInstance.listSessionsOfAuthorUsingGET(authorID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthorApi#listSessionsOfAuthorUsingGET");
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
| **authorID** | **String**|  | [optional] |

### Return type

[**ListSessionsOfAuthorUsingGET200Response**](ListSessionsOfAuthorUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ok (code 0) |  -  |
| **400** | generic api error (code 1) |  -  |
| **401** | no or wrong API key (code 4) |  -  |
| **500** | internal api error (code 2) |  -  |

<a id="listSessionsOfAuthorUsingPOST"></a>
# **listSessionsOfAuthorUsingPOST**
> ListSessionsOfAuthorUsingGET200Response listSessionsOfAuthorUsingPOST(authorID)

returns all sessions of an author

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    AuthorApi apiInstance = new AuthorApi(defaultClient);
    String authorID = "authorID_example"; // String | 
    try {
      ListSessionsOfAuthorUsingGET200Response result = apiInstance.listSessionsOfAuthorUsingPOST(authorID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthorApi#listSessionsOfAuthorUsingPOST");
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
| **authorID** | **String**|  | [optional] |

### Return type

[**ListSessionsOfAuthorUsingGET200Response**](ListSessionsOfAuthorUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ok (code 0) |  -  |
| **400** | generic api error (code 1) |  -  |
| **401** | no or wrong API key (code 4) |  -  |
| **500** | internal api error (code 2) |  -  |

