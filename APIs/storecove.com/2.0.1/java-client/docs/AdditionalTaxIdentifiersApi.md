# AdditionalTaxIdentifiersApi

All URIs are relative to *https://api.storecove.com/api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createAdditionalTaxIdentifier**](AdditionalTaxIdentifiersApi.md#createAdditionalTaxIdentifier) | **POST** /legal_entities/{legal_entity_id}/additional_tax_identifiers | Create a new AdditionalTaxIdentifier |
| [**deleteAdditionalTaxIdentifier**](AdditionalTaxIdentifiersApi.md#deleteAdditionalTaxIdentifier) | **DELETE** /legal_entities/{legal_entity_id}/additional_tax_identifiers/{id} | Delete AdditionalTaxIdentifier |
| [**getAdditionalTaxIdentifier**](AdditionalTaxIdentifiersApi.md#getAdditionalTaxIdentifier) | **GET** /legal_entities/{legal_entity_id}/additional_tax_identifiers/{id} | Get AdditionalTaxIdentifier |
| [**updateAdditionalTaxIdentifier**](AdditionalTaxIdentifiersApi.md#updateAdditionalTaxIdentifier) | **PATCH** /legal_entities/{legal_entity_id}/additional_tax_identifiers/{id} | Update AdditionalTaxIdentifier |


<a id="createAdditionalTaxIdentifier"></a>
# **createAdditionalTaxIdentifier**
> AdditionalTaxIdentifier createAdditionalTaxIdentifier(legalEntityId, additionalTaxIdentifierCreate)

Create a new AdditionalTaxIdentifier

Create a new AdditionalTaxIdentifier. An AdditionalTaxIdentifier is a seconday tax identifier that is used inside the EU when sending invoices to consumers. In that case, the VAT of the receiving country is used and if the sender has a local VAT identifier, that is used to identifiy the sender, instead of the sender&#39;s origin country VAT number. To use these identifiers, use the invoice.consumerTaxMode &#x3D; true property.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdditionalTaxIdentifiersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.storecove.com/api/v2");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    AdditionalTaxIdentifiersApi apiInstance = new AdditionalTaxIdentifiersApi(defaultClient);
    Long legalEntityId = 56L; // Long | The id of the LegalEntity for which to create the AdditionalTaxIdentifier
    AdditionalTaxIdentifierCreate additionalTaxIdentifierCreate = new AdditionalTaxIdentifierCreate(); // AdditionalTaxIdentifierCreate | AdditionalTaxIdentifier to create
    try {
      AdditionalTaxIdentifier result = apiInstance.createAdditionalTaxIdentifier(legalEntityId, additionalTaxIdentifierCreate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdditionalTaxIdentifiersApi#createAdditionalTaxIdentifier");
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
| **legalEntityId** | **Long**| The id of the LegalEntity for which to create the AdditionalTaxIdentifier | |
| **additionalTaxIdentifierCreate** | [**AdditionalTaxIdentifierCreate**](AdditionalTaxIdentifierCreate.md)| AdditionalTaxIdentifier to create | |

### Return type

[**AdditionalTaxIdentifier**](AdditionalTaxIdentifier.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **422** | Unprocessable Entity |  -  |

<a id="deleteAdditionalTaxIdentifier"></a>
# **deleteAdditionalTaxIdentifier**
> deleteAdditionalTaxIdentifier(legalEntityId, id)

Delete AdditionalTaxIdentifier

Delete an AdditionalTaxIdentifier

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdditionalTaxIdentifiersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.storecove.com/api/v2");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    AdditionalTaxIdentifiersApi apiInstance = new AdditionalTaxIdentifiersApi(defaultClient);
    Long legalEntityId = 56L; // Long | The id of the LegalEntity the AdditionalTaxIdentifier belongs to
    Long id = 56L; // Long | The id of the AdditionalTaxIdentifier
    try {
      apiInstance.deleteAdditionalTaxIdentifier(legalEntityId, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdditionalTaxIdentifiersApi#deleteAdditionalTaxIdentifier");
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
| **legalEntityId** | **Long**| The id of the LegalEntity the AdditionalTaxIdentifier belongs to | |
| **id** | **Long**| The id of the AdditionalTaxIdentifier | |

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getAdditionalTaxIdentifier"></a>
# **getAdditionalTaxIdentifier**
> AdditionalTaxIdentifier getAdditionalTaxIdentifier(legalEntityId, id)

Get AdditionalTaxIdentifier

Get an AdditionalTaxIdentifier

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdditionalTaxIdentifiersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.storecove.com/api/v2");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    AdditionalTaxIdentifiersApi apiInstance = new AdditionalTaxIdentifiersApi(defaultClient);
    Long legalEntityId = 56L; // Long | The id of the LegalEntity the AdditionalTaxIdentifier belongs to
    Long id = 56L; // Long | The id of the AdditionalTaxIdentifier
    try {
      AdditionalTaxIdentifier result = apiInstance.getAdditionalTaxIdentifier(legalEntityId, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdditionalTaxIdentifiersApi#getAdditionalTaxIdentifier");
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
| **legalEntityId** | **Long**| The id of the LegalEntity the AdditionalTaxIdentifier belongs to | |
| **id** | **Long**| The id of the AdditionalTaxIdentifier | |

### Return type

[**AdditionalTaxIdentifier**](AdditionalTaxIdentifier.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="updateAdditionalTaxIdentifier"></a>
# **updateAdditionalTaxIdentifier**
> AdditionalTaxIdentifier updateAdditionalTaxIdentifier(legalEntityId, id, additionalTaxIdentifierUpdate)

Update AdditionalTaxIdentifier

Update an AdditionalTaxIdentifier

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdditionalTaxIdentifiersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.storecove.com/api/v2");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    AdditionalTaxIdentifiersApi apiInstance = new AdditionalTaxIdentifiersApi(defaultClient);
    Long legalEntityId = 56L; // Long | The id of the LegalEntity the AdditionalTaxIdentifier belongs to
    Long id = 56L; // Long | The id of the AdditionalTaxIdentifier to be updated
    AdditionalTaxIdentifierUpdate additionalTaxIdentifierUpdate = new AdditionalTaxIdentifierUpdate(); // AdditionalTaxIdentifierUpdate | AdditionalTaxIdentifier to update
    try {
      AdditionalTaxIdentifier result = apiInstance.updateAdditionalTaxIdentifier(legalEntityId, id, additionalTaxIdentifierUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdditionalTaxIdentifiersApi#updateAdditionalTaxIdentifier");
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
| **legalEntityId** | **Long**| The id of the LegalEntity the AdditionalTaxIdentifier belongs to | |
| **id** | **Long**| The id of the AdditionalTaxIdentifier to be updated | |
| **additionalTaxIdentifierUpdate** | [**AdditionalTaxIdentifierUpdate**](AdditionalTaxIdentifierUpdate.md)| AdditionalTaxIdentifier to update | |

### Return type

[**AdditionalTaxIdentifier**](AdditionalTaxIdentifier.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

