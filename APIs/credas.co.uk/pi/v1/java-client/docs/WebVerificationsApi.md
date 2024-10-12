# WebVerificationsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getWebVerificationsByReferenceId**](WebVerificationsApi.md#getWebVerificationsByReferenceId) | **POST** /api/web-verifications/by-referenceid | Retrieves secure links to web verification pages searching by the Reference Id. |
| [**getWebVerificationsByRegistrationId**](WebVerificationsApi.md#getWebVerificationsByRegistrationId) | **POST** /api/web-verifications/by-registrationid | Retrieves secure link to web verification page searching by the Registration Id. |


<a id="getWebVerificationsByReferenceId"></a>
# **getWebVerificationsByReferenceId**
> CredasApiModelsWebVerificationsGetWebVerificationsResponse getWebVerificationsByReferenceId(apikey, credasApiModelsWebVerificationsGetWebVerificationsByReferenceIdRequest)

Retrieves secure links to web verification pages searching by the Reference Id.

It may return none, one or many (up to 20) matching results.  Each result contains a secure url; UTC date/time of when the link expires; name details of a person associated with the registration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebVerificationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    WebVerificationsApi apiInstance = new WebVerificationsApi(defaultClient);
    String apikey = "apikey_example"; // String | ApiKey supplied.
    CredasApiModelsWebVerificationsGetWebVerificationsByReferenceIdRequest credasApiModelsWebVerificationsGetWebVerificationsByReferenceIdRequest = new CredasApiModelsWebVerificationsGetWebVerificationsByReferenceIdRequest(); // CredasApiModelsWebVerificationsGetWebVerificationsByReferenceIdRequest | 
    try {
      CredasApiModelsWebVerificationsGetWebVerificationsResponse result = apiInstance.getWebVerificationsByReferenceId(apikey, credasApiModelsWebVerificationsGetWebVerificationsByReferenceIdRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebVerificationsApi#getWebVerificationsByReferenceId");
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
| **credasApiModelsWebVerificationsGetWebVerificationsByReferenceIdRequest** | [**CredasApiModelsWebVerificationsGetWebVerificationsByReferenceIdRequest**](CredasApiModelsWebVerificationsGetWebVerificationsByReferenceIdRequest.md)|  | [optional] |

### Return type

[**CredasApiModelsWebVerificationsGetWebVerificationsResponse**](CredasApiModelsWebVerificationsGetWebVerificationsResponse.md)

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

<a id="getWebVerificationsByRegistrationId"></a>
# **getWebVerificationsByRegistrationId**
> CredasApiModelsWebVerificationsGetWebVerificationsResponse getWebVerificationsByRegistrationId(apikey, credasApiModelsWebVerificationsGetWebVerificationsByRegistrationIdRequest)

Retrieves secure link to web verification page searching by the Registration Id.

It may return none or one matching result.  Each result contains a secure url; UTC date/time of when the link expires; name details of a person associated with the registration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebVerificationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    WebVerificationsApi apiInstance = new WebVerificationsApi(defaultClient);
    String apikey = "apikey_example"; // String | ApiKey supplied.
    CredasApiModelsWebVerificationsGetWebVerificationsByRegistrationIdRequest credasApiModelsWebVerificationsGetWebVerificationsByRegistrationIdRequest = new CredasApiModelsWebVerificationsGetWebVerificationsByRegistrationIdRequest(); // CredasApiModelsWebVerificationsGetWebVerificationsByRegistrationIdRequest | 
    try {
      CredasApiModelsWebVerificationsGetWebVerificationsResponse result = apiInstance.getWebVerificationsByRegistrationId(apikey, credasApiModelsWebVerificationsGetWebVerificationsByRegistrationIdRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebVerificationsApi#getWebVerificationsByRegistrationId");
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
| **credasApiModelsWebVerificationsGetWebVerificationsByRegistrationIdRequest** | [**CredasApiModelsWebVerificationsGetWebVerificationsByRegistrationIdRequest**](CredasApiModelsWebVerificationsGetWebVerificationsByRegistrationIdRequest.md)|  | [optional] |

### Return type

[**CredasApiModelsWebVerificationsGetWebVerificationsResponse**](CredasApiModelsWebVerificationsGetWebVerificationsResponse.md)

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

