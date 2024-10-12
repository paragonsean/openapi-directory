# FeaturesApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createOrganizationEarlyAccessFeaturesOptIn_2**](FeaturesApi.md#createOrganizationEarlyAccessFeaturesOptIn_2) | **POST** /organizations/{organizationId}/earlyAccess/features/optIns | Create a new early access feature opt-in for an organization |
| [**deleteOrganizationEarlyAccessFeaturesOptIn_2**](FeaturesApi.md#deleteOrganizationEarlyAccessFeaturesOptIn_2) | **DELETE** /organizations/{organizationId}/earlyAccess/features/optIns/{optInId} | Delete an early access feature opt-in |
| [**getOrganizationEarlyAccessFeaturesOptIn_2**](FeaturesApi.md#getOrganizationEarlyAccessFeaturesOptIn_2) | **GET** /organizations/{organizationId}/earlyAccess/features/optIns/{optInId} | Show an early access feature opt-in for an organization |
| [**getOrganizationEarlyAccessFeaturesOptIns_2**](FeaturesApi.md#getOrganizationEarlyAccessFeaturesOptIns_2) | **GET** /organizations/{organizationId}/earlyAccess/features/optIns | List the early access feature opt-ins for an organization |
| [**getOrganizationEarlyAccessFeatures_2**](FeaturesApi.md#getOrganizationEarlyAccessFeatures_2) | **GET** /organizations/{organizationId}/earlyAccess/features | List the available early access features for organization |
| [**updateOrganizationEarlyAccessFeaturesOptIn_2**](FeaturesApi.md#updateOrganizationEarlyAccessFeaturesOptIn_2) | **PUT** /organizations/{organizationId}/earlyAccess/features/optIns/{optInId} | Update an early access feature opt-in for an organization |


<a id="createOrganizationEarlyAccessFeaturesOptIn_2"></a>
# **createOrganizationEarlyAccessFeaturesOptIn_2**
> Object createOrganizationEarlyAccessFeaturesOptIn_2(organizationId, createOrganizationEarlyAccessFeaturesOptInRequest)

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
import org.openapitools.client.api.FeaturesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    FeaturesApi apiInstance = new FeaturesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    CreateOrganizationEarlyAccessFeaturesOptInRequest createOrganizationEarlyAccessFeaturesOptInRequest = new CreateOrganizationEarlyAccessFeaturesOptInRequest(); // CreateOrganizationEarlyAccessFeaturesOptInRequest | 
    try {
      Object result = apiInstance.createOrganizationEarlyAccessFeaturesOptIn_2(organizationId, createOrganizationEarlyAccessFeaturesOptInRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeaturesApi#createOrganizationEarlyAccessFeaturesOptIn_2");
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

<a id="deleteOrganizationEarlyAccessFeaturesOptIn_2"></a>
# **deleteOrganizationEarlyAccessFeaturesOptIn_2**
> deleteOrganizationEarlyAccessFeaturesOptIn_2(organizationId, optInId)

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
import org.openapitools.client.api.FeaturesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    FeaturesApi apiInstance = new FeaturesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String optInId = "optInId_example"; // String | 
    try {
      apiInstance.deleteOrganizationEarlyAccessFeaturesOptIn_2(organizationId, optInId);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeaturesApi#deleteOrganizationEarlyAccessFeaturesOptIn_2");
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

<a id="getOrganizationEarlyAccessFeaturesOptIn_2"></a>
# **getOrganizationEarlyAccessFeaturesOptIn_2**
> Object getOrganizationEarlyAccessFeaturesOptIn_2(organizationId, optInId)

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
import org.openapitools.client.api.FeaturesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    FeaturesApi apiInstance = new FeaturesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String optInId = "optInId_example"; // String | 
    try {
      Object result = apiInstance.getOrganizationEarlyAccessFeaturesOptIn_2(organizationId, optInId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeaturesApi#getOrganizationEarlyAccessFeaturesOptIn_2");
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

<a id="getOrganizationEarlyAccessFeaturesOptIns_2"></a>
# **getOrganizationEarlyAccessFeaturesOptIns_2**
> List&lt;Object&gt; getOrganizationEarlyAccessFeaturesOptIns_2(organizationId)

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
import org.openapitools.client.api.FeaturesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    FeaturesApi apiInstance = new FeaturesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    try {
      List<Object> result = apiInstance.getOrganizationEarlyAccessFeaturesOptIns_2(organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeaturesApi#getOrganizationEarlyAccessFeaturesOptIns_2");
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

<a id="getOrganizationEarlyAccessFeatures_2"></a>
# **getOrganizationEarlyAccessFeatures_2**
> List&lt;Object&gt; getOrganizationEarlyAccessFeatures_2(organizationId)

List the available early access features for organization

List the available early access features for organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeaturesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    FeaturesApi apiInstance = new FeaturesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    try {
      List<Object> result = apiInstance.getOrganizationEarlyAccessFeatures_2(organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeaturesApi#getOrganizationEarlyAccessFeatures_2");
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

<a id="updateOrganizationEarlyAccessFeaturesOptIn_2"></a>
# **updateOrganizationEarlyAccessFeaturesOptIn_2**
> Object updateOrganizationEarlyAccessFeaturesOptIn_2(organizationId, optInId, updateOrganizationEarlyAccessFeaturesOptInRequest)

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
import org.openapitools.client.api.FeaturesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    FeaturesApi apiInstance = new FeaturesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String optInId = "optInId_example"; // String | 
    UpdateOrganizationEarlyAccessFeaturesOptInRequest updateOrganizationEarlyAccessFeaturesOptInRequest = new UpdateOrganizationEarlyAccessFeaturesOptInRequest(); // UpdateOrganizationEarlyAccessFeaturesOptInRequest | 
    try {
      Object result = apiInstance.updateOrganizationEarlyAccessFeaturesOptIn_2(organizationId, optInId, updateOrganizationEarlyAccessFeaturesOptInRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeaturesApi#updateOrganizationEarlyAccessFeaturesOptIn_2");
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

