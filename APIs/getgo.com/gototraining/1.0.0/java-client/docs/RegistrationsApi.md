# RegistrationsApi

All URIs are relative to *https://api.getgo.com/G2T/rest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cancelRegistration**](RegistrationsApi.md#cancelRegistration) | **DELETE** /organizers/{organizerKey}/trainings/{trainingKey}/registrants/{registrantKey} | Cancel Registration |
| [**getRegistrant**](RegistrationsApi.md#getRegistrant) | **GET** /organizers/{organizerKey}/trainings/{trainingKey}/registrants/{registrantKey} | Get Registrant |
| [**getRegistrants**](RegistrationsApi.md#getRegistrants) | **GET** /organizers/{organizerKey}/trainings/{trainingKey}/registrants | Get Training Registrants |
| [**registerForTraining**](RegistrationsApi.md#registerForTraining) | **POST** /organizers/{organizerKey}/trainings/{trainingKey}/registrants | Register for Training |


<a id="cancelRegistration"></a>
# **cancelRegistration**
> cancelRegistration(authorization, organizerKey, trainingKey, registrantKey)

Cancel Registration

This call cancels a registration in a scheduled training for a specific registrant. If the registrant has paid for the training, a cancellation cannot be completed with this method; it must be completed on the external admin site. No notification is sent to the registrant or the organizer by default. The registrant can re-register if needed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistrationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.getgo.com/G2T/rest");

    RegistrationsApi apiInstance = new RegistrationsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long organizerKey = 56L; // Long | The key of the training organizer
    Long trainingKey = 56L; // Long | The key of the training
    Long registrantKey = 56L; // Long | The key of the registrant
    try {
      apiInstance.cancelRegistration(authorization, organizerKey, trainingKey, registrantKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrationsApi#cancelRegistration");
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
| **authorization** | **String**| Access token | |
| **organizerKey** | **Long**| The key of the training organizer | |
| **trainingKey** | **Long**| The key of the training | |
| **registrantKey** | **Long**| The key of the registrant | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getRegistrant"></a>
# **getRegistrant**
> Registrant getRegistrant(authorization, organizerKey, trainingKey, registrantKey)

Get Registrant

Retrieves details for specific registrant in a specific training. Registrants can be:&lt;br&gt;WAITING - registrant registered and is awaiting approval (where organizer has required approval)&lt;br&gt;APPROVED - registrant registered and is approved&lt;br&gt;DENIED - registrant registered and was not approved.&lt;br&gt;&lt;br&gt;IMPORTANT: The registrant data caches are typically updated immediately and the data will be returned in the response. However, the update can take as long as two hours.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistrationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.getgo.com/G2T/rest");

    RegistrationsApi apiInstance = new RegistrationsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long organizerKey = 56L; // Long | The key of the training organizer
    Long trainingKey = 56L; // Long | The key of the training
    Long registrantKey = 56L; // Long | The key of the registrant
    try {
      Registrant result = apiInstance.getRegistrant(authorization, organizerKey, trainingKey, registrantKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrationsApi#getRegistrant");
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
| **authorization** | **String**| Access token | |
| **organizerKey** | **Long**| The key of the training organizer | |
| **trainingKey** | **Long**| The key of the training | |
| **registrantKey** | **Long**| The key of the registrant | |

### Return type

[**Registrant**](Registrant.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getRegistrants"></a>
# **getRegistrants**
> List&lt;Registrant&gt; getRegistrants(authorization, organizerKey, trainingKey)

Get Training Registrants

Retrieves details on all registrants for a specific training. Registrants can be:&lt;br&gt;WAITING - registrant registered and is awaiting approval (where organizer has required approval)&lt;br&gt;APPROVED - registrant registered and is approved&lt;br&gt;DENIED - registrant registered and was not approved.&lt;br&gt;&lt;br&gt;IMPORTANT: The registrant data caches are typically updated immediately and the data will be returned in the response. However, the update can take as long as two hours.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistrationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.getgo.com/G2T/rest");

    RegistrationsApi apiInstance = new RegistrationsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long organizerKey = 56L; // Long | The key of the training organizer
    Long trainingKey = 56L; // Long | The key of the training
    try {
      List<Registrant> result = apiInstance.getRegistrants(authorization, organizerKey, trainingKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrationsApi#getRegistrants");
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
| **authorization** | **String**| Access token | |
| **organizerKey** | **Long**| The key of the training organizer | |
| **trainingKey** | **Long**| The key of the training | |

### Return type

[**List&lt;Registrant&gt;**](Registrant.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="registerForTraining"></a>
# **registerForTraining**
> RegistrantCreated registerForTraining(authorization, organizerKey, trainingKey, body)

Register for Training

Registers one person, identified by a unique email address, for a training. Approval is automatic unless payment or approval is required. The response contains the Confirmation page URL and Join URL for the registrant. NOTE: If some registrants do not receive a confirmation email, the emails could be getting blocked by their email server due to spam filtering or a grey-listing setting.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistrationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.getgo.com/G2T/rest");

    RegistrationsApi apiInstance = new RegistrationsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long organizerKey = 56L; // Long | The key of the training organizer
    Long trainingKey = 56L; // Long | The key of the training
    RegistrantReqCreate body = new RegistrantReqCreate(); // RegistrantReqCreate | The details of the registrant to create
    try {
      RegistrantCreated result = apiInstance.registerForTraining(authorization, organizerKey, trainingKey, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrationsApi#registerForTraining");
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
| **authorization** | **String**| Access token | |
| **organizerKey** | **Long**| The key of the training organizer | |
| **trainingKey** | **Long**| The key of the training | |
| **body** | [**RegistrantReqCreate**](RegistrantReqCreate.md)| The details of the registrant to create | |

### Return type

[**RegistrantCreated**](RegistrantCreated.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **409** | Conflict |  -  |

