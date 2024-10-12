# PersonalPagingPolicyValuesApi

All URIs are relative to *https://api.victorops.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiPublicV1PoliciesTypesContactsGet**](PersonalPagingPolicyValuesApi.md#apiPublicV1PoliciesTypesContactsGet) | **GET** /api-public/v1/policies/types/contacts | Get the available contact types |
| [**apiPublicV1PoliciesTypesNotificationsGet**](PersonalPagingPolicyValuesApi.md#apiPublicV1PoliciesTypesNotificationsGet) | **GET** /api-public/v1/policies/types/notifications | Get the available notification types |
| [**apiPublicV1PoliciesTypesTimeoutsGet**](PersonalPagingPolicyValuesApi.md#apiPublicV1PoliciesTypesTimeoutsGet) | **GET** /api-public/v1/policies/types/timeouts | Get the available timeout values |


<a id="apiPublicV1PoliciesTypesContactsGet"></a>
# **apiPublicV1PoliciesTypesContactsGet**
> ApiPublicV1PoliciesTypesContactsGet200Response apiPublicV1PoliciesTypesContactsGet(xVOApiId, xVOApiKey)

Get the available contact types

Get the available contact types  description: \&quot;Email Address\&quot;, type: \&quot;email\&quot; description: \&quot;Phone Number\&quot;, type: \&quot;phone\&quot;  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PersonalPagingPolicyValuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    PersonalPagingPolicyValuesApi apiInstance = new PersonalPagingPolicyValuesApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    try {
      ApiPublicV1PoliciesTypesContactsGet200Response result = apiInstance.apiPublicV1PoliciesTypesContactsGet(xVOApiId, xVOApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PersonalPagingPolicyValuesApi#apiPublicV1PoliciesTypesContactsGet");
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
| **xVOApiId** | **String**| Your API ID | |
| **xVOApiKey** | **String**| Your API Key | |

### Return type

[**ApiPublicV1PoliciesTypesContactsGet200Response**](ApiPublicV1PoliciesTypesContactsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All the available contact types |  -  |
| **400** | Problem with the request arguments.  The response payload may include an error message. |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **500** | Internal Server Error |  -  |

<a id="apiPublicV1PoliciesTypesNotificationsGet"></a>
# **apiPublicV1PoliciesTypesNotificationsGet**
> ApiPublicV1PoliciesTypesNotificationsGet200Response apiPublicV1PoliciesTypesNotificationsGet(xVOApiId, xVOApiKey)

Get the available notification types

Get the available notification types  description: \&quot;Send a push notification to all my devices\&quot;, type: \&quot;push\&quot; description: \&quot;Send an email to an email address\&quot;, type: \&quot;email\&quot; description: \&quot;Send an SMS to a phone number\&quot;, type: \&quot;sms\&quot; description: \&quot;Make a phone call to a phone number\&quot;, type: \&quot;phone\&quot;  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PersonalPagingPolicyValuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    PersonalPagingPolicyValuesApi apiInstance = new PersonalPagingPolicyValuesApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    try {
      ApiPublicV1PoliciesTypesNotificationsGet200Response result = apiInstance.apiPublicV1PoliciesTypesNotificationsGet(xVOApiId, xVOApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PersonalPagingPolicyValuesApi#apiPublicV1PoliciesTypesNotificationsGet");
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
| **xVOApiId** | **String**| Your API ID | |
| **xVOApiKey** | **String**| Your API Key | |

### Return type

[**ApiPublicV1PoliciesTypesNotificationsGet200Response**](ApiPublicV1PoliciesTypesNotificationsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All the available contact types |  -  |
| **400** | Problem with the request arguments.  The response payload may include an error message. |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **500** | Internal Server Error |  -  |

<a id="apiPublicV1PoliciesTypesTimeoutsGet"></a>
# **apiPublicV1PoliciesTypesTimeoutsGet**
> ApiPublicV1PoliciesTypesTimeoutsGet200Response apiPublicV1PoliciesTypesTimeoutsGet(xVOApiId, xVOApiKey)

Get the available timeout values

Get the available timeout values  description: \&quot;If still unacked after 1 minute\&quot;, type: 1 description: \&quot;If still unacked after 5 minutes\&quot;, type: 5 description: \&quot;If still unacked after 10 minutes\&quot;, type: 10 description: \&quot;If still unacked after 15 minutes\&quot;, type: 15 description: \&quot;If still unacked after 20 minutes\&quot;, type: 20 description: \&quot;If still unacked after 25 minutes\&quot;, type: 25 description: \&quot;If still unacked after 30 minutes\&quot;, type: 30 description: \&quot;If still unacked after 45 minutes\&quot;, type: 45 description: \&quot;If still unacked after 60 minutes\&quot;, type: 60  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PersonalPagingPolicyValuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    PersonalPagingPolicyValuesApi apiInstance = new PersonalPagingPolicyValuesApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    try {
      ApiPublicV1PoliciesTypesTimeoutsGet200Response result = apiInstance.apiPublicV1PoliciesTypesTimeoutsGet(xVOApiId, xVOApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PersonalPagingPolicyValuesApi#apiPublicV1PoliciesTypesTimeoutsGet");
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
| **xVOApiId** | **String**| Your API ID | |
| **xVOApiKey** | **String**| Your API Key | |

### Return type

[**ApiPublicV1PoliciesTypesTimeoutsGet200Response**](ApiPublicV1PoliciesTypesTimeoutsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All the available timeout types. |  -  |
| **400** | Problem with the request arguments.  The response payload may include an error message. |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **500** | Internal Server Error |  -  |

