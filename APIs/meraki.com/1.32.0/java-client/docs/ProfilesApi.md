# ProfilesApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createNetworkSensorAlertsProfile_2**](ProfilesApi.md#createNetworkSensorAlertsProfile_2) | **POST** /networks/{networkId}/sensor/alerts/profiles | Creates a sensor alert profile for a network. |
| [**createOrganizationAlertsProfile_2**](ProfilesApi.md#createOrganizationAlertsProfile_2) | **POST** /organizations/{organizationId}/alerts/profiles | Create an organization-wide alert configuration |
| [**deleteNetworkSensorAlertsProfile_2**](ProfilesApi.md#deleteNetworkSensorAlertsProfile_2) | **DELETE** /networks/{networkId}/sensor/alerts/profiles/{id} | Deletes a sensor alert profile from a network. |
| [**deleteOrganizationAlertsProfile_2**](ProfilesApi.md#deleteOrganizationAlertsProfile_2) | **DELETE** /organizations/{organizationId}/alerts/profiles/{alertConfigId} | Removes an organization-wide alert config |
| [**getNetworkSensorAlertsProfile_2**](ProfilesApi.md#getNetworkSensorAlertsProfile_2) | **GET** /networks/{networkId}/sensor/alerts/profiles/{id} | Show details of a sensor alert profile for a network. |
| [**getNetworkSensorAlertsProfiles_2**](ProfilesApi.md#getNetworkSensorAlertsProfiles_2) | **GET** /networks/{networkId}/sensor/alerts/profiles | Lists all sensor alert profiles for a network. |
| [**getNetworkSmProfiles_1**](ProfilesApi.md#getNetworkSmProfiles_1) | **GET** /networks/{networkId}/sm/profiles | List all profiles in a network |
| [**getOrganizationAlertsProfiles_2**](ProfilesApi.md#getOrganizationAlertsProfiles_2) | **GET** /organizations/{organizationId}/alerts/profiles | List all organization-wide alert configurations |
| [**getOrganizationConfigTemplateSwitchProfilePort_2**](ProfilesApi.md#getOrganizationConfigTemplateSwitchProfilePort_2) | **GET** /organizations/{organizationId}/configTemplates/{configTemplateId}/switch/profiles/{profileId}/ports/{portId} | Return a switch profile port |
| [**getOrganizationConfigTemplateSwitchProfilePorts_2**](ProfilesApi.md#getOrganizationConfigTemplateSwitchProfilePorts_2) | **GET** /organizations/{organizationId}/configTemplates/{configTemplateId}/switch/profiles/{profileId}/ports | Return all the ports of a switch profile |
| [**getOrganizationConfigTemplateSwitchProfiles_2**](ProfilesApi.md#getOrganizationConfigTemplateSwitchProfiles_2) | **GET** /organizations/{organizationId}/configTemplates/{configTemplateId}/switch/profiles | List the switch profiles for your switch template configuration |
| [**updateNetworkSensorAlertsProfile_2**](ProfilesApi.md#updateNetworkSensorAlertsProfile_2) | **PUT** /networks/{networkId}/sensor/alerts/profiles/{id} | Updates a sensor alert profile for a network. |
| [**updateOrganizationAlertsProfile_2**](ProfilesApi.md#updateOrganizationAlertsProfile_2) | **PUT** /organizations/{organizationId}/alerts/profiles/{alertConfigId} | Update an organization-wide alert config |
| [**updateOrganizationConfigTemplateSwitchProfilePort_2**](ProfilesApi.md#updateOrganizationConfigTemplateSwitchProfilePort_2) | **PUT** /organizations/{organizationId}/configTemplates/{configTemplateId}/switch/profiles/{profileId}/ports/{portId} | Update a switch profile port |


<a id="createNetworkSensorAlertsProfile_2"></a>
# **createNetworkSensorAlertsProfile_2**
> GetNetworkSensorAlertsProfiles200ResponseInner createNetworkSensorAlertsProfile_2(networkId, createNetworkSensorAlertsProfileRequest)

Creates a sensor alert profile for a network.

Creates a sensor alert profile for a network.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ProfilesApi apiInstance = new ProfilesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkSensorAlertsProfileRequest createNetworkSensorAlertsProfileRequest = new CreateNetworkSensorAlertsProfileRequest(); // CreateNetworkSensorAlertsProfileRequest | 
    try {
      GetNetworkSensorAlertsProfiles200ResponseInner result = apiInstance.createNetworkSensorAlertsProfile_2(networkId, createNetworkSensorAlertsProfileRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfilesApi#createNetworkSensorAlertsProfile_2");
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
| **networkId** | **String**|  | |
| **createNetworkSensorAlertsProfileRequest** | [**CreateNetworkSensorAlertsProfileRequest**](CreateNetworkSensorAlertsProfileRequest.md)|  | |

### Return type

[**GetNetworkSensorAlertsProfiles200ResponseInner**](GetNetworkSensorAlertsProfiles200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="createOrganizationAlertsProfile_2"></a>
# **createOrganizationAlertsProfile_2**
> Object createOrganizationAlertsProfile_2(organizationId, createOrganizationAlertsProfileRequest)

Create an organization-wide alert configuration

Create an organization-wide alert configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ProfilesApi apiInstance = new ProfilesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    CreateOrganizationAlertsProfileRequest createOrganizationAlertsProfileRequest = new CreateOrganizationAlertsProfileRequest(); // CreateOrganizationAlertsProfileRequest | 
    try {
      Object result = apiInstance.createOrganizationAlertsProfile_2(organizationId, createOrganizationAlertsProfileRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfilesApi#createOrganizationAlertsProfile_2");
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
| **createOrganizationAlertsProfileRequest** | [**CreateOrganizationAlertsProfileRequest**](CreateOrganizationAlertsProfileRequest.md)|  | |

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

<a id="deleteNetworkSensorAlertsProfile_2"></a>
# **deleteNetworkSensorAlertsProfile_2**
> deleteNetworkSensorAlertsProfile_2(networkId, id)

Deletes a sensor alert profile from a network.

Deletes a sensor alert profile from a network.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ProfilesApi apiInstance = new ProfilesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String id = "id_example"; // String | 
    try {
      apiInstance.deleteNetworkSensorAlertsProfile_2(networkId, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfilesApi#deleteNetworkSensorAlertsProfile_2");
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
| **networkId** | **String**|  | |
| **id** | **String**|  | |

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

<a id="deleteOrganizationAlertsProfile_2"></a>
# **deleteOrganizationAlertsProfile_2**
> deleteOrganizationAlertsProfile_2(organizationId, alertConfigId)

Removes an organization-wide alert config

Removes an organization-wide alert config

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ProfilesApi apiInstance = new ProfilesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String alertConfigId = "alertConfigId_example"; // String | 
    try {
      apiInstance.deleteOrganizationAlertsProfile_2(organizationId, alertConfigId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfilesApi#deleteOrganizationAlertsProfile_2");
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
| **alertConfigId** | **String**|  | |

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

<a id="getNetworkSensorAlertsProfile_2"></a>
# **getNetworkSensorAlertsProfile_2**
> GetNetworkSensorAlertsProfiles200ResponseInner getNetworkSensorAlertsProfile_2(networkId, id)

Show details of a sensor alert profile for a network.

Show details of a sensor alert profile for a network.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ProfilesApi apiInstance = new ProfilesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String id = "id_example"; // String | 
    try {
      GetNetworkSensorAlertsProfiles200ResponseInner result = apiInstance.getNetworkSensorAlertsProfile_2(networkId, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfilesApi#getNetworkSensorAlertsProfile_2");
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
| **networkId** | **String**|  | |
| **id** | **String**|  | |

### Return type

[**GetNetworkSensorAlertsProfiles200ResponseInner**](GetNetworkSensorAlertsProfiles200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkSensorAlertsProfiles_2"></a>
# **getNetworkSensorAlertsProfiles_2**
> List&lt;GetNetworkSensorAlertsProfiles200ResponseInner&gt; getNetworkSensorAlertsProfiles_2(networkId)

Lists all sensor alert profiles for a network.

Lists all sensor alert profiles for a network.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ProfilesApi apiInstance = new ProfilesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<GetNetworkSensorAlertsProfiles200ResponseInner> result = apiInstance.getNetworkSensorAlertsProfiles_2(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfilesApi#getNetworkSensorAlertsProfiles_2");
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
| **networkId** | **String**|  | |

### Return type

[**List&lt;GetNetworkSensorAlertsProfiles200ResponseInner&gt;**](GetNetworkSensorAlertsProfiles200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkSmProfiles_1"></a>
# **getNetworkSmProfiles_1**
> List&lt;GetNetworkSmProfiles200ResponseInner&gt; getNetworkSmProfiles_1(networkId)

List all profiles in a network

List all profiles in a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ProfilesApi apiInstance = new ProfilesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<GetNetworkSmProfiles200ResponseInner> result = apiInstance.getNetworkSmProfiles_1(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfilesApi#getNetworkSmProfiles_1");
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
| **networkId** | **String**|  | |

### Return type

[**List&lt;GetNetworkSmProfiles200ResponseInner&gt;**](GetNetworkSmProfiles200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getOrganizationAlertsProfiles_2"></a>
# **getOrganizationAlertsProfiles_2**
> List&lt;Object&gt; getOrganizationAlertsProfiles_2(organizationId)

List all organization-wide alert configurations

List all organization-wide alert configurations

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ProfilesApi apiInstance = new ProfilesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    try {
      List<Object> result = apiInstance.getOrganizationAlertsProfiles_2(organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfilesApi#getOrganizationAlertsProfiles_2");
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

<a id="getOrganizationConfigTemplateSwitchProfilePort_2"></a>
# **getOrganizationConfigTemplateSwitchProfilePort_2**
> GetOrganizationConfigTemplateSwitchProfilePorts200ResponseInner getOrganizationConfigTemplateSwitchProfilePort_2(organizationId, configTemplateId, profileId, portId)

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
import org.openapitools.client.api.ProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ProfilesApi apiInstance = new ProfilesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String configTemplateId = "configTemplateId_example"; // String | 
    String profileId = "profileId_example"; // String | 
    String portId = "portId_example"; // String | 
    try {
      GetOrganizationConfigTemplateSwitchProfilePorts200ResponseInner result = apiInstance.getOrganizationConfigTemplateSwitchProfilePort_2(organizationId, configTemplateId, profileId, portId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfilesApi#getOrganizationConfigTemplateSwitchProfilePort_2");
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

<a id="getOrganizationConfigTemplateSwitchProfilePorts_2"></a>
# **getOrganizationConfigTemplateSwitchProfilePorts_2**
> List&lt;GetOrganizationConfigTemplateSwitchProfilePorts200ResponseInner&gt; getOrganizationConfigTemplateSwitchProfilePorts_2(organizationId, configTemplateId, profileId)

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
import org.openapitools.client.api.ProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ProfilesApi apiInstance = new ProfilesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String configTemplateId = "configTemplateId_example"; // String | 
    String profileId = "profileId_example"; // String | 
    try {
      List<GetOrganizationConfigTemplateSwitchProfilePorts200ResponseInner> result = apiInstance.getOrganizationConfigTemplateSwitchProfilePorts_2(organizationId, configTemplateId, profileId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfilesApi#getOrganizationConfigTemplateSwitchProfilePorts_2");
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

<a id="getOrganizationConfigTemplateSwitchProfiles_2"></a>
# **getOrganizationConfigTemplateSwitchProfiles_2**
> GetOrganizationConfigTemplateSwitchProfiles200Response getOrganizationConfigTemplateSwitchProfiles_2(organizationId, configTemplateId)

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
import org.openapitools.client.api.ProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ProfilesApi apiInstance = new ProfilesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String configTemplateId = "configTemplateId_example"; // String | 
    try {
      GetOrganizationConfigTemplateSwitchProfiles200Response result = apiInstance.getOrganizationConfigTemplateSwitchProfiles_2(organizationId, configTemplateId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfilesApi#getOrganizationConfigTemplateSwitchProfiles_2");
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

<a id="updateNetworkSensorAlertsProfile_2"></a>
# **updateNetworkSensorAlertsProfile_2**
> GetNetworkSensorAlertsProfiles200ResponseInner updateNetworkSensorAlertsProfile_2(networkId, id, updateNetworkSensorAlertsProfileRequest)

Updates a sensor alert profile for a network.

Updates a sensor alert profile for a network.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ProfilesApi apiInstance = new ProfilesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String id = "id_example"; // String | 
    UpdateNetworkSensorAlertsProfileRequest updateNetworkSensorAlertsProfileRequest = new UpdateNetworkSensorAlertsProfileRequest(); // UpdateNetworkSensorAlertsProfileRequest | 
    try {
      GetNetworkSensorAlertsProfiles200ResponseInner result = apiInstance.updateNetworkSensorAlertsProfile_2(networkId, id, updateNetworkSensorAlertsProfileRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfilesApi#updateNetworkSensorAlertsProfile_2");
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
| **networkId** | **String**|  | |
| **id** | **String**|  | |
| **updateNetworkSensorAlertsProfileRequest** | [**UpdateNetworkSensorAlertsProfileRequest**](UpdateNetworkSensorAlertsProfileRequest.md)|  | [optional] |

### Return type

[**GetNetworkSensorAlertsProfiles200ResponseInner**](GetNetworkSensorAlertsProfiles200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateOrganizationAlertsProfile_2"></a>
# **updateOrganizationAlertsProfile_2**
> Object updateOrganizationAlertsProfile_2(organizationId, alertConfigId, updateOrganizationAlertsProfileRequest)

Update an organization-wide alert config

Update an organization-wide alert config

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ProfilesApi apiInstance = new ProfilesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String alertConfigId = "alertConfigId_example"; // String | 
    UpdateOrganizationAlertsProfileRequest updateOrganizationAlertsProfileRequest = new UpdateOrganizationAlertsProfileRequest(); // UpdateOrganizationAlertsProfileRequest | 
    try {
      Object result = apiInstance.updateOrganizationAlertsProfile_2(organizationId, alertConfigId, updateOrganizationAlertsProfileRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfilesApi#updateOrganizationAlertsProfile_2");
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
| **alertConfigId** | **String**|  | |
| **updateOrganizationAlertsProfileRequest** | [**UpdateOrganizationAlertsProfileRequest**](UpdateOrganizationAlertsProfileRequest.md)|  | [optional] |

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

<a id="updateOrganizationConfigTemplateSwitchProfilePort_2"></a>
# **updateOrganizationConfigTemplateSwitchProfilePort_2**
> GetOrganizationConfigTemplateSwitchProfilePorts200ResponseInner updateOrganizationConfigTemplateSwitchProfilePort_2(organizationId, configTemplateId, profileId, portId, updateOrganizationConfigTemplateSwitchProfilePortRequest)

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
import org.openapitools.client.api.ProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ProfilesApi apiInstance = new ProfilesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String configTemplateId = "configTemplateId_example"; // String | 
    String profileId = "profileId_example"; // String | 
    String portId = "portId_example"; // String | 
    UpdateOrganizationConfigTemplateSwitchProfilePortRequest updateOrganizationConfigTemplateSwitchProfilePortRequest = new UpdateOrganizationConfigTemplateSwitchProfilePortRequest(); // UpdateOrganizationConfigTemplateSwitchProfilePortRequest | 
    try {
      GetOrganizationConfigTemplateSwitchProfilePorts200ResponseInner result = apiInstance.updateOrganizationConfigTemplateSwitchProfilePort_2(organizationId, configTemplateId, profileId, portId, updateOrganizationConfigTemplateSwitchProfilePortRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfilesApi#updateOrganizationConfigTemplateSwitchProfilePort_2");
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

