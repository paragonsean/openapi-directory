# RegistrantsApi

All URIs are relative to *https://api.getgo.com/G2W/rest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createRegistrant**](RegistrantsApi.md#createRegistrant) | **POST** /organizers/{organizerKey}/webinars/{webinarKey}/registrants | Create registrant |
| [**deleteRegistrant**](RegistrantsApi.md#deleteRegistrant) | **DELETE** /organizers/{organizerKey}/webinars/{webinarKey}/registrants/{registrantKey} | Delete registrant |
| [**getAllRegistrantsForWebinar**](RegistrantsApi.md#getAllRegistrantsForWebinar) | **GET** /organizers/{organizerKey}/webinars/{webinarKey}/registrants | Get registrants |
| [**getRegistrant**](RegistrantsApi.md#getRegistrant) | **GET** /organizers/{organizerKey}/webinars/{webinarKey}/registrants/{registrantKey} | Get registrant |
| [**getRegistrationFields**](RegistrantsApi.md#getRegistrationFields) | **GET** /organizers/{organizerKey}/webinars/{webinarKey}/registrants/fields | Get registration fields |


<a id="createRegistrant"></a>
# **createRegistrant**
> RegistrantCreated createRegistrant(authorization, organizerKey, webinarKey, body, accept, resendConfirmation)

Create registrant

Register an attendee for a scheduled webinar. The response contains the registrantKey and join URL for the registrant. An email will be sent to the registrant unless the organizer turns off the confirmation email setting from the GoToWebinar website. Please note that you must provide all required fields including custom fields defined during the webinar creation. Use the API call &#39;Get registration fields&#39; to get a list of all fields, if they are required, and their possible values. At this time there are two versions of the &#39;Create Registrant&#39; call. The first version only accepts firstName, lastName, and email and ignores all other fields. If you have custom fields or want to capture additional information this version won&#39;t work for you. The second version allows you to pass all required and optional fields, including custom fields defined when creating the webinar. To use the second version you must pass the header value &#39;Accept: application/vnd.citrix.g2wapi-v1.1+json&#39; instead of &#39;Accept: application/json&#39;. Leaving this header out results in the first version of the API call.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistrantsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.getgo.com/G2W/rest");

    RegistrantsApi apiInstance = new RegistrantsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long organizerKey = 56L; // Long | The key of the organizer
    Long webinarKey = 56L; // Long | The key of the webinar
    RegistrantFields body = new RegistrantFields(); // RegistrantFields | The registrant details. To get all possible values run the API call 'Get registration fields' which is also part of this documentation.
    String accept = "accept_example"; // String | Set to 'application/vnd.citrix.g2wapi-v1.1+json' to make a registration using fields (custom or default) additional to the basic ones.
    Boolean resendConfirmation = true; // Boolean | Indicates whether the confirmation email should be resent when a registrant is re-registered. The default value is false.
    try {
      RegistrantCreated result = apiInstance.createRegistrant(authorization, organizerKey, webinarKey, body, accept, resendConfirmation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrantsApi#createRegistrant");
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
| **organizerKey** | **Long**| The key of the organizer | |
| **webinarKey** | **Long**| The key of the webinar | |
| **body** | [**RegistrantFields**](RegistrantFields.md)| The registrant details. To get all possible values run the API call &#39;Get registration fields&#39; which is also part of this documentation. | |
| **accept** | **String**| Set to &#39;application/vnd.citrix.g2wapi-v1.1+json&#39; to make a registration using fields (custom or default) additional to the basic ones. | [optional] |
| **resendConfirmation** | **Boolean**| Indicates whether the confirmation email should be resent when a registrant is re-registered. The default value is false. | [optional] |

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
| **404** | Not found |  -  |
| **409** | The user is already registered |  -  |

<a id="deleteRegistrant"></a>
# **deleteRegistrant**
> deleteRegistrant(authorization, organizerKey, webinarKey, registrantKey)

Delete registrant

Removes a webinar registrant from current registrations for the specified webinar. The webinar must be a scheduled, future webinar.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistrantsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.getgo.com/G2W/rest");

    RegistrantsApi apiInstance = new RegistrantsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long organizerKey = 56L; // Long | The key of the organizer
    Long webinarKey = 56L; // Long | The key of the webinar
    Long registrantKey = 56L; // Long | The key of the registrant
    try {
      apiInstance.deleteRegistrant(authorization, organizerKey, webinarKey, registrantKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrantsApi#deleteRegistrant");
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
| **organizerKey** | **Long**| The key of the organizer | |
| **webinarKey** | **Long**| The key of the webinar | |
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
| **204** | No content |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |

<a id="getAllRegistrantsForWebinar"></a>
# **getAllRegistrantsForWebinar**
> List&lt;Registrant&gt; getAllRegistrantsForWebinar(authorization, organizerKey, webinarKey)

Get registrants

Retrieve registration details for all registrants of a specific webinar. Registrant details will not include all fields captured when creating the registrant. To see all data, use the API call &#39;Get Registrant&#39;. Registrants can have one of the following states; &lt;br&gt;WAITING - registrant registered and is awaiting approval (where organizer has required approval), &lt;br&gt;APPROVED - registrant registered and is approved, and &lt;br&gt;DENIED - registrant registered and was denied.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistrantsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.getgo.com/G2W/rest");

    RegistrantsApi apiInstance = new RegistrantsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long organizerKey = 56L; // Long | The key of the organizer
    Long webinarKey = 56L; // Long | The key of the webinar
    try {
      List<Registrant> result = apiInstance.getAllRegistrantsForWebinar(authorization, organizerKey, webinarKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrantsApi#getAllRegistrantsForWebinar");
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
| **organizerKey** | **Long**| The key of the organizer | |
| **webinarKey** | **Long**| The key of the webinar | |

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
| **404** | Not found |  -  |

<a id="getRegistrant"></a>
# **getRegistrant**
> RegistrantDetailed getRegistrant(authorization, organizerKey, webinarKey, registrantKey)

Get registrant

Retrieve registration details for a specific registrant.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistrantsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.getgo.com/G2W/rest");

    RegistrantsApi apiInstance = new RegistrantsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long organizerKey = 56L; // Long | The key of the organizer
    Long webinarKey = 56L; // Long | The key of the webinar
    Long registrantKey = 56L; // Long | The key of the registrant
    try {
      RegistrantDetailed result = apiInstance.getRegistrant(authorization, organizerKey, webinarKey, registrantKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrantsApi#getRegistrant");
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
| **organizerKey** | **Long**| The key of the organizer | |
| **webinarKey** | **Long**| The key of the webinar | |
| **registrantKey** | **Long**| The key of the registrant | |

### Return type

[**RegistrantDetailed**](RegistrantDetailed.md)

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
| **404** | Not found |  -  |

<a id="getRegistrationFields"></a>
# **getRegistrationFields**
> RegistrationFields getRegistrationFields(authorization, organizerKey, webinarKey)

Get registration fields

Retrieve required, optional registration, and custom questions for a specified webinar.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistrantsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.getgo.com/G2W/rest");

    RegistrantsApi apiInstance = new RegistrantsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long organizerKey = 56L; // Long | The key of the organizer
    Long webinarKey = 56L; // Long | The key of the webinar
    try {
      RegistrationFields result = apiInstance.getRegistrationFields(authorization, organizerKey, webinarKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrantsApi#getRegistrationFields");
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
| **organizerKey** | **Long**| The key of the organizer | |
| **webinarKey** | **Long**| The key of the webinar | |

### Return type

[**RegistrationFields**](RegistrationFields.md)

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
| **404** | Not found |  -  |

