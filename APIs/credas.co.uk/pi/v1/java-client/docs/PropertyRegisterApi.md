# PropertyRegisterApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addPropertyRegisterCheck**](PropertyRegisterApi.md#addPropertyRegisterCheck) | **POST** /api/property-register | Creates new property registry check against the registration. |
| [**getPropertyRegisterCheckResult**](PropertyRegisterApi.md#getPropertyRegisterCheckResult) | **GET** /api/property-register/{id} | Retrieves property registry check associated with the registration. |


<a id="addPropertyRegisterCheck"></a>
# **addPropertyRegisterCheck**
> CredasApiModelsPropertyRegisterPropertyRegisterCheckResponse addPropertyRegisterCheck(apikey, credasApiModelsPropertyRegisterPropertyRegisterCheckRequest)

Creates new property registry check against the registration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PropertyRegisterApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    PropertyRegisterApi apiInstance = new PropertyRegisterApi(defaultClient);
    String apikey = "apikey_example"; // String | ApiKey supplied.
    CredasApiModelsPropertyRegisterPropertyRegisterCheckRequest credasApiModelsPropertyRegisterPropertyRegisterCheckRequest = new CredasApiModelsPropertyRegisterPropertyRegisterCheckRequest(); // CredasApiModelsPropertyRegisterPropertyRegisterCheckRequest | Object containing check details.
    try {
      CredasApiModelsPropertyRegisterPropertyRegisterCheckResponse result = apiInstance.addPropertyRegisterCheck(apikey, credasApiModelsPropertyRegisterPropertyRegisterCheckRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PropertyRegisterApi#addPropertyRegisterCheck");
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
| **credasApiModelsPropertyRegisterPropertyRegisterCheckRequest** | [**CredasApiModelsPropertyRegisterPropertyRegisterCheckRequest**](CredasApiModelsPropertyRegisterPropertyRegisterCheckRequest.md)| Object containing check details. | [optional] |

### Return type

[**CredasApiModelsPropertyRegisterPropertyRegisterCheckResponse**](CredasApiModelsPropertyRegisterPropertyRegisterCheckResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/*+json, application/*+xml, application/json, application/json-patch+json, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Details of newly added data check. |  -  |
| **400** | If the service was supplied invalid data. |  -  |
| **401** | If credentials supplied were invalid. |  -  |
| **402** | Error code meaning that the operation was aborted due to insufficient credits. |  -  |
| **500** | If an unexpected exception occurred whilst processing the request. |  -  |

<a id="getPropertyRegisterCheckResult"></a>
# **getPropertyRegisterCheckResult**
> CredasApiModelsPropertyRegisterPropertyRegisterCheckResponse getPropertyRegisterCheckResult(id, apikey)

Retrieves property registry check associated with the registration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PropertyRegisterApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    PropertyRegisterApi apiInstance = new PropertyRegisterApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | Id of the registration.
    String apikey = "apikey_example"; // String | ApiKey supplied.
    try {
      CredasApiModelsPropertyRegisterPropertyRegisterCheckResponse result = apiInstance.getPropertyRegisterCheckResult(id, apikey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PropertyRegisterApi#getPropertyRegisterCheckResult");
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

[**CredasApiModelsPropertyRegisterPropertyRegisterCheckResponse**](CredasApiModelsPropertyRegisterPropertyRegisterCheckResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Details of the property register check. |  -  |
| **400** | If the service was supplied invalid data. |  -  |
| **401** | If credentials supplied were invalid. |  -  |
| **404** | If registration does not have associated property register check. |  -  |
| **500** | If an unexpected exception occurred whilst processing the request. |  -  |

