# StackScriptsApi

All URIs are relative to *https://api.linode.com/v4*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addStackScript**](StackScriptsApi.md#addStackScript) | **POST** /linode/stackscripts | StackScript Create |
| [**deleteStackScript**](StackScriptsApi.md#deleteStackScript) | **DELETE** /linode/stackscripts/{stackscriptId} | StackScript Delete |
| [**getStackScript**](StackScriptsApi.md#getStackScript) | **GET** /linode/stackscripts/{stackscriptId} | StackScript View |
| [**getStackScripts**](StackScriptsApi.md#getStackScripts) | **GET** /linode/stackscripts | StackScripts List |
| [**updateStackScript**](StackScriptsApi.md#updateStackScript) | **PUT** /linode/stackscripts/{stackscriptId} | StackScript Update |


<a id="addStackScript"></a>
# **addStackScript**
> StackScript addStackScript(stackScript)

StackScript Create

Creates a StackScript in your Account. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StackScriptsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    StackScriptsApi apiInstance = new StackScriptsApi(defaultClient);
    StackScript stackScript = new StackScript(); // StackScript | The properties to set for the new StackScript.
    try {
      StackScript result = apiInstance.addStackScript(stackScript);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StackScriptsApi#addStackScript");
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
| **stackScript** | [**StackScript**](StackScript.md)| The properties to set for the new StackScript. | |

### Return type

[**StackScript**](StackScript.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | StackScript successfully created. |  -  |
| **0** | Error |  -  |

<a id="deleteStackScript"></a>
# **deleteStackScript**
> Object deleteStackScript(stackscriptId)

StackScript Delete

Deletes a private StackScript you have permission to &#x60;read_write&#x60;. You cannot delete a public StackScript. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StackScriptsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    StackScriptsApi apiInstance = new StackScriptsApi(defaultClient);
    String stackscriptId = "stackscriptId_example"; // String | The ID of the StackScript to look up.
    try {
      Object result = apiInstance.deleteStackScript(stackscriptId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StackScriptsApi#deleteStackScript");
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
| **stackscriptId** | **String**| The ID of the StackScript to look up. | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | StackScript was deleted. |  -  |
| **0** | Error |  -  |

<a id="getStackScript"></a>
# **getStackScript**
> StackScript getStackScript(stackscriptId)

StackScript View

Returns all of the information about a specified StackScript, including the contents of the script. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StackScriptsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    StackScriptsApi apiInstance = new StackScriptsApi(defaultClient);
    String stackscriptId = "stackscriptId_example"; // String | The ID of the StackScript to look up.
    try {
      StackScript result = apiInstance.getStackScript(stackscriptId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StackScriptsApi#getStackScript");
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
| **stackscriptId** | **String**| The ID of the StackScript to look up. | |

### Return type

[**StackScript**](StackScript.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A single StackScript. |  -  |
| **0** | Error |  -  |

<a id="getStackScripts"></a>
# **getStackScripts**
> GetStackScripts200Response getStackScripts(page, pageSize)

StackScripts List

If the request is not authenticated, only public StackScripts are returned.  For more information on StackScripts, please read our [StackScripts documentation](/docs/products/tools/stackscripts/). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StackScriptsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    StackScriptsApi apiInstance = new StackScriptsApi(defaultClient);
    Integer page = 1; // Integer | The page of a collection to return.
    Integer pageSize = 100; // Integer | The number of items to return per page.
    try {
      GetStackScripts200Response result = apiInstance.getStackScripts(page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StackScriptsApi#getStackScripts");
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
| **page** | **Integer**| The page of a collection to return. | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of items to return per page. | [optional] [default to 100] |

### Return type

[**GetStackScripts200Response**](GetStackScripts200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of StackScripts available to the User, including private StackScripts owned by the User if the request is authenticated.  |  -  |
| **0** | Error |  -  |

<a id="updateStackScript"></a>
# **updateStackScript**
> StackScript updateStackScript(stackscriptId, stackScript)

StackScript Update

Updates a StackScript.  **Once a StackScript is made public, it cannot be made private.** 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StackScriptsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    StackScriptsApi apiInstance = new StackScriptsApi(defaultClient);
    String stackscriptId = "stackscriptId_example"; // String | The ID of the StackScript to look up.
    StackScript stackScript = new StackScript(); // StackScript | The fields to update.
    try {
      StackScript result = apiInstance.updateStackScript(stackscriptId, stackScript);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StackScriptsApi#updateStackScript");
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
| **stackscriptId** | **String**| The ID of the StackScript to look up. | |
| **stackScript** | [**StackScript**](StackScript.md)| The fields to update. | [optional] |

### Return type

[**StackScript**](StackScript.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | StackScript was successfully modified. |  -  |
| **0** | Error |  -  |

