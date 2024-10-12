# TopLevelDomainsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**topLevelDomainsGet**](TopLevelDomainsApi.md#topLevelDomainsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.DomainRegistration/topLevelDomains/{name} | Get details of a top-level domain. |
| [**topLevelDomainsList**](TopLevelDomainsApi.md#topLevelDomainsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.DomainRegistration/topLevelDomains | Get all top-level domains supported for registration. |
| [**topLevelDomainsListAgreements**](TopLevelDomainsApi.md#topLevelDomainsListAgreements) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.DomainRegistration/topLevelDomains/{name}/listAgreements | Gets all legal agreements that user needs to accept before purchasing a domain. |


<a id="topLevelDomainsGet"></a>
# **topLevelDomainsGet**
> TopLevelDomain topLevelDomainsGet(name, subscriptionId, apiVersion)

Get details of a top-level domain.

Get details of a top-level domain.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TopLevelDomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TopLevelDomainsApi apiInstance = new TopLevelDomainsApi(defaultClient);
    String name = "name_example"; // String | Name of the top-level domain.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      TopLevelDomain result = apiInstance.topLevelDomainsGet(name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TopLevelDomainsApi#topLevelDomainsGet");
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
| **name** | **String**| Name of the top-level domain. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**TopLevelDomain**](TopLevelDomain.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

<a id="topLevelDomainsList"></a>
# **topLevelDomainsList**
> TopLevelDomainCollection topLevelDomainsList(subscriptionId, apiVersion)

Get all top-level domains supported for registration.

Get all top-level domains supported for registration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TopLevelDomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TopLevelDomainsApi apiInstance = new TopLevelDomainsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      TopLevelDomainCollection result = apiInstance.topLevelDomainsList(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TopLevelDomainsApi#topLevelDomainsList");
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
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**TopLevelDomainCollection**](TopLevelDomainCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

<a id="topLevelDomainsListAgreements"></a>
# **topLevelDomainsListAgreements**
> TldLegalAgreementCollection topLevelDomainsListAgreements(name, subscriptionId, apiVersion, agreementOption)

Gets all legal agreements that user needs to accept before purchasing a domain.

Gets all legal agreements that user needs to accept before purchasing a domain.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TopLevelDomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TopLevelDomainsApi apiInstance = new TopLevelDomainsApi(defaultClient);
    String name = "name_example"; // String | Name of the top-level domain.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    TopLevelDomainAgreementOption agreementOption = new TopLevelDomainAgreementOption(); // TopLevelDomainAgreementOption | Domain agreement options.
    try {
      TldLegalAgreementCollection result = apiInstance.topLevelDomainsListAgreements(name, subscriptionId, apiVersion, agreementOption);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TopLevelDomainsApi#topLevelDomainsListAgreements");
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
| **name** | **String**| Name of the top-level domain. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |
| **agreementOption** | [**TopLevelDomainAgreementOption**](TopLevelDomainAgreementOption.md)| Domain agreement options. | |

### Return type

[**TldLegalAgreementCollection**](TldLegalAgreementCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

