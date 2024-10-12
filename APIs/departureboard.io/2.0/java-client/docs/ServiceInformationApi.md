# ServiceInformationApi

All URIs are relative to *https://api.departureboard.io/api/v2.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getServiceDetailsByID**](ServiceInformationApi.md#getServiceDetailsByID) | **GET** /getServiceDetailsByID/{serviceID} | getServiceDetailsByID is used to get information on a service, by the Service ID. This will typically return a train service, but will also return a bus and ferry services. The Service ID must be provided in the serviceIDUrlSafe format that is provided in the response for Arrival and Departure Boards. A service ID is specific to a station, and can only be looked up for a short time after a train/bus/ferry arrives at, or departs from a station. This is a National Rail limitation. |


<a id="getServiceDetailsByID"></a>
# **getServiceDetailsByID**
> getServiceDetailsByID(serviceID, apiKey)

getServiceDetailsByID is used to get information on a service, by the Service ID. This will typically return a train service, but will also return a bus and ferry services. The Service ID must be provided in the serviceIDUrlSafe format that is provided in the response for Arrival and Departure Boards. A service ID is specific to a station, and can only be looked up for a short time after a train/bus/ferry arrives at, or departs from a station. This is a National Rail limitation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceInformationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.departureboard.io/api/v2.0");

    ServiceInformationApi apiInstance = new ServiceInformationApi(defaultClient);
    String serviceID = "serviceID_example"; // String | The Service ID for the Train Service you wish to look up in the URL Safe format. For example \"qsec4O8LW7k8ITcOt_ir4Q--\".
    String apiKey = "apiKey_example"; // String | The National Rail OpenLDBWS API Key to use for looking up service information. You must register with National Rail to obtain this key and whitelist it with us. See https://api.departureboard.io/docs/registration for more information.
    try {
      apiInstance.getServiceDetailsByID(serviceID, apiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceInformationApi#getServiceDetailsByID");
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
| **serviceID** | **String**| The Service ID for the Train Service you wish to look up in the URL Safe format. For example \&quot;qsec4O8LW7k8ITcOt_ir4Q--\&quot;. | |
| **apiKey** | **String**| The National Rail OpenLDBWS API Key to use for looking up service information. You must register with National Rail to obtain this key and whitelist it with us. See https://api.departureboard.io/docs/registration for more information. | |

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
| **200** | **OK**: The API Request was successful and returned data. |  -  |
| **400** | Your request was not valid. &lt;br&gt;&lt;br&gt;The departureboard.io API performs validation of queries to make sure they make sense and will return a valid response from National Rail. Bad queries made directly to the National Rail API return a generic &#x60;500 Internal Server Error&#x60; response which is difficult to troubleshoot.&lt;br&gt;&lt;br&gt;By validating requests the departureboard.io API can provide improved error messages to help with troubleshooting, and prevent bad queries from ever reaching National Rail. |  -  |
| **401** | **Unauthorized**: Your National Rail API key is wrong or your key has not been registered in the [departureboard.io API Portal](https://api-portal.departureboard.io) as detailed in the [registration](https://api.departureboard.io/docs/registration) section of the documentation.&lt;br&gt;&lt;br&gt;You should double check your API Key is valid and has been whitelisted. Newly generated API Keys can take up to 15 minutes to become active. |  -  |
| **429** | **Too Many Requests**: You have exceeded the rate limit. &lt;br&gt;&lt;br&gt;Get in touch to arrange an exception, or slow down your requests. |  -  |
| **500** | **Internal Server Error**: There was an unknown error returning the response.&lt;br&gt;&lt;br&gt;This error is served when an unknown error is encountered returning your response. This is often due to upstream problems with National Rail, for example them returning a bad response or malformed data. In rare circumstances it can be caused by a bad request that was not caught in the departureboard.io validation. |  -  |
| **503** | **Service Unavailable**: The National Rail upstream API is experiencing issues.&lt;br&gt;&lt;br&gt;This error is returned when the departureboard.io API detects issues with the upstream National Rail API. The departureboard.io API is functioning but cannot return a result as the National Rail API is down. |  -  |

