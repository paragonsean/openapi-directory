# RegistrationSchemasApi

All URIs are relative to *https://api.test.osf.io/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**registrationSchemaRead**](RegistrationSchemasApi.md#registrationSchemaRead) | **GET** /schemas/registrations/{registration_schema_id} | Retrieve a Registration Schema |
| [**registrationSchemasList**](RegistrationSchemasApi.md#registrationSchemasList) | **GET** /schemas/registrations/ | Retrieve a list of Registration Schemas |


<a id="registrationSchemaRead"></a>
# **registrationSchemaRead**
> RegistrationSchema registrationSchemaRead(registrationSchemaId)

Retrieve a Registration Schema

Retrieves the details of a given Registration Schema. Registration Schemas defines the desired supplemental information that should accompany be included in a Registration. Registration Schemas are Read-only to API users. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the requested Registration Schemas, if the request is successful. #### Errors If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistrationSchemasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    RegistrationSchemasApi apiInstance = new RegistrationSchemasApi(defaultClient);
    String registrationSchemaId = "registrationSchemaId_example"; // String | The unique identifier of the Registration Schema example `6176c9d45e01f100091d4f94`.
    try {
      RegistrationSchema result = apiInstance.registrationSchemaRead(registrationSchemaId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrationSchemasApi#registrationSchemaRead");
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
| **registrationSchemaId** | **String**| The unique identifier of the Registration Schema example &#x60;6176c9d45e01f100091d4f94&#x60;. | |

### Return type

[**RegistrationSchema**](RegistrationSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="registrationSchemasList"></a>
# **registrationSchemasList**
> RegistrationSchema registrationSchemasList()

Retrieve a list of Registration Schemas

Retrieve a paginated list of all active Registration Schemas. Registration Schemas describe the supplemental questions that accompany a registration. Registration Schemas are read-only for API users. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys. The &#x60;data&#x60; key contains an array of 10 Registration Schemas. Each resource in the array is a separate Registration Schemas object. The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination). #### Errors This request should never return an error.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistrationSchemasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    RegistrationSchemasApi apiInstance = new RegistrationSchemasApi(defaultClient);
    try {
      RegistrationSchema result = apiInstance.registrationSchemasList();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrationSchemasApi#registrationSchemasList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RegistrationSchema**](RegistrationSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

