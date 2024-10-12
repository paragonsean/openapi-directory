# AddonsApi

All URIs are relative to *https://api.clever-cloud.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteOrganisationsIdAddonsAddonIdTagsTag_0**](AddonsApi.md#deleteOrganisationsIdAddonsAddonIdTagsTag_0) | **DELETE** /organisations/{id}/addons/{addonId}/tags/{tag} |  |
| [**deleteOrganisationsIdAddonsAddonId_0**](AddonsApi.md#deleteOrganisationsIdAddonsAddonId_0) | **DELETE** /organisations/{id}/addons/{addonId} |  |
| [**deleteOrganisationsIdApplicationsAppIdAddonsAddonId_0**](AddonsApi.md#deleteOrganisationsIdApplicationsAppIdAddonsAddonId_0) | **DELETE** /organisations/{id}/applications/{appId}/addons/{addonId} |  |
| [**deleteSelfAddonsAddonIdTagsTag_0**](AddonsApi.md#deleteSelfAddonsAddonIdTagsTag_0) | **DELETE** /self/addons/{addonId}/tags/{tag} |  |
| [**deleteSelfAddonsAddonId_0**](AddonsApi.md#deleteSelfAddonsAddonId_0) | **DELETE** /self/addons/{addonId} |  |
| [**deleteSelfApplicationsAppIdAddonsAddonId_0**](AddonsApi.md#deleteSelfApplicationsAppIdAddonsAddonId_0) | **DELETE** /self/applications/{appId}/addons/{addonId} |  |
| [**getConfigProviderEnv_0**](AddonsApi.md#getConfigProviderEnv_0) | **GET** /v4/addon-providers/config-provider/addons/{configurationProviderId}/env | Get provider&#39;s addon environment |
| [**getConfigProvider_0**](AddonsApi.md#getConfigProvider_0) | **GET** /v4/addon-providers/config-provider/addons/{configurationProviderId} | Get Addon provider configuration |
| [**getMatomo_0**](AddonsApi.md#getMatomo_0) | **GET** /v4/addon-providers/addon-matomo/addons/{matomoId} | Get Matomo addon |
| [**getOrganisationsIdAddonsAddonIdApplications_0**](AddonsApi.md#getOrganisationsIdAddonsAddonIdApplications_0) | **GET** /organisations/{id}/addons/{addonId}/applications |  |
| [**getOrganisationsIdAddonsAddonIdEnv_0**](AddonsApi.md#getOrganisationsIdAddonsAddonIdEnv_0) | **GET** /organisations/{id}/addons/{addonId}/env |  |
| [**getOrganisationsIdAddonsAddonIdTags_0**](AddonsApi.md#getOrganisationsIdAddonsAddonIdTags_0) | **GET** /organisations/{id}/addons/{addonId}/tags |  |
| [**getOrganisationsIdAddonsAddonId_0**](AddonsApi.md#getOrganisationsIdAddonsAddonId_0) | **GET** /organisations/{id}/addons/{addonId} |  |
| [**getOrganisationsIdAddons_0**](AddonsApi.md#getOrganisationsIdAddons_0) | **GET** /organisations/{id}/addons |  |
| [**getOrganisationsIdApplicationsAppIdAddonsEnv_0**](AddonsApi.md#getOrganisationsIdApplicationsAppIdAddonsEnv_0) | **GET** /organisations/{id}/applications/{appId}/addons/env |  |
| [**getOrganisationsIdApplicationsAppIdAddons_0**](AddonsApi.md#getOrganisationsIdApplicationsAppIdAddons_0) | **GET** /organisations/{id}/applications/{appId}/addons |  |
| [**getSelfAddonsAddonIdApplications_0**](AddonsApi.md#getSelfAddonsAddonIdApplications_0) | **GET** /self/addons/{addonId}/applications |  |
| [**getSelfAddonsAddonIdEnv_0**](AddonsApi.md#getSelfAddonsAddonIdEnv_0) | **GET** /self/addons/{addonId}/env |  |
| [**getSelfAddonsAddonIdSso_0**](AddonsApi.md#getSelfAddonsAddonIdSso_0) | **GET** /self/addons/{addonId}/sso |  |
| [**getSelfAddonsAddonIdTags_0**](AddonsApi.md#getSelfAddonsAddonIdTags_0) | **GET** /self/addons/{addonId}/tags |  |
| [**getSelfAddonsAddonId_0**](AddonsApi.md#getSelfAddonsAddonId_0) | **GET** /self/addons/{addonId} | Specific addon |
| [**getSelfAddons_0**](AddonsApi.md#getSelfAddons_0) | **GET** /self/addons | Addon |
| [**getSelfApplicationsAppIdAddonsEnv_0**](AddonsApi.md#getSelfApplicationsAppIdAddonsEnv_0) | **GET** /self/applications/{appId}/addons/env |  |
| [**getSelfApplicationsAppIdAddons_0**](AddonsApi.md#getSelfApplicationsAppIdAddons_0) | **GET** /self/applications/{appId}/addons |  |
| [**organisationsIdAddonsAddonIdInstancesGet_0**](AddonsApi.md#organisationsIdAddonsAddonIdInstancesGet_0) | **GET** /organisations/{id}/addons/{addonId}/instances | List instances for this add-on. |
| [**organisationsIdAddonsAddonIdInstancesInstanceIdGet_0**](AddonsApi.md#organisationsIdAddonsAddonIdInstancesInstanceIdGet_0) | **GET** /organisations/{id}/addons/{addonId}/instances/{instanceId} | Get a specific instance for {addonId} |
| [**organisationsIdAddonsAddonIdMigrationsGet_0**](AddonsApi.md#organisationsIdAddonsAddonIdMigrationsGet_0) | **GET** /organisations/{id}/addons/{addonId}/migrations | Get past migrations from add-on. |
| [**organisationsIdAddonsAddonIdMigrationsMigrationIdGet_0**](AddonsApi.md#organisationsIdAddonsAddonIdMigrationsMigrationIdGet_0) | **GET** /organisations/{id}/addons/{addonId}/migrations/{migrationId} | Get a given migration |
| [**organisationsIdAddonsAddonIdMigrationsPost_0**](AddonsApi.md#organisationsIdAddonsAddonIdMigrationsPost_0) | **POST** /organisations/{id}/addons/{addonId}/migrations | Start a new add-on migration |
| [**organisationsIdAddonsAddonIdSsoGet_0**](AddonsApi.md#organisationsIdAddonsAddonIdSsoGet_0) | **GET** /organisations/{id}/addons/{addonId}/sso |  |
| [**organisationsIdAddonsPreordersPost_0**](AddonsApi.md#organisationsIdAddonsPreordersPost_0) | **POST** /organisations/{id}/addons/preorders |  |
| [**postOrganisationsIdAddons_0**](AddonsApi.md#postOrganisationsIdAddons_0) | **POST** /organisations/{id}/addons |  |
| [**postOrganisationsIdApplicationsAppIdAddons_0**](AddonsApi.md#postOrganisationsIdApplicationsAppIdAddons_0) | **POST** /organisations/{id}/applications/{appId}/addons |  |
| [**postSelfAddons_0**](AddonsApi.md#postSelfAddons_0) | **POST** /self/addons |  |
| [**postSelfApplicationsAppIdAddons_0**](AddonsApi.md#postSelfApplicationsAppIdAddons_0) | **POST** /self/applications/{appId}/addons |  |
| [**putOrganisationsIdAddonsAddonIdTagsTag_0**](AddonsApi.md#putOrganisationsIdAddonsAddonIdTagsTag_0) | **PUT** /organisations/{id}/addons/{addonId}/tags/{tag} |  |
| [**putOrganisationsIdAddonsAddonId_0**](AddonsApi.md#putOrganisationsIdAddonsAddonId_0) | **PUT** /organisations/{id}/addons/{addonId} |  |
| [**putSelfAddonsAddonIdPlan_0**](AddonsApi.md#putSelfAddonsAddonIdPlan_0) | **PUT** /self/addons/{addonId}/plan |  |
| [**putSelfAddonsAddonIdTagsTag_0**](AddonsApi.md#putSelfAddonsAddonIdTagsTag_0) | **PUT** /self/addons/{addonId}/tags/{tag} |  |
| [**putSelfAddonsAddonId_0**](AddonsApi.md#putSelfAddonsAddonId_0) | **PUT** /self/addons/{addonId} |  |
| [**selfAddonsPreordersPost_0**](AddonsApi.md#selfAddonsPreordersPost_0) | **POST** /self/addons/preorders |  |
| [**updateConfigProviderEnv_0**](AddonsApi.md#updateConfigProviderEnv_0) | **PUT** /v4/addon-providers/config-provider/addons/{configurationProviderId}/env | Update provider&#39;s addon environment |
| [**vendorAddonsPost_0**](AddonsApi.md#vendorAddonsPost_0) | **POST** /vendor//addons |  |


<a id="deleteOrganisationsIdAddonsAddonIdTagsTag_0"></a>
# **deleteOrganisationsIdAddonsAddonIdTagsTag_0**
> deleteOrganisationsIdAddonsAddonIdTagsTag_0(id, tag, addonId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AddonsApi apiInstance = new AddonsApi(defaultClient);
    String id = "id_example"; // String | 
    String tag = "tag_example"; // String | 
    String addonId = "addonId_example"; // String | 
    try {
      apiInstance.deleteOrganisationsIdAddonsAddonIdTagsTag_0(id, tag, addonId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddonsApi#deleteOrganisationsIdAddonsAddonIdTagsTag_0");
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
| **id** | **String**|  | |
| **tag** | **String**|  | |
| **addonId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | deleteAddonTag |  -  |

<a id="deleteOrganisationsIdAddonsAddonId_0"></a>
# **deleteOrganisationsIdAddonsAddonId_0**
> deleteOrganisationsIdAddonsAddonId_0(id, addonId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AddonsApi apiInstance = new AddonsApi(defaultClient);
    String id = "id_example"; // String | 
    String addonId = "addonId_example"; // String | 
    try {
      apiInstance.deleteOrganisationsIdAddonsAddonId_0(id, addonId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddonsApi#deleteOrganisationsIdAddonsAddonId_0");
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
| **id** | **String**|  | |
| **addonId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | deprovisionAddon |  -  |

<a id="deleteOrganisationsIdApplicationsAppIdAddonsAddonId_0"></a>
# **deleteOrganisationsIdApplicationsAppIdAddonsAddonId_0**
> deleteOrganisationsIdApplicationsAppIdAddonsAddonId_0(id, appId, addonId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AddonsApi apiInstance = new AddonsApi(defaultClient);
    String id = "id_example"; // String | 
    String appId = "appId_example"; // String | 
    String addonId = "addonId_example"; // String | 
    try {
      apiInstance.deleteOrganisationsIdApplicationsAppIdAddonsAddonId_0(id, appId, addonId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddonsApi#deleteOrganisationsIdApplicationsAppIdAddonsAddonId_0");
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
| **id** | **String**|  | |
| **appId** | **String**|  | |
| **addonId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | unlinkAddonFromApplication |  -  |

<a id="deleteSelfAddonsAddonIdTagsTag_0"></a>
# **deleteSelfAddonsAddonIdTagsTag_0**
> deleteSelfAddonsAddonIdTagsTag_0(tag, addonId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AddonsApi apiInstance = new AddonsApi(defaultClient);
    String tag = "tag_example"; // String | 
    String addonId = "addonId_example"; // String | 
    try {
      apiInstance.deleteSelfAddonsAddonIdTagsTag_0(tag, addonId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddonsApi#deleteSelfAddonsAddonIdTagsTag_0");
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
| **tag** | **String**|  | |
| **addonId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | deleteAddonTag |  -  |

<a id="deleteSelfAddonsAddonId_0"></a>
# **deleteSelfAddonsAddonId_0**
> deleteSelfAddonsAddonId_0(addonId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AddonsApi apiInstance = new AddonsApi(defaultClient);
    String addonId = "addonId_example"; // String | 
    try {
      apiInstance.deleteSelfAddonsAddonId_0(addonId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddonsApi#deleteSelfAddonsAddonId_0");
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
| **addonId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | deprovisionAddon |  -  |

<a id="deleteSelfApplicationsAppIdAddonsAddonId_0"></a>
# **deleteSelfApplicationsAppIdAddonsAddonId_0**
> deleteSelfApplicationsAppIdAddonsAddonId_0(appId, addonId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AddonsApi apiInstance = new AddonsApi(defaultClient);
    String appId = "appId_example"; // String | 
    String addonId = "addonId_example"; // String | 
    try {
      apiInstance.deleteSelfApplicationsAppIdAddonsAddonId_0(appId, addonId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddonsApi#deleteSelfApplicationsAppIdAddonsAddonId_0");
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
| **appId** | **String**|  | |
| **addonId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | unlinkAddonFromApplication |  -  |

<a id="getConfigProviderEnv_0"></a>
# **getConfigProviderEnv_0**
> List&lt;Object&gt; getConfigProviderEnv_0(configurationProviderId, body)

Get provider&#39;s addon environment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AddonsApi apiInstance = new AddonsApi(defaultClient);
    String configurationProviderId = "configurationProviderId_example"; // String | Automatically added
    String body = "body_example"; // String | 
    try {
      List<Object> result = apiInstance.getConfigProviderEnv_0(configurationProviderId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddonsApi#getConfigProviderEnv_0");
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
| **configurationProviderId** | **String**| Automatically added | |
| **body** | **String**|  | [optional] |

### Return type

**List&lt;Object&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | config provider environment variables |  -  |
| **401** |  |  -  |

<a id="getConfigProvider_0"></a>
# **getConfigProvider_0**
> Object getConfigProvider_0(configurationProviderId, body)

Get Addon provider configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AddonsApi apiInstance = new AddonsApi(defaultClient);
    String configurationProviderId = "configurationProviderId_example"; // String | Automatically added
    String body = "body_example"; // String | 
    try {
      Object result = apiInstance.getConfigProvider_0(configurationProviderId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddonsApi#getConfigProvider_0");
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
| **configurationProviderId** | **String**| Automatically added | |
| **body** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | requested config provider object |  -  |
| **401** |  |  -  |

<a id="getMatomo_0"></a>
# **getMatomo_0**
> Object getMatomo_0(matomoId, body)

Get Matomo addon

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AddonsApi apiInstance = new AddonsApi(defaultClient);
    String matomoId = "matomoId_example"; // String | Automatically added
    String body = "body_example"; // String | 
    try {
      Object result = apiInstance.getMatomo_0(matomoId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddonsApi#getMatomo_0");
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
| **matomoId** | **String**| Automatically added | |
| **body** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | default response |  -  |

<a id="getOrganisationsIdAddonsAddonIdApplications_0"></a>
# **getOrganisationsIdAddonsAddonIdApplications_0**
> List&lt;Application&gt; getOrganisationsIdAddonsAddonIdApplications_0(id, addonId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AddonsApi apiInstance = new AddonsApi(defaultClient);
    String id = "id_example"; // String | 
    String addonId = "addonId_example"; // String | 
    try {
      List<Application> result = apiInstance.getOrganisationsIdAddonsAddonIdApplications_0(id, addonId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddonsApi#getOrganisationsIdAddonsAddonIdApplications_0");
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
| **id** | **String**|  | |
| **addonId** | **String**|  | |

### Return type

[**List&lt;Application&gt;**](Application.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getApplicationsLinkedToAddon |  -  |

<a id="getOrganisationsIdAddonsAddonIdEnv_0"></a>
# **getOrganisationsIdAddonsAddonIdEnv_0**
> List&lt;ListEnv&gt; getOrganisationsIdAddonsAddonIdEnv_0(id, addonId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AddonsApi apiInstance = new AddonsApi(defaultClient);
    String id = "id_example"; // String | 
    String addonId = "addonId_example"; // String | 
    try {
      List<ListEnv> result = apiInstance.getOrganisationsIdAddonsAddonIdEnv_0(id, addonId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddonsApi#getOrganisationsIdAddonsAddonIdEnv_0");
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
| **id** | **String**|  | |
| **addonId** | **String**|  | |

### Return type

[**List&lt;ListEnv&gt;**](ListEnv.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getAddonEnv |  -  |

<a id="getOrganisationsIdAddonsAddonIdTags_0"></a>
# **getOrganisationsIdAddonsAddonIdTags_0**
> List&lt;String&gt; getOrganisationsIdAddonsAddonIdTags_0(id, addonId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AddonsApi apiInstance = new AddonsApi(defaultClient);
    String id = "id_example"; // String | 
    String addonId = "addonId_example"; // String | 
    try {
      List<String> result = apiInstance.getOrganisationsIdAddonsAddonIdTags_0(id, addonId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddonsApi#getOrganisationsIdAddonsAddonIdTags_0");
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
| **id** | **String**|  | |
| **addonId** | **String**|  | |

### Return type

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getAddonTags |  -  |

<a id="getOrganisationsIdAddonsAddonId_0"></a>
# **getOrganisationsIdAddonsAddonId_0**
> Addon getOrganisationsIdAddonsAddonId_0(id, addonId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AddonsApi apiInstance = new AddonsApi(defaultClient);
    String id = "id_example"; // String | 
    String addonId = "addonId_example"; // String | 
    try {
      Addon result = apiInstance.getOrganisationsIdAddonsAddonId_0(id, addonId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddonsApi#getOrganisationsIdAddonsAddonId_0");
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
| **id** | **String**|  | |
| **addonId** | **String**|  | |

### Return type

[**Addon**](Addon.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getAddon |  -  |

<a id="getOrganisationsIdAddons_0"></a>
# **getOrganisationsIdAddons_0**
> List&lt;Addon&gt; getOrganisationsIdAddons_0(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AddonsApi apiInstance = new AddonsApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      List<Addon> result = apiInstance.getOrganisationsIdAddons_0(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddonsApi#getOrganisationsIdAddons_0");
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
| **id** | **String**|  | |

### Return type

[**List&lt;Addon&gt;**](Addon.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getAddons |  -  |

<a id="getOrganisationsIdApplicationsAppIdAddonsEnv_0"></a>
# **getOrganisationsIdApplicationsAppIdAddonsEnv_0**
> List&lt;Env&gt; getOrganisationsIdApplicationsAppIdAddonsEnv_0(id, appId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AddonsApi apiInstance = new AddonsApi(defaultClient);
    String id = "id_example"; // String | 
    String appId = "appId_example"; // String | 
    try {
      List<Env> result = apiInstance.getOrganisationsIdApplicationsAppIdAddonsEnv_0(id, appId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddonsApi#getOrganisationsIdApplicationsAppIdAddonsEnv_0");
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
| **id** | **String**|  | |
| **appId** | **String**|  | |

### Return type

[**List&lt;Env&gt;**](Env.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getEnvOfAddonsLinkedToApplication |  -  |

<a id="getOrganisationsIdApplicationsAppIdAddons_0"></a>
# **getOrganisationsIdApplicationsAppIdAddons_0**
> List&lt;Addon&gt; getOrganisationsIdApplicationsAppIdAddons_0(id, appId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AddonsApi apiInstance = new AddonsApi(defaultClient);
    String id = "id_example"; // String | 
    String appId = "appId_example"; // String | 
    try {
      List<Addon> result = apiInstance.getOrganisationsIdApplicationsAppIdAddons_0(id, appId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddonsApi#getOrganisationsIdApplicationsAppIdAddons_0");
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
| **id** | **String**|  | |
| **appId** | **String**|  | |

### Return type

[**List&lt;Addon&gt;**](Addon.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getAddonsLinkedToApplication |  -  |

<a id="getSelfAddonsAddonIdApplications_0"></a>
# **getSelfAddonsAddonIdApplications_0**
> List&lt;Application&gt; getSelfAddonsAddonIdApplications_0(addonId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AddonsApi apiInstance = new AddonsApi(defaultClient);
    String addonId = "addonId_example"; // String | 
    try {
      List<Application> result = apiInstance.getSelfAddonsAddonIdApplications_0(addonId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddonsApi#getSelfAddonsAddonIdApplications_0");
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
| **addonId** | **String**|  | |

### Return type

[**List&lt;Application&gt;**](Application.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getApplicationsLinkedToAddon |  -  |

<a id="getSelfAddonsAddonIdEnv_0"></a>
# **getSelfAddonsAddonIdEnv_0**
> List&lt;ListEnv&gt; getSelfAddonsAddonIdEnv_0(addonId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AddonsApi apiInstance = new AddonsApi(defaultClient);
    String addonId = "addonId_example"; // String | 
    try {
      List<ListEnv> result = apiInstance.getSelfAddonsAddonIdEnv_0(addonId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddonsApi#getSelfAddonsAddonIdEnv_0");
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
| **addonId** | **String**|  | |

### Return type

[**List&lt;ListEnv&gt;**](ListEnv.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getAddonEnv |  -  |

<a id="getSelfAddonsAddonIdSso_0"></a>
# **getSelfAddonsAddonIdSso_0**
> Sso getSelfAddonsAddonIdSso_0(addonId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AddonsApi apiInstance = new AddonsApi(defaultClient);
    String addonId = "addonId_example"; // String | 
    try {
      Sso result = apiInstance.getSelfAddonsAddonIdSso_0(addonId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddonsApi#getSelfAddonsAddonIdSso_0");
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
| **addonId** | **String**|  | |

### Return type

[**Sso**](Sso.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getSSOData |  -  |

<a id="getSelfAddonsAddonIdTags_0"></a>
# **getSelfAddonsAddonIdTags_0**
> List&lt;String&gt; getSelfAddonsAddonIdTags_0(addonId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AddonsApi apiInstance = new AddonsApi(defaultClient);
    String addonId = "addonId_example"; // String | 
    try {
      List<String> result = apiInstance.getSelfAddonsAddonIdTags_0(addonId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddonsApi#getSelfAddonsAddonIdTags_0");
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
| **addonId** | **String**|  | |

### Return type

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getAddonTags |  -  |

<a id="getSelfAddonsAddonId_0"></a>
# **getSelfAddonsAddonId_0**
> Addon getSelfAddonsAddonId_0(addonId)

Specific addon

Get a specific addon

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AddonsApi apiInstance = new AddonsApi(defaultClient);
    String addonId = "addonId_example"; // String | 
    try {
      Addon result = apiInstance.getSelfAddonsAddonId_0(addonId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddonsApi#getSelfAddonsAddonId_0");
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
| **addonId** | **String**|  | |

### Return type

[**Addon**](Addon.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getAddon |  -  |

<a id="getSelfAddons_0"></a>
# **getSelfAddons_0**
> List&lt;Addon&gt; getSelfAddons_0()

Addon

Get all the addons

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AddonsApi apiInstance = new AddonsApi(defaultClient);
    try {
      List<Addon> result = apiInstance.getSelfAddons_0();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddonsApi#getSelfAddons_0");
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

[**List&lt;Addon&gt;**](Addon.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getAddons |  -  |

<a id="getSelfApplicationsAppIdAddonsEnv_0"></a>
# **getSelfApplicationsAppIdAddonsEnv_0**
> List&lt;Env&gt; getSelfApplicationsAppIdAddonsEnv_0(appId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AddonsApi apiInstance = new AddonsApi(defaultClient);
    String appId = "appId_example"; // String | 
    try {
      List<Env> result = apiInstance.getSelfApplicationsAppIdAddonsEnv_0(appId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddonsApi#getSelfApplicationsAppIdAddonsEnv_0");
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
| **appId** | **String**|  | |

### Return type

[**List&lt;Env&gt;**](Env.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getEnvOfAddonsLinkedToApplication |  -  |

<a id="getSelfApplicationsAppIdAddons_0"></a>
# **getSelfApplicationsAppIdAddons_0**
> List&lt;Addon&gt; getSelfApplicationsAppIdAddons_0(appId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AddonsApi apiInstance = new AddonsApi(defaultClient);
    String appId = "appId_example"; // String | 
    try {
      List<Addon> result = apiInstance.getSelfApplicationsAppIdAddons_0(appId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddonsApi#getSelfApplicationsAppIdAddons_0");
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
| **appId** | **String**|  | |

### Return type

[**List&lt;Addon&gt;**](Addon.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getAddonsLinkedToApplication |  -  |

<a id="organisationsIdAddonsAddonIdInstancesGet_0"></a>
# **organisationsIdAddonsAddonIdInstancesGet_0**
> List&lt;SupernovaInstanceView&gt; organisationsIdAddonsAddonIdInstancesGet_0(id, addonId, deploymentId, withDeleted)

List instances for this add-on.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AddonsApi apiInstance = new AddonsApi(defaultClient);
    String id = "id_example"; // String | 
    String addonId = "addonId_example"; // String | 
    String deploymentId = "deploymentId_example"; // String | 
    String withDeleted = "withDeleted_example"; // String | 
    try {
      List<SupernovaInstanceView> result = apiInstance.organisationsIdAddonsAddonIdInstancesGet_0(id, addonId, deploymentId, withDeleted);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddonsApi#organisationsIdAddonsAddonIdInstancesGet_0");
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
| **id** | **String**|  | |
| **addonId** | **String**|  | |
| **deploymentId** | **String**|  | [optional] |
| **withDeleted** | **String**|  | [optional] |

### Return type

[**List&lt;SupernovaInstanceView&gt;**](SupernovaInstanceView.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The instance list |  -  |

<a id="organisationsIdAddonsAddonIdInstancesInstanceIdGet_0"></a>
# **organisationsIdAddonsAddonIdInstancesInstanceIdGet_0**
> SupernovaInstanceView organisationsIdAddonsAddonIdInstancesInstanceIdGet_0(instanceId, id, addonId)

Get a specific instance for {addonId}

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AddonsApi apiInstance = new AddonsApi(defaultClient);
    String instanceId = "instanceId_example"; // String | 
    String id = "id_example"; // String | 
    String addonId = "addonId_example"; // String | 
    try {
      SupernovaInstanceView result = apiInstance.organisationsIdAddonsAddonIdInstancesInstanceIdGet_0(instanceId, id, addonId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddonsApi#organisationsIdAddonsAddonIdInstancesInstanceIdGet_0");
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
| **instanceId** | **String**|  | |
| **id** | **String**|  | |
| **addonId** | **String**|  | |

### Return type

[**SupernovaInstanceView**](SupernovaInstanceView.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An instance |  -  |

<a id="organisationsIdAddonsAddonIdMigrationsGet_0"></a>
# **organisationsIdAddonsAddonIdMigrationsGet_0**
> List&lt;AddonMigration&gt; organisationsIdAddonsAddonIdMigrationsGet_0(id, addonId)

Get past migrations from add-on.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AddonsApi apiInstance = new AddonsApi(defaultClient);
    String id = "id_example"; // String | 
    String addonId = "addonId_example"; // String | 
    try {
      List<AddonMigration> result = apiInstance.organisationsIdAddonsAddonIdMigrationsGet_0(id, addonId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddonsApi#organisationsIdAddonsAddonIdMigrationsGet_0");
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
| **id** | **String**|  | |
| **addonId** | **String**|  | |

### Return type

[**List&lt;AddonMigration&gt;**](AddonMigration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of migrations |  -  |

<a id="organisationsIdAddonsAddonIdMigrationsMigrationIdGet_0"></a>
# **organisationsIdAddonsAddonIdMigrationsMigrationIdGet_0**
> AddonMigration organisationsIdAddonsAddonIdMigrationsMigrationIdGet_0(migrationId, id, addonId)

Get a given migration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AddonsApi apiInstance = new AddonsApi(defaultClient);
    String migrationId = "migrationId_example"; // String | 
    String id = "id_example"; // String | 
    String addonId = "addonId_example"; // String | 
    try {
      AddonMigration result = apiInstance.organisationsIdAddonsAddonIdMigrationsMigrationIdGet_0(migrationId, id, addonId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddonsApi#organisationsIdAddonsAddonIdMigrationsMigrationIdGet_0");
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
| **migrationId** | **String**|  | |
| **id** | **String**|  | |
| **addonId** | **String**|  | |

### Return type

[**AddonMigration**](AddonMigration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The migration object |  -  |

<a id="organisationsIdAddonsAddonIdMigrationsPost_0"></a>
# **organisationsIdAddonsAddonIdMigrationsPost_0**
> Object organisationsIdAddonsAddonIdMigrationsPost_0(id, addonId, organisationsIdAddonsAddonIdMigrationsPostRequest)

Start a new add-on migration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AddonsApi apiInstance = new AddonsApi(defaultClient);
    String id = "id_example"; // String | 
    String addonId = "addonId_example"; // String | 
    OrganisationsIdAddonsAddonIdMigrationsPostRequest organisationsIdAddonsAddonIdMigrationsPostRequest = new OrganisationsIdAddonsAddonIdMigrationsPostRequest(); // OrganisationsIdAddonsAddonIdMigrationsPostRequest | 
    try {
      Object result = apiInstance.organisationsIdAddonsAddonIdMigrationsPost_0(id, addonId, organisationsIdAddonsAddonIdMigrationsPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddonsApi#organisationsIdAddonsAddonIdMigrationsPost_0");
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
| **id** | **String**|  | |
| **addonId** | **String**|  | |
| **organisationsIdAddonsAddonIdMigrationsPostRequest** | [**OrganisationsIdAddonsAddonIdMigrationsPostRequest**](OrganisationsIdAddonsAddonIdMigrationsPostRequest.md)|  | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Migration has started. |  -  |

<a id="organisationsIdAddonsAddonIdSsoGet_0"></a>
# **organisationsIdAddonsAddonIdSsoGet_0**
> Sso organisationsIdAddonsAddonIdSsoGet_0(id, addonId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AddonsApi apiInstance = new AddonsApi(defaultClient);
    String id = "id_example"; // String | 
    String addonId = "addonId_example"; // String | 
    try {
      Sso result = apiInstance.organisationsIdAddonsAddonIdSsoGet_0(id, addonId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddonsApi#organisationsIdAddonsAddonIdSsoGet_0");
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
| **id** | **String**|  | |
| **addonId** | **String**|  | |

### Return type

[**Sso**](Sso.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getSSOData |  -  |

<a id="organisationsIdAddonsPreordersPost_0"></a>
# **organisationsIdAddonsPreordersPost_0**
> organisationsIdAddonsPreordersPost_0(id, wannabeAddon)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AddonsApi apiInstance = new AddonsApi(defaultClient);
    String id = "id_example"; // String | 
    WannabeAddon wannabeAddon = new WannabeAddon(); // WannabeAddon | 
    try {
      apiInstance.organisationsIdAddonsPreordersPost_0(id, wannabeAddon);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddonsApi#organisationsIdAddonsPreordersPost_0");
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
| **id** | **String**|  | |
| **wannabeAddon** | [**WannabeAddon**](WannabeAddon.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status 200 |  -  |

<a id="postOrganisationsIdAddons_0"></a>
# **postOrganisationsIdAddons_0**
> Addon postOrganisationsIdAddons_0(id, wannabeAddon)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AddonsApi apiInstance = new AddonsApi(defaultClient);
    String id = "id_example"; // String | 
    WannabeAddon wannabeAddon = new WannabeAddon(); // WannabeAddon | 
    try {
      Addon result = apiInstance.postOrganisationsIdAddons_0(id, wannabeAddon);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddonsApi#postOrganisationsIdAddons_0");
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
| **id** | **String**|  | |
| **wannabeAddon** | [**WannabeAddon**](WannabeAddon.md)|  | |

### Return type

[**Addon**](Addon.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | provisionAddon |  -  |

<a id="postOrganisationsIdApplicationsAppIdAddons_0"></a>
# **postOrganisationsIdApplicationsAppIdAddons_0**
> postOrganisationsIdApplicationsAppIdAddons_0(id, appId, body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AddonsApi apiInstance = new AddonsApi(defaultClient);
    String id = "id_example"; // String | 
    String appId = "appId_example"; // String | 
    Body body = new Body(); // Body | 
    try {
      apiInstance.postOrganisationsIdApplicationsAppIdAddons_0(id, appId, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddonsApi#postOrganisationsIdApplicationsAppIdAddons_0");
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
| **id** | **String**|  | |
| **appId** | **String**|  | |
| **body** | [**Body**](Body.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | linkAddonToApplication |  -  |

<a id="postSelfAddons_0"></a>
# **postSelfAddons_0**
> postSelfAddons_0(wannabeAddon)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AddonsApi apiInstance = new AddonsApi(defaultClient);
    WannabeAddon wannabeAddon = new WannabeAddon(); // WannabeAddon | 
    try {
      apiInstance.postSelfAddons_0(wannabeAddon);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddonsApi#postSelfAddons_0");
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
| **wannabeAddon** | [**WannabeAddon**](WannabeAddon.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | provisionAddon |  -  |

<a id="postSelfApplicationsAppIdAddons_0"></a>
# **postSelfApplicationsAppIdAddons_0**
> postSelfApplicationsAppIdAddons_0(appId, body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AddonsApi apiInstance = new AddonsApi(defaultClient);
    String appId = "appId_example"; // String | 
    Body body = new Body(); // Body | 
    try {
      apiInstance.postSelfApplicationsAppIdAddons_0(appId, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddonsApi#postSelfApplicationsAppIdAddons_0");
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
| **appId** | **String**|  | |
| **body** | [**Body**](Body.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | linkAddonToApplication |  -  |

<a id="putOrganisationsIdAddonsAddonIdTagsTag_0"></a>
# **putOrganisationsIdAddonsAddonIdTagsTag_0**
> putOrganisationsIdAddonsAddonIdTagsTag_0(id, tag, addonId, body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AddonsApi apiInstance = new AddonsApi(defaultClient);
    String id = "id_example"; // String | 
    String tag = "tag_example"; // String | 
    String addonId = "addonId_example"; // String | 
    Body body = new Body(); // Body | 
    try {
      apiInstance.putOrganisationsIdAddonsAddonIdTagsTag_0(id, tag, addonId, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddonsApi#putOrganisationsIdAddonsAddonIdTagsTag_0");
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
| **id** | **String**|  | |
| **tag** | **String**|  | |
| **addonId** | **String**|  | |
| **body** | [**Body**](Body.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | addAddonTag |  -  |

<a id="putOrganisationsIdAddonsAddonId_0"></a>
# **putOrganisationsIdAddonsAddonId_0**
> Addon putOrganisationsIdAddonsAddonId_0(id, addonId, wannabeAddon)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AddonsApi apiInstance = new AddonsApi(defaultClient);
    String id = "id_example"; // String | 
    String addonId = "addonId_example"; // String | 
    WannabeAddon wannabeAddon = new WannabeAddon(); // WannabeAddon | 
    try {
      Addon result = apiInstance.putOrganisationsIdAddonsAddonId_0(id, addonId, wannabeAddon);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddonsApi#putOrganisationsIdAddonsAddonId_0");
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
| **id** | **String**|  | |
| **addonId** | **String**|  | |
| **wannabeAddon** | [**WannabeAddon**](WannabeAddon.md)|  | |

### Return type

[**Addon**](Addon.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Update addon information |  -  |

<a id="putSelfAddonsAddonIdPlan_0"></a>
# **putSelfAddonsAddonIdPlan_0**
> putSelfAddonsAddonIdPlan_0(addonId, wannabePlan)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AddonsApi apiInstance = new AddonsApi(defaultClient);
    String addonId = "addonId_example"; // String | 
    WannabePlan wannabePlan = new WannabePlan(); // WannabePlan | 
    try {
      apiInstance.putSelfAddonsAddonIdPlan_0(addonId, wannabePlan);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddonsApi#putSelfAddonsAddonIdPlan_0");
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
| **addonId** | **String**|  | |
| **wannabePlan** | [**WannabePlan**](WannabePlan.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Update plan of an add-on. |  -  |

<a id="putSelfAddonsAddonIdTagsTag_0"></a>
# **putSelfAddonsAddonIdTagsTag_0**
> putSelfAddonsAddonIdTagsTag_0(tag, addonId, body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AddonsApi apiInstance = new AddonsApi(defaultClient);
    String tag = "tag_example"; // String | 
    String addonId = "addonId_example"; // String | 
    Body body = new Body(); // Body | 
    try {
      apiInstance.putSelfAddonsAddonIdTagsTag_0(tag, addonId, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddonsApi#putSelfAddonsAddonIdTagsTag_0");
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
| **tag** | **String**|  | |
| **addonId** | **String**|  | |
| **body** | [**Body**](Body.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | addAddonTag |  -  |

<a id="putSelfAddonsAddonId_0"></a>
# **putSelfAddonsAddonId_0**
> putSelfAddonsAddonId_0(addonId, wannabeAddon)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AddonsApi apiInstance = new AddonsApi(defaultClient);
    String addonId = "addonId_example"; // String | 
    WannabeAddon wannabeAddon = new WannabeAddon(); // WannabeAddon | 
    try {
      apiInstance.putSelfAddonsAddonId_0(addonId, wannabeAddon);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddonsApi#putSelfAddonsAddonId_0");
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
| **addonId** | **String**|  | |
| **wannabeAddon** | [**WannabeAddon**](WannabeAddon.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Update addon informations |  -  |

<a id="selfAddonsPreordersPost_0"></a>
# **selfAddonsPreordersPost_0**
> selfAddonsPreordersPost_0(wannabeAddon)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AddonsApi apiInstance = new AddonsApi(defaultClient);
    WannabeAddon wannabeAddon = new WannabeAddon(); // WannabeAddon | 
    try {
      apiInstance.selfAddonsPreordersPost_0(wannabeAddon);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddonsApi#selfAddonsPreordersPost_0");
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
| **wannabeAddon** | [**WannabeAddon**](WannabeAddon.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status 200 |  -  |

<a id="updateConfigProviderEnv_0"></a>
# **updateConfigProviderEnv_0**
> List&lt;Object&gt; updateConfigProviderEnv_0(configurationProviderId, requestBody)

Update provider&#39;s addon environment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AddonsApi apiInstance = new AddonsApi(defaultClient);
    String configurationProviderId = "configurationProviderId_example"; // String | Automatically added
    List<Object> requestBody = null; // List<Object> | 
    try {
      List<Object> result = apiInstance.updateConfigProviderEnv_0(configurationProviderId, requestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddonsApi#updateConfigProviderEnv_0");
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
| **configurationProviderId** | **String**| Automatically added | |
| **requestBody** | [**List&lt;Object&gt;**](Object.md)|  | |

### Return type

**List&lt;Object&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | updated config providers environment variables |  -  |
| **401** |  |  -  |

<a id="vendorAddonsPost_0"></a>
# **vendorAddonsPost_0**
> vendorAddonsPost_0()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    AddonsApi apiInstance = new AddonsApi(defaultClient);
    try {
      apiInstance.vendorAddonsPost_0();
    } catch (ApiException e) {
      System.err.println("Exception when calling AddonsApi#vendorAddonsPost_0");
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status 200 |  -  |

