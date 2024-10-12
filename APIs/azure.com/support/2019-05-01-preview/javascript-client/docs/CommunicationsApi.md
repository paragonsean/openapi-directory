# MicrosoftSupport.CommunicationsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**communicationsCheckNameAvailability**](CommunicationsApi.md#communicationsCheckNameAvailability) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Support/supportTickets/{supportTicketName}/checkNameAvailability | 
[**communicationsCreate**](CommunicationsApi.md#communicationsCreate) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.Support/supportTickets/{supportTicketName}/communications/{communicationName} | 
[**communicationsGet**](CommunicationsApi.md#communicationsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Support/supportTickets/{supportTicketName}/communications/{communicationName} | 
[**communicationsList**](CommunicationsApi.md#communicationsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Support/supportTickets/{supportTicketName}/communications | 



## communicationsCheckNameAvailability

> CheckNameAvailabilityOutput communicationsCheckNameAvailability(supportTicketName, subscriptionId, apiVersion, checkNameAvailabilityInput)



Check the availability of a resource name. This API should to be used to check the uniqueness of the name for adding a new communication to the support ticket.

### Example

```javascript
import MicrosoftSupport from 'microsoft_support';
let defaultClient = MicrosoftSupport.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftSupport.CommunicationsApi();
let supportTicketName = "supportTicketName_example"; // String | Support ticket name
let subscriptionId = "subscriptionId_example"; // String | Azure subscription id
let apiVersion = "apiVersion_example"; // String | Api version
let checkNameAvailabilityInput = new MicrosoftSupport.CheckNameAvailabilityInput(); // CheckNameAvailabilityInput | Input to check
apiInstance.communicationsCheckNameAvailability(supportTicketName, subscriptionId, apiVersion, checkNameAvailabilityInput, (error, data, response) => {
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
 **checkNameAvailabilityInput** | [**CheckNameAvailabilityInput**](CheckNameAvailabilityInput.md)| Input to check | 

### Return type

[**CheckNameAvailabilityOutput**](CheckNameAvailabilityOutput.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## communicationsCreate

> CommunicationDetails communicationsCreate(supportTicketName, communicationName, subscriptionId, apiVersion, createCommunicationParameters)



Adds a new customer communication to an Azure support ticket. Adding attachments are not currently supported via the API. &lt;br/&gt;To add a file to a support ticket, visit the &lt;a target&#x3D;&#39;_blank&#39; href&#x3D;&#39;https://portal.azure.com/#blade/Microsoft_Azure_Support/HelpAndSupportBlade/managesupportrequest&#39;&gt;Manage support ticket&lt;/a&gt; page in the Azure portal, select the support ticket, and use the file upload control to add a new file.

### Example

```javascript
import MicrosoftSupport from 'microsoft_support';
let defaultClient = MicrosoftSupport.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftSupport.CommunicationsApi();
let supportTicketName = "supportTicketName_example"; // String | Support ticket name
let communicationName = "communicationName_example"; // String | Communication name
let subscriptionId = "subscriptionId_example"; // String | Azure subscription id
let apiVersion = "apiVersion_example"; // String | Api version
let createCommunicationParameters = new MicrosoftSupport.CommunicationDetails(); // CommunicationDetails | Communication object
apiInstance.communicationsCreate(supportTicketName, communicationName, subscriptionId, apiVersion, createCommunicationParameters, (error, data, response) => {
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
 **communicationName** | **String**| Communication name | 
 **subscriptionId** | **String**| Azure subscription id | 
 **apiVersion** | **String**| Api version | 
 **createCommunicationParameters** | [**CommunicationDetails**](CommunicationDetails.md)| Communication object | 

### Return type

[**CommunicationDetails**](CommunicationDetails.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## communicationsGet

> CommunicationDetails communicationsGet(supportTicketName, communicationName, subscriptionId, apiVersion)



Returns details of a specific communication in a support ticket.

### Example

```javascript
import MicrosoftSupport from 'microsoft_support';
let defaultClient = MicrosoftSupport.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftSupport.CommunicationsApi();
let supportTicketName = "supportTicketName_example"; // String | Support ticket name
let communicationName = "communicationName_example"; // String | Communication name
let subscriptionId = "subscriptionId_example"; // String | Azure subscription id
let apiVersion = "apiVersion_example"; // String | Api version
apiInstance.communicationsGet(supportTicketName, communicationName, subscriptionId, apiVersion, (error, data, response) => {
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
 **communicationName** | **String**| Communication name | 
 **subscriptionId** | **String**| Azure subscription id | 
 **apiVersion** | **String**| Api version | 

### Return type

[**CommunicationDetails**](CommunicationDetails.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## communicationsList

> CommunicationsListResult communicationsList(supportTicketName, subscriptionId, apiVersion, opts)



Lists all communications (attachments not included) for a support ticket. &lt;br/&gt;&lt;/br&gt; You can also filter support ticket communications by &lt;i&gt;CreatedDate&lt;/i&gt;�or &lt;i&gt;CommunicationType&lt;/i&gt; using the $filter parameter. The only type of communication supported today is &lt;i&gt;Web&lt;/i&gt;. Output will be a paged result with &lt;i&gt;nextLink&lt;/i&gt;, using which you can retrieve the next set of Communication results. &lt;br/&gt;&lt;br/&gt; Support ticket data is available for 12 months after ticket creation. If a ticket was created more than 12 months ago, a request for data might cause an error.

### Example

```javascript
import MicrosoftSupport from 'microsoft_support';
let defaultClient = MicrosoftSupport.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftSupport.CommunicationsApi();
let supportTicketName = "supportTicketName_example"; // String | Support ticket name
let subscriptionId = "subscriptionId_example"; // String | Azure subscription id
let apiVersion = "apiVersion_example"; // String | Api version
let opts = {
  'top': 56, // Number | The number of values to return in the collection. Default is 10 and max is 10.
  'filter': "filter_example" // String | The filter to apply on the operation. You can filter by communicationType and createdDate properties. CommunicationType supports Equals ('eq') operator and createdDate supports Greater Than ('gt') and Greater Than or Equals ('ge') operators. You may combine the CommunicationType and CreatedDate filters by Logical And ('and') operator.
};
apiInstance.communicationsList(supportTicketName, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **top** | **Number**| The number of values to return in the collection. Default is 10 and max is 10. | [optional] 
 **filter** | **String**| The filter to apply on the operation. You can filter by communicationType and createdDate properties. CommunicationType supports Equals (&#39;eq&#39;) operator and createdDate supports Greater Than (&#39;gt&#39;) and Greater Than or Equals (&#39;ge&#39;) operators. You may combine the CommunicationType and CreatedDate filters by Logical And (&#39;and&#39;) operator. | [optional] 

### Return type

[**CommunicationsListResult**](CommunicationsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

