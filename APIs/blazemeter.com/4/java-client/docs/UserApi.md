# UserApi

All URIs are relative to *https://a.blazemeter.com/api/v4*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**activeSessions**](UserApi.md#activeSessions) | **GET** /user/active/sessions | &amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt; |
| [**panicTerminate**](UserApi.md#panicTerminate) | **POST** /user/active/terminate | &amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt; |
| [**register**](UserApi.md#register) | **POST** /user/register | Registration&amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt; |
| [**registerRetrieve**](UserApi.md#registerRetrieve) | **GET** /user/register | Registration&amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt; |
| [**retrieveCollections**](UserApi.md#retrieveCollections) | **GET** /user/collections | List organization multi-tests&amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt; |
| [**retrieveInvites**](UserApi.md#retrieveInvites) | **GET** /user/invites | &amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt; |
| [**retrieveLocations**](UserApi.md#retrieveLocations) | **GET** /user/locations | Get user available locations&amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt; |
| [**retrieveMasters**](UserApi.md#retrieveMasters) | **GET** /user/masters | List user private masters&amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt; |
| [**retrieveProjects**](UserApi.md#retrieveProjects) | **GET** /user/projects | Get user projects&amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt; |
| [**retrieveTests**](UserApi.md#retrieveTests) | **GET** /user/tests | List user private tests&amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt; |
| [**top**](UserApi.md#top) | **GET** /user/top | &amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt; |
| [**userPasswordPatch**](UserApi.md#userPasswordPatch) | **PATCH** /user/password | Update user name&amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt; |
| [**userPasswordPost**](UserApi.md#userPasswordPost) | **POST** /user/password | Update user name&amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt; |
| [**userPasswordPut**](UserApi.md#userPasswordPut) | **PUT** /user/password | Update user name&amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt; |


<a id="activeSessions"></a>
# **activeSessions**
> Object activeSessions()

&amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://a.blazemeter.com/api/v4");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    UserApi apiInstance = new UserApi(defaultClient);
    try {
      Object result = apiInstance.activeSessions();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#activeSessions");
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

**Object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html, text/javascript, text/csv, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="panicTerminate"></a>
# **panicTerminate**
> Object panicTerminate(blazemeterRoutingV4UserModel5)

&amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://a.blazemeter.com/api/v4");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    UserApi apiInstance = new UserApi(defaultClient);
    Object blazemeterRoutingV4UserModel5 = null; // Object | <section class=\"body-param\"><strong>session_ids</strong> (required)<br/></section>
    try {
      Object result = apiInstance.panicTerminate(blazemeterRoutingV4UserModel5);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#panicTerminate");
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
| **blazemeterRoutingV4UserModel5** | **Object**| &lt;section class&#x3D;\&quot;body-param\&quot;&gt;&lt;strong&gt;session_ids&lt;/strong&gt; (required)&lt;br/&gt;&lt;/section&gt; | [optional] |

### Return type

**Object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, text/csv, text/plain
 - **Accept**: application/json, text/html, text/javascript, text/csv, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="register"></a>
# **register**
> Object register(blazemeterRoutingV4UserModel4)

Registration&amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://a.blazemeter.com/api/v4");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    UserApi apiInstance = new UserApi(defaultClient);
    Object blazemeterRoutingV4UserModel4 = null; // Object | <section class=\"body-param\"><strong>firstName</strong> (required)<br/><strong>lastName</strong> (required)<br/><strong>email</strong> (required)<br/><strong>password</strong> (required)<br/></section>
    try {
      Object result = apiInstance.register(blazemeterRoutingV4UserModel4);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#register");
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
| **blazemeterRoutingV4UserModel4** | **Object**| &lt;section class&#x3D;\&quot;body-param\&quot;&gt;&lt;strong&gt;firstName&lt;/strong&gt; (required)&lt;br/&gt;&lt;strong&gt;lastName&lt;/strong&gt; (required)&lt;br/&gt;&lt;strong&gt;email&lt;/strong&gt; (required)&lt;br/&gt;&lt;strong&gt;password&lt;/strong&gt; (required)&lt;br/&gt;&lt;/section&gt; | |

### Return type

**Object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, text/csv, text/plain
 - **Accept**: application/json, text/html, text/javascript, text/csv, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **500** | RestException |  -  |

<a id="registerRetrieve"></a>
# **registerRetrieve**
> Object registerRetrieve(email, password, firstName, lastName)

Registration&amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://a.blazemeter.com/api/v4");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    UserApi apiInstance = new UserApi(defaultClient);
    String email = "email_example"; // String | Email address
    String password = "password_example"; // String | Password
    String firstName = "firstName_example"; // String | First name
    String lastName = "lastName_example"; // String | Last name
    try {
      Object result = apiInstance.registerRetrieve(email, password, firstName, lastName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#registerRetrieve");
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
| **email** | **String**| Email address | |
| **password** | **String**| Password | |
| **firstName** | **String**| First name | [optional] |
| **lastName** | **String**| Last name | [optional] |

### Return type

**Object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html, text/javascript, text/csv, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **500** | RestException |  -  |

<a id="retrieveCollections"></a>
# **retrieveCollections**
> Object retrieveCollections(skip, limit)

List organization multi-tests&amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://a.blazemeter.com/api/v4");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    UserApi apiInstance = new UserApi(defaultClient);
    String skip = "skip_example"; // String | 
    String limit = "limit_example"; // String | 
    try {
      Object result = apiInstance.retrieveCollections(skip, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#retrieveCollections");
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
| **skip** | **String**|  | [optional] |
| **limit** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html, text/javascript, text/csv, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **500** | RestException |  -  |

<a id="retrieveInvites"></a>
# **retrieveInvites**
> List&lt;String&gt; retrieveInvites()

&amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://a.blazemeter.com/api/v4");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    UserApi apiInstance = new UserApi(defaultClient);
    try {
      List<String> result = apiInstance.retrieveInvites();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#retrieveInvites");
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

**List&lt;String&gt;**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html, text/javascript, text/csv, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="retrieveLocations"></a>
# **retrieveLocations**
> Object retrieveLocations()

Get user available locations&amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://a.blazemeter.com/api/v4");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    UserApi apiInstance = new UserApi(defaultClient);
    try {
      Object result = apiInstance.retrieveLocations();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#retrieveLocations");
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

**Object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html, text/javascript, text/csv, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **500** | RestException |  -  |

<a id="retrieveMasters"></a>
# **retrieveMasters**
> Object retrieveMasters(skip, limit)

List user private masters&amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://a.blazemeter.com/api/v4");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    UserApi apiInstance = new UserApi(defaultClient);
    Long skip = 56L; // Long | 
    Long limit = 1000L; // Long | 
    try {
      Object result = apiInstance.retrieveMasters(skip, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#retrieveMasters");
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
| **skip** | **Long**|  | [optional] |
| **limit** | **Long**|  | [optional] [default to 1000] |

### Return type

**Object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html, text/javascript, text/csv, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="retrieveProjects"></a>
# **retrieveProjects**
> Object retrieveProjects()

Get user projects&amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://a.blazemeter.com/api/v4");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    UserApi apiInstance = new UserApi(defaultClient);
    try {
      Object result = apiInstance.retrieveProjects();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#retrieveProjects");
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

**Object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html, text/javascript, text/csv, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="retrieveTests"></a>
# **retrieveTests**
> Object retrieveTests(skip, limit)

List user private tests&amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://a.blazemeter.com/api/v4");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    UserApi apiInstance = new UserApi(defaultClient);
    String skip = "skip_example"; // String | 
    String limit = "limit_example"; // String | 
    try {
      Object result = apiInstance.retrieveTests(skip, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#retrieveTests");
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
| **skip** | **String**|  | [optional] |
| **limit** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html, text/javascript, text/csv, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **500** | RestException |  -  |

<a id="top"></a>
# **top**
> List&lt;String&gt; top()

&amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://a.blazemeter.com/api/v4");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    UserApi apiInstance = new UserApi(defaultClient);
    try {
      List<String> result = apiInstance.top();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#top");
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

**List&lt;String&gt;**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html, text/javascript, text/csv, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="userPasswordPatch"></a>
# **userPasswordPatch**
> Object userPasswordPatch(blazemeterRoutingV4UserModel1)

Update user name&amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://a.blazemeter.com/api/v4");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    UserApi apiInstance = new UserApi(defaultClient);
    Object blazemeterRoutingV4UserModel1 = null; // Object | <section class=\"body-param\"><strong>currentPassword</strong> (required)<br/><strong>newPassword</strong> (required)<br/></section>
    try {
      Object result = apiInstance.userPasswordPatch(blazemeterRoutingV4UserModel1);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#userPasswordPatch");
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
| **blazemeterRoutingV4UserModel1** | **Object**| &lt;section class&#x3D;\&quot;body-param\&quot;&gt;&lt;strong&gt;currentPassword&lt;/strong&gt; (required)&lt;br/&gt;&lt;strong&gt;newPassword&lt;/strong&gt; (required)&lt;br/&gt;&lt;/section&gt; | |

### Return type

**Object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, text/csv, text/plain
 - **Accept**: application/json, text/html, text/javascript, text/csv, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **500** | RestException |  -  |

<a id="userPasswordPost"></a>
# **userPasswordPost**
> Object userPasswordPost(blazemeterRoutingV4UserModel3)

Update user name&amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://a.blazemeter.com/api/v4");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    UserApi apiInstance = new UserApi(defaultClient);
    Object blazemeterRoutingV4UserModel3 = null; // Object | <section class=\"body-param\"><strong>currentPassword</strong> (required)<br/><strong>newPassword</strong> (required)<br/></section>
    try {
      Object result = apiInstance.userPasswordPost(blazemeterRoutingV4UserModel3);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#userPasswordPost");
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
| **blazemeterRoutingV4UserModel3** | **Object**| &lt;section class&#x3D;\&quot;body-param\&quot;&gt;&lt;strong&gt;currentPassword&lt;/strong&gt; (required)&lt;br/&gt;&lt;strong&gt;newPassword&lt;/strong&gt; (required)&lt;br/&gt;&lt;/section&gt; | |

### Return type

**Object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, text/csv, text/plain
 - **Accept**: application/json, text/html, text/javascript, text/csv, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **500** | RestException |  -  |

<a id="userPasswordPut"></a>
# **userPasswordPut**
> Object userPasswordPut(blazemeterRoutingV4UserModel2)

Update user name&amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://a.blazemeter.com/api/v4");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    UserApi apiInstance = new UserApi(defaultClient);
    Object blazemeterRoutingV4UserModel2 = null; // Object | <section class=\"body-param\"><strong>currentPassword</strong> (required)<br/><strong>newPassword</strong> (required)<br/></section>
    try {
      Object result = apiInstance.userPasswordPut(blazemeterRoutingV4UserModel2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#userPasswordPut");
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
| **blazemeterRoutingV4UserModel2** | **Object**| &lt;section class&#x3D;\&quot;body-param\&quot;&gt;&lt;strong&gt;currentPassword&lt;/strong&gt; (required)&lt;br/&gt;&lt;strong&gt;newPassword&lt;/strong&gt; (required)&lt;br/&gt;&lt;/section&gt; | |

### Return type

**Object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, text/csv, text/plain
 - **Accept**: application/json, text/html, text/javascript, text/csv, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **500** | RestException |  -  |

