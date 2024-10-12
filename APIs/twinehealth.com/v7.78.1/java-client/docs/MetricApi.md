# MetricApi

All URIs are relative to *https://api.twinehealth.com/pub*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createPatientHealthMetric**](MetricApi.md#createPatientHealthMetric) | **POST** /patient_health_metric | Create patient health metrics |
| [**fetchPatientHealthMetric**](MetricApi.md#fetchPatientHealthMetric) | **GET** /patient_health_metric/{id} | Get a patient health metric |
| [**fetchPatientHealthMetrics**](MetricApi.md#fetchPatientHealthMetrics) | **GET** /patient_health_metric | List patient health metrics |


<a id="createPatientHealthMetric"></a>
# **createPatientHealthMetric**
> CreatePatientHealthMetricResponse createPatientHealthMetric(createPatientHealthMetricRequest)

Create patient health metrics

Create one or more patient health metrics.  Example for creating a patient health result with a patient specified using &#x60;meta.query&#x60; instead of &#x60;id&#x60;:  &#x60;&#x60;&#x60;JSON   {     \&quot;data\&quot;: {       \&quot;type\&quot;: \&quot;patient_health_metric\&quot;,        \&quot;attributes\&quot;: {          \&quot;code\&quot;: {            \&quot;system\&quot;: \&quot;LOINC\&quot;,            \&quot;value\&quot;: \&quot;13457-7\&quot;          },          \&quot;type\&quot;: \&quot;ldl_cholesterol\&quot;,          \&quot;occurred_at\&quot;: \&quot;2017-03-14T11:00:57.000Z\&quot;,          \&quot;value\&quot;: 121,          \&quot;unit\&quot;: \&quot;mg/dl\&quot;       },       \&quot;relationships\&quot;: {         \&quot;patient\&quot;: {           \&quot;data\&quot;: {             \&quot;type\&quot;: \&quot;patient\&quot;,             \&quot;meta\&quot;: {               \&quot;query\&quot;: {                 \&quot;identifier\&quot;: {                   \&quot;system\&quot;: \&quot;medical-record-number\&quot;,                   \&quot;value\&quot;: \&quot;121212\&quot;                 },                 \&quot;organization\&quot;: \&quot;58c4554710123c5c40dbab81\&quot;               }             }           }         }       }     }   } &#x60;&#x60;&#x60; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetricApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twinehealth.com/pub");

    MetricApi apiInstance = new MetricApi(defaultClient);
    CreatePatientHealthMetricRequest createPatientHealthMetricRequest = new CreatePatientHealthMetricRequest(); // CreatePatientHealthMetricRequest | 
    try {
      CreatePatientHealthMetricResponse result = apiInstance.createPatientHealthMetric(createPatientHealthMetricRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricApi#createPatientHealthMetric");
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
| **createPatientHealthMetricRequest** | [**CreatePatientHealthMetricRequest**](CreatePatientHealthMetricRequest.md)|  | |

### Return type

[**CreatePatientHealthMetricResponse**](CreatePatientHealthMetricResponse.md)

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

<a id="fetchPatientHealthMetric"></a>
# **fetchPatientHealthMetric**
> FetchPatientHealthMetricResponse fetchPatientHealthMetric(id)

Get a patient health metric

Get the plan summary for a patient.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetricApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twinehealth.com/pub");

    MetricApi apiInstance = new MetricApi(defaultClient);
    String id = "id_example"; // String | Patient health metric identifier
    try {
      FetchPatientHealthMetricResponse result = apiInstance.fetchPatientHealthMetric(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricApi#fetchPatientHealthMetric");
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
| **id** | **String**| Patient health metric identifier | |

### Return type

[**FetchPatientHealthMetricResponse**](FetchPatientHealthMetricResponse.md)

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

<a id="fetchPatientHealthMetrics"></a>
# **fetchPatientHealthMetrics**
> FetchPatientHealthMetricResponse fetchPatientHealthMetrics(filterPatient, filterGroups, filterOrganization, pageNumber, pageSize, pageLimit, pageCursor)

List patient health metrics

Get a list of patient health metrics.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetricApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twinehealth.com/pub");

    MetricApi apiInstance = new MetricApi(defaultClient);
    String filterPatient = "filterPatient_example"; // String | Filter the patient health metrics for a specified patient. Note that one of the following filters must be specified: `filter[patient]`, `filter[groups]`, `filter[organization]`. 
    String filterGroups = "filterGroups_example"; // String | Comma-separated list of group ids. Note that one of the following filters must be specified: `filter[patient]`, `filter[groups]`, `filter[organization]`. 
    String filterOrganization = "filterOrganization_example"; // String | Fitbit Plus organization id. Note that one of the following filters must be specified: `filter[patient]`, `filter[groups]`, `filter[organization]`. 
    Integer pageNumber = 1; // Integer | Page number
    Integer pageSize = 10; // Integer | Page size
    Integer pageLimit = 50; // Integer | Page limit
    String pageCursor = "pageCursor_example"; // String | Page cursor
    try {
      FetchPatientHealthMetricResponse result = apiInstance.fetchPatientHealthMetrics(filterPatient, filterGroups, filterOrganization, pageNumber, pageSize, pageLimit, pageCursor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricApi#fetchPatientHealthMetrics");
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
| **filterPatient** | **String**| Filter the patient health metrics for a specified patient. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[groups]&#x60;, &#x60;filter[organization]&#x60;.  | [optional] |
| **filterGroups** | **String**| Comma-separated list of group ids. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[groups]&#x60;, &#x60;filter[organization]&#x60;.  | [optional] |
| **filterOrganization** | **String**| Fitbit Plus organization id. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[groups]&#x60;, &#x60;filter[organization]&#x60;.  | [optional] |
| **pageNumber** | **Integer**| Page number | [optional] [default to 1] |
| **pageSize** | **Integer**| Page size | [optional] [default to 10] |
| **pageLimit** | **Integer**| Page limit | [optional] [default to 50] |
| **pageCursor** | **String**| Page cursor | [optional] |

### Return type

[**FetchPatientHealthMetricResponse**](FetchPatientHealthMetricResponse.md)

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

