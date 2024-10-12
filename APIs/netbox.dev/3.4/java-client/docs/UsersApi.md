# UsersApi

All URIs are relative to *https://demo.netbox.dev/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**usersConfigList**](UsersApi.md#usersConfigList) | **GET** /users/config/ |  |
| [**usersGroupsBulkDelete**](UsersApi.md#usersGroupsBulkDelete) | **DELETE** /users/groups/ |  |
| [**usersGroupsBulkPartialUpdate**](UsersApi.md#usersGroupsBulkPartialUpdate) | **PATCH** /users/groups/ |  |
| [**usersGroupsBulkUpdate**](UsersApi.md#usersGroupsBulkUpdate) | **PUT** /users/groups/ |  |
| [**usersGroupsCreate**](UsersApi.md#usersGroupsCreate) | **POST** /users/groups/ |  |
| [**usersGroupsDelete**](UsersApi.md#usersGroupsDelete) | **DELETE** /users/groups/{id}/ |  |
| [**usersGroupsList**](UsersApi.md#usersGroupsList) | **GET** /users/groups/ |  |
| [**usersGroupsPartialUpdate**](UsersApi.md#usersGroupsPartialUpdate) | **PATCH** /users/groups/{id}/ |  |
| [**usersGroupsRead**](UsersApi.md#usersGroupsRead) | **GET** /users/groups/{id}/ |  |
| [**usersGroupsUpdate**](UsersApi.md#usersGroupsUpdate) | **PUT** /users/groups/{id}/ |  |
| [**usersPermissionsBulkDelete**](UsersApi.md#usersPermissionsBulkDelete) | **DELETE** /users/permissions/ |  |
| [**usersPermissionsBulkPartialUpdate**](UsersApi.md#usersPermissionsBulkPartialUpdate) | **PATCH** /users/permissions/ |  |
| [**usersPermissionsBulkUpdate**](UsersApi.md#usersPermissionsBulkUpdate) | **PUT** /users/permissions/ |  |
| [**usersPermissionsCreate**](UsersApi.md#usersPermissionsCreate) | **POST** /users/permissions/ |  |
| [**usersPermissionsDelete**](UsersApi.md#usersPermissionsDelete) | **DELETE** /users/permissions/{id}/ |  |
| [**usersPermissionsList**](UsersApi.md#usersPermissionsList) | **GET** /users/permissions/ |  |
| [**usersPermissionsPartialUpdate**](UsersApi.md#usersPermissionsPartialUpdate) | **PATCH** /users/permissions/{id}/ |  |
| [**usersPermissionsRead**](UsersApi.md#usersPermissionsRead) | **GET** /users/permissions/{id}/ |  |
| [**usersPermissionsUpdate**](UsersApi.md#usersPermissionsUpdate) | **PUT** /users/permissions/{id}/ |  |
| [**usersTokensBulkDelete**](UsersApi.md#usersTokensBulkDelete) | **DELETE** /users/tokens/ |  |
| [**usersTokensBulkPartialUpdate**](UsersApi.md#usersTokensBulkPartialUpdate) | **PATCH** /users/tokens/ |  |
| [**usersTokensBulkUpdate**](UsersApi.md#usersTokensBulkUpdate) | **PUT** /users/tokens/ |  |
| [**usersTokensCreate**](UsersApi.md#usersTokensCreate) | **POST** /users/tokens/ |  |
| [**usersTokensDelete**](UsersApi.md#usersTokensDelete) | **DELETE** /users/tokens/{id}/ |  |
| [**usersTokensList**](UsersApi.md#usersTokensList) | **GET** /users/tokens/ |  |
| [**usersTokensPartialUpdate**](UsersApi.md#usersTokensPartialUpdate) | **PATCH** /users/tokens/{id}/ |  |
| [**usersTokensProvisionCreate**](UsersApi.md#usersTokensProvisionCreate) | **POST** /users/tokens/provision/ |  |
| [**usersTokensRead**](UsersApi.md#usersTokensRead) | **GET** /users/tokens/{id}/ |  |
| [**usersTokensUpdate**](UsersApi.md#usersTokensUpdate) | **PUT** /users/tokens/{id}/ |  |
| [**usersUsersBulkDelete**](UsersApi.md#usersUsersBulkDelete) | **DELETE** /users/users/ |  |
| [**usersUsersBulkPartialUpdate**](UsersApi.md#usersUsersBulkPartialUpdate) | **PATCH** /users/users/ |  |
| [**usersUsersBulkUpdate**](UsersApi.md#usersUsersBulkUpdate) | **PUT** /users/users/ |  |
| [**usersUsersCreate**](UsersApi.md#usersUsersCreate) | **POST** /users/users/ |  |
| [**usersUsersDelete**](UsersApi.md#usersUsersDelete) | **DELETE** /users/users/{id}/ |  |
| [**usersUsersList**](UsersApi.md#usersUsersList) | **GET** /users/users/ |  |
| [**usersUsersPartialUpdate**](UsersApi.md#usersUsersPartialUpdate) | **PATCH** /users/users/{id}/ |  |
| [**usersUsersRead**](UsersApi.md#usersUsersRead) | **GET** /users/users/{id}/ |  |
| [**usersUsersUpdate**](UsersApi.md#usersUsersUpdate) | **PUT** /users/users/{id}/ |  |


<a id="usersConfigList"></a>
# **usersConfigList**
> usersConfigList()



Return the UserConfig for the currently authenticated User.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.netbox.dev/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    try {
      apiInstance.usersConfigList();
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersConfigList");
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

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="usersGroupsBulkDelete"></a>
# **usersGroupsBulkDelete**
> usersGroupsBulkDelete()





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.netbox.dev/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    try {
      apiInstance.usersGroupsBulkDelete();
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersGroupsBulkDelete");
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

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |

<a id="usersGroupsBulkPartialUpdate"></a>
# **usersGroupsBulkPartialUpdate**
> Group usersGroupsBulkPartialUpdate(group)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.netbox.dev/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    Group group = new Group(); // Group | 
    try {
      Group result = apiInstance.usersGroupsBulkPartialUpdate(group);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersGroupsBulkPartialUpdate");
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
| **group** | [**Group**](Group.md)|  | |

### Return type

[**Group**](Group.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="usersGroupsBulkUpdate"></a>
# **usersGroupsBulkUpdate**
> Group usersGroupsBulkUpdate(group)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.netbox.dev/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    Group group = new Group(); // Group | 
    try {
      Group result = apiInstance.usersGroupsBulkUpdate(group);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersGroupsBulkUpdate");
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
| **group** | [**Group**](Group.md)|  | |

### Return type

[**Group**](Group.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="usersGroupsCreate"></a>
# **usersGroupsCreate**
> Group usersGroupsCreate(group)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.netbox.dev/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    Group group = new Group(); // Group | 
    try {
      Group result = apiInstance.usersGroupsCreate(group);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersGroupsCreate");
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
| **group** | [**Group**](Group.md)|  | |

### Return type

[**Group**](Group.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="usersGroupsDelete"></a>
# **usersGroupsDelete**
> usersGroupsDelete(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.netbox.dev/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this group.
    try {
      apiInstance.usersGroupsDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersGroupsDelete");
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
| **id** | **Integer**| A unique integer value identifying this group. | |

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |

<a id="usersGroupsList"></a>
# **usersGroupsList**
> UsersGroupsList200Response usersGroupsList(id, name, q, idN, idLte, idLt, idGte, idGt, nameN, nameIc, nameNic, nameIew, nameNiew, nameIsw, nameNisw, nameIe, nameNie, nameEmpty, ordering, limit, offset)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.netbox.dev/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String id = "id_example"; // String | 
    String name = "name_example"; // String | 
    String q = "q_example"; // String | 
    String idN = "idN_example"; // String | 
    String idLte = "idLte_example"; // String | 
    String idLt = "idLt_example"; // String | 
    String idGte = "idGte_example"; // String | 
    String idGt = "idGt_example"; // String | 
    String nameN = "nameN_example"; // String | 
    String nameIc = "nameIc_example"; // String | 
    String nameNic = "nameNic_example"; // String | 
    String nameIew = "nameIew_example"; // String | 
    String nameNiew = "nameNiew_example"; // String | 
    String nameIsw = "nameIsw_example"; // String | 
    String nameNisw = "nameNisw_example"; // String | 
    String nameIe = "nameIe_example"; // String | 
    String nameNie = "nameNie_example"; // String | 
    String nameEmpty = "nameEmpty_example"; // String | 
    String ordering = "ordering_example"; // String | Which field to use when ordering the results.
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      UsersGroupsList200Response result = apiInstance.usersGroupsList(id, name, q, idN, idLte, idLt, idGte, idGt, nameN, nameIc, nameNic, nameIew, nameNiew, nameIsw, nameNisw, nameIe, nameNie, nameEmpty, ordering, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersGroupsList");
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
| **id** | **String**|  | [optional] |
| **name** | **String**|  | [optional] |
| **q** | **String**|  | [optional] |
| **idN** | **String**|  | [optional] |
| **idLte** | **String**|  | [optional] |
| **idLt** | **String**|  | [optional] |
| **idGte** | **String**|  | [optional] |
| **idGt** | **String**|  | [optional] |
| **nameN** | **String**|  | [optional] |
| **nameIc** | **String**|  | [optional] |
| **nameNic** | **String**|  | [optional] |
| **nameIew** | **String**|  | [optional] |
| **nameNiew** | **String**|  | [optional] |
| **nameIsw** | **String**|  | [optional] |
| **nameNisw** | **String**|  | [optional] |
| **nameIe** | **String**|  | [optional] |
| **nameNie** | **String**|  | [optional] |
| **nameEmpty** | **String**|  | [optional] |
| **ordering** | **String**| Which field to use when ordering the results. | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |

### Return type

[**UsersGroupsList200Response**](UsersGroupsList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="usersGroupsPartialUpdate"></a>
# **usersGroupsPartialUpdate**
> Group usersGroupsPartialUpdate(id, group)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.netbox.dev/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this group.
    Group group = new Group(); // Group | 
    try {
      Group result = apiInstance.usersGroupsPartialUpdate(id, group);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersGroupsPartialUpdate");
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
| **id** | **Integer**| A unique integer value identifying this group. | |
| **group** | [**Group**](Group.md)|  | |

### Return type

[**Group**](Group.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="usersGroupsRead"></a>
# **usersGroupsRead**
> Group usersGroupsRead(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.netbox.dev/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this group.
    try {
      Group result = apiInstance.usersGroupsRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersGroupsRead");
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
| **id** | **Integer**| A unique integer value identifying this group. | |

### Return type

[**Group**](Group.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="usersGroupsUpdate"></a>
# **usersGroupsUpdate**
> Group usersGroupsUpdate(id, group)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.netbox.dev/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this group.
    Group group = new Group(); // Group | 
    try {
      Group result = apiInstance.usersGroupsUpdate(id, group);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersGroupsUpdate");
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
| **id** | **Integer**| A unique integer value identifying this group. | |
| **group** | [**Group**](Group.md)|  | |

### Return type

[**Group**](Group.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="usersPermissionsBulkDelete"></a>
# **usersPermissionsBulkDelete**
> usersPermissionsBulkDelete()





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.netbox.dev/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    try {
      apiInstance.usersPermissionsBulkDelete();
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersPermissionsBulkDelete");
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

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |

<a id="usersPermissionsBulkPartialUpdate"></a>
# **usersPermissionsBulkPartialUpdate**
> ObjectPermission usersPermissionsBulkPartialUpdate(writableObjectPermission)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.netbox.dev/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    WritableObjectPermission writableObjectPermission = new WritableObjectPermission(); // WritableObjectPermission | 
    try {
      ObjectPermission result = apiInstance.usersPermissionsBulkPartialUpdate(writableObjectPermission);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersPermissionsBulkPartialUpdate");
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
| **writableObjectPermission** | [**WritableObjectPermission**](WritableObjectPermission.md)|  | |

### Return type

[**ObjectPermission**](ObjectPermission.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="usersPermissionsBulkUpdate"></a>
# **usersPermissionsBulkUpdate**
> ObjectPermission usersPermissionsBulkUpdate(writableObjectPermission)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.netbox.dev/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    WritableObjectPermission writableObjectPermission = new WritableObjectPermission(); // WritableObjectPermission | 
    try {
      ObjectPermission result = apiInstance.usersPermissionsBulkUpdate(writableObjectPermission);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersPermissionsBulkUpdate");
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
| **writableObjectPermission** | [**WritableObjectPermission**](WritableObjectPermission.md)|  | |

### Return type

[**ObjectPermission**](ObjectPermission.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="usersPermissionsCreate"></a>
# **usersPermissionsCreate**
> ObjectPermission usersPermissionsCreate(writableObjectPermission)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.netbox.dev/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    WritableObjectPermission writableObjectPermission = new WritableObjectPermission(); // WritableObjectPermission | 
    try {
      ObjectPermission result = apiInstance.usersPermissionsCreate(writableObjectPermission);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersPermissionsCreate");
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
| **writableObjectPermission** | [**WritableObjectPermission**](WritableObjectPermission.md)|  | |

### Return type

[**ObjectPermission**](ObjectPermission.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="usersPermissionsDelete"></a>
# **usersPermissionsDelete**
> usersPermissionsDelete(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.netbox.dev/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this permission.
    try {
      apiInstance.usersPermissionsDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersPermissionsDelete");
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
| **id** | **Integer**| A unique integer value identifying this permission. | |

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |

<a id="usersPermissionsList"></a>
# **usersPermissionsList**
> UsersPermissionsList200Response usersPermissionsList(id, name, enabled, objectTypes, description, q, userId, user, groupId, group, idN, idLte, idLt, idGte, idGt, nameN, nameIc, nameNic, nameIew, nameNiew, nameIsw, nameNisw, nameIe, nameNie, nameEmpty, objectTypesN, descriptionN, descriptionIc, descriptionNic, descriptionIew, descriptionNiew, descriptionIsw, descriptionNisw, descriptionIe, descriptionNie, descriptionEmpty, userIdN, userN, groupIdN, groupN, ordering, limit, offset)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.netbox.dev/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String id = "id_example"; // String | 
    String name = "name_example"; // String | 
    String enabled = "enabled_example"; // String | 
    String objectTypes = "objectTypes_example"; // String | 
    String description = "description_example"; // String | 
    String q = "q_example"; // String | 
    String userId = "userId_example"; // String | 
    String user = "user_example"; // String | 
    String groupId = "groupId_example"; // String | 
    String group = "group_example"; // String | 
    String idN = "idN_example"; // String | 
    String idLte = "idLte_example"; // String | 
    String idLt = "idLt_example"; // String | 
    String idGte = "idGte_example"; // String | 
    String idGt = "idGt_example"; // String | 
    String nameN = "nameN_example"; // String | 
    String nameIc = "nameIc_example"; // String | 
    String nameNic = "nameNic_example"; // String | 
    String nameIew = "nameIew_example"; // String | 
    String nameNiew = "nameNiew_example"; // String | 
    String nameIsw = "nameIsw_example"; // String | 
    String nameNisw = "nameNisw_example"; // String | 
    String nameIe = "nameIe_example"; // String | 
    String nameNie = "nameNie_example"; // String | 
    String nameEmpty = "nameEmpty_example"; // String | 
    String objectTypesN = "objectTypesN_example"; // String | 
    String descriptionN = "descriptionN_example"; // String | 
    String descriptionIc = "descriptionIc_example"; // String | 
    String descriptionNic = "descriptionNic_example"; // String | 
    String descriptionIew = "descriptionIew_example"; // String | 
    String descriptionNiew = "descriptionNiew_example"; // String | 
    String descriptionIsw = "descriptionIsw_example"; // String | 
    String descriptionNisw = "descriptionNisw_example"; // String | 
    String descriptionIe = "descriptionIe_example"; // String | 
    String descriptionNie = "descriptionNie_example"; // String | 
    String descriptionEmpty = "descriptionEmpty_example"; // String | 
    String userIdN = "userIdN_example"; // String | 
    String userN = "userN_example"; // String | 
    String groupIdN = "groupIdN_example"; // String | 
    String groupN = "groupN_example"; // String | 
    String ordering = "ordering_example"; // String | Which field to use when ordering the results.
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      UsersPermissionsList200Response result = apiInstance.usersPermissionsList(id, name, enabled, objectTypes, description, q, userId, user, groupId, group, idN, idLte, idLt, idGte, idGt, nameN, nameIc, nameNic, nameIew, nameNiew, nameIsw, nameNisw, nameIe, nameNie, nameEmpty, objectTypesN, descriptionN, descriptionIc, descriptionNic, descriptionIew, descriptionNiew, descriptionIsw, descriptionNisw, descriptionIe, descriptionNie, descriptionEmpty, userIdN, userN, groupIdN, groupN, ordering, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersPermissionsList");
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
| **id** | **String**|  | [optional] |
| **name** | **String**|  | [optional] |
| **enabled** | **String**|  | [optional] |
| **objectTypes** | **String**|  | [optional] |
| **description** | **String**|  | [optional] |
| **q** | **String**|  | [optional] |
| **userId** | **String**|  | [optional] |
| **user** | **String**|  | [optional] |
| **groupId** | **String**|  | [optional] |
| **group** | **String**|  | [optional] |
| **idN** | **String**|  | [optional] |
| **idLte** | **String**|  | [optional] |
| **idLt** | **String**|  | [optional] |
| **idGte** | **String**|  | [optional] |
| **idGt** | **String**|  | [optional] |
| **nameN** | **String**|  | [optional] |
| **nameIc** | **String**|  | [optional] |
| **nameNic** | **String**|  | [optional] |
| **nameIew** | **String**|  | [optional] |
| **nameNiew** | **String**|  | [optional] |
| **nameIsw** | **String**|  | [optional] |
| **nameNisw** | **String**|  | [optional] |
| **nameIe** | **String**|  | [optional] |
| **nameNie** | **String**|  | [optional] |
| **nameEmpty** | **String**|  | [optional] |
| **objectTypesN** | **String**|  | [optional] |
| **descriptionN** | **String**|  | [optional] |
| **descriptionIc** | **String**|  | [optional] |
| **descriptionNic** | **String**|  | [optional] |
| **descriptionIew** | **String**|  | [optional] |
| **descriptionNiew** | **String**|  | [optional] |
| **descriptionIsw** | **String**|  | [optional] |
| **descriptionNisw** | **String**|  | [optional] |
| **descriptionIe** | **String**|  | [optional] |
| **descriptionNie** | **String**|  | [optional] |
| **descriptionEmpty** | **String**|  | [optional] |
| **userIdN** | **String**|  | [optional] |
| **userN** | **String**|  | [optional] |
| **groupIdN** | **String**|  | [optional] |
| **groupN** | **String**|  | [optional] |
| **ordering** | **String**| Which field to use when ordering the results. | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |

### Return type

[**UsersPermissionsList200Response**](UsersPermissionsList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="usersPermissionsPartialUpdate"></a>
# **usersPermissionsPartialUpdate**
> ObjectPermission usersPermissionsPartialUpdate(id, writableObjectPermission)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.netbox.dev/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this permission.
    WritableObjectPermission writableObjectPermission = new WritableObjectPermission(); // WritableObjectPermission | 
    try {
      ObjectPermission result = apiInstance.usersPermissionsPartialUpdate(id, writableObjectPermission);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersPermissionsPartialUpdate");
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
| **id** | **Integer**| A unique integer value identifying this permission. | |
| **writableObjectPermission** | [**WritableObjectPermission**](WritableObjectPermission.md)|  | |

### Return type

[**ObjectPermission**](ObjectPermission.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="usersPermissionsRead"></a>
# **usersPermissionsRead**
> ObjectPermission usersPermissionsRead(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.netbox.dev/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this permission.
    try {
      ObjectPermission result = apiInstance.usersPermissionsRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersPermissionsRead");
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
| **id** | **Integer**| A unique integer value identifying this permission. | |

### Return type

[**ObjectPermission**](ObjectPermission.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="usersPermissionsUpdate"></a>
# **usersPermissionsUpdate**
> ObjectPermission usersPermissionsUpdate(id, writableObjectPermission)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.netbox.dev/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this permission.
    WritableObjectPermission writableObjectPermission = new WritableObjectPermission(); // WritableObjectPermission | 
    try {
      ObjectPermission result = apiInstance.usersPermissionsUpdate(id, writableObjectPermission);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersPermissionsUpdate");
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
| **id** | **Integer**| A unique integer value identifying this permission. | |
| **writableObjectPermission** | [**WritableObjectPermission**](WritableObjectPermission.md)|  | |

### Return type

[**ObjectPermission**](ObjectPermission.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="usersTokensBulkDelete"></a>
# **usersTokensBulkDelete**
> usersTokensBulkDelete()





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.netbox.dev/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    try {
      apiInstance.usersTokensBulkDelete();
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersTokensBulkDelete");
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

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |

<a id="usersTokensBulkPartialUpdate"></a>
# **usersTokensBulkPartialUpdate**
> Token usersTokensBulkPartialUpdate(writableToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.netbox.dev/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    WritableToken writableToken = new WritableToken(); // WritableToken | 
    try {
      Token result = apiInstance.usersTokensBulkPartialUpdate(writableToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersTokensBulkPartialUpdate");
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
| **writableToken** | [**WritableToken**](WritableToken.md)|  | |

### Return type

[**Token**](Token.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="usersTokensBulkUpdate"></a>
# **usersTokensBulkUpdate**
> Token usersTokensBulkUpdate(writableToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.netbox.dev/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    WritableToken writableToken = new WritableToken(); // WritableToken | 
    try {
      Token result = apiInstance.usersTokensBulkUpdate(writableToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersTokensBulkUpdate");
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
| **writableToken** | [**WritableToken**](WritableToken.md)|  | |

### Return type

[**Token**](Token.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="usersTokensCreate"></a>
# **usersTokensCreate**
> Token usersTokensCreate(writableToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.netbox.dev/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    WritableToken writableToken = new WritableToken(); // WritableToken | 
    try {
      Token result = apiInstance.usersTokensCreate(writableToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersTokensCreate");
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
| **writableToken** | [**WritableToken**](WritableToken.md)|  | |

### Return type

[**Token**](Token.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="usersTokensDelete"></a>
# **usersTokensDelete**
> usersTokensDelete(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.netbox.dev/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this token.
    try {
      apiInstance.usersTokensDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersTokensDelete");
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
| **id** | **Integer**| A unique integer value identifying this token. | |

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |

<a id="usersTokensList"></a>
# **usersTokensList**
> UsersTokensList200Response usersTokensList(id, key, writeEnabled, description, q, userId, user, created, createdGte, createdLte, expires, expiresGte, expiresLte, idN, idLte, idLt, idGte, idGt, keyN, keyIc, keyNic, keyIew, keyNiew, keyIsw, keyNisw, keyIe, keyNie, keyEmpty, descriptionN, descriptionIc, descriptionNic, descriptionIew, descriptionNiew, descriptionIsw, descriptionNisw, descriptionIe, descriptionNie, descriptionEmpty, userIdN, userN, ordering, limit, offset)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.netbox.dev/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String id = "id_example"; // String | 
    String key = "key_example"; // String | 
    String writeEnabled = "writeEnabled_example"; // String | 
    String description = "description_example"; // String | 
    String q = "q_example"; // String | 
    String userId = "userId_example"; // String | 
    String user = "user_example"; // String | 
    String created = "created_example"; // String | 
    String createdGte = "createdGte_example"; // String | 
    String createdLte = "createdLte_example"; // String | 
    String expires = "expires_example"; // String | 
    String expiresGte = "expiresGte_example"; // String | 
    String expiresLte = "expiresLte_example"; // String | 
    String idN = "idN_example"; // String | 
    String idLte = "idLte_example"; // String | 
    String idLt = "idLt_example"; // String | 
    String idGte = "idGte_example"; // String | 
    String idGt = "idGt_example"; // String | 
    String keyN = "keyN_example"; // String | 
    String keyIc = "keyIc_example"; // String | 
    String keyNic = "keyNic_example"; // String | 
    String keyIew = "keyIew_example"; // String | 
    String keyNiew = "keyNiew_example"; // String | 
    String keyIsw = "keyIsw_example"; // String | 
    String keyNisw = "keyNisw_example"; // String | 
    String keyIe = "keyIe_example"; // String | 
    String keyNie = "keyNie_example"; // String | 
    String keyEmpty = "keyEmpty_example"; // String | 
    String descriptionN = "descriptionN_example"; // String | 
    String descriptionIc = "descriptionIc_example"; // String | 
    String descriptionNic = "descriptionNic_example"; // String | 
    String descriptionIew = "descriptionIew_example"; // String | 
    String descriptionNiew = "descriptionNiew_example"; // String | 
    String descriptionIsw = "descriptionIsw_example"; // String | 
    String descriptionNisw = "descriptionNisw_example"; // String | 
    String descriptionIe = "descriptionIe_example"; // String | 
    String descriptionNie = "descriptionNie_example"; // String | 
    String descriptionEmpty = "descriptionEmpty_example"; // String | 
    String userIdN = "userIdN_example"; // String | 
    String userN = "userN_example"; // String | 
    String ordering = "ordering_example"; // String | Which field to use when ordering the results.
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      UsersTokensList200Response result = apiInstance.usersTokensList(id, key, writeEnabled, description, q, userId, user, created, createdGte, createdLte, expires, expiresGte, expiresLte, idN, idLte, idLt, idGte, idGt, keyN, keyIc, keyNic, keyIew, keyNiew, keyIsw, keyNisw, keyIe, keyNie, keyEmpty, descriptionN, descriptionIc, descriptionNic, descriptionIew, descriptionNiew, descriptionIsw, descriptionNisw, descriptionIe, descriptionNie, descriptionEmpty, userIdN, userN, ordering, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersTokensList");
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
| **id** | **String**|  | [optional] |
| **key** | **String**|  | [optional] |
| **writeEnabled** | **String**|  | [optional] |
| **description** | **String**|  | [optional] |
| **q** | **String**|  | [optional] |
| **userId** | **String**|  | [optional] |
| **user** | **String**|  | [optional] |
| **created** | **String**|  | [optional] |
| **createdGte** | **String**|  | [optional] |
| **createdLte** | **String**|  | [optional] |
| **expires** | **String**|  | [optional] |
| **expiresGte** | **String**|  | [optional] |
| **expiresLte** | **String**|  | [optional] |
| **idN** | **String**|  | [optional] |
| **idLte** | **String**|  | [optional] |
| **idLt** | **String**|  | [optional] |
| **idGte** | **String**|  | [optional] |
| **idGt** | **String**|  | [optional] |
| **keyN** | **String**|  | [optional] |
| **keyIc** | **String**|  | [optional] |
| **keyNic** | **String**|  | [optional] |
| **keyIew** | **String**|  | [optional] |
| **keyNiew** | **String**|  | [optional] |
| **keyIsw** | **String**|  | [optional] |
| **keyNisw** | **String**|  | [optional] |
| **keyIe** | **String**|  | [optional] |
| **keyNie** | **String**|  | [optional] |
| **keyEmpty** | **String**|  | [optional] |
| **descriptionN** | **String**|  | [optional] |
| **descriptionIc** | **String**|  | [optional] |
| **descriptionNic** | **String**|  | [optional] |
| **descriptionIew** | **String**|  | [optional] |
| **descriptionNiew** | **String**|  | [optional] |
| **descriptionIsw** | **String**|  | [optional] |
| **descriptionNisw** | **String**|  | [optional] |
| **descriptionIe** | **String**|  | [optional] |
| **descriptionNie** | **String**|  | [optional] |
| **descriptionEmpty** | **String**|  | [optional] |
| **userIdN** | **String**|  | [optional] |
| **userN** | **String**|  | [optional] |
| **ordering** | **String**| Which field to use when ordering the results. | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |

### Return type

[**UsersTokensList200Response**](UsersTokensList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="usersTokensPartialUpdate"></a>
# **usersTokensPartialUpdate**
> Token usersTokensPartialUpdate(id, writableToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.netbox.dev/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this token.
    WritableToken writableToken = new WritableToken(); // WritableToken | 
    try {
      Token result = apiInstance.usersTokensPartialUpdate(id, writableToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersTokensPartialUpdate");
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
| **id** | **Integer**| A unique integer value identifying this token. | |
| **writableToken** | [**WritableToken**](WritableToken.md)|  | |

### Return type

[**Token**](Token.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="usersTokensProvisionCreate"></a>
# **usersTokensProvisionCreate**
> usersTokensProvisionCreate()



Non-authenticated REST API endpoint via which a user may create a Token.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.netbox.dev/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    try {
      apiInstance.usersTokensProvisionCreate();
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersTokensProvisionCreate");
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

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="usersTokensRead"></a>
# **usersTokensRead**
> Token usersTokensRead(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.netbox.dev/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this token.
    try {
      Token result = apiInstance.usersTokensRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersTokensRead");
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
| **id** | **Integer**| A unique integer value identifying this token. | |

### Return type

[**Token**](Token.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="usersTokensUpdate"></a>
# **usersTokensUpdate**
> Token usersTokensUpdate(id, writableToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.netbox.dev/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this token.
    WritableToken writableToken = new WritableToken(); // WritableToken | 
    try {
      Token result = apiInstance.usersTokensUpdate(id, writableToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersTokensUpdate");
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
| **id** | **Integer**| A unique integer value identifying this token. | |
| **writableToken** | [**WritableToken**](WritableToken.md)|  | |

### Return type

[**Token**](Token.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="usersUsersBulkDelete"></a>
# **usersUsersBulkDelete**
> usersUsersBulkDelete()





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.netbox.dev/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    try {
      apiInstance.usersUsersBulkDelete();
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersUsersBulkDelete");
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

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |

<a id="usersUsersBulkPartialUpdate"></a>
# **usersUsersBulkPartialUpdate**
> User usersUsersBulkPartialUpdate(writableUser)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.netbox.dev/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    WritableUser writableUser = new WritableUser(); // WritableUser | 
    try {
      User result = apiInstance.usersUsersBulkPartialUpdate(writableUser);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersUsersBulkPartialUpdate");
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
| **writableUser** | [**WritableUser**](WritableUser.md)|  | |

### Return type

[**User**](User.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="usersUsersBulkUpdate"></a>
# **usersUsersBulkUpdate**
> User usersUsersBulkUpdate(writableUser)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.netbox.dev/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    WritableUser writableUser = new WritableUser(); // WritableUser | 
    try {
      User result = apiInstance.usersUsersBulkUpdate(writableUser);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersUsersBulkUpdate");
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
| **writableUser** | [**WritableUser**](WritableUser.md)|  | |

### Return type

[**User**](User.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="usersUsersCreate"></a>
# **usersUsersCreate**
> User usersUsersCreate(writableUser)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.netbox.dev/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    WritableUser writableUser = new WritableUser(); // WritableUser | 
    try {
      User result = apiInstance.usersUsersCreate(writableUser);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersUsersCreate");
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
| **writableUser** | [**WritableUser**](WritableUser.md)|  | |

### Return type

[**User**](User.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="usersUsersDelete"></a>
# **usersUsersDelete**
> usersUsersDelete(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.netbox.dev/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this user.
    try {
      apiInstance.usersUsersDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersUsersDelete");
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
| **id** | **Integer**| A unique integer value identifying this user. | |

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |

<a id="usersUsersList"></a>
# **usersUsersList**
> UsersUsersList200Response usersUsersList(id, username, firstName, lastName, email, isStaff, isActive, q, groupId, group, idN, idLte, idLt, idGte, idGt, usernameN, usernameIc, usernameNic, usernameIew, usernameNiew, usernameIsw, usernameNisw, usernameIe, usernameNie, usernameEmpty, firstNameN, firstNameIc, firstNameNic, firstNameIew, firstNameNiew, firstNameIsw, firstNameNisw, firstNameIe, firstNameNie, firstNameEmpty, lastNameN, lastNameIc, lastNameNic, lastNameIew, lastNameNiew, lastNameIsw, lastNameNisw, lastNameIe, lastNameNie, lastNameEmpty, emailN, emailIc, emailNic, emailIew, emailNiew, emailIsw, emailNisw, emailIe, emailNie, emailEmpty, groupIdN, groupN, ordering, limit, offset)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.netbox.dev/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String id = "id_example"; // String | 
    String username = "username_example"; // String | 
    String firstName = "firstName_example"; // String | 
    String lastName = "lastName_example"; // String | 
    String email = "email_example"; // String | 
    String isStaff = "isStaff_example"; // String | 
    String isActive = "isActive_example"; // String | 
    String q = "q_example"; // String | 
    String groupId = "groupId_example"; // String | 
    String group = "group_example"; // String | 
    String idN = "idN_example"; // String | 
    String idLte = "idLte_example"; // String | 
    String idLt = "idLt_example"; // String | 
    String idGte = "idGte_example"; // String | 
    String idGt = "idGt_example"; // String | 
    String usernameN = "usernameN_example"; // String | 
    String usernameIc = "usernameIc_example"; // String | 
    String usernameNic = "usernameNic_example"; // String | 
    String usernameIew = "usernameIew_example"; // String | 
    String usernameNiew = "usernameNiew_example"; // String | 
    String usernameIsw = "usernameIsw_example"; // String | 
    String usernameNisw = "usernameNisw_example"; // String | 
    String usernameIe = "usernameIe_example"; // String | 
    String usernameNie = "usernameNie_example"; // String | 
    String usernameEmpty = "usernameEmpty_example"; // String | 
    String firstNameN = "firstNameN_example"; // String | 
    String firstNameIc = "firstNameIc_example"; // String | 
    String firstNameNic = "firstNameNic_example"; // String | 
    String firstNameIew = "firstNameIew_example"; // String | 
    String firstNameNiew = "firstNameNiew_example"; // String | 
    String firstNameIsw = "firstNameIsw_example"; // String | 
    String firstNameNisw = "firstNameNisw_example"; // String | 
    String firstNameIe = "firstNameIe_example"; // String | 
    String firstNameNie = "firstNameNie_example"; // String | 
    String firstNameEmpty = "firstNameEmpty_example"; // String | 
    String lastNameN = "lastNameN_example"; // String | 
    String lastNameIc = "lastNameIc_example"; // String | 
    String lastNameNic = "lastNameNic_example"; // String | 
    String lastNameIew = "lastNameIew_example"; // String | 
    String lastNameNiew = "lastNameNiew_example"; // String | 
    String lastNameIsw = "lastNameIsw_example"; // String | 
    String lastNameNisw = "lastNameNisw_example"; // String | 
    String lastNameIe = "lastNameIe_example"; // String | 
    String lastNameNie = "lastNameNie_example"; // String | 
    String lastNameEmpty = "lastNameEmpty_example"; // String | 
    String emailN = "emailN_example"; // String | 
    String emailIc = "emailIc_example"; // String | 
    String emailNic = "emailNic_example"; // String | 
    String emailIew = "emailIew_example"; // String | 
    String emailNiew = "emailNiew_example"; // String | 
    String emailIsw = "emailIsw_example"; // String | 
    String emailNisw = "emailNisw_example"; // String | 
    String emailIe = "emailIe_example"; // String | 
    String emailNie = "emailNie_example"; // String | 
    String emailEmpty = "emailEmpty_example"; // String | 
    String groupIdN = "groupIdN_example"; // String | 
    String groupN = "groupN_example"; // String | 
    String ordering = "ordering_example"; // String | Which field to use when ordering the results.
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      UsersUsersList200Response result = apiInstance.usersUsersList(id, username, firstName, lastName, email, isStaff, isActive, q, groupId, group, idN, idLte, idLt, idGte, idGt, usernameN, usernameIc, usernameNic, usernameIew, usernameNiew, usernameIsw, usernameNisw, usernameIe, usernameNie, usernameEmpty, firstNameN, firstNameIc, firstNameNic, firstNameIew, firstNameNiew, firstNameIsw, firstNameNisw, firstNameIe, firstNameNie, firstNameEmpty, lastNameN, lastNameIc, lastNameNic, lastNameIew, lastNameNiew, lastNameIsw, lastNameNisw, lastNameIe, lastNameNie, lastNameEmpty, emailN, emailIc, emailNic, emailIew, emailNiew, emailIsw, emailNisw, emailIe, emailNie, emailEmpty, groupIdN, groupN, ordering, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersUsersList");
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
| **id** | **String**|  | [optional] |
| **username** | **String**|  | [optional] |
| **firstName** | **String**|  | [optional] |
| **lastName** | **String**|  | [optional] |
| **email** | **String**|  | [optional] |
| **isStaff** | **String**|  | [optional] |
| **isActive** | **String**|  | [optional] |
| **q** | **String**|  | [optional] |
| **groupId** | **String**|  | [optional] |
| **group** | **String**|  | [optional] |
| **idN** | **String**|  | [optional] |
| **idLte** | **String**|  | [optional] |
| **idLt** | **String**|  | [optional] |
| **idGte** | **String**|  | [optional] |
| **idGt** | **String**|  | [optional] |
| **usernameN** | **String**|  | [optional] |
| **usernameIc** | **String**|  | [optional] |
| **usernameNic** | **String**|  | [optional] |
| **usernameIew** | **String**|  | [optional] |
| **usernameNiew** | **String**|  | [optional] |
| **usernameIsw** | **String**|  | [optional] |
| **usernameNisw** | **String**|  | [optional] |
| **usernameIe** | **String**|  | [optional] |
| **usernameNie** | **String**|  | [optional] |
| **usernameEmpty** | **String**|  | [optional] |
| **firstNameN** | **String**|  | [optional] |
| **firstNameIc** | **String**|  | [optional] |
| **firstNameNic** | **String**|  | [optional] |
| **firstNameIew** | **String**|  | [optional] |
| **firstNameNiew** | **String**|  | [optional] |
| **firstNameIsw** | **String**|  | [optional] |
| **firstNameNisw** | **String**|  | [optional] |
| **firstNameIe** | **String**|  | [optional] |
| **firstNameNie** | **String**|  | [optional] |
| **firstNameEmpty** | **String**|  | [optional] |
| **lastNameN** | **String**|  | [optional] |
| **lastNameIc** | **String**|  | [optional] |
| **lastNameNic** | **String**|  | [optional] |
| **lastNameIew** | **String**|  | [optional] |
| **lastNameNiew** | **String**|  | [optional] |
| **lastNameIsw** | **String**|  | [optional] |
| **lastNameNisw** | **String**|  | [optional] |
| **lastNameIe** | **String**|  | [optional] |
| **lastNameNie** | **String**|  | [optional] |
| **lastNameEmpty** | **String**|  | [optional] |
| **emailN** | **String**|  | [optional] |
| **emailIc** | **String**|  | [optional] |
| **emailNic** | **String**|  | [optional] |
| **emailIew** | **String**|  | [optional] |
| **emailNiew** | **String**|  | [optional] |
| **emailIsw** | **String**|  | [optional] |
| **emailNisw** | **String**|  | [optional] |
| **emailIe** | **String**|  | [optional] |
| **emailNie** | **String**|  | [optional] |
| **emailEmpty** | **String**|  | [optional] |
| **groupIdN** | **String**|  | [optional] |
| **groupN** | **String**|  | [optional] |
| **ordering** | **String**| Which field to use when ordering the results. | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |

### Return type

[**UsersUsersList200Response**](UsersUsersList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="usersUsersPartialUpdate"></a>
# **usersUsersPartialUpdate**
> User usersUsersPartialUpdate(id, writableUser)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.netbox.dev/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this user.
    WritableUser writableUser = new WritableUser(); // WritableUser | 
    try {
      User result = apiInstance.usersUsersPartialUpdate(id, writableUser);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersUsersPartialUpdate");
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
| **id** | **Integer**| A unique integer value identifying this user. | |
| **writableUser** | [**WritableUser**](WritableUser.md)|  | |

### Return type

[**User**](User.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="usersUsersRead"></a>
# **usersUsersRead**
> User usersUsersRead(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.netbox.dev/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this user.
    try {
      User result = apiInstance.usersUsersRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersUsersRead");
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
| **id** | **Integer**| A unique integer value identifying this user. | |

### Return type

[**User**](User.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="usersUsersUpdate"></a>
# **usersUsersUpdate**
> User usersUsersUpdate(id, writableUser)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.netbox.dev/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this user.
    WritableUser writableUser = new WritableUser(); // WritableUser | 
    try {
      User result = apiInstance.usersUsersUpdate(id, writableUser);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersUsersUpdate");
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
| **id** | **Integer**| A unique integer value identifying this user. | |
| **writableUser** | [**WritableUser**](WritableUser.md)|  | |

### Return type

[**User**](User.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

