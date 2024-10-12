# UsersWriteApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**flextimeAdjustmentsDeleteFlextimeAdjustment**](UsersWriteApi.md#flextimeAdjustmentsDeleteFlextimeAdjustment) | **DELETE** /v1/flextimeadjustments/{guid} | Delete an flextime adjustment. |
| [**flextimeAdjustmentsPatchFlextimeAdjustment**](UsersWriteApi.md#flextimeAdjustmentsPatchFlextimeAdjustment) | **PATCH** /v1/flextimeadjustments/{guid} | Update (Patch) an Flextime Adjustment or a part of it. |
| [**flextimeAdjustmentsPostFlextimeAdjustment**](UsersWriteApi.md#flextimeAdjustmentsPostFlextimeAdjustment) | **POST** /v1/flextimeadjustments | Insert a flextime adjustment. |
| [**keywordsLinkKeywordToUser**](UsersWriteApi.md#keywordsLinkKeywordToUser) | **POST** /v1/users/{userGuid}/keywords/{guid} | Link existing keyword to user |
| [**userCustomValuesPatchUserCustomValue**](UsersWriteApi.md#userCustomValuesPatchUserCustomValue) | **PATCH** /v1/users/customvalues/{guid} | Update (Patch) a user custom value or a part of it. |
| [**userCustomValuesPostUserCustomValue**](UsersWriteApi.md#userCustomValuesPostUserCustomValue) | **POST** /v1/users/customvalues | Insert a user custom value. |
| [**usersPatchUser**](UsersWriteApi.md#usersPatchUser) | **PATCH** /v1/users/{guid} | Update (Patch) an user or a part of it. |
| [**usersPostUser**](UsersWriteApi.md#usersPostUser) | **POST** /v1/users | Insert an user. |
| [**workContractsPatchWorkContract_0**](UsersWriteApi.md#workContractsPatchWorkContract_0) | **PATCH** /v1/workcontracts/{guid} | Update (Patch) a work contract or a part of it. |
| [**workContractsPostWorkContract_0**](UsersWriteApi.md#workContractsPostWorkContract_0) | **POST** /v1/workcontracts | Insert a work contract. |
| [**workdaysPatchWorkDay**](UsersWriteApi.md#workdaysPatchWorkDay) | **PATCH** /v1/users/{userGuid}/workdays/{date} | Update (Patch) a workday or a part of it |


<a id="flextimeAdjustmentsDeleteFlextimeAdjustment"></a>
# **flextimeAdjustmentsDeleteFlextimeAdjustment**
> flextimeAdjustmentsDeleteFlextimeAdjustment(guid)

Delete an flextime adjustment.

Returns: No Content (204) if succeeded. Not found (404) if flextime adjustment can&#39;t be found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersWriteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersWriteApi apiInstance = new UsersWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID for the flextime adjustment to delete.
    try {
      apiInstance.flextimeAdjustmentsDeleteFlextimeAdjustment(guid);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersWriteApi#flextimeAdjustmentsDeleteFlextimeAdjustment");
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
| **guid** | **String**| ID for the flextime adjustment to delete. | |

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="flextimeAdjustmentsPatchFlextimeAdjustment"></a>
# **flextimeAdjustmentsPatchFlextimeAdjustment**
> List&lt;FlextimeAdjustmentOutputModel&gt; flextimeAdjustmentsPatchFlextimeAdjustment(guid, patchOperation)

Update (Patch) an Flextime Adjustment or a part of it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersWriteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersWriteApi apiInstance = new UsersWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the Flextime Adjustment.
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON patch document of FlextimeAdjustmentInputModel.
    try {
      List<FlextimeAdjustmentOutputModel> result = apiInstance.flextimeAdjustmentsPatchFlextimeAdjustment(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersWriteApi#flextimeAdjustmentsPatchFlextimeAdjustment");
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
| **guid** | **String**| ID of the Flextime Adjustment. | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON patch document of FlextimeAdjustmentInputModel. | [optional] |

### Return type

[**List&lt;FlextimeAdjustmentOutputModel&gt;**](FlextimeAdjustmentOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated Flextime Adjustment. |  -  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="flextimeAdjustmentsPostFlextimeAdjustment"></a>
# **flextimeAdjustmentsPostFlextimeAdjustment**
> FlextimeAdjustmentOutputModel flextimeAdjustmentsPostFlextimeAdjustment(flextimeAdjustmentInputModel)

Insert a flextime adjustment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersWriteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersWriteApi apiInstance = new UsersWriteApi(defaultClient);
    FlextimeAdjustmentInputModel flextimeAdjustmentInputModel = new FlextimeAdjustmentInputModel(); // FlextimeAdjustmentInputModel | FlextimeAdjustmentInputModel.
    try {
      FlextimeAdjustmentOutputModel result = apiInstance.flextimeAdjustmentsPostFlextimeAdjustment(flextimeAdjustmentInputModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersWriteApi#flextimeAdjustmentsPostFlextimeAdjustment");
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
| **flextimeAdjustmentInputModel** | [**FlextimeAdjustmentInputModel**](FlextimeAdjustmentInputModel.md)| FlextimeAdjustmentInputModel. | [optional] |

### Return type

[**FlextimeAdjustmentOutputModel**](FlextimeAdjustmentOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Inserted FlextimeAdjustment. |  -  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="keywordsLinkKeywordToUser"></a>
# **keywordsLinkKeywordToUser**
> UserKeywordModel keywordsLinkKeywordToUser(userGuid, guid)

Link existing keyword to user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersWriteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersWriteApi apiInstance = new UsersWriteApi(defaultClient);
    String userGuid = "userGuid_example"; // String | 
    String guid = "guid_example"; // String | 
    try {
      UserKeywordModel result = apiInstance.keywordsLinkKeywordToUser(userGuid, guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersWriteApi#keywordsLinkKeywordToUser");
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
| **userGuid** | **String**|  | |
| **guid** | **String**|  | |

### Return type

[**UserKeywordModel**](UserKeywordModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created user keyword link. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="userCustomValuesPatchUserCustomValue"></a>
# **userCustomValuesPatchUserCustomValue**
> List&lt;UserCustomValueOutputModel&gt; userCustomValuesPatchUserCustomValue(guid, patchOperation)

Update (Patch) a user custom value or a part of it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersWriteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersWriteApi apiInstance = new UsersWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the user custom value Can also be comma separate list of IDs to patch multiple user custom values with one call. When multiple IDs are given, returns model which has list of succeeded user custom values and list of errors.
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON Patch document of UserCustomValueModel.
    try {
      List<UserCustomValueOutputModel> result = apiInstance.userCustomValuesPatchUserCustomValue(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersWriteApi#userCustomValuesPatchUserCustomValue");
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
| **guid** | **String**| ID of the user custom value Can also be comma separate list of IDs to patch multiple user custom values with one call. When multiple IDs are given, returns model which has list of succeeded user custom values and list of errors. | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON Patch document of UserCustomValueModel. | [optional] |

### Return type

[**List&lt;UserCustomValueOutputModel&gt;**](UserCustomValueOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of updated user custom values. |  -  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="userCustomValuesPostUserCustomValue"></a>
# **userCustomValuesPostUserCustomValue**
> List&lt;UserCustomValueOutputModel&gt; userCustomValuesPostUserCustomValue(userCustomValueInputModel)

Insert a user custom value.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersWriteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersWriteApi apiInstance = new UsersWriteApi(defaultClient);
    UserCustomValueInputModel userCustomValueInputModel = new UserCustomValueInputModel(); // UserCustomValueInputModel | UserCustomValueModel.
    try {
      List<UserCustomValueOutputModel> result = apiInstance.userCustomValuesPostUserCustomValue(userCustomValueInputModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersWriteApi#userCustomValuesPostUserCustomValue");
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
| **userCustomValueInputModel** | [**UserCustomValueInputModel**](UserCustomValueInputModel.md)| UserCustomValueModel. | [optional] |

### Return type

[**List&lt;UserCustomValueOutputModel&gt;**](UserCustomValueOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created user custom value. |  -  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="usersPatchUser"></a>
# **usersPatchUser**
> List&lt;UserOutputModel&gt; usersPatchUser(guid, patchOperation)

Update (Patch) an user or a part of it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersWriteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersWriteApi apiInstance = new UsersWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the user.
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON Patch document of UserModel.
    try {
      List<UserOutputModel> result = apiInstance.usersPatchUser(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersWriteApi#usersPatchUser");
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
| **guid** | **String**| ID of the user. | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON Patch document of UserModel. | [optional] |

### Return type

[**List&lt;UserOutputModel&gt;**](UserOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of updated users. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="usersPostUser"></a>
# **usersPostUser**
> UserOutputModel usersPostUser(userInputModel)

Insert an user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersWriteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersWriteApi apiInstance = new UsersWriteApi(defaultClient);
    UserInputModel userInputModel = new UserInputModel(); // UserInputModel | UserModel.
    try {
      UserOutputModel result = apiInstance.usersPostUser(userInputModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersWriteApi#usersPostUser");
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
| **userInputModel** | [**UserInputModel**](UserInputModel.md)| UserModel. | [optional] |

### Return type

[**UserOutputModel**](UserOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created user. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="workContractsPatchWorkContract_0"></a>
# **workContractsPatchWorkContract_0**
> List&lt;WorkContractOutputModel&gt; workContractsPatchWorkContract_0(guid, patchOperation)

Update (Patch) a work contract or a part of it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersWriteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersWriteApi apiInstance = new UsersWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the work contract.
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON patch document of WorkContractOutputModel.
    try {
      List<WorkContractOutputModel> result = apiInstance.workContractsPatchWorkContract_0(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersWriteApi#workContractsPatchWorkContract_0");
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
| **guid** | **String**| ID of the work contract. | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON patch document of WorkContractOutputModel. | [optional] |

### Return type

[**List&lt;WorkContractOutputModel&gt;**](WorkContractOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | list of updated work contract. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="workContractsPostWorkContract_0"></a>
# **workContractsPostWorkContract_0**
> WorkContractOutputModel workContractsPostWorkContract_0(resetFlextime, workContractInputModel)

Insert a work contract.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersWriteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersWriteApi apiInstance = new UsersWriteApi(defaultClient);
    Boolean resetFlextime = true; // Boolean | Optional. Reset flextime to zero when new work contract starts or keep the flextime value. Default true = reset flextime.
    WorkContractInputModel workContractInputModel = new WorkContractInputModel(); // WorkContractInputModel | WorkContractOutputModel.
    try {
      WorkContractOutputModel result = apiInstance.workContractsPostWorkContract_0(resetFlextime, workContractInputModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersWriteApi#workContractsPostWorkContract_0");
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
| **resetFlextime** | **Boolean**| Optional. Reset flextime to zero when new work contract starts or keep the flextime value. Default true &#x3D; reset flextime. | [optional] [default to true] |
| **workContractInputModel** | [**WorkContractInputModel**](WorkContractInputModel.md)| WorkContractOutputModel. | [optional] |

### Return type

[**WorkContractOutputModel**](WorkContractOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created work contract. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="workdaysPatchWorkDay"></a>
# **workdaysPatchWorkDay**
> List&lt;WorkdayModel&gt; workdaysPatchWorkDay(userGuid, date, patchOperation)

Update (Patch) a workday or a part of it

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersWriteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersWriteApi apiInstance = new UsersWriteApi(defaultClient);
    String userGuid = "userGuid_example"; // String | ID of the user.
    OffsetDateTime date = OffsetDateTime.now(); // OffsetDateTime | Date of the workday..
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON patch document of WorkdayModel
    try {
      List<WorkdayModel> result = apiInstance.workdaysPatchWorkDay(userGuid, date, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersWriteApi#workdaysPatchWorkDay");
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
| **userGuid** | **String**| ID of the user. | |
| **date** | **OffsetDateTime**| Date of the workday.. | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON patch document of WorkdayModel | [optional] |

### Return type

[**List&lt;WorkdayModel&gt;**](WorkdayModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | list of updated workdays |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

