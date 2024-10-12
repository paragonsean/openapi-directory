# SamlApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createOrganizationSamlIdp_1**](SamlApi.md#createOrganizationSamlIdp_1) | **POST** /organizations/{organizationId}/saml/idps | Create a SAML IdP for your organization. |
| [**deleteOrganizationSamlIdp_1**](SamlApi.md#deleteOrganizationSamlIdp_1) | **DELETE** /organizations/{organizationId}/saml/idps/{idpId} | Remove a SAML IdP in your organization. |
| [**getOrganizationSamlIdp_1**](SamlApi.md#getOrganizationSamlIdp_1) | **GET** /organizations/{organizationId}/saml/idps/{idpId} | Get a SAML IdP from your organization. |
| [**getOrganizationSamlIdps_1**](SamlApi.md#getOrganizationSamlIdps_1) | **GET** /organizations/{organizationId}/saml/idps | List the SAML IdPs in your organization. |
| [**getOrganizationSaml_1**](SamlApi.md#getOrganizationSaml_1) | **GET** /organizations/{organizationId}/saml | Returns the SAML SSO enabled settings for an organization. |
| [**updateOrganizationSamlIdp_1**](SamlApi.md#updateOrganizationSamlIdp_1) | **PUT** /organizations/{organizationId}/saml/idps/{idpId} | Update a SAML IdP in your organization |
| [**updateOrganizationSaml_1**](SamlApi.md#updateOrganizationSaml_1) | **PUT** /organizations/{organizationId}/saml | Updates the SAML SSO enabled settings for an organization. |


<a id="createOrganizationSamlIdp_1"></a>
# **createOrganizationSamlIdp_1**
> List&lt;GetOrganizationSamlIdps200ResponseInner&gt; createOrganizationSamlIdp_1(organizationId, createOrganizationSamlIdpRequest)

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
import org.openapitools.client.api.SamlApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SamlApi apiInstance = new SamlApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    CreateOrganizationSamlIdpRequest createOrganizationSamlIdpRequest = new CreateOrganizationSamlIdpRequest(); // CreateOrganizationSamlIdpRequest | 
    try {
      List<GetOrganizationSamlIdps200ResponseInner> result = apiInstance.createOrganizationSamlIdp_1(organizationId, createOrganizationSamlIdpRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SamlApi#createOrganizationSamlIdp_1");
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

<a id="deleteOrganizationSamlIdp_1"></a>
# **deleteOrganizationSamlIdp_1**
> deleteOrganizationSamlIdp_1(organizationId, idpId)

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
import org.openapitools.client.api.SamlApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SamlApi apiInstance = new SamlApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String idpId = "idpId_example"; // String | 
    try {
      apiInstance.deleteOrganizationSamlIdp_1(organizationId, idpId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SamlApi#deleteOrganizationSamlIdp_1");
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

<a id="getOrganizationSamlIdp_1"></a>
# **getOrganizationSamlIdp_1**
> GetOrganizationSamlIdps200ResponseInner getOrganizationSamlIdp_1(organizationId, idpId)

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
import org.openapitools.client.api.SamlApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SamlApi apiInstance = new SamlApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String idpId = "idpId_example"; // String | 
    try {
      GetOrganizationSamlIdps200ResponseInner result = apiInstance.getOrganizationSamlIdp_1(organizationId, idpId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SamlApi#getOrganizationSamlIdp_1");
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

<a id="getOrganizationSamlIdps_1"></a>
# **getOrganizationSamlIdps_1**
> List&lt;GetOrganizationSamlIdps200ResponseInner&gt; getOrganizationSamlIdps_1(organizationId)

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
import org.openapitools.client.api.SamlApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SamlApi apiInstance = new SamlApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    try {
      List<GetOrganizationSamlIdps200ResponseInner> result = apiInstance.getOrganizationSamlIdps_1(organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SamlApi#getOrganizationSamlIdps_1");
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

<a id="getOrganizationSaml_1"></a>
# **getOrganizationSaml_1**
> GetOrganizationSaml200Response getOrganizationSaml_1(organizationId)

Returns the SAML SSO enabled settings for an organization.

Returns the SAML SSO enabled settings for an organization.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SamlApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SamlApi apiInstance = new SamlApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    try {
      GetOrganizationSaml200Response result = apiInstance.getOrganizationSaml_1(organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SamlApi#getOrganizationSaml_1");
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

[**GetOrganizationSaml200Response**](GetOrganizationSaml200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateOrganizationSamlIdp_1"></a>
# **updateOrganizationSamlIdp_1**
> List&lt;GetOrganizationSamlIdps200ResponseInner&gt; updateOrganizationSamlIdp_1(organizationId, idpId, updateOrganizationSamlIdpRequest)

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
import org.openapitools.client.api.SamlApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SamlApi apiInstance = new SamlApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String idpId = "idpId_example"; // String | 
    UpdateOrganizationSamlIdpRequest updateOrganizationSamlIdpRequest = new UpdateOrganizationSamlIdpRequest(); // UpdateOrganizationSamlIdpRequest | 
    try {
      List<GetOrganizationSamlIdps200ResponseInner> result = apiInstance.updateOrganizationSamlIdp_1(organizationId, idpId, updateOrganizationSamlIdpRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SamlApi#updateOrganizationSamlIdp_1");
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

<a id="updateOrganizationSaml_1"></a>
# **updateOrganizationSaml_1**
> GetOrganizationSaml200Response updateOrganizationSaml_1(organizationId, updateOrganizationSamlRequest)

Updates the SAML SSO enabled settings for an organization.

Updates the SAML SSO enabled settings for an organization.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SamlApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SamlApi apiInstance = new SamlApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    UpdateOrganizationSamlRequest updateOrganizationSamlRequest = new UpdateOrganizationSamlRequest(); // UpdateOrganizationSamlRequest | 
    try {
      GetOrganizationSaml200Response result = apiInstance.updateOrganizationSaml_1(organizationId, updateOrganizationSamlRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SamlApi#updateOrganizationSaml_1");
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
| **updateOrganizationSamlRequest** | [**UpdateOrganizationSamlRequest**](UpdateOrganizationSamlRequest.md)|  | [optional] |

### Return type

[**GetOrganizationSaml200Response**](GetOrganizationSaml200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

