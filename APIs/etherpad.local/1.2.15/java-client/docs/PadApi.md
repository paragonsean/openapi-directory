# PadApi

All URIs are relative to *http://etherpad.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**appendChatMessageUsingGET**](PadApi.md#appendChatMessageUsingGET) | **GET** /appendChatMessage | appends a chat message |
| [**appendChatMessageUsingPOST**](PadApi.md#appendChatMessageUsingPOST) | **POST** /appendChatMessage | appends a chat message |
| [**checkTokenUsingGET**](PadApi.md#checkTokenUsingGET) | **GET** /checkToken | returns ok when the current api token is valid |
| [**checkTokenUsingPOST**](PadApi.md#checkTokenUsingPOST) | **POST** /checkToken | returns ok when the current api token is valid |
| [**createDiffHTMLUsingGET**](PadApi.md#createDiffHTMLUsingGET) | **GET** /createDiffHTML |  |
| [**createDiffHTMLUsingPOST**](PadApi.md#createDiffHTMLUsingPOST) | **POST** /createDiffHTML |  |
| [**createPadUsingGET**](PadApi.md#createPadUsingGET) | **GET** /createPad |  |
| [**createPadUsingPOST**](PadApi.md#createPadUsingPOST) | **POST** /createPad |  |
| [**deletePadUsingGET**](PadApi.md#deletePadUsingGET) | **GET** /deletePad | deletes a pad |
| [**deletePadUsingPOST**](PadApi.md#deletePadUsingPOST) | **POST** /deletePad | deletes a pad |
| [**getChatHeadUsingGET**](PadApi.md#getChatHeadUsingGET) | **GET** /getChatHead | returns the chatHead (chat-message) of the pad |
| [**getChatHeadUsingPOST**](PadApi.md#getChatHeadUsingPOST) | **POST** /getChatHead | returns the chatHead (chat-message) of the pad |
| [**getChatHistoryUsingGET**](PadApi.md#getChatHistoryUsingGET) | **GET** /getChatHistory | returns the chat history |
| [**getChatHistoryUsingPOST**](PadApi.md#getChatHistoryUsingPOST) | **POST** /getChatHistory | returns the chat history |
| [**getHTMLUsingGET**](PadApi.md#getHTMLUsingGET) | **GET** /getHTML | returns the text of a pad formatted as HTML |
| [**getHTMLUsingPOST**](PadApi.md#getHTMLUsingPOST) | **POST** /getHTML | returns the text of a pad formatted as HTML |
| [**getLastEditedUsingGET**](PadApi.md#getLastEditedUsingGET) | **GET** /getLastEdited | returns the timestamp of the last revision of the pad |
| [**getLastEditedUsingPOST**](PadApi.md#getLastEditedUsingPOST) | **POST** /getLastEdited | returns the timestamp of the last revision of the pad |
| [**getPublicStatusUsingGET**](PadApi.md#getPublicStatusUsingGET) | **GET** /getPublicStatus | return true of false |
| [**getPublicStatusUsingPOST**](PadApi.md#getPublicStatusUsingPOST) | **POST** /getPublicStatus | return true of false |
| [**getReadOnlyIDUsingGET**](PadApi.md#getReadOnlyIDUsingGET) | **GET** /getReadOnlyID | returns the read only link of a pad |
| [**getReadOnlyIDUsingPOST**](PadApi.md#getReadOnlyIDUsingPOST) | **POST** /getReadOnlyID | returns the read only link of a pad |
| [**getRevisionsCountUsingGET**](PadApi.md#getRevisionsCountUsingGET) | **GET** /getRevisionsCount | returns the number of revisions of this pad |
| [**getRevisionsCountUsingPOST**](PadApi.md#getRevisionsCountUsingPOST) | **POST** /getRevisionsCount | returns the number of revisions of this pad |
| [**getTextUsingGET**](PadApi.md#getTextUsingGET) | **GET** /getText | returns the text of a pad |
| [**getTextUsingPOST**](PadApi.md#getTextUsingPOST) | **POST** /getText | returns the text of a pad |
| [**listAllPadsUsingGET**](PadApi.md#listAllPadsUsingGET) | **GET** /listAllPads | list all the pads |
| [**listAllPadsUsingPOST**](PadApi.md#listAllPadsUsingPOST) | **POST** /listAllPads | list all the pads |
| [**listAuthorsOfPadUsingGET**](PadApi.md#listAuthorsOfPadUsingGET) | **GET** /listAuthorsOfPad | returns an array of authors who contributed to this pad |
| [**listAuthorsOfPadUsingPOST**](PadApi.md#listAuthorsOfPadUsingPOST) | **POST** /listAuthorsOfPad | returns an array of authors who contributed to this pad |
| [**padUsersCountUsingGET**](PadApi.md#padUsersCountUsingGET) | **GET** /padUsersCount | returns the number of user that are currently editing this pad |
| [**padUsersCountUsingPOST**](PadApi.md#padUsersCountUsingPOST) | **POST** /padUsersCount | returns the number of user that are currently editing this pad |
| [**padUsersUsingGET**](PadApi.md#padUsersUsingGET) | **GET** /padUsers | returns the list of users that are currently editing this pad |
| [**padUsersUsingPOST**](PadApi.md#padUsersUsingPOST) | **POST** /padUsers | returns the list of users that are currently editing this pad |
| [**sendClientsMessageUsingGET**](PadApi.md#sendClientsMessageUsingGET) | **GET** /sendClientsMessage | sends a custom message of type msg to the pad |
| [**sendClientsMessageUsingPOST**](PadApi.md#sendClientsMessageUsingPOST) | **POST** /sendClientsMessage | sends a custom message of type msg to the pad |
| [**setHTMLUsingGET**](PadApi.md#setHTMLUsingGET) | **GET** /setHTML | sets the text of a pad with HTML |
| [**setHTMLUsingPOST**](PadApi.md#setHTMLUsingPOST) | **POST** /setHTML | sets the text of a pad with HTML |
| [**setPublicStatusUsingGET**](PadApi.md#setPublicStatusUsingGET) | **GET** /setPublicStatus | sets a boolean for the public status of a pad |
| [**setPublicStatusUsingPOST**](PadApi.md#setPublicStatusUsingPOST) | **POST** /setPublicStatus | sets a boolean for the public status of a pad |
| [**setTextUsingGET**](PadApi.md#setTextUsingGET) | **GET** /setText | sets the text of a pad |
| [**setTextUsingPOST**](PadApi.md#setTextUsingPOST) | **POST** /setText | sets the text of a pad |


<a id="appendChatMessageUsingGET"></a>
# **appendChatMessageUsingGET**
> AppendChatMessageUsingGET200Response appendChatMessageUsingGET(padID, text, authorID, time)

appends a chat message

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    PadApi apiInstance = new PadApi(defaultClient);
    String padID = "padID_example"; // String | 
    String text = "text_example"; // String | 
    String authorID = "authorID_example"; // String | 
    String time = "time_example"; // String | 
    try {
      AppendChatMessageUsingGET200Response result = apiInstance.appendChatMessageUsingGET(padID, text, authorID, time);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PadApi#appendChatMessageUsingGET");
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
| **padID** | **String**|  | [optional] |
| **text** | **String**|  | [optional] |
| **authorID** | **String**|  | [optional] |
| **time** | **String**|  | [optional] |

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

<a id="appendChatMessageUsingPOST"></a>
# **appendChatMessageUsingPOST**
> AppendChatMessageUsingGET200Response appendChatMessageUsingPOST(padID, text, authorID, time)

appends a chat message

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    PadApi apiInstance = new PadApi(defaultClient);
    String padID = "padID_example"; // String | 
    String text = "text_example"; // String | 
    String authorID = "authorID_example"; // String | 
    String time = "time_example"; // String | 
    try {
      AppendChatMessageUsingGET200Response result = apiInstance.appendChatMessageUsingPOST(padID, text, authorID, time);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PadApi#appendChatMessageUsingPOST");
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
| **padID** | **String**|  | [optional] |
| **text** | **String**|  | [optional] |
| **authorID** | **String**|  | [optional] |
| **time** | **String**|  | [optional] |

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

<a id="checkTokenUsingGET"></a>
# **checkTokenUsingGET**
> AppendChatMessageUsingGET200Response checkTokenUsingGET()

returns ok when the current api token is valid

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    PadApi apiInstance = new PadApi(defaultClient);
    try {
      AppendChatMessageUsingGET200Response result = apiInstance.checkTokenUsingGET();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PadApi#checkTokenUsingGET");
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

<a id="checkTokenUsingPOST"></a>
# **checkTokenUsingPOST**
> AppendChatMessageUsingGET200Response checkTokenUsingPOST()

returns ok when the current api token is valid

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    PadApi apiInstance = new PadApi(defaultClient);
    try {
      AppendChatMessageUsingGET200Response result = apiInstance.checkTokenUsingPOST();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PadApi#checkTokenUsingPOST");
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

<a id="createDiffHTMLUsingGET"></a>
# **createDiffHTMLUsingGET**
> CreateDiffHTMLUsingGET200Response createDiffHTMLUsingGET(padID, startRev, endRev)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    PadApi apiInstance = new PadApi(defaultClient);
    String padID = "padID_example"; // String | 
    String startRev = "startRev_example"; // String | 
    String endRev = "endRev_example"; // String | 
    try {
      CreateDiffHTMLUsingGET200Response result = apiInstance.createDiffHTMLUsingGET(padID, startRev, endRev);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PadApi#createDiffHTMLUsingGET");
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
| **padID** | **String**|  | [optional] |
| **startRev** | **String**|  | [optional] |
| **endRev** | **String**|  | [optional] |

### Return type

[**CreateDiffHTMLUsingGET200Response**](CreateDiffHTMLUsingGET200Response.md)

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

<a id="createDiffHTMLUsingPOST"></a>
# **createDiffHTMLUsingPOST**
> CreateDiffHTMLUsingGET200Response createDiffHTMLUsingPOST(padID, startRev, endRev)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    PadApi apiInstance = new PadApi(defaultClient);
    String padID = "padID_example"; // String | 
    String startRev = "startRev_example"; // String | 
    String endRev = "endRev_example"; // String | 
    try {
      CreateDiffHTMLUsingGET200Response result = apiInstance.createDiffHTMLUsingPOST(padID, startRev, endRev);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PadApi#createDiffHTMLUsingPOST");
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
| **padID** | **String**|  | [optional] |
| **startRev** | **String**|  | [optional] |
| **endRev** | **String**|  | [optional] |

### Return type

[**CreateDiffHTMLUsingGET200Response**](CreateDiffHTMLUsingGET200Response.md)

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

<a id="createPadUsingGET"></a>
# **createPadUsingGET**
> AppendChatMessageUsingGET200Response createPadUsingGET(padID, text)



creates a new (non-group) pad. Note that if you need to create a group Pad, you should call createGroupPad

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    PadApi apiInstance = new PadApi(defaultClient);
    String padID = "padID_example"; // String | 
    String text = "text_example"; // String | 
    try {
      AppendChatMessageUsingGET200Response result = apiInstance.createPadUsingGET(padID, text);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PadApi#createPadUsingGET");
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
| **padID** | **String**|  | [optional] |
| **text** | **String**|  | [optional] |

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

<a id="createPadUsingPOST"></a>
# **createPadUsingPOST**
> AppendChatMessageUsingGET200Response createPadUsingPOST(padID, text)



creates a new (non-group) pad. Note that if you need to create a group Pad, you should call createGroupPad

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    PadApi apiInstance = new PadApi(defaultClient);
    String padID = "padID_example"; // String | 
    String text = "text_example"; // String | 
    try {
      AppendChatMessageUsingGET200Response result = apiInstance.createPadUsingPOST(padID, text);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PadApi#createPadUsingPOST");
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
| **padID** | **String**|  | [optional] |
| **text** | **String**|  | [optional] |

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

<a id="deletePadUsingGET"></a>
# **deletePadUsingGET**
> AppendChatMessageUsingGET200Response deletePadUsingGET(padID)

deletes a pad

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    PadApi apiInstance = new PadApi(defaultClient);
    String padID = "padID_example"; // String | 
    try {
      AppendChatMessageUsingGET200Response result = apiInstance.deletePadUsingGET(padID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PadApi#deletePadUsingGET");
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
| **padID** | **String**|  | [optional] |

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

<a id="deletePadUsingPOST"></a>
# **deletePadUsingPOST**
> AppendChatMessageUsingGET200Response deletePadUsingPOST(padID)

deletes a pad

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    PadApi apiInstance = new PadApi(defaultClient);
    String padID = "padID_example"; // String | 
    try {
      AppendChatMessageUsingGET200Response result = apiInstance.deletePadUsingPOST(padID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PadApi#deletePadUsingPOST");
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
| **padID** | **String**|  | [optional] |

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

<a id="getChatHeadUsingGET"></a>
# **getChatHeadUsingGET**
> GetChatHeadUsingGET200Response getChatHeadUsingGET(padID)

returns the chatHead (chat-message) of the pad

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    PadApi apiInstance = new PadApi(defaultClient);
    String padID = "padID_example"; // String | 
    try {
      GetChatHeadUsingGET200Response result = apiInstance.getChatHeadUsingGET(padID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PadApi#getChatHeadUsingGET");
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
| **padID** | **String**|  | [optional] |

### Return type

[**GetChatHeadUsingGET200Response**](GetChatHeadUsingGET200Response.md)

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

<a id="getChatHeadUsingPOST"></a>
# **getChatHeadUsingPOST**
> GetChatHeadUsingGET200Response getChatHeadUsingPOST(padID)

returns the chatHead (chat-message) of the pad

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    PadApi apiInstance = new PadApi(defaultClient);
    String padID = "padID_example"; // String | 
    try {
      GetChatHeadUsingGET200Response result = apiInstance.getChatHeadUsingPOST(padID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PadApi#getChatHeadUsingPOST");
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
| **padID** | **String**|  | [optional] |

### Return type

[**GetChatHeadUsingGET200Response**](GetChatHeadUsingGET200Response.md)

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

<a id="getChatHistoryUsingGET"></a>
# **getChatHistoryUsingGET**
> GetChatHistoryUsingGET200Response getChatHistoryUsingGET(padID, start, end)

returns the chat history

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    PadApi apiInstance = new PadApi(defaultClient);
    String padID = "padID_example"; // String | 
    String start = "start_example"; // String | 
    String end = "end_example"; // String | 
    try {
      GetChatHistoryUsingGET200Response result = apiInstance.getChatHistoryUsingGET(padID, start, end);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PadApi#getChatHistoryUsingGET");
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
| **padID** | **String**|  | [optional] |
| **start** | **String**|  | [optional] |
| **end** | **String**|  | [optional] |

### Return type

[**GetChatHistoryUsingGET200Response**](GetChatHistoryUsingGET200Response.md)

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

<a id="getChatHistoryUsingPOST"></a>
# **getChatHistoryUsingPOST**
> GetChatHistoryUsingGET200Response getChatHistoryUsingPOST(padID, start, end)

returns the chat history

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    PadApi apiInstance = new PadApi(defaultClient);
    String padID = "padID_example"; // String | 
    String start = "start_example"; // String | 
    String end = "end_example"; // String | 
    try {
      GetChatHistoryUsingGET200Response result = apiInstance.getChatHistoryUsingPOST(padID, start, end);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PadApi#getChatHistoryUsingPOST");
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
| **padID** | **String**|  | [optional] |
| **start** | **String**|  | [optional] |
| **end** | **String**|  | [optional] |

### Return type

[**GetChatHistoryUsingGET200Response**](GetChatHistoryUsingGET200Response.md)

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

<a id="getHTMLUsingGET"></a>
# **getHTMLUsingGET**
> GetHTMLUsingGET200Response getHTMLUsingGET(padID, rev)

returns the text of a pad formatted as HTML

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    PadApi apiInstance = new PadApi(defaultClient);
    String padID = "padID_example"; // String | 
    String rev = "rev_example"; // String | 
    try {
      GetHTMLUsingGET200Response result = apiInstance.getHTMLUsingGET(padID, rev);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PadApi#getHTMLUsingGET");
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
| **padID** | **String**|  | [optional] |
| **rev** | **String**|  | [optional] |

### Return type

[**GetHTMLUsingGET200Response**](GetHTMLUsingGET200Response.md)

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

<a id="getHTMLUsingPOST"></a>
# **getHTMLUsingPOST**
> GetHTMLUsingGET200Response getHTMLUsingPOST(padID, rev)

returns the text of a pad formatted as HTML

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    PadApi apiInstance = new PadApi(defaultClient);
    String padID = "padID_example"; // String | 
    String rev = "rev_example"; // String | 
    try {
      GetHTMLUsingGET200Response result = apiInstance.getHTMLUsingPOST(padID, rev);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PadApi#getHTMLUsingPOST");
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
| **padID** | **String**|  | [optional] |
| **rev** | **String**|  | [optional] |

### Return type

[**GetHTMLUsingGET200Response**](GetHTMLUsingGET200Response.md)

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

<a id="getLastEditedUsingGET"></a>
# **getLastEditedUsingGET**
> GetLastEditedUsingGET200Response getLastEditedUsingGET(padID)

returns the timestamp of the last revision of the pad

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    PadApi apiInstance = new PadApi(defaultClient);
    String padID = "padID_example"; // String | 
    try {
      GetLastEditedUsingGET200Response result = apiInstance.getLastEditedUsingGET(padID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PadApi#getLastEditedUsingGET");
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
| **padID** | **String**|  | [optional] |

### Return type

[**GetLastEditedUsingGET200Response**](GetLastEditedUsingGET200Response.md)

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

<a id="getLastEditedUsingPOST"></a>
# **getLastEditedUsingPOST**
> GetLastEditedUsingGET200Response getLastEditedUsingPOST(padID)

returns the timestamp of the last revision of the pad

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    PadApi apiInstance = new PadApi(defaultClient);
    String padID = "padID_example"; // String | 
    try {
      GetLastEditedUsingGET200Response result = apiInstance.getLastEditedUsingPOST(padID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PadApi#getLastEditedUsingPOST");
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
| **padID** | **String**|  | [optional] |

### Return type

[**GetLastEditedUsingGET200Response**](GetLastEditedUsingGET200Response.md)

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

<a id="getPublicStatusUsingGET"></a>
# **getPublicStatusUsingGET**
> GetPublicStatusUsingGET200Response getPublicStatusUsingGET(padID)

return true of false

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    PadApi apiInstance = new PadApi(defaultClient);
    String padID = "padID_example"; // String | 
    try {
      GetPublicStatusUsingGET200Response result = apiInstance.getPublicStatusUsingGET(padID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PadApi#getPublicStatusUsingGET");
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
| **padID** | **String**|  | [optional] |

### Return type

[**GetPublicStatusUsingGET200Response**](GetPublicStatusUsingGET200Response.md)

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

<a id="getPublicStatusUsingPOST"></a>
# **getPublicStatusUsingPOST**
> GetPublicStatusUsingGET200Response getPublicStatusUsingPOST(padID)

return true of false

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    PadApi apiInstance = new PadApi(defaultClient);
    String padID = "padID_example"; // String | 
    try {
      GetPublicStatusUsingGET200Response result = apiInstance.getPublicStatusUsingPOST(padID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PadApi#getPublicStatusUsingPOST");
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
| **padID** | **String**|  | [optional] |

### Return type

[**GetPublicStatusUsingGET200Response**](GetPublicStatusUsingGET200Response.md)

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

<a id="getReadOnlyIDUsingGET"></a>
# **getReadOnlyIDUsingGET**
> GetReadOnlyIDUsingGET200Response getReadOnlyIDUsingGET(padID)

returns the read only link of a pad

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    PadApi apiInstance = new PadApi(defaultClient);
    String padID = "padID_example"; // String | 
    try {
      GetReadOnlyIDUsingGET200Response result = apiInstance.getReadOnlyIDUsingGET(padID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PadApi#getReadOnlyIDUsingGET");
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
| **padID** | **String**|  | [optional] |

### Return type

[**GetReadOnlyIDUsingGET200Response**](GetReadOnlyIDUsingGET200Response.md)

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

<a id="getReadOnlyIDUsingPOST"></a>
# **getReadOnlyIDUsingPOST**
> GetReadOnlyIDUsingGET200Response getReadOnlyIDUsingPOST(padID)

returns the read only link of a pad

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    PadApi apiInstance = new PadApi(defaultClient);
    String padID = "padID_example"; // String | 
    try {
      GetReadOnlyIDUsingGET200Response result = apiInstance.getReadOnlyIDUsingPOST(padID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PadApi#getReadOnlyIDUsingPOST");
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
| **padID** | **String**|  | [optional] |

### Return type

[**GetReadOnlyIDUsingGET200Response**](GetReadOnlyIDUsingGET200Response.md)

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

<a id="getRevisionsCountUsingGET"></a>
# **getRevisionsCountUsingGET**
> GetRevisionsCountUsingGET200Response getRevisionsCountUsingGET(padID)

returns the number of revisions of this pad

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    PadApi apiInstance = new PadApi(defaultClient);
    String padID = "padID_example"; // String | 
    try {
      GetRevisionsCountUsingGET200Response result = apiInstance.getRevisionsCountUsingGET(padID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PadApi#getRevisionsCountUsingGET");
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
| **padID** | **String**|  | [optional] |

### Return type

[**GetRevisionsCountUsingGET200Response**](GetRevisionsCountUsingGET200Response.md)

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

<a id="getRevisionsCountUsingPOST"></a>
# **getRevisionsCountUsingPOST**
> GetRevisionsCountUsingGET200Response getRevisionsCountUsingPOST(padID)

returns the number of revisions of this pad

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    PadApi apiInstance = new PadApi(defaultClient);
    String padID = "padID_example"; // String | 
    try {
      GetRevisionsCountUsingGET200Response result = apiInstance.getRevisionsCountUsingPOST(padID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PadApi#getRevisionsCountUsingPOST");
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
| **padID** | **String**|  | [optional] |

### Return type

[**GetRevisionsCountUsingGET200Response**](GetRevisionsCountUsingGET200Response.md)

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

<a id="getTextUsingGET"></a>
# **getTextUsingGET**
> GetTextUsingGET200Response getTextUsingGET(padID, rev)

returns the text of a pad

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    PadApi apiInstance = new PadApi(defaultClient);
    String padID = "padID_example"; // String | 
    String rev = "rev_example"; // String | 
    try {
      GetTextUsingGET200Response result = apiInstance.getTextUsingGET(padID, rev);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PadApi#getTextUsingGET");
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
| **padID** | **String**|  | [optional] |
| **rev** | **String**|  | [optional] |

### Return type

[**GetTextUsingGET200Response**](GetTextUsingGET200Response.md)

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

<a id="getTextUsingPOST"></a>
# **getTextUsingPOST**
> GetTextUsingGET200Response getTextUsingPOST(padID, rev)

returns the text of a pad

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    PadApi apiInstance = new PadApi(defaultClient);
    String padID = "padID_example"; // String | 
    String rev = "rev_example"; // String | 
    try {
      GetTextUsingGET200Response result = apiInstance.getTextUsingPOST(padID, rev);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PadApi#getTextUsingPOST");
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
| **padID** | **String**|  | [optional] |
| **rev** | **String**|  | [optional] |

### Return type

[**GetTextUsingGET200Response**](GetTextUsingGET200Response.md)

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

<a id="listAllPadsUsingGET"></a>
# **listAllPadsUsingGET**
> ListAllPadsUsingGET200Response listAllPadsUsingGET()

list all the pads

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    PadApi apiInstance = new PadApi(defaultClient);
    try {
      ListAllPadsUsingGET200Response result = apiInstance.listAllPadsUsingGET();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PadApi#listAllPadsUsingGET");
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

<a id="listAllPadsUsingPOST"></a>
# **listAllPadsUsingPOST**
> ListAllPadsUsingGET200Response listAllPadsUsingPOST()

list all the pads

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    PadApi apiInstance = new PadApi(defaultClient);
    try {
      ListAllPadsUsingGET200Response result = apiInstance.listAllPadsUsingPOST();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PadApi#listAllPadsUsingPOST");
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

<a id="listAuthorsOfPadUsingGET"></a>
# **listAuthorsOfPadUsingGET**
> ListAuthorsOfPadUsingGET200Response listAuthorsOfPadUsingGET(padID)

returns an array of authors who contributed to this pad

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    PadApi apiInstance = new PadApi(defaultClient);
    String padID = "padID_example"; // String | 
    try {
      ListAuthorsOfPadUsingGET200Response result = apiInstance.listAuthorsOfPadUsingGET(padID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PadApi#listAuthorsOfPadUsingGET");
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
| **padID** | **String**|  | [optional] |

### Return type

[**ListAuthorsOfPadUsingGET200Response**](ListAuthorsOfPadUsingGET200Response.md)

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

<a id="listAuthorsOfPadUsingPOST"></a>
# **listAuthorsOfPadUsingPOST**
> ListAuthorsOfPadUsingGET200Response listAuthorsOfPadUsingPOST(padID)

returns an array of authors who contributed to this pad

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    PadApi apiInstance = new PadApi(defaultClient);
    String padID = "padID_example"; // String | 
    try {
      ListAuthorsOfPadUsingGET200Response result = apiInstance.listAuthorsOfPadUsingPOST(padID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PadApi#listAuthorsOfPadUsingPOST");
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
| **padID** | **String**|  | [optional] |

### Return type

[**ListAuthorsOfPadUsingGET200Response**](ListAuthorsOfPadUsingGET200Response.md)

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

<a id="padUsersCountUsingGET"></a>
# **padUsersCountUsingGET**
> PadUsersCountUsingGET200Response padUsersCountUsingGET(padID)

returns the number of user that are currently editing this pad

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    PadApi apiInstance = new PadApi(defaultClient);
    String padID = "padID_example"; // String | 
    try {
      PadUsersCountUsingGET200Response result = apiInstance.padUsersCountUsingGET(padID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PadApi#padUsersCountUsingGET");
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
| **padID** | **String**|  | [optional] |

### Return type

[**PadUsersCountUsingGET200Response**](PadUsersCountUsingGET200Response.md)

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

<a id="padUsersCountUsingPOST"></a>
# **padUsersCountUsingPOST**
> PadUsersCountUsingGET200Response padUsersCountUsingPOST(padID)

returns the number of user that are currently editing this pad

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    PadApi apiInstance = new PadApi(defaultClient);
    String padID = "padID_example"; // String | 
    try {
      PadUsersCountUsingGET200Response result = apiInstance.padUsersCountUsingPOST(padID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PadApi#padUsersCountUsingPOST");
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
| **padID** | **String**|  | [optional] |

### Return type

[**PadUsersCountUsingGET200Response**](PadUsersCountUsingGET200Response.md)

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

<a id="padUsersUsingGET"></a>
# **padUsersUsingGET**
> PadUsersUsingGET200Response padUsersUsingGET(padID)

returns the list of users that are currently editing this pad

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    PadApi apiInstance = new PadApi(defaultClient);
    String padID = "padID_example"; // String | 
    try {
      PadUsersUsingGET200Response result = apiInstance.padUsersUsingGET(padID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PadApi#padUsersUsingGET");
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
| **padID** | **String**|  | [optional] |

### Return type

[**PadUsersUsingGET200Response**](PadUsersUsingGET200Response.md)

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

<a id="padUsersUsingPOST"></a>
# **padUsersUsingPOST**
> PadUsersUsingGET200Response padUsersUsingPOST(padID)

returns the list of users that are currently editing this pad

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    PadApi apiInstance = new PadApi(defaultClient);
    String padID = "padID_example"; // String | 
    try {
      PadUsersUsingGET200Response result = apiInstance.padUsersUsingPOST(padID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PadApi#padUsersUsingPOST");
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
| **padID** | **String**|  | [optional] |

### Return type

[**PadUsersUsingGET200Response**](PadUsersUsingGET200Response.md)

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

<a id="sendClientsMessageUsingGET"></a>
# **sendClientsMessageUsingGET**
> AppendChatMessageUsingGET200Response sendClientsMessageUsingGET(padID, msg)

sends a custom message of type msg to the pad

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    PadApi apiInstance = new PadApi(defaultClient);
    String padID = "padID_example"; // String | 
    String msg = "msg_example"; // String | 
    try {
      AppendChatMessageUsingGET200Response result = apiInstance.sendClientsMessageUsingGET(padID, msg);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PadApi#sendClientsMessageUsingGET");
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
| **padID** | **String**|  | [optional] |
| **msg** | **String**|  | [optional] |

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

<a id="sendClientsMessageUsingPOST"></a>
# **sendClientsMessageUsingPOST**
> AppendChatMessageUsingGET200Response sendClientsMessageUsingPOST(padID, msg)

sends a custom message of type msg to the pad

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    PadApi apiInstance = new PadApi(defaultClient);
    String padID = "padID_example"; // String | 
    String msg = "msg_example"; // String | 
    try {
      AppendChatMessageUsingGET200Response result = apiInstance.sendClientsMessageUsingPOST(padID, msg);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PadApi#sendClientsMessageUsingPOST");
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
| **padID** | **String**|  | [optional] |
| **msg** | **String**|  | [optional] |

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

<a id="setHTMLUsingGET"></a>
# **setHTMLUsingGET**
> AppendChatMessageUsingGET200Response setHTMLUsingGET(padID, html)

sets the text of a pad with HTML

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    PadApi apiInstance = new PadApi(defaultClient);
    String padID = "padID_example"; // String | 
    String html = "html_example"; // String | 
    try {
      AppendChatMessageUsingGET200Response result = apiInstance.setHTMLUsingGET(padID, html);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PadApi#setHTMLUsingGET");
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
| **padID** | **String**|  | [optional] |
| **html** | **String**|  | [optional] |

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

<a id="setHTMLUsingPOST"></a>
# **setHTMLUsingPOST**
> AppendChatMessageUsingGET200Response setHTMLUsingPOST(padID, html)

sets the text of a pad with HTML

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    PadApi apiInstance = new PadApi(defaultClient);
    String padID = "padID_example"; // String | 
    String html = "html_example"; // String | 
    try {
      AppendChatMessageUsingGET200Response result = apiInstance.setHTMLUsingPOST(padID, html);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PadApi#setHTMLUsingPOST");
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
| **padID** | **String**|  | [optional] |
| **html** | **String**|  | [optional] |

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

<a id="setPublicStatusUsingGET"></a>
# **setPublicStatusUsingGET**
> AppendChatMessageUsingGET200Response setPublicStatusUsingGET(padID, publicStatus)

sets a boolean for the public status of a pad

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    PadApi apiInstance = new PadApi(defaultClient);
    String padID = "padID_example"; // String | 
    String publicStatus = "publicStatus_example"; // String | 
    try {
      AppendChatMessageUsingGET200Response result = apiInstance.setPublicStatusUsingGET(padID, publicStatus);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PadApi#setPublicStatusUsingGET");
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
| **padID** | **String**|  | [optional] |
| **publicStatus** | **String**|  | [optional] |

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

<a id="setPublicStatusUsingPOST"></a>
# **setPublicStatusUsingPOST**
> AppendChatMessageUsingGET200Response setPublicStatusUsingPOST(padID, publicStatus)

sets a boolean for the public status of a pad

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    PadApi apiInstance = new PadApi(defaultClient);
    String padID = "padID_example"; // String | 
    String publicStatus = "publicStatus_example"; // String | 
    try {
      AppendChatMessageUsingGET200Response result = apiInstance.setPublicStatusUsingPOST(padID, publicStatus);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PadApi#setPublicStatusUsingPOST");
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
| **padID** | **String**|  | [optional] |
| **publicStatus** | **String**|  | [optional] |

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

<a id="setTextUsingGET"></a>
# **setTextUsingGET**
> AppendChatMessageUsingGET200Response setTextUsingGET(padID, text)

sets the text of a pad

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    PadApi apiInstance = new PadApi(defaultClient);
    String padID = "padID_example"; // String | 
    String text = "text_example"; // String | 
    try {
      AppendChatMessageUsingGET200Response result = apiInstance.setTextUsingGET(padID, text);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PadApi#setTextUsingGET");
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
| **padID** | **String**|  | [optional] |
| **text** | **String**|  | [optional] |

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

<a id="setTextUsingPOST"></a>
# **setTextUsingPOST**
> AppendChatMessageUsingGET200Response setTextUsingPOST(padID, text)

sets the text of a pad

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    PadApi apiInstance = new PadApi(defaultClient);
    String padID = "padID_example"; // String | 
    String text = "text_example"; // String | 
    try {
      AppendChatMessageUsingGET200Response result = apiInstance.setTextUsingPOST(padID, text);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PadApi#setTextUsingPOST");
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
| **padID** | **String**|  | [optional] |
| **text** | **String**|  | [optional] |

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

