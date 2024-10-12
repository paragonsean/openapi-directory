# OptInsApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createOrganizationEarlyAccessFeaturesOptIn_3**](OptInsApi.md#createOrganizationEarlyAccessFeaturesOptIn_3) | **POST** /organizations/{organizationId}/earlyAccess/features/optIns | Create a new early access feature opt-in for an organization |
| [**deleteOrganizationEarlyAccessFeaturesOptIn_3**](OptInsApi.md#deleteOrganizationEarlyAccessFeaturesOptIn_3) | **DELETE** /organizations/{organizationId}/earlyAccess/features/optIns/{optInId} | Delete an early access feature opt-in |
| [**getOrganizationEarlyAccessFeaturesOptIn_3**](OptInsApi.md#getOrganizationEarlyAccessFeaturesOptIn_3) | **GET** /organizations/{organizationId}/earlyAccess/features/optIns/{optInId} | Show an early access feature opt-in for an organization |
| [**getOrganizationEarlyAccessFeaturesOptIns_3**](OptInsApi.md#getOrganizationEarlyAccessFeaturesOptIns_3) | **GET** /organizations/{organizationId}/earlyAccess/features/optIns | List the early access feature opt-ins for an organization |
| [**updateOrganizationEarlyAccessFeaturesOptIn_3**](OptInsApi.md#updateOrganizationEarlyAccessFeaturesOptIn_3) | **PUT** /organizations/{organizationId}/earlyAccess/features/optIns/{optInId} | Update an early access feature opt-in for an organization |


<a id="createOrganizationEarlyAccessFeaturesOptIn_3"></a>
# **createOrganizationEarlyAccessFeaturesOptIn_3**
> Object createOrganizationEarlyAccessFeaturesOptIn_3(organizationId, createOrganizationEarlyAccessFeaturesOptInRequest)

Create a new early access feature opt-in for an organization

Create a new early access feature opt-in for an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OptInsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    OptInsApi apiInstance = new OptInsApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    CreateOrganizationEarlyAccessFeaturesOptInRequest createOrganizationEarlyAccessFeaturesOptInRequest = new CreateOrganizationEarlyAccessFeaturesOptInRequest(); // CreateOrganizationEarlyAccessFeaturesOptInRequest | 
    try {
      Object result = apiInstance.createOrganizationEarlyAccessFeaturesOptIn_3(organizationId, createOrganizationEarlyAccessFeaturesOptInRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OptInsApi#createOrganizationEarlyAccessFeaturesOptIn_3");
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
| **createOrganizationEarlyAccessFeaturesOptInRequest** | [**CreateOrganizationEarlyAccessFeaturesOptInRequest**](CreateOrganizationEarlyAccessFeaturesOptInRequest.md)|  | |

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

<a id="deleteOrganizationEarlyAccessFeaturesOptIn_3"></a>
# **deleteOrganizationEarlyAccessFeaturesOptIn_3**
> deleteOrganizationEarlyAccessFeaturesOptIn_3(organizationId, optInId)

Delete an early access feature opt-in

Delete an early access feature opt-in

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OptInsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    OptInsApi apiInstance = new OptInsApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String optInId = "optInId_example"; // String | 
    try {
      apiInstance.deleteOrganizationEarlyAccessFeaturesOptIn_3(organizationId, optInId);
    } catch (ApiException e) {
      System.err.println("Exception when calling OptInsApi#deleteOrganizationEarlyAccessFeaturesOptIn_3");
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
| **optInId** | **String**|  | |

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

<a id="getOrganizationEarlyAccessFeaturesOptIn_3"></a>
# **getOrganizationEarlyAccessFeaturesOptIn_3**
> Object getOrganizationEarlyAccessFeaturesOptIn_3(organizationId, optInId)

Show an early access feature opt-in for an organization

Show an early access feature opt-in for an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OptInsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    OptInsApi apiInstance = new OptInsApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String optInId = "optInId_example"; // String | 
    try {
      Object result = apiInstance.getOrganizationEarlyAccessFeaturesOptIn_3(organizationId, optInId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OptInsApi#getOrganizationEarlyAccessFeaturesOptIn_3");
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
| **optInId** | **String**|  | |

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

<a id="getOrganizationEarlyAccessFeaturesOptIns_3"></a>
# **getOrganizationEarlyAccessFeaturesOptIns_3**
> List&lt;Object&gt; getOrganizationEarlyAccessFeaturesOptIns_3(organizationId)

List the early access feature opt-ins for an organization

List the early access feature opt-ins for an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OptInsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    OptInsApi apiInstance = new OptInsApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    try {
      List<Object> result = apiInstance.getOrganizationEarlyAccessFeaturesOptIns_3(organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OptInsApi#getOrganizationEarlyAccessFeaturesOptIns_3");
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

<a id="updateOrganizationEarlyAccessFeaturesOptIn_3"></a>
# **updateOrganizationEarlyAccessFeaturesOptIn_3**
> Object updateOrganizationEarlyAccessFeaturesOptIn_3(organizationId, optInId, updateOrganizationEarlyAccessFeaturesOptInRequest)

Update an early access feature opt-in for an organization

Update an early access feature opt-in for an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OptInsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    OptInsApi apiInstance = new OptInsApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String optInId = "optInId_example"; // String | 
    UpdateOrganizationEarlyAccessFeaturesOptInRequest updateOrganizationEarlyAccessFeaturesOptInRequest = new UpdateOrganizationEarlyAccessFeaturesOptInRequest(); // UpdateOrganizationEarlyAccessFeaturesOptInRequest | 
    try {
      Object result = apiInstance.updateOrganizationEarlyAccessFeaturesOptIn_3(organizationId, optInId, updateOrganizationEarlyAccessFeaturesOptInRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OptInsApi#updateOrganizationEarlyAccessFeaturesOptIn_3");
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
| **optInId** | **String**|  | |
| **updateOrganizationEarlyAccessFeaturesOptInRequest** | [**UpdateOrganizationEarlyAccessFeaturesOptInRequest**](UpdateOrganizationEarlyAccessFeaturesOptInRequest.md)|  | [optional] |

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

