# CertificateActionsApi

All URIs are relative to *https://api.hetzner.cloud/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**certificatesIdActionsActionIdGet**](CertificateActionsApi.md#certificatesIdActionsActionIdGet) | **GET** /certificates/{id}/actions/{action_id} | Get an Action for a Certificate |
| [**certificatesIdActionsGet**](CertificateActionsApi.md#certificatesIdActionsGet) | **GET** /certificates/{id}/actions | Get all Actions for a Certificate |
| [**certificatesIdActionsRetryPost**](CertificateActionsApi.md#certificatesIdActionsRetryPost) | **POST** /certificates/{id}/actions/retry | Retry Issuance or Renewal |


<a id="certificatesIdActionsActionIdGet"></a>
# **certificatesIdActionsActionIdGet**
> ActionResponse certificatesIdActionsActionIdGet(id, actionId)

Get an Action for a Certificate

Returns a specific Action for a Certificate. Only type &#x60;managed&#x60; Certificates have Actions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificateActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    CertificateActionsApi apiInstance = new CertificateActionsApi(defaultClient);
    Integer id = 56; // Integer | ID of the Certificate
    Integer actionId = 56; // Integer | ID of the Action
    try {
      ActionResponse result = apiInstance.certificatesIdActionsActionIdGet(id, actionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificateActionsApi#certificatesIdActionsActionIdGet");
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
| **id** | **Integer**| ID of the Certificate | |
| **actionId** | **Integer**| ID of the Action | |

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The &#x60;action&#x60; key contains the Certificate Action |  -  |

<a id="certificatesIdActionsGet"></a>
# **certificatesIdActionsGet**
> ActionsResponse certificatesIdActionsGet(id, sort, status)

Get all Actions for a Certificate

Returns all Action objects for a Certificate. You can sort the results by using the &#x60;sort&#x60; URI parameter, and filter them with the &#x60;status&#x60; parameter.  Only type &#x60;managed&#x60; Certificates can have Actions. For type &#x60;uploaded&#x60; Certificates the &#x60;actions&#x60; key will always contain an empty array. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificateActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    CertificateActionsApi apiInstance = new CertificateActionsApi(defaultClient);
    Integer id = 56; // Integer | ID of the Resource
    String sort = "id"; // String | Can be used multiple times.
    String status = "running"; // String | Can be used multiple times, the response will contain only Actions with specified statuses
    try {
      ActionsResponse result = apiInstance.certificatesIdActionsGet(id, sort, status);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificateActionsApi#certificatesIdActionsGet");
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
| **id** | **Integer**| ID of the Resource | |
| **sort** | **String**| Can be used multiple times. | [optional] [enum: id, id:asc, id:desc, command, command:asc, command:desc, status, status:asc, status:desc, progress, progress:asc, progress:desc, started, started:asc, started:desc, finished, finished:asc, finished:desc] |
| **status** | **String**| Can be used multiple times, the response will contain only Actions with specified statuses | [optional] [enum: running, success, error] |

### Return type

[**ActionsResponse**](ActionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The &#x60;actions&#x60; key contains a list of Actions |  -  |

<a id="certificatesIdActionsRetryPost"></a>
# **certificatesIdActionsRetryPost**
> ActionResponse certificatesIdActionsRetryPost(id)

Retry Issuance or Renewal

Retry a failed Certificate issuance or renewal.  Only applicable if the type of the Certificate is &#x60;managed&#x60; and the issuance or renewal status is &#x60;failed&#x60;.  #### Call specific error codes  | Code                                                    | Description                                                               | |---------------------------------------------------------|---------------------------------------------------------------------------| | &#x60;caa_record_does_not_allow_ca&#x60;                          | CAA record does not allow certificate authority                           | | &#x60;ca_dns_validation_failed&#x60;                              | Certificate Authority: DNS validation failed                              | | &#x60;ca_too_many_authorizations_failed_recently&#x60;            | Certificate Authority: Too many authorizations failed recently            | | &#x60;ca_too_many_certificates_issued_for_registered_domain&#x60; | Certificate Authority: Too many certificates issued for registered domain | | &#x60;ca_too_many_duplicate_certificates&#x60;                    | Certificate Authority: Too many duplicate certificates                    | | &#x60;could_not_verify_domain_delegated_to_zone&#x60;             | Could not verify domain delegated to zone                                 | | &#x60;dns_zone_not_found&#x60;                                    | DNS zone not found                                                        | | &#x60;dns_zone_is_secondary_zone&#x60;                            | DNS zone is a secondary zone                                              | 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificateActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    CertificateActionsApi apiInstance = new CertificateActionsApi(defaultClient);
    Integer id = 56; // Integer | ID of the Certificate
    try {
      ActionResponse result = apiInstance.certificatesIdActionsRetryPost(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificateActionsApi#certificatesIdActionsRetryPost");
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
| **id** | **Integer**| ID of the Certificate | |

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The &#x60;action&#x60; key contains the resulting Action |  -  |

