# PciQuestionnairesApi

All URIs are relative to *https://kyc-test.adyen.com/lem/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getLegalEntitiesIdPciQuestionnaires**](PciQuestionnairesApi.md#getLegalEntitiesIdPciQuestionnaires) | **GET** /legalEntities/{id}/pciQuestionnaires | Get PCI questionnaire details |
| [**getLegalEntitiesIdPciQuestionnairesPciid**](PciQuestionnairesApi.md#getLegalEntitiesIdPciQuestionnairesPciid) | **GET** /legalEntities/{id}/pciQuestionnaires/{pciid} | Get PCI questionnaire |
| [**postLegalEntitiesIdPciQuestionnairesGeneratePciTemplates**](PciQuestionnairesApi.md#postLegalEntitiesIdPciQuestionnairesGeneratePciTemplates) | **POST** /legalEntities/{id}/pciQuestionnaires/generatePciTemplates | Generate PCI questionnaire |
| [**postLegalEntitiesIdPciQuestionnairesSignPciTemplates**](PciQuestionnairesApi.md#postLegalEntitiesIdPciQuestionnairesSignPciTemplates) | **POST** /legalEntities/{id}/pciQuestionnaires/signPciTemplates | Sign PCI questionnaire |


<a id="getLegalEntitiesIdPciQuestionnaires"></a>
# **getLegalEntitiesIdPciQuestionnaires**
> GetPciQuestionnaireInfosResponse getLegalEntitiesIdPciQuestionnaires(id)

Get PCI questionnaire details

Get a list of signed PCI questionnaires.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PciQuestionnairesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://kyc-test.adyen.com/lem/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    PciQuestionnairesApi apiInstance = new PciQuestionnairesApi(defaultClient);
    String id = "id_example"; // String | The unique identifier of the legal entity to get PCI questionnaire information.
    try {
      GetPciQuestionnaireInfosResponse result = apiInstance.getLegalEntitiesIdPciQuestionnaires(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PciQuestionnairesApi#getLegalEntitiesIdPciQuestionnaires");
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
| **id** | **String**| The unique identifier of the legal entity to get PCI questionnaire information. | |

### Return type

[**GetPciQuestionnaireInfosResponse**](GetPciQuestionnaireInfosResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="getLegalEntitiesIdPciQuestionnairesPciid"></a>
# **getLegalEntitiesIdPciQuestionnairesPciid**
> GetPciQuestionnaireResponse getLegalEntitiesIdPciQuestionnairesPciid(id, pciid)

Get PCI questionnaire

Returns the signed PCI questionnaire.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PciQuestionnairesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://kyc-test.adyen.com/lem/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    PciQuestionnairesApi apiInstance = new PciQuestionnairesApi(defaultClient);
    String id = "id_example"; // String | The legal entity ID of the individual who signed the PCI questionnaire.
    String pciid = "pciid_example"; // String | The unique identifier of the signed PCI questionnaire.
    try {
      GetPciQuestionnaireResponse result = apiInstance.getLegalEntitiesIdPciQuestionnairesPciid(id, pciid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PciQuestionnairesApi#getLegalEntitiesIdPciQuestionnairesPciid");
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
| **id** | **String**| The legal entity ID of the individual who signed the PCI questionnaire. | |
| **pciid** | **String**| The unique identifier of the signed PCI questionnaire. | |

### Return type

[**GetPciQuestionnaireResponse**](GetPciQuestionnaireResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="postLegalEntitiesIdPciQuestionnairesGeneratePciTemplates"></a>
# **postLegalEntitiesIdPciQuestionnairesGeneratePciTemplates**
> GeneratePciDescriptionResponse postLegalEntitiesIdPciQuestionnairesGeneratePciTemplates(id, generatePciDescriptionRequest)

Generate PCI questionnaire

Generates the required PCI questionnaires based on the user&#39;s [salesChannel](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/businessLines__reqParam_salesChannels).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PciQuestionnairesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://kyc-test.adyen.com/lem/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    PciQuestionnairesApi apiInstance = new PciQuestionnairesApi(defaultClient);
    String id = "id_example"; // String | The unique identifier of the legal entity to get PCI questionnaire information.
    GeneratePciDescriptionRequest generatePciDescriptionRequest = new GeneratePciDescriptionRequest(); // GeneratePciDescriptionRequest | 
    try {
      GeneratePciDescriptionResponse result = apiInstance.postLegalEntitiesIdPciQuestionnairesGeneratePciTemplates(id, generatePciDescriptionRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PciQuestionnairesApi#postLegalEntitiesIdPciQuestionnairesGeneratePciTemplates");
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
| **id** | **String**| The unique identifier of the legal entity to get PCI questionnaire information. | |
| **generatePciDescriptionRequest** | [**GeneratePciDescriptionRequest**](GeneratePciDescriptionRequest.md)|  | [optional] |

### Return type

[**GeneratePciDescriptionResponse**](GeneratePciDescriptionResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="postLegalEntitiesIdPciQuestionnairesSignPciTemplates"></a>
# **postLegalEntitiesIdPciQuestionnairesSignPciTemplates**
> PciSigningResponse postLegalEntitiesIdPciQuestionnairesSignPciTemplates(id, pciSigningRequest)

Sign PCI questionnaire

Signs the required PCI questionnaire.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PciQuestionnairesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://kyc-test.adyen.com/lem/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    PciQuestionnairesApi apiInstance = new PciQuestionnairesApi(defaultClient);
    String id = "id_example"; // String | The legal entity ID of the user that has a contractual relationship with your platform.
    PciSigningRequest pciSigningRequest = new PciSigningRequest(); // PciSigningRequest | 
    try {
      PciSigningResponse result = apiInstance.postLegalEntitiesIdPciQuestionnairesSignPciTemplates(id, pciSigningRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PciQuestionnairesApi#postLegalEntitiesIdPciQuestionnairesSignPciTemplates");
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
| **id** | **String**| The legal entity ID of the user that has a contractual relationship with your platform. | |
| **pciSigningRequest** | [**PciSigningRequest**](PciSigningRequest.md)|  | [optional] |

### Return type

[**PciSigningResponse**](PciSigningResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

