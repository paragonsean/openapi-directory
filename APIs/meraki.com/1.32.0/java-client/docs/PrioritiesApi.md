# PrioritiesApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getOrganizationBrandingPoliciesPriorities_2**](PrioritiesApi.md#getOrganizationBrandingPoliciesPriorities_2) | **GET** /organizations/{organizationId}/brandingPolicies/priorities | Return the branding policy IDs of an organization in priority order |
| [**updateOrganizationBrandingPoliciesPriorities_2**](PrioritiesApi.md#updateOrganizationBrandingPoliciesPriorities_2) | **PUT** /organizations/{organizationId}/brandingPolicies/priorities | Update the priority ordering of an organization&#39;s branding policies. |


<a id="getOrganizationBrandingPoliciesPriorities_2"></a>
# **getOrganizationBrandingPoliciesPriorities_2**
> GetOrganizationBrandingPoliciesPriorities200Response getOrganizationBrandingPoliciesPriorities_2(organizationId)

Return the branding policy IDs of an organization in priority order

Return the branding policy IDs of an organization in priority order. IDs are ordered in ascending order of priority (IDs later in the array have higher priority).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrioritiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    PrioritiesApi apiInstance = new PrioritiesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    try {
      GetOrganizationBrandingPoliciesPriorities200Response result = apiInstance.getOrganizationBrandingPoliciesPriorities_2(organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrioritiesApi#getOrganizationBrandingPoliciesPriorities_2");
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

[**GetOrganizationBrandingPoliciesPriorities200Response**](GetOrganizationBrandingPoliciesPriorities200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateOrganizationBrandingPoliciesPriorities_2"></a>
# **updateOrganizationBrandingPoliciesPriorities_2**
> GetOrganizationBrandingPoliciesPriorities200Response updateOrganizationBrandingPoliciesPriorities_2(organizationId, updateOrganizationBrandingPoliciesPrioritiesRequest)

Update the priority ordering of an organization&#39;s branding policies.

Update the priority ordering of an organization&#39;s branding policies.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrioritiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    PrioritiesApi apiInstance = new PrioritiesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    UpdateOrganizationBrandingPoliciesPrioritiesRequest updateOrganizationBrandingPoliciesPrioritiesRequest = new UpdateOrganizationBrandingPoliciesPrioritiesRequest(); // UpdateOrganizationBrandingPoliciesPrioritiesRequest | 
    try {
      GetOrganizationBrandingPoliciesPriorities200Response result = apiInstance.updateOrganizationBrandingPoliciesPriorities_2(organizationId, updateOrganizationBrandingPoliciesPrioritiesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrioritiesApi#updateOrganizationBrandingPoliciesPriorities_2");
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
| **updateOrganizationBrandingPoliciesPrioritiesRequest** | [**UpdateOrganizationBrandingPoliciesPrioritiesRequest**](UpdateOrganizationBrandingPoliciesPrioritiesRequest.md)|  | [optional] |

### Return type

[**GetOrganizationBrandingPoliciesPriorities200Response**](GetOrganizationBrandingPoliciesPriorities200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

