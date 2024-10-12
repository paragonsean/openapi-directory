# DefaultApi

All URIs are relative to *http://etherpad.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**appendTextUsingGET**](DefaultApi.md#appendTextUsingGET) | **GET** /appendText |  |
| [**appendTextUsingPOST**](DefaultApi.md#appendTextUsingPOST) | **POST** /appendText |  |
| [**copyPadUsingGET**](DefaultApi.md#copyPadUsingGET) | **GET** /copyPad |  |
| [**copyPadUsingPOST**](DefaultApi.md#copyPadUsingPOST) | **POST** /copyPad |  |
| [**copyPadWithoutHistoryUsingGET**](DefaultApi.md#copyPadWithoutHistoryUsingGET) | **GET** /copyPadWithoutHistory |  |
| [**copyPadWithoutHistoryUsingPOST**](DefaultApi.md#copyPadWithoutHistoryUsingPOST) | **POST** /copyPadWithoutHistory |  |
| [**getAttributePoolUsingGET**](DefaultApi.md#getAttributePoolUsingGET) | **GET** /getAttributePool |  |
| [**getAttributePoolUsingPOST**](DefaultApi.md#getAttributePoolUsingPOST) | **POST** /getAttributePool |  |
| [**getPadIDUsingGET**](DefaultApi.md#getPadIDUsingGET) | **GET** /getPadID |  |
| [**getPadIDUsingPOST**](DefaultApi.md#getPadIDUsingPOST) | **POST** /getPadID |  |
| [**getRevisionChangesetUsingGET**](DefaultApi.md#getRevisionChangesetUsingGET) | **GET** /getRevisionChangeset |  |
| [**getRevisionChangesetUsingPOST**](DefaultApi.md#getRevisionChangesetUsingPOST) | **POST** /getRevisionChangeset |  |
| [**getSavedRevisionsCountUsingGET**](DefaultApi.md#getSavedRevisionsCountUsingGET) | **GET** /getSavedRevisionsCount |  |
| [**getSavedRevisionsCountUsingPOST**](DefaultApi.md#getSavedRevisionsCountUsingPOST) | **POST** /getSavedRevisionsCount |  |
| [**getStatsUsingGET**](DefaultApi.md#getStatsUsingGET) | **GET** /getStats |  |
| [**getStatsUsingPOST**](DefaultApi.md#getStatsUsingPOST) | **POST** /getStats |  |
| [**listSavedRevisionsUsingGET**](DefaultApi.md#listSavedRevisionsUsingGET) | **GET** /listSavedRevisions |  |
| [**listSavedRevisionsUsingPOST**](DefaultApi.md#listSavedRevisionsUsingPOST) | **POST** /listSavedRevisions |  |
| [**movePadUsingGET**](DefaultApi.md#movePadUsingGET) | **GET** /movePad |  |
| [**movePadUsingPOST**](DefaultApi.md#movePadUsingPOST) | **POST** /movePad |  |
| [**restoreRevisionUsingGET**](DefaultApi.md#restoreRevisionUsingGET) | **GET** /restoreRevision |  |
| [**restoreRevisionUsingPOST**](DefaultApi.md#restoreRevisionUsingPOST) | **POST** /restoreRevision |  |
| [**saveRevisionUsingGET**](DefaultApi.md#saveRevisionUsingGET) | **GET** /saveRevision |  |
| [**saveRevisionUsingPOST**](DefaultApi.md#saveRevisionUsingPOST) | **POST** /saveRevision |  |


<a id="appendTextUsingGET"></a>
# **appendTextUsingGET**
> AppendChatMessageUsingGET200Response appendTextUsingGET(padID, text)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String padID = "padID_example"; // String | 
    String text = "text_example"; // String | 
    try {
      AppendChatMessageUsingGET200Response result = apiInstance.appendTextUsingGET(padID, text);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#appendTextUsingGET");
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

<a id="appendTextUsingPOST"></a>
# **appendTextUsingPOST**
> AppendChatMessageUsingGET200Response appendTextUsingPOST(padID, text)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String padID = "padID_example"; // String | 
    String text = "text_example"; // String | 
    try {
      AppendChatMessageUsingGET200Response result = apiInstance.appendTextUsingPOST(padID, text);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#appendTextUsingPOST");
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

<a id="copyPadUsingGET"></a>
# **copyPadUsingGET**
> AppendChatMessageUsingGET200Response copyPadUsingGET(sourceID, destinationID, force)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String sourceID = "sourceID_example"; // String | 
    String destinationID = "destinationID_example"; // String | 
    String force = "force_example"; // String | 
    try {
      AppendChatMessageUsingGET200Response result = apiInstance.copyPadUsingGET(sourceID, destinationID, force);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#copyPadUsingGET");
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
| **sourceID** | **String**|  | [optional] |
| **destinationID** | **String**|  | [optional] |
| **force** | **String**|  | [optional] |

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

<a id="copyPadUsingPOST"></a>
# **copyPadUsingPOST**
> AppendChatMessageUsingGET200Response copyPadUsingPOST(sourceID, destinationID, force)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String sourceID = "sourceID_example"; // String | 
    String destinationID = "destinationID_example"; // String | 
    String force = "force_example"; // String | 
    try {
      AppendChatMessageUsingGET200Response result = apiInstance.copyPadUsingPOST(sourceID, destinationID, force);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#copyPadUsingPOST");
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
| **sourceID** | **String**|  | [optional] |
| **destinationID** | **String**|  | [optional] |
| **force** | **String**|  | [optional] |

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

<a id="copyPadWithoutHistoryUsingGET"></a>
# **copyPadWithoutHistoryUsingGET**
> AppendChatMessageUsingGET200Response copyPadWithoutHistoryUsingGET(sourceID, destinationID, force)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String sourceID = "sourceID_example"; // String | 
    String destinationID = "destinationID_example"; // String | 
    String force = "force_example"; // String | 
    try {
      AppendChatMessageUsingGET200Response result = apiInstance.copyPadWithoutHistoryUsingGET(sourceID, destinationID, force);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#copyPadWithoutHistoryUsingGET");
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
| **sourceID** | **String**|  | [optional] |
| **destinationID** | **String**|  | [optional] |
| **force** | **String**|  | [optional] |

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

<a id="copyPadWithoutHistoryUsingPOST"></a>
# **copyPadWithoutHistoryUsingPOST**
> AppendChatMessageUsingGET200Response copyPadWithoutHistoryUsingPOST(sourceID, destinationID, force)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String sourceID = "sourceID_example"; // String | 
    String destinationID = "destinationID_example"; // String | 
    String force = "force_example"; // String | 
    try {
      AppendChatMessageUsingGET200Response result = apiInstance.copyPadWithoutHistoryUsingPOST(sourceID, destinationID, force);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#copyPadWithoutHistoryUsingPOST");
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
| **sourceID** | **String**|  | [optional] |
| **destinationID** | **String**|  | [optional] |
| **force** | **String**|  | [optional] |

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

<a id="getAttributePoolUsingGET"></a>
# **getAttributePoolUsingGET**
> AppendChatMessageUsingGET200Response getAttributePoolUsingGET(padID)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String padID = "padID_example"; // String | 
    try {
      AppendChatMessageUsingGET200Response result = apiInstance.getAttributePoolUsingGET(padID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getAttributePoolUsingGET");
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

<a id="getAttributePoolUsingPOST"></a>
# **getAttributePoolUsingPOST**
> AppendChatMessageUsingGET200Response getAttributePoolUsingPOST(padID)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String padID = "padID_example"; // String | 
    try {
      AppendChatMessageUsingGET200Response result = apiInstance.getAttributePoolUsingPOST(padID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getAttributePoolUsingPOST");
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

<a id="getPadIDUsingGET"></a>
# **getPadIDUsingGET**
> AppendChatMessageUsingGET200Response getPadIDUsingGET(roID)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String roID = "roID_example"; // String | 
    try {
      AppendChatMessageUsingGET200Response result = apiInstance.getPadIDUsingGET(roID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getPadIDUsingGET");
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
| **roID** | **String**|  | [optional] |

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

<a id="getPadIDUsingPOST"></a>
# **getPadIDUsingPOST**
> AppendChatMessageUsingGET200Response getPadIDUsingPOST(roID)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String roID = "roID_example"; // String | 
    try {
      AppendChatMessageUsingGET200Response result = apiInstance.getPadIDUsingPOST(roID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getPadIDUsingPOST");
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
| **roID** | **String**|  | [optional] |

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

<a id="getRevisionChangesetUsingGET"></a>
# **getRevisionChangesetUsingGET**
> AppendChatMessageUsingGET200Response getRevisionChangesetUsingGET(padID, rev)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String padID = "padID_example"; // String | 
    String rev = "rev_example"; // String | 
    try {
      AppendChatMessageUsingGET200Response result = apiInstance.getRevisionChangesetUsingGET(padID, rev);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getRevisionChangesetUsingGET");
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

<a id="getRevisionChangesetUsingPOST"></a>
# **getRevisionChangesetUsingPOST**
> AppendChatMessageUsingGET200Response getRevisionChangesetUsingPOST(padID, rev)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String padID = "padID_example"; // String | 
    String rev = "rev_example"; // String | 
    try {
      AppendChatMessageUsingGET200Response result = apiInstance.getRevisionChangesetUsingPOST(padID, rev);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getRevisionChangesetUsingPOST");
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

<a id="getSavedRevisionsCountUsingGET"></a>
# **getSavedRevisionsCountUsingGET**
> AppendChatMessageUsingGET200Response getSavedRevisionsCountUsingGET(padID)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String padID = "padID_example"; // String | 
    try {
      AppendChatMessageUsingGET200Response result = apiInstance.getSavedRevisionsCountUsingGET(padID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getSavedRevisionsCountUsingGET");
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

<a id="getSavedRevisionsCountUsingPOST"></a>
# **getSavedRevisionsCountUsingPOST**
> AppendChatMessageUsingGET200Response getSavedRevisionsCountUsingPOST(padID)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String padID = "padID_example"; // String | 
    try {
      AppendChatMessageUsingGET200Response result = apiInstance.getSavedRevisionsCountUsingPOST(padID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getSavedRevisionsCountUsingPOST");
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

<a id="getStatsUsingGET"></a>
# **getStatsUsingGET**
> AppendChatMessageUsingGET200Response getStatsUsingGET()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      AppendChatMessageUsingGET200Response result = apiInstance.getStatsUsingGET();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getStatsUsingGET");
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

<a id="getStatsUsingPOST"></a>
# **getStatsUsingPOST**
> AppendChatMessageUsingGET200Response getStatsUsingPOST()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      AppendChatMessageUsingGET200Response result = apiInstance.getStatsUsingPOST();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getStatsUsingPOST");
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

<a id="listSavedRevisionsUsingGET"></a>
# **listSavedRevisionsUsingGET**
> AppendChatMessageUsingGET200Response listSavedRevisionsUsingGET(padID)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String padID = "padID_example"; // String | 
    try {
      AppendChatMessageUsingGET200Response result = apiInstance.listSavedRevisionsUsingGET(padID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listSavedRevisionsUsingGET");
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

<a id="listSavedRevisionsUsingPOST"></a>
# **listSavedRevisionsUsingPOST**
> AppendChatMessageUsingGET200Response listSavedRevisionsUsingPOST(padID)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String padID = "padID_example"; // String | 
    try {
      AppendChatMessageUsingGET200Response result = apiInstance.listSavedRevisionsUsingPOST(padID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listSavedRevisionsUsingPOST");
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

<a id="movePadUsingGET"></a>
# **movePadUsingGET**
> AppendChatMessageUsingGET200Response movePadUsingGET(sourceID, destinationID, force)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String sourceID = "sourceID_example"; // String | 
    String destinationID = "destinationID_example"; // String | 
    String force = "force_example"; // String | 
    try {
      AppendChatMessageUsingGET200Response result = apiInstance.movePadUsingGET(sourceID, destinationID, force);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#movePadUsingGET");
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
| **sourceID** | **String**|  | [optional] |
| **destinationID** | **String**|  | [optional] |
| **force** | **String**|  | [optional] |

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

<a id="movePadUsingPOST"></a>
# **movePadUsingPOST**
> AppendChatMessageUsingGET200Response movePadUsingPOST(sourceID, destinationID, force)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String sourceID = "sourceID_example"; // String | 
    String destinationID = "destinationID_example"; // String | 
    String force = "force_example"; // String | 
    try {
      AppendChatMessageUsingGET200Response result = apiInstance.movePadUsingPOST(sourceID, destinationID, force);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#movePadUsingPOST");
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
| **sourceID** | **String**|  | [optional] |
| **destinationID** | **String**|  | [optional] |
| **force** | **String**|  | [optional] |

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

<a id="restoreRevisionUsingGET"></a>
# **restoreRevisionUsingGET**
> AppendChatMessageUsingGET200Response restoreRevisionUsingGET(padID, rev)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String padID = "padID_example"; // String | 
    String rev = "rev_example"; // String | 
    try {
      AppendChatMessageUsingGET200Response result = apiInstance.restoreRevisionUsingGET(padID, rev);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#restoreRevisionUsingGET");
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

<a id="restoreRevisionUsingPOST"></a>
# **restoreRevisionUsingPOST**
> AppendChatMessageUsingGET200Response restoreRevisionUsingPOST(padID, rev)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String padID = "padID_example"; // String | 
    String rev = "rev_example"; // String | 
    try {
      AppendChatMessageUsingGET200Response result = apiInstance.restoreRevisionUsingPOST(padID, rev);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#restoreRevisionUsingPOST");
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

<a id="saveRevisionUsingGET"></a>
# **saveRevisionUsingGET**
> AppendChatMessageUsingGET200Response saveRevisionUsingGET(padID, rev)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String padID = "padID_example"; // String | 
    String rev = "rev_example"; // String | 
    try {
      AppendChatMessageUsingGET200Response result = apiInstance.saveRevisionUsingGET(padID, rev);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#saveRevisionUsingGET");
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

<a id="saveRevisionUsingPOST"></a>
# **saveRevisionUsingPOST**
> AppendChatMessageUsingGET200Response saveRevisionUsingPOST(padID, rev)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String padID = "padID_example"; // String | 
    String rev = "rev_example"; // String | 
    try {
      AppendChatMessageUsingGET200Response result = apiInstance.saveRevisionUsingPOST(padID, rev);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#saveRevisionUsingPOST");
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

