# AlertsApi

All URIs are relative to *https://connect.signl4.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**alertsAcknowledgeAllPost**](AlertsApi.md#alertsAcknowledgeAllPost) | **POST** /alerts/acknowledgeAll | Confirms all visible alerts |
| [**alertsAcknowledgeMultiplePost**](AlertsApi.md#alertsAcknowledgeMultiplePost) | **POST** /alerts/acknowledgeMultiple | Acknowlegde multiple alerts |
| [**alertsAlertIdAcknowledgePost**](AlertsApi.md#alertsAlertIdAcknowledgePost) | **POST** /alerts/{alertId}/acknowledge | Acknowledge an alert |
| [**alertsAlertIdAnnotatePost**](AlertsApi.md#alertsAlertIdAnnotatePost) | **POST** /alerts/{alertId}/annotate | Annotate Alert |
| [**alertsAlertIdAnnotationsGet**](AlertsApi.md#alertsAlertIdAnnotationsGet) | **GET** /alerts/{alertId}/annotations | Get annotations of an alert |
| [**alertsAlertIdAttachmentsAttachmentIdGet**](AlertsApi.md#alertsAlertIdAttachmentsAttachmentIdGet) | **GET** /alerts/{alertId}/attachments/{attachmentId} | Gets a specified attachment of a specified alert. |
| [**alertsAlertIdAttachmentsGet**](AlertsApi.md#alertsAlertIdAttachmentsGet) | **GET** /alerts/{alertId}/attachments | Get attachments of an alert |
| [**alertsAlertIdClosePost**](AlertsApi.md#alertsAlertIdClosePost) | **POST** /alerts/{alertId}/close | Close an alert |
| [**alertsAlertIdGet**](AlertsApi.md#alertsAlertIdGet) | **GET** /alerts/{alertId} | Get Alert |
| [**alertsAlertIdNotificationsGet**](AlertsApi.md#alertsAlertIdNotificationsGet) | **GET** /alerts/{alertId}/notifications | Get alert notifications |
| [**alertsAlertIdOverviewGet**](AlertsApi.md#alertsAlertIdOverviewGet) | **GET** /alerts/{alertId}/overview | Get an overview alert. |
| [**alertsAlertIdUndoAcknowledgePost**](AlertsApi.md#alertsAlertIdUndoAcknowledgePost) | **POST** /alerts/{alertId}/undoAcknowledge | Undo the acknowledgement of an alert. |
| [**alertsAlertIdUndoClosePost**](AlertsApi.md#alertsAlertIdUndoClosePost) | **POST** /alerts/{alertId}/undoClose | Undo the closure of an alert. |
| [**alertsCloseAllPost**](AlertsApi.md#alertsCloseAllPost) | **POST** /alerts/closeAll | Close all acknowledged alerts. |
| [**alertsCloseMultiplePost**](AlertsApi.md#alertsCloseMultiplePost) | **POST** /alerts/closeMultiple | Close multiple alerts |
| [**alertsPagedPost**](AlertsApi.md#alertsPagedPost) | **POST** /alerts/paged | Gets alerts paged |
| [**alertsPost**](AlertsApi.md#alertsPost) | **POST** /alerts | Trigger Alert |
| [**alertsReportGet**](AlertsApi.md#alertsReportGet) | **GET** /alerts/report | Get Alert Report |
| [**alertsUndoAcknowledgeMultiplePost**](AlertsApi.md#alertsUndoAcknowledgeMultiplePost) | **POST** /alerts/undoAcknowledgeMultiple | Queue undo of multiple acknowledgments. |
| [**alertsUndoCloseMultiplePost**](AlertsApi.md#alertsUndoCloseMultiplePost) | **POST** /alerts/undoCloseMultiple | Withdraw closure of multiple alerts |


<a id="alertsAcknowledgeAllPost"></a>
# **alertsAcknowledgeAllPost**
> alertsAcknowledgeAllPost(userId, changeAlertStatusFilterInfo)

Confirms all visible alerts

This method confirms all unhandled alerts your team currently has by a specific user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AlertsApi apiInstance = new AlertsApi(defaultClient);
    String userId = "userId_example"; // String | User ID of the user to be used to acknowledge the alarms.
    ChangeAlertStatusFilterInfo changeAlertStatusFilterInfo = new ChangeAlertStatusFilterInfo(); // ChangeAlertStatusFilterInfo | 
    try {
      apiInstance.alertsAcknowledgeAllPost(userId, changeAlertStatusFilterInfo);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertsApi#alertsAcknowledgeAllPost");
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
| **userId** | **String**| User ID of the user to be used to acknowledge the alarms. | [optional] |
| **changeAlertStatusFilterInfo** | [**ChangeAlertStatusFilterInfo**](ChangeAlertStatusFilterInfo.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **400** | Required information could not be found in the request/claims. |  -  |
| **404** | Required entities could not be found in the database. |  -  |
| **500** | Internal general error occured. |  -  |

<a id="alertsAcknowledgeMultiplePost"></a>
# **alertsAcknowledgeMultiplePost**
> alertsAcknowledgeMultiplePost(changeAlertStatusMultipleInfo)

Acknowlegde multiple alerts

This method confirms all alerts provided.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AlertsApi apiInstance = new AlertsApi(defaultClient);
    ChangeAlertStatusMultipleInfo changeAlertStatusMultipleInfo = new ChangeAlertStatusMultipleInfo(); // ChangeAlertStatusMultipleInfo | 
    try {
      apiInstance.alertsAcknowledgeMultiplePost(changeAlertStatusMultipleInfo);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertsApi#alertsAcknowledgeMultiplePost");
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
| **changeAlertStatusMultipleInfo** | [**ChangeAlertStatusMultipleInfo**](ChangeAlertStatusMultipleInfo.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **400** | Required information could not be found in the request/claims. |  -  |
| **404** | Not Found |  -  |
| **500** | Internal general error occured. |  -  |

<a id="alertsAlertIdAcknowledgePost"></a>
# **alertsAlertIdAcknowledgePost**
> AlertInfo alertsAlertIdAcknowledgePost(alertId, changeAlertStatusInfo)

Acknowledge an alert

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AlertsApi apiInstance = new AlertsApi(defaultClient);
    String alertId = "alertId_example"; // String | Id to acknowledge an alert.
    ChangeAlertStatusInfo changeAlertStatusInfo = new ChangeAlertStatusInfo(); // ChangeAlertStatusInfo | 
    try {
      AlertInfo result = apiInstance.alertsAlertIdAcknowledgePost(alertId, changeAlertStatusInfo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertsApi#alertsAlertIdAcknowledgePost");
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
| **alertId** | **String**| Id to acknowledge an alert. | |
| **changeAlertStatusInfo** | [**ChangeAlertStatusInfo**](ChangeAlertStatusInfo.md)|  | [optional] |

### Return type

[**AlertInfo**](AlertInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Required information could not be found in the request/claims. |  -  |
| **404** | No alert with id was found. |  -  |
| **409** | Alert can&#39;t be acknowledged because it is against the defined alert lifecycle. |  -  |
| **500** | Internal general error occured. |  -  |

<a id="alertsAlertIdAnnotatePost"></a>
# **alertsAlertIdAnnotatePost**
> AlertAnnotationInfo alertsAlertIdAnnotatePost(alertId, alertAnnotationInfo)

Annotate Alert

Annotates an alert by given Annotation Info.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AlertsApi apiInstance = new AlertsApi(defaultClient);
    String alertId = "alertId_example"; // String | Id of the alert to annotate.
    AlertAnnotationInfo alertAnnotationInfo = new AlertAnnotationInfo(); // AlertAnnotationInfo | Annotation Information.
    try {
      AlertAnnotationInfo result = apiInstance.alertsAlertIdAnnotatePost(alertId, alertAnnotationInfo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertsApi#alertsAlertIdAnnotatePost");
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
| **alertId** | **String**| Id of the alert to annotate. | |
| **alertAnnotationInfo** | [**AlertAnnotationInfo**](AlertAnnotationInfo.md)| Annotation Information. | [optional] |

### Return type

[**AlertAnnotationInfo**](AlertAnnotationInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Required information could not be found in the request/claims. |  -  |
| **404** | Required entities could not be found in the database. |  -  |
| **500** | Internal general error occured. |  -  |

<a id="alertsAlertIdAnnotationsGet"></a>
# **alertsAlertIdAnnotationsGet**
> List&lt;AlertAnnotationInfo&gt; alertsAlertIdAnnotationsGet(alertId)

Get annotations of an alert

Get annotations of an alert by id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AlertsApi apiInstance = new AlertsApi(defaultClient);
    String alertId = "alertId_example"; // String | Id of the requested Alert.
    try {
      List<AlertAnnotationInfo> result = apiInstance.alertsAlertIdAnnotationsGet(alertId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertsApi#alertsAlertIdAnnotationsGet");
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
| **alertId** | **String**| Id of the requested Alert. | |

### Return type

[**List&lt;AlertAnnotationInfo&gt;**](AlertAnnotationInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **204** | No annotations were found for the alert. |  -  |
| **400** | Required information could not be found in the request/claims. |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

<a id="alertsAlertIdAttachmentsAttachmentIdGet"></a>
# **alertsAlertIdAttachmentsAttachmentIdGet**
> File alertsAlertIdAttachmentsAttachmentIdGet(alertId, attachmentId, width, height, scale)

Gets a specified attachment of a specified alert.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AlertsApi apiInstance = new AlertsApi(defaultClient);
    String alertId = "alertId_example"; // String | Id of the alert that contains the wanted attachment.
    String attachmentId = "attachmentId_example"; // String | Id of the attachment, that you want to retrieve.
    Integer width = 56; // Integer | Optional parameter defining the wanted width of the picture that is retrieved.
    Integer height = 56; // Integer | Optional parameter defining the wanted height of the picture that is retrieved.
    Boolean scale = true; // Boolean | Optional parameter defining whether it's wanted to scale the retrieved image. Default is set to  true.
    try {
      File result = apiInstance.alertsAlertIdAttachmentsAttachmentIdGet(alertId, attachmentId, width, height, scale);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertsApi#alertsAlertIdAttachmentsAttachmentIdGet");
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
| **alertId** | **String**| Id of the alert that contains the wanted attachment. | |
| **attachmentId** | **String**| Id of the attachment, that you want to retrieve. | |
| **width** | **Integer**| Optional parameter defining the wanted width of the picture that is retrieved. | [optional] |
| **height** | **Integer**| Optional parameter defining the wanted height of the picture that is retrieved. | [optional] |
| **scale** | **Boolean**| Optional parameter defining whether it&#39;s wanted to scale the retrieved image. Default is set to  true. | [optional] [default to true] |

### Return type

[**File**](File.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the attachment image with additional meta information. |  -  |
| **204** | The image of the attachment was not uploaded yet. |  -  |
| **400** | A passed parameter was either empty or invalid. |  -  |
| **403** | Authorization failed. |  -  |
| **404** | The attachment image was not found. |  -  |
| **500** | Internal general error occured. |  -  |

<a id="alertsAlertIdAttachmentsGet"></a>
# **alertsAlertIdAttachmentsGet**
> List&lt;AlertAttachmentInfo&gt; alertsAlertIdAttachmentsGet(alertId)

Get attachments of an alert

Get attachments of an alert by id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AlertsApi apiInstance = new AlertsApi(defaultClient);
    String alertId = "alertId_example"; // String | Id of the requested Alert.
    try {
      List<AlertAttachmentInfo> result = apiInstance.alertsAlertIdAttachmentsGet(alertId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertsApi#alertsAlertIdAttachmentsGet");
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
| **alertId** | **String**| Id of the requested Alert. | |

### Return type

[**List&lt;AlertAttachmentInfo&gt;**](AlertAttachmentInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Required information could not be found in the request/claims. |  -  |
| **404** | Required entities could not be found in the database. |  -  |
| **500** | Internal general error occured. |  -  |

<a id="alertsAlertIdClosePost"></a>
# **alertsAlertIdClosePost**
> AlertInfo alertsAlertIdClosePost(alertId, changeAlertStatusInfo)

Close an alert

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AlertsApi apiInstance = new AlertsApi(defaultClient);
    String alertId = "alertId_example"; // String | Id to acknowledge an alert.
    ChangeAlertStatusInfo changeAlertStatusInfo = new ChangeAlertStatusInfo(); // ChangeAlertStatusInfo | 
    try {
      AlertInfo result = apiInstance.alertsAlertIdClosePost(alertId, changeAlertStatusInfo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertsApi#alertsAlertIdClosePost");
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
| **alertId** | **String**| Id to acknowledge an alert. | |
| **changeAlertStatusInfo** | [**ChangeAlertStatusInfo**](ChangeAlertStatusInfo.md)|  | [optional] |

### Return type

[**AlertInfo**](AlertInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Required information could not be found in the request/claims. |  -  |
| **404** | No alert with id was found. |  -  |
| **409** | Alert can&#39;t be closed because it is against the defined alert lifecycle. |  -  |
| **500** | Internal general error occured. |  -  |

<a id="alertsAlertIdGet"></a>
# **alertsAlertIdGet**
> AlertInfo alertsAlertIdGet(alertId)

Get Alert

Gets an alert by id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AlertsApi apiInstance = new AlertsApi(defaultClient);
    String alertId = "alertId_example"; // String | Id of the requested Alert.
    try {
      AlertInfo result = apiInstance.alertsAlertIdGet(alertId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertsApi#alertsAlertIdGet");
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
| **alertId** | **String**| Id of the requested Alert. | |

### Return type

[**AlertInfo**](AlertInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Required information could not be found in the request/claims. |  -  |
| **404** | Required entities could not be found in the database. |  -  |
| **500** | Internal general error occured. |  -  |

<a id="alertsAlertIdNotificationsGet"></a>
# **alertsAlertIdNotificationsGet**
> List&lt;AlertNotificationInfo&gt; alertsAlertIdNotificationsGet(alertId)

Get alert notifications

Get notifications of all users by alert id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AlertsApi apiInstance = new AlertsApi(defaultClient);
    String alertId = "alertId_example"; // String | Id of the requested Alert.
    try {
      List<AlertNotificationInfo> result = apiInstance.alertsAlertIdNotificationsGet(alertId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertsApi#alertsAlertIdNotificationsGet");
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
| **alertId** | **String**| Id of the requested Alert. | |

### Return type

[**List&lt;AlertNotificationInfo&gt;**](AlertNotificationInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Required information could not be found in the request/claims. |  -  |
| **404** | Required entities could not be found in the database. |  -  |
| **500** | Internal general error occured. |  -  |

<a id="alertsAlertIdOverviewGet"></a>
# **alertsAlertIdOverviewGet**
> OverviewAlert alertsAlertIdOverviewGet(alertId)

Get an overview alert.

Get overview alert by id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AlertsApi apiInstance = new AlertsApi(defaultClient);
    String alertId = "alertId_example"; // String | Id of the requested Alert.
    try {
      OverviewAlert result = apiInstance.alertsAlertIdOverviewGet(alertId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertsApi#alertsAlertIdOverviewGet");
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
| **alertId** | **String**| Id of the requested Alert. | |

### Return type

[**OverviewAlert**](OverviewAlert.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns alert with all information attached. |  -  |
| **400** | Required information could not be found in the request/claims. |  -  |
| **404** | Required entities could not be found in the database. |  -  |
| **500** | Server Error |  -  |

<a id="alertsAlertIdUndoAcknowledgePost"></a>
# **alertsAlertIdUndoAcknowledgePost**
> OverviewAlert alertsAlertIdUndoAcknowledgePost(alertId, changeAlertStatusInfo)

Undo the acknowledgement of an alert.

This method tries to undo an alert acknowledgement.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AlertsApi apiInstance = new AlertsApi(defaultClient);
    String alertId = "alertId_example"; // String | 
    ChangeAlertStatusInfo changeAlertStatusInfo = new ChangeAlertStatusInfo(); // ChangeAlertStatusInfo | 
    try {
      OverviewAlert result = apiInstance.alertsAlertIdUndoAcknowledgePost(alertId, changeAlertStatusInfo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertsApi#alertsAlertIdUndoAcknowledgePost");
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
| **alertId** | **String**|  | |
| **changeAlertStatusInfo** | [**ChangeAlertStatusInfo**](ChangeAlertStatusInfo.md)|  | [optional] |

### Return type

[**OverviewAlert**](OverviewAlert.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns updated alert. |  -  |
| **400** | Required information could not be found in the request/claims. |  -  |
| **403** | User is not allowed to undo the acknowledgement. |  -  |
| **500** | Internal general error occured. |  -  |

<a id="alertsAlertIdUndoClosePost"></a>
# **alertsAlertIdUndoClosePost**
> OverviewAlert alertsAlertIdUndoClosePost(alertId, changeAlertStatusInfo)

Undo the closure of an alert.

This method tries to undo an alert close.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AlertsApi apiInstance = new AlertsApi(defaultClient);
    String alertId = "alertId_example"; // String | 
    ChangeAlertStatusInfo changeAlertStatusInfo = new ChangeAlertStatusInfo(); // ChangeAlertStatusInfo | 
    try {
      OverviewAlert result = apiInstance.alertsAlertIdUndoClosePost(alertId, changeAlertStatusInfo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertsApi#alertsAlertIdUndoClosePost");
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
| **alertId** | **String**|  | |
| **changeAlertStatusInfo** | [**ChangeAlertStatusInfo**](ChangeAlertStatusInfo.md)|  | [optional] |

### Return type

[**OverviewAlert**](OverviewAlert.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Required information could not be found in the request/claims. |  -  |
| **403** | User is not allowed to undo the close. |  -  |
| **500** | Internal general error occured. |  -  |

<a id="alertsCloseAllPost"></a>
# **alertsCloseAllPost**
> alertsCloseAllPost(userId, changeAlertStatusFilterInfo)

Close all acknowledged alerts.

This method closes all acknowledged alerts your team currently has.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AlertsApi apiInstance = new AlertsApi(defaultClient);
    String userId = "userId_example"; // String | User ID of the user to be used to close the alarms.
    ChangeAlertStatusFilterInfo changeAlertStatusFilterInfo = new ChangeAlertStatusFilterInfo(); // ChangeAlertStatusFilterInfo | 
    try {
      apiInstance.alertsCloseAllPost(userId, changeAlertStatusFilterInfo);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertsApi#alertsCloseAllPost");
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
| **userId** | **String**| User ID of the user to be used to close the alarms. | [optional] |
| **changeAlertStatusFilterInfo** | [**ChangeAlertStatusFilterInfo**](ChangeAlertStatusFilterInfo.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **400** | Required information could not be found in the request/claims. |  -  |
| **404** | Required entities could not be found in the database. |  -  |
| **500** | Internal general error occured. |  -  |

<a id="alertsCloseMultiplePost"></a>
# **alertsCloseMultiplePost**
> alertsCloseMultiplePost(changeAlertStatusMultipleInfo)

Close multiple alerts

This method closes all alerts provided.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AlertsApi apiInstance = new AlertsApi(defaultClient);
    ChangeAlertStatusMultipleInfo changeAlertStatusMultipleInfo = new ChangeAlertStatusMultipleInfo(); // ChangeAlertStatusMultipleInfo | 
    try {
      apiInstance.alertsCloseMultiplePost(changeAlertStatusMultipleInfo);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertsApi#alertsCloseMultiplePost");
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
| **changeAlertStatusMultipleInfo** | [**ChangeAlertStatusMultipleInfo**](ChangeAlertStatusMultipleInfo.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **400** | Required information could not be found in the request/claims. |  -  |
| **404** | Not Found |  -  |
| **500** | Internal general error occured. |  -  |

<a id="alertsPagedPost"></a>
# **alertsPagedPost**
> OverviewAlertPagedResultsPublic alertsPagedPost(maxResults, userId, alertFilterPublic)

Gets alerts paged

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AlertsApi apiInstance = new AlertsApi(defaultClient);
    Integer maxResults = 56; // Integer | Defines the limit of retrieved alert details per request. 1 to 100 are allowed per request.                  Number of alerts could be less if filtered but at least 1.
    String userId = "userId_example"; // String | User ID of the user you want to get alerts for.
    AlertFilterPublic alertFilterPublic = new AlertFilterPublic(); // AlertFilterPublic | The filter defines which alerts are supposed to be retrieved.
    try {
      OverviewAlertPagedResultsPublic result = apiInstance.alertsPagedPost(maxResults, userId, alertFilterPublic);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertsApi#alertsPagedPost");
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
| **maxResults** | **Integer**| Defines the limit of retrieved alert details per request. 1 to 100 are allowed per request.                  Number of alerts could be less if filtered but at least 1. | [optional] |
| **userId** | **String**| User ID of the user you want to get alerts for. | [optional] |
| **alertFilterPublic** | [**AlertFilterPublic**](AlertFilterPublic.md)| The filter defines which alerts are supposed to be retrieved. | [optional] |

### Return type

[**OverviewAlertPagedResultsPublic**](OverviewAlertPagedResultsPublic.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a paged result with found alerts and continuation token if more alerts are in the database. |  -  |
| **204** | There were no alerts found for the specified filter. |  -  |
| **400** | Required parameters could not be found in the request/claims. |  -  |
| **403** | Authorization failed |  -  |
| **404** | Not Found |  -  |
| **500** | Internal general error occured. |  -  |

<a id="alertsPost"></a>
# **alertsPost**
> AlertInfo alertsPost(raiseAlertInfo)

Trigger Alert

Triggers a new alert for your team. All team members on duty will receive alert notifications.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AlertsApi apiInstance = new AlertsApi(defaultClient);
    RaiseAlertInfo raiseAlertInfo = new RaiseAlertInfo(); // RaiseAlertInfo | Alert to raise.
    try {
      AlertInfo result = apiInstance.alertsPost(raiseAlertInfo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertsApi#alertsPost");
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
| **raiseAlertInfo** | [**RaiseAlertInfo**](RaiseAlertInfo.md)| Alert to raise. | [optional] |

### Return type

[**AlertInfo**](AlertInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **400** | Required information could not be found in the request/claims. |  -  |
| **404** | Required entities could not be found in the database. |  -  |
| **500** | Internal general error occured. |  -  |

<a id="alertsReportGet"></a>
# **alertsReportGet**
> AlertReport alertsReportGet(userId)

Get Alert Report

Returns information about the occurred alert volume in different time periods as well as information about the  response behaviour (amount of confirmed and unhandled alerts) of your team members.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AlertsApi apiInstance = new AlertsApi(defaultClient);
    String userId = "userId_example"; // String | User ID of the user for whom you want a report.
    try {
      AlertReport result = apiInstance.alertsReportGet(userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertsApi#alertsReportGet");
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
| **userId** | **String**| User ID of the user for whom you want a report. | [optional] |

### Return type

[**AlertReport**](AlertReport.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Required information could not be found in the request/claims. |  -  |
| **404** | Required entities could not be found in the database. |  -  |
| **500** | Internal general error occured. |  -  |

<a id="alertsUndoAcknowledgeMultiplePost"></a>
# **alertsUndoAcknowledgeMultiplePost**
> alertsUndoAcknowledgeMultiplePost(changeAlertStatusMultipleInfo)

Queue undo of multiple acknowledgments.

This method tries to undo the acknowledgement of multiple alerts via a queue. The operation is handled in the background.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AlertsApi apiInstance = new AlertsApi(defaultClient);
    ChangeAlertStatusMultipleInfo changeAlertStatusMultipleInfo = new ChangeAlertStatusMultipleInfo(); // ChangeAlertStatusMultipleInfo | Configure which user should be undone for which alerts.
    try {
      apiInstance.alertsUndoAcknowledgeMultiplePost(changeAlertStatusMultipleInfo);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertsApi#alertsUndoAcknowledgeMultiplePost");
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
| **changeAlertStatusMultipleInfo** | [**ChangeAlertStatusMultipleInfo**](ChangeAlertStatusMultipleInfo.md)| Configure which user should be undone for which alerts. | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **400** | Required information could not be found in the request/claims. |  -  |
| **403** | Forbidden |  -  |
| **500** | Internal general error occured. |  -  |

<a id="alertsUndoCloseMultiplePost"></a>
# **alertsUndoCloseMultiplePost**
> alertsUndoCloseMultiplePost(changeAlertStatusMultipleInfo)

Withdraw closure of multiple alerts

This method tries to undo multiple alert closes. The operation is handled in the background.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AlertsApi apiInstance = new AlertsApi(defaultClient);
    ChangeAlertStatusMultipleInfo changeAlertStatusMultipleInfo = new ChangeAlertStatusMultipleInfo(); // ChangeAlertStatusMultipleInfo | 
    try {
      apiInstance.alertsUndoCloseMultiplePost(changeAlertStatusMultipleInfo);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertsApi#alertsUndoCloseMultiplePost");
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
| **changeAlertStatusMultipleInfo** | [**ChangeAlertStatusMultipleInfo**](ChangeAlertStatusMultipleInfo.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **400** | Required information could not be found in the request/claims. |  -  |
| **404** | Not Found |  -  |
| **500** | Internal general error occured. |  -  |

