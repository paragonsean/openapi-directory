# GroupsApi

All URIs are relative to *http://keycloak.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**realmGroupsCountGet**](GroupsApi.md#realmGroupsCountGet) | **GET** /{realm}/groups/count | Returns the groups counts. |
| [**realmGroupsGet**](GroupsApi.md#realmGroupsGet) | **GET** /{realm}/groups | Get group hierarchy. |
| [**realmGroupsIdChildrenPost**](GroupsApi.md#realmGroupsIdChildrenPost) | **POST** /{realm}/groups/{id}/children | Set or create child. |
| [**realmGroupsIdDelete**](GroupsApi.md#realmGroupsIdDelete) | **DELETE** /{realm}/groups/{id} |  |
| [**realmGroupsIdGet**](GroupsApi.md#realmGroupsIdGet) | **GET** /{realm}/groups/{id} |  |
| [**realmGroupsIdManagementPermissionsGet**](GroupsApi.md#realmGroupsIdManagementPermissionsGet) | **GET** /{realm}/groups/{id}/management/permissions | Return object stating whether client Authorization permissions have been initialized or not and a reference |
| [**realmGroupsIdManagementPermissionsPut**](GroupsApi.md#realmGroupsIdManagementPermissionsPut) | **PUT** /{realm}/groups/{id}/management/permissions | Return object stating whether client Authorization permissions have been initialized or not and a reference |
| [**realmGroupsIdMembersGet**](GroupsApi.md#realmGroupsIdMembersGet) | **GET** /{realm}/groups/{id}/members | Get users   Returns a list of users, filtered according to query parameters |
| [**realmGroupsIdPut**](GroupsApi.md#realmGroupsIdPut) | **PUT** /{realm}/groups/{id} | Update group, ignores subgroups. |
| [**realmGroupsPost**](GroupsApi.md#realmGroupsPost) | **POST** /{realm}/groups | create or add a top level realm groupSet or create child. |


<a id="realmGroupsCountGet"></a>
# **realmGroupsCountGet**
> Map&lt;String, Object&gt; realmGroupsCountGet(realm, search, top)

Returns the groups counts.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String search = "search_example"; // String | 
    Boolean top = true; // Boolean | 
    try {
      Map<String, Object> result = apiInstance.realmGroupsCountGet(realm, search, top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#realmGroupsCountGet");
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
| **realm** | **String**| realm name (not id!) | |
| **search** | **String**|  | [optional] |
| **top** | **Boolean**|  | [optional] |

### Return type

**Map&lt;String, Object&gt;**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmGroupsGet"></a>
# **realmGroupsGet**
> List&lt;GroupRepresentation&gt; realmGroupsGet(realm, briefRepresentation, first, max, search)

Get group hierarchy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    Boolean briefRepresentation = true; // Boolean | 
    Integer first = 56; // Integer | 
    Integer max = 56; // Integer | 
    String search = "search_example"; // String | 
    try {
      List<GroupRepresentation> result = apiInstance.realmGroupsGet(realm, briefRepresentation, first, max, search);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#realmGroupsGet");
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
| **realm** | **String**| realm name (not id!) | |
| **briefRepresentation** | **Boolean**|  | [optional] |
| **first** | **Integer**|  | [optional] |
| **max** | **Integer**|  | [optional] |
| **search** | **String**|  | [optional] |

### Return type

[**List&lt;GroupRepresentation&gt;**](GroupRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmGroupsIdChildrenPost"></a>
# **realmGroupsIdChildrenPost**
> realmGroupsIdChildrenPost(realm, id, groupRepresentation)

Set or create child.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | 
    GroupRepresentation groupRepresentation = new GroupRepresentation(); // GroupRepresentation | 
    try {
      apiInstance.realmGroupsIdChildrenPost(realm, id, groupRepresentation);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#realmGroupsIdChildrenPost");
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
| **realm** | **String**| realm name (not id!) | |
| **id** | **String**|  | |
| **groupRepresentation** | [**GroupRepresentation**](GroupRepresentation.md)|  | |

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmGroupsIdDelete"></a>
# **realmGroupsIdDelete**
> realmGroupsIdDelete(realm, id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | 
    try {
      apiInstance.realmGroupsIdDelete(realm, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#realmGroupsIdDelete");
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
| **realm** | **String**| realm name (not id!) | |
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmGroupsIdGet"></a>
# **realmGroupsIdGet**
> GroupRepresentation realmGroupsIdGet(realm, id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | 
    try {
      GroupRepresentation result = apiInstance.realmGroupsIdGet(realm, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#realmGroupsIdGet");
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
| **realm** | **String**| realm name (not id!) | |
| **id** | **String**|  | |

### Return type

[**GroupRepresentation**](GroupRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmGroupsIdManagementPermissionsGet"></a>
# **realmGroupsIdManagementPermissionsGet**
> ManagementPermissionReference realmGroupsIdManagementPermissionsGet(realm, id)

Return object stating whether client Authorization permissions have been initialized or not and a reference

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | 
    try {
      ManagementPermissionReference result = apiInstance.realmGroupsIdManagementPermissionsGet(realm, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#realmGroupsIdManagementPermissionsGet");
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
| **realm** | **String**| realm name (not id!) | |
| **id** | **String**|  | |

### Return type

[**ManagementPermissionReference**](ManagementPermissionReference.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmGroupsIdManagementPermissionsPut"></a>
# **realmGroupsIdManagementPermissionsPut**
> ManagementPermissionReference realmGroupsIdManagementPermissionsPut(realm, id, managementPermissionReference)

Return object stating whether client Authorization permissions have been initialized or not and a reference

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | 
    ManagementPermissionReference managementPermissionReference = new ManagementPermissionReference(); // ManagementPermissionReference | 
    try {
      ManagementPermissionReference result = apiInstance.realmGroupsIdManagementPermissionsPut(realm, id, managementPermissionReference);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#realmGroupsIdManagementPermissionsPut");
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
| **realm** | **String**| realm name (not id!) | |
| **id** | **String**|  | |
| **managementPermissionReference** | [**ManagementPermissionReference**](ManagementPermissionReference.md)|  | |

### Return type

[**ManagementPermissionReference**](ManagementPermissionReference.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmGroupsIdMembersGet"></a>
# **realmGroupsIdMembersGet**
> List&lt;UserRepresentation&gt; realmGroupsIdMembersGet(realm, id, briefRepresentation, first, max)

Get users   Returns a list of users, filtered according to query parameters

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | 
    Boolean briefRepresentation = true; // Boolean | Only return basic information (only guaranteed to return id, username, created, first and last name,  email, enabled state, email verification state, federation link, and access.  Note that it means that namely user attributes, required actions, and not before are not returned.)
    Integer first = 56; // Integer | Pagination offset
    Integer max = 56; // Integer | Maximum results size (defaults to 100)
    try {
      List<UserRepresentation> result = apiInstance.realmGroupsIdMembersGet(realm, id, briefRepresentation, first, max);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#realmGroupsIdMembersGet");
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
| **realm** | **String**| realm name (not id!) | |
| **id** | **String**|  | |
| **briefRepresentation** | **Boolean**| Only return basic information (only guaranteed to return id, username, created, first and last name,  email, enabled state, email verification state, federation link, and access.  Note that it means that namely user attributes, required actions, and not before are not returned.) | [optional] |
| **first** | **Integer**| Pagination offset | [optional] |
| **max** | **Integer**| Maximum results size (defaults to 100) | [optional] |

### Return type

[**List&lt;UserRepresentation&gt;**](UserRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmGroupsIdPut"></a>
# **realmGroupsIdPut**
> realmGroupsIdPut(realm, id, groupRepresentation)

Update group, ignores subgroups.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | 
    GroupRepresentation groupRepresentation = new GroupRepresentation(); // GroupRepresentation | 
    try {
      apiInstance.realmGroupsIdPut(realm, id, groupRepresentation);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#realmGroupsIdPut");
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
| **realm** | **String**| realm name (not id!) | |
| **id** | **String**|  | |
| **groupRepresentation** | [**GroupRepresentation**](GroupRepresentation.md)|  | |

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmGroupsPost"></a>
# **realmGroupsPost**
> realmGroupsPost(realm, groupRepresentation)

create or add a top level realm groupSet or create child.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    GroupRepresentation groupRepresentation = new GroupRepresentation(); // GroupRepresentation | 
    try {
      apiInstance.realmGroupsPost(realm, groupRepresentation);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#realmGroupsPost");
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
| **realm** | **String**| realm name (not id!) | |
| **groupRepresentation** | [**GroupRepresentation**](GroupRepresentation.md)|  | |

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

