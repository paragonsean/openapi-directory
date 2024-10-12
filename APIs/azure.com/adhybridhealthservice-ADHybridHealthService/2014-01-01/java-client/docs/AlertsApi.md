# AlertsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**serviceMembersListAlerts**](AlertsApi.md#serviceMembersListAlerts) | **GET** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/servicemembers/{serviceMemberId}/alerts |  |
| [**servicesListAlerts**](AlertsApi.md#servicesListAlerts) | **GET** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/alerts |  |


<a id="serviceMembersListAlerts"></a>
# **serviceMembersListAlerts**
> Alerts serviceMembersListAlerts(serviceMemberId, serviceName, apiVersion, $filter, state, from, to)



Gets the details of an alert for a given service and server combination.

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
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AlertsApi apiInstance = new AlertsApi(defaultClient);
    UUID serviceMemberId = UUID.randomUUID(); // UUID | The server Id for which the alert details needs to be queried.
    String serviceName = "serviceName_example"; // String | The name of the service.
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    String $filter = "$filter_example"; // String | The alert property filter to apply.
    String state = "state_example"; // String | The alert state to query for.
    OffsetDateTime from = OffsetDateTime.now(); // OffsetDateTime | The start date to query for.
    OffsetDateTime to = OffsetDateTime.now(); // OffsetDateTime | The end date till when to query for.
    try {
      Alerts result = apiInstance.serviceMembersListAlerts(serviceMemberId, serviceName, apiVersion, $filter, state, from, to);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertsApi#serviceMembersListAlerts");
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
| **serviceMemberId** | **UUID**| The server Id for which the alert details needs to be queried. | |
| **serviceName** | **String**| The name of the service. | |
| **apiVersion** | **String**| The version of the API to be used with the client request. | |
| **$filter** | **String**| The alert property filter to apply. | [optional] |
| **state** | **String**| The alert state to query for. | [optional] |
| **from** | **OffsetDateTime**| The start date to query for. | [optional] |
| **to** | **OffsetDateTime**| The end date till when to query for. | [optional] |

### Return type

[**Alerts**](Alerts.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of alerts. |  -  |

<a id="servicesListAlerts"></a>
# **servicesListAlerts**
> Alerts servicesListAlerts(serviceName, apiVersion, $filter, state, from, to)



Gets the alerts for a given service.

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
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AlertsApi apiInstance = new AlertsApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service.
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    String $filter = "$filter_example"; // String | The alert property filter to apply.
    String state = "state_example"; // String | The alert state to query for.
    OffsetDateTime from = OffsetDateTime.now(); // OffsetDateTime | The start date to query for.
    OffsetDateTime to = OffsetDateTime.now(); // OffsetDateTime | The end date till when to query for.
    try {
      Alerts result = apiInstance.servicesListAlerts(serviceName, apiVersion, $filter, state, from, to);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertsApi#servicesListAlerts");
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
| **$filter** | **String**| The alert property filter to apply. | [optional] |
| **state** | **String**| The alert state to query for. | [optional] |
| **from** | **OffsetDateTime**| The start date to query for. | [optional] |
| **to** | **OffsetDateTime**| The end date till when to query for. | [optional] |

### Return type

[**Alerts**](Alerts.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of alerts. |  -  |

