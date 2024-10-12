# RegistrationsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addInstantRegistration**](RegistrationsApi.md#addInstantRegistration) | **POST** /api/registrations/instant | Creates new registration record, adds an ID document and optional selfie image in one go. |
| [**addRegistration**](RegistrationsApi.md#addRegistration) | **POST** /api/registrations | Creates new registration. |
| [**apiRegistrationsIdPdfExportSectionsGet**](RegistrationsApi.md#apiRegistrationsIdPdfExportSectionsGet) | **GET** /api/registrations/{id}/pdf-export-sections | Returns a PDF report for a given registration containing specified sections |
| [**checkSubmittedIdDocuments**](RegistrationsApi.md#checkSubmittedIdDocuments) | **GET** /api/registrations/{id}/check-submitted-id-documents | Checks if submitted documents are sufficient to complete registration. |
| [**getRegistrationPdfExport**](RegistrationsApi.md#getRegistrationPdfExport) | **GET** /api/registrations/{id}/pdf-export | Returns PDF export for a given registration. |
| [**getRegistrationSearch**](RegistrationsApi.md#getRegistrationSearch) | **GET** /api/registrations/search | Gets paged registration list by search criteria or nothing if there are no matching fields.  Optional parameters may be appended to the query string.  Maximum page size is 50. |
| [**getRegistrationSettings**](RegistrationsApi.md#getRegistrationSettings) | **GET** /api/registrations/{id}/settings | Gets registration settings or nothing if there are no settings associated with the registration. |
| [**getRegistrationSummariesByReferenceId**](RegistrationsApi.md#getRegistrationSummariesByReferenceId) | **GET** /api/registrations/referenceid/{referenceId}/summary | Finds registrations by the ReferenceId. |
| [**getRegistrationSummary**](RegistrationsApi.md#getRegistrationSummary) | **GET** /api/registrations/{id}/summary | Finds a registration by the Id. |
| [**getRegistrationSummaryByRegCode**](RegistrationsApi.md#getRegistrationSummaryByRegCode) | **GET** /api/registrations/regcode/{regCode}/summary | Finds a registration by the RegCode. |
| [**getRegistrationSupportedIdDocuments**](RegistrationsApi.md#getRegistrationSupportedIdDocuments) | **GET** /api/registrations/{id}/supported-id-documents | Get a list of supported id document for the specified registration id. |
| [**getShareCodePdfExport**](RegistrationsApi.md#getShareCodePdfExport) | **GET** /api/registrations/{id}/pdf-settlement-status | Returns settlement status PDF (Share Code) for a given registration. |
| [**overrideCheckStatus**](RegistrationsApi.md#overrideCheckStatus) | **PUT** /api/registrations/{id}/override-check-status | Sets an override for a specific check on the registration. |
| [**resendInvitation**](RegistrationsApi.md#resendInvitation) | **POST** /api/registrations/{id}/resend-invitation | Resends any invitation for the specified registration. |
| [**updateContactDetails**](RegistrationsApi.md#updateContactDetails) | **PUT** /api/registrations/{id}/contact-details | Updates a registration&#39;s contact details. |
| [**updateRegistrationSettings**](RegistrationsApi.md#updateRegistrationSettings) | **PUT** /api/registrations/{id}/settings | Updates registration settings. |
| [**updateRegistrationStatus**](RegistrationsApi.md#updateRegistrationStatus) | **PUT** /api/registrations/{id}/status | Updates the status of the registration to one specified in the request. |


<a id="addInstantRegistration"></a>
# **addInstantRegistration**
> CredasApiModelsRegistrationsAddInstantRegistrationResponse addInstantRegistration(apikey, credasApiModelsRegistrationsAddInstantRegistrationRequest)

Creates new registration record, adds an ID document and optional selfie image in one go.

It&#39;s designed to provide a quick integration path for external systems which capture these details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistrationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    RegistrationsApi apiInstance = new RegistrationsApi(defaultClient);
    String apikey = "apikey_example"; // String | ApiKey supplied.
    CredasApiModelsRegistrationsAddInstantRegistrationRequest credasApiModelsRegistrationsAddInstantRegistrationRequest = new CredasApiModelsRegistrationsAddInstantRegistrationRequest(); // CredasApiModelsRegistrationsAddInstantRegistrationRequest | The Credas.Api.Models.Registrations.AddInstantRegistrationRequest object containing required data.
    try {
      CredasApiModelsRegistrationsAddInstantRegistrationResponse result = apiInstance.addInstantRegistration(apikey, credasApiModelsRegistrationsAddInstantRegistrationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrationsApi#addInstantRegistration");
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
| **apikey** | **String**| ApiKey supplied. | |
| **credasApiModelsRegistrationsAddInstantRegistrationRequest** | [**CredasApiModelsRegistrationsAddInstantRegistrationRequest**](CredasApiModelsRegistrationsAddInstantRegistrationRequest.md)| The Credas.Api.Models.Registrations.AddInstantRegistrationRequest object containing required data. | [optional] |

### Return type

[**CredasApiModelsRegistrationsAddInstantRegistrationResponse**](CredasApiModelsRegistrationsAddInstantRegistrationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/*+json, application/*+xml, application/json, application/json-patch+json, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK response with object containing the document information. |  -  |
| **400** | If the service was supplied invalid data. |  -  |
| **401** | If credentials supplied were invalid. |  -  |
| **500** | If an unexpected exception occurred whilst processing the request. |  -  |

<a id="addRegistration"></a>
# **addRegistration**
> CredasApiModelsRegistrationsAddRegistrationResponse addRegistration(apikey, credasApiModelsRegistrationsAddRegistrationRequest)

Creates new registration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistrationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    RegistrationsApi apiInstance = new RegistrationsApi(defaultClient);
    String apikey = "apikey_example"; // String | ApiKey supplied.
    CredasApiModelsRegistrationsAddRegistrationRequest credasApiModelsRegistrationsAddRegistrationRequest = new CredasApiModelsRegistrationsAddRegistrationRequest(); // CredasApiModelsRegistrationsAddRegistrationRequest | Object containing registration details.
    try {
      CredasApiModelsRegistrationsAddRegistrationResponse result = apiInstance.addRegistration(apikey, credasApiModelsRegistrationsAddRegistrationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrationsApi#addRegistration");
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
| **apikey** | **String**| ApiKey supplied. | |
| **credasApiModelsRegistrationsAddRegistrationRequest** | [**CredasApiModelsRegistrationsAddRegistrationRequest**](CredasApiModelsRegistrationsAddRegistrationRequest.md)| Object containing registration details. | [optional] |

### Return type

[**CredasApiModelsRegistrationsAddRegistrationResponse**](CredasApiModelsRegistrationsAddRegistrationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/*+json, application/*+xml, application/json, application/json-patch+json, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Details of newly added registration. |  -  |
| **400** | If the service was supplied invalid data. |  -  |
| **401** | If credentials supplied were invalid. |  -  |
| **402** | Error code meaning that the operation was aborted due to insufficient credits. |  -  |
| **500** | If an unexpected exception occurred whilst processing the request. |  -  |

<a id="apiRegistrationsIdPdfExportSectionsGet"></a>
# **apiRegistrationsIdPdfExportSectionsGet**
> byte[] apiRegistrationsIdPdfExportSectionsGet(id, apikey, comments, contactDetails, standardChecks, pepSanctionChecks, proofOfOwnership, bankAccountCheck, creditStatusCheck, liveness, excludeSelfie, excludeIDDocuments, diATFSection)

Returns a PDF report for a given registration containing specified sections

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistrationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    RegistrationsApi apiInstance = new RegistrationsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | Id of the registration.
    String apikey = "apikey_example"; // String | ApiKey supplied.
    Boolean comments = true; // Boolean | 
    Boolean contactDetails = true; // Boolean | 
    Boolean standardChecks = true; // Boolean | 
    Boolean pepSanctionChecks = true; // Boolean | 
    Boolean proofOfOwnership = true; // Boolean | 
    Boolean bankAccountCheck = true; // Boolean | 
    Boolean creditStatusCheck = true; // Boolean | 
    Boolean liveness = true; // Boolean | 
    Boolean excludeSelfie = true; // Boolean | 
    Boolean excludeIDDocuments = true; // Boolean | 
    Boolean diATFSection = true; // Boolean | 
    try {
      byte[] result = apiInstance.apiRegistrationsIdPdfExportSectionsGet(id, apikey, comments, contactDetails, standardChecks, pepSanctionChecks, proofOfOwnership, bankAccountCheck, creditStatusCheck, liveness, excludeSelfie, excludeIDDocuments, diATFSection);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrationsApi#apiRegistrationsIdPdfExportSectionsGet");
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
| **id** | **UUID**| Id of the registration. | |
| **apikey** | **String**| ApiKey supplied. | |
| **comments** | **Boolean**|  | [optional] |
| **contactDetails** | **Boolean**|  | [optional] |
| **standardChecks** | **Boolean**|  | [optional] |
| **pepSanctionChecks** | **Boolean**|  | [optional] |
| **proofOfOwnership** | **Boolean**|  | [optional] |
| **bankAccountCheck** | **Boolean**|  | [optional] |
| **creditStatusCheck** | **Boolean**|  | [optional] |
| **liveness** | **Boolean**|  | [optional] |
| **excludeSelfie** | **Boolean**|  | [optional] |
| **excludeIDDocuments** | **Boolean**|  | [optional] |
| **diATFSection** | **Boolean**|  | [optional] |

### Return type

**byte[]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | PDF document containing registration extract as byte stream. |  -  |
| **400** | If the service was supplied invalid data. |  -  |
| **401** | If credentials supplied were invalid. |  -  |
| **403** | If requesting entity have no permission to access the resource. |  -  |
| **404** | If registration matching the Id was not found. |  -  |
| **500** | If an unexpected exception occurred whilst processing the request. |  -  |

<a id="checkSubmittedIdDocuments"></a>
# **checkSubmittedIdDocuments**
> CredasApiModelsRegistrationsCheckSubmittedIdDocumentsResponse checkSubmittedIdDocuments(id, apikey)

Checks if submitted documents are sufficient to complete registration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistrationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    RegistrationsApi apiInstance = new RegistrationsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | Id of the registration.
    String apikey = "apikey_example"; // String | ApiKey supplied.
    try {
      CredasApiModelsRegistrationsCheckSubmittedIdDocumentsResponse result = apiInstance.checkSubmittedIdDocuments(id, apikey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrationsApi#checkSubmittedIdDocuments");
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
| **id** | **UUID**| Id of the registration. | |
| **apikey** | **String**| ApiKey supplied. | |

### Return type

[**CredasApiModelsRegistrationsCheckSubmittedIdDocumentsResponse**](CredasApiModelsRegistrationsCheckSubmittedIdDocumentsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK response with object containing the result of the document check. |  -  |
| **400** | If the service was supplied invalid data. |  -  |
| **401** | If credentials supplied were invalid. |  -  |
| **500** | If an unexpected exception occurred whilst processing the request. |  -  |

<a id="getRegistrationPdfExport"></a>
# **getRegistrationPdfExport**
> byte[] getRegistrationPdfExport(id, apikey)

Returns PDF export for a given registration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistrationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    RegistrationsApi apiInstance = new RegistrationsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | Id of the registration.
    String apikey = "apikey_example"; // String | ApiKey supplied.
    try {
      byte[] result = apiInstance.getRegistrationPdfExport(id, apikey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrationsApi#getRegistrationPdfExport");
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
| **id** | **UUID**| Id of the registration. | |
| **apikey** | **String**| ApiKey supplied. | |

### Return type

**byte[]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | PDF document containing registration extract as byte stream. |  -  |
| **400** | If the service was supplied invalid data. |  -  |
| **401** | If credentials supplied were invalid. |  -  |
| **403** | If requesting entity have no permission to access the resource. |  -  |
| **404** | If registration matching the Id was not found. |  -  |
| **500** | If an unexpected exception occurred whilst processing the request. |  -  |

<a id="getRegistrationSearch"></a>
# **getRegistrationSearch**
> CredasApiModelsRegistrationsPagedRegistrationSummary getRegistrationSearch(apikey, pageNum, pageSize, forename, surname, email, dob)

Gets paged registration list by search criteria or nothing if there are no matching fields.  Optional parameters may be appended to the query string.  Maximum page size is 50.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistrationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    RegistrationsApi apiInstance = new RegistrationsApi(defaultClient);
    String apikey = "apikey_example"; // String | ApiKey supplied.
    Integer pageNum = 0; // Integer | Zero-based page number to retrieve.
    Integer pageSize = 50; // Integer | Number of records to return on each request (Maximum value is 50).
    String forename = "forename_example"; // String | Search by forename.
    String surname = "surname_example"; // String | Search by surname.
    String email = "email_example"; // String | Search by user email.
    String dob = "dob_example"; // String | Date of birth in (yyyy-MM-dd) format
    try {
      CredasApiModelsRegistrationsPagedRegistrationSummary result = apiInstance.getRegistrationSearch(apikey, pageNum, pageSize, forename, surname, email, dob);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrationsApi#getRegistrationSearch");
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
| **apikey** | **String**| ApiKey supplied. | |
| **pageNum** | **Integer**| Zero-based page number to retrieve. | [optional] [default to 0] |
| **pageSize** | **Integer**| Number of records to return on each request (Maximum value is 50). | [optional] [default to 50] |
| **forename** | **String**| Search by forename. | [optional] |
| **surname** | **String**| Search by surname. | [optional] |
| **email** | **String**| Search by user email. | [optional] |
| **dob** | **String**| Date of birth in (yyyy-MM-dd) format | [optional] |

### Return type

[**CredasApiModelsRegistrationsPagedRegistrationSummary**](CredasApiModelsRegistrationsPagedRegistrationSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Registration summary object list. |  -  |
| **400** | If the service was supplied invalid data. |  -  |
| **401** | If credentials supplied were invalid. |  -  |
| **403** | If requesting entity have no permission to access the resource. |  -  |
| **404** | If registration matching the Id was not found. |  -  |
| **500** | If an unexpected exception occurred whilst processing the request. |  -  |

<a id="getRegistrationSettings"></a>
# **getRegistrationSettings**
> getRegistrationSettings(id, apikey)

Gets registration settings or nothing if there are no settings associated with the registration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistrationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    RegistrationsApi apiInstance = new RegistrationsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | Id of the registration.
    String apikey = "apikey_example"; // String | ApiKey supplied.
    try {
      apiInstance.getRegistrationSettings(id, apikey);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrationsApi#getRegistrationSettings");
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
| **id** | **UUID**| Id of the registration. | |
| **apikey** | **String**| ApiKey supplied. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Registration settings updated. |  -  |
| **400** | If the service was supplied invalid data. |  -  |
| **401** | If credentials supplied were invalid. |  -  |
| **403** | If requesting entity have no permission to access the resource. |  -  |
| **404** | If registration matching the Id was not found. |  -  |
| **500** | If an unexpected exception occurred whilst processing the request. |  -  |

<a id="getRegistrationSummariesByReferenceId"></a>
# **getRegistrationSummariesByReferenceId**
> List&lt;CredasApiModelsRegistrationsRegistrationSummary&gt; getRegistrationSummariesByReferenceId(referenceId, apikey)

Finds registrations by the ReferenceId.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistrationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    RegistrationsApi apiInstance = new RegistrationsApi(defaultClient);
    String referenceId = "referenceId_example"; // String | ReferenceId - from external system to match Registrations on.
    String apikey = "apikey_example"; // String | ApiKey supplied.
    try {
      List<CredasApiModelsRegistrationsRegistrationSummary> result = apiInstance.getRegistrationSummariesByReferenceId(referenceId, apikey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrationsApi#getRegistrationSummariesByReferenceId");
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
| **referenceId** | **String**| ReferenceId - from external system to match Registrations on. | |
| **apikey** | **String**| ApiKey supplied. | |

### Return type

[**List&lt;CredasApiModelsRegistrationsRegistrationSummary&gt;**](CredasApiModelsRegistrationsRegistrationSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Collection of Registration summary objects. |  -  |
| **400** | If the service was supplied invalid data. |  -  |
| **401** | If credentials supplied were invalid. |  -  |
| **403** | If requesting entity have no permission to access the resource. |  -  |
| **404** | If registration matching the RegCode was not found. |  -  |
| **500** | If an unexpected exception occurred whilst processing the request. |  -  |

<a id="getRegistrationSummary"></a>
# **getRegistrationSummary**
> CredasApiModelsRegistrationsRegistrationSummary getRegistrationSummary(id, apikey)

Finds a registration by the Id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistrationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    RegistrationsApi apiInstance = new RegistrationsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | Id of the registration.
    String apikey = "apikey_example"; // String | ApiKey supplied.
    try {
      CredasApiModelsRegistrationsRegistrationSummary result = apiInstance.getRegistrationSummary(id, apikey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrationsApi#getRegistrationSummary");
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
| **id** | **UUID**| Id of the registration. | |
| **apikey** | **String**| ApiKey supplied. | |

### Return type

[**CredasApiModelsRegistrationsRegistrationSummary**](CredasApiModelsRegistrationsRegistrationSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Registration summary object. |  -  |
| **400** | If the service was supplied invalid data. |  -  |
| **401** | If credentials supplied were invalid. |  -  |
| **403** | If requesting entity have no permission to access the resource. |  -  |
| **404** | If registration matching the Id was not found. |  -  |
| **500** | If an unexpected exception occurred whilst processing the request. |  -  |

<a id="getRegistrationSummaryByRegCode"></a>
# **getRegistrationSummaryByRegCode**
> CredasApiModelsRegistrationsRegistrationSummary getRegistrationSummaryByRegCode(regCode, apikey)

Finds a registration by the RegCode.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistrationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    RegistrationsApi apiInstance = new RegistrationsApi(defaultClient);
    String regCode = "regCode_example"; // String | RegCode - short unique identifier.
    String apikey = "apikey_example"; // String | ApiKey supplied.
    try {
      CredasApiModelsRegistrationsRegistrationSummary result = apiInstance.getRegistrationSummaryByRegCode(regCode, apikey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrationsApi#getRegistrationSummaryByRegCode");
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
| **regCode** | **String**| RegCode - short unique identifier. | |
| **apikey** | **String**| ApiKey supplied. | |

### Return type

[**CredasApiModelsRegistrationsRegistrationSummary**](CredasApiModelsRegistrationsRegistrationSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Registration summary object. |  -  |
| **400** | If the service was supplied invalid data. |  -  |
| **401** | If credentials supplied were invalid. |  -  |
| **403** | If requesting entity have no permission to access the resource. |  -  |
| **404** | If registration matching the RegCode was not found. |  -  |
| **500** | If an unexpected exception occurred whilst processing the request. |  -  |

<a id="getRegistrationSupportedIdDocuments"></a>
# **getRegistrationSupportedIdDocuments**
> CredasApiModelsRegistrationsSupportedIdDocument getRegistrationSupportedIdDocuments(id, apikey)

Get a list of supported id document for the specified registration id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistrationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    RegistrationsApi apiInstance = new RegistrationsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | Id of the registration.
    String apikey = "apikey_example"; // String | ApiKey supplied.
    try {
      CredasApiModelsRegistrationsSupportedIdDocument result = apiInstance.getRegistrationSupportedIdDocuments(id, apikey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrationsApi#getRegistrationSupportedIdDocuments");
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
| **id** | **UUID**| Id of the registration. | |
| **apikey** | **String**| ApiKey supplied. | |

### Return type

[**CredasApiModelsRegistrationsSupportedIdDocument**](CredasApiModelsRegistrationsSupportedIdDocument.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of supported id document objects. |  -  |
| **400** | If the service was supplied invalid data. |  -  |
| **401** | If credentials supplied were invalid. |  -  |
| **403** | If requesting entity have no permission to access the resource. |  -  |
| **404** | If registration matching the Id was not found. |  -  |
| **500** | If an unexpected exception occurred whilst processing the request. |  -  |

<a id="getShareCodePdfExport"></a>
# **getShareCodePdfExport**
> byte[] getShareCodePdfExport(id, apikey)

Returns settlement status PDF (Share Code) for a given registration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistrationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    RegistrationsApi apiInstance = new RegistrationsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | Id of the registration.
    String apikey = "apikey_example"; // String | ApiKey supplied.
    try {
      byte[] result = apiInstance.getShareCodePdfExport(id, apikey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrationsApi#getShareCodePdfExport");
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
| **id** | **UUID**| Id of the registration. | |
| **apikey** | **String**| ApiKey supplied. | |

### Return type

**byte[]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | PDF document containing settlement status information extract as byte stream. |  -  |
| **400** | If the service was supplied invalid data. |  -  |
| **401** | If credentials supplied were invalid. |  -  |
| **403** | If requesting entity have no permission to access the resource. |  -  |
| **404** | If registration matching the Id was not found. |  -  |
| **500** | If an unexpected exception occurred whilst processing the request. |  -  |

<a id="overrideCheckStatus"></a>
# **overrideCheckStatus**
> overrideCheckStatus(id, apikey, credasApiModelsStatusOverridesOverrideCheckStatusRequest)

Sets an override for a specific check on the registration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistrationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    RegistrationsApi apiInstance = new RegistrationsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | Id of the registration.
    String apikey = "apikey_example"; // String | ApiKey supplied.
    CredasApiModelsStatusOverridesOverrideCheckStatusRequest credasApiModelsStatusOverridesOverrideCheckStatusRequest = new CredasApiModelsStatusOverridesOverrideCheckStatusRequest(); // CredasApiModelsStatusOverridesOverrideCheckStatusRequest | Request data.
    try {
      apiInstance.overrideCheckStatus(id, apikey, credasApiModelsStatusOverridesOverrideCheckStatusRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrationsApi#overrideCheckStatus");
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
| **id** | **UUID**| Id of the registration. | |
| **apikey** | **String**| ApiKey supplied. | |
| **credasApiModelsStatusOverridesOverrideCheckStatusRequest** | [**CredasApiModelsStatusOverridesOverrideCheckStatusRequest**](CredasApiModelsStatusOverridesOverrideCheckStatusRequest.md)| Request data. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/*+json, application/*+xml, application/json, application/json-patch+json, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status of the operation. |  -  |
| **400** | If the service was supplied invalid data. |  -  |
| **401** | If credentials supplied were invalid. |  -  |
| **403** | If requesting entity have no permission to access the resource. |  -  |
| **404** | If registration matching the Id was not found. |  -  |
| **500** | If an unexpected exception occurred whilst processing the request. |  -  |

<a id="resendInvitation"></a>
# **resendInvitation**
> resendInvitation(id, apikey)

Resends any invitation for the specified registration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistrationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    RegistrationsApi apiInstance = new RegistrationsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | Id of the registration.
    String apikey = "apikey_example"; // String | ApiKey supplied.
    try {
      apiInstance.resendInvitation(id, apikey);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrationsApi#resendInvitation");
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
| **id** | **UUID**| Id of the registration. | |
| **apikey** | **String**| ApiKey supplied. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Invitation sent. |  -  |
| **400** | If the service was supplied invalid data. |  -  |
| **401** | If credentials supplied were invalid. |  -  |
| **403** | If requesting entity have no permission to access the resource. |  -  |
| **404** | If registration matching the Id was not found. |  -  |
| **500** | If an unexpected exception occurred whilst processing the request. |  -  |

<a id="updateContactDetails"></a>
# **updateContactDetails**
> updateContactDetails(id, apikey, credasApiModelsRegistrationsUpdateContactDetailsRequest)

Updates a registration&#39;s contact details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistrationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    RegistrationsApi apiInstance = new RegistrationsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | Id of the registration.
    String apikey = "apikey_example"; // String | ApiKey supplied.
    CredasApiModelsRegistrationsUpdateContactDetailsRequest credasApiModelsRegistrationsUpdateContactDetailsRequest = new CredasApiModelsRegistrationsUpdateContactDetailsRequest(); // CredasApiModelsRegistrationsUpdateContactDetailsRequest | Object containing contact details.
    try {
      apiInstance.updateContactDetails(id, apikey, credasApiModelsRegistrationsUpdateContactDetailsRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrationsApi#updateContactDetails");
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
| **id** | **UUID**| Id of the registration. | |
| **apikey** | **String**| ApiKey supplied. | |
| **credasApiModelsRegistrationsUpdateContactDetailsRequest** | [**CredasApiModelsRegistrationsUpdateContactDetailsRequest**](CredasApiModelsRegistrationsUpdateContactDetailsRequest.md)| Object containing contact details. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/*+json, application/*+xml, application/json, application/json-patch+json, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Registration contact details updated. |  -  |
| **400** | If the service was supplied invalid data. |  -  |
| **401** | If credentials supplied were invalid. |  -  |
| **403** | If requesting entity have no permission to access the resource. |  -  |
| **404** | If registration matching the Id was not found. |  -  |
| **500** | If an unexpected exception occurred whilst processing the request. |  -  |

<a id="updateRegistrationSettings"></a>
# **updateRegistrationSettings**
> updateRegistrationSettings(id, apikey, credasApiModelsRegistrationsRegistrationSettings)

Updates registration settings.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistrationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    RegistrationsApi apiInstance = new RegistrationsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | Id of the registration.
    String apikey = "apikey_example"; // String | ApiKey supplied.
    CredasApiModelsRegistrationsRegistrationSettings credasApiModelsRegistrationsRegistrationSettings = new CredasApiModelsRegistrationsRegistrationSettings(); // CredasApiModelsRegistrationsRegistrationSettings | Object containing registration settings.
    try {
      apiInstance.updateRegistrationSettings(id, apikey, credasApiModelsRegistrationsRegistrationSettings);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrationsApi#updateRegistrationSettings");
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
| **id** | **UUID**| Id of the registration. | |
| **apikey** | **String**| ApiKey supplied. | |
| **credasApiModelsRegistrationsRegistrationSettings** | [**CredasApiModelsRegistrationsRegistrationSettings**](CredasApiModelsRegistrationsRegistrationSettings.md)| Object containing registration settings. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/*+json, application/*+xml, application/json, application/json-patch+json, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Registration settings updated. |  -  |
| **400** | If the service was supplied invalid data. |  -  |
| **401** | If credentials supplied were invalid. |  -  |
| **403** | If requesting entity have no permission to access the resource. |  -  |
| **404** | If registration matching the Id was not found. |  -  |
| **500** | If an unexpected exception occurred whilst processing the request. |  -  |

<a id="updateRegistrationStatus"></a>
# **updateRegistrationStatus**
> updateRegistrationStatus(id, apikey, credasApiModelsRegistrationsUpdateRegistrationStatusRequest)

Updates the status of the registration to one specified in the request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistrationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    RegistrationsApi apiInstance = new RegistrationsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | Id of the registration.
    String apikey = "apikey_example"; // String | ApiKey supplied.
    CredasApiModelsRegistrationsUpdateRegistrationStatusRequest credasApiModelsRegistrationsUpdateRegistrationStatusRequest = new CredasApiModelsRegistrationsUpdateRegistrationStatusRequest(); // CredasApiModelsRegistrationsUpdateRegistrationStatusRequest | Request object containing the details.
    try {
      apiInstance.updateRegistrationStatus(id, apikey, credasApiModelsRegistrationsUpdateRegistrationStatusRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrationsApi#updateRegistrationStatus");
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
| **id** | **UUID**| Id of the registration. | |
| **apikey** | **String**| ApiKey supplied. | |
| **credasApiModelsRegistrationsUpdateRegistrationStatusRequest** | [**CredasApiModelsRegistrationsUpdateRegistrationStatusRequest**](CredasApiModelsRegistrationsUpdateRegistrationStatusRequest.md)| Request object containing the details. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/*+json, application/*+xml, application/json, application/json-patch+json, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Update was successful. |  -  |
| **400** | If the service was supplied invalid data. |  -  |
| **401** | If credentials supplied were invalid. |  -  |
| **404** | If the registration was not found. |  -  |
| **500** | If an unexpected exception occurred whilst processing the request. |  -  |

