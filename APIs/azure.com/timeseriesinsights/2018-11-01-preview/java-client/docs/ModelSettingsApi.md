# ModelSettingsApi

All URIs are relative to *https://azure.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**modelSettingsGet**](ModelSettingsApi.md#modelSettingsGet) | **GET** /timeseries/modelSettings |  |
| [**modelSettingsUpdate**](ModelSettingsApi.md#modelSettingsUpdate) | **PATCH** /timeseries/modelSettings |  |


<a id="modelSettingsGet"></a>
# **modelSettingsGet**
> ModelSettingsResponse modelSettingsGet(apiVersion, xMsClientRequestId, xMsClientSessionId)



Returns the model settings which includes model display name, Time Series ID properties and default type ID. Every pay-as-you-go environment has a model that is automatically created.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ModelSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ModelSettingsApi apiInstance = new ModelSettingsApi(defaultClient);
    String apiVersion = "2018-11-01-preview"; // String | Version of the API to be used with the client request. Currently supported version is \"2018-11-01-preview\".
    String xMsClientRequestId = "xMsClientRequestId_example"; // String | Optional client request ID. Service records this value. Allows the service to trace operation across services, and allows the customer to contact support regarding a particular request.
    String xMsClientSessionId = "xMsClientSessionId_example"; // String | Optional client session ID. Service records this value. Allows the service to trace a group of related operations across services, and allows the customer to contact support regarding a particular group of requests.
    try {
      ModelSettingsResponse result = apiInstance.modelSettingsGet(apiVersion, xMsClientRequestId, xMsClientSessionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ModelSettingsApi#modelSettingsGet");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. Currently supported version is \&quot;2018-11-01-preview\&quot;. | [default to 2018-11-01-preview] |
| **xMsClientRequestId** | **String**| Optional client request ID. Service records this value. Allows the service to trace operation across services, and allows the customer to contact support regarding a particular request. | [optional] |
| **xMsClientSessionId** | **String**| Optional client session ID. Service records this value. Allows the service to trace a group of related operations across services, and allows the customer to contact support regarding a particular group of requests. | [optional] |

### Return type

[**ModelSettingsResponse**](ModelSettingsResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation. |  * x-ms-request-id - Server-generated request ID. Can be used to contact support to investigate a request. <br>  |
| **0** | Unexpected error. |  * x-ms-request-id - Server-generated request ID. Can be used to contact support to investigate a request. <br>  |

<a id="modelSettingsUpdate"></a>
# **modelSettingsUpdate**
> ModelSettingsResponse modelSettingsUpdate(apiVersion, parameters, xMsClientRequestId, xMsClientSessionId)



Updates time series model settings - either the model name or default type ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ModelSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ModelSettingsApi apiInstance = new ModelSettingsApi(defaultClient);
    String apiVersion = "2018-11-01-preview"; // String | Version of the API to be used with the client request. Currently supported version is \"2018-11-01-preview\".
    UpdateModelSettingsRequest parameters = new UpdateModelSettingsRequest(); // UpdateModelSettingsRequest | Model settings update request body.
    String xMsClientRequestId = "xMsClientRequestId_example"; // String | Optional client request ID. Service records this value. Allows the service to trace operation across services, and allows the customer to contact support regarding a particular request.
    String xMsClientSessionId = "xMsClientSessionId_example"; // String | Optional client session ID. Service records this value. Allows the service to trace a group of related operations across services, and allows the customer to contact support regarding a particular group of requests.
    try {
      ModelSettingsResponse result = apiInstance.modelSettingsUpdate(apiVersion, parameters, xMsClientRequestId, xMsClientSessionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ModelSettingsApi#modelSettingsUpdate");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. Currently supported version is \&quot;2018-11-01-preview\&quot;. | [default to 2018-11-01-preview] |
| **parameters** | [**UpdateModelSettingsRequest**](UpdateModelSettingsRequest.md)| Model settings update request body. | |
| **xMsClientRequestId** | **String**| Optional client request ID. Service records this value. Allows the service to trace operation across services, and allows the customer to contact support regarding a particular request. | [optional] |
| **xMsClientSessionId** | **String**| Optional client session ID. Service records this value. Allows the service to trace a group of related operations across services, and allows the customer to contact support regarding a particular group of requests. | [optional] |

### Return type

[**ModelSettingsResponse**](ModelSettingsResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation returns new full model settings. |  * x-ms-request-id - Server-generated request ID. Can be used to contact support to investigate a request. <br>  |
| **0** | Unexpected error. |  * x-ms-request-id - Server-generated request ID. Can be used to contact support to investigate a request. <br>  |

