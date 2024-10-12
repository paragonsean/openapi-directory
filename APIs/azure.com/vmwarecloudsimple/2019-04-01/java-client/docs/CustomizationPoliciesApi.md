# CustomizationPoliciesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**customizationPoliciesGet**](CustomizationPoliciesApi.md#customizationPoliciesGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.VMwareCloudSimple/locations/{regionId}/privateClouds/{pcName}/customizationPolicies/{customizationPolicyName} | Implements get of customization policy |
| [**customizationPoliciesList**](CustomizationPoliciesApi.md#customizationPoliciesList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.VMwareCloudSimple/locations/{regionId}/privateClouds/{pcName}/customizationPolicies | Implements get of customization policies list |


<a id="customizationPoliciesGet"></a>
# **customizationPoliciesGet**
> CustomizationPolicy customizationPoliciesGet(apiVersion, subscriptionId, regionId, pcName, customizationPolicyName)

Implements get of customization policy

Returns customization policy by its name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomizationPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CustomizationPoliciesApi apiInstance = new CustomizationPoliciesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String regionId = "regionId_example"; // String | The region Id (westus, eastus)
    String pcName = "pcName_example"; // String | The private cloud name
    String customizationPolicyName = "customizationPolicyName_example"; // String | customization policy name
    try {
      CustomizationPolicy result = apiInstance.customizationPoliciesGet(apiVersion, subscriptionId, regionId, pcName, customizationPolicyName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomizationPoliciesApi#customizationPoliciesGet");
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
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription ID. | |
| **regionId** | **String**| The region Id (westus, eastus) | |
| **pcName** | **String**| The private cloud name | |
| **customizationPolicyName** | **String**| customization policy name | |

### Return type

[**CustomizationPolicy**](CustomizationPolicy.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | General Error |  -  |

<a id="customizationPoliciesList"></a>
# **customizationPoliciesList**
> CustomizationPoliciesListResponse customizationPoliciesList(subscriptionId, regionId, pcName, apiVersion, $filter)

Implements get of customization policies list

Returns list of customization policies in region for private cloud

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomizationPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CustomizationPoliciesApi apiInstance = new CustomizationPoliciesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String regionId = "regionId_example"; // String | The region Id (westus, eastus)
    String pcName = "pcName_example"; // String | The private cloud name
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String $filter = "$filter_example"; // String | The filter to apply on the list operation. only type is allowed here as a filter e.g. $filter=type eq 'xxxx'
    try {
      CustomizationPoliciesListResponse result = apiInstance.customizationPoliciesList(subscriptionId, regionId, pcName, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomizationPoliciesApi#customizationPoliciesList");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **regionId** | **String**| The region Id (westus, eastus) | |
| **pcName** | **String**| The private cloud name | |
| **apiVersion** | **String**| Client API version. | |
| **$filter** | **String**| The filter to apply on the list operation. only type is allowed here as a filter e.g. $filter&#x3D;type eq &#39;xxxx&#39; | [optional] |

### Return type

[**CustomizationPoliciesListResponse**](CustomizationPoliciesListResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | General Error |  -  |

