# LinodeApi.AccountApi

All URIs are relative to *https://api.linode.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**acceptEntityTransfer**](AccountApi.md#acceptEntityTransfer) | **POST** /account/entity-transfers/{token}/accept | Entity Transfer Accept
[**acceptServiceTransfer**](AccountApi.md#acceptServiceTransfer) | **POST** /account/service-transfers/{token}/accept | Service Transfer Accept
[**cancelAccount**](AccountApi.md#cancelAccount) | **POST** /account/cancel | Account Cancel
[**createClient**](AccountApi.md#createClient) | **POST** /account/oauth-clients | OAuth Client Create
[**createCreditCard**](AccountApi.md#createCreditCard) | **POST** /account/credit-card | Credit Card Add/Edit
[**createEntityTransfer**](AccountApi.md#createEntityTransfer) | **POST** /account/entity-transfers | Entity Transfer Create
[**createPayPalPayment**](AccountApi.md#createPayPalPayment) | **POST** /account/payments/paypal | PayPal Payment Stage
[**createPayment**](AccountApi.md#createPayment) | **POST** /account/payments | Payment Make
[**createPaymentMethod**](AccountApi.md#createPaymentMethod) | **POST** /account/payment-methods | Payment Method Add
[**createPromoCredit**](AccountApi.md#createPromoCredit) | **POST** /account/promo-codes | Promo Credit Add
[**createServiceTransfer**](AccountApi.md#createServiceTransfer) | **POST** /account/service-transfers | Service Transfer Create
[**createUser**](AccountApi.md#createUser) | **POST** /account/users | User Create
[**deleteClient**](AccountApi.md#deleteClient) | **DELETE** /account/oauth-clients/{clientId} | OAuth Client Delete
[**deleteEntityTransfer**](AccountApi.md#deleteEntityTransfer) | **DELETE** /account/entity-transfers/{token} | Entity Transfer Cancel
[**deletePaymentMethod**](AccountApi.md#deletePaymentMethod) | **DELETE** /account/payment-methods/{paymentMethodId} | Payment Method Delete
[**deleteServiceTransfer**](AccountApi.md#deleteServiceTransfer) | **DELETE** /account/service-transfers/{token} | Service Transfer Cancel
[**deleteUser**](AccountApi.md#deleteUser) | **DELETE** /account/users/{username} | User Delete
[**enableAccountManaged**](AccountApi.md#enableAccountManaged) | **POST** /account/settings/managed-enable | Linode Managed Enable
[**eventRead**](AccountApi.md#eventRead) | **POST** /account/events/{eventId}/read | Event Mark as Read
[**eventSeen**](AccountApi.md#eventSeen) | **POST** /account/events/{eventId}/seen | Event Mark as Seen
[**executePayPalPayment**](AccountApi.md#executePayPalPayment) | **POST** /account/payments/paypal/execute | Staged/Approved PayPal Payment Execute
[**getAccount**](AccountApi.md#getAccount) | **GET** /account | Account View
[**getAccountLogin**](AccountApi.md#getAccountLogin) | **GET** /account/logins/{loginId} | Login View
[**getAccountLogins**](AccountApi.md#getAccountLogins) | **GET** /account/logins | User Logins List All
[**getAccountSettings**](AccountApi.md#getAccountSettings) | **GET** /account/settings | Account Settings View
[**getClient**](AccountApi.md#getClient) | **GET** /account/oauth-clients/{clientId} | OAuth Client View
[**getClientThumbnail**](AccountApi.md#getClientThumbnail) | **GET** /account/oauth-clients/{clientId}/thumbnail | OAuth Client Thumbnail View
[**getClients**](AccountApi.md#getClients) | **GET** /account/oauth-clients | OAuth Clients List
[**getEntityTransfer**](AccountApi.md#getEntityTransfer) | **GET** /account/entity-transfers/{token} | Entity Transfer View
[**getEntityTransfers**](AccountApi.md#getEntityTransfers) | **GET** /account/entity-transfers | Entity Transfers List
[**getEvent**](AccountApi.md#getEvent) | **GET** /account/events/{eventId} | Event View
[**getEvents**](AccountApi.md#getEvents) | **GET** /account/events | Events List
[**getInvoice**](AccountApi.md#getInvoice) | **GET** /account/invoices/{invoiceId} | Invoice View
[**getInvoiceItems**](AccountApi.md#getInvoiceItems) | **GET** /account/invoices/{invoiceId}/items | Invoice Items List
[**getInvoices**](AccountApi.md#getInvoices) | **GET** /account/invoices | Invoices List
[**getMaintenance**](AccountApi.md#getMaintenance) | **GET** /account/maintenance | Maintenance List
[**getNotifications**](AccountApi.md#getNotifications) | **GET** /account/notifications | Notifications List
[**getPayment**](AccountApi.md#getPayment) | **GET** /account/payments/{paymentId} | Payment View
[**getPaymentMethod**](AccountApi.md#getPaymentMethod) | **GET** /account/payment-methods/{paymentMethodId} | Payment Method View
[**getPaymentMethods**](AccountApi.md#getPaymentMethods) | **GET** /account/payment-methods | Payment Methods List
[**getPayments**](AccountApi.md#getPayments) | **GET** /account/payments | Payments List
[**getServiceTransfer**](AccountApi.md#getServiceTransfer) | **GET** /account/service-transfers/{token} | Service Transfer View
[**getServiceTransfers**](AccountApi.md#getServiceTransfers) | **GET** /account/service-transfers | Service Transfers List
[**getTransfer**](AccountApi.md#getTransfer) | **GET** /account/transfer | Network Utilization View
[**getUser**](AccountApi.md#getUser) | **GET** /account/users/{username} | User View
[**getUserGrants**](AccountApi.md#getUserGrants) | **GET** /account/users/{username}/grants | User&#39;s Grants View
[**getUsers**](AccountApi.md#getUsers) | **GET** /account/users | Users List
[**makePaymentMethodDefault**](AccountApi.md#makePaymentMethodDefault) | **POST** /account/payment-methods/{paymentMethodId}/make-default | Payment Method Make Default
[**resetClientSecret**](AccountApi.md#resetClientSecret) | **POST** /account/oauth-clients/{clientId}/reset-secret | OAuth Client Secret Reset
[**setClientThumbnail**](AccountApi.md#setClientThumbnail) | **PUT** /account/oauth-clients/{clientId}/thumbnail | OAuth Client Thumbnail Update
[**updateAccount**](AccountApi.md#updateAccount) | **PUT** /account | Account Update
[**updateAccountSettings**](AccountApi.md#updateAccountSettings) | **PUT** /account/settings | Account Settings Update
[**updateClient**](AccountApi.md#updateClient) | **PUT** /account/oauth-clients/{clientId} | OAuth Client Update
[**updateUser**](AccountApi.md#updateUser) | **PUT** /account/users/{username} | User Update
[**updateUserGrants**](AccountApi.md#updateUserGrants) | **PUT** /account/users/{username}/grants | User&#39;s Grants Update



## acceptEntityTransfer

> Object acceptEntityTransfer(token)

Entity Transfer Accept

**DEPRECATED**. Please use [Service Transfer Accept](/docs/api/account/#service-transfer-accept). 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.AccountApi();
let token = "token_example"; // String | The UUID of the Entity Transfer.
apiInstance.acceptEntityTransfer(token, (error, data, response) => {
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
 **token** | **String**| The UUID of the Entity Transfer. | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## acceptServiceTransfer

> Object acceptServiceTransfer(token)

Service Transfer Accept

Accept a Service Transfer for the provided token to receive the services included in the transfer to your account. At this time, only Linodes can be transferred.  When accepted, email confirmations are sent to the accounts that created and accepted the transfer. A transfer can take up to three hours to complete once accepted. Once a transfer is completed, billing for transferred services ends for the sending account and begins for the receiving account.  This command can only be accessed by the unrestricted users of the account that receives the transfer. Users of the same account that created a transfer cannot accept the transfer.  There are several conditions that must be met in order to accept a transfer request:  1. Only transfers with a &#x60;pending&#x60; status can be accepted.  1. The account accepting the transfer must have a registered payment method and must not have a past due   balance or other account limitations for the services to be transferred.  1. Both the account that created the transfer and the account that is accepting the transfer must not have any active Terms of Service violations.  1. The service must still be owned by the account that created the transfer.  1. Linodes must not:      * be assigned to a NodeBalancer, Firewall, VLAN, or Managed Service.      * have any attached Block Storage Volumes.      * have any shared IP addresses.      * have any assigned /56, /64, or /116 IPv6 ranges.  Any and all of the above conditions must be cured and maintained by the relevant account prior to the transfer&#39;s expiration to allow the transfer to be accepted by the receiving account. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.AccountApi();
let token = "token_example"; // String | The UUID of the Service Transfer.
apiInstance.acceptServiceTransfer(token, (error, data, response) => {
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
 **token** | **String**| The UUID of the Service Transfer. | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cancelAccount

> CancelAccount200Response cancelAccount(cancelAccountRequest)

Account Cancel

Cancels an active Linode account. This action will cause Linode to attempt to charge the credit card on file for the remaining balance. An error will occur if Linode fails to charge the credit card on file. Restricted users will not be able to cancel an account. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.AccountApi();
let cancelAccountRequest = new LinodeApi.CancelAccountRequest(); // CancelAccountRequest | Supply a comment stating the reason that you are cancelling your account. 
apiInstance.cancelAccount(cancelAccountRequest, (error, data, response) => {
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
 **cancelAccountRequest** | [**CancelAccountRequest**](CancelAccountRequest.md)| Supply a comment stating the reason that you are cancelling your account.  | 

### Return type

[**CancelAccount200Response**](CancelAccount200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createClient

> OAuthClient createClient(opts)

OAuth Client Create

Creates an OAuth Client, which can be used to allow users (using their Linode account) to log in to your own application, and optionally grant your application some amount of access to their Linodes or other entities. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.AccountApi();
let opts = {
  'oAuthClient': new LinodeApi.OAuthClient() // OAuthClient | Information about the OAuth Client to create.
};
apiInstance.createClient(opts, (error, data, response) => {
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
 **oAuthClient** | [**OAuthClient**](OAuthClient.md)| Information about the OAuth Client to create. | [optional] 

### Return type

[**OAuthClient**](OAuthClient.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createCreditCard

> Object createCreditCard(creditCard)

Credit Card Add/Edit

**DEPRECATED**. Please use Payment Method Add ([POST /account/payment-methods](/docs/api/account/#payment-method-add)).  Adds a credit card Payment Method to your account and sets it as the default method. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.AccountApi();
let creditCard = new LinodeApi.CreditCard(); // CreditCard | Update the credit card information associated with your Account.
apiInstance.createCreditCard(creditCard, (error, data, response) => {
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
 **creditCard** | [**CreditCard**](CreditCard.md)| Update the credit card information associated with your Account. | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createEntityTransfer

> EntityTransfer createEntityTransfer(opts)

Entity Transfer Create

**DEPRECATED**. Please use [Service Transfer Create](/docs/api/account/#service-transfer-create). 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.AccountApi();
let opts = {
  'createEntityTransferRequest': new LinodeApi.CreateEntityTransferRequest() // CreateEntityTransferRequest | The entities to include in this transfer request.
};
apiInstance.createEntityTransfer(opts, (error, data, response) => {
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
 **createEntityTransferRequest** | [**CreateEntityTransferRequest**](CreateEntityTransferRequest.md)| The entities to include in this transfer request. | [optional] 

### Return type

[**EntityTransfer**](EntityTransfer.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createPayPalPayment

> CreatePayPalPayment200Response createPayPalPayment(payPal)

PayPal Payment Stage

**Note**: This endpoint is disabled and no longer accessible. PayPal can be designated as a Payment Method for automated payments using the Cloud Manager. See [Manage Payment Methods](/docs/products/platform/billing/guides/payment-methods/). 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.AccountApi();
let payPal = new LinodeApi.PayPal(); // PayPal | The amount of the Payment to submit via PayPal. 
apiInstance.createPayPalPayment(payPal, (error, data, response) => {
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
 **payPal** | [**PayPal**](PayPal.md)| The amount of the Payment to submit via PayPal.  | 

### Return type

[**CreatePayPalPayment200Response**](CreatePayPalPayment200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createPayment

> Payment createPayment(paymentRequest)

Payment Make

Makes a Payment to your Account.  * The requested amount is charged to the default Payment Method if no &#x60;payment_method_id&#x60; is specified.  * A &#x60;payment_submitted&#x60; event is generated when a payment is successfully submitted. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.AccountApi();
let paymentRequest = new LinodeApi.PaymentRequest(); // PaymentRequest | Information about the Payment you are making.
apiInstance.createPayment(paymentRequest, (error, data, response) => {
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
 **paymentRequest** | [**PaymentRequest**](PaymentRequest.md)| Information about the Payment you are making. | 

### Return type

[**Payment**](Payment.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createPaymentMethod

> Object createPaymentMethod(createPaymentMethodRequest)

Payment Method Add

Adds a Payment Method to your Account with the option to set it as the default method.  * Adding a default Payment Method removes the default status from any other Payment Method.  * An Account can have up to 6 active Payment Methods.  * Up to 60 Payment Methods can be added each day.  * Prior to adding a Payment Method, ensure that your billing address information is up-to-date with a valid &#x60;zip&#x60; by using the Account Update ([PUT /account](/docs/api/account/#account-update)) endpoint.  * A &#x60;payment_method_add&#x60; event is generated when a payment is successfully submitted. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.AccountApi();
let createPaymentMethodRequest = new LinodeApi.CreatePaymentMethodRequest(); // CreatePaymentMethodRequest | The details of the Payment Method to add.
apiInstance.createPaymentMethod(createPaymentMethodRequest, (error, data, response) => {
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
 **createPaymentMethodRequest** | [**CreatePaymentMethodRequest**](CreatePaymentMethodRequest.md)| The details of the Payment Method to add. | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createPromoCredit

> Promotion createPromoCredit(opts)

Promo Credit Add

Adds an expiring Promo Credit to your account.  The following restrictions apply:  * Your account must be less than 90 days old. * There must not be an existing Promo Credit already on your account. * The requesting User must be unrestricted. Use the User Update   ([PUT /account/users/{username}](/docs/api/account/#user-update)) to change a User&#39;s restricted status. * The &#x60;promo_code&#x60; must be valid and unexpired. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.AccountApi();
let opts = {
  'createPromoCreditRequest': new LinodeApi.CreatePromoCreditRequest() // CreatePromoCreditRequest | Enter a Promo Code to add its associated credit to your Account.
};
apiInstance.createPromoCredit(opts, (error, data, response) => {
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
 **createPromoCreditRequest** | [**CreatePromoCreditRequest**](CreatePromoCreditRequest.md)| Enter a Promo Code to add its associated credit to your Account. | [optional] 

### Return type

[**Promotion**](Promotion.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createServiceTransfer

> ServiceTransfer createServiceTransfer(opts)

Service Transfer Create

Creates a transfer request for the specified services. A request can contain any of the specified service types and any number of each service type. At this time, only Linodes can be transferred.  When created successfully, a confirmation email is sent to the account that created this transfer containing a transfer token and instructions on completing the transfer.  When a transfer is [accepted](/docs/api/account/#service-transfer-accept), the requested services are moved to the receiving account. Linode services will not experience interruptions due to the transfer process. Backups for Linodes are transferred as well.  DNS records that are associated with requested services will not be transferred or updated. Please ensure that associated DNS records have been updated or communicated to the recipient prior to the transfer.  A transfer can take up to three hours to complete once accepted. When a transfer is completed, billing for transferred services ends for the sending account and begins for the receiving account.  This command can only be accessed by the unrestricted users of an account.  There are several conditions that must be met in order to successfully create a transfer request:  1. The account creating the transfer must not have a past due balance or active Terms of Service violation.  1. The service must be owned by the account that is creating the transfer.  1. The service must not be assigned to another Service Transfer that is pending or that has been accepted and is incomplete.  1. Linodes must not:      * be assigned to a NodeBalancer, Firewall, VLAN, or Managed Service.      * have any attached Block Storage Volumes.      * have any shared IP addresses.      * have any assigned /56, /64, or /116 IPv6 ranges. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.AccountApi();
let opts = {
  'createServiceTransferRequest': new LinodeApi.CreateServiceTransferRequest() // CreateServiceTransferRequest | The services to include in this transfer request.
};
apiInstance.createServiceTransfer(opts, (error, data, response) => {
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
 **createServiceTransferRequest** | [**CreateServiceTransferRequest**](CreateServiceTransferRequest.md)| The services to include in this transfer request. | [optional] 

### Return type

[**ServiceTransfer**](ServiceTransfer.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createUser

> User createUser(opts)

User Create

Creates a User on your Account. Once created, a confirmation message containing password creation and login instructions is sent to the User&#39;s email address.  This command can only be accessed by the unrestricted users of an account.  The User&#39;s account access is determined by whether or not they are restricted, and what grants they have been given. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.AccountApi();
let opts = {
  'user': new LinodeApi.User() // User | Information about the User to create.
};
apiInstance.createUser(opts, (error, data, response) => {
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
 **user** | [**User**](User.md)| Information about the User to create. | [optional] 

### Return type

[**User**](User.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteClient

> Object deleteClient(clientId)

OAuth Client Delete

Deletes an OAuth Client registered with Linode. The Client ID and Client secret will no longer be accepted by &lt;a target&#x3D;\&quot;_top\&quot; href&#x3D;\&quot;https://login.linode.com\&quot;&gt;https://login.linode.com&lt;/a&gt;, and all tokens issued to this client will be invalidated (meaning that if your application was using a token, it will no longer work). 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.AccountApi();
let clientId = "clientId_example"; // String | The OAuth Client ID to look up.
apiInstance.deleteClient(clientId, (error, data, response) => {
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
 **clientId** | **String**| The OAuth Client ID to look up. | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteEntityTransfer

> Object deleteEntityTransfer(token)

Entity Transfer Cancel

**DEPRECATED**. Please use [Service Transfer Cancel](/docs/api/account/#service-transfer-cancel). 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.AccountApi();
let token = "token_example"; // String | The UUID of the Entity Transfer.
apiInstance.deleteEntityTransfer(token, (error, data, response) => {
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
 **token** | **String**| The UUID of the Entity Transfer. | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deletePaymentMethod

> Object deletePaymentMethod(paymentMethodId)

Payment Method Delete

Deactivate the specified Payment Method.  The default Payment Method can not be deleted. To add a new default Payment Method, access the Payment Method Add ([POST /account/payment-methods](/docs/api/account/#payment-method-add)) endpoint. To designate an existing Payment Method as the default method, access the Payment Method Make Default ([POST /account/payment-methods/{paymentMethodId}/make-default](/docs/api/account/#payment-method-make-default)) endpoint. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.AccountApi();
let paymentMethodId = 56; // Number | The ID of the Payment Method to look up.
apiInstance.deletePaymentMethod(paymentMethodId, (error, data, response) => {
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
 **paymentMethodId** | **Number**| The ID of the Payment Method to look up. | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteServiceTransfer

> Object deleteServiceTransfer(token)

Service Transfer Cancel

Cancels the Service Transfer for the provided token. Once cancelled, a transfer cannot be accepted or otherwise acted on in any way. If cancelled in error, the transfer must be [created](/docs/api/account/#service-transfer-create) again.  When cancelled, an email notification for the cancellation is sent to the account that created this transfer. Transfers can not be cancelled if they are expired or have been accepted.  This command can only be accessed by the unrestricted users of the account that created this transfer. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.AccountApi();
let token = "token_example"; // String | The UUID of the Service Transfer.
apiInstance.deleteServiceTransfer(token, (error, data, response) => {
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
 **token** | **String**| The UUID of the Service Transfer. | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteUser

> Object deleteUser(username)

User Delete

Deletes a User. The deleted User will be immediately logged out and may no longer log in or perform any actions. All of the User&#39;s Grants will be removed.  This command can only be accessed by the unrestricted users of an account. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.AccountApi();
let username = "username_example"; // String | The username to look up.
apiInstance.deleteUser(username, (error, data, response) => {
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
 **username** | **String**| The username to look up. | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## enableAccountManaged

> Object enableAccountManaged()

Linode Managed Enable

Enables Linode Managed for the entire account and sends a welcome email to the account&#39;s associated email address. Linode Managed can monitor any service or software stack reachable over TCP or HTTP. See our [Linode Managed guide](/docs/guides/linode-managed/) to learn more. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.AccountApi();
apiInstance.enableAccountManaged((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## eventRead

> Object eventRead(eventId)

Event Mark as Read

Marks a single Event as read.

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.AccountApi();
let eventId = 56; // Number | The ID of the Event to designate as read.
apiInstance.eventRead(eventId, (error, data, response) => {
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
 **eventId** | **Number**| The ID of the Event to designate as read. | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## eventSeen

> Object eventSeen(eventId)

Event Mark as Seen

Marks all Events up to and including this Event by ID as seen. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.AccountApi();
let eventId = 56; // Number | The ID of the Event to designate as seen.
apiInstance.eventSeen(eventId, (error, data, response) => {
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
 **eventId** | **Number**| The ID of the Event to designate as seen. | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## executePayPalPayment

> Object executePayPalPayment(payPalExecute)

Staged/Approved PayPal Payment Execute

**Note**: This endpoint is disabled and no longer accessible. PayPal can be designated as a Payment Method for automated payments using the Cloud Manager. See [Manage Payment Methods](/docs/products/platform/billing/guides/payment-methods/). 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.AccountApi();
let payPalExecute = new LinodeApi.PayPalExecute(); // PayPalExecute | The details of the Payment to execute. 
apiInstance.executePayPalPayment(payPalExecute, (error, data, response) => {
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
 **payPalExecute** | [**PayPalExecute**](PayPalExecute.md)| The details of the Payment to execute.  | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getAccount

> Account getAccount()

Account View

Returns the contact and billing information related to your Account. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.AccountApi();
apiInstance.getAccount((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**Account**](Account.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAccountLogin

> Login getAccountLogin(loginId)

Login View

Returns a Login object that displays information about a successful login. The logins that can be viewed can be for any user on the account, and are not limited to only the logins of the user that is accessing this API endpoint. This command can only be accessed by the unrestricted users of the account. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.AccountApi();
let loginId = 56; // Number | The ID of the login object to access.
apiInstance.getAccountLogin(loginId, (error, data, response) => {
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
 **loginId** | **Number**| The ID of the login object to access. | 

### Return type

[**Login**](Login.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAccountLogins

> GetAccountLogins200Response getAccountLogins()

User Logins List All

Returns a collection of successful logins for all users on the account during the last 90 days. This command can only be accessed by the unrestricted users of an account. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.AccountApi();
apiInstance.getAccountLogins((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**GetAccountLogins200Response**](GetAccountLogins200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAccountSettings

> AccountSettings getAccountSettings()

Account Settings View

Returns information related to your Account settings: Managed service subscription, Longview subscription, and network helper. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.AccountApi();
apiInstance.getAccountSettings((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**AccountSettings**](AccountSettings.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getClient

> OAuthClient getClient(clientId)

OAuth Client View

Returns information about a single OAuth client. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.AccountApi();
let clientId = "clientId_example"; // String | The OAuth Client ID to look up.
apiInstance.getClient(clientId, (error, data, response) => {
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
 **clientId** | **String**| The OAuth Client ID to look up. | 

### Return type

[**OAuthClient**](OAuthClient.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getClientThumbnail

> File getClientThumbnail(clientId)

OAuth Client Thumbnail View

Returns the thumbnail for this OAuth Client.  This is a publicly-viewable endpoint, and can be accessed without authentication. 

### Example

```javascript
import LinodeApi from 'linode_api';

let apiInstance = new LinodeApi.AccountApi();
let clientId = "clientId_example"; // String | The OAuth Client ID to look up.
apiInstance.getClientThumbnail(clientId, (error, data, response) => {
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
 **clientId** | **String**| The OAuth Client ID to look up. | 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/png, application/json


## getClients

> GetClients200Response getClients(opts)

OAuth Clients List

Returns a paginated list of OAuth Clients registered to your Account.  OAuth Clients allow users to log into applications you write or host using their Linode Account, and may allow them to grant some level of access to their Linodes or other entities to your application. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.AccountApi();
let opts = {
  'page': 1, // Number | The page of a collection to return.
  'pageSize': 100 // Number | The number of items to return per page.
};
apiInstance.getClients(opts, (error, data, response) => {
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
 **page** | **Number**| The page of a collection to return. | [optional] [default to 1]
 **pageSize** | **Number**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetClients200Response**](GetClients200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEntityTransfer

> EntityTransfer getEntityTransfer(token)

Entity Transfer View

**DEPRECATED**. Please use [Service Transfer View](/docs/api/account/#service-transfer-view). 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.AccountApi();
let token = "token_example"; // String | The UUID of the Entity Transfer.
apiInstance.getEntityTransfer(token, (error, data, response) => {
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
 **token** | **String**| The UUID of the Entity Transfer. | 

### Return type

[**EntityTransfer**](EntityTransfer.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEntityTransfers

> GetEntityTransfers200Response getEntityTransfers(opts)

Entity Transfers List

**DEPRECATED**. Please use [Service Transfers List](/docs/api/account/#service-transfers-list). 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.AccountApi();
let opts = {
  'page': 1, // Number | The page of a collection to return.
  'pageSize': 100 // Number | The number of items to return per page.
};
apiInstance.getEntityTransfers(opts, (error, data, response) => {
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
 **page** | **Number**| The page of a collection to return. | [optional] [default to 1]
 **pageSize** | **Number**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetEntityTransfers200Response**](GetEntityTransfers200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEvent

> Event getEvent(eventId)

Event View

Returns a single Event object. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.AccountApi();
let eventId = 56; // Number | The ID of the Event.
apiInstance.getEvent(eventId, (error, data, response) => {
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
 **eventId** | **Number**| The ID of the Event. | 

### Return type

[**Event**](Event.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEvents

> GetEvents200Response getEvents(opts)

Events List

Returns a collection of Event objects representing actions taken on your Account from the last 90 days. The Events returned depend on your grants. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.AccountApi();
let opts = {
  'page': 1, // Number | The page of a collection to return.
  'pageSize': 100 // Number | The number of items to return per page.
};
apiInstance.getEvents(opts, (error, data, response) => {
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
 **page** | **Number**| The page of a collection to return. | [optional] [default to 1]
 **pageSize** | **Number**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetEvents200Response**](GetEvents200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getInvoice

> Invoice getInvoice(invoiceId)

Invoice View

Returns a single Invoice object.

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.AccountApi();
let invoiceId = 56; // Number | The ID of the Invoice.
apiInstance.getInvoice(invoiceId, (error, data, response) => {
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
 **invoiceId** | **Number**| The ID of the Invoice. | 

### Return type

[**Invoice**](Invoice.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getInvoiceItems

> GetInvoiceItems200Response getInvoiceItems(invoiceId, opts)

Invoice Items List

Returns a paginated list of Invoice items.

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.AccountApi();
let invoiceId = 56; // Number | The ID of the Invoice.
let opts = {
  'page': 1, // Number | The page of a collection to return.
  'pageSize': 100 // Number | The number of items to return per page.
};
apiInstance.getInvoiceItems(invoiceId, opts, (error, data, response) => {
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
 **invoiceId** | **Number**| The ID of the Invoice. | 
 **page** | **Number**| The page of a collection to return. | [optional] [default to 1]
 **pageSize** | **Number**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetInvoiceItems200Response**](GetInvoiceItems200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getInvoices

> GetInvoices200Response getInvoices(opts)

Invoices List

Returns a paginated list of Invoices against your Account. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.AccountApi();
let opts = {
  'page': 1, // Number | The page of a collection to return.
  'pageSize': 100 // Number | The number of items to return per page.
};
apiInstance.getInvoices(opts, (error, data, response) => {
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
 **page** | **Number**| The page of a collection to return. | [optional] [default to 1]
 **pageSize** | **Number**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetInvoices200Response**](GetInvoices200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMaintenance

> GetMaintenance200Response getMaintenance()

Maintenance List

Returns a collection of Maintenance objects for any entity a user has permissions to view. Cancelled Maintenance objects are not returned.  Currently, Linodes are the only entities available for viewing. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.AccountApi();
apiInstance.getMaintenance((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**GetMaintenance200Response**](GetMaintenance200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNotifications

> GetNotifications200Response getNotifications()

Notifications List

Returns a collection of Notification objects representing important, often time-sensitive items related to your Account. You cannot interact directly with Notifications, and a Notification will disappear when the circumstances causing it have been resolved. For example, if you have an important Ticket open, you must respond to the Ticket to dismiss the Notification. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.AccountApi();
apiInstance.getNotifications((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**GetNotifications200Response**](GetNotifications200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPayment

> Payment getPayment(paymentId)

Payment View

Returns information about a specific Payment. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.AccountApi();
let paymentId = 56; // Number | The ID of the Payment to look up.
apiInstance.getPayment(paymentId, (error, data, response) => {
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
 **paymentId** | **Number**| The ID of the Payment to look up. | 

### Return type

[**Payment**](Payment.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPaymentMethod

> PaymentMethod getPaymentMethod(paymentMethodId)

Payment Method View

View the details of the specified Payment Method. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.AccountApi();
let paymentMethodId = 56; // Number | The ID of the Payment Method to look up.
apiInstance.getPaymentMethod(paymentMethodId, (error, data, response) => {
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
 **paymentMethodId** | **Number**| The ID of the Payment Method to look up. | 

### Return type

[**PaymentMethod**](PaymentMethod.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPaymentMethods

> GetPaymentMethods200Response getPaymentMethods(opts)

Payment Methods List

Returns a paginated list of Payment Methods for this Account. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.AccountApi();
let opts = {
  'page': 1, // Number | The page of a collection to return.
  'pageSize': 100 // Number | The number of items to return per page.
};
apiInstance.getPaymentMethods(opts, (error, data, response) => {
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
 **page** | **Number**| The page of a collection to return. | [optional] [default to 1]
 **pageSize** | **Number**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetPaymentMethods200Response**](GetPaymentMethods200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPayments

> GetPayments200Response getPayments(opts)

Payments List

Returns a paginated list of Payments made on this Account. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.AccountApi();
let opts = {
  'page': 1, // Number | The page of a collection to return.
  'pageSize': 100 // Number | The number of items to return per page.
};
apiInstance.getPayments(opts, (error, data, response) => {
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
 **page** | **Number**| The page of a collection to return. | [optional] [default to 1]
 **pageSize** | **Number**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetPayments200Response**](GetPayments200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getServiceTransfer

> ServiceTransfer getServiceTransfer(token)

Service Transfer View

Returns the details of the Service Transfer for the provided token.  While a transfer is pending, any unrestricted user *of any account* can access this command. After a transfer has been accepted, it can only be viewed by unrestricted users of the accounts that created and accepted the transfer. If cancelled or expired, only unrestricted users of the account that created the transfer can view it. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.AccountApi();
let token = "token_example"; // String | The UUID of the Service Transfer.
apiInstance.getServiceTransfer(token, (error, data, response) => {
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
 **token** | **String**| The UUID of the Service Transfer. | 

### Return type

[**ServiceTransfer**](ServiceTransfer.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getServiceTransfers

> GetServiceTransfers200Response getServiceTransfers(opts)

Service Transfers List

Returns a collection of all created and accepted Service Transfers for this account, regardless of the user that created or accepted the transfer.  This command can only be accessed by the unrestricted users of an account. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.AccountApi();
let opts = {
  'page': 1, // Number | The page of a collection to return.
  'pageSize': 100 // Number | The number of items to return per page.
};
apiInstance.getServiceTransfers(opts, (error, data, response) => {
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
 **page** | **Number**| The page of a collection to return. | [optional] [default to 1]
 **pageSize** | **Number**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetServiceTransfers200Response**](GetServiceTransfers200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTransfer

> Transfer getTransfer()

Network Utilization View

Returns a Transfer object showing your network utilization, in GB, for the current month. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.AccountApi();
apiInstance.getTransfer((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**Transfer**](Transfer.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUser

> User getUser(username)

User View

Returns information about a single User on your Account.  This command can only be accessed by the unrestricted users of an account. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.AccountApi();
let username = "username_example"; // String | The username to look up.
apiInstance.getUser(username, (error, data, response) => {
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
 **username** | **String**| The username to look up. | 

### Return type

[**User**](User.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUserGrants

> GrantsResponse getUserGrants(username)

User&#39;s Grants View

Returns the full grants structure for the specified account User (other than the account owner, see below for details). This includes all entities on the Account alongside the level of access this User has to each of them.  This command can only be accessed by the unrestricted users of an account.  The current authenticated User, including the account owner, may view their own grants at the [/profile/grants](/docs/api/profile/#grants-list) endpoint, but will not see entities that they do not have access to. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.AccountApi();
let username = "username_example"; // String | The username to look up.
apiInstance.getUserGrants(username, (error, data, response) => {
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
 **username** | **String**| The username to look up. | 

### Return type

[**GrantsResponse**](GrantsResponse.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUsers

> GetUsers200Response getUsers(opts)

Users List

Returns a paginated list of Users on your Account.  This command can only be accessed by the unrestricted users of an account.  Users may access all or part of your Account based on their restricted status and grants.  An unrestricted User may access everything on the account, whereas restricted User may only access entities or perform actions they&#39;ve been given specific grants to. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.AccountApi();
let opts = {
  'page': 1, // Number | The page of a collection to return.
  'pageSize': 100 // Number | The number of items to return per page.
};
apiInstance.getUsers(opts, (error, data, response) => {
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
 **page** | **Number**| The page of a collection to return. | [optional] [default to 1]
 **pageSize** | **Number**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetUsers200Response**](GetUsers200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## makePaymentMethodDefault

> Object makePaymentMethodDefault(paymentMethodId)

Payment Method Make Default

Make the specified Payment Method the default method for automatically processing payments.  Removes the default status from any other Payment Method. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.AccountApi();
let paymentMethodId = 56; // Number | The ID of the Payment Method to make default.
apiInstance.makePaymentMethodDefault(paymentMethodId, (error, data, response) => {
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
 **paymentMethodId** | **Number**| The ID of the Payment Method to make default. | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resetClientSecret

> OAuthClient resetClientSecret(clientId)

OAuth Client Secret Reset

Resets the OAuth Client secret for a client you own, and returns the OAuth Client with the plaintext secret. This secret is not supposed to be publicly known or disclosed anywhere. This can be used to generate a new secret in case the one you have has been leaked, or to get a new secret if you lost the original. The old secret is expired immediately, and logins to your client with the old secret will fail. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.AccountApi();
let clientId = "clientId_example"; // String | The OAuth Client ID to look up.
apiInstance.resetClientSecret(clientId, (error, data, response) => {
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
 **clientId** | **String**| The OAuth Client ID to look up. | 

### Return type

[**OAuthClient**](OAuthClient.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setClientThumbnail

> Object setClientThumbnail(clientId, body)

OAuth Client Thumbnail Update

Upload a thumbnail for a client you own.  You must upload an image file that will be returned when the thumbnail is retrieved.  This image will be publicly-viewable. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.AccountApi();
let clientId = "clientId_example"; // String | The OAuth Client ID to look up.
let body = "/path/to/file"; // File | The image to set as the thumbnail.
apiInstance.setClientThumbnail(clientId, body, (error, data, response) => {
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
 **clientId** | **String**| The OAuth Client ID to look up. | 
 **body** | **File**| The image to set as the thumbnail. | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: image/png
- **Accept**: application/json


## updateAccount

> Account updateAccount(account)

Account Update

Updates contact and billing information related to your Account. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.AccountApi();
let account = new LinodeApi.Account(); // Account | Update contact and billing information.  Account properties that are excluded from a request remain unchanged.  When updating an Account's `country` to \"US\", an error is returned if the Account's `zip` is not a valid US zip code. 
apiInstance.updateAccount(account, (error, data, response) => {
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
 **account** | [**Account**](Account.md)| Update contact and billing information.  Account properties that are excluded from a request remain unchanged.  When updating an Account&#39;s &#x60;country&#x60; to \&quot;US\&quot;, an error is returned if the Account&#39;s &#x60;zip&#x60; is not a valid US zip code.  | 

### Return type

[**Account**](Account.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateAccountSettings

> AccountSettings updateAccountSettings(accountSettings)

Account Settings Update

Updates your Account settings.  To update your Longview subscription plan, send a request to [Update Longview Plan](/docs/api/longview/#longview-plan-update). 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.AccountApi();
let accountSettings = new LinodeApi.AccountSettings(); // AccountSettings | Update Account settings information.
apiInstance.updateAccountSettings(accountSettings, (error, data, response) => {
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
 **accountSettings** | [**AccountSettings**](AccountSettings.md)| Update Account settings information. | 

### Return type

[**AccountSettings**](AccountSettings.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateClient

> OAuthClient updateClient(clientId, opts)

OAuth Client Update

Update information about an OAuth Client on your Account. This can be especially useful to update the &#x60;redirect_uri&#x60; of your client in the event that the callback url changed in your application. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.AccountApi();
let clientId = "clientId_example"; // String | The OAuth Client ID to look up.
let opts = {
  'oAuthClient': new LinodeApi.OAuthClient() // OAuthClient | The fields to update.
};
apiInstance.updateClient(clientId, opts, (error, data, response) => {
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
 **clientId** | **String**| The OAuth Client ID to look up. | 
 **oAuthClient** | [**OAuthClient**](OAuthClient.md)| The fields to update. | [optional] 

### Return type

[**OAuthClient**](OAuthClient.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateUser

> User updateUser(username, opts)

User Update

Update information about a User on your Account. This can be used to change the restricted status of a User. When making a User restricted, no grants will be configured by default and you must then set up grants in order for the User to access anything on the Account.  This command can only be accessed by the unrestricted users of an account. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.AccountApi();
let username = "username_example"; // String | The username to look up.
let opts = {
  'user': new LinodeApi.User() // User | The information to update.
};
apiInstance.updateUser(username, opts, (error, data, response) => {
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
 **username** | **String**| The username to look up. | 
 **user** | [**User**](User.md)| The information to update. | [optional] 

### Return type

[**User**](User.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateUserGrants

> GrantsResponse updateUserGrants(username, grantsResponse)

User&#39;s Grants Update

Update the grants a User has. This can be used to give a User access to new entities or actions, or take access away.  You do not need to include the grant for every entity on the Account in this request; any that are not included will remain unchanged.  This command can only be accessed by the unrestricted users of an account. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.AccountApi();
let username = "username_example"; // String | The username to look up.
let grantsResponse = new LinodeApi.GrantsResponse(); // GrantsResponse | The grants to update. Omitted grants will be left unchanged.
apiInstance.updateUserGrants(username, grantsResponse, (error, data, response) => {
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
 **username** | **String**| The username to look up. | 
 **grantsResponse** | [**GrantsResponse**](GrantsResponse.md)| The grants to update. Omitted grants will be left unchanged. | 

### Return type

[**GrantsResponse**](GrantsResponse.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

