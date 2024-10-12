# ApplicationApi

All URIs are relative to *https://api.nexmo.com/beta/chatapp-accounts*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**linkApplication**](ApplicationApi.md#linkApplication) | **POST** /{provider}/{external_id}/applications | Link application to an account |
| [**unliWithoutApplicationnkApplication**](ApplicationApi.md#unliWithoutApplicationnkApplication) | **DELETE** /{provider}/{external_id}/applications/{application_id} | Unlink application from an account |


<a id="linkApplication"></a>
# **linkApplication**
> AccountResponse linkApplication(provider, externalId, linkApplicationRequest)

Link application to an account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nexmo.com/beta/chatapp-accounts");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    ApplicationApi apiInstance = new ApplicationApi(defaultClient);
    String provider = "messenger"; // String | Provider of the account you want to assign an application to
    String externalId = "externalId_example"; // String | External id of the account you want to assign an application to. This is channel dependent. For Facebook it will be your Facebook Page ID, for Viber your Viber Service Message ID and for WhatsApp your WhatsApp number.
    LinkApplicationRequest linkApplicationRequest = new LinkApplicationRequest(); // LinkApplicationRequest | Request body can contain any of the following. Please note, the only one application can be linked to the account.
    try {
      AccountResponse result = apiInstance.linkApplication(provider, externalId, linkApplicationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationApi#linkApplication");
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
| **provider** | **String**| Provider of the account you want to assign an application to | [enum: messenger, viber_service_msg, whatsapp] |
| **externalId** | **String**| External id of the account you want to assign an application to. This is channel dependent. For Facebook it will be your Facebook Page ID, for Viber your Viber Service Message ID and for WhatsApp your WhatsApp number. | |
| **linkApplicationRequest** | [**LinkApplicationRequest**](LinkApplicationRequest.md)| Request body can contain any of the following. Please note, the only one application can be linked to the account. | |

### Return type

[**AccountResponse**](AccountResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |
| **401** | Unauthorized. |  -  |
| **403** | Forbidden. |  -  |
| **409** | Conflict. |  -  |

<a id="unliWithoutApplicationnkApplication"></a>
# **unliWithoutApplicationnkApplication**
> unliWithoutApplicationnkApplication(provider, externalId, applicationId)

Unlink application from an account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nexmo.com/beta/chatapp-accounts");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    ApplicationApi apiInstance = new ApplicationApi(defaultClient);
    String provider = "messenger"; // String | Provider of the account you want to unlink an application from
    String externalId = "externalId_example"; // String | External id of the account you want to unlink an application from
    String applicationId = "applicationId_example"; // String | Id of the application you want to unlink
    try {
      apiInstance.unliWithoutApplicationnkApplication(provider, externalId, applicationId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationApi#unliWithoutApplicationnkApplication");
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
| **provider** | **String**| Provider of the account you want to unlink an application from | [enum: messenger, viber_service_msg, whatsapp] |
| **externalId** | **String**| External id of the account you want to unlink an application from | |
| **applicationId** | **String**| Id of the application you want to unlink | |

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content. |  -  |
| **401** | Unauthorized. |  -  |
| **403** | Forbidden. |  -  |
| **409** | Conflict. |  -  |

