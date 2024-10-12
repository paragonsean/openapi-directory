# DevelopersFindAndModifyDevelopersApi

All URIs are relative to *https://market.openchannel.io/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**developersDeveloperIdDelete**](DevelopersFindAndModifyDevelopersApi.md#developersDeveloperIdDelete) | **DELETE** /developers/{developerId} | Removes a single developer |
| [**developersDeveloperIdGet**](DevelopersFindAndModifyDevelopersApi.md#developersDeveloperIdGet) | **GET** /developers/{developerId} | Returns a single developer |
| [**developersDeveloperIdPatch**](DevelopersFindAndModifyDevelopersApi.md#developersDeveloperIdPatch) | **PATCH** /developers/{developerId} | Updates the developer fields |
| [**developersDeveloperIdPost**](DevelopersFindAndModifyDevelopersApi.md#developersDeveloperIdPost) | **POST** /developers/{developerId} | Updates the developer record or adds the developer if it doesn&#39;t exist |
| [**developersGet**](DevelopersFindAndModifyDevelopersApi.md#developersGet) | **GET** /developers | Returns a paginated list of developers |


<a id="developersDeveloperIdDelete"></a>
# **developersDeveloperIdDelete**
> developersDeveloperIdDelete(developerId)

Removes a single developer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevelopersFindAndModifyDevelopersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DevelopersFindAndModifyDevelopersApi apiInstance = new DevelopersFindAndModifyDevelopersApi(defaultClient);
    String developerId = "developerId_example"; // String | The id of the developer to be removed
    try {
      apiInstance.developersDeveloperIdDelete(developerId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevelopersFindAndModifyDevelopersApi#developersDeveloperIdDelete");
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
| **developerId** | **String**| The id of the developer to be removed | |

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request - Required parameters are missing, malformed or invalid |  -  |
| **404** | Not Found - Developer is not found |  -  |
| **0** | OK |  -  |

<a id="developersDeveloperIdGet"></a>
# **developersDeveloperIdGet**
> Developer developersDeveloperIdGet(developerId)

Returns a single developer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevelopersFindAndModifyDevelopersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DevelopersFindAndModifyDevelopersApi apiInstance = new DevelopersFindAndModifyDevelopersApi(defaultClient);
    String developerId = "developerId_example"; // String | The id of the developer to be located
    try {
      Developer result = apiInstance.developersDeveloperIdGet(developerId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevelopersFindAndModifyDevelopersApi#developersDeveloperIdGet");
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
| **developerId** | **String**| The id of the developer to be located | |

### Return type

[**Developer**](Developer.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request - Required parameters are missing, malformed or invalid |  -  |
| **404** | Not Found - Developer is not found |  -  |
| **0** | OK |  -  |

<a id="developersDeveloperIdPatch"></a>
# **developersDeveloperIdPatch**
> Developer developersDeveloperIdPatch(developerId, type, email, username, name, customData)

Updates the developer fields

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevelopersFindAndModifyDevelopersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DevelopersFindAndModifyDevelopersApi apiInstance = new DevelopersFindAndModifyDevelopersApi(defaultClient);
    String developerId = "developerId_example"; // String | The id of the developer to be located
    String type = "type_example"; // String | The type for this developer
    String email = "email_example"; // String | The developer's email
    String username = "username_example"; // String | The developer's username
    String name = "name_example"; // String | The developer's name
    String customData = "customData_example"; // String | A custom JSON object that you can create and attach to this record
    try {
      Developer result = apiInstance.developersDeveloperIdPatch(developerId, type, email, username, name, customData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevelopersFindAndModifyDevelopersApi#developersDeveloperIdPatch");
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
| **developerId** | **String**| The id of the developer to be located | |
| **type** | **String**| The type for this developer | [optional] |
| **email** | **String**| The developer&#39;s email | [optional] |
| **username** | **String**| The developer&#39;s username | [optional] |
| **name** | **String**| The developer&#39;s name | [optional] |
| **customData** | **String**| A custom JSON object that you can create and attach to this record | [optional] |

### Return type

[**Developer**](Developer.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request - Required parameters are missing, malformed or invalid |  -  |
| **404** | Not Found - The developer is not found |  -  |
| **0** | OK |  -  |

<a id="developersDeveloperIdPost"></a>
# **developersDeveloperIdPost**
> Developer developersDeveloperIdPost(developerId, type, email, username, name, customData)

Updates the developer record or adds the developer if it doesn&#39;t exist

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevelopersFindAndModifyDevelopersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DevelopersFindAndModifyDevelopersApi apiInstance = new DevelopersFindAndModifyDevelopersApi(defaultClient);
    String developerId = "developerId_example"; // String | The id of the developer to be located
    String type = "type_example"; // String | The type for this developer
    String email = "email_example"; // String | The developer's email
    String username = "username_example"; // String | The developer's username
    String name = "name_example"; // String | The developer's name
    String customData = "customData_example"; // String | A custom JSON object that you can create and attach to this record
    try {
      Developer result = apiInstance.developersDeveloperIdPost(developerId, type, email, username, name, customData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevelopersFindAndModifyDevelopersApi#developersDeveloperIdPost");
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
| **developerId** | **String**| The id of the developer to be located | |
| **type** | **String**| The type for this developer | [optional] |
| **email** | **String**| The developer&#39;s email | [optional] |
| **username** | **String**| The developer&#39;s username | [optional] |
| **name** | **String**| The developer&#39;s name | [optional] |
| **customData** | **String**| A custom JSON object that you can create and attach to this record | [optional] |

### Return type

[**Developer**](Developer.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request - Required parameters are missing, malformed or invalid |  -  |
| **0** | OK |  -  |

<a id="developersGet"></a>
# **developersGet**
> DeveloperPages developersGet(query, sort, pageNumber, limit)

Returns a paginated list of developers

- Results are paginated and the default is value is 100 if no limit is provided 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevelopersFindAndModifyDevelopersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DevelopersFindAndModifyDevelopersApi apiInstance = new DevelopersFindAndModifyDevelopersApi(defaultClient);
    String query = "query_example"; // String | A query document. Example: {'name':'John'} matches all the developers that have the name 'John'
    String sort = "sort_example"; // String | A sort document. Example: {'name':1} sorts the results by name in ascending order
    Integer pageNumber = 56; // Integer | The result set page number to be returned
    Integer limit = 56; // Integer | The maximum number of results to return per page
    try {
      DeveloperPages result = apiInstance.developersGet(query, sort, pageNumber, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevelopersFindAndModifyDevelopersApi#developersGet");
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
| **query** | **String**| A query document. Example: {&#39;name&#39;:&#39;John&#39;} matches all the developers that have the name &#39;John&#39; | [optional] |
| **sort** | **String**| A sort document. Example: {&#39;name&#39;:1} sorts the results by name in ascending order | [optional] |
| **pageNumber** | **Integer**| The result set page number to be returned | [optional] |
| **limit** | **Integer**| The maximum number of results to return per page | [optional] |

### Return type

[**DeveloperPages**](DeveloperPages.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request - Required parameters are missing, malformed or invalid |  -  |
| **0** | OK |  -  |

