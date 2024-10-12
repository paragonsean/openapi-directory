# MarketplaceRegistrationDefinitionsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**marketplaceRegistrationDefinitionsGet**](MarketplaceRegistrationDefinitionsApi.md#marketplaceRegistrationDefinitionsGet) | **GET** /{scope}/providers/Microsoft.ManagedServices/marketplaceRegistrationDefinitions/{marketplaceIdentifier} |  |
| [**marketplaceRegistrationDefinitionsList**](MarketplaceRegistrationDefinitionsApi.md#marketplaceRegistrationDefinitionsList) | **GET** /{scope}/providers/Microsoft.ManagedServices/marketplaceRegistrationDefinitions |  |


<a id="marketplaceRegistrationDefinitionsGet"></a>
# **marketplaceRegistrationDefinitionsGet**
> RegistrationDefinition marketplaceRegistrationDefinitionsGet(scope, marketplaceIdentifier, apiVersion)



Get the marketplace registration definition for the marketplace identifier.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplaceRegistrationDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    MarketplaceRegistrationDefinitionsApi apiInstance = new MarketplaceRegistrationDefinitionsApi(defaultClient);
    String scope = "scope_example"; // String | Scope of the resource.
    String marketplaceIdentifier = "marketplaceIdentifier_example"; // String | Market place identifer. Expected Formats - {publisher}.{product[-preview]}.{planName}.{version} or {publisher}.{product[-preview]}.{planName} or {publisher}.{product[-preview]} or {publisher}).
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    try {
      RegistrationDefinition result = apiInstance.marketplaceRegistrationDefinitionsGet(scope, marketplaceIdentifier, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplaceRegistrationDefinitionsApi#marketplaceRegistrationDefinitionsGet");
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
| **scope** | **String**| Scope of the resource. | |
| **marketplaceIdentifier** | **String**| Market place identifer. Expected Formats - {publisher}.{product[-preview]}.{planName}.{version} or {publisher}.{product[-preview]}.{planName} or {publisher}.{product[-preview]} or {publisher}). | |
| **apiVersion** | **String**| The API version to use for this operation. | |

### Return type

[**RegistrationDefinition**](RegistrationDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns the details of the marketplace registration definition. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="marketplaceRegistrationDefinitionsList"></a>
# **marketplaceRegistrationDefinitionsList**
> MarketplaceRegistrationDefinitionList marketplaceRegistrationDefinitionsList(scope, apiVersion, $filter)



Gets a list of the marketplace registration definitions for the marketplace identifier.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplaceRegistrationDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    MarketplaceRegistrationDefinitionsApi apiInstance = new MarketplaceRegistrationDefinitionsApi(defaultClient);
    String scope = "scope_example"; // String | Scope of the resource.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String $filter = "$filter_example"; // String | The filter query parameter. Might be used to filter marketplace registration definition by plan identifier, publisher, version etc.
    try {
      MarketplaceRegistrationDefinitionList result = apiInstance.marketplaceRegistrationDefinitionsList(scope, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplaceRegistrationDefinitionsApi#marketplaceRegistrationDefinitionsList");
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
| **scope** | **String**| Scope of the resource. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **$filter** | **String**| The filter query parameter. Might be used to filter marketplace registration definition by plan identifier, publisher, version etc. | [optional] |

### Return type

[**MarketplaceRegistrationDefinitionList**](MarketplaceRegistrationDefinitionList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns a list of the marketplace registration definitions. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

