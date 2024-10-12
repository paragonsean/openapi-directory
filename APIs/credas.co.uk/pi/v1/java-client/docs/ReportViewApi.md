# ReportViewApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getReportViewByReferenceId**](ReportViewApi.md#getReportViewByReferenceId) | **POST** /api/report-view/by-referenceid | Retrieves secure links to registration details pages searching by the Reference Id. |
| [**getReportViewByRegistrationId**](ReportViewApi.md#getReportViewByRegistrationId) | **POST** /api/report-view/by-registrationid | Retrieves secure link to registration details page searching by the Registration Id. |


<a id="getReportViewByReferenceId"></a>
# **getReportViewByReferenceId**
> CredasApiModelsReportViewGetReportViewResponse getReportViewByReferenceId(apikey, credasApiModelsReportViewGetReportViewByReferenceIdRequest)

Retrieves secure links to registration details pages searching by the Reference Id.

It may return none, one or many (up to 20) matching results.  Each result contains a secure url; UTC date/time of when the link expires; name details of a person associated with the registration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportViewApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ReportViewApi apiInstance = new ReportViewApi(defaultClient);
    String apikey = "apikey_example"; // String | ApiKey supplied.
    CredasApiModelsReportViewGetReportViewByReferenceIdRequest credasApiModelsReportViewGetReportViewByReferenceIdRequest = new CredasApiModelsReportViewGetReportViewByReferenceIdRequest(); // CredasApiModelsReportViewGetReportViewByReferenceIdRequest | Request object
    try {
      CredasApiModelsReportViewGetReportViewResponse result = apiInstance.getReportViewByReferenceId(apikey, credasApiModelsReportViewGetReportViewByReferenceIdRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportViewApi#getReportViewByReferenceId");
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
| **credasApiModelsReportViewGetReportViewByReferenceIdRequest** | [**CredasApiModelsReportViewGetReportViewByReferenceIdRequest**](CredasApiModelsReportViewGetReportViewByReferenceIdRequest.md)| Request object | [optional] |

### Return type

[**CredasApiModelsReportViewGetReportViewResponse**](CredasApiModelsReportViewGetReportViewResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/*+json, application/*+xml, application/json, application/json-patch+json, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Results of the query |  -  |
| **400** | If the service was supplied invalid data. |  -  |
| **401** | If credentials supplied were invalid. |  -  |
| **500** | If an unexpected exception occurred whilst processing the request. |  -  |

<a id="getReportViewByRegistrationId"></a>
# **getReportViewByRegistrationId**
> CredasApiModelsReportViewGetReportViewResponse getReportViewByRegistrationId(apikey, credasApiModelsReportViewGetReportViewByRegistrationIdRequest)

Retrieves secure link to registration details page searching by the Registration Id.

It may return none or one matching result.  Each result contains a secure url; UTC date/time of when the link expires; name details of a person associated with the registration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportViewApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ReportViewApi apiInstance = new ReportViewApi(defaultClient);
    String apikey = "apikey_example"; // String | ApiKey supplied.
    CredasApiModelsReportViewGetReportViewByRegistrationIdRequest credasApiModelsReportViewGetReportViewByRegistrationIdRequest = new CredasApiModelsReportViewGetReportViewByRegistrationIdRequest(); // CredasApiModelsReportViewGetReportViewByRegistrationIdRequest | Request object
    try {
      CredasApiModelsReportViewGetReportViewResponse result = apiInstance.getReportViewByRegistrationId(apikey, credasApiModelsReportViewGetReportViewByRegistrationIdRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportViewApi#getReportViewByRegistrationId");
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
| **credasApiModelsReportViewGetReportViewByRegistrationIdRequest** | [**CredasApiModelsReportViewGetReportViewByRegistrationIdRequest**](CredasApiModelsReportViewGetReportViewByRegistrationIdRequest.md)| Request object | [optional] |

### Return type

[**CredasApiModelsReportViewGetReportViewResponse**](CredasApiModelsReportViewGetReportViewResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/*+json, application/*+xml, application/json, application/json-patch+json, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Results of the query |  -  |
| **400** | If the service was supplied invalid data. |  -  |
| **401** | If credentials supplied were invalid. |  -  |
| **500** | If an unexpected exception occurred whilst processing the request. |  -  |

