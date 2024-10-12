# CoOrganizersApi

All URIs are relative to *https://api.getgo.com/G2W/rest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createCoorganizers**](CoOrganizersApi.md#createCoorganizers) | **POST** /organizers/{organizerKey}/webinars/{webinarKey}/coorganizers | Create co-organizers |
| [**deleteCoorganizer**](CoOrganizersApi.md#deleteCoorganizer) | **DELETE** /organizers/{organizerKey}/webinars/{webinarKey}/coorganizers/{coorganizerKey} | Delete co-organizer |
| [**getCoorganizers**](CoOrganizersApi.md#getCoorganizers) | **GET** /organizers/{organizerKey}/webinars/{webinarKey}/coorganizers | Get co-organizers |
| [**resendCoorganizerInvitation**](CoOrganizersApi.md#resendCoorganizerInvitation) | **POST** /organizers/{organizerKey}/webinars/{webinarKey}/coorganizers/{coorganizerKey}/resendInvitation | Resend invitation |


<a id="createCoorganizers"></a>
# **createCoorganizers**
> List&lt;Coorganizer&gt; createCoorganizers(authorization, organizerKey, webinarKey, body)

Create co-organizers

Creates co-organizers for the specified webinar. For co-organizers that have a GoToWebinar account you have to set the parameter &#39;external&#39; to &#39;false&#39;. In this case you have to pass the parameter &#39;organizerKey&#39; only. For co-organizers that have no GoToWebinar account you have to set the parameter &#39;external&#39; to &#39;true&#39;. In this case you have to pass the parameters &#39;givenName&#39; and &#39;email&#39;. Since there is no parameter for &#39;surname&#39; you should pass first and last name to the parameter &#39;givenName&#39;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CoOrganizersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.getgo.com/G2W/rest");

    CoOrganizersApi apiInstance = new CoOrganizersApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long organizerKey = 56L; // Long | The key of the organizer
    Long webinarKey = 56L; // Long | The key of the webinar
    List<CoorganizerReqCreate> body = Arrays.asList(); // List<CoorganizerReqCreate> | The co-organizer details
    try {
      List<Coorganizer> result = apiInstance.createCoorganizers(authorization, organizerKey, webinarKey, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CoOrganizersApi#createCoorganizers");
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
| **body** | [**List&lt;CoorganizerReqCreate&gt;**](CoorganizerReqCreate.md)| The co-organizer details | |

### Return type

[**List&lt;Coorganizer&gt;**](Coorganizer.md)

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

<a id="deleteCoorganizer"></a>
# **deleteCoorganizer**
> deleteCoorganizer(authorization, organizerKey, webinarKey, coorganizerKey, external)

Delete co-organizer

Deletes an internal co-organizer specified by the coorganizerKey (memberKey).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CoOrganizersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.getgo.com/G2W/rest");

    CoOrganizersApi apiInstance = new CoOrganizersApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long organizerKey = 56L; // Long | The key of the organizer
    Long webinarKey = 56L; // Long | The key of the webinar
    Long coorganizerKey = 56L; // Long | The key of the internal or external co-organizer (memberKey)
    Boolean external = true; // Boolean | By default only internal co-organizers (with a GoToWebinar account) can be deleted. If you want to use this call for external co-organizers you have to set this parameter to 'true'.
    try {
      apiInstance.deleteCoorganizer(authorization, organizerKey, webinarKey, coorganizerKey, external);
    } catch (ApiException e) {
      System.err.println("Exception when calling CoOrganizersApi#deleteCoorganizer");
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
| **coorganizerKey** | **Long**| The key of the internal or external co-organizer (memberKey) | |
| **external** | **Boolean**| By default only internal co-organizers (with a GoToWebinar account) can be deleted. If you want to use this call for external co-organizers you have to set this parameter to &#39;true&#39;. | [optional] |

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
| **204** | No Content (Co-organizer was deleted) |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getCoorganizers"></a>
# **getCoorganizers**
> List&lt;Coorganizer&gt; getCoorganizers(authorization, organizerKey, webinarKey)

Get co-organizers

Returns the co-organizers for the specified webinar. The original organizer who created the webinar is filtered out of the list. If the webinar has no co-organizers, an empty array is returned. Co-organizers that do not have a GoToWebinar account are returned as external co-organizers. For those organizers no surname is returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CoOrganizersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.getgo.com/G2W/rest");

    CoOrganizersApi apiInstance = new CoOrganizersApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long organizerKey = 56L; // Long | The key of the organizer
    Long webinarKey = 56L; // Long | The key of the webinar
    try {
      List<Coorganizer> result = apiInstance.getCoorganizers(authorization, organizerKey, webinarKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CoOrganizersApi#getCoorganizers");
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

[**List&lt;Coorganizer&gt;**](Coorganizer.md)

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

<a id="resendCoorganizerInvitation"></a>
# **resendCoorganizerInvitation**
> resendCoorganizerInvitation(authorization, organizerKey, webinarKey, coorganizerKey, external)

Resend invitation

Resends an invitation email to the specified co-organizer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CoOrganizersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.getgo.com/G2W/rest");

    CoOrganizersApi apiInstance = new CoOrganizersApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long organizerKey = 56L; // Long | The key of the organizer
    Long webinarKey = 56L; // Long | The key of the webinar
    Long coorganizerKey = 56L; // Long | The key of the internal or external co-organizer (memberKey)
    Boolean external = true; // Boolean | By default only internal co-organizers (with a GoToWebinar account) will retrieve the resent invitation email. If you want to use this call for external co-organizers you have to set this parameter to 'true'.
    try {
      apiInstance.resendCoorganizerInvitation(authorization, organizerKey, webinarKey, coorganizerKey, external);
    } catch (ApiException e) {
      System.err.println("Exception when calling CoOrganizersApi#resendCoorganizerInvitation");
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
| **coorganizerKey** | **Long**| The key of the internal or external co-organizer (memberKey) | |
| **external** | **Boolean**| By default only internal co-organizers (with a GoToWebinar account) will retrieve the resent invitation email. If you want to use this call for external co-organizers you have to set this parameter to &#39;true&#39;. | [optional] |

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
| **204** | No Content (Invitation email was sent) |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

