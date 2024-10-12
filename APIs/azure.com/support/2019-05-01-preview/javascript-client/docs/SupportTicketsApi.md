# MicrosoftSupport.SupportTicketsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**supportTicketsCheckNameAvailability**](SupportTicketsApi.md#supportTicketsCheckNameAvailability) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Support/checkNameAvailability | 
[**supportTicketsCreate**](SupportTicketsApi.md#supportTicketsCreate) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.Support/supportTickets/{supportTicketName} | 
[**supportTicketsGet**](SupportTicketsApi.md#supportTicketsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Support/supportTickets/{supportTicketName} | 
[**supportTicketsList**](SupportTicketsApi.md#supportTicketsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Support/supportTickets | 
[**supportTicketsUpdate**](SupportTicketsApi.md#supportTicketsUpdate) | **PATCH** /subscriptions/{subscriptionId}/providers/Microsoft.Support/supportTickets/{supportTicketName} | 



## supportTicketsCheckNameAvailability

> CheckNameAvailabilityOutput supportTicketsCheckNameAvailability(subscriptionId, apiVersion, checkNameAvailabilityInput)



Check the availability of a resource name. This API should to be used to check the uniqueness of the name for support ticket creation for the selected subscription.

### Example

```javascript
import MicrosoftSupport from 'microsoft_support';
let defaultClient = MicrosoftSupport.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftSupport.SupportTicketsApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription id
let apiVersion = "apiVersion_example"; // String | Api version
let checkNameAvailabilityInput = new MicrosoftSupport.CheckNameAvailabilityInput(); // CheckNameAvailabilityInput | Input to check.
apiInstance.supportTicketsCheckNameAvailability(subscriptionId, apiVersion, checkNameAvailabilityInput, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription id | 
 **apiVersion** | **String**| Api version | 
 **checkNameAvailabilityInput** | [**CheckNameAvailabilityInput**](CheckNameAvailabilityInput.md)| Input to check. | 

### Return type

[**CheckNameAvailabilityOutput**](CheckNameAvailabilityOutput.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## supportTicketsCreate

> SupportTicketDetails supportTicketsCreate(supportTicketName, subscriptionId, apiVersion, createSupportTicketParameters)



Creates a new support ticket for Quota increase, Technical, Billing, and Subscription Management issues for the specified subscription. &lt;br/&gt;&lt;br/&gt;A paid technical support plan is required to create a support ticket using this API. &lt;a href&#x3D;&#39;https://aka.ms/supportticketAPI&#39;&gt;Learn more&lt;/a&gt; &lt;br/&gt;&lt;br/&gt; Use the Services API to map the right Service Id to the issue type. For example: For billing tickets set *serviceId* to *&#39;/providers/Microsoft.Support/services/517f2da6-78fd-0498-4e22-ad26996b1dfc&#39;*. &lt;br/&gt; For Technical issues, the Service id will map to the Azure service you want to raise a support ticket for. &lt;br/&gt;&lt;br/&gt;Always call the Services and ProblemClassifications API to get the most recent set of services and problem categories required for support ticket creation.

### Example

```javascript
import MicrosoftSupport from 'microsoft_support';
let defaultClient = MicrosoftSupport.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftSupport.SupportTicketsApi();
let supportTicketName = "supportTicketName_example"; // String | Support ticket name.
let subscriptionId = "subscriptionId_example"; // String | Azure subscription id
let apiVersion = "apiVersion_example"; // String | Api version
let createSupportTicketParameters = new MicrosoftSupport.SupportTicketDetails(); // SupportTicketDetails | Support ticket request payload.
apiInstance.supportTicketsCreate(supportTicketName, subscriptionId, apiVersion, createSupportTicketParameters, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supportTicketName** | **String**| Support ticket name. | 
 **subscriptionId** | **String**| Azure subscription id | 
 **apiVersion** | **String**| Api version | 
 **createSupportTicketParameters** | [**SupportTicketDetails**](SupportTicketDetails.md)| Support ticket request payload. | 

### Return type

[**SupportTicketDetails**](SupportTicketDetails.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## supportTicketsGet

> SupportTicketDetails supportTicketsGet(supportTicketName, subscriptionId, apiVersion)



Gets details for a specific support ticket in an Azure subscription. &lt;br/&gt;&lt;br/&gt;Support ticket data is available for 12 months after ticket creation. If a ticket was created more than 12 months ago, a request for data might cause an error.

### Example

```javascript
import MicrosoftSupport from 'microsoft_support';
let defaultClient = MicrosoftSupport.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftSupport.SupportTicketsApi();
let supportTicketName = "supportTicketName_example"; // String | Support ticket name
let subscriptionId = "subscriptionId_example"; // String | Azure subscription id
let apiVersion = "apiVersion_example"; // String | Api version
apiInstance.supportTicketsGet(supportTicketName, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supportTicketName** | **String**| Support ticket name | 
 **subscriptionId** | **String**| Azure subscription id | 
 **apiVersion** | **String**| Api version | 

### Return type

[**SupportTicketDetails**](SupportTicketDetails.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## supportTicketsList

> SupportTicketsListResult supportTicketsList(subscriptionId, apiVersion, opts)



Lists all the support tickets for an Azure subscription. &lt;br/&gt;&lt;br/&gt;You can also filter the support tickets by &lt;i&gt;Status&lt;/i&gt; or &lt;i&gt;CreatedDate&lt;/i&gt; using the $filter parameter. Output will be a paged result with &lt;i&gt;nextLink&lt;/i&gt;, using which you can retrieve the next set of support tickets. &lt;br/&gt;&lt;br/&gt;Support ticket data is available for 12 months after ticket creation. If a ticket was created more than 12 months ago, a request for data might cause an error.

### Example

```javascript
import MicrosoftSupport from 'microsoft_support';
let defaultClient = MicrosoftSupport.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftSupport.SupportTicketsApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription id
let apiVersion = "apiVersion_example"; // String | Api version
let opts = {
  'top': 56, // Number | The number of values to return in the collection. Default is 25 and max is 100.
  'filter': "filter_example" // String | The filter to apply on the operation. We support 'odata v4.0' filter semantics. <a target='_blank' href='https://docs.microsoft.com/odata/concepts/queryoptions-overview'>Learn more</a> <br/><i>Status</i> filter can only be used with 'eq' operator. For <i>CreatedDate</i> filter, the supported operators are 'gt' and 'ge'. When using both filters, combine them using the logical 'AND'.
};
apiInstance.supportTicketsList(subscriptionId, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure subscription id | 
 **apiVersion** | **String**| Api version | 
 **top** | **Number**| The number of values to return in the collection. Default is 25 and max is 100. | [optional] 
 **filter** | **String**| The filter to apply on the operation. We support &#39;odata v4.0&#39; filter semantics. &lt;a target&#x3D;&#39;_blank&#39; href&#x3D;&#39;https://docs.microsoft.com/odata/concepts/queryoptions-overview&#39;&gt;Learn more&lt;/a&gt; &lt;br/&gt;&lt;i&gt;Status&lt;/i&gt; filter can only be used with &#39;eq&#39; operator. For &lt;i&gt;CreatedDate&lt;/i&gt; filter, the supported operators are &#39;gt&#39; and &#39;ge&#39;. When using both filters, combine them using the logical &#39;AND&#39;. | [optional] 

### Return type

[**SupportTicketsListResult**](SupportTicketsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## supportTicketsUpdate

> SupportTicketDetails supportTicketsUpdate(supportTicketName, subscriptionId, apiVersion, updateSupportTicket)



This API allows you to update the severity level or your contact information in the support ticket. &lt;br/&gt;&lt;br/&gt; Note: The severity levels cannot be changed if a support ticket is actively being worked upon by an Azure support engineer. In such a case, contact your support engineer to request severity update by adding a new communication using the Communications API.

### Example

```javascript
import MicrosoftSupport from 'microsoft_support';
let defaultClient = MicrosoftSupport.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftSupport.SupportTicketsApi();
let supportTicketName = "supportTicketName_example"; // String | Support ticket name
let subscriptionId = "subscriptionId_example"; // String | Azure subscription id
let apiVersion = "apiVersion_example"; // String | Api version
let updateSupportTicket = new MicrosoftSupport.UpdateSupportTicket(); // UpdateSupportTicket | UpdateSupportTicket object
apiInstance.supportTicketsUpdate(supportTicketName, subscriptionId, apiVersion, updateSupportTicket, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supportTicketName** | **String**| Support ticket name | 
 **subscriptionId** | **String**| Azure subscription id | 
 **apiVersion** | **String**| Api version | 
 **updateSupportTicket** | [**UpdateSupportTicket**](UpdateSupportTicket.md)| UpdateSupportTicket object | 

### Return type

[**SupportTicketDetails**](SupportTicketDetails.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

