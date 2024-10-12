# PeppolIdentifiersApi

All URIs are relative to *https://api.storecove.com/api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createPeppolIdentifier**](PeppolIdentifiersApi.md#createPeppolIdentifier) | **POST** /legal_entities/{legal_entity_id}/peppol_identifiers | Create a new PeppolIdentifier |
| [**deletePeppolIdentifier**](PeppolIdentifiersApi.md#deletePeppolIdentifier) | **DELETE** /legal_entities/{legal_entity_id}/peppol_identifiers/{superscheme}/{scheme}/{identifier} | Delete PeppolIdentifier |


<a id="createPeppolIdentifier"></a>
# **createPeppolIdentifier**
> PeppolIdentifier createPeppolIdentifier(legalEntityId, peppolIdentifierCreate)

Create a new PeppolIdentifier

Create a brand new new PeppolIdentifier. For &lt;&lt;_sg_singapore&gt;&gt;, special rules apply.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeppolIdentifiersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.storecove.com/api/v2");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    PeppolIdentifiersApi apiInstance = new PeppolIdentifiersApi(defaultClient);
    Long legalEntityId = 56L; // Long | The id of the LegalEntity for which to create the PeppolIdentifier
    PeppolIdentifierCreate peppolIdentifierCreate = new PeppolIdentifierCreate(); // PeppolIdentifierCreate | PeppolIdentifier to create
    try {
      PeppolIdentifier result = apiInstance.createPeppolIdentifier(legalEntityId, peppolIdentifierCreate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeppolIdentifiersApi#createPeppolIdentifier");
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
| **legalEntityId** | **Long**| The id of the LegalEntity for which to create the PeppolIdentifier | |
| **peppolIdentifierCreate** | [**PeppolIdentifierCreate**](PeppolIdentifierCreate.md)| PeppolIdentifier to create | |

### Return type

[**PeppolIdentifier**](PeppolIdentifier.md)

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

<a id="deletePeppolIdentifier"></a>
# **deletePeppolIdentifier**
> deletePeppolIdentifier(legalEntityId, superscheme, scheme, identifier)

Delete PeppolIdentifier

Delete a PeppolIdentifier.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeppolIdentifiersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.storecove.com/api/v2");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    PeppolIdentifiersApi apiInstance = new PeppolIdentifiersApi(defaultClient);
    Long legalEntityId = 56L; // Long | The id of the LegalEntity this PeppolIdentifier belongs to
    String superscheme = "superscheme_example"; // String | The superscheme of the identifier. Should always be \"iso6523-actorid-upis\".
    String scheme = "scheme_example"; // String | PEPPOL identifier scheme id, e.g. \"DE:VAT\". For a full list see <<_receiver_identifiers_list>>.
    String identifier = "identifier_example"; // String | PEPPOL identifier
    try {
      apiInstance.deletePeppolIdentifier(legalEntityId, superscheme, scheme, identifier);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeppolIdentifiersApi#deletePeppolIdentifier");
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
| **legalEntityId** | **Long**| The id of the LegalEntity this PeppolIdentifier belongs to | |
| **superscheme** | **String**| The superscheme of the identifier. Should always be \&quot;iso6523-actorid-upis\&quot;. | |
| **scheme** | **String**| PEPPOL identifier scheme id, e.g. \&quot;DE:VAT\&quot;. For a full list see &lt;&lt;_receiver_identifiers_list&gt;&gt;. | |
| **identifier** | **String**| PEPPOL identifier | |

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

