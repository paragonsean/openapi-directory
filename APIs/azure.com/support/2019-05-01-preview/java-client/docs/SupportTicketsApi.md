# SupportTicketsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**supportTicketsCheckNameAvailability**](SupportTicketsApi.md#supportTicketsCheckNameAvailability) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Support/checkNameAvailability |  |
| [**supportTicketsCreate**](SupportTicketsApi.md#supportTicketsCreate) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.Support/supportTickets/{supportTicketName} |  |
| [**supportTicketsGet**](SupportTicketsApi.md#supportTicketsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Support/supportTickets/{supportTicketName} |  |
| [**supportTicketsList**](SupportTicketsApi.md#supportTicketsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Support/supportTickets |  |
| [**supportTicketsUpdate**](SupportTicketsApi.md#supportTicketsUpdate) | **PATCH** /subscriptions/{subscriptionId}/providers/Microsoft.Support/supportTickets/{supportTicketName} |  |


<a id="supportTicketsCheckNameAvailability"></a>
# **supportTicketsCheckNameAvailability**
> CheckNameAvailabilityOutput supportTicketsCheckNameAvailability(subscriptionId, apiVersion, checkNameAvailabilityInput)



Check the availability of a resource name. This API should to be used to check the uniqueness of the name for support ticket creation for the selected subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SupportTicketsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SupportTicketsApi apiInstance = new SupportTicketsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription id
    String apiVersion = "apiVersion_example"; // String | Api version
    CheckNameAvailabilityInput checkNameAvailabilityInput = new CheckNameAvailabilityInput(); // CheckNameAvailabilityInput | Input to check.
    try {
      CheckNameAvailabilityOutput result = apiInstance.supportTicketsCheckNameAvailability(subscriptionId, apiVersion, checkNameAvailabilityInput);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SupportTicketsApi#supportTicketsCheckNameAvailability");
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
| **subscriptionId** | **String**| Azure subscription id | |
| **apiVersion** | **String**| Api version | |
| **checkNameAvailabilityInput** | [**CheckNameAvailabilityInput**](CheckNameAvailabilityInput.md)| Input to check. | |

### Return type

[**CheckNameAvailabilityOutput**](CheckNameAvailabilityOutput.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="supportTicketsCreate"></a>
# **supportTicketsCreate**
> SupportTicketDetails supportTicketsCreate(supportTicketName, subscriptionId, apiVersion, createSupportTicketParameters)



Creates a new support ticket for Quota increase, Technical, Billing, and Subscription Management issues for the specified subscription. &lt;br/&gt;&lt;br/&gt;A paid technical support plan is required to create a support ticket using this API. &lt;a href&#x3D;&#39;https://aka.ms/supportticketAPI&#39;&gt;Learn more&lt;/a&gt; &lt;br/&gt;&lt;br/&gt; Use the Services API to map the right Service Id to the issue type. For example: For billing tickets set *serviceId* to *&#39;/providers/Microsoft.Support/services/517f2da6-78fd-0498-4e22-ad26996b1dfc&#39;*. &lt;br/&gt; For Technical issues, the Service id will map to the Azure service you want to raise a support ticket for. &lt;br/&gt;&lt;br/&gt;Always call the Services and ProblemClassifications API to get the most recent set of services and problem categories required for support ticket creation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SupportTicketsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SupportTicketsApi apiInstance = new SupportTicketsApi(defaultClient);
    String supportTicketName = "supportTicketName_example"; // String | Support ticket name.
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription id
    String apiVersion = "apiVersion_example"; // String | Api version
    SupportTicketDetails createSupportTicketParameters = new SupportTicketDetails(); // SupportTicketDetails | Support ticket request payload.
    try {
      SupportTicketDetails result = apiInstance.supportTicketsCreate(supportTicketName, subscriptionId, apiVersion, createSupportTicketParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SupportTicketsApi#supportTicketsCreate");
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
| **supportTicketName** | **String**| Support ticket name. | |
| **subscriptionId** | **String**| Azure subscription id | |
| **apiVersion** | **String**| Api version | |
| **createSupportTicketParameters** | [**SupportTicketDetails**](SupportTicketDetails.md)| Support ticket request payload. | |

### Return type

[**SupportTicketDetails**](SupportTicketDetails.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - SupportTicket created successfully |  -  |
| **202** | Accepted, SupportTicket will be created asynchronously |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="supportTicketsGet"></a>
# **supportTicketsGet**
> SupportTicketDetails supportTicketsGet(supportTicketName, subscriptionId, apiVersion)



Gets details for a specific support ticket in an Azure subscription. &lt;br/&gt;&lt;br/&gt;Support ticket data is available for 12 months after ticket creation. If a ticket was created more than 12 months ago, a request for data might cause an error.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SupportTicketsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SupportTicketsApi apiInstance = new SupportTicketsApi(defaultClient);
    String supportTicketName = "supportTicketName_example"; // String | Support ticket name
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription id
    String apiVersion = "apiVersion_example"; // String | Api version
    try {
      SupportTicketDetails result = apiInstance.supportTicketsGet(supportTicketName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SupportTicketsApi#supportTicketsGet");
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
| **supportTicketName** | **String**| Support ticket name | |
| **subscriptionId** | **String**| Azure subscription id | |
| **apiVersion** | **String**| Api version | |

### Return type

[**SupportTicketDetails**](SupportTicketDetails.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved support ticket. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="supportTicketsList"></a>
# **supportTicketsList**
> SupportTicketsListResult supportTicketsList(subscriptionId, apiVersion, $top, $filter)



Lists all the support tickets for an Azure subscription. &lt;br/&gt;&lt;br/&gt;You can also filter the support tickets by &lt;i&gt;Status&lt;/i&gt; or &lt;i&gt;CreatedDate&lt;/i&gt; using the $filter parameter. Output will be a paged result with &lt;i&gt;nextLink&lt;/i&gt;, using which you can retrieve the next set of support tickets. &lt;br/&gt;&lt;br/&gt;Support ticket data is available for 12 months after ticket creation. If a ticket was created more than 12 months ago, a request for data might cause an error.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SupportTicketsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SupportTicketsApi apiInstance = new SupportTicketsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription id
    String apiVersion = "apiVersion_example"; // String | Api version
    Integer $top = 56; // Integer | The number of values to return in the collection. Default is 25 and max is 100.
    String $filter = "$filter_example"; // String | The filter to apply on the operation. We support 'odata v4.0' filter semantics. <a target='_blank' href='https://docs.microsoft.com/odata/concepts/queryoptions-overview'>Learn more</a> <br/><i>Status</i> filter can only be used with 'eq' operator. For <i>CreatedDate</i> filter, the supported operators are 'gt' and 'ge'. When using both filters, combine them using the logical 'AND'.
    try {
      SupportTicketsListResult result = apiInstance.supportTicketsList(subscriptionId, apiVersion, $top, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SupportTicketsApi#supportTicketsList");
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
| **subscriptionId** | **String**| Azure subscription id | |
| **apiVersion** | **String**| Api version | |
| **$top** | **Integer**| The number of values to return in the collection. Default is 25 and max is 100. | [optional] |
| **$filter** | **String**| The filter to apply on the operation. We support &#39;odata v4.0&#39; filter semantics. &lt;a target&#x3D;&#39;_blank&#39; href&#x3D;&#39;https://docs.microsoft.com/odata/concepts/queryoptions-overview&#39;&gt;Learn more&lt;/a&gt; &lt;br/&gt;&lt;i&gt;Status&lt;/i&gt; filter can only be used with &#39;eq&#39; operator. For &lt;i&gt;CreatedDate&lt;/i&gt; filter, the supported operators are &#39;gt&#39; and &#39;ge&#39;. When using both filters, combine them using the logical &#39;AND&#39;. | [optional] |

### Return type

[**SupportTicketsListResult**](SupportTicketsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved support tickets. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="supportTicketsUpdate"></a>
# **supportTicketsUpdate**
> SupportTicketDetails supportTicketsUpdate(supportTicketName, subscriptionId, apiVersion, updateSupportTicket)



This API allows you to update the severity level or your contact information in the support ticket. &lt;br/&gt;&lt;br/&gt; Note: The severity levels cannot be changed if a support ticket is actively being worked upon by an Azure support engineer. In such a case, contact your support engineer to request severity update by adding a new communication using the Communications API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SupportTicketsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SupportTicketsApi apiInstance = new SupportTicketsApi(defaultClient);
    String supportTicketName = "supportTicketName_example"; // String | Support ticket name
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription id
    String apiVersion = "apiVersion_example"; // String | Api version
    UpdateSupportTicket updateSupportTicket = new UpdateSupportTicket(); // UpdateSupportTicket | UpdateSupportTicket object
    try {
      SupportTicketDetails result = apiInstance.supportTicketsUpdate(supportTicketName, subscriptionId, apiVersion, updateSupportTicket);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SupportTicketsApi#supportTicketsUpdate");
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
| **supportTicketName** | **String**| Support ticket name | |
| **subscriptionId** | **String**| Azure subscription id | |
| **apiVersion** | **String**| Api version | |
| **updateSupportTicket** | [**UpdateSupportTicket**](UpdateSupportTicket.md)| UpdateSupportTicket object | |

### Return type

[**SupportTicketDetails**](SupportTicketDetails.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated support ticket. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

