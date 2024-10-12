# GroupApi

All URIs are relative to *http://etherpad.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createGroupIfNotExistsForUsingGET**](GroupApi.md#createGroupIfNotExistsForUsingGET) | **GET** /createGroupIfNotExistsFor | this functions helps you to map your application group ids to Etherpad group ids |
| [**createGroupIfNotExistsForUsingPOST**](GroupApi.md#createGroupIfNotExistsForUsingPOST) | **POST** /createGroupIfNotExistsFor | this functions helps you to map your application group ids to Etherpad group ids |
| [**createGroupPadUsingGET**](GroupApi.md#createGroupPadUsingGET) | **GET** /createGroupPad | creates a new pad in this group |
| [**createGroupPadUsingPOST**](GroupApi.md#createGroupPadUsingPOST) | **POST** /createGroupPad | creates a new pad in this group |
| [**createGroupUsingGET**](GroupApi.md#createGroupUsingGET) | **GET** /createGroup | creates a new group |
| [**createGroupUsingPOST**](GroupApi.md#createGroupUsingPOST) | **POST** /createGroup | creates a new group |
| [**deleteGroupUsingGET**](GroupApi.md#deleteGroupUsingGET) | **GET** /deleteGroup | deletes a group |
| [**deleteGroupUsingPOST**](GroupApi.md#deleteGroupUsingPOST) | **POST** /deleteGroup | deletes a group |
| [**listAllGroupsUsingGET**](GroupApi.md#listAllGroupsUsingGET) | **GET** /listAllGroups |  |
| [**listAllGroupsUsingPOST**](GroupApi.md#listAllGroupsUsingPOST) | **POST** /listAllGroups |  |
| [**listPadsUsingGET**](GroupApi.md#listPadsUsingGET) | **GET** /listPads | returns all pads of this group |
| [**listPadsUsingPOST**](GroupApi.md#listPadsUsingPOST) | **POST** /listPads | returns all pads of this group |
| [**listSessionsOfGroupUsingGET**](GroupApi.md#listSessionsOfGroupUsingGET) | **GET** /listSessionsOfGroup |  |
| [**listSessionsOfGroupUsingPOST**](GroupApi.md#listSessionsOfGroupUsingPOST) | **POST** /listSessionsOfGroup |  |


<a id="createGroupIfNotExistsForUsingGET"></a>
# **createGroupIfNotExistsForUsingGET**
> CreateGroupUsingGET200Response createGroupIfNotExistsForUsingGET(groupMapper)

this functions helps you to map your application group ids to Etherpad group ids

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    GroupApi apiInstance = new GroupApi(defaultClient);
    String groupMapper = "groupMapper_example"; // String | 
    try {
      CreateGroupUsingGET200Response result = apiInstance.createGroupIfNotExistsForUsingGET(groupMapper);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupApi#createGroupIfNotExistsForUsingGET");
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
| **groupMapper** | **String**|  | [optional] |

### Return type

[**CreateGroupUsingGET200Response**](CreateGroupUsingGET200Response.md)

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

<a id="createGroupIfNotExistsForUsingPOST"></a>
# **createGroupIfNotExistsForUsingPOST**
> CreateGroupUsingGET200Response createGroupIfNotExistsForUsingPOST(groupMapper)

this functions helps you to map your application group ids to Etherpad group ids

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    GroupApi apiInstance = new GroupApi(defaultClient);
    String groupMapper = "groupMapper_example"; // String | 
    try {
      CreateGroupUsingGET200Response result = apiInstance.createGroupIfNotExistsForUsingPOST(groupMapper);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupApi#createGroupIfNotExistsForUsingPOST");
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
| **groupMapper** | **String**|  | [optional] |

### Return type

[**CreateGroupUsingGET200Response**](CreateGroupUsingGET200Response.md)

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

<a id="createGroupPadUsingGET"></a>
# **createGroupPadUsingGET**
> AppendChatMessageUsingGET200Response createGroupPadUsingGET(groupID, padName, text)

creates a new pad in this group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    GroupApi apiInstance = new GroupApi(defaultClient);
    String groupID = "groupID_example"; // String | 
    String padName = "padName_example"; // String | 
    String text = "text_example"; // String | 
    try {
      AppendChatMessageUsingGET200Response result = apiInstance.createGroupPadUsingGET(groupID, padName, text);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupApi#createGroupPadUsingGET");
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
| **padName** | **String**|  | [optional] |
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

<a id="createGroupPadUsingPOST"></a>
# **createGroupPadUsingPOST**
> AppendChatMessageUsingGET200Response createGroupPadUsingPOST(groupID, padName, text)

creates a new pad in this group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    GroupApi apiInstance = new GroupApi(defaultClient);
    String groupID = "groupID_example"; // String | 
    String padName = "padName_example"; // String | 
    String text = "text_example"; // String | 
    try {
      AppendChatMessageUsingGET200Response result = apiInstance.createGroupPadUsingPOST(groupID, padName, text);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupApi#createGroupPadUsingPOST");
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
| **padName** | **String**|  | [optional] |
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

<a id="createGroupUsingGET"></a>
# **createGroupUsingGET**
> CreateGroupUsingGET200Response createGroupUsingGET()

creates a new group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    GroupApi apiInstance = new GroupApi(defaultClient);
    try {
      CreateGroupUsingGET200Response result = apiInstance.createGroupUsingGET();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupApi#createGroupUsingGET");
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

[**CreateGroupUsingGET200Response**](CreateGroupUsingGET200Response.md)

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

<a id="createGroupUsingPOST"></a>
# **createGroupUsingPOST**
> CreateGroupUsingGET200Response createGroupUsingPOST()

creates a new group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    GroupApi apiInstance = new GroupApi(defaultClient);
    try {
      CreateGroupUsingGET200Response result = apiInstance.createGroupUsingPOST();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupApi#createGroupUsingPOST");
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

[**CreateGroupUsingGET200Response**](CreateGroupUsingGET200Response.md)

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

<a id="deleteGroupUsingGET"></a>
# **deleteGroupUsingGET**
> AppendChatMessageUsingGET200Response deleteGroupUsingGET(groupID)

deletes a group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    GroupApi apiInstance = new GroupApi(defaultClient);
    String groupID = "groupID_example"; // String | 
    try {
      AppendChatMessageUsingGET200Response result = apiInstance.deleteGroupUsingGET(groupID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupApi#deleteGroupUsingGET");
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

<a id="deleteGroupUsingPOST"></a>
# **deleteGroupUsingPOST**
> AppendChatMessageUsingGET200Response deleteGroupUsingPOST(groupID)

deletes a group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    GroupApi apiInstance = new GroupApi(defaultClient);
    String groupID = "groupID_example"; // String | 
    try {
      AppendChatMessageUsingGET200Response result = apiInstance.deleteGroupUsingPOST(groupID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupApi#deleteGroupUsingPOST");
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

<a id="listAllGroupsUsingGET"></a>
# **listAllGroupsUsingGET**
> ListAllGroupsUsingGET200Response listAllGroupsUsingGET()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    GroupApi apiInstance = new GroupApi(defaultClient);
    try {
      ListAllGroupsUsingGET200Response result = apiInstance.listAllGroupsUsingGET();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupApi#listAllGroupsUsingGET");
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

[**ListAllGroupsUsingGET200Response**](ListAllGroupsUsingGET200Response.md)

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

<a id="listAllGroupsUsingPOST"></a>
# **listAllGroupsUsingPOST**
> ListAllGroupsUsingGET200Response listAllGroupsUsingPOST()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    GroupApi apiInstance = new GroupApi(defaultClient);
    try {
      ListAllGroupsUsingGET200Response result = apiInstance.listAllGroupsUsingPOST();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupApi#listAllGroupsUsingPOST");
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

[**ListAllGroupsUsingGET200Response**](ListAllGroupsUsingGET200Response.md)

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

<a id="listPadsUsingGET"></a>
# **listPadsUsingGET**
> ListAllPadsUsingGET200Response listPadsUsingGET(groupID)

returns all pads of this group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    GroupApi apiInstance = new GroupApi(defaultClient);
    String groupID = "groupID_example"; // String | 
    try {
      ListAllPadsUsingGET200Response result = apiInstance.listPadsUsingGET(groupID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupApi#listPadsUsingGET");
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

<a id="listPadsUsingPOST"></a>
# **listPadsUsingPOST**
> ListAllPadsUsingGET200Response listPadsUsingPOST(groupID)

returns all pads of this group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    GroupApi apiInstance = new GroupApi(defaultClient);
    String groupID = "groupID_example"; // String | 
    try {
      ListAllPadsUsingGET200Response result = apiInstance.listPadsUsingPOST(groupID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupApi#listPadsUsingPOST");
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

<a id="listSessionsOfGroupUsingGET"></a>
# **listSessionsOfGroupUsingGET**
> ListSessionsOfAuthorUsingGET200Response listSessionsOfGroupUsingGET(groupID)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    GroupApi apiInstance = new GroupApi(defaultClient);
    String groupID = "groupID_example"; // String | 
    try {
      ListSessionsOfAuthorUsingGET200Response result = apiInstance.listSessionsOfGroupUsingGET(groupID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupApi#listSessionsOfGroupUsingGET");
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

<a id="listSessionsOfGroupUsingPOST"></a>
# **listSessionsOfGroupUsingPOST**
> ListSessionsOfAuthorUsingGET200Response listSessionsOfGroupUsingPOST(groupID)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://etherpad.local");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    GroupApi apiInstance = new GroupApi(defaultClient);
    String groupID = "groupID_example"; // String | 
    try {
      ListSessionsOfAuthorUsingGET200Response result = apiInstance.listSessionsOfGroupUsingPOST(groupID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupApi#listSessionsOfGroupUsingPOST");
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

