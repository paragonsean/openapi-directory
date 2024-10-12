# ServicesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**servicesGet**](ServicesApi.md#servicesGet) | **GET** /providers/Microsoft.Support/services/{serviceName} |  |
| [**servicesList**](ServicesApi.md#servicesList) | **GET** /providers/Microsoft.Support/services |  |


<a id="servicesGet"></a>
# **servicesGet**
> Service servicesGet(serviceName, apiVersion)



Gets a specific Azure service for support ticket creation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServicesApi apiInstance = new ServicesApi(defaultClient);
    String serviceName = "serviceName_example"; // String | Name of Azure service
    String apiVersion = "apiVersion_example"; // String | Api version
    try {
      Service result = apiInstance.servicesGet(serviceName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicesApi#servicesGet");
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
| **serviceName** | **String**| Name of Azure service | |
| **apiVersion** | **String**| Api version | |

### Return type

[**Service**](Service.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved Azure service for support ticket creation. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="servicesList"></a>
# **servicesList**
> ServicesListResult servicesList(apiVersion)



Lists all the Azure services available for support ticket creation. Here are the Service Ids for **Billing**, **Subscription Management**, and **Service and subscription limits (Quotas)** issues: &lt;br/&gt;&lt;table&gt;&lt;tr&gt;&lt;td&gt;&lt;u&gt;Issue type&lt;/u&gt;&lt;/td&gt;&lt;td&gt;&lt;u&gt;Service Id&lt;/u&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Billing&lt;/td&gt;&lt;td&gt;&#39;/providers/Microsoft.Support/services/517f2da6-78fd-0498-4e22-ad26996b1dfc&#39;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Subscription Management&lt;/td&gt;&lt;td&gt;&#39;/providers/Microsoft.Support/services/f3dc5421-79ef-1efa-41a5-42bf3cbb52c6&#39;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Quota&lt;/td&gt;&lt;td&gt;&#39;/providers/Microsoft.Support/services/06bfd9d3-516b-d5c6-5802-169c800dec89&#39;&lt;/td&gt;&lt;/tr&gt;&lt;/table&gt; &lt;br/&gt;&lt;br/&gt; For **Technical** issues, select the Service Id that maps to the Azure service/product as displayed in the **Services** drop-down list on the Azure portal&#39;s &lt;a target&#x3D;&#39;_blank&#39; href&#x3D;&#39;https://portal.azure.com/#blade/Microsoft_Azure_Support/HelpAndSupportBlade/overview&#39;&gt;New support request&lt;/a&gt; page. &lt;br/&gt;&lt;br/&gt; Always use the service and it&#39;s corresponding problem classification(s) obtained programmatically for support ticket creation. This practice ensures that you always have the most recent set of service and problem classification Ids.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServicesApi apiInstance = new ServicesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Api version
    try {
      ServicesListResult result = apiInstance.servicesList(apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicesApi#servicesList");
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
| **apiVersion** | **String**| Api version | |

### Return type

[**ServicesListResult**](ServicesListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved list of Azure services available for support. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

