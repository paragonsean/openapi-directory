# ConfigTemplatesApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createOrganizationConfigTemplate_1**](ConfigTemplatesApi.md#createOrganizationConfigTemplate_1) | **POST** /organizations/{organizationId}/configTemplates | Create a new configuration template |
| [**deleteOrganizationConfigTemplate_1**](ConfigTemplatesApi.md#deleteOrganizationConfigTemplate_1) | **DELETE** /organizations/{organizationId}/configTemplates/{configTemplateId} | Remove a configuration template |
| [**getOrganizationConfigTemplateSwitchProfilePort_1**](ConfigTemplatesApi.md#getOrganizationConfigTemplateSwitchProfilePort_1) | **GET** /organizations/{organizationId}/configTemplates/{configTemplateId}/switch/profiles/{profileId}/ports/{portId} | Return a switch profile port |
| [**getOrganizationConfigTemplateSwitchProfilePorts_1**](ConfigTemplatesApi.md#getOrganizationConfigTemplateSwitchProfilePorts_1) | **GET** /organizations/{organizationId}/configTemplates/{configTemplateId}/switch/profiles/{profileId}/ports | Return all the ports of a switch profile |
| [**getOrganizationConfigTemplateSwitchProfiles_1**](ConfigTemplatesApi.md#getOrganizationConfigTemplateSwitchProfiles_1) | **GET** /organizations/{organizationId}/configTemplates/{configTemplateId}/switch/profiles | List the switch profiles for your switch template configuration |
| [**getOrganizationConfigTemplate_1**](ConfigTemplatesApi.md#getOrganizationConfigTemplate_1) | **GET** /organizations/{organizationId}/configTemplates/{configTemplateId} | Return a single configuration template |
| [**getOrganizationConfigTemplates_1**](ConfigTemplatesApi.md#getOrganizationConfigTemplates_1) | **GET** /organizations/{organizationId}/configTemplates | List the configuration templates for this organization |
| [**updateOrganizationConfigTemplateSwitchProfilePort_1**](ConfigTemplatesApi.md#updateOrganizationConfigTemplateSwitchProfilePort_1) | **PUT** /organizations/{organizationId}/configTemplates/{configTemplateId}/switch/profiles/{profileId}/ports/{portId} | Update a switch profile port |
| [**updateOrganizationConfigTemplate_1**](ConfigTemplatesApi.md#updateOrganizationConfigTemplate_1) | **PUT** /organizations/{organizationId}/configTemplates/{configTemplateId} | Update a configuration template |


<a id="createOrganizationConfigTemplate_1"></a>
# **createOrganizationConfigTemplate_1**
> Object createOrganizationConfigTemplate_1(organizationId, createOrganizationConfigTemplateRequest)

Create a new configuration template

Create a new configuration template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigTemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ConfigTemplatesApi apiInstance = new ConfigTemplatesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    CreateOrganizationConfigTemplateRequest createOrganizationConfigTemplateRequest = new CreateOrganizationConfigTemplateRequest(); // CreateOrganizationConfigTemplateRequest | 
    try {
      Object result = apiInstance.createOrganizationConfigTemplate_1(organizationId, createOrganizationConfigTemplateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigTemplatesApi#createOrganizationConfigTemplate_1");
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
| **organizationId** | **String**|  | |
| **createOrganizationConfigTemplateRequest** | [**CreateOrganizationConfigTemplateRequest**](CreateOrganizationConfigTemplateRequest.md)|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation |  -  |

<a id="deleteOrganizationConfigTemplate_1"></a>
# **deleteOrganizationConfigTemplate_1**
> deleteOrganizationConfigTemplate_1(organizationId, configTemplateId)

Remove a configuration template

Remove a configuration template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigTemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ConfigTemplatesApi apiInstance = new ConfigTemplatesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String configTemplateId = "configTemplateId_example"; // String | 
    try {
      apiInstance.deleteOrganizationConfigTemplate_1(organizationId, configTemplateId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigTemplatesApi#deleteOrganizationConfigTemplate_1");
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
| **organizationId** | **String**|  | |
| **configTemplateId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successful operation |  -  |

<a id="getOrganizationConfigTemplateSwitchProfilePort_1"></a>
# **getOrganizationConfigTemplateSwitchProfilePort_1**
> GetOrganizationConfigTemplateSwitchProfilePorts200ResponseInner getOrganizationConfigTemplateSwitchProfilePort_1(organizationId, configTemplateId, profileId, portId)

Return a switch profile port

Return a switch profile port

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigTemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ConfigTemplatesApi apiInstance = new ConfigTemplatesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String configTemplateId = "configTemplateId_example"; // String | 
    String profileId = "profileId_example"; // String | 
    String portId = "portId_example"; // String | 
    try {
      GetOrganizationConfigTemplateSwitchProfilePorts200ResponseInner result = apiInstance.getOrganizationConfigTemplateSwitchProfilePort_1(organizationId, configTemplateId, profileId, portId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigTemplatesApi#getOrganizationConfigTemplateSwitchProfilePort_1");
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
| **organizationId** | **String**|  | |
| **configTemplateId** | **String**|  | |
| **profileId** | **String**|  | |
| **portId** | **String**|  | |

### Return type

[**GetOrganizationConfigTemplateSwitchProfilePorts200ResponseInner**](GetOrganizationConfigTemplateSwitchProfilePorts200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getOrganizationConfigTemplateSwitchProfilePorts_1"></a>
# **getOrganizationConfigTemplateSwitchProfilePorts_1**
> List&lt;GetOrganizationConfigTemplateSwitchProfilePorts200ResponseInner&gt; getOrganizationConfigTemplateSwitchProfilePorts_1(organizationId, configTemplateId, profileId)

Return all the ports of a switch profile

Return all the ports of a switch profile

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigTemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ConfigTemplatesApi apiInstance = new ConfigTemplatesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String configTemplateId = "configTemplateId_example"; // String | 
    String profileId = "profileId_example"; // String | 
    try {
      List<GetOrganizationConfigTemplateSwitchProfilePorts200ResponseInner> result = apiInstance.getOrganizationConfigTemplateSwitchProfilePorts_1(organizationId, configTemplateId, profileId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigTemplatesApi#getOrganizationConfigTemplateSwitchProfilePorts_1");
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
| **organizationId** | **String**|  | |
| **configTemplateId** | **String**|  | |
| **profileId** | **String**|  | |

### Return type

[**List&lt;GetOrganizationConfigTemplateSwitchProfilePorts200ResponseInner&gt;**](GetOrganizationConfigTemplateSwitchProfilePorts200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getOrganizationConfigTemplateSwitchProfiles_1"></a>
# **getOrganizationConfigTemplateSwitchProfiles_1**
> GetOrganizationConfigTemplateSwitchProfiles200Response getOrganizationConfigTemplateSwitchProfiles_1(organizationId, configTemplateId)

List the switch profiles for your switch template configuration

List the switch profiles for your switch template configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigTemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ConfigTemplatesApi apiInstance = new ConfigTemplatesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String configTemplateId = "configTemplateId_example"; // String | 
    try {
      GetOrganizationConfigTemplateSwitchProfiles200Response result = apiInstance.getOrganizationConfigTemplateSwitchProfiles_1(organizationId, configTemplateId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigTemplatesApi#getOrganizationConfigTemplateSwitchProfiles_1");
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
| **organizationId** | **String**|  | |
| **configTemplateId** | **String**|  | |

### Return type

[**GetOrganizationConfigTemplateSwitchProfiles200Response**](GetOrganizationConfigTemplateSwitchProfiles200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getOrganizationConfigTemplate_1"></a>
# **getOrganizationConfigTemplate_1**
> Object getOrganizationConfigTemplate_1(organizationId, configTemplateId)

Return a single configuration template

Return a single configuration template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigTemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ConfigTemplatesApi apiInstance = new ConfigTemplatesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String configTemplateId = "configTemplateId_example"; // String | 
    try {
      Object result = apiInstance.getOrganizationConfigTemplate_1(organizationId, configTemplateId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigTemplatesApi#getOrganizationConfigTemplate_1");
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
| **organizationId** | **String**|  | |
| **configTemplateId** | **String**|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getOrganizationConfigTemplates_1"></a>
# **getOrganizationConfigTemplates_1**
> List&lt;Object&gt; getOrganizationConfigTemplates_1(organizationId)

List the configuration templates for this organization

List the configuration templates for this organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigTemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ConfigTemplatesApi apiInstance = new ConfigTemplatesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    try {
      List<Object> result = apiInstance.getOrganizationConfigTemplates_1(organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigTemplatesApi#getOrganizationConfigTemplates_1");
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
| **organizationId** | **String**|  | |

### Return type

**List&lt;Object&gt;**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateOrganizationConfigTemplateSwitchProfilePort_1"></a>
# **updateOrganizationConfigTemplateSwitchProfilePort_1**
> GetOrganizationConfigTemplateSwitchProfilePorts200ResponseInner updateOrganizationConfigTemplateSwitchProfilePort_1(organizationId, configTemplateId, profileId, portId, updateOrganizationConfigTemplateSwitchProfilePortRequest)

Update a switch profile port

Update a switch profile port

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigTemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ConfigTemplatesApi apiInstance = new ConfigTemplatesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String configTemplateId = "configTemplateId_example"; // String | 
    String profileId = "profileId_example"; // String | 
    String portId = "portId_example"; // String | 
    UpdateOrganizationConfigTemplateSwitchProfilePortRequest updateOrganizationConfigTemplateSwitchProfilePortRequest = new UpdateOrganizationConfigTemplateSwitchProfilePortRequest(); // UpdateOrganizationConfigTemplateSwitchProfilePortRequest | 
    try {
      GetOrganizationConfigTemplateSwitchProfilePorts200ResponseInner result = apiInstance.updateOrganizationConfigTemplateSwitchProfilePort_1(organizationId, configTemplateId, profileId, portId, updateOrganizationConfigTemplateSwitchProfilePortRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigTemplatesApi#updateOrganizationConfigTemplateSwitchProfilePort_1");
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
| **organizationId** | **String**|  | |
| **configTemplateId** | **String**|  | |
| **profileId** | **String**|  | |
| **portId** | **String**|  | |
| **updateOrganizationConfigTemplateSwitchProfilePortRequest** | [**UpdateOrganizationConfigTemplateSwitchProfilePortRequest**](UpdateOrganizationConfigTemplateSwitchProfilePortRequest.md)|  | [optional] |

### Return type

[**GetOrganizationConfigTemplateSwitchProfilePorts200ResponseInner**](GetOrganizationConfigTemplateSwitchProfilePorts200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateOrganizationConfigTemplate_1"></a>
# **updateOrganizationConfigTemplate_1**
> Object updateOrganizationConfigTemplate_1(organizationId, configTemplateId, updateOrganizationConfigTemplateRequest)

Update a configuration template

Update a configuration template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigTemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ConfigTemplatesApi apiInstance = new ConfigTemplatesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String configTemplateId = "configTemplateId_example"; // String | 
    UpdateOrganizationConfigTemplateRequest updateOrganizationConfigTemplateRequest = new UpdateOrganizationConfigTemplateRequest(); // UpdateOrganizationConfigTemplateRequest | 
    try {
      Object result = apiInstance.updateOrganizationConfigTemplate_1(organizationId, configTemplateId, updateOrganizationConfigTemplateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigTemplatesApi#updateOrganizationConfigTemplate_1");
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
| **organizationId** | **String**|  | |
| **configTemplateId** | **String**|  | |
| **updateOrganizationConfigTemplateRequest** | [**UpdateOrganizationConfigTemplateRequest**](UpdateOrganizationConfigTemplateRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

