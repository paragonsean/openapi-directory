# PatientApi

All URIs are relative to *https://api.twinehealth.com/pub*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createPatient**](PatientApi.md#createPatient) | **POST** /patient | Create a patient |
| [**fetchPatient**](PatientApi.md#fetchPatient) | **GET** /patient/{id} | Get a patient |
| [**fetchPatientCoaches**](PatientApi.md#fetchPatientCoaches) | **GET** /patient/{id}/coaches | List coaches for a patient |
| [**fetchPatientGroups**](PatientApi.md#fetchPatientGroups) | **GET** /patient/{id}/groups | List groups for a patient |
| [**fetchPatients**](PatientApi.md#fetchPatients) | **GET** /patient | List patients |
| [**updatePatient**](PatientApi.md#updatePatient) | **PATCH** /patient/{id} | Update a patient |
| [**upsertPatient**](PatientApi.md#upsertPatient) | **PUT** /patient | Upsert patient |


<a id="createPatient"></a>
# **createPatient**
> CreatePatientResponse createPatient(createPatientRequest)

Create a patient

Create a patient record.  Example for creating a patient with a group specified using &#x60;meta.query&#x60; instead of &#x60;id&#x60;:  &#x60;&#x60;&#x60;JSON {   \&quot;data\&quot;: {     \&quot;type\&quot;: \&quot;patient\&quot;,     \&quot;attributes\&quot;: {       \&quot;first_name\&quot;: \&quot;Andrew\&quot;,       \&quot;last_name\&quot;: \&quot;Smith\&quot;     },     \&quot;relationships\&quot;: {       \&quot;groups\&quot;: {         \&quot;data\&quot;: [           {             \&quot;type\&quot;: \&quot;group\&quot;,             \&quot;meta\&quot;: {               \&quot;query\&quot;: {                 \&quot;organization\&quot;: \&quot;58c88de7c93eb96357a87033\&quot;,                 \&quot;name\&quot;: \&quot;Patients Lead\&quot;               }             }           }         ]       }     }   } } &#x60;&#x60;&#x60; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PatientApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twinehealth.com/pub");

    PatientApi apiInstance = new PatientApi(defaultClient);
    CreatePatientRequest createPatientRequest = new CreatePatientRequest(); // CreatePatientRequest | 
    try {
      CreatePatientResponse result = apiInstance.createPatient(createPatientRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PatientApi#createPatient");
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
| **createPatientRequest** | [**CreatePatientRequest**](CreatePatientRequest.md)|  | |

### Return type

[**CreatePatientResponse**](CreatePatientResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **409** | Invalid Request |  -  |

<a id="fetchPatient"></a>
# **fetchPatient**
> FetchPatientResponse fetchPatient(id)

Get a patient

Gets a patient record by id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PatientApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twinehealth.com/pub");

    PatientApi apiInstance = new PatientApi(defaultClient);
    String id = "id_example"; // String | Patient identifier
    try {
      FetchPatientResponse result = apiInstance.fetchPatient(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PatientApi#fetchPatient");
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
| **id** | **String**| Patient identifier | |

### Return type

[**FetchPatientResponse**](FetchPatientResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="fetchPatientCoaches"></a>
# **fetchPatientCoaches**
> FetchCoachesResponse fetchPatientCoaches(id)

List coaches for a patient

Get the list of coaches for a patient.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PatientApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twinehealth.com/pub");

    PatientApi apiInstance = new PatientApi(defaultClient);
    String id = "id_example"; // String | Patient identifier
    try {
      FetchCoachesResponse result = apiInstance.fetchPatientCoaches(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PatientApi#fetchPatientCoaches");
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
| **id** | **String**| Patient identifier | |

### Return type

[**FetchCoachesResponse**](FetchCoachesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="fetchPatientGroups"></a>
# **fetchPatientGroups**
> FetchGroupsResponse fetchPatientGroups(id)

List groups for a patient

Get the list of groups for a patient.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PatientApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twinehealth.com/pub");

    PatientApi apiInstance = new PatientApi(defaultClient);
    String id = "id_example"; // String | Patient identifier
    try {
      FetchGroupsResponse result = apiInstance.fetchPatientGroups(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PatientApi#fetchPatientGroups");
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
| **id** | **String**| Patient identifier | |

### Return type

[**FetchGroupsResponse**](FetchGroupsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="fetchPatients"></a>
# **fetchPatients**
> FetchPatientsResponse fetchPatients(filterGroups, filterOrganization, filterIdentifierSystem, filterIdentifierValue, filterArchived, filterCreatedAt, filterUpdatedAt, pageNumber, pageSize, pageLimit, pageCursor)

List patients

Get a list of patients.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PatientApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twinehealth.com/pub");

    PatientApi apiInstance = new PatientApi(defaultClient);
    String filterGroups = "filterGroups_example"; // String | Comma-separated list of group ids. Note that either `filter[group]` or `filter[organization]` must be specified.
    String filterOrganization = "filterOrganization_example"; // String | Fitbit Plus organization id. Note that either `filter[group]` or `filter[organization]` must be specified.
    String filterIdentifierSystem = "filterIdentifierSystem_example"; // String | Identifier system (example: \"MyEHR\") - requires a \"filter[identifier][value]\" parameter
    String filterIdentifierValue = "filterIdentifierValue_example"; // String | Identifier value (example: \"12345\") - requires a \"filter[identifier][system]\" parameter
    Boolean filterArchived = true; // Boolean | If not specified, return all patients. If set to 'true' return only archived patients, if set to 'false', return only patients who are not archived.
    String filterCreatedAt = "filterCreatedAt_example"; // String | The start (inclusive) and end (exclusive) dates are ISO date and time strings separated by `..`. Example for patients created in November 2017 (America/New_York): `filter[created_at]=2017-11-01T00:00:00-04:00..2017-12-01T00:00:00-05:00` 
    String filterUpdatedAt = "filterUpdatedAt_example"; // String | The start (inclusive) and end (exclusive) dates are ISO date and time strings separated by `..`. Example for patients updated in November 2017 (America/New_York): `filter[updated_at]=2017-11-01T00:00:00-04:00..2017-12-01T00:00:00-05:00` 
    Integer pageNumber = 1; // Integer | Page number
    Integer pageSize = 10; // Integer | Page size
    Integer pageLimit = 50; // Integer | Page limit
    String pageCursor = "pageCursor_example"; // String | Page cursor
    try {
      FetchPatientsResponse result = apiInstance.fetchPatients(filterGroups, filterOrganization, filterIdentifierSystem, filterIdentifierValue, filterArchived, filterCreatedAt, filterUpdatedAt, pageNumber, pageSize, pageLimit, pageCursor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PatientApi#fetchPatients");
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
| **filterGroups** | **String**| Comma-separated list of group ids. Note that either &#x60;filter[group]&#x60; or &#x60;filter[organization]&#x60; must be specified. | [optional] |
| **filterOrganization** | **String**| Fitbit Plus organization id. Note that either &#x60;filter[group]&#x60; or &#x60;filter[organization]&#x60; must be specified. | [optional] |
| **filterIdentifierSystem** | **String**| Identifier system (example: \&quot;MyEHR\&quot;) - requires a \&quot;filter[identifier][value]\&quot; parameter | [optional] |
| **filterIdentifierValue** | **String**| Identifier value (example: \&quot;12345\&quot;) - requires a \&quot;filter[identifier][system]\&quot; parameter | [optional] |
| **filterArchived** | **Boolean**| If not specified, return all patients. If set to &#39;true&#39; return only archived patients, if set to &#39;false&#39;, return only patients who are not archived. | [optional] |
| **filterCreatedAt** | **String**| The start (inclusive) and end (exclusive) dates are ISO date and time strings separated by &#x60;..&#x60;. Example for patients created in November 2017 (America/New_York): &#x60;filter[created_at]&#x3D;2017-11-01T00:00:00-04:00..2017-12-01T00:00:00-05:00&#x60;  | [optional] |
| **filterUpdatedAt** | **String**| The start (inclusive) and end (exclusive) dates are ISO date and time strings separated by &#x60;..&#x60;. Example for patients updated in November 2017 (America/New_York): &#x60;filter[updated_at]&#x3D;2017-11-01T00:00:00-04:00..2017-12-01T00:00:00-05:00&#x60;  | [optional] |
| **pageNumber** | **Integer**| Page number | [optional] [default to 1] |
| **pageSize** | **Integer**| Page size | [optional] [default to 10] |
| **pageLimit** | **Integer**| Page limit | [optional] [default to 50] |
| **pageCursor** | **String**| Page cursor | [optional] |

### Return type

[**FetchPatientsResponse**](FetchPatientsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **409** | Invalid Request |  -  |

<a id="updatePatient"></a>
# **updatePatient**
> UpdatePatientResponse updatePatient(id, updatePatientRequest)

Update a patient

Update a patient record.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PatientApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twinehealth.com/pub");

    PatientApi apiInstance = new PatientApi(defaultClient);
    String id = "id_example"; // String | Patient identifier
    UpdatePatientRequest updatePatientRequest = new UpdatePatientRequest(); // UpdatePatientRequest | 
    try {
      UpdatePatientResponse result = apiInstance.updatePatient(id, updatePatientRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PatientApi#updatePatient");
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
| **id** | **String**| Patient identifier | |
| **updatePatientRequest** | [**UpdatePatientRequest**](UpdatePatientRequest.md)|  | |

### Return type

[**UpdatePatientResponse**](UpdatePatientResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **409** | Invalid Request |  -  |

<a id="upsertPatient"></a>
# **upsertPatient**
> CreatePatientResponse upsertPatient(upsertPatientRequest)

Upsert patient

Create a new patient or update an existing patient

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PatientApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twinehealth.com/pub");

    PatientApi apiInstance = new PatientApi(defaultClient);
    UpsertPatientRequest upsertPatientRequest = new UpsertPatientRequest(); // UpsertPatientRequest | 
    try {
      CreatePatientResponse result = apiInstance.upsertPatient(upsertPatientRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PatientApi#upsertPatient");
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
| **upsertPatientRequest** | [**UpsertPatientRequest**](UpsertPatientRequest.md)|  | |

### Return type

[**CreatePatientResponse**](CreatePatientResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **409** | Invalid Request |  -  |

