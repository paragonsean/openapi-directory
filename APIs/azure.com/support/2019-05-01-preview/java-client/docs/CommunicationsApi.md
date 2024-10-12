# CommunicationsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**communicationsCheckNameAvailability**](CommunicationsApi.md#communicationsCheckNameAvailability) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Support/supportTickets/{supportTicketName}/checkNameAvailability |  |
| [**communicationsCreate**](CommunicationsApi.md#communicationsCreate) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.Support/supportTickets/{supportTicketName}/communications/{communicationName} |  |
| [**communicationsGet**](CommunicationsApi.md#communicationsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Support/supportTickets/{supportTicketName}/communications/{communicationName} |  |
| [**communicationsList**](CommunicationsApi.md#communicationsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Support/supportTickets/{supportTicketName}/communications |  |


<a id="communicationsCheckNameAvailability"></a>
# **communicationsCheckNameAvailability**
> CheckNameAvailabilityOutput communicationsCheckNameAvailability(supportTicketName, subscriptionId, apiVersion, checkNameAvailabilityInput)



Check the availability of a resource name. This API should to be used to check the uniqueness of the name for adding a new communication to the support ticket.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommunicationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CommunicationsApi apiInstance = new CommunicationsApi(defaultClient);
    String supportTicketName = "supportTicketName_example"; // String | Support ticket name
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription id
    String apiVersion = "apiVersion_example"; // String | Api version
    CheckNameAvailabilityInput checkNameAvailabilityInput = new CheckNameAvailabilityInput(); // CheckNameAvailabilityInput | Input to check
    try {
      CheckNameAvailabilityOutput result = apiInstance.communicationsCheckNameAvailability(supportTicketName, subscriptionId, apiVersion, checkNameAvailabilityInput);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommunicationsApi#communicationsCheckNameAvailability");
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
| **checkNameAvailabilityInput** | [**CheckNameAvailabilityInput**](CheckNameAvailabilityInput.md)| Input to check | |

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

<a id="communicationsCreate"></a>
# **communicationsCreate**
> CommunicationDetails communicationsCreate(supportTicketName, communicationName, subscriptionId, apiVersion, createCommunicationParameters)



Adds a new customer communication to an Azure support ticket. Adding attachments are not currently supported via the API. &lt;br/&gt;To add a file to a support ticket, visit the &lt;a target&#x3D;&#39;_blank&#39; href&#x3D;&#39;https://portal.azure.com/#blade/Microsoft_Azure_Support/HelpAndSupportBlade/managesupportrequest&#39;&gt;Manage support ticket&lt;/a&gt; page in the Azure portal, select the support ticket, and use the file upload control to add a new file.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommunicationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CommunicationsApi apiInstance = new CommunicationsApi(defaultClient);
    String supportTicketName = "supportTicketName_example"; // String | Support ticket name
    String communicationName = "communicationName_example"; // String | Communication name
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription id
    String apiVersion = "apiVersion_example"; // String | Api version
    CommunicationDetails createCommunicationParameters = new CommunicationDetails(); // CommunicationDetails | Communication object
    try {
      CommunicationDetails result = apiInstance.communicationsCreate(supportTicketName, communicationName, subscriptionId, apiVersion, createCommunicationParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommunicationsApi#communicationsCreate");
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
| **communicationName** | **String**| Communication name | |
| **subscriptionId** | **String**| Azure subscription id | |
| **apiVersion** | **String**| Api version | |
| **createCommunicationParameters** | [**CommunicationDetails**](CommunicationDetails.md)| Communication object | |

### Return type

[**CommunicationDetails**](CommunicationDetails.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Communication created successfully. |  -  |
| **202** | Accepted, Communication will be created asynchronously |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="communicationsGet"></a>
# **communicationsGet**
> CommunicationDetails communicationsGet(supportTicketName, communicationName, subscriptionId, apiVersion)



Returns details of a specific communication in a support ticket.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommunicationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CommunicationsApi apiInstance = new CommunicationsApi(defaultClient);
    String supportTicketName = "supportTicketName_example"; // String | Support ticket name
    String communicationName = "communicationName_example"; // String | Communication name
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription id
    String apiVersion = "apiVersion_example"; // String | Api version
    try {
      CommunicationDetails result = apiInstance.communicationsGet(supportTicketName, communicationName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommunicationsApi#communicationsGet");
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
| **communicationName** | **String**| Communication name | |
| **subscriptionId** | **String**| Azure subscription id | |
| **apiVersion** | **String**| Api version | |

### Return type

[**CommunicationDetails**](CommunicationDetails.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved communication details. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="communicationsList"></a>
# **communicationsList**
> CommunicationsListResult communicationsList(supportTicketName, subscriptionId, apiVersion, $top, $filter)



Lists all communications (attachments not included) for a support ticket. &lt;br/&gt;&lt;/br&gt; You can also filter support ticket communications by &lt;i&gt;CreatedDate&lt;/i&gt;�or &lt;i&gt;CommunicationType&lt;/i&gt; using the $filter parameter. The only type of communication supported today is &lt;i&gt;Web&lt;/i&gt;. Output will be a paged result with &lt;i&gt;nextLink&lt;/i&gt;, using which you can retrieve the next set of Communication results. &lt;br/&gt;&lt;br/&gt; Support ticket data is available for 12 months after ticket creation. If a ticket was created more than 12 months ago, a request for data might cause an error.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommunicationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CommunicationsApi apiInstance = new CommunicationsApi(defaultClient);
    String supportTicketName = "supportTicketName_example"; // String | Support ticket name
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription id
    String apiVersion = "apiVersion_example"; // String | Api version
    Integer $top = 56; // Integer | The number of values to return in the collection. Default is 10 and max is 10.
    String $filter = "$filter_example"; // String | The filter to apply on the operation. You can filter by communicationType and createdDate properties. CommunicationType supports Equals ('eq') operator and createdDate supports Greater Than ('gt') and Greater Than or Equals ('ge') operators. You may combine the CommunicationType and CreatedDate filters by Logical And ('and') operator.
    try {
      CommunicationsListResult result = apiInstance.communicationsList(supportTicketName, subscriptionId, apiVersion, $top, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommunicationsApi#communicationsList");
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
| **$top** | **Integer**| The number of values to return in the collection. Default is 10 and max is 10. | [optional] |
| **$filter** | **String**| The filter to apply on the operation. You can filter by communicationType and createdDate properties. CommunicationType supports Equals (&#39;eq&#39;) operator and createdDate supports Greater Than (&#39;gt&#39;) and Greater Than or Equals (&#39;ge&#39;) operators. You may combine the CommunicationType and CreatedDate filters by Logical And (&#39;and&#39;) operator. | [optional] |

### Return type

[**CommunicationsListResult**](CommunicationsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved communications for a support ticket. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

