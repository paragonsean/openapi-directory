# ClientApiApi

All URIs are relative to *https://api.tradematic.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**clientApikeysGet**](ClientApiApi.md#clientApikeysGet) | **GET** /client/apikeys | Get API keys |
| [**clientApikeysKeyidDelete**](ClientApiApi.md#clientApikeysKeyidDelete) | **DELETE** /client/apikeys/{keyid} | Delete API key |
| [**clientApikeysPost**](ClientApiApi.md#clientApikeysPost) | **POST** /client/apikeys | Create new API key |
| [**clientUsersGet**](ClientApiApi.md#clientUsersGet) | **GET** /client/users | Get users list |
| [**clientUsersLoginPost**](ClientApiApi.md#clientUsersLoginPost) | **POST** /client/users/login | Logs user into the system |
| [**clientUsersRegisterPost**](ClientApiApi.md#clientUsersRegisterPost) | **POST** /client/users/register | Register a new user |
| [**clientUsersUseridGet**](ClientApiApi.md#clientUsersUseridGet) | **GET** /client/users/{userid} | Get user by ID |


<a id="clientApikeysGet"></a>
# **clientApikeysGet**
> List&lt;APIKey&gt; clientApikeysGet()

Get API keys

Get API keys

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tradematic.com");
    
    // Configure API key authorization: Secured
    ApiKeyAuth Secured = (ApiKeyAuth) defaultClient.getAuthentication("Secured");
    Secured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Secured.setApiKeyPrefix("Token");

    ClientApiApi apiInstance = new ClientApiApi(defaultClient);
    try {
      List<APIKey> result = apiInstance.clientApikeysGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientApiApi#clientApikeysGet");
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

[**List&lt;APIKey&gt;**](APIKey.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **500** | Error |  -  |

<a id="clientApikeysKeyidDelete"></a>
# **clientApikeysKeyidDelete**
> ClientApikeysKeyidDelete200Response clientApikeysKeyidDelete(keyid)

Delete API key

Delete API key

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tradematic.com");
    
    // Configure API key authorization: Secured
    ApiKeyAuth Secured = (ApiKeyAuth) defaultClient.getAuthentication("Secured");
    Secured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Secured.setApiKeyPrefix("Token");

    ClientApiApi apiInstance = new ClientApiApi(defaultClient);
    Long keyid = 56L; // Long | 
    try {
      ClientApikeysKeyidDelete200Response result = apiInstance.clientApikeysKeyidDelete(keyid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientApiApi#clientApikeysKeyidDelete");
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
| **keyid** | **Long**|  | |

### Return type

[**ClientApikeysKeyidDelete200Response**](ClientApikeysKeyidDelete200Response.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **500** | Error |  -  |

<a id="clientApikeysPost"></a>
# **clientApikeysPost**
> ClientApikeysPost200Response clientApikeysPost()

Create new API key

Create new API key

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tradematic.com");
    
    // Configure API key authorization: Secured
    ApiKeyAuth Secured = (ApiKeyAuth) defaultClient.getAuthentication("Secured");
    Secured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Secured.setApiKeyPrefix("Token");

    ClientApiApi apiInstance = new ClientApiApi(defaultClient);
    try {
      ClientApikeysPost200Response result = apiInstance.clientApikeysPost();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientApiApi#clientApikeysPost");
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

[**ClientApikeysPost200Response**](ClientApikeysPost200Response.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **500** | Error |  -  |

<a id="clientUsersGet"></a>
# **clientUsersGet**
> List&lt;User&gt; clientUsersGet()

Get users list

Get users list

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tradematic.com");
    
    // Configure API key authorization: Secured
    ApiKeyAuth Secured = (ApiKeyAuth) defaultClient.getAuthentication("Secured");
    Secured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Secured.setApiKeyPrefix("Token");

    ClientApiApi apiInstance = new ClientApiApi(defaultClient);
    try {
      List<User> result = apiInstance.clientUsersGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientApiApi#clientUsersGet");
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

[**List&lt;User&gt;**](User.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **500** | Error |  -  |

<a id="clientUsersLoginPost"></a>
# **clientUsersLoginPost**
> ClientUsersLoginPost200Response clientUsersLoginPost()

Logs user into the system

Logs user into the system

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tradematic.com");
    
    // Configure API key authorization: Secured
    ApiKeyAuth Secured = (ApiKeyAuth) defaultClient.getAuthentication("Secured");
    Secured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Secured.setApiKeyPrefix("Token");

    ClientApiApi apiInstance = new ClientApiApi(defaultClient);
    try {
      ClientUsersLoginPost200Response result = apiInstance.clientUsersLoginPost();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientApiApi#clientUsersLoginPost");
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

[**ClientUsersLoginPost200Response**](ClientUsersLoginPost200Response.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **500** | Error |  -  |

<a id="clientUsersRegisterPost"></a>
# **clientUsersRegisterPost**
> ClientUsersRegisterPost200Response clientUsersRegisterPost(body)

Register a new user

Register a new user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tradematic.com");
    
    // Configure API key authorization: Secured
    ApiKeyAuth Secured = (ApiKeyAuth) defaultClient.getAuthentication("Secured");
    Secured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Secured.setApiKeyPrefix("Token");

    ClientApiApi apiInstance = new ClientApiApi(defaultClient);
    ClientUsersRegisterPostRequest body = new ClientUsersRegisterPostRequest(); // ClientUsersRegisterPostRequest | 
    try {
      ClientUsersRegisterPost200Response result = apiInstance.clientUsersRegisterPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientApiApi#clientUsersRegisterPost");
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
| **body** | [**ClientUsersRegisterPostRequest**](ClientUsersRegisterPostRequest.md)|  | |

### Return type

[**ClientUsersRegisterPost200Response**](ClientUsersRegisterPost200Response.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **500** | Error |  -  |

<a id="clientUsersUseridGet"></a>
# **clientUsersUseridGet**
> User clientUsersUseridGet(userid)

Get user by ID

Get user by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tradematic.com");
    
    // Configure API key authorization: Secured
    ApiKeyAuth Secured = (ApiKeyAuth) defaultClient.getAuthentication("Secured");
    Secured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Secured.setApiKeyPrefix("Token");

    ClientApiApi apiInstance = new ClientApiApi(defaultClient);
    Long userid = 56L; // Long | 
    try {
      User result = apiInstance.clientUsersUseridGet(userid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientApiApi#clientUsersUseridGet");
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
| **userid** | **Long**|  | |

### Return type

[**User**](User.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **500** | Error |  -  |

