# UserDefinedTagApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createUserDefinedTag**](UserDefinedTagApi.md#createUserDefinedTag) | **POST** /user_defined_tag | Create a user-defined resource tag for tagging cloud compute resources |
| [**deleteUserDefinedTag**](UserDefinedTagApi.md#deleteUserDefinedTag) | **DELETE** /user_defined_tag/{id} | Delete a user-defined resource tag |
| [**deleteUserDefinedTagBulk**](UserDefinedTagApi.md#deleteUserDefinedTagBulk) | **DELETE** /user_defined_tag | Delete a list of user-defined resource tags |
| [**getUserDefinedTag**](UserDefinedTagApi.md#getUserDefinedTag) | **GET** /user_defined_tag/{id} | Get user-defined tag |
| [**queryUserDefinedTag**](UserDefinedTagApi.md#queryUserDefinedTag) | **GET** /user_defined_tag | Get user-defined resource tags |
| [**updateUserDefinedTag**](UserDefinedTagApi.md#updateUserDefinedTag) | **PATCH** /user_defined_tag/{id} | Update the value of a user-defined resource tag |


<a id="createUserDefinedTag"></a>
# **createUserDefinedTag**
> ResourceTagDetail createUserDefinedTag(resourceTagDefinition)

Create a user-defined resource tag for tagging cloud compute resources

Create a user-defined resource tag for tagging cloud compute resources created by CloudOn and CloutOut. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserDefinedTagApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    UserDefinedTagApi apiInstance = new UserDefinedTagApi(defaultClient);
    ResourceTagDefinition resourceTagDefinition = new ResourceTagDefinition(); // ResourceTagDefinition | The definition of a new user-defined resource tag to be created. 
    try {
      ResourceTagDetail result = apiInstance.createUserDefinedTag(resourceTagDefinition);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserDefinedTagApi#createUserDefinedTag");
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
| **resourceTagDefinition** | [**ResourceTagDefinition**](ResourceTagDefinition.md)| The definition of a new user-defined resource tag to be created.  | |

### Return type

[**ResourceTagDetail**](ResourceTagDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return the successfully created ResourceTag details. |  -  |

<a id="deleteUserDefinedTag"></a>
# **deleteUserDefinedTag**
> deleteUserDefinedTag(id)

Delete a user-defined resource tag

Delete a user-defined resource tag.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserDefinedTagApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    UserDefinedTagApi apiInstance = new UserDefinedTagApi(defaultClient);
    String id = "id_example"; // String | ID of the user-defined resource tag.
    try {
      apiInstance.deleteUserDefinedTag(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserDefinedTagApi#deleteUserDefinedTag");
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
| **id** | **String**| ID of the user-defined resource tag. | |

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Result of the delete request. |  -  |

<a id="deleteUserDefinedTagBulk"></a>
# **deleteUserDefinedTagBulk**
> ResourceTagDeleteResponse deleteUserDefinedTagBulk(ids)

Delete a list of user-defined resource tags

Delete a list of user-defined resource tags in one delete operation. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserDefinedTagApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    UserDefinedTagApi apiInstance = new UserDefinedTagApi(defaultClient);
    List<String> ids = Arrays.asList(); // List<String> | An array of IDs of the user-defined resource tags to be deleted. Any non-existent ID in the array will be ignored. 
    try {
      ResourceTagDeleteResponse result = apiInstance.deleteUserDefinedTagBulk(ids);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserDefinedTagApi#deleteUserDefinedTagBulk");
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
| **ids** | [**List&lt;String&gt;**](String.md)| An array of IDs of the user-defined resource tags to be deleted. Any non-existent ID in the array will be ignored.  | |

### Return type

[**ResourceTagDeleteResponse**](ResourceTagDeleteResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return a list of IDs that were deleted successfully. |  -  |

<a id="getUserDefinedTag"></a>
# **getUserDefinedTag**
> ResourceTagDetail getUserDefinedTag(id)

Get user-defined tag

Retrieve details of a user-defined resource tag.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserDefinedTagApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    UserDefinedTagApi apiInstance = new UserDefinedTagApi(defaultClient);
    String id = "id_example"; // String | ID of the user-defined resource tag.
    try {
      ResourceTagDetail result = apiInstance.getUserDefinedTag(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserDefinedTagApi#getUserDefinedTag");
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
| **id** | **String**| ID of the user-defined resource tag. | |

### Return type

[**ResourceTagDetail**](ResourceTagDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | resource tag detail. |  -  |

<a id="queryUserDefinedTag"></a>
# **queryUserDefinedTag**
> ResourceTagGetResponse queryUserDefinedTag(key, scopeRefId)

Get user-defined resource tags

Get user-defined resource tags for the cloud compute resources created by CloudOn and CloudOut. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserDefinedTagApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    UserDefinedTagApi apiInstance = new UserDefinedTagApi(defaultClient);
    String key = "key_example"; // String | Filter results by resource tag.
    String scopeRefId = "scopeRefId_example"; // String | Filter results by archival location id.
    try {
      ResourceTagGetResponse result = apiInstance.queryUserDefinedTag(key, scopeRefId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserDefinedTagApi#queryUserDefinedTag");
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
| **key** | **String**| Filter results by resource tag. | [optional] |
| **scopeRefId** | **String**| Filter results by archival location id. | [optional] |

### Return type

[**ResourceTagGetResponse**](ResourceTagGetResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of user-defined resource tags. |  -  |

<a id="updateUserDefinedTag"></a>
# **updateUserDefinedTag**
> ResourceTagDetail updateUserDefinedTag(id, resourceTagUpdate)

Update the value of a user-defined resource tag

Update the value of a user-defined resource tag. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserDefinedTagApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    UserDefinedTagApi apiInstance = new UserDefinedTagApi(defaultClient);
    String id = "id_example"; // String | ID of the user-defined resource tag.
    ResourceTagUpdate resourceTagUpdate = new ResourceTagUpdate(); // ResourceTagUpdate | Properties to update.
    try {
      ResourceTagDetail result = apiInstance.updateUserDefinedTag(id, resourceTagUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserDefinedTagApi#updateUserDefinedTag");
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
| **id** | **String**| ID of the user-defined resource tag. | |
| **resourceTagUpdate** | [**ResourceTagUpdate**](ResourceTagUpdate.md)| Properties to update. | |

### Return type

[**ResourceTagDetail**](ResourceTagDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated resource tag detail. |  -  |

