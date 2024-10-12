# EarlyAccessApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createOrganizationEarlyAccessFeaturesOptIn_1**](EarlyAccessApi.md#createOrganizationEarlyAccessFeaturesOptIn_1) | **POST** /organizations/{organizationId}/earlyAccess/features/optIns | Create a new early access feature opt-in for an organization |
| [**deleteOrganizationEarlyAccessFeaturesOptIn_1**](EarlyAccessApi.md#deleteOrganizationEarlyAccessFeaturesOptIn_1) | **DELETE** /organizations/{organizationId}/earlyAccess/features/optIns/{optInId} | Delete an early access feature opt-in |
| [**getOrganizationEarlyAccessFeaturesOptIn_1**](EarlyAccessApi.md#getOrganizationEarlyAccessFeaturesOptIn_1) | **GET** /organizations/{organizationId}/earlyAccess/features/optIns/{optInId} | Show an early access feature opt-in for an organization |
| [**getOrganizationEarlyAccessFeaturesOptIns_1**](EarlyAccessApi.md#getOrganizationEarlyAccessFeaturesOptIns_1) | **GET** /organizations/{organizationId}/earlyAccess/features/optIns | List the early access feature opt-ins for an organization |
| [**getOrganizationEarlyAccessFeatures_1**](EarlyAccessApi.md#getOrganizationEarlyAccessFeatures_1) | **GET** /organizations/{organizationId}/earlyAccess/features | List the available early access features for organization |
| [**updateOrganizationEarlyAccessFeaturesOptIn_1**](EarlyAccessApi.md#updateOrganizationEarlyAccessFeaturesOptIn_1) | **PUT** /organizations/{organizationId}/earlyAccess/features/optIns/{optInId} | Update an early access feature opt-in for an organization |


<a id="createOrganizationEarlyAccessFeaturesOptIn_1"></a>
# **createOrganizationEarlyAccessFeaturesOptIn_1**
> Object createOrganizationEarlyAccessFeaturesOptIn_1(organizationId, createOrganizationEarlyAccessFeaturesOptInRequest)

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
import org.openapitools.client.api.EarlyAccessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    EarlyAccessApi apiInstance = new EarlyAccessApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    CreateOrganizationEarlyAccessFeaturesOptInRequest createOrganizationEarlyAccessFeaturesOptInRequest = new CreateOrganizationEarlyAccessFeaturesOptInRequest(); // CreateOrganizationEarlyAccessFeaturesOptInRequest | 
    try {
      Object result = apiInstance.createOrganizationEarlyAccessFeaturesOptIn_1(organizationId, createOrganizationEarlyAccessFeaturesOptInRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EarlyAccessApi#createOrganizationEarlyAccessFeaturesOptIn_1");
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

<a id="deleteOrganizationEarlyAccessFeaturesOptIn_1"></a>
# **deleteOrganizationEarlyAccessFeaturesOptIn_1**
> deleteOrganizationEarlyAccessFeaturesOptIn_1(organizationId, optInId)

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
import org.openapitools.client.api.EarlyAccessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    EarlyAccessApi apiInstance = new EarlyAccessApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String optInId = "optInId_example"; // String | 
    try {
      apiInstance.deleteOrganizationEarlyAccessFeaturesOptIn_1(organizationId, optInId);
    } catch (ApiException e) {
      System.err.println("Exception when calling EarlyAccessApi#deleteOrganizationEarlyAccessFeaturesOptIn_1");
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

<a id="getOrganizationEarlyAccessFeaturesOptIn_1"></a>
# **getOrganizationEarlyAccessFeaturesOptIn_1**
> Object getOrganizationEarlyAccessFeaturesOptIn_1(organizationId, optInId)

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
import org.openapitools.client.api.EarlyAccessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    EarlyAccessApi apiInstance = new EarlyAccessApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String optInId = "optInId_example"; // String | 
    try {
      Object result = apiInstance.getOrganizationEarlyAccessFeaturesOptIn_1(organizationId, optInId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EarlyAccessApi#getOrganizationEarlyAccessFeaturesOptIn_1");
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

<a id="getOrganizationEarlyAccessFeaturesOptIns_1"></a>
# **getOrganizationEarlyAccessFeaturesOptIns_1**
> List&lt;Object&gt; getOrganizationEarlyAccessFeaturesOptIns_1(organizationId)

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
import org.openapitools.client.api.EarlyAccessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    EarlyAccessApi apiInstance = new EarlyAccessApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    try {
      List<Object> result = apiInstance.getOrganizationEarlyAccessFeaturesOptIns_1(organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EarlyAccessApi#getOrganizationEarlyAccessFeaturesOptIns_1");
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

<a id="getOrganizationEarlyAccessFeatures_1"></a>
# **getOrganizationEarlyAccessFeatures_1**
> List&lt;Object&gt; getOrganizationEarlyAccessFeatures_1(organizationId)

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
import org.openapitools.client.api.EarlyAccessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    EarlyAccessApi apiInstance = new EarlyAccessApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    try {
      List<Object> result = apiInstance.getOrganizationEarlyAccessFeatures_1(organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EarlyAccessApi#getOrganizationEarlyAccessFeatures_1");
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

<a id="updateOrganizationEarlyAccessFeaturesOptIn_1"></a>
# **updateOrganizationEarlyAccessFeaturesOptIn_1**
> Object updateOrganizationEarlyAccessFeaturesOptIn_1(organizationId, optInId, updateOrganizationEarlyAccessFeaturesOptInRequest)

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
import org.openapitools.client.api.EarlyAccessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    EarlyAccessApi apiInstance = new EarlyAccessApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String optInId = "optInId_example"; // String | 
    UpdateOrganizationEarlyAccessFeaturesOptInRequest updateOrganizationEarlyAccessFeaturesOptInRequest = new UpdateOrganizationEarlyAccessFeaturesOptInRequest(); // UpdateOrganizationEarlyAccessFeaturesOptInRequest | 
    try {
      Object result = apiInstance.updateOrganizationEarlyAccessFeaturesOptIn_1(organizationId, optInId, updateOrganizationEarlyAccessFeaturesOptInRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EarlyAccessApi#updateOrganizationEarlyAccessFeaturesOptIn_1");
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

