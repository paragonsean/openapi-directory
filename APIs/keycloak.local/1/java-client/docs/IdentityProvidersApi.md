# IdentityProvidersApi

All URIs are relative to *http://keycloak.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**realmIdentityProviderImportConfigPost**](IdentityProvidersApi.md#realmIdentityProviderImportConfigPost) | **POST** /{realm}/identity-provider/import-config | Import identity provider from uploaded JSON file |
| [**realmIdentityProviderInstancesAliasDelete**](IdentityProvidersApi.md#realmIdentityProviderInstancesAliasDelete) | **DELETE** /{realm}/identity-provider/instances/{alias} | Delete the identity provider |
| [**realmIdentityProviderInstancesAliasExportGet**](IdentityProvidersApi.md#realmIdentityProviderInstancesAliasExportGet) | **GET** /{realm}/identity-provider/instances/{alias}/export | Export public broker configuration for identity provider |
| [**realmIdentityProviderInstancesAliasGet**](IdentityProvidersApi.md#realmIdentityProviderInstancesAliasGet) | **GET** /{realm}/identity-provider/instances/{alias} | Get the identity provider |
| [**realmIdentityProviderInstancesAliasManagementPermissionsGet**](IdentityProvidersApi.md#realmIdentityProviderInstancesAliasManagementPermissionsGet) | **GET** /{realm}/identity-provider/instances/{alias}/management/permissions | Return object stating whether client Authorization permissions have been initialized or not and a reference |
| [**realmIdentityProviderInstancesAliasManagementPermissionsPut**](IdentityProvidersApi.md#realmIdentityProviderInstancesAliasManagementPermissionsPut) | **PUT** /{realm}/identity-provider/instances/{alias}/management/permissions | Return object stating whether client Authorization permissions have been initialized or not and a reference |
| [**realmIdentityProviderInstancesAliasMapperTypesGet**](IdentityProvidersApi.md#realmIdentityProviderInstancesAliasMapperTypesGet) | **GET** /{realm}/identity-provider/instances/{alias}/mapper-types | Get mapper types for identity provider |
| [**realmIdentityProviderInstancesAliasMappersGet**](IdentityProvidersApi.md#realmIdentityProviderInstancesAliasMappersGet) | **GET** /{realm}/identity-provider/instances/{alias}/mappers | Get mappers for identity provider |
| [**realmIdentityProviderInstancesAliasMappersIdDelete**](IdentityProvidersApi.md#realmIdentityProviderInstancesAliasMappersIdDelete) | **DELETE** /{realm}/identity-provider/instances/{alias}/mappers/{id} | Delete a mapper for the identity provider |
| [**realmIdentityProviderInstancesAliasMappersIdGet**](IdentityProvidersApi.md#realmIdentityProviderInstancesAliasMappersIdGet) | **GET** /{realm}/identity-provider/instances/{alias}/mappers/{id} | Get mapper by id for the identity provider |
| [**realmIdentityProviderInstancesAliasMappersIdPut**](IdentityProvidersApi.md#realmIdentityProviderInstancesAliasMappersIdPut) | **PUT** /{realm}/identity-provider/instances/{alias}/mappers/{id} | Update a mapper for the identity provider |
| [**realmIdentityProviderInstancesAliasMappersPost**](IdentityProvidersApi.md#realmIdentityProviderInstancesAliasMappersPost) | **POST** /{realm}/identity-provider/instances/{alias}/mappers | Add a mapper to identity provider |
| [**realmIdentityProviderInstancesAliasPut**](IdentityProvidersApi.md#realmIdentityProviderInstancesAliasPut) | **PUT** /{realm}/identity-provider/instances/{alias} | Update the identity provider |
| [**realmIdentityProviderInstancesGet**](IdentityProvidersApi.md#realmIdentityProviderInstancesGet) | **GET** /{realm}/identity-provider/instances | Get identity providers |
| [**realmIdentityProviderInstancesPost**](IdentityProvidersApi.md#realmIdentityProviderInstancesPost) | **POST** /{realm}/identity-provider/instances | Create a new identity provider |
| [**realmIdentityProviderProvidersProviderIdGet**](IdentityProvidersApi.md#realmIdentityProviderProvidersProviderIdGet) | **GET** /{realm}/identity-provider/providers/{provider_id} | Get identity providers |


<a id="realmIdentityProviderImportConfigPost"></a>
# **realmIdentityProviderImportConfigPost**
> Map&lt;String, Object&gt; realmIdentityProviderImportConfigPost(realm)

Import identity provider from uploaded JSON file

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdentityProvidersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    IdentityProvidersApi apiInstance = new IdentityProvidersApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    try {
      Map<String, Object> result = apiInstance.realmIdentityProviderImportConfigPost(realm);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdentityProvidersApi#realmIdentityProviderImportConfigPost");
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

<a id="realmIdentityProviderInstancesAliasDelete"></a>
# **realmIdentityProviderInstancesAliasDelete**
> realmIdentityProviderInstancesAliasDelete(realm, alias)

Delete the identity provider

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdentityProvidersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    IdentityProvidersApi apiInstance = new IdentityProvidersApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String alias = "alias_example"; // String | 
    try {
      apiInstance.realmIdentityProviderInstancesAliasDelete(realm, alias);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdentityProvidersApi#realmIdentityProviderInstancesAliasDelete");
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
| **alias** | **String**|  | |

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

<a id="realmIdentityProviderInstancesAliasExportGet"></a>
# **realmIdentityProviderInstancesAliasExportGet**
> realmIdentityProviderInstancesAliasExportGet(realm, alias, format)

Export public broker configuration for identity provider

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdentityProvidersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    IdentityProvidersApi apiInstance = new IdentityProvidersApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String alias = "alias_example"; // String | 
    String format = "format_example"; // String | Format to use
    try {
      apiInstance.realmIdentityProviderInstancesAliasExportGet(realm, alias, format);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdentityProvidersApi#realmIdentityProviderInstancesAliasExportGet");
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
| **alias** | **String**|  | |
| **format** | **String**| Format to use | [optional] |

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

<a id="realmIdentityProviderInstancesAliasGet"></a>
# **realmIdentityProviderInstancesAliasGet**
> IdentityProviderRepresentation realmIdentityProviderInstancesAliasGet(realm, alias)

Get the identity provider

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdentityProvidersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    IdentityProvidersApi apiInstance = new IdentityProvidersApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String alias = "alias_example"; // String | 
    try {
      IdentityProviderRepresentation result = apiInstance.realmIdentityProviderInstancesAliasGet(realm, alias);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdentityProvidersApi#realmIdentityProviderInstancesAliasGet");
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
| **alias** | **String**|  | |

### Return type

[**IdentityProviderRepresentation**](IdentityProviderRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmIdentityProviderInstancesAliasManagementPermissionsGet"></a>
# **realmIdentityProviderInstancesAliasManagementPermissionsGet**
> ManagementPermissionReference realmIdentityProviderInstancesAliasManagementPermissionsGet(realm, alias)

Return object stating whether client Authorization permissions have been initialized or not and a reference

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdentityProvidersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    IdentityProvidersApi apiInstance = new IdentityProvidersApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String alias = "alias_example"; // String | 
    try {
      ManagementPermissionReference result = apiInstance.realmIdentityProviderInstancesAliasManagementPermissionsGet(realm, alias);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdentityProvidersApi#realmIdentityProviderInstancesAliasManagementPermissionsGet");
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
| **alias** | **String**|  | |

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

<a id="realmIdentityProviderInstancesAliasManagementPermissionsPut"></a>
# **realmIdentityProviderInstancesAliasManagementPermissionsPut**
> ManagementPermissionReference realmIdentityProviderInstancesAliasManagementPermissionsPut(realm, alias, managementPermissionReference)

Return object stating whether client Authorization permissions have been initialized or not and a reference

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdentityProvidersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    IdentityProvidersApi apiInstance = new IdentityProvidersApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String alias = "alias_example"; // String | 
    ManagementPermissionReference managementPermissionReference = new ManagementPermissionReference(); // ManagementPermissionReference | 
    try {
      ManagementPermissionReference result = apiInstance.realmIdentityProviderInstancesAliasManagementPermissionsPut(realm, alias, managementPermissionReference);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdentityProvidersApi#realmIdentityProviderInstancesAliasManagementPermissionsPut");
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
| **alias** | **String**|  | |
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

<a id="realmIdentityProviderInstancesAliasMapperTypesGet"></a>
# **realmIdentityProviderInstancesAliasMapperTypesGet**
> realmIdentityProviderInstancesAliasMapperTypesGet(realm, alias)

Get mapper types for identity provider

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdentityProvidersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    IdentityProvidersApi apiInstance = new IdentityProvidersApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String alias = "alias_example"; // String | 
    try {
      apiInstance.realmIdentityProviderInstancesAliasMapperTypesGet(realm, alias);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdentityProvidersApi#realmIdentityProviderInstancesAliasMapperTypesGet");
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
| **alias** | **String**|  | |

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

<a id="realmIdentityProviderInstancesAliasMappersGet"></a>
# **realmIdentityProviderInstancesAliasMappersGet**
> List&lt;IdentityProviderMapperRepresentation&gt; realmIdentityProviderInstancesAliasMappersGet(realm, alias)

Get mappers for identity provider

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdentityProvidersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    IdentityProvidersApi apiInstance = new IdentityProvidersApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String alias = "alias_example"; // String | 
    try {
      List<IdentityProviderMapperRepresentation> result = apiInstance.realmIdentityProviderInstancesAliasMappersGet(realm, alias);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdentityProvidersApi#realmIdentityProviderInstancesAliasMappersGet");
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
| **alias** | **String**|  | |

### Return type

[**List&lt;IdentityProviderMapperRepresentation&gt;**](IdentityProviderMapperRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmIdentityProviderInstancesAliasMappersIdDelete"></a>
# **realmIdentityProviderInstancesAliasMappersIdDelete**
> realmIdentityProviderInstancesAliasMappersIdDelete(realm, alias, id)

Delete a mapper for the identity provider

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdentityProvidersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    IdentityProvidersApi apiInstance = new IdentityProvidersApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String alias = "alias_example"; // String | 
    String id = "id_example"; // String | Mapper id
    try {
      apiInstance.realmIdentityProviderInstancesAliasMappersIdDelete(realm, alias, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdentityProvidersApi#realmIdentityProviderInstancesAliasMappersIdDelete");
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
| **alias** | **String**|  | |
| **id** | **String**| Mapper id | |

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

<a id="realmIdentityProviderInstancesAliasMappersIdGet"></a>
# **realmIdentityProviderInstancesAliasMappersIdGet**
> IdentityProviderMapperRepresentation realmIdentityProviderInstancesAliasMappersIdGet(realm, alias, id)

Get mapper by id for the identity provider

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdentityProvidersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    IdentityProvidersApi apiInstance = new IdentityProvidersApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String alias = "alias_example"; // String | 
    String id = "id_example"; // String | Mapper id
    try {
      IdentityProviderMapperRepresentation result = apiInstance.realmIdentityProviderInstancesAliasMappersIdGet(realm, alias, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdentityProvidersApi#realmIdentityProviderInstancesAliasMappersIdGet");
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
| **alias** | **String**|  | |
| **id** | **String**| Mapper id | |

### Return type

[**IdentityProviderMapperRepresentation**](IdentityProviderMapperRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmIdentityProviderInstancesAliasMappersIdPut"></a>
# **realmIdentityProviderInstancesAliasMappersIdPut**
> realmIdentityProviderInstancesAliasMappersIdPut(realm, alias, id, identityProviderMapperRepresentation)

Update a mapper for the identity provider

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdentityProvidersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    IdentityProvidersApi apiInstance = new IdentityProvidersApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String alias = "alias_example"; // String | 
    String id = "id_example"; // String | Mapper id
    IdentityProviderMapperRepresentation identityProviderMapperRepresentation = new IdentityProviderMapperRepresentation(); // IdentityProviderMapperRepresentation | 
    try {
      apiInstance.realmIdentityProviderInstancesAliasMappersIdPut(realm, alias, id, identityProviderMapperRepresentation);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdentityProvidersApi#realmIdentityProviderInstancesAliasMappersIdPut");
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
| **alias** | **String**|  | |
| **id** | **String**| Mapper id | |
| **identityProviderMapperRepresentation** | [**IdentityProviderMapperRepresentation**](IdentityProviderMapperRepresentation.md)|  | |

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

<a id="realmIdentityProviderInstancesAliasMappersPost"></a>
# **realmIdentityProviderInstancesAliasMappersPost**
> realmIdentityProviderInstancesAliasMappersPost(realm, alias, identityProviderMapperRepresentation)

Add a mapper to identity provider

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdentityProvidersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    IdentityProvidersApi apiInstance = new IdentityProvidersApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String alias = "alias_example"; // String | 
    IdentityProviderMapperRepresentation identityProviderMapperRepresentation = new IdentityProviderMapperRepresentation(); // IdentityProviderMapperRepresentation | 
    try {
      apiInstance.realmIdentityProviderInstancesAliasMappersPost(realm, alias, identityProviderMapperRepresentation);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdentityProvidersApi#realmIdentityProviderInstancesAliasMappersPost");
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
| **alias** | **String**|  | |
| **identityProviderMapperRepresentation** | [**IdentityProviderMapperRepresentation**](IdentityProviderMapperRepresentation.md)|  | |

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

<a id="realmIdentityProviderInstancesAliasPut"></a>
# **realmIdentityProviderInstancesAliasPut**
> realmIdentityProviderInstancesAliasPut(realm, alias, identityProviderRepresentation)

Update the identity provider

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdentityProvidersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    IdentityProvidersApi apiInstance = new IdentityProvidersApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String alias = "alias_example"; // String | 
    IdentityProviderRepresentation identityProviderRepresentation = new IdentityProviderRepresentation(); // IdentityProviderRepresentation | 
    try {
      apiInstance.realmIdentityProviderInstancesAliasPut(realm, alias, identityProviderRepresentation);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdentityProvidersApi#realmIdentityProviderInstancesAliasPut");
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
| **alias** | **String**|  | |
| **identityProviderRepresentation** | [**IdentityProviderRepresentation**](IdentityProviderRepresentation.md)|  | |

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

<a id="realmIdentityProviderInstancesGet"></a>
# **realmIdentityProviderInstancesGet**
> List&lt;IdentityProviderRepresentation&gt; realmIdentityProviderInstancesGet(realm)

Get identity providers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdentityProvidersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    IdentityProvidersApi apiInstance = new IdentityProvidersApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    try {
      List<IdentityProviderRepresentation> result = apiInstance.realmIdentityProviderInstancesGet(realm);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdentityProvidersApi#realmIdentityProviderInstancesGet");
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

### Return type

[**List&lt;IdentityProviderRepresentation&gt;**](IdentityProviderRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmIdentityProviderInstancesPost"></a>
# **realmIdentityProviderInstancesPost**
> realmIdentityProviderInstancesPost(realm, identityProviderRepresentation)

Create a new identity provider

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdentityProvidersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    IdentityProvidersApi apiInstance = new IdentityProvidersApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    IdentityProviderRepresentation identityProviderRepresentation = new IdentityProviderRepresentation(); // IdentityProviderRepresentation | JSON body
    try {
      apiInstance.realmIdentityProviderInstancesPost(realm, identityProviderRepresentation);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdentityProvidersApi#realmIdentityProviderInstancesPost");
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
| **identityProviderRepresentation** | [**IdentityProviderRepresentation**](IdentityProviderRepresentation.md)| JSON body | |

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

<a id="realmIdentityProviderProvidersProviderIdGet"></a>
# **realmIdentityProviderProvidersProviderIdGet**
> realmIdentityProviderProvidersProviderIdGet(realm, providerId)

Get identity providers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdentityProvidersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    IdentityProvidersApi apiInstance = new IdentityProvidersApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String providerId = "providerId_example"; // String | Provider id
    try {
      apiInstance.realmIdentityProviderProvidersProviderIdGet(realm, providerId);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdentityProvidersApi#realmIdentityProviderProvidersProviderIdGet");
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
| **providerId** | **String**| Provider id | |

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

