# AliasApi

All URIs are relative to *https://api.shorten.rest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createAlias**](AliasApi.md#createAlias) | **POST** /aliases | Create alias |
| [**deleteAlias**](AliasApi.md#deleteAlias) | **DELETE** /aliases | Delete alias |
| [**getAlias**](AliasApi.md#getAlias) | **GET** /aliases | Get alias |
| [**getAliases**](AliasApi.md#getAliases) | **GET** /aliases/all | Get aliases by domain |
| [**updateAlias**](AliasApi.md#updateAlias) | **PUT** /aliases | Update alias |


<a id="createAlias"></a>
# **createAlias**
> CreateAliasResponseModel createAlias(createAliasModel, domainName, aliasName)

Create alias

This POST method creates a new alias under a specified domain. If no domain is specified in the request the alias will be attached to the default domain Short.fyi    **NOTE:** You can override the domain level Meta Tags and Tracking Snippets by specifying them for each URL. Any variables you add to a specific URL will always override domain level settings.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AliasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shorten.rest");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    AliasApi apiInstance = new AliasApi(defaultClient);
    CreateAliasModel createAliasModel = new CreateAliasModel(); // CreateAliasModel | alias properties
    String domainName = "short.fyi"; // String | domain which alias will belong to (string without `http/https` or `/`)
    String aliasName = "@rnd"; // String | alias (without `/` at the beginning)
    try {
      CreateAliasResponseModel result = apiInstance.createAlias(createAliasModel, domainName, aliasName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AliasApi#createAlias");
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
| **createAliasModel** | [**CreateAliasModel**](CreateAliasModel.md)| alias properties | |
| **domainName** | **String**| domain which alias will belong to (string without &#x60;http/https&#x60; or &#x60;/&#x60;) | [optional] [default to short.fyi] |
| **aliasName** | **String**| alias (without &#x60;/&#x60; at the beginning) | [optional] [default to @rnd] |

### Return type

[**CreateAliasResponseModel**](CreateAliasResponseModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response contains aliasName, domainName and full generated short link |  -  |

<a id="deleteAlias"></a>
# **deleteAlias**
> deleteAlias(aliasName, domainName)

Delete alias

Deletes a single alias by providing alias and domain. If no domain is provided the API will search for the matching alias within the Short.fyi domain

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AliasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shorten.rest");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    AliasApi apiInstance = new AliasApi(defaultClient);
    String aliasName = "aBcDe012"; // String | alias (without `/` at the beginning)
    String domainName = "short.fyi"; // String | domain which alias belongs to (string without `http/https` or `/`)
    try {
      apiInstance.deleteAlias(aliasName, domainName);
    } catch (ApiException e) {
      System.err.println("Exception when calling AliasApi#deleteAlias");
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
| **aliasName** | **String**| alias (without &#x60;/&#x60; at the beginning) | |
| **domainName** | **String**| domain which alias belongs to (string without &#x60;http/https&#x60; or &#x60;/&#x60;) | [optional] [default to short.fyi] |

### Return type

null (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Empty response |  -  |

<a id="getAlias"></a>
# **getAlias**
> AliasModel getAlias(aliasName, domainName)

Get alias

Get detailed information for a single alias by providing its alias and domain name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AliasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shorten.rest");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    AliasApi apiInstance = new AliasApi(defaultClient);
    String aliasName = "aBcDe012"; // String | alias value (without `/` at the beginning)
    String domainName = "short.fyi"; // String | domain which alias belongs to (string without `http/https` or `/`)
    try {
      AliasModel result = apiInstance.getAlias(aliasName, domainName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AliasApi#getAlias");
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
| **aliasName** | **String**| alias value (without &#x60;/&#x60; at the beginning) | |
| **domainName** | **String**| domain which alias belongs to (string without &#x60;http/https&#x60; or &#x60;/&#x60;) | [optional] [default to short.fyi] |

### Return type

[**AliasModel**](AliasModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Alias model or **null** |  -  |

<a id="getAliases"></a>
# **getAliases**
> GetAliasesModel getAliases(domainName, continueFrom, limit)

Get aliases by domain

Obtain a list of all alias names associated with your account and given domain. Result array is in descending order by creation date.    If no domain is specified you will receive a list of all the alias names you have created using the Short.fyi domain.    If there are more results than the limit for the request the response will return you a value in lastId property you can specify it in the continueFrom query parameter to get the next batch of records.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AliasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shorten.rest");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    AliasApi apiInstance = new AliasApi(defaultClient);
    String domainName = "short.fyi"; // String | The domain name to get the aliases for (string without `http/https` or `/`)
    String continueFrom = "1588788835614657618"; // String | An ID returned by a previous query to continue aliases retrieval (see lastId in response)
    Integer limit = 1000; // Integer | Number of results to return per request
    try {
      GetAliasesModel result = apiInstance.getAliases(domainName, continueFrom, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AliasApi#getAliases");
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
| **domainName** | **String**| The domain name to get the aliases for (string without &#x60;http/https&#x60; or &#x60;/&#x60;) | [optional] [default to short.fyi] |
| **continueFrom** | **String**| An ID returned by a previous query to continue aliases retrieval (see lastId in response) | [optional] |
| **limit** | **Integer**| Number of results to return per request | [optional] [default to 1000] |

### Return type

[**GetAliasesModel**](GetAliasesModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | returns Array of aliases with lastId |  -  |

<a id="updateAlias"></a>
# **updateAlias**
> updateAlias(aliasName, createAliasModel, domainName)

Update alias

Update a single short URL by providing its alias and domain as a parameter, and the data you wish to update in the body of the request. If no domain is provided you will receive the alias found attached to the Short.fyi domain (if it exists and is linked to your account!)   ### NOTE:    ( * )If you add a metatag or a snippet with a same name to an alias and the domain it&#39;s related to, the value will be taken from the alias and not the domain    ( ** ) When you update any array property (like destinations) the block is updated **completely** so you have to specify the old records to avoid deleting them   ( *** ) The method updates only the specified properties so if there was no change in one of them you don&#39;t have to send it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AliasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shorten.rest");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    AliasApi apiInstance = new AliasApi(defaultClient);
    String aliasName = "aBcDe012"; // String | alias (without `/` at the beginning)
    CreateAliasModel createAliasModel = new CreateAliasModel(); // CreateAliasModel | alias properties you wish to be updated
    String domainName = "short.fyi"; // String | domain which alias belongs to (string without `http/https` or `/`)
    try {
      apiInstance.updateAlias(aliasName, createAliasModel, domainName);
    } catch (ApiException e) {
      System.err.println("Exception when calling AliasApi#updateAlias");
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
| **aliasName** | **String**| alias (without &#x60;/&#x60; at the beginning) | |
| **createAliasModel** | [**CreateAliasModel**](CreateAliasModel.md)| alias properties you wish to be updated | |
| **domainName** | **String**| domain which alias belongs to (string without &#x60;http/https&#x60; or &#x60;/&#x60;) | [optional] [default to short.fyi] |

### Return type

null (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Empty response |  -  |

