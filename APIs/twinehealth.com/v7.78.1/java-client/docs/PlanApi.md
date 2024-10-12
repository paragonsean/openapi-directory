# PlanApi

All URIs are relative to *https://api.twinehealth.com/pub*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchPatientPlanSummaries**](PlanApi.md#fetchPatientPlanSummaries) | **GET** /patient_plan_summary | List patient plan summaries |
| [**fetchPatientPlanSummary**](PlanApi.md#fetchPatientPlanSummary) | **GET** /patient_plan_summary/{id} | Get the plan summary for a patient |
| [**updatePatientPlanSummary**](PlanApi.md#updatePatientPlanSummary) | **PATCH** /patient_plan_summary/{id} | Update a plan summary |


<a id="fetchPatientPlanSummaries"></a>
# **fetchPatientPlanSummaries**
> FetchPatientPlanSummariesResponse fetchPatientPlanSummaries(filterPatient, filterGroups, filterOrganization, include)

List patient plan summaries

Get a list of patient plan summaries

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlanApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twinehealth.com/pub");

    PlanApi apiInstance = new PlanApi(defaultClient);
    String filterPatient = "filterPatient_example"; // String | Patient id to fetch plan summary for. Note that one of the following filters must be specified: `filter[patient]`, `filter[groups]`, `filter[organization]`. 
    String filterGroups = "filterGroups_example"; // String | Comma-separated list of group ids. Note that one of the following filters must be specified: `filter[patient]`, `filter[groups]`, `filter[organization]`. 
    String filterOrganization = "filterOrganization_example"; // String | Fitbit Plus organization id. Note that one of the following filters must be specified: `filter[patient]`, `filter[groups]`, `filter[organization]`. 
    String include = "actions"; // String | List of related resources to include in the response
    try {
      FetchPatientPlanSummariesResponse result = apiInstance.fetchPatientPlanSummaries(filterPatient, filterGroups, filterOrganization, include);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlanApi#fetchPatientPlanSummaries");
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
| **filterPatient** | **String**| Patient id to fetch plan summary for. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[groups]&#x60;, &#x60;filter[organization]&#x60;.  | [optional] |
| **filterGroups** | **String**| Comma-separated list of group ids. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[groups]&#x60;, &#x60;filter[organization]&#x60;.  | [optional] |
| **filterOrganization** | **String**| Fitbit Plus organization id. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[groups]&#x60;, &#x60;filter[organization]&#x60;.  | [optional] |
| **include** | **String**| List of related resources to include in the response | [optional] [enum: actions, bundles, patient, current_results] |

### Return type

[**FetchPatientPlanSummariesResponse**](FetchPatientPlanSummariesResponse.md)

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

<a id="fetchPatientPlanSummary"></a>
# **fetchPatientPlanSummary**
> FetchPatientPlanSummaryResponse fetchPatientPlanSummary(id, include)

Get the plan summary for a patient

Get the plan summary for a patient.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlanApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twinehealth.com/pub");

    PlanApi apiInstance = new PlanApi(defaultClient);
    String id = "id_example"; // String | Plan summary identifier
    String include = "actions"; // String | List of related resources to include in the response
    try {
      FetchPatientPlanSummaryResponse result = apiInstance.fetchPatientPlanSummary(id, include);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlanApi#fetchPatientPlanSummary");
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
| **id** | **String**| Plan summary identifier | |
| **include** | **String**| List of related resources to include in the response | [optional] [enum: actions, bundles, patient, current_results] |

### Return type

[**FetchPatientPlanSummaryResponse**](FetchPatientPlanSummaryResponse.md)

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

<a id="updatePatientPlanSummary"></a>
# **updatePatientPlanSummary**
> UpdatePatientPlanSummaryResponse updatePatientPlanSummary(id, updatePatientPlanSummaryRequest)

Update a plan summary

Update a plan summary record for a patient.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlanApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twinehealth.com/pub");

    PlanApi apiInstance = new PlanApi(defaultClient);
    String id = "id_example"; // String | Plan summary identifier
    UpdatePatientPlanSummaryRequest updatePatientPlanSummaryRequest = new UpdatePatientPlanSummaryRequest(); // UpdatePatientPlanSummaryRequest | 
    try {
      UpdatePatientPlanSummaryResponse result = apiInstance.updatePatientPlanSummary(id, updatePatientPlanSummaryRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlanApi#updatePatientPlanSummary");
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
| **id** | **String**| Plan summary identifier | |
| **updatePatientPlanSummaryRequest** | [**UpdatePatientPlanSummaryRequest**](UpdatePatientPlanSummaryRequest.md)|  | |

### Return type

[**UpdatePatientPlanSummaryResponse**](UpdatePatientPlanSummaryResponse.md)

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

