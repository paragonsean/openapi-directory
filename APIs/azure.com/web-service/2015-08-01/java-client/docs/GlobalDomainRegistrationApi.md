# GlobalDomainRegistrationApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**globalDomainRegistrationCheckDomainAvailability**](GlobalDomainRegistrationApi.md#globalDomainRegistrationCheckDomainAvailability) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.DomainRegistration/checkDomainAvailability | Checks if a domain is available for registration |
| [**globalDomainRegistrationGetAllDomains**](GlobalDomainRegistrationApi.md#globalDomainRegistrationGetAllDomains) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.DomainRegistration/domains | Lists all domains in a subscription |
| [**globalDomainRegistrationGetDomainControlCenterSsoRequest**](GlobalDomainRegistrationApi.md#globalDomainRegistrationGetDomainControlCenterSsoRequest) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.DomainRegistration/generateSsoRequest | Generates a single sign on request for domain management portal |
| [**globalDomainRegistrationListDomainRecommendations**](GlobalDomainRegistrationApi.md#globalDomainRegistrationListDomainRecommendations) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.DomainRegistration/listDomainRecommendations | Lists domain recommendations based on keywords |
| [**globalDomainRegistrationValidateDomainPurchaseInformation**](GlobalDomainRegistrationApi.md#globalDomainRegistrationValidateDomainPurchaseInformation) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.DomainRegistration/validateDomainRegistrationInformation | Validates domain registration information |


<a id="globalDomainRegistrationCheckDomainAvailability"></a>
# **globalDomainRegistrationCheckDomainAvailability**
> DomainAvailablilityCheckResult globalDomainRegistrationCheckDomainAvailability(subscriptionId, apiVersion, identifier)

Checks if a domain is available for registration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GlobalDomainRegistrationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GlobalDomainRegistrationApi apiInstance = new GlobalDomainRegistrationApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    NameIdentifier identifier = new NameIdentifier(); // NameIdentifier | Name of the domain
    try {
      DomainAvailablilityCheckResult result = apiInstance.globalDomainRegistrationCheckDomainAvailability(subscriptionId, apiVersion, identifier);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GlobalDomainRegistrationApi#globalDomainRegistrationCheckDomainAvailability");
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
| **identifier** | [**NameIdentifier**](NameIdentifier.md)| Name of the domain | |

### Return type

[**DomainAvailablilityCheckResult**](DomainAvailablilityCheckResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="globalDomainRegistrationGetAllDomains"></a>
# **globalDomainRegistrationGetAllDomains**
> DomainCollection globalDomainRegistrationGetAllDomains(subscriptionId, apiVersion)

Lists all domains in a subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GlobalDomainRegistrationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GlobalDomainRegistrationApi apiInstance = new GlobalDomainRegistrationApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      DomainCollection result = apiInstance.globalDomainRegistrationGetAllDomains(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GlobalDomainRegistrationApi#globalDomainRegistrationGetAllDomains");
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

[**DomainCollection**](DomainCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="globalDomainRegistrationGetDomainControlCenterSsoRequest"></a>
# **globalDomainRegistrationGetDomainControlCenterSsoRequest**
> DomainControlCenterSsoRequest globalDomainRegistrationGetDomainControlCenterSsoRequest(subscriptionId, apiVersion)

Generates a single sign on request for domain management portal

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GlobalDomainRegistrationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GlobalDomainRegistrationApi apiInstance = new GlobalDomainRegistrationApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      DomainControlCenterSsoRequest result = apiInstance.globalDomainRegistrationGetDomainControlCenterSsoRequest(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GlobalDomainRegistrationApi#globalDomainRegistrationGetDomainControlCenterSsoRequest");
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

[**DomainControlCenterSsoRequest**](DomainControlCenterSsoRequest.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="globalDomainRegistrationListDomainRecommendations"></a>
# **globalDomainRegistrationListDomainRecommendations**
> NameIdentifierCollection globalDomainRegistrationListDomainRecommendations(subscriptionId, apiVersion, parameters)

Lists domain recommendations based on keywords

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GlobalDomainRegistrationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GlobalDomainRegistrationApi apiInstance = new GlobalDomainRegistrationApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    DomainRecommendationSearchParameters parameters = new DomainRecommendationSearchParameters(); // DomainRecommendationSearchParameters | Domain recommendation search parameters
    try {
      NameIdentifierCollection result = apiInstance.globalDomainRegistrationListDomainRecommendations(subscriptionId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GlobalDomainRegistrationApi#globalDomainRegistrationListDomainRecommendations");
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
| **parameters** | [**DomainRecommendationSearchParameters**](DomainRecommendationSearchParameters.md)| Domain recommendation search parameters | |

### Return type

[**NameIdentifierCollection**](NameIdentifierCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="globalDomainRegistrationValidateDomainPurchaseInformation"></a>
# **globalDomainRegistrationValidateDomainPurchaseInformation**
> Object globalDomainRegistrationValidateDomainPurchaseInformation(subscriptionId, apiVersion, domainRegistrationInput)

Validates domain registration information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GlobalDomainRegistrationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GlobalDomainRegistrationApi apiInstance = new GlobalDomainRegistrationApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    DomainRegistrationInput domainRegistrationInput = new DomainRegistrationInput(); // DomainRegistrationInput | Domain registration information
    try {
      Object result = apiInstance.globalDomainRegistrationValidateDomainPurchaseInformation(subscriptionId, apiVersion, domainRegistrationInput);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GlobalDomainRegistrationApi#globalDomainRegistrationValidateDomainPurchaseInformation");
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
| **domainRegistrationInput** | [**DomainRegistrationInput**](DomainRegistrationInput.md)| Domain registration information | |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

