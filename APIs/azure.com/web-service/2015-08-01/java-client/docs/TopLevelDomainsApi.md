# TopLevelDomainsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**topLevelDomainsGetGetTopLevelDomains**](TopLevelDomainsApi.md#topLevelDomainsGetGetTopLevelDomains) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.DomainRegistration/topLevelDomains | Lists all top level domains supported for registration |
| [**topLevelDomainsGetTopLevelDomain**](TopLevelDomainsApi.md#topLevelDomainsGetTopLevelDomain) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.DomainRegistration/topLevelDomains/{name} | Gets details of a top level domain |
| [**topLevelDomainsListTopLevelDomainAgreements**](TopLevelDomainsApi.md#topLevelDomainsListTopLevelDomainAgreements) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.DomainRegistration/topLevelDomains/{name}/listAgreements | Lists legal agreements that user needs to accept before purchasing domain |


<a id="topLevelDomainsGetGetTopLevelDomains"></a>
# **topLevelDomainsGetGetTopLevelDomains**
> TopLevelDomainCollection topLevelDomainsGetGetTopLevelDomains(subscriptionId, apiVersion)

Lists all top level domains supported for registration

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
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      TopLevelDomainCollection result = apiInstance.topLevelDomainsGetGetTopLevelDomains(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TopLevelDomainsApi#topLevelDomainsGetGetTopLevelDomains");
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
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**TopLevelDomainCollection**](TopLevelDomainCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="topLevelDomainsGetTopLevelDomain"></a>
# **topLevelDomainsGetTopLevelDomain**
> TopLevelDomain topLevelDomainsGetTopLevelDomain(name, subscriptionId, apiVersion)

Gets details of a top level domain

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
    String name = "name_example"; // String | Name of the top level domain
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      TopLevelDomain result = apiInstance.topLevelDomainsGetTopLevelDomain(name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TopLevelDomainsApi#topLevelDomainsGetTopLevelDomain");
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
| **name** | **String**| Name of the top level domain | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**TopLevelDomain**](TopLevelDomain.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="topLevelDomainsListTopLevelDomainAgreements"></a>
# **topLevelDomainsListTopLevelDomainAgreements**
> TldLegalAgreementCollection topLevelDomainsListTopLevelDomainAgreements(name, subscriptionId, apiVersion, agreementOption)

Lists legal agreements that user needs to accept before purchasing domain

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
    String name = "name_example"; // String | Name of the top level domain
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    TopLevelDomainAgreementOption agreementOption = new TopLevelDomainAgreementOption(); // TopLevelDomainAgreementOption | Domain agreement options
    try {
      TldLegalAgreementCollection result = apiInstance.topLevelDomainsListTopLevelDomainAgreements(name, subscriptionId, apiVersion, agreementOption);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TopLevelDomainsApi#topLevelDomainsListTopLevelDomainAgreements");
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
| **name** | **String**| Name of the top level domain | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **agreementOption** | [**TopLevelDomainAgreementOption**](TopLevelDomainAgreementOption.md)| Domain agreement options | |

### Return type

[**TldLegalAgreementCollection**](TldLegalAgreementCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

