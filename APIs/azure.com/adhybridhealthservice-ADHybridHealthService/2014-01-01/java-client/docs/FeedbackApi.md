# FeedbackApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**servicesAddAlertFeedback**](FeedbackApi.md#servicesAddAlertFeedback) | **POST** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/feedbacktype/alerts/feedback |  |
| [**servicesListAlertFeedback**](FeedbackApi.md#servicesListAlertFeedback) | **GET** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/feedbacktype/alerts/{shortName}/alertfeedback |  |


<a id="servicesAddAlertFeedback"></a>
# **servicesAddAlertFeedback**
> AlertFeedback servicesAddAlertFeedback(serviceName, apiVersion, alertFeedback)



Adds an alert feedback submitted by customer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeedbackApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    FeedbackApi apiInstance = new FeedbackApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service.
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    AlertFeedback alertFeedback = new AlertFeedback(); // AlertFeedback | The alert feedback.
    try {
      AlertFeedback result = apiInstance.servicesAddAlertFeedback(serviceName, apiVersion, alertFeedback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeedbackApi#servicesAddAlertFeedback");
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
| **serviceName** | **String**| The name of the service. | |
| **apiVersion** | **String**| The version of the API to be used with the client request. | |
| **alertFeedback** | [**AlertFeedback**](AlertFeedback.md)| The alert feedback. | |

### Return type

[**AlertFeedback**](AlertFeedback.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully added alert feedback. |  -  |

<a id="servicesListAlertFeedback"></a>
# **servicesListAlertFeedback**
> AlertFeedbacks servicesListAlertFeedback(serviceName, shortName, apiVersion)



Gets a list of all alert feedback for a given tenant and alert type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeedbackApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    FeedbackApi apiInstance = new FeedbackApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service.
    String shortName = "shortName_example"; // String | The name of the alert.
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    try {
      AlertFeedbacks result = apiInstance.servicesListAlertFeedback(serviceName, shortName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeedbackApi#servicesListAlertFeedback");
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
| **serviceName** | **String**| The name of the service. | |
| **shortName** | **String**| The name of the alert. | |
| **apiVersion** | **String**| The version of the API to be used with the client request. | |

### Return type

[**AlertFeedbacks**](AlertFeedbacks.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of alert feedback. |  -  |

