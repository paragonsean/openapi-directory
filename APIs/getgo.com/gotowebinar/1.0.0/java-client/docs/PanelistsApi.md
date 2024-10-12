# PanelistsApi

All URIs are relative to *https://api.getgo.com/G2W/rest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createPanelists**](PanelistsApi.md#createPanelists) | **POST** /organizers/{organizerKey}/webinars/{webinarKey}/panelists | Create Panelists |
| [**deleteWebinarPanelist**](PanelistsApi.md#deleteWebinarPanelist) | **DELETE** /organizers/{organizerKey}/webinars/{webinarKey}/panelists/{panelistKey} | Delete webinar panelist |
| [**getPanelists**](PanelistsApi.md#getPanelists) | **GET** /organizers/{organizerKey}/webinars/{webinarKey}/panelists | Get webinar panelists |
| [**resendPanelistInvitation**](PanelistsApi.md#resendPanelistInvitation) | **POST** /organizers/{organizerKey}/webinars/{webinarKey}/panelists/{panelistKey}/resendInvitation | Resend panelist invitation |


<a id="createPanelists"></a>
# **createPanelists**
> List&lt;CreatedPanelist&gt; createPanelists(authorization, organizerKey, webinarKey, body)

Create Panelists

Create panelists for a specified webinar

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PanelistsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.getgo.com/G2W/rest");

    PanelistsApi apiInstance = new PanelistsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long organizerKey = 56L; // Long | The key of the organizer
    Long webinarKey = 56L; // Long | The key of the webinar
    List<PanelistReqCreate> body = Arrays.asList(); // List<PanelistReqCreate> | Array of panelists
    try {
      List<CreatedPanelist> result = apiInstance.createPanelists(authorization, organizerKey, webinarKey, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PanelistsApi#createPanelists");
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
| **body** | [**List&lt;PanelistReqCreate&gt;**](PanelistReqCreate.md)| Array of panelists | |

### Return type

[**List&lt;CreatedPanelist&gt;**](CreatedPanelist.md)

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

<a id="deleteWebinarPanelist"></a>
# **deleteWebinarPanelist**
> deleteWebinarPanelist(authorization, organizerKey, webinarKey, panelistKey)

Delete webinar panelist

Removes a webinar panelist.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PanelistsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.getgo.com/G2W/rest");

    PanelistsApi apiInstance = new PanelistsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long organizerKey = 56L; // Long | The key of the organizer
    Long webinarKey = 56L; // Long | The key of the webinar
    Long panelistKey = 56L; // Long | The key of the webinar panelist
    try {
      apiInstance.deleteWebinarPanelist(authorization, organizerKey, webinarKey, panelistKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling PanelistsApi#deleteWebinarPanelist");
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
| **panelistKey** | **Long**| The key of the webinar panelist | |

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

<a id="getPanelists"></a>
# **getPanelists**
> List&lt;Panelist&gt; getPanelists(authorization, organizerKey, webinarKey)

Get webinar panelists

Retrieves all the panelists for a specific webinar.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PanelistsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.getgo.com/G2W/rest");

    PanelistsApi apiInstance = new PanelistsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long organizerKey = 56L; // Long | The key of the organizer
    Long webinarKey = 56L; // Long | The key of the webinar
    try {
      List<Panelist> result = apiInstance.getPanelists(authorization, organizerKey, webinarKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PanelistsApi#getPanelists");
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

[**List&lt;Panelist&gt;**](Panelist.md)

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

<a id="resendPanelistInvitation"></a>
# **resendPanelistInvitation**
> resendPanelistInvitation(authorization, organizerKey, webinarKey, panelistKey)

Resend panelist invitation

Resend the panelist invitation email.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PanelistsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.getgo.com/G2W/rest");

    PanelistsApi apiInstance = new PanelistsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long organizerKey = 56L; // Long | The key of the organizer
    Long webinarKey = 56L; // Long | The key of the webinar
    Long panelistKey = 56L; // Long | The key of the webinar panelist
    try {
      apiInstance.resendPanelistInvitation(authorization, organizerKey, webinarKey, panelistKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling PanelistsApi#resendPanelistInvitation");
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
| **panelistKey** | **Long**| The key of the webinar panelist | |

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
| **204** | Created |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

