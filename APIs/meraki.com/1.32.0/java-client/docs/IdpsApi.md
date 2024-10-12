# IdpsApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createOrganizationSamlIdp_2**](IdpsApi.md#createOrganizationSamlIdp_2) | **POST** /organizations/{organizationId}/saml/idps | Create a SAML IdP for your organization. |
| [**deleteOrganizationSamlIdp_2**](IdpsApi.md#deleteOrganizationSamlIdp_2) | **DELETE** /organizations/{organizationId}/saml/idps/{idpId} | Remove a SAML IdP in your organization. |
| [**getOrganizationSamlIdp_2**](IdpsApi.md#getOrganizationSamlIdp_2) | **GET** /organizations/{organizationId}/saml/idps/{idpId} | Get a SAML IdP from your organization. |
| [**getOrganizationSamlIdps_2**](IdpsApi.md#getOrganizationSamlIdps_2) | **GET** /organizations/{organizationId}/saml/idps | List the SAML IdPs in your organization. |
| [**updateOrganizationSamlIdp_2**](IdpsApi.md#updateOrganizationSamlIdp_2) | **PUT** /organizations/{organizationId}/saml/idps/{idpId} | Update a SAML IdP in your organization |


<a id="createOrganizationSamlIdp_2"></a>
# **createOrganizationSamlIdp_2**
> List&lt;GetOrganizationSamlIdps200ResponseInner&gt; createOrganizationSamlIdp_2(organizationId, createOrganizationSamlIdpRequest)

Create a SAML IdP for your organization.

Create a SAML IdP for your organization.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdpsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    IdpsApi apiInstance = new IdpsApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    CreateOrganizationSamlIdpRequest createOrganizationSamlIdpRequest = new CreateOrganizationSamlIdpRequest(); // CreateOrganizationSamlIdpRequest | 
    try {
      List<GetOrganizationSamlIdps200ResponseInner> result = apiInstance.createOrganizationSamlIdp_2(organizationId, createOrganizationSamlIdpRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdpsApi#createOrganizationSamlIdp_2");
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
| **createOrganizationSamlIdpRequest** | [**CreateOrganizationSamlIdpRequest**](CreateOrganizationSamlIdpRequest.md)|  | |

### Return type

[**List&lt;GetOrganizationSamlIdps200ResponseInner&gt;**](GetOrganizationSamlIdps200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation |  -  |

<a id="deleteOrganizationSamlIdp_2"></a>
# **deleteOrganizationSamlIdp_2**
> deleteOrganizationSamlIdp_2(organizationId, idpId)

Remove a SAML IdP in your organization.

Remove a SAML IdP in your organization.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdpsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    IdpsApi apiInstance = new IdpsApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String idpId = "idpId_example"; // String | 
    try {
      apiInstance.deleteOrganizationSamlIdp_2(organizationId, idpId);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdpsApi#deleteOrganizationSamlIdp_2");
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
| **idpId** | **String**|  | |

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

<a id="getOrganizationSamlIdp_2"></a>
# **getOrganizationSamlIdp_2**
> GetOrganizationSamlIdps200ResponseInner getOrganizationSamlIdp_2(organizationId, idpId)

Get a SAML IdP from your organization.

Get a SAML IdP from your organization.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdpsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    IdpsApi apiInstance = new IdpsApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String idpId = "idpId_example"; // String | 
    try {
      GetOrganizationSamlIdps200ResponseInner result = apiInstance.getOrganizationSamlIdp_2(organizationId, idpId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdpsApi#getOrganizationSamlIdp_2");
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
| **idpId** | **String**|  | |

### Return type

[**GetOrganizationSamlIdps200ResponseInner**](GetOrganizationSamlIdps200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getOrganizationSamlIdps_2"></a>
# **getOrganizationSamlIdps_2**
> List&lt;GetOrganizationSamlIdps200ResponseInner&gt; getOrganizationSamlIdps_2(organizationId)

List the SAML IdPs in your organization.

List the SAML IdPs in your organization.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdpsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    IdpsApi apiInstance = new IdpsApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    try {
      List<GetOrganizationSamlIdps200ResponseInner> result = apiInstance.getOrganizationSamlIdps_2(organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdpsApi#getOrganizationSamlIdps_2");
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

[**List&lt;GetOrganizationSamlIdps200ResponseInner&gt;**](GetOrganizationSamlIdps200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateOrganizationSamlIdp_2"></a>
# **updateOrganizationSamlIdp_2**
> List&lt;GetOrganizationSamlIdps200ResponseInner&gt; updateOrganizationSamlIdp_2(organizationId, idpId, updateOrganizationSamlIdpRequest)

Update a SAML IdP in your organization

Update a SAML IdP in your organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdpsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    IdpsApi apiInstance = new IdpsApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String idpId = "idpId_example"; // String | 
    UpdateOrganizationSamlIdpRequest updateOrganizationSamlIdpRequest = new UpdateOrganizationSamlIdpRequest(); // UpdateOrganizationSamlIdpRequest | 
    try {
      List<GetOrganizationSamlIdps200ResponseInner> result = apiInstance.updateOrganizationSamlIdp_2(organizationId, idpId, updateOrganizationSamlIdpRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdpsApi#updateOrganizationSamlIdp_2");
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
| **idpId** | **String**|  | |
| **updateOrganizationSamlIdpRequest** | [**UpdateOrganizationSamlIdpRequest**](UpdateOrganizationSamlIdpRequest.md)|  | [optional] |

### Return type

[**List&lt;GetOrganizationSamlIdps200ResponseInner&gt;**](GetOrganizationSamlIdps200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

