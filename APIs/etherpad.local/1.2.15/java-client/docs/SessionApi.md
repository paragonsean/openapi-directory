# SessionApi

All URIs are relative to *http://etherpad.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createSessionUsingGET**](SessionApi.md#createSessionUsingGET) | **GET** /createSession | creates a new session. validUntil is an unix timestamp in seconds |
| [**createSessionUsingPOST**](SessionApi.md#createSessionUsingPOST) | **POST** /createSession | creates a new session. validUntil is an unix timestamp in seconds |
| [**deleteSessionUsingGET**](SessionApi.md#deleteSessionUsingGET) | **GET** /deleteSession | deletes a session |
| [**deleteSessionUsingPOST**](SessionApi.md#deleteSessionUsingPOST) | **POST** /deleteSession | deletes a session |
| [**getSessionInfoUsingGET**](SessionApi.md#getSessionInfoUsingGET) | **GET** /getSessionInfo | returns informations about a session |
| [**getSessionInfoUsingPOST**](SessionApi.md#getSessionInfoUsingPOST) | **POST** /getSessionInfo | returns informations about a session |


<a id="createSessionUsingGET"></a>
# **createSessionUsingGET**
> CreateSessionUsingGET200Response createSessionUsingGET(groupID, authorID, validUntil)

creates a new session. validUntil is an unix timestamp in seconds

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SessionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    SessionApi apiInstance = new SessionApi(defaultClient);
    String groupID = "groupID_example"; // String | 
    String authorID = "authorID_example"; // String | 
    String validUntil = "validUntil_example"; // String | 
    try {
      CreateSessionUsingGET200Response result = apiInstance.createSessionUsingGET(groupID, authorID, validUntil);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SessionApi#createSessionUsingGET");
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
| **groupID** | **String**|  | [optional] |
| **authorID** | **String**|  | [optional] |
| **validUntil** | **String**|  | [optional] |

### Return type

[**CreateSessionUsingGET200Response**](CreateSessionUsingGET200Response.md)

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

<a id="createSessionUsingPOST"></a>
# **createSessionUsingPOST**
> CreateSessionUsingGET200Response createSessionUsingPOST(groupID, authorID, validUntil)

creates a new session. validUntil is an unix timestamp in seconds

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SessionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    SessionApi apiInstance = new SessionApi(defaultClient);
    String groupID = "groupID_example"; // String | 
    String authorID = "authorID_example"; // String | 
    String validUntil = "validUntil_example"; // String | 
    try {
      CreateSessionUsingGET200Response result = apiInstance.createSessionUsingPOST(groupID, authorID, validUntil);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SessionApi#createSessionUsingPOST");
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
| **groupID** | **String**|  | [optional] |
| **authorID** | **String**|  | [optional] |
| **validUntil** | **String**|  | [optional] |

### Return type

[**CreateSessionUsingGET200Response**](CreateSessionUsingGET200Response.md)

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

<a id="deleteSessionUsingGET"></a>
# **deleteSessionUsingGET**
> AppendChatMessageUsingGET200Response deleteSessionUsingGET(sessionID)

deletes a session

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SessionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    SessionApi apiInstance = new SessionApi(defaultClient);
    String sessionID = "sessionID_example"; // String | 
    try {
      AppendChatMessageUsingGET200Response result = apiInstance.deleteSessionUsingGET(sessionID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SessionApi#deleteSessionUsingGET");
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
| **sessionID** | **String**|  | [optional] |

### Return type

[**AppendChatMessageUsingGET200Response**](AppendChatMessageUsingGET200Response.md)

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

<a id="deleteSessionUsingPOST"></a>
# **deleteSessionUsingPOST**
> AppendChatMessageUsingGET200Response deleteSessionUsingPOST(sessionID)

deletes a session

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SessionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    SessionApi apiInstance = new SessionApi(defaultClient);
    String sessionID = "sessionID_example"; // String | 
    try {
      AppendChatMessageUsingGET200Response result = apiInstance.deleteSessionUsingPOST(sessionID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SessionApi#deleteSessionUsingPOST");
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
| **sessionID** | **String**|  | [optional] |

### Return type

[**AppendChatMessageUsingGET200Response**](AppendChatMessageUsingGET200Response.md)

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

<a id="getSessionInfoUsingGET"></a>
# **getSessionInfoUsingGET**
> GetSessionInfoUsingGET200Response getSessionInfoUsingGET(sessionID)

returns informations about a session

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SessionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    SessionApi apiInstance = new SessionApi(defaultClient);
    String sessionID = "sessionID_example"; // String | 
    try {
      GetSessionInfoUsingGET200Response result = apiInstance.getSessionInfoUsingGET(sessionID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SessionApi#getSessionInfoUsingGET");
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
| **sessionID** | **String**|  | [optional] |

### Return type

[**GetSessionInfoUsingGET200Response**](GetSessionInfoUsingGET200Response.md)

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

<a id="getSessionInfoUsingPOST"></a>
# **getSessionInfoUsingPOST**
> GetSessionInfoUsingGET200Response getSessionInfoUsingPOST(sessionID)

returns informations about a session

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SessionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    SessionApi apiInstance = new SessionApi(defaultClient);
    String sessionID = "sessionID_example"; // String | 
    try {
      GetSessionInfoUsingGET200Response result = apiInstance.getSessionInfoUsingPOST(sessionID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SessionApi#getSessionInfoUsingPOST");
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
| **sessionID** | **String**|  | [optional] |

### Return type

[**GetSessionInfoUsingGET200Response**](GetSessionInfoUsingGET200Response.md)

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

