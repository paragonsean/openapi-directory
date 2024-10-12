# RoleMapperApi

All URIs are relative to *http://keycloak.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**realmGroupsIdRoleMappingsGet**](RoleMapperApi.md#realmGroupsIdRoleMappingsGet) | **GET** /{realm}/groups/{id}/role-mappings | Get role mappings |
| [**realmGroupsIdRoleMappingsRealmAvailableGet**](RoleMapperApi.md#realmGroupsIdRoleMappingsRealmAvailableGet) | **GET** /{realm}/groups/{id}/role-mappings/realm/available | Get realm-level roles that can be mapped |
| [**realmGroupsIdRoleMappingsRealmCompositeGet**](RoleMapperApi.md#realmGroupsIdRoleMappingsRealmCompositeGet) | **GET** /{realm}/groups/{id}/role-mappings/realm/composite | Get effective realm-level role mappings   This will recurse all composite roles to get the result. |
| [**realmGroupsIdRoleMappingsRealmDelete**](RoleMapperApi.md#realmGroupsIdRoleMappingsRealmDelete) | **DELETE** /{realm}/groups/{id}/role-mappings/realm | Delete realm-level role mappings |
| [**realmGroupsIdRoleMappingsRealmGet**](RoleMapperApi.md#realmGroupsIdRoleMappingsRealmGet) | **GET** /{realm}/groups/{id}/role-mappings/realm | Get realm-level role mappings |
| [**realmGroupsIdRoleMappingsRealmPost**](RoleMapperApi.md#realmGroupsIdRoleMappingsRealmPost) | **POST** /{realm}/groups/{id}/role-mappings/realm | Add realm-level role mappings to the user |
| [**realmUsersIdRoleMappingsGet**](RoleMapperApi.md#realmUsersIdRoleMappingsGet) | **GET** /{realm}/users/{id}/role-mappings | Get role mappings |
| [**realmUsersIdRoleMappingsRealmAvailableGet**](RoleMapperApi.md#realmUsersIdRoleMappingsRealmAvailableGet) | **GET** /{realm}/users/{id}/role-mappings/realm/available | Get realm-level roles that can be mapped |
| [**realmUsersIdRoleMappingsRealmCompositeGet**](RoleMapperApi.md#realmUsersIdRoleMappingsRealmCompositeGet) | **GET** /{realm}/users/{id}/role-mappings/realm/composite | Get effective realm-level role mappings   This will recurse all composite roles to get the result. |
| [**realmUsersIdRoleMappingsRealmDelete**](RoleMapperApi.md#realmUsersIdRoleMappingsRealmDelete) | **DELETE** /{realm}/users/{id}/role-mappings/realm | Delete realm-level role mappings |
| [**realmUsersIdRoleMappingsRealmGet**](RoleMapperApi.md#realmUsersIdRoleMappingsRealmGet) | **GET** /{realm}/users/{id}/role-mappings/realm | Get realm-level role mappings |
| [**realmUsersIdRoleMappingsRealmPost**](RoleMapperApi.md#realmUsersIdRoleMappingsRealmPost) | **POST** /{realm}/users/{id}/role-mappings/realm | Add realm-level role mappings to the user |


<a id="realmGroupsIdRoleMappingsGet"></a>
# **realmGroupsIdRoleMappingsGet**
> MappingsRepresentation realmGroupsIdRoleMappingsGet(realm, id)

Get role mappings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoleMapperApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RoleMapperApi apiInstance = new RoleMapperApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | 
    try {
      MappingsRepresentation result = apiInstance.realmGroupsIdRoleMappingsGet(realm, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoleMapperApi#realmGroupsIdRoleMappingsGet");
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

[**MappingsRepresentation**](MappingsRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmGroupsIdRoleMappingsRealmAvailableGet"></a>
# **realmGroupsIdRoleMappingsRealmAvailableGet**
> List&lt;RoleRepresentation&gt; realmGroupsIdRoleMappingsRealmAvailableGet(realm, id)

Get realm-level roles that can be mapped

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoleMapperApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RoleMapperApi apiInstance = new RoleMapperApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | 
    try {
      List<RoleRepresentation> result = apiInstance.realmGroupsIdRoleMappingsRealmAvailableGet(realm, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoleMapperApi#realmGroupsIdRoleMappingsRealmAvailableGet");
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

[**List&lt;RoleRepresentation&gt;**](RoleRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmGroupsIdRoleMappingsRealmCompositeGet"></a>
# **realmGroupsIdRoleMappingsRealmCompositeGet**
> List&lt;RoleRepresentation&gt; realmGroupsIdRoleMappingsRealmCompositeGet(realm, id)

Get effective realm-level role mappings   This will recurse all composite roles to get the result.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoleMapperApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RoleMapperApi apiInstance = new RoleMapperApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | 
    try {
      List<RoleRepresentation> result = apiInstance.realmGroupsIdRoleMappingsRealmCompositeGet(realm, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoleMapperApi#realmGroupsIdRoleMappingsRealmCompositeGet");
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

[**List&lt;RoleRepresentation&gt;**](RoleRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmGroupsIdRoleMappingsRealmDelete"></a>
# **realmGroupsIdRoleMappingsRealmDelete**
> realmGroupsIdRoleMappingsRealmDelete(realm, id, roleRepresentation)

Delete realm-level role mappings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoleMapperApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RoleMapperApi apiInstance = new RoleMapperApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | 
    List<RoleRepresentation> roleRepresentation = Arrays.asList(); // List<RoleRepresentation> | 
    try {
      apiInstance.realmGroupsIdRoleMappingsRealmDelete(realm, id, roleRepresentation);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoleMapperApi#realmGroupsIdRoleMappingsRealmDelete");
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
| **roleRepresentation** | [**List&lt;RoleRepresentation&gt;**](RoleRepresentation.md)|  | |

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

<a id="realmGroupsIdRoleMappingsRealmGet"></a>
# **realmGroupsIdRoleMappingsRealmGet**
> List&lt;RoleRepresentation&gt; realmGroupsIdRoleMappingsRealmGet(realm, id)

Get realm-level role mappings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoleMapperApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RoleMapperApi apiInstance = new RoleMapperApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | 
    try {
      List<RoleRepresentation> result = apiInstance.realmGroupsIdRoleMappingsRealmGet(realm, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoleMapperApi#realmGroupsIdRoleMappingsRealmGet");
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

[**List&lt;RoleRepresentation&gt;**](RoleRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmGroupsIdRoleMappingsRealmPost"></a>
# **realmGroupsIdRoleMappingsRealmPost**
> realmGroupsIdRoleMappingsRealmPost(realm, id, roleRepresentation)

Add realm-level role mappings to the user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoleMapperApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RoleMapperApi apiInstance = new RoleMapperApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | 
    List<RoleRepresentation> roleRepresentation = Arrays.asList(); // List<RoleRepresentation> | Roles to add
    try {
      apiInstance.realmGroupsIdRoleMappingsRealmPost(realm, id, roleRepresentation);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoleMapperApi#realmGroupsIdRoleMappingsRealmPost");
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
| **roleRepresentation** | [**List&lt;RoleRepresentation&gt;**](RoleRepresentation.md)| Roles to add | |

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

<a id="realmUsersIdRoleMappingsGet"></a>
# **realmUsersIdRoleMappingsGet**
> MappingsRepresentation realmUsersIdRoleMappingsGet(realm, id)

Get role mappings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoleMapperApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RoleMapperApi apiInstance = new RoleMapperApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | User id
    try {
      MappingsRepresentation result = apiInstance.realmUsersIdRoleMappingsGet(realm, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoleMapperApi#realmUsersIdRoleMappingsGet");
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
| **id** | **String**| User id | |

### Return type

[**MappingsRepresentation**](MappingsRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmUsersIdRoleMappingsRealmAvailableGet"></a>
# **realmUsersIdRoleMappingsRealmAvailableGet**
> List&lt;RoleRepresentation&gt; realmUsersIdRoleMappingsRealmAvailableGet(realm, id)

Get realm-level roles that can be mapped

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoleMapperApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RoleMapperApi apiInstance = new RoleMapperApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | User id
    try {
      List<RoleRepresentation> result = apiInstance.realmUsersIdRoleMappingsRealmAvailableGet(realm, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoleMapperApi#realmUsersIdRoleMappingsRealmAvailableGet");
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
| **id** | **String**| User id | |

### Return type

[**List&lt;RoleRepresentation&gt;**](RoleRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmUsersIdRoleMappingsRealmCompositeGet"></a>
# **realmUsersIdRoleMappingsRealmCompositeGet**
> List&lt;RoleRepresentation&gt; realmUsersIdRoleMappingsRealmCompositeGet(realm, id)

Get effective realm-level role mappings   This will recurse all composite roles to get the result.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoleMapperApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RoleMapperApi apiInstance = new RoleMapperApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | User id
    try {
      List<RoleRepresentation> result = apiInstance.realmUsersIdRoleMappingsRealmCompositeGet(realm, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoleMapperApi#realmUsersIdRoleMappingsRealmCompositeGet");
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
| **id** | **String**| User id | |

### Return type

[**List&lt;RoleRepresentation&gt;**](RoleRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmUsersIdRoleMappingsRealmDelete"></a>
# **realmUsersIdRoleMappingsRealmDelete**
> realmUsersIdRoleMappingsRealmDelete(realm, id, roleRepresentation)

Delete realm-level role mappings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoleMapperApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RoleMapperApi apiInstance = new RoleMapperApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | User id
    List<RoleRepresentation> roleRepresentation = Arrays.asList(); // List<RoleRepresentation> | 
    try {
      apiInstance.realmUsersIdRoleMappingsRealmDelete(realm, id, roleRepresentation);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoleMapperApi#realmUsersIdRoleMappingsRealmDelete");
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
| **id** | **String**| User id | |
| **roleRepresentation** | [**List&lt;RoleRepresentation&gt;**](RoleRepresentation.md)|  | |

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

<a id="realmUsersIdRoleMappingsRealmGet"></a>
# **realmUsersIdRoleMappingsRealmGet**
> List&lt;RoleRepresentation&gt; realmUsersIdRoleMappingsRealmGet(realm, id)

Get realm-level role mappings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoleMapperApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RoleMapperApi apiInstance = new RoleMapperApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | User id
    try {
      List<RoleRepresentation> result = apiInstance.realmUsersIdRoleMappingsRealmGet(realm, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoleMapperApi#realmUsersIdRoleMappingsRealmGet");
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
| **id** | **String**| User id | |

### Return type

[**List&lt;RoleRepresentation&gt;**](RoleRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmUsersIdRoleMappingsRealmPost"></a>
# **realmUsersIdRoleMappingsRealmPost**
> realmUsersIdRoleMappingsRealmPost(realm, id, roleRepresentation)

Add realm-level role mappings to the user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoleMapperApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RoleMapperApi apiInstance = new RoleMapperApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | User id
    List<RoleRepresentation> roleRepresentation = Arrays.asList(); // List<RoleRepresentation> | Roles to add
    try {
      apiInstance.realmUsersIdRoleMappingsRealmPost(realm, id, roleRepresentation);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoleMapperApi#realmUsersIdRoleMappingsRealmPost");
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
| **id** | **String**| User id | |
| **roleRepresentation** | [**List&lt;RoleRepresentation&gt;**](RoleRepresentation.md)| Roles to add | |

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

