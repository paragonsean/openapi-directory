# ResultApi

All URIs are relative to *https://api.twinehealth.com/pub*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchPatientHealthResult**](ResultApi.md#fetchPatientHealthResult) | **GET** /result/{id} | Get a patient health result |
| [**fetchPatientHealthResults**](ResultApi.md#fetchPatientHealthResults) | **GET** /result | List patient health results |


<a id="fetchPatientHealthResult"></a>
# **fetchPatientHealthResult**
> FetchPatientHealthResultResponse fetchPatientHealthResult(id)

Get a patient health result

Get patient health result by id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twinehealth.com/pub");

    ResultApi apiInstance = new ResultApi(defaultClient);
    String id = "id_example"; // String | Patient health result identifier
    try {
      FetchPatientHealthResultResponse result = apiInstance.fetchPatientHealthResult(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResultApi#fetchPatientHealthResult");
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
| **id** | **String**| Patient health result identifier | |

### Return type

[**FetchPatientHealthResultResponse**](FetchPatientHealthResultResponse.md)

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

<a id="fetchPatientHealthResults"></a>
# **fetchPatientHealthResults**
> FetchPatientHealthResultResponse fetchPatientHealthResults(filterPatient, filterActions, filterStartAt, filterEndAt, filterThreads, filterCreatedAt, filterUpdatedAt, pageNumber, pageSize, pageLimit, pageAfter)

List patient health results

Get a list of patient health results.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twinehealth.com/pub");

    ResultApi apiInstance = new ResultApi(defaultClient);
    String filterPatient = "filterPatient_example"; // String | Filter the patient health results for a specified patient
    String filterActions = "filterActions_example"; // String | A comma-separated list of action identifiers
    String filterStartAt = "filterStartAt_example"; // String | Filter results that occurred after the passed ISO date and time string
    String filterEndAt = "filterEndAt_example"; // String | Filter results that occurred before the passed ISO date and time string
    String filterThreads = "filterThreads_example"; // String | A comma-separated list of thread identifiers
    String filterCreatedAt = "filterCreatedAt_example"; // String | The start (inclusive) and end (exclusive) dates are ISO date and time strings separated by `..`. Example for results created in November 2017 (America/New_York): `filter[created_at]=2017-11-01T00:00:00-04:00..2017-12-01T00:00:00-05:00` 
    String filterUpdatedAt = "filterUpdatedAt_example"; // String | The start (inclusive) and end (exclusive) dates are ISO date and time strings separated by `..`. Example for results updated in November 2017 (America/New_York): `filter[updated_at]=2017-11-01T00:00:00-04:00..2017-12-01T00:00:00-05:00` 
    Integer pageNumber = 1; // Integer | Page number
    Integer pageSize = 10; // Integer | Page size
    Integer pageLimit = 50; // Integer | Page limit
    String pageAfter = "pageAfter_example"; // String | Page cursor
    try {
      FetchPatientHealthResultResponse result = apiInstance.fetchPatientHealthResults(filterPatient, filterActions, filterStartAt, filterEndAt, filterThreads, filterCreatedAt, filterUpdatedAt, pageNumber, pageSize, pageLimit, pageAfter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResultApi#fetchPatientHealthResults");
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
| **filterPatient** | **String**| Filter the patient health results for a specified patient | |
| **filterActions** | **String**| A comma-separated list of action identifiers | [optional] |
| **filterStartAt** | **String**| Filter results that occurred after the passed ISO date and time string | [optional] |
| **filterEndAt** | **String**| Filter results that occurred before the passed ISO date and time string | [optional] |
| **filterThreads** | **String**| A comma-separated list of thread identifiers | [optional] |
| **filterCreatedAt** | **String**| The start (inclusive) and end (exclusive) dates are ISO date and time strings separated by &#x60;..&#x60;. Example for results created in November 2017 (America/New_York): &#x60;filter[created_at]&#x3D;2017-11-01T00:00:00-04:00..2017-12-01T00:00:00-05:00&#x60;  | [optional] |
| **filterUpdatedAt** | **String**| The start (inclusive) and end (exclusive) dates are ISO date and time strings separated by &#x60;..&#x60;. Example for results updated in November 2017 (America/New_York): &#x60;filter[updated_at]&#x3D;2017-11-01T00:00:00-04:00..2017-12-01T00:00:00-05:00&#x60;  | [optional] |
| **pageNumber** | **Integer**| Page number | [optional] [default to 1] |
| **pageSize** | **Integer**| Page size | [optional] [default to 10] |
| **pageLimit** | **Integer**| Page limit | [optional] [default to 50] |
| **pageAfter** | **String**| Page cursor | [optional] |

### Return type

[**FetchPatientHealthResultResponse**](FetchPatientHealthResultResponse.md)

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

