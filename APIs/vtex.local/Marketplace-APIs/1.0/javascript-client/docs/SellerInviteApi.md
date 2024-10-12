# MarketplaceApi.SellerInviteApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**acceptSellerLead**](SellerInviteApi.md#acceptSellerLead) | **PUT** /seller-register/pvt/seller-leads/{sellerLeadId} | Accept Seller Lead
[**createSellerFromSellerLead**](SellerInviteApi.md#createSellerFromSellerLead) | **PUT** /seller-register/pvt/seller-leads/{sellerLeadId}/seller | Create Seller From Lead
[**createSellerLead**](SellerInviteApi.md#createSellerLead) | **POST** /seller-register/pvt/seller-leads | Invite Seller Lead
[**listSellerLeads**](SellerInviteApi.md#listSellerLeads) | **GET** /seller-register/pvt/seller-leads | List Seller Leads
[**removeSellerLead**](SellerInviteApi.md#removeSellerLead) | **DELETE** /seller-register/pvt/seller-leads/{sellerLeadId} | Delete Seller Lead
[**resendSellerLeadRequest**](SellerInviteApi.md#resendSellerLeadRequest) | **PUT** /seller-register/pvt/seller-leads/{sellerLeadId}/status | Resend Seller Lead Invite
[**retrieveSellerLead**](SellerInviteApi.md#retrieveSellerLead) | **GET** /seller-register/pvt/seller-leads/{sellerLeadId} | Get Seller Lead&#39;s Data by Id



## acceptSellerLead

> acceptSellerLead(accountName, environment, sellerLeadId, accept, contentType, acceptSellerLeadRequest)

Accept Seller Lead

This endpoint is triggered by the seller onboarding wizard, once the seller confirms their invitation. It can be used by marketplace operators to manually accept seller leads, and carry on with their onboarding process.   Note that there&#39;s no specific API call that allows status changes. The operations only allow the seller lead to move forward:    From &#x60;invite&#x60; &gt; to &#x60;Accept&#x60; &gt; closing on &#x60;Create Seller&#x60;.    If you want to change the status, you can start the process again, by deleting that lead through the *Delete Seller Lead* endpoint, and resending the invite through the *Resend Seller Lead&#39;s Invite* endpoint.

### Example

```javascript
import MarketplaceApi from 'marketplace_api';
let defaultClient = MarketplaceApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new MarketplaceApi.SellerInviteApi();
let accountName = "'apiexamples'"; // String | Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account.
let environment = "'vtexcommercestable'"; // String | Environment to use. Used as part of the URL.
let sellerLeadId = "sellerLeadId_example"; // String | ID of the Seller Lead invited to the marketplace.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let contentType = "'application/json'"; // String | Type of the content being sent.
let acceptSellerLeadRequest = {"accountId":"5fb38ace-d95e-45ad-970d-ee97cce9fbcd","accountable":{"email":"email@email.com","name":"Jane Smith","phone":"1234567890"},"address":{"city":"Rio de Janeiro","complement":"Appartment 1234","neighborhood":"VTEX quarter","number":"25","postalcode":"12345678","state":"RJ","street":"VTEX street"},"document":"12345671000","email":"seller@email.com","hasAcceptedLegalTerms":true,"salesChannel":"1","sellerAccountName":"seller123","sellerEmail":"selleremail@email.com","sellerName":"Seller Name","sellerType":1}; // AcceptSellerLeadRequest | 
apiInstance.acceptSellerLead(accountName, environment, sellerLeadId, accept, contentType, acceptSellerLeadRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountName** | **String**| Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account. | [default to &#39;apiexamples&#39;]
 **environment** | **String**| Environment to use. Used as part of the URL. | [default to &#39;vtexcommercestable&#39;]
 **sellerLeadId** | **String**| ID of the Seller Lead invited to the marketplace. | 
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **acceptSellerLeadRequest** | [**AcceptSellerLeadRequest**](AcceptSellerLeadRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## createSellerFromSellerLead

> createSellerFromSellerLead(accountName, environment, isActive, sellerLeadId, accept, contentType)

Create Seller From Lead

This endpoint is used by marketplace operators to create seller accounts. The request will only accept Seller Leads whose status is &#x60;accepted&#x60;. If they are already &#x60;connected&#x60; or &#x60;invited&#x60;, the call will not be fulfilled.   The creation of the account at VTEX is done by an internal Billing service. There is no seller account and marketplace affiliation if you do not go through this step.   Note that there&#39;s no specific API call that allows status changes. The operations only allow the seller lead to move forward:    From &#x60;invite&#x60; &gt; to &#x60;Accept&#x60; &gt; closing on &#x60;Create Seller&#x60;.    If you want to change the status, you can start the process again, by deleting that lead through the *Delete Seller Lead* endpoint, and resending the invite through the *Resend Seller Lead&#39;s Invite* endpoint.

### Example

```javascript
import MarketplaceApi from 'marketplace_api';
let defaultClient = MarketplaceApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new MarketplaceApi.SellerInviteApi();
let accountName = "'apiexamples'"; // String | Marketplace's account name, the same one inputted on the endpoint's path.
let environment = "'vtexcommercestable'"; // String | Environment to use. Used as part of the URL.
let isActive = false; // Boolean | Whether the Seller Lead is `active` or not in Seller Portal. This request only supports the value `false` in this field. If that´s not the case, the request will respond with an internal error.
let sellerLeadId = "sellerLeadId_example"; // String | ID of the Seller Lead invited to the marketplace.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let contentType = "'application/json'"; // String | Type of the content being sent.
apiInstance.createSellerFromSellerLead(accountName, environment, isActive, sellerLeadId, accept, contentType, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountName** | **String**| Marketplace&#39;s account name, the same one inputted on the endpoint&#39;s path. | [default to &#39;apiexamples&#39;]
 **environment** | **String**| Environment to use. Used as part of the URL. | [default to &#39;vtexcommercestable&#39;]
 **isActive** | **Boolean**| Whether the Seller Lead is &#x60;active&#x60; or not in Seller Portal. This request only supports the value &#x60;false&#x60; in this field. If that´s not the case, the request will respond with an internal error. | [default to false]
 **sellerLeadId** | **String**| ID of the Seller Lead invited to the marketplace. | 
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## createSellerLead

> createSellerLead(accountName, environment, accept, contentType, createSellerLeadRequest)

Invite Seller Lead

This API is used by marketplace operators to invite sellers to join their marketplace. The request sends an email to the seller, inviting sellers to activate their store. The invitation&#39;s link in the email is unique per user, and available for only seven days for the seller to click and begin activating their store.   The email template is completely customizable. All email templates that VTEX sends to seller leads can be found and edited in the marketplace&#39;s VTEX Admin, on the Message Center section.

### Example

```javascript
import MarketplaceApi from 'marketplace_api';
let defaultClient = MarketplaceApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new MarketplaceApi.SellerInviteApi();
let accountName = "'apiexample'"; // String | Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account.
let environment = "'vtexcommercestable'"; // String | Environment to use. Used as part of the URL.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let createSellerLeadRequest = {"accountId":"5fb38ace-d95e-45ad-970d-ee97cce9fbcd","accountable":{"email":"email@email.com","name":"Jane Smith","phone":"1234567890"},"address":{"city":"Rio de Janeiro","complement":"Appartment 1234","neighborhood":"VTEX quarter","number":"25","postalcode":"12345678","state":"RJ","street":"VTEX street"},"document":"12345671000","email":"email@email.com","hasAcceptedLegalTerms":true,"salesChannel":"1","sellerAccountName":"seller123","sellerEmail":"selleremail@email.com","sellerName":"Seller Name","sellerType":1}; // CreateSellerLeadRequest | 
apiInstance.createSellerLead(accountName, environment, accept, contentType, createSellerLeadRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountName** | **String**| Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account. | [default to &#39;apiexample&#39;]
 **environment** | **String**| Environment to use. Used as part of the URL. | [default to &#39;vtexcommercestable&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **contentType** | **String**| Describes the type of the content being sent. | [default to &#39;application/json&#39;]
 **createSellerLeadRequest** | [**CreateSellerLeadRequest**](CreateSellerLeadRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## listSellerLeads

> listSellerLeads(accountName, environment, offset, limit, isConnected, search, status, orderBy, accept, contentType)

List Seller Leads

This call&#39;s response includes a list of all sellers invited by the marketplace operator to join them. Retrieved results can be filtered by adding optional query fields to the request. Each seller listed includes the following information:   - &#x60;id&#x60;   - &#x60;createdAt&#x60;   - &#x60;status&#x60;   - &#x60;isConnected&#x60;   - &#x60;sellerEmail&#x60;   - &#x60;sellerName&#x60;   - &#x60;salesChannel&#x60;   - &#x60;email&#x60;

### Example

```javascript
import MarketplaceApi from 'marketplace_api';
let defaultClient = MarketplaceApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new MarketplaceApi.SellerInviteApi();
let accountName = "'apiexamples'"; // String | Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account.
let environment = "'vtexcommercestable'"; // String | Environment to use. Used as part of the URL.
let offset = 0; // Number | This field determines the limit used to retrieve the list of sellers. The response includes objects starting `from` the value inputted here.
let limit = 15; // Number | This field determines the limit used to retrieve the list of sellers. The response includes objects until the value inputted here.            
let isConnected = "''"; // String | Query param that enables results to be filter by whether the seller lead is already connected to the marketplace or not.
let search = "'user email'"; // String | Custom search field, that filters sellers invited by specific marketplace operator's  email.
let status = "'invited'"; // String | Seller Lead's status. Includes `accepted`, `connected` or `invited`.
let orderBy = "orderBy_example"; // String | Query param determining how data will be ordered in the response, ordering by name or ID in descending our ascending order. Includes the following values:   `namesort` = desc/asc   `idsort` = desc/asc
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
apiInstance.listSellerLeads(accountName, environment, offset, limit, isConnected, search, status, orderBy, accept, contentType, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountName** | **String**| Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account. | [default to &#39;apiexamples&#39;]
 **environment** | **String**| Environment to use. Used as part of the URL. | [default to &#39;vtexcommercestable&#39;]
 **offset** | **Number**| This field determines the limit used to retrieve the list of sellers. The response includes objects starting &#x60;from&#x60; the value inputted here. | [default to 0]
 **limit** | **Number**| This field determines the limit used to retrieve the list of sellers. The response includes objects until the value inputted here.             | [default to 15]
 **isConnected** | **String**| Query param that enables results to be filter by whether the seller lead is already connected to the marketplace or not. | [default to &#39;&#39;]
 **search** | **String**| Custom search field, that filters sellers invited by specific marketplace operator&#39;s  email. | [default to &#39;user email&#39;]
 **status** | **String**| Seller Lead&#39;s status. Includes &#x60;accepted&#x60;, &#x60;connected&#x60; or &#x60;invited&#x60;. | [default to &#39;invited&#39;]
 **orderBy** | **String**| Query param determining how data will be ordered in the response, ordering by name or ID in descending our ascending order. Includes the following values:   &#x60;namesort&#x60; &#x3D; desc/asc   &#x60;idsort&#x60; &#x3D; desc/asc | 
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **contentType** | **String**| Describes the type of the content being sent. | [default to &#39;application/json&#39;]

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## removeSellerLead

> removeSellerLead(accountName, environment, sellerLeadId, accept, contentType)

Delete Seller Lead

This endpoint permanently deletes a seller previously invited to the marketplace, if the seller has not already accepted the invitation.

### Example

```javascript
import MarketplaceApi from 'marketplace_api';
let defaultClient = MarketplaceApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new MarketplaceApi.SellerInviteApi();
let accountName = "'apiexamples'"; // String | Name of the VTEX account that belongs to the marketplace.
let environment = "'vtexcommercestable'"; // String | Environment to use. Used as part of the URL.
let sellerLeadId = "sellerLeadId_example"; // String | ID of the Seller Lead invited to the marketplace.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let contentType = "'application/json'"; // String | Type of the content being sent.
apiInstance.removeSellerLead(accountName, environment, sellerLeadId, accept, contentType, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountName** | **String**| Name of the VTEX account that belongs to the marketplace. | [default to &#39;apiexamples&#39;]
 **environment** | **String**| Environment to use. Used as part of the URL. | [default to &#39;vtexcommercestable&#39;]
 **sellerLeadId** | **String**| ID of the Seller Lead invited to the marketplace. | 
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## resendSellerLeadRequest

> resendSellerLeadRequest(accountName, environment, sellerLeadId, accept, contentType, resendSellerLeadRequestRequest)

Resend Seller Lead Invite

This endpoint allows marketplace operators to resend an invitation to a seller lead, previously invited to join their marketplace. The request will only accept Seller Leads whose status is &#x60;invited&#x60;. If they are already &#x60;connected&#x60; or &#x60;accepted&#x60;, the call will not be fulfilled.

### Example

```javascript
import MarketplaceApi from 'marketplace_api';
let defaultClient = MarketplaceApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new MarketplaceApi.SellerInviteApi();
let accountName = "'apiexamples'"; // String | Name of the VTEX account that belongs to the marketplace.
let environment = "'vtexcommercestable'"; // String | Environment to use. Used as part of the URL.
let sellerLeadId = "sellerLeadId_example"; // String | ID of the Seller Lead invited to the marketplace.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let contentType = "'application/json'"; // String | Type of the content being sent.
let resendSellerLeadRequestRequest = {"status":"accepted"}; // ResendSellerLeadRequestRequest | 
apiInstance.resendSellerLeadRequest(accountName, environment, sellerLeadId, accept, contentType, resendSellerLeadRequestRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountName** | **String**| Name of the VTEX account that belongs to the marketplace. | [default to &#39;apiexamples&#39;]
 **environment** | **String**| Environment to use. Used as part of the URL. | [default to &#39;vtexcommercestable&#39;]
 **sellerLeadId** | **String**| ID of the Seller Lead invited to the marketplace. | 
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **resendSellerLeadRequestRequest** | [**ResendSellerLeadRequestRequest**](ResendSellerLeadRequestRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## retrieveSellerLead

> retrieveSellerLead(accountName, environment, sellerLeadId, accept, contentType)

Get Seller Lead&#39;s Data by Id

Marketplace operators may call this endpoint to retrieve information about a specific seller invited to the Seller Portal, by searching through their &#x60;Seller Lead Id&#x60;. To know the chosen seller&#39;s &#x60;sellerLeadId&#x60;, marketplace operators can count on the *List Sellers* endpoint&#39;s response as well. Each seller listed includes the following information:   - &#x60;id&#x60;   - &#x60;createdAt&#x60;   - &#x60;status&#x60;   - &#x60;isConnected&#x60;   - &#x60;sellerEmail&#x60;   - &#x60;sellerName&#x60;   - &#x60;salesChannel&#x60;   - &#x60;email&#x60;

### Example

```javascript
import MarketplaceApi from 'marketplace_api';
let defaultClient = MarketplaceApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new MarketplaceApi.SellerInviteApi();
let accountName = "'apiexamples'"; // String | Name of the VTEX account that belongs to the marketplace.
let environment = "'vtexcommercestable'"; // String | Environment to use. Used as part of the URL.
let sellerLeadId = "sellerLeadId_example"; // String | ID of the Seller Lead invited to the marketplace.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let contentType = "'application/json'"; // String | Type of the content being sent.
apiInstance.retrieveSellerLead(accountName, environment, sellerLeadId, accept, contentType, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountName** | **String**| Name of the VTEX account that belongs to the marketplace. | [default to &#39;apiexamples&#39;]
 **environment** | **String**| Environment to use. Used as part of the URL. | [default to &#39;vtexcommercestable&#39;]
 **sellerLeadId** | **String**| ID of the Seller Lead invited to the marketplace. | 
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

