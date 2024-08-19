# IncreaseApi.DefaultApi

All URIs are relative to *https://api.increase.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**actionARealTimeDecision**](DefaultApi.md#actionARealTimeDecision) | **POST** /real_time_decisions/{real_time_decision_id}/action | Action a Real-Time Decision
[**approveACheckTransfer**](DefaultApi.md#approveACheckTransfer) | **POST** /check_transfers/{check_transfer_id}/approve | Approve a Check Transfer
[**approveAWireTransfer**](DefaultApi.md#approveAWireTransfer) | **POST** /wire_transfers/{wire_transfer_id}/approve | Approve a Wire Transfer
[**approveAnAccountTransfer**](DefaultApi.md#approveAnAccountTransfer) | **POST** /account_transfers/{account_transfer_id}/approve | Approve an Account Transfer
[**approveAnAchTransfer**](DefaultApi.md#approveAnAchTransfer) | **POST** /ach_transfers/{ach_transfer_id}/approve | Approve an ACH Transfer
[**cancelAPendingAchTransfer**](DefaultApi.md#cancelAPendingAchTransfer) | **POST** /ach_transfers/{ach_transfer_id}/cancel | Cancel a pending ACH Transfer
[**cancelAPendingCheckTransfer**](DefaultApi.md#cancelAPendingCheckTransfer) | **POST** /check_transfers/{check_transfer_id}/cancel | Cancel a pending Check Transfer
[**cancelAPendingWireTransfer**](DefaultApi.md#cancelAPendingWireTransfer) | **POST** /wire_transfers/{wire_transfer_id}/cancel | Cancel a pending Wire Transfer
[**cancelAnAccountTransfer**](DefaultApi.md#cancelAnAccountTransfer) | **POST** /account_transfers/{account_transfer_id}/cancel | Cancel an Account Transfer
[**closeAnAccount**](DefaultApi.md#closeAnAccount) | **POST** /accounts/{account_id}/close | Close an Account
[**completeASandboxAccountTransfer**](DefaultApi.md#completeASandboxAccountTransfer) | **POST** /simulations/account_transfers/{account_transfer_id}/complete | Complete a Sandbox Account Transfer
[**completeASandboxRealTimePaymentsTransfer**](DefaultApi.md#completeASandboxRealTimePaymentsTransfer) | **POST** /simulations/real_time_payments_transfers/{real_time_payments_transfer_id}/complete | Complete a Sandbox Real Time Payments Transfer
[**createABookkeepingAccount**](DefaultApi.md#createABookkeepingAccount) | **POST** /bookkeeping_accounts | Create a Bookkeeping Account
[**createABookkeepingEntrySet**](DefaultApi.md#createABookkeepingEntrySet) | **POST** /bookkeeping_entry_sets | Create a Bookkeeping Entry Set
[**createACard**](DefaultApi.md#createACard) | **POST** /cards | Create a Card
[**createACardDispute**](DefaultApi.md#createACardDispute) | **POST** /card_disputes | Create a Card Dispute
[**createACardProfile**](DefaultApi.md#createACardProfile) | **POST** /card_profiles | Create a Card Profile
[**createACheckDeposit**](DefaultApi.md#createACheckDeposit) | **POST** /check_deposits | Create a Check Deposit
[**createACheckTransfer**](DefaultApi.md#createACheckTransfer) | **POST** /check_transfers | Create a Check Transfer
[**createAFile**](DefaultApi.md#createAFile) | **POST** /files | Create a File
[**createALimit**](DefaultApi.md#createALimit) | **POST** /limits | Create a Limit
[**createARealTimePaymentsTransfer**](DefaultApi.md#createARealTimePaymentsTransfer) | **POST** /real_time_payments_transfers | Create a Real Time Payments Transfer
[**createASupplementalDocumentForAnEntity**](DefaultApi.md#createASupplementalDocumentForAnEntity) | **POST** /entities/{entity_id}/supplemental_documents | Create a supplemental document for an Entity
[**createAWireDrawdownRequest**](DefaultApi.md#createAWireDrawdownRequest) | **POST** /wire_drawdown_requests | Create a Wire Drawdown Request
[**createAWireTransfer**](DefaultApi.md#createAWireTransfer) | **POST** /wire_transfers | Create a Wire Transfer
[**createAnAccount**](DefaultApi.md#createAnAccount) | **POST** /accounts | Create an Account
[**createAnAccountNumber**](DefaultApi.md#createAnAccountNumber) | **POST** /account_numbers | Create an Account Number
[**createAnAccountTransfer**](DefaultApi.md#createAnAccountTransfer) | **POST** /account_transfers | Create an Account Transfer
[**createAnAchPrenotification**](DefaultApi.md#createAnAchPrenotification) | **POST** /ach_prenotifications | Create an ACH Prenotification
[**createAnAchReturn**](DefaultApi.md#createAnAchReturn) | **POST** /inbound_ach_transfer_returns | Create an ACH Return
[**createAnAchTransfer**](DefaultApi.md#createAnAchTransfer) | **POST** /ach_transfers | Create an ACH Transfer
[**createAnEntity**](DefaultApi.md#createAnEntity) | **POST** /entities | Create an Entity
[**createAnEventSubscription**](DefaultApi.md#createAnEventSubscription) | **POST** /event_subscriptions | Create an Event Subscription
[**createAnExport**](DefaultApi.md#createAnExport) | **POST** /exports | Create an Export
[**createAnExternalAccount**](DefaultApi.md#createAnExternalAccount) | **POST** /external_accounts | Create an External Account
[**depositASandboxCheckTransfer**](DefaultApi.md#depositASandboxCheckTransfer) | **POST** /simulations/check_transfers/{check_transfer_id}/deposit | Deposit a Sandbox Check Transfer
[**listAccountNumbers**](DefaultApi.md#listAccountNumbers) | **GET** /account_numbers | List Account Numbers
[**listAccountStatements**](DefaultApi.md#listAccountStatements) | **GET** /account_statements | List Account Statements
[**listAccountTransfers**](DefaultApi.md#listAccountTransfers) | **GET** /account_transfers | List Account Transfers
[**listAccounts**](DefaultApi.md#listAccounts) | **GET** /accounts | List Accounts
[**listAchPrenotifications**](DefaultApi.md#listAchPrenotifications) | **GET** /ach_prenotifications | List ACH Prenotifications
[**listAchTransfers**](DefaultApi.md#listAchTransfers) | **GET** /ach_transfers | List ACH Transfers
[**listBookkeepingAccounts**](DefaultApi.md#listBookkeepingAccounts) | **GET** /bookkeeping_accounts | List Bookkeeping Accounts
[**listBookkeepingEntries**](DefaultApi.md#listBookkeepingEntries) | **GET** /bookkeeping_entries | List Bookkeeping Entries
[**listCardDisputes**](DefaultApi.md#listCardDisputes) | **GET** /card_disputes | List Card Disputes
[**listCardProfiles**](DefaultApi.md#listCardProfiles) | **GET** /card_profiles | List Card Profiles
[**listCards**](DefaultApi.md#listCards) | **GET** /cards | List Cards
[**listCheckDeposits**](DefaultApi.md#listCheckDeposits) | **GET** /check_deposits | List Check Deposits
[**listCheckTransfers**](DefaultApi.md#listCheckTransfers) | **GET** /check_transfers | List Check Transfers
[**listDeclinedTransactions**](DefaultApi.md#listDeclinedTransactions) | **GET** /declined_transactions | List Declined Transactions
[**listDigitalWalletTokens**](DefaultApi.md#listDigitalWalletTokens) | **GET** /digital_wallet_tokens | List Digital Wallet Tokens
[**listDocuments**](DefaultApi.md#listDocuments) | **GET** /documents | List Documents
[**listEntities**](DefaultApi.md#listEntities) | **GET** /entities | List Entities
[**listEventSubscriptions**](DefaultApi.md#listEventSubscriptions) | **GET** /event_subscriptions | List Event Subscriptions
[**listEvents**](DefaultApi.md#listEvents) | **GET** /events | List Events
[**listExports**](DefaultApi.md#listExports) | **GET** /exports | List Exports
[**listExternalAccounts**](DefaultApi.md#listExternalAccounts) | **GET** /external_accounts | List External Accounts
[**listFiles**](DefaultApi.md#listFiles) | **GET** /files | List Files
[**listInboundAchTransferReturns**](DefaultApi.md#listInboundAchTransferReturns) | **GET** /inbound_ach_transfer_returns | List Inbound ACH Transfer Returns
[**listInboundWireDrawdownRequests**](DefaultApi.md#listInboundWireDrawdownRequests) | **GET** /inbound_wire_drawdown_requests | List Inbound Wire Drawdown Requests
[**listLimits**](DefaultApi.md#listLimits) | **GET** /limits | List Limits
[**listOauthConnections**](DefaultApi.md#listOauthConnections) | **GET** /oauth_connections | List OAuth Connections
[**listPendingTransactions**](DefaultApi.md#listPendingTransactions) | **GET** /pending_transactions | List Pending Transactions
[**listPrograms**](DefaultApi.md#listPrograms) | **GET** /programs | List Programs
[**listRealTimePaymentsTransfers**](DefaultApi.md#listRealTimePaymentsTransfers) | **GET** /real_time_payments_transfers | List Real Time Payments Transfers
[**listRoutingNumbers**](DefaultApi.md#listRoutingNumbers) | **GET** /routing_numbers | List Routing Numbers
[**listTransactions**](DefaultApi.md#listTransactions) | **GET** /transactions | List Transactions
[**listWireDrawdownRequests**](DefaultApi.md#listWireDrawdownRequests) | **GET** /wire_drawdown_requests | List Wire Drawdown Requests
[**listWireTransfers**](DefaultApi.md#listWireTransfers) | **GET** /wire_transfers | List Wire Transfers
[**lookUpTheBalanceForAnAccount**](DefaultApi.md#lookUpTheBalanceForAnAccount) | **POST** /balance_lookups | Look up the balance for an Account
[**mailASandboxCheckTransfer**](DefaultApi.md#mailASandboxCheckTransfer) | **POST** /simulations/check_transfers/{check_transfer_id}/mail | Mail a Sandbox Check Transfer
[**rejectASandboxCheckDeposit**](DefaultApi.md#rejectASandboxCheckDeposit) | **POST** /simulations/check_deposits/{check_deposit_id}/reject | Reject a Sandbox Check Deposit
[**requestAStopPaymentOnACheckTransfer**](DefaultApi.md#requestAStopPaymentOnACheckTransfer) | **POST** /check_transfers/{check_transfer_id}/stop_payment | Request a stop payment on a Check Transfer
[**retrieveACard**](DefaultApi.md#retrieveACard) | **GET** /cards/{card_id} | Retrieve a Card
[**retrieveACardDispute**](DefaultApi.md#retrieveACardDispute) | **GET** /card_disputes/{card_dispute_id} | Retrieve a Card Dispute
[**retrieveACardProfile**](DefaultApi.md#retrieveACardProfile) | **GET** /card_profiles/{card_profile_id} | Retrieve a Card Profile
[**retrieveACheckDeposit**](DefaultApi.md#retrieveACheckDeposit) | **GET** /check_deposits/{check_deposit_id} | Retrieve a Check Deposit
[**retrieveACheckTransfer**](DefaultApi.md#retrieveACheckTransfer) | **GET** /check_transfers/{check_transfer_id} | Retrieve a Check Transfer
[**retrieveADeclinedTransaction**](DefaultApi.md#retrieveADeclinedTransaction) | **GET** /declined_transactions/{declined_transaction_id} | Retrieve a Declined Transaction
[**retrieveADigitalWalletToken**](DefaultApi.md#retrieveADigitalWalletToken) | **GET** /digital_wallet_tokens/{digital_wallet_token_id} | Retrieve a Digital Wallet Token
[**retrieveADocument**](DefaultApi.md#retrieveADocument) | **GET** /documents/{document_id} | Retrieve a Document
[**retrieveAFile**](DefaultApi.md#retrieveAFile) | **GET** /files/{file_id} | Retrieve a File
[**retrieveALimit**](DefaultApi.md#retrieveALimit) | **GET** /limits/{limit_id} | Retrieve a Limit
[**retrieveAPendingTransaction**](DefaultApi.md#retrieveAPendingTransaction) | **GET** /pending_transactions/{pending_transaction_id} | Retrieve a Pending Transaction
[**retrieveAProgram**](DefaultApi.md#retrieveAProgram) | **GET** /programs/{program_id} | Retrieve a Program
[**retrieveARealTimeDecision**](DefaultApi.md#retrieveARealTimeDecision) | **GET** /real_time_decisions/{real_time_decision_id} | Retrieve a Real-Time Decision
[**retrieveARealTimePaymentsTransfer**](DefaultApi.md#retrieveARealTimePaymentsTransfer) | **GET** /real_time_payments_transfers/{real_time_payments_transfer_id} | Retrieve a Real Time Payments Transfer
[**retrieveATransaction**](DefaultApi.md#retrieveATransaction) | **GET** /transactions/{transaction_id} | Retrieve a Transaction
[**retrieveAWireDrawdownRequest**](DefaultApi.md#retrieveAWireDrawdownRequest) | **GET** /wire_drawdown_requests/{wire_drawdown_request_id} | Retrieve a Wire Drawdown Request
[**retrieveAWireTransfer**](DefaultApi.md#retrieveAWireTransfer) | **GET** /wire_transfers/{wire_transfer_id} | Retrieve a Wire Transfer
[**retrieveAnAccount**](DefaultApi.md#retrieveAnAccount) | **GET** /accounts/{account_id} | Retrieve an Account
[**retrieveAnAccountNumber**](DefaultApi.md#retrieveAnAccountNumber) | **GET** /account_numbers/{account_number_id} | Retrieve an Account Number
[**retrieveAnAccountStatement**](DefaultApi.md#retrieveAnAccountStatement) | **GET** /account_statements/{account_statement_id} | Retrieve an Account Statement
[**retrieveAnAccountTransfer**](DefaultApi.md#retrieveAnAccountTransfer) | **GET** /account_transfers/{account_transfer_id} | Retrieve an Account Transfer
[**retrieveAnAchPrenotification**](DefaultApi.md#retrieveAnAchPrenotification) | **GET** /ach_prenotifications/{ach_prenotification_id} | Retrieve an ACH Prenotification
[**retrieveAnAchTransfer**](DefaultApi.md#retrieveAnAchTransfer) | **GET** /ach_transfers/{ach_transfer_id} | Retrieve an ACH Transfer
[**retrieveAnEntity**](DefaultApi.md#retrieveAnEntity) | **GET** /entities/{entity_id} | Retrieve an Entity
[**retrieveAnEvent**](DefaultApi.md#retrieveAnEvent) | **GET** /events/{event_id} | Retrieve an Event
[**retrieveAnEventSubscription**](DefaultApi.md#retrieveAnEventSubscription) | **GET** /event_subscriptions/{event_subscription_id} | Retrieve an Event Subscription
[**retrieveAnExport**](DefaultApi.md#retrieveAnExport) | **GET** /exports/{export_id} | Retrieve an Export
[**retrieveAnExternalAccount**](DefaultApi.md#retrieveAnExternalAccount) | **GET** /external_accounts/{external_account_id} | Retrieve an External Account
[**retrieveAnInboundAchTransferReturn**](DefaultApi.md#retrieveAnInboundAchTransferReturn) | **GET** /inbound_ach_transfer_returns/{inbound_ach_transfer_return_id} | Retrieve an Inbound ACH Transfer Return
[**retrieveAnInboundWireDrawdownRequest**](DefaultApi.md#retrieveAnInboundWireDrawdownRequest) | **GET** /inbound_wire_drawdown_requests/{inbound_wire_drawdown_request_id} | Retrieve an Inbound Wire Drawdown Request
[**retrieveAnOauthConnection**](DefaultApi.md#retrieveAnOauthConnection) | **GET** /oauth_connections/{oauth_connection_id} | Retrieve an OAuth Connection
[**retrieveGroupDetails**](DefaultApi.md#retrieveGroupDetails) | **GET** /groups/current | Retrieve Group details
[**retrieveSensitiveDetailsForACard**](DefaultApi.md#retrieveSensitiveDetailsForACard) | **GET** /cards/{card_id}/details | Retrieve sensitive details for a Card
[**returnASandboxAchTransfer**](DefaultApi.md#returnASandboxAchTransfer) | **POST** /simulations/ach_transfers/{ach_transfer_id}/return | Return a Sandbox ACH Transfer
[**returnASandboxCheckDeposit**](DefaultApi.md#returnASandboxCheckDeposit) | **POST** /simulations/check_deposits/{check_deposit_id}/return | Return a Sandbox Check Deposit
[**returnASandboxCheckTransfer**](DefaultApi.md#returnASandboxCheckTransfer) | **POST** /simulations/check_transfers/{check_transfer_id}/return | Return a Sandbox Check Transfer
[**reverseASandboxWireTransfer**](DefaultApi.md#reverseASandboxWireTransfer) | **POST** /simulations/wire_transfers/{wire_transfer_id}/reverse | Reverse a Sandbox Wire Transfer
[**simulateARealTimePaymentsTransferToYourAccount**](DefaultApi.md#simulateARealTimePaymentsTransferToYourAccount) | **POST** /simulations/inbound_real_time_payments_transfers | Simulate a Real Time Payments Transfer to your account
[**simulateARefundOnACard**](DefaultApi.md#simulateARefundOnACard) | **POST** /simulations/card_refunds | Simulate a refund on a card
[**simulateATaxDocumentBeingCreated**](DefaultApi.md#simulateATaxDocumentBeingCreated) | **POST** /simulations/documents | Simulate a tax document being created
[**simulateAWireTransferToYourAccount**](DefaultApi.md#simulateAWireTransferToYourAccount) | **POST** /simulations/inbound_wire_transfers | Simulate a Wire Transfer to your account
[**simulateAnAccountStatementBeingCreated**](DefaultApi.md#simulateAnAccountStatementBeingCreated) | **POST** /simulations/account_statements | Simulate an Account Statement being created
[**simulateAnAchTransferToYourAccount**](DefaultApi.md#simulateAnAchTransferToYourAccount) | **POST** /simulations/inbound_ach_transfers | Simulate an ACH Transfer to your account
[**simulateAnAuthorizationOnACard**](DefaultApi.md#simulateAnAuthorizationOnACard) | **POST** /simulations/card_authorizations | Simulate an authorization on a Card
[**simulateAnInboundWireDrawdownRequestBeingCreated**](DefaultApi.md#simulateAnInboundWireDrawdownRequestBeingCreated) | **POST** /simulations/inbound_wire_drawdown_requests | Simulate an Inbound Wire Drawdown request being created
[**simulateAnInterestPaymentToYourAccount**](DefaultApi.md#simulateAnInterestPaymentToYourAccount) | **POST** /simulations/interest_payment | Simulate an Interest Payment to your account
[**simulateDigitalWalletProvisioningForACard**](DefaultApi.md#simulateDigitalWalletProvisioningForACard) | **POST** /simulations/digital_wallet_token_requests | Simulate digital wallet provisioning for a card
[**simulateSettlingACardAuthorization**](DefaultApi.md#simulateSettlingACardAuthorization) | **POST** /simulations/card_settlements | Simulate settling a card authorization
[**simulatesAdvancingTheStateOfACardDispute**](DefaultApi.md#simulatesAdvancingTheStateOfACardDispute) | **POST** /simulations/card_disputes/{card_dispute_id}/action | Simulates advancing the state of a card dispute
[**submitASandboxAchTransfer**](DefaultApi.md#submitASandboxAchTransfer) | **POST** /simulations/ach_transfers/{ach_transfer_id}/submit | Submit a Sandbox ACH Transfer
[**submitASandboxCheckDeposit**](DefaultApi.md#submitASandboxCheckDeposit) | **POST** /simulations/check_deposits/{check_deposit_id}/submit | Submit a Sandbox Check Deposit
[**submitASandboxWireTransfer**](DefaultApi.md#submitASandboxWireTransfer) | **POST** /simulations/wire_transfers/{wire_transfer_id}/submit | Submit a Sandbox Wire Transfer
[**updateACard**](DefaultApi.md#updateACard) | **PATCH** /cards/{card_id} | Update a Card
[**updateALimit**](DefaultApi.md#updateALimit) | **PATCH** /limits/{limit_id} | Update a Limit
[**updateAnAccount**](DefaultApi.md#updateAnAccount) | **PATCH** /accounts/{account_id} | Update an Account
[**updateAnAccountNumber**](DefaultApi.md#updateAnAccountNumber) | **PATCH** /account_numbers/{account_number_id} | Update an Account Number
[**updateAnEventSubscription**](DefaultApi.md#updateAnEventSubscription) | **PATCH** /event_subscriptions/{event_subscription_id} | Update an Event Subscription
[**updateAnExternalAccount**](DefaultApi.md#updateAnExternalAccount) | **PATCH** /external_accounts/{external_account_id} | Update an External Account



## actionARealTimeDecision

> RealTimeDecision actionARealTimeDecision(realTimeDecisionId, actionARealTimeDecisionParameters)

Action a Real-Time Decision

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let realTimeDecisionId = "real_time_decision_j76n2e810ezcg3zh5qtn"; // String | 
let actionARealTimeDecisionParameters = new IncreaseApi.ActionARealTimeDecisionParameters(); // ActionARealTimeDecisionParameters | 
apiInstance.actionARealTimeDecision(realTimeDecisionId, actionARealTimeDecisionParameters, (error, data, response) => {
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
 **realTimeDecisionId** | **String**|  | 
 **actionARealTimeDecisionParameters** | [**ActionARealTimeDecisionParameters**](ActionARealTimeDecisionParameters.md)|  | 

### Return type

[**RealTimeDecision**](RealTimeDecision.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## approveACheckTransfer

> CheckTransfer approveACheckTransfer(checkTransferId)

Approve a Check Transfer

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let checkTransferId = "check_transfer_30b43acfu9vw8fyc4f5"; // String | 
apiInstance.approveACheckTransfer(checkTransferId, (error, data, response) => {
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
 **checkTransferId** | **String**|  | 

### Return type

[**CheckTransfer**](CheckTransfer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## approveAWireTransfer

> WireTransfer approveAWireTransfer(wireTransferId)

Approve a Wire Transfer

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let wireTransferId = "wire_transfer_5akynk7dqsq25qwk9q2u"; // String | 
apiInstance.approveAWireTransfer(wireTransferId, (error, data, response) => {
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
 **wireTransferId** | **String**|  | 

### Return type

[**WireTransfer**](WireTransfer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## approveAnAccountTransfer

> AccountTransfer approveAnAccountTransfer(accountTransferId)

Approve an Account Transfer

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let accountTransferId = "account_transfer_7k9qe1ysdgqztnt63l7n"; // String | 
apiInstance.approveAnAccountTransfer(accountTransferId, (error, data, response) => {
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
 **accountTransferId** | **String**|  | 

### Return type

[**AccountTransfer**](AccountTransfer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## approveAnAchTransfer

> AchTransfer approveAnAchTransfer(achTransferId)

Approve an ACH Transfer

Approves an ACH Transfer in a pending_approval state.

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let achTransferId = "ach_transfer_uoxatyh3lt5evrsdvo7q"; // String | 
apiInstance.approveAnAchTransfer(achTransferId, (error, data, response) => {
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
 **achTransferId** | **String**|  | 

### Return type

[**AchTransfer**](AchTransfer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cancelAPendingAchTransfer

> AchTransfer cancelAPendingAchTransfer(achTransferId)

Cancel a pending ACH Transfer

Cancels an ACH Transfer in a pending_approval state.

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let achTransferId = "ach_transfer_uoxatyh3lt5evrsdvo7q"; // String | 
apiInstance.cancelAPendingAchTransfer(achTransferId, (error, data, response) => {
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
 **achTransferId** | **String**|  | 

### Return type

[**AchTransfer**](AchTransfer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cancelAPendingCheckTransfer

> CheckTransfer cancelAPendingCheckTransfer(checkTransferId)

Cancel a pending Check Transfer

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let checkTransferId = "check_transfer_30b43acfu9vw8fyc4f5"; // String | 
apiInstance.cancelAPendingCheckTransfer(checkTransferId, (error, data, response) => {
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
 **checkTransferId** | **String**|  | 

### Return type

[**CheckTransfer**](CheckTransfer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cancelAPendingWireTransfer

> WireTransfer cancelAPendingWireTransfer(wireTransferId)

Cancel a pending Wire Transfer

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let wireTransferId = "wire_transfer_5akynk7dqsq25qwk9q2u"; // String | 
apiInstance.cancelAPendingWireTransfer(wireTransferId, (error, data, response) => {
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
 **wireTransferId** | **String**|  | 

### Return type

[**WireTransfer**](WireTransfer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cancelAnAccountTransfer

> AccountTransfer cancelAnAccountTransfer(accountTransferId)

Cancel an Account Transfer

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let accountTransferId = "account_transfer_7k9qe1ysdgqztnt63l7n"; // String | 
apiInstance.cancelAnAccountTransfer(accountTransferId, (error, data, response) => {
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
 **accountTransferId** | **String**|  | 

### Return type

[**AccountTransfer**](AccountTransfer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## closeAnAccount

> Account closeAnAccount(accountId)

Close an Account

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let accountId = "account_in71c4amph0vgo2qllky"; // String | 
apiInstance.closeAnAccount(accountId, (error, data, response) => {
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
 **accountId** | **String**|  | 

### Return type

[**Account**](Account.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## completeASandboxAccountTransfer

> AccountTransfer completeASandboxAccountTransfer(accountTransferId)

Complete a Sandbox Account Transfer

If your account is configured to require approval for each transfer, this endpoint simulates the approval of an [Account Transfer](#account-transfers). You can also approve sandbox Account Transfers in the dashboard. This transfer must first have a &#x60;status&#x60; of &#x60;pending_approval&#x60;.

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let accountTransferId = "account_transfer_7k9qe1ysdgqztnt63l7n"; // String | 
apiInstance.completeASandboxAccountTransfer(accountTransferId, (error, data, response) => {
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
 **accountTransferId** | **String**|  | 

### Return type

[**AccountTransfer**](AccountTransfer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## completeASandboxRealTimePaymentsTransfer

> RealTimePaymentsTransfer completeASandboxRealTimePaymentsTransfer(realTimePaymentsTransferId, completeASandboxRealTimePaymentsTransferParameters)

Complete a Sandbox Real Time Payments Transfer

Simulates submission of a Real Time Payments transfer and handling the response from the destination financial institution. This transfer must first have a &#x60;status&#x60; of &#x60;pending_submission&#x60;.

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let realTimePaymentsTransferId = "real_time_payments_transfer_iyuhl5kdn7ssmup83mvq"; // String | 
let completeASandboxRealTimePaymentsTransferParameters = new IncreaseApi.CompleteASandboxRealTimePaymentsTransferParameters(); // CompleteASandboxRealTimePaymentsTransferParameters | 
apiInstance.completeASandboxRealTimePaymentsTransfer(realTimePaymentsTransferId, completeASandboxRealTimePaymentsTransferParameters, (error, data, response) => {
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
 **realTimePaymentsTransferId** | **String**|  | 
 **completeASandboxRealTimePaymentsTransferParameters** | [**CompleteASandboxRealTimePaymentsTransferParameters**](CompleteASandboxRealTimePaymentsTransferParameters.md)|  | 

### Return type

[**RealTimePaymentsTransfer**](RealTimePaymentsTransfer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createABookkeepingAccount

> BookkeepingAccount createABookkeepingAccount(createABookkeepingAccountParameters)

Create a Bookkeeping Account

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let createABookkeepingAccountParameters = new IncreaseApi.CreateABookkeepingAccountParameters(); // CreateABookkeepingAccountParameters | 
apiInstance.createABookkeepingAccount(createABookkeepingAccountParameters, (error, data, response) => {
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
 **createABookkeepingAccountParameters** | [**CreateABookkeepingAccountParameters**](CreateABookkeepingAccountParameters.md)|  | 

### Return type

[**BookkeepingAccount**](BookkeepingAccount.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createABookkeepingEntrySet

> BookkeepingEntrySet createABookkeepingEntrySet(createABookkeepingEntrySetParameters)

Create a Bookkeeping Entry Set

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let createABookkeepingEntrySetParameters = new IncreaseApi.CreateABookkeepingEntrySetParameters(); // CreateABookkeepingEntrySetParameters | 
apiInstance.createABookkeepingEntrySet(createABookkeepingEntrySetParameters, (error, data, response) => {
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
 **createABookkeepingEntrySetParameters** | [**CreateABookkeepingEntrySetParameters**](CreateABookkeepingEntrySetParameters.md)|  | 

### Return type

[**BookkeepingEntrySet**](BookkeepingEntrySet.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createACard

> Card createACard(createACardParameters)

Create a Card

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let createACardParameters = new IncreaseApi.CreateACardParameters(); // CreateACardParameters | 
apiInstance.createACard(createACardParameters, (error, data, response) => {
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
 **createACardParameters** | [**CreateACardParameters**](CreateACardParameters.md)|  | 

### Return type

[**Card**](Card.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createACardDispute

> CardDispute createACardDispute(createACardDisputeParameters)

Create a Card Dispute

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let createACardDisputeParameters = new IncreaseApi.CreateACardDisputeParameters(); // CreateACardDisputeParameters | 
apiInstance.createACardDispute(createACardDisputeParameters, (error, data, response) => {
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
 **createACardDisputeParameters** | [**CreateACardDisputeParameters**](CreateACardDisputeParameters.md)|  | 

### Return type

[**CardDispute**](CardDispute.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createACardProfile

> CardProfile createACardProfile(createACardProfileParameters)

Create a Card Profile

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let createACardProfileParameters = new IncreaseApi.CreateACardProfileParameters(); // CreateACardProfileParameters | 
apiInstance.createACardProfile(createACardProfileParameters, (error, data, response) => {
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
 **createACardProfileParameters** | [**CreateACardProfileParameters**](CreateACardProfileParameters.md)|  | 

### Return type

[**CardProfile**](CardProfile.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createACheckDeposit

> CheckDeposit createACheckDeposit(createACheckDepositParameters)

Create a Check Deposit

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let createACheckDepositParameters = new IncreaseApi.CreateACheckDepositParameters(); // CreateACheckDepositParameters | 
apiInstance.createACheckDeposit(createACheckDepositParameters, (error, data, response) => {
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
 **createACheckDepositParameters** | [**CreateACheckDepositParameters**](CreateACheckDepositParameters.md)|  | 

### Return type

[**CheckDeposit**](CheckDeposit.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createACheckTransfer

> CheckTransfer createACheckTransfer(createACheckTransferParameters)

Create a Check Transfer

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let createACheckTransferParameters = new IncreaseApi.CreateACheckTransferParameters(); // CreateACheckTransferParameters | 
apiInstance.createACheckTransfer(createACheckTransferParameters, (error, data, response) => {
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
 **createACheckTransferParameters** | [**CreateACheckTransferParameters**](CreateACheckTransferParameters.md)|  | 

### Return type

[**CheckTransfer**](CheckTransfer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createAFile

> File createAFile(file, purpose, opts)

Create a File

To upload a file to Increase, you&#39;ll need to send a request of Content-Type &#x60;multipart/form-data&#x60;. The request should contain the file you would like to upload, as well as the parameters for creating a file.

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let file = "/path/to/file"; // File | The file contents. This should follow the specifications of [RFC 7578](https://datatracker.ietf.org/doc/html/rfc7578) which defines file transfers for the multipart/form-data protocol.
let purpose = "purpose_example"; // String | What the File will be used for in Increase's systems.
let opts = {
  'description': "description_example" // String | The description you choose to give the File.
};
apiInstance.createAFile(file, purpose, opts, (error, data, response) => {
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
 **file** | **File**| The file contents. This should follow the specifications of [RFC 7578](https://datatracker.ietf.org/doc/html/rfc7578) which defines file transfers for the multipart/form-data protocol. | 
 **purpose** | **String**| What the File will be used for in Increase&#39;s systems. | 
 **description** | **String**| The description you choose to give the File. | [optional] 

### Return type

**File**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## createALimit

> Limit createALimit(createALimitParameters)

Create a Limit

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let createALimitParameters = new IncreaseApi.CreateALimitParameters(); // CreateALimitParameters | 
apiInstance.createALimit(createALimitParameters, (error, data, response) => {
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
 **createALimitParameters** | [**CreateALimitParameters**](CreateALimitParameters.md)|  | 

### Return type

[**Limit**](Limit.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createARealTimePaymentsTransfer

> RealTimePaymentsTransfer createARealTimePaymentsTransfer(createARealTimePaymentsTransferParameters)

Create a Real Time Payments Transfer

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let createARealTimePaymentsTransferParameters = new IncreaseApi.CreateARealTimePaymentsTransferParameters(); // CreateARealTimePaymentsTransferParameters | 
apiInstance.createARealTimePaymentsTransfer(createARealTimePaymentsTransferParameters, (error, data, response) => {
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
 **createARealTimePaymentsTransferParameters** | [**CreateARealTimePaymentsTransferParameters**](CreateARealTimePaymentsTransferParameters.md)|  | 

### Return type

[**RealTimePaymentsTransfer**](RealTimePaymentsTransfer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createASupplementalDocumentForAnEntity

> Entity createASupplementalDocumentForAnEntity(entityId, createASupplementalDocumentForAnEntityParameters)

Create a supplemental document for an Entity

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let entityId = "entity_n8y8tnk2p9339ti393yi"; // String | 
let createASupplementalDocumentForAnEntityParameters = new IncreaseApi.CreateASupplementalDocumentForAnEntityParameters(); // CreateASupplementalDocumentForAnEntityParameters | 
apiInstance.createASupplementalDocumentForAnEntity(entityId, createASupplementalDocumentForAnEntityParameters, (error, data, response) => {
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
 **entityId** | **String**|  | 
 **createASupplementalDocumentForAnEntityParameters** | [**CreateASupplementalDocumentForAnEntityParameters**](CreateASupplementalDocumentForAnEntityParameters.md)|  | 

### Return type

[**Entity**](Entity.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createAWireDrawdownRequest

> WireDrawdownRequest createAWireDrawdownRequest(createAWireDrawdownRequestParameters)

Create a Wire Drawdown Request

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let createAWireDrawdownRequestParameters = new IncreaseApi.CreateAWireDrawdownRequestParameters(); // CreateAWireDrawdownRequestParameters | 
apiInstance.createAWireDrawdownRequest(createAWireDrawdownRequestParameters, (error, data, response) => {
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
 **createAWireDrawdownRequestParameters** | [**CreateAWireDrawdownRequestParameters**](CreateAWireDrawdownRequestParameters.md)|  | 

### Return type

[**WireDrawdownRequest**](WireDrawdownRequest.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createAWireTransfer

> WireTransfer createAWireTransfer(createAWireTransferParameters)

Create a Wire Transfer

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let createAWireTransferParameters = new IncreaseApi.CreateAWireTransferParameters(); // CreateAWireTransferParameters | 
apiInstance.createAWireTransfer(createAWireTransferParameters, (error, data, response) => {
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
 **createAWireTransferParameters** | [**CreateAWireTransferParameters**](CreateAWireTransferParameters.md)|  | 

### Return type

[**WireTransfer**](WireTransfer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createAnAccount

> Account createAnAccount(createAnAccountParameters)

Create an Account

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let createAnAccountParameters = new IncreaseApi.CreateAnAccountParameters(); // CreateAnAccountParameters | 
apiInstance.createAnAccount(createAnAccountParameters, (error, data, response) => {
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
 **createAnAccountParameters** | [**CreateAnAccountParameters**](CreateAnAccountParameters.md)|  | 

### Return type

[**Account**](Account.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createAnAccountNumber

> AccountNumber createAnAccountNumber(createAnAccountNumberParameters)

Create an Account Number

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let createAnAccountNumberParameters = new IncreaseApi.CreateAnAccountNumberParameters(); // CreateAnAccountNumberParameters | 
apiInstance.createAnAccountNumber(createAnAccountNumberParameters, (error, data, response) => {
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
 **createAnAccountNumberParameters** | [**CreateAnAccountNumberParameters**](CreateAnAccountNumberParameters.md)|  | 

### Return type

[**AccountNumber**](AccountNumber.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createAnAccountTransfer

> AccountTransfer createAnAccountTransfer(createAnAccountTransferParameters)

Create an Account Transfer

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let createAnAccountTransferParameters = new IncreaseApi.CreateAnAccountTransferParameters(); // CreateAnAccountTransferParameters | 
apiInstance.createAnAccountTransfer(createAnAccountTransferParameters, (error, data, response) => {
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
 **createAnAccountTransferParameters** | [**CreateAnAccountTransferParameters**](CreateAnAccountTransferParameters.md)|  | 

### Return type

[**AccountTransfer**](AccountTransfer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createAnAchPrenotification

> AchPrenotification createAnAchPrenotification(createAnAchPrenotificationParameters)

Create an ACH Prenotification

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let createAnAchPrenotificationParameters = new IncreaseApi.CreateAnAchPrenotificationParameters(); // CreateAnAchPrenotificationParameters | 
apiInstance.createAnAchPrenotification(createAnAchPrenotificationParameters, (error, data, response) => {
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
 **createAnAchPrenotificationParameters** | [**CreateAnAchPrenotificationParameters**](CreateAnAchPrenotificationParameters.md)|  | 

### Return type

[**AchPrenotification**](AchPrenotification.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createAnAchReturn

> InboundAchTransferReturn createAnAchReturn(createAnAchReturnParameters)

Create an ACH Return

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let createAnAchReturnParameters = new IncreaseApi.CreateAnAchReturnParameters(); // CreateAnAchReturnParameters | 
apiInstance.createAnAchReturn(createAnAchReturnParameters, (error, data, response) => {
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
 **createAnAchReturnParameters** | [**CreateAnAchReturnParameters**](CreateAnAchReturnParameters.md)|  | 

### Return type

[**InboundAchTransferReturn**](InboundAchTransferReturn.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createAnAchTransfer

> AchTransfer createAnAchTransfer(createAnAchTransferParameters)

Create an ACH Transfer

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let createAnAchTransferParameters = new IncreaseApi.CreateAnAchTransferParameters(); // CreateAnAchTransferParameters | 
apiInstance.createAnAchTransfer(createAnAchTransferParameters, (error, data, response) => {
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
 **createAnAchTransferParameters** | [**CreateAnAchTransferParameters**](CreateAnAchTransferParameters.md)|  | 

### Return type

[**AchTransfer**](AchTransfer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createAnEntity

> Entity createAnEntity(createAnEntityParameters)

Create an Entity

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let createAnEntityParameters = new IncreaseApi.CreateAnEntityParameters(); // CreateAnEntityParameters | 
apiInstance.createAnEntity(createAnEntityParameters, (error, data, response) => {
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
 **createAnEntityParameters** | [**CreateAnEntityParameters**](CreateAnEntityParameters.md)|  | 

### Return type

[**Entity**](Entity.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createAnEventSubscription

> EventSubscription createAnEventSubscription(createAnEventSubscriptionParameters)

Create an Event Subscription

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let createAnEventSubscriptionParameters = new IncreaseApi.CreateAnEventSubscriptionParameters(); // CreateAnEventSubscriptionParameters | 
apiInstance.createAnEventSubscription(createAnEventSubscriptionParameters, (error, data, response) => {
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
 **createAnEventSubscriptionParameters** | [**CreateAnEventSubscriptionParameters**](CreateAnEventSubscriptionParameters.md)|  | 

### Return type

[**EventSubscription**](EventSubscription.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createAnExport

> Export createAnExport(createAnExportParameters)

Create an Export

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let createAnExportParameters = new IncreaseApi.CreateAnExportParameters(); // CreateAnExportParameters | 
apiInstance.createAnExport(createAnExportParameters, (error, data, response) => {
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
 **createAnExportParameters** | [**CreateAnExportParameters**](CreateAnExportParameters.md)|  | 

### Return type

[**Export**](Export.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createAnExternalAccount

> ExternalAccount createAnExternalAccount(createAnExternalAccountParameters)

Create an External Account

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let createAnExternalAccountParameters = new IncreaseApi.CreateAnExternalAccountParameters(); // CreateAnExternalAccountParameters | 
apiInstance.createAnExternalAccount(createAnExternalAccountParameters, (error, data, response) => {
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
 **createAnExternalAccountParameters** | [**CreateAnExternalAccountParameters**](CreateAnExternalAccountParameters.md)|  | 

### Return type

[**ExternalAccount**](ExternalAccount.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## depositASandboxCheckTransfer

> CheckTransfer depositASandboxCheckTransfer(checkTransferId)

Deposit a Sandbox Check Transfer

Simulates a [Check Transfer](#check-transfers) being deposited at a bank. This transfer must first have a &#x60;status&#x60; of &#x60;mailed&#x60;.

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let checkTransferId = "check_transfer_30b43acfu9vw8fyc4f5"; // String | 
apiInstance.depositASandboxCheckTransfer(checkTransferId, (error, data, response) => {
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
 **checkTransferId** | **String**|  | 

### Return type

[**CheckTransfer**](CheckTransfer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAccountNumbers

> AccountNumberList listAccountNumbers(opts)

List Account Numbers

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let opts = {
  'cursor': "cursor_example", // String | 
  'limit': 56, // Number | 
  'status': "status_example", // String | 
  'accountId': "accountId_example", // String | 
  'createdAtAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'createdAtBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'createdAtOnOrAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'createdAtOnOrBefore': new Date("2013-10-20T19:20:30+01:00") // Date | 
};
apiInstance.listAccountNumbers(opts, (error, data, response) => {
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
 **cursor** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] 
 **status** | **String**|  | [optional] 
 **accountId** | **String**|  | [optional] 
 **createdAtAfter** | **Date**|  | [optional] 
 **createdAtBefore** | **Date**|  | [optional] 
 **createdAtOnOrAfter** | **Date**|  | [optional] 
 **createdAtOnOrBefore** | **Date**|  | [optional] 

### Return type

[**AccountNumberList**](AccountNumberList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAccountStatements

> AccountStatementList listAccountStatements(opts)

List Account Statements

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let opts = {
  'cursor': "cursor_example", // String | 
  'limit': 56, // Number | 
  'accountId': "account_in71c4amph0vgo2qllky", // String | 
  'statementPeriodStartAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'statementPeriodStartBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'statementPeriodStartOnOrAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'statementPeriodStartOnOrBefore': new Date("2013-10-20T19:20:30+01:00") // Date | 
};
apiInstance.listAccountStatements(opts, (error, data, response) => {
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
 **cursor** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] 
 **accountId** | **String**|  | [optional] 
 **statementPeriodStartAfter** | **Date**|  | [optional] 
 **statementPeriodStartBefore** | **Date**|  | [optional] 
 **statementPeriodStartOnOrAfter** | **Date**|  | [optional] 
 **statementPeriodStartOnOrBefore** | **Date**|  | [optional] 

### Return type

[**AccountStatementList**](AccountStatementList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAccountTransfers

> AccountTransferList listAccountTransfers(opts)

List Account Transfers

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let opts = {
  'cursor': "cursor_example", // String | 
  'limit': 56, // Number | 
  'accountId': "account_in71c4amph0vgo2qllky", // String | 
  'createdAtAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'createdAtBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'createdAtOnOrAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'createdAtOnOrBefore': new Date("2013-10-20T19:20:30+01:00") // Date | 
};
apiInstance.listAccountTransfers(opts, (error, data, response) => {
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
 **cursor** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] 
 **accountId** | **String**|  | [optional] 
 **createdAtAfter** | **Date**|  | [optional] 
 **createdAtBefore** | **Date**|  | [optional] 
 **createdAtOnOrAfter** | **Date**|  | [optional] 
 **createdAtOnOrBefore** | **Date**|  | [optional] 

### Return type

[**AccountTransferList**](AccountTransferList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAccounts

> AccountList listAccounts(opts)

List Accounts

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let opts = {
  'cursor': "cursor_example", // String | 
  'limit': 56, // Number | 
  'entityId': "entity_n8y8tnk2p9339ti393yi", // String | 
  'status': "status_example", // String | 
  'createdAtAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'createdAtBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'createdAtOnOrAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'createdAtOnOrBefore': new Date("2013-10-20T19:20:30+01:00") // Date | 
};
apiInstance.listAccounts(opts, (error, data, response) => {
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
 **cursor** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] 
 **entityId** | **String**|  | [optional] 
 **status** | **String**|  | [optional] 
 **createdAtAfter** | **Date**|  | [optional] 
 **createdAtBefore** | **Date**|  | [optional] 
 **createdAtOnOrAfter** | **Date**|  | [optional] 
 **createdAtOnOrBefore** | **Date**|  | [optional] 

### Return type

[**AccountList**](AccountList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAchPrenotifications

> AchPrenotificationList listAchPrenotifications(opts)

List ACH Prenotifications

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let opts = {
  'cursor': "cursor_example", // String | 
  'limit': 56, // Number | 
  'createdAtAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'createdAtBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'createdAtOnOrAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'createdAtOnOrBefore': new Date("2013-10-20T19:20:30+01:00") // Date | 
};
apiInstance.listAchPrenotifications(opts, (error, data, response) => {
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
 **cursor** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] 
 **createdAtAfter** | **Date**|  | [optional] 
 **createdAtBefore** | **Date**|  | [optional] 
 **createdAtOnOrAfter** | **Date**|  | [optional] 
 **createdAtOnOrBefore** | **Date**|  | [optional] 

### Return type

[**AchPrenotificationList**](AchPrenotificationList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAchTransfers

> AchTransferList listAchTransfers(opts)

List ACH Transfers

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let opts = {
  'cursor': "cursor_example", // String | 
  'limit': 56, // Number | 
  'accountId': "account_in71c4amph0vgo2qllky", // String | 
  'externalAccountId': "externalAccountId_example", // String | 
  'createdAtAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'createdAtBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'createdAtOnOrAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'createdAtOnOrBefore': new Date("2013-10-20T19:20:30+01:00") // Date | 
};
apiInstance.listAchTransfers(opts, (error, data, response) => {
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
 **cursor** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] 
 **accountId** | **String**|  | [optional] 
 **externalAccountId** | **String**|  | [optional] 
 **createdAtAfter** | **Date**|  | [optional] 
 **createdAtBefore** | **Date**|  | [optional] 
 **createdAtOnOrAfter** | **Date**|  | [optional] 
 **createdAtOnOrBefore** | **Date**|  | [optional] 

### Return type

[**AchTransferList**](AchTransferList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listBookkeepingAccounts

> BookkeepingAccountList listBookkeepingAccounts(opts)

List Bookkeeping Accounts

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let opts = {
  'cursor': "cursor_example", // String | 
  'limit': 56 // Number | 
};
apiInstance.listBookkeepingAccounts(opts, (error, data, response) => {
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
 **cursor** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] 

### Return type

[**BookkeepingAccountList**](BookkeepingAccountList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listBookkeepingEntries

> BookkeepingEntryList listBookkeepingEntries(opts)

List Bookkeeping Entries

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let opts = {
  'cursor': "cursor_example", // String | 
  'limit': 56 // Number | 
};
apiInstance.listBookkeepingEntries(opts, (error, data, response) => {
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
 **cursor** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] 

### Return type

[**BookkeepingEntryList**](BookkeepingEntryList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listCardDisputes

> CardDisputeList listCardDisputes(opts)

List Card Disputes

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let opts = {
  'cursor': "cursor_example", // String | 
  'limit': 56, // Number | 
  'createdAtAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'createdAtBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'createdAtOnOrAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'createdAtOnOrBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'statusIn': ["null"] // [String] | 
};
apiInstance.listCardDisputes(opts, (error, data, response) => {
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
 **cursor** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] 
 **createdAtAfter** | **Date**|  | [optional] 
 **createdAtBefore** | **Date**|  | [optional] 
 **createdAtOnOrAfter** | **Date**|  | [optional] 
 **createdAtOnOrBefore** | **Date**|  | [optional] 
 **statusIn** | [**[String]**](String.md)|  | [optional] 

### Return type

[**CardDisputeList**](CardDisputeList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listCardProfiles

> CardProfileList listCardProfiles(opts)

List Card Profiles

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let opts = {
  'cursor': "cursor_example", // String | 
  'limit': 56, // Number | 
  'statusIn': ["null"] // [String] | 
};
apiInstance.listCardProfiles(opts, (error, data, response) => {
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
 **cursor** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] 
 **statusIn** | [**[String]**](String.md)|  | [optional] 

### Return type

[**CardProfileList**](CardProfileList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listCards

> CardList listCards(opts)

List Cards

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let opts = {
  'cursor': "cursor_example", // String | 
  'limit': 56, // Number | 
  'accountId': "account_in71c4amph0vgo2qllky", // String | 
  'createdAtAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'createdAtBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'createdAtOnOrAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'createdAtOnOrBefore': new Date("2013-10-20T19:20:30+01:00") // Date | 
};
apiInstance.listCards(opts, (error, data, response) => {
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
 **cursor** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] 
 **accountId** | **String**|  | [optional] 
 **createdAtAfter** | **Date**|  | [optional] 
 **createdAtBefore** | **Date**|  | [optional] 
 **createdAtOnOrAfter** | **Date**|  | [optional] 
 **createdAtOnOrBefore** | **Date**|  | [optional] 

### Return type

[**CardList**](CardList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listCheckDeposits

> CheckDepositList listCheckDeposits(opts)

List Check Deposits

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let opts = {
  'cursor': "cursor_example", // String | 
  'limit': 56, // Number | 
  'accountId': "account_in71c4amph0vgo2qllky", // String | 
  'createdAtAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'createdAtBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'createdAtOnOrAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'createdAtOnOrBefore': new Date("2013-10-20T19:20:30+01:00") // Date | 
};
apiInstance.listCheckDeposits(opts, (error, data, response) => {
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
 **cursor** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] 
 **accountId** | **String**|  | [optional] 
 **createdAtAfter** | **Date**|  | [optional] 
 **createdAtBefore** | **Date**|  | [optional] 
 **createdAtOnOrAfter** | **Date**|  | [optional] 
 **createdAtOnOrBefore** | **Date**|  | [optional] 

### Return type

[**CheckDepositList**](CheckDepositList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listCheckTransfers

> CheckTransferList listCheckTransfers(opts)

List Check Transfers

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let opts = {
  'cursor': "cursor_example", // String | 
  'limit': 56, // Number | 
  'accountId': "account_in71c4amph0vgo2qllky", // String | 
  'createdAtAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'createdAtBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'createdAtOnOrAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'createdAtOnOrBefore': new Date("2013-10-20T19:20:30+01:00") // Date | 
};
apiInstance.listCheckTransfers(opts, (error, data, response) => {
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
 **cursor** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] 
 **accountId** | **String**|  | [optional] 
 **createdAtAfter** | **Date**|  | [optional] 
 **createdAtBefore** | **Date**|  | [optional] 
 **createdAtOnOrAfter** | **Date**|  | [optional] 
 **createdAtOnOrBefore** | **Date**|  | [optional] 

### Return type

[**CheckTransferList**](CheckTransferList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listDeclinedTransactions

> DeclinedTransactionList listDeclinedTransactions(opts)

List Declined Transactions

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let opts = {
  'cursor': "cursor_example", // String | 
  'limit': 56, // Number | 
  'accountId': "accountId_example", // String | 
  'createdAtAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'createdAtBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'createdAtOnOrAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'createdAtOnOrBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'routeId': "routeId_example" // String | 
};
apiInstance.listDeclinedTransactions(opts, (error, data, response) => {
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
 **cursor** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] 
 **accountId** | **String**|  | [optional] 
 **createdAtAfter** | **Date**|  | [optional] 
 **createdAtBefore** | **Date**|  | [optional] 
 **createdAtOnOrAfter** | **Date**|  | [optional] 
 **createdAtOnOrBefore** | **Date**|  | [optional] 
 **routeId** | **String**|  | [optional] 

### Return type

[**DeclinedTransactionList**](DeclinedTransactionList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listDigitalWalletTokens

> DigitalWalletTokenList listDigitalWalletTokens(opts)

List Digital Wallet Tokens

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let opts = {
  'cursor': "cursor_example", // String | 
  'limit': 56, // Number | 
  'cardId': "card_oubs0hwk5rn6knuecxg2", // String | 
  'createdAtAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'createdAtBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'createdAtOnOrAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'createdAtOnOrBefore': new Date("2013-10-20T19:20:30+01:00") // Date | 
};
apiInstance.listDigitalWalletTokens(opts, (error, data, response) => {
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
 **cursor** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] 
 **cardId** | **String**|  | [optional] 
 **createdAtAfter** | **Date**|  | [optional] 
 **createdAtBefore** | **Date**|  | [optional] 
 **createdAtOnOrAfter** | **Date**|  | [optional] 
 **createdAtOnOrBefore** | **Date**|  | [optional] 

### Return type

[**DigitalWalletTokenList**](DigitalWalletTokenList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listDocuments

> DocumentList listDocuments(opts)

List Documents

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let opts = {
  'cursor': "cursor_example", // String | 
  'limit': 56, // Number | 
  'entityId': "entityId_example", // String | 
  'categoryIn': ["null"], // [String] | 
  'createdAtAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'createdAtBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'createdAtOnOrAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'createdAtOnOrBefore': new Date("2013-10-20T19:20:30+01:00") // Date | 
};
apiInstance.listDocuments(opts, (error, data, response) => {
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
 **cursor** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] 
 **entityId** | **String**|  | [optional] 
 **categoryIn** | [**[String]**](String.md)|  | [optional] 
 **createdAtAfter** | **Date**|  | [optional] 
 **createdAtBefore** | **Date**|  | [optional] 
 **createdAtOnOrAfter** | **Date**|  | [optional] 
 **createdAtOnOrBefore** | **Date**|  | [optional] 

### Return type

[**DocumentList**](DocumentList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listEntities

> EntityList listEntities(opts)

List Entities

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let opts = {
  'cursor': "cursor_example", // String | 
  'limit': 56, // Number | 
  'createdAtAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'createdAtBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'createdAtOnOrAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'createdAtOnOrBefore': new Date("2013-10-20T19:20:30+01:00") // Date | 
};
apiInstance.listEntities(opts, (error, data, response) => {
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
 **cursor** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] 
 **createdAtAfter** | **Date**|  | [optional] 
 **createdAtBefore** | **Date**|  | [optional] 
 **createdAtOnOrAfter** | **Date**|  | [optional] 
 **createdAtOnOrBefore** | **Date**|  | [optional] 

### Return type

[**EntityList**](EntityList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listEventSubscriptions

> EventSubscriptionList listEventSubscriptions(opts)

List Event Subscriptions

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let opts = {
  'cursor': "cursor_example", // String | 
  'limit': 56 // Number | 
};
apiInstance.listEventSubscriptions(opts, (error, data, response) => {
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
 **cursor** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] 

### Return type

[**EventSubscriptionList**](EventSubscriptionList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listEvents

> EventList listEvents(opts)

List Events

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let opts = {
  'cursor': "cursor_example", // String | 
  'limit': 56, // Number | 
  'createdAtAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'createdAtBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'createdAtOnOrAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'createdAtOnOrBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'categoryIn': ["null"], // [String] | 
  'associatedObjectId': "associatedObjectId_example" // String | 
};
apiInstance.listEvents(opts, (error, data, response) => {
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
 **cursor** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] 
 **createdAtAfter** | **Date**|  | [optional] 
 **createdAtBefore** | **Date**|  | [optional] 
 **createdAtOnOrAfter** | **Date**|  | [optional] 
 **createdAtOnOrBefore** | **Date**|  | [optional] 
 **categoryIn** | [**[String]**](String.md)|  | [optional] 
 **associatedObjectId** | **String**|  | [optional] 

### Return type

[**EventList**](EventList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listExports

> ExportList listExports(opts)

List Exports

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let opts = {
  'cursor': "cursor_example", // String | 
  'limit': 56 // Number | 
};
apiInstance.listExports(opts, (error, data, response) => {
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
 **cursor** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] 

### Return type

[**ExportList**](ExportList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listExternalAccounts

> ExternalAccountList listExternalAccounts(opts)

List External Accounts

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let opts = {
  'cursor': "cursor_example", // String | 
  'limit': 56, // Number | 
  'statusIn': ["null"] // [String] | 
};
apiInstance.listExternalAccounts(opts, (error, data, response) => {
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
 **cursor** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] 
 **statusIn** | [**[String]**](String.md)|  | [optional] 

### Return type

[**ExternalAccountList**](ExternalAccountList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listFiles

> FileList listFiles(opts)

List Files

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let opts = {
  'cursor': "cursor_example", // String | 
  'limit': 56, // Number | 
  'createdAtAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'createdAtBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'createdAtOnOrAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'createdAtOnOrBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'purposeIn': ["null"] // [String] | 
};
apiInstance.listFiles(opts, (error, data, response) => {
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
 **cursor** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] 
 **createdAtAfter** | **Date**|  | [optional] 
 **createdAtBefore** | **Date**|  | [optional] 
 **createdAtOnOrAfter** | **Date**|  | [optional] 
 **createdAtOnOrBefore** | **Date**|  | [optional] 
 **purposeIn** | [**[String]**](String.md)|  | [optional] 

### Return type

[**FileList**](FileList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listInboundAchTransferReturns

> InboundAchTransferReturnList listInboundAchTransferReturns(opts)

List Inbound ACH Transfer Returns

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let opts = {
  'cursor': "cursor_example", // String | 
  'limit': 56 // Number | 
};
apiInstance.listInboundAchTransferReturns(opts, (error, data, response) => {
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
 **cursor** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] 

### Return type

[**InboundAchTransferReturnList**](InboundAchTransferReturnList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listInboundWireDrawdownRequests

> InboundWireDrawdownRequestList listInboundWireDrawdownRequests(opts)

List Inbound Wire Drawdown Requests

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let opts = {
  'cursor': "cursor_example", // String | 
  'limit': 56 // Number | 
};
apiInstance.listInboundWireDrawdownRequests(opts, (error, data, response) => {
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
 **cursor** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] 

### Return type

[**InboundWireDrawdownRequestList**](InboundWireDrawdownRequestList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listLimits

> LimitList listLimits(opts)

List Limits

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let opts = {
  'cursor': "cursor_example", // String | 
  'limit': 56, // Number | 
  'modelId': "account_number_v18nkfqm6afpsrvy82b2", // String | 
  'status': "active" // String | 
};
apiInstance.listLimits(opts, (error, data, response) => {
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
 **cursor** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] 
 **modelId** | **String**|  | [optional] 
 **status** | **String**|  | [optional] 

### Return type

[**LimitList**](LimitList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listOauthConnections

> OauthConnectionList listOauthConnections(opts)

List OAuth Connections

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let opts = {
  'cursor': "cursor_example", // String | 
  'limit': 56 // Number | 
};
apiInstance.listOauthConnections(opts, (error, data, response) => {
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
 **cursor** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] 

### Return type

[**OauthConnectionList**](OauthConnectionList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listPendingTransactions

> PendingTransactionList listPendingTransactions(opts)

List Pending Transactions

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let opts = {
  'cursor': "cursor_example", // String | 
  'limit': 56, // Number | 
  'accountId': "accountId_example", // String | 
  'routeId': "routeId_example", // String | 
  'sourceId': "sourceId_example", // String | 
  'statusIn': ["null"], // [String] | 
  'createdAtAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'createdAtBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'createdAtOnOrAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'createdAtOnOrBefore': new Date("2013-10-20T19:20:30+01:00") // Date | 
};
apiInstance.listPendingTransactions(opts, (error, data, response) => {
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
 **cursor** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] 
 **accountId** | **String**|  | [optional] 
 **routeId** | **String**|  | [optional] 
 **sourceId** | **String**|  | [optional] 
 **statusIn** | [**[String]**](String.md)|  | [optional] 
 **createdAtAfter** | **Date**|  | [optional] 
 **createdAtBefore** | **Date**|  | [optional] 
 **createdAtOnOrAfter** | **Date**|  | [optional] 
 **createdAtOnOrBefore** | **Date**|  | [optional] 

### Return type

[**PendingTransactionList**](PendingTransactionList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listPrograms

> ProgramList listPrograms(opts)

List Programs

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let opts = {
  'cursor': "cursor_example", // String | 
  'limit': 56 // Number | 
};
apiInstance.listPrograms(opts, (error, data, response) => {
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
 **cursor** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] 

### Return type

[**ProgramList**](ProgramList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listRealTimePaymentsTransfers

> RealTimePaymentsTransferList listRealTimePaymentsTransfers(opts)

List Real Time Payments Transfers

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let opts = {
  'cursor': "cursor_example", // String | 
  'limit': 56, // Number | 
  'accountId': "account_in71c4amph0vgo2qllky", // String | 
  'externalAccountId': "externalAccountId_example", // String | 
  'createdAtAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'createdAtBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'createdAtOnOrAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'createdAtOnOrBefore': new Date("2013-10-20T19:20:30+01:00") // Date | 
};
apiInstance.listRealTimePaymentsTransfers(opts, (error, data, response) => {
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
 **cursor** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] 
 **accountId** | **String**|  | [optional] 
 **externalAccountId** | **String**|  | [optional] 
 **createdAtAfter** | **Date**|  | [optional] 
 **createdAtBefore** | **Date**|  | [optional] 
 **createdAtOnOrAfter** | **Date**|  | [optional] 
 **createdAtOnOrBefore** | **Date**|  | [optional] 

### Return type

[**RealTimePaymentsTransferList**](RealTimePaymentsTransferList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listRoutingNumbers

> RoutingNumberList listRoutingNumbers(routingNumber, opts)

List Routing Numbers

You can use this API to confirm if a routing number is valid, such as when a user is providing you with bank account details. Since routing numbers uniquely identify a bank, this will always return 0 or 1 entry. In Sandbox, the only valid routing number for this method is 110000000.

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let routingNumber = "021000021"; // String | 
let opts = {
  'cursor': "cursor_example", // String | 
  'limit': 56 // Number | 
};
apiInstance.listRoutingNumbers(routingNumber, opts, (error, data, response) => {
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
 **routingNumber** | **String**|  | 
 **cursor** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] 

### Return type

[**RoutingNumberList**](RoutingNumberList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTransactions

> TransactionList listTransactions(opts)

List Transactions

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let opts = {
  'cursor': "cursor_example", // String | 
  'limit': 56, // Number | 
  'accountId': "accountId_example", // String | 
  'createdAtAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'createdAtBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'createdAtOnOrAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'createdAtOnOrBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'categoryIn': ["null"], // [String] | 
  'routeId': "routeId_example" // String | 
};
apiInstance.listTransactions(opts, (error, data, response) => {
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
 **cursor** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] 
 **accountId** | **String**|  | [optional] 
 **createdAtAfter** | **Date**|  | [optional] 
 **createdAtBefore** | **Date**|  | [optional] 
 **createdAtOnOrAfter** | **Date**|  | [optional] 
 **createdAtOnOrBefore** | **Date**|  | [optional] 
 **categoryIn** | [**[String]**](String.md)|  | [optional] 
 **routeId** | **String**|  | [optional] 

### Return type

[**TransactionList**](TransactionList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listWireDrawdownRequests

> WireDrawdownRequestList listWireDrawdownRequests(opts)

List Wire Drawdown Requests

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let opts = {
  'cursor': "cursor_example", // String | 
  'limit': 56 // Number | 
};
apiInstance.listWireDrawdownRequests(opts, (error, data, response) => {
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
 **cursor** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] 

### Return type

[**WireDrawdownRequestList**](WireDrawdownRequestList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listWireTransfers

> WireTransferList listWireTransfers(opts)

List Wire Transfers

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let opts = {
  'cursor': "cursor_example", // String | 
  'limit': 56, // Number | 
  'accountId': "account_in71c4amph0vgo2qllky", // String | 
  'externalAccountId': "externalAccountId_example", // String | 
  'createdAtAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'createdAtBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'createdAtOnOrAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'createdAtOnOrBefore': new Date("2013-10-20T19:20:30+01:00") // Date | 
};
apiInstance.listWireTransfers(opts, (error, data, response) => {
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
 **cursor** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] 
 **accountId** | **String**|  | [optional] 
 **externalAccountId** | **String**|  | [optional] 
 **createdAtAfter** | **Date**|  | [optional] 
 **createdAtBefore** | **Date**|  | [optional] 
 **createdAtOnOrAfter** | **Date**|  | [optional] 
 **createdAtOnOrBefore** | **Date**|  | [optional] 

### Return type

[**WireTransferList**](WireTransferList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## lookUpTheBalanceForAnAccount

> BalanceLookup lookUpTheBalanceForAnAccount(lookUpTheBalanceForAnAccountParameters)

Look up the balance for an Account

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let lookUpTheBalanceForAnAccountParameters = new IncreaseApi.LookUpTheBalanceForAnAccountParameters(); // LookUpTheBalanceForAnAccountParameters | 
apiInstance.lookUpTheBalanceForAnAccount(lookUpTheBalanceForAnAccountParameters, (error, data, response) => {
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
 **lookUpTheBalanceForAnAccountParameters** | [**LookUpTheBalanceForAnAccountParameters**](LookUpTheBalanceForAnAccountParameters.md)|  | 

### Return type

[**BalanceLookup**](BalanceLookup.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## mailASandboxCheckTransfer

> CheckTransfer mailASandboxCheckTransfer(checkTransferId)

Mail a Sandbox Check Transfer

Simulates the mailing of a [Check Transfer](#check-transfers), which happens once per weekday in production but can be sped up in sandbox. This transfer must first have a &#x60;status&#x60; of &#x60;pending_approval&#x60; or &#x60;pending_submission&#x60;.

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let checkTransferId = "check_transfer_30b43acfu9vw8fyc4f5"; // String | 
apiInstance.mailASandboxCheckTransfer(checkTransferId, (error, data, response) => {
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
 **checkTransferId** | **String**|  | 

### Return type

[**CheckTransfer**](CheckTransfer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## rejectASandboxCheckDeposit

> CheckDeposit rejectASandboxCheckDeposit(checkDepositId)

Reject a Sandbox Check Deposit

Simulates the rejection of a [Check Deposit](#check-deposits) by Increase due to factors like poor image quality. This Check Deposit must first have a &#x60;status&#x60; of &#x60;pending&#x60;.

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let checkDepositId = "check_deposit_f06n9gpg7sxn8t19lfc1"; // String | 
apiInstance.rejectASandboxCheckDeposit(checkDepositId, (error, data, response) => {
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
 **checkDepositId** | **String**|  | 

### Return type

[**CheckDeposit**](CheckDeposit.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestAStopPaymentOnACheckTransfer

> CheckTransfer requestAStopPaymentOnACheckTransfer(checkTransferId)

Request a stop payment on a Check Transfer

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let checkTransferId = "check_transfer_30b43acfu9vw8fyc4f5"; // String | 
apiInstance.requestAStopPaymentOnACheckTransfer(checkTransferId, (error, data, response) => {
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
 **checkTransferId** | **String**|  | 

### Return type

[**CheckTransfer**](CheckTransfer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveACard

> Card retrieveACard(cardId)

Retrieve a Card

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let cardId = "card_oubs0hwk5rn6knuecxg2"; // String | 
apiInstance.retrieveACard(cardId, (error, data, response) => {
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
 **cardId** | **String**|  | 

### Return type

[**Card**](Card.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveACardDispute

> CardDispute retrieveACardDispute(cardDisputeId)

Retrieve a Card Dispute

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let cardDisputeId = "card_dispute_h9sc95nbl1cgltpp7men"; // String | 
apiInstance.retrieveACardDispute(cardDisputeId, (error, data, response) => {
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
 **cardDisputeId** | **String**|  | 

### Return type

[**CardDispute**](CardDispute.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveACardProfile

> CardProfile retrieveACardProfile(cardProfileId)

Retrieve a Card Profile

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let cardProfileId = "card_profile_cox5y73lob2eqly18piy"; // String | 
apiInstance.retrieveACardProfile(cardProfileId, (error, data, response) => {
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
 **cardProfileId** | **String**|  | 

### Return type

[**CardProfile**](CardProfile.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveACheckDeposit

> CheckDeposit retrieveACheckDeposit(checkDepositId)

Retrieve a Check Deposit

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let checkDepositId = "check_deposit_instruction_q2shv7x9qhevfm71kor8"; // String | 
apiInstance.retrieveACheckDeposit(checkDepositId, (error, data, response) => {
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
 **checkDepositId** | **String**|  | 

### Return type

[**CheckDeposit**](CheckDeposit.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveACheckTransfer

> CheckTransfer retrieveACheckTransfer(checkTransferId)

Retrieve a Check Transfer

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let checkTransferId = "check_transfer_30b43acfu9vw8fyc4f5"; // String | 
apiInstance.retrieveACheckTransfer(checkTransferId, (error, data, response) => {
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
 **checkTransferId** | **String**|  | 

### Return type

[**CheckTransfer**](CheckTransfer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveADeclinedTransaction

> DeclinedTransaction retrieveADeclinedTransaction(declinedTransactionId)

Retrieve a Declined Transaction

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let declinedTransactionId = "declined_transaction_17jbn0yyhvkt4v4ooym8"; // String | 
apiInstance.retrieveADeclinedTransaction(declinedTransactionId, (error, data, response) => {
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
 **declinedTransactionId** | **String**|  | 

### Return type

[**DeclinedTransaction**](DeclinedTransaction.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveADigitalWalletToken

> DigitalWalletToken retrieveADigitalWalletToken(digitalWalletTokenId)

Retrieve a Digital Wallet Token

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let digitalWalletTokenId = "digital_wallet_token_izi62go3h51p369jrie0"; // String | 
apiInstance.retrieveADigitalWalletToken(digitalWalletTokenId, (error, data, response) => {
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
 **digitalWalletTokenId** | **String**|  | 

### Return type

[**DigitalWalletToken**](DigitalWalletToken.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveADocument

> Document retrieveADocument(documentId)

Retrieve a Document

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let documentId = "document_qjtqc6s4c14ve2q89izm"; // String | 
apiInstance.retrieveADocument(documentId, (error, data, response) => {
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
 **documentId** | **String**|  | 

### Return type

[**Document**](Document.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveAFile

> File retrieveAFile(fileId)

Retrieve a File

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let fileId = "file_makxrc67oh9l6sg7w9yc"; // String | 
apiInstance.retrieveAFile(fileId, (error, data, response) => {
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
 **fileId** | **String**|  | 

### Return type

**File**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveALimit

> Limit retrieveALimit(limitId)

Retrieve a Limit

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let limitId = "limit_fku42k0qtc8ulsuas38q"; // String | 
apiInstance.retrieveALimit(limitId, (error, data, response) => {
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
 **limitId** | **String**|  | 

### Return type

[**Limit**](Limit.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveAPendingTransaction

> PendingTransaction retrieveAPendingTransaction(pendingTransactionId)

Retrieve a Pending Transaction

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let pendingTransactionId = "pending_transaction_k1sfetcau2qbvjbzgju4"; // String | 
apiInstance.retrieveAPendingTransaction(pendingTransactionId, (error, data, response) => {
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
 **pendingTransactionId** | **String**|  | 

### Return type

[**PendingTransaction**](PendingTransaction.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveAProgram

> Program retrieveAProgram(programId)

Retrieve a Program

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let programId = "program_i2v2os4mwza1oetokh9i"; // String | 
apiInstance.retrieveAProgram(programId, (error, data, response) => {
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
 **programId** | **String**|  | 

### Return type

[**Program**](Program.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveARealTimeDecision

> RealTimeDecision retrieveARealTimeDecision(realTimeDecisionId)

Retrieve a Real-Time Decision

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let realTimeDecisionId = "real_time_decision_j76n2e810ezcg3zh5qtn"; // String | 
apiInstance.retrieveARealTimeDecision(realTimeDecisionId, (error, data, response) => {
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
 **realTimeDecisionId** | **String**|  | 

### Return type

[**RealTimeDecision**](RealTimeDecision.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveARealTimePaymentsTransfer

> RealTimePaymentsTransfer retrieveARealTimePaymentsTransfer(realTimePaymentsTransferId)

Retrieve a Real Time Payments Transfer

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let realTimePaymentsTransferId = "real_time_payments_transfer_iyuhl5kdn7ssmup83mvq"; // String | 
apiInstance.retrieveARealTimePaymentsTransfer(realTimePaymentsTransferId, (error, data, response) => {
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
 **realTimePaymentsTransferId** | **String**|  | 

### Return type

[**RealTimePaymentsTransfer**](RealTimePaymentsTransfer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveATransaction

> Transaction retrieveATransaction(transactionId)

Retrieve a Transaction

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let transactionId = "transaction_uyrp7fld2ium70oa7oi"; // String | 
apiInstance.retrieveATransaction(transactionId, (error, data, response) => {
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
 **transactionId** | **String**|  | 

### Return type

[**Transaction**](Transaction.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveAWireDrawdownRequest

> WireDrawdownRequest retrieveAWireDrawdownRequest(wireDrawdownRequestId)

Retrieve a Wire Drawdown Request

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let wireDrawdownRequestId = "wire_drawdown_request_q6lmocus3glo0lr2bfv3"; // String | 
apiInstance.retrieveAWireDrawdownRequest(wireDrawdownRequestId, (error, data, response) => {
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
 **wireDrawdownRequestId** | **String**|  | 

### Return type

[**WireDrawdownRequest**](WireDrawdownRequest.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveAWireTransfer

> WireTransfer retrieveAWireTransfer(wireTransferId)

Retrieve a Wire Transfer

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let wireTransferId = "wire_transfer_5akynk7dqsq25qwk9q2u"; // String | 
apiInstance.retrieveAWireTransfer(wireTransferId, (error, data, response) => {
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
 **wireTransferId** | **String**|  | 

### Return type

[**WireTransfer**](WireTransfer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveAnAccount

> Account retrieveAnAccount(accountId)

Retrieve an Account

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let accountId = "account_in71c4amph0vgo2qllky"; // String | 
apiInstance.retrieveAnAccount(accountId, (error, data, response) => {
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
 **accountId** | **String**|  | 

### Return type

[**Account**](Account.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveAnAccountNumber

> AccountNumber retrieveAnAccountNumber(accountNumberId)

Retrieve an Account Number

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let accountNumberId = "account_number_v18nkfqm6afpsrvy82b2"; // String | 
apiInstance.retrieveAnAccountNumber(accountNumberId, (error, data, response) => {
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
 **accountNumberId** | **String**|  | 

### Return type

[**AccountNumber**](AccountNumber.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveAnAccountStatement

> AccountStatement retrieveAnAccountStatement(accountStatementId)

Retrieve an Account Statement

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let accountStatementId = "account_statement_lkc03a4skm2k7f38vj15"; // String | 
apiInstance.retrieveAnAccountStatement(accountStatementId, (error, data, response) => {
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
 **accountStatementId** | **String**|  | 

### Return type

[**AccountStatement**](AccountStatement.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveAnAccountTransfer

> AccountTransfer retrieveAnAccountTransfer(accountTransferId)

Retrieve an Account Transfer

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let accountTransferId = "account_transfer_7k9qe1ysdgqztnt63l7n"; // String | 
apiInstance.retrieveAnAccountTransfer(accountTransferId, (error, data, response) => {
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
 **accountTransferId** | **String**|  | 

### Return type

[**AccountTransfer**](AccountTransfer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveAnAchPrenotification

> AchPrenotification retrieveAnAchPrenotification(achPrenotificationId)

Retrieve an ACH Prenotification

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let achPrenotificationId = "ach_prenotification_ubjf9qqsxl3obbcn1u34"; // String | 
apiInstance.retrieveAnAchPrenotification(achPrenotificationId, (error, data, response) => {
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
 **achPrenotificationId** | **String**|  | 

### Return type

[**AchPrenotification**](AchPrenotification.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveAnAchTransfer

> AchTransfer retrieveAnAchTransfer(achTransferId)

Retrieve an ACH Transfer

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let achTransferId = "ach_transfer_uoxatyh3lt5evrsdvo7q"; // String | 
apiInstance.retrieveAnAchTransfer(achTransferId, (error, data, response) => {
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
 **achTransferId** | **String**|  | 

### Return type

[**AchTransfer**](AchTransfer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveAnEntity

> Entity retrieveAnEntity(entityId)

Retrieve an Entity

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let entityId = "entity_n8y8tnk2p9339ti393yi"; // String | 
apiInstance.retrieveAnEntity(entityId, (error, data, response) => {
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
 **entityId** | **String**|  | 

### Return type

[**Entity**](Entity.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveAnEvent

> Event retrieveAnEvent(eventId)

Retrieve an Event

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let eventId = "event_001dzz0r20rzr4zrhrr1364hy80"; // String | 
apiInstance.retrieveAnEvent(eventId, (error, data, response) => {
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
 **eventId** | **String**|  | 

### Return type

[**Event**](Event.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveAnEventSubscription

> EventSubscription retrieveAnEventSubscription(eventSubscriptionId)

Retrieve an Event Subscription

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let eventSubscriptionId = "event_subscription_001dzz0r20rcdxgb013zqb8m04g"; // String | 
apiInstance.retrieveAnEventSubscription(eventSubscriptionId, (error, data, response) => {
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
 **eventSubscriptionId** | **String**|  | 

### Return type

[**EventSubscription**](EventSubscription.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveAnExport

> Export retrieveAnExport(exportId)

Retrieve an Export

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let exportId = "export_8s4m48qz3bclzje0zwh9"; // String | 
apiInstance.retrieveAnExport(exportId, (error, data, response) => {
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
 **exportId** | **String**|  | 

### Return type

[**Export**](Export.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveAnExternalAccount

> ExternalAccount retrieveAnExternalAccount(externalAccountId)

Retrieve an External Account

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let externalAccountId = "external_account_ukk55lr923a3ac0pp7iv"; // String | 
apiInstance.retrieveAnExternalAccount(externalAccountId, (error, data, response) => {
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
 **externalAccountId** | **String**|  | 

### Return type

[**ExternalAccount**](ExternalAccount.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveAnInboundAchTransferReturn

> InboundAchTransferReturn retrieveAnInboundAchTransferReturn(inboundAchTransferReturnId)

Retrieve an Inbound ACH Transfer Return

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let inboundAchTransferReturnId = "inbound_ach_transfer_return_fhcxk5huskwhmt7iz0gk"; // String | 
apiInstance.retrieveAnInboundAchTransferReturn(inboundAchTransferReturnId, (error, data, response) => {
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
 **inboundAchTransferReturnId** | **String**|  | 

### Return type

[**InboundAchTransferReturn**](InboundAchTransferReturn.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveAnInboundWireDrawdownRequest

> InboundWireDrawdownRequest retrieveAnInboundWireDrawdownRequest(inboundWireDrawdownRequestId)

Retrieve an Inbound Wire Drawdown Request

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let inboundWireDrawdownRequestId = "inbound_wire_drawdown_request_u5a92ikqhz1ytphn799e"; // String | 
apiInstance.retrieveAnInboundWireDrawdownRequest(inboundWireDrawdownRequestId, (error, data, response) => {
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
 **inboundWireDrawdownRequestId** | **String**|  | 

### Return type

[**InboundWireDrawdownRequest**](InboundWireDrawdownRequest.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveAnOauthConnection

> OauthConnection retrieveAnOauthConnection(oauthConnectionId)

Retrieve an OAuth Connection

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let oauthConnectionId = "connection_dauknoksyr4wilz4e6my"; // String | 
apiInstance.retrieveAnOauthConnection(oauthConnectionId, (error, data, response) => {
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
 **oauthConnectionId** | **String**|  | 

### Return type

[**OauthConnection**](OauthConnection.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveGroupDetails

> Group retrieveGroupDetails()

Retrieve Group details

Returns details for the currently authenticated Group.

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
apiInstance.retrieveGroupDetails((error, data, response) => {
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

[**Group**](Group.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveSensitiveDetailsForACard

> CardDetails retrieveSensitiveDetailsForACard(cardId)

Retrieve sensitive details for a Card

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let cardId = "card_oubs0hwk5rn6knuecxg2"; // String | 
apiInstance.retrieveSensitiveDetailsForACard(cardId, (error, data, response) => {
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
 **cardId** | **String**|  | 

### Return type

[**CardDetails**](CardDetails.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## returnASandboxAchTransfer

> AchTransfer returnASandboxAchTransfer(achTransferId, returnASandboxAchTransferParameters)

Return a Sandbox ACH Transfer

Simulates the return of an [ACH Transfer](#ach-transfers) by the Federal Reserve due to an error condition. This will also create a Transaction to account for the returned funds. This transfer must first have a &#x60;status&#x60; of &#x60;submitted&#x60;.

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let achTransferId = "ach_transfer_uoxatyh3lt5evrsdvo7q"; // String | 
let returnASandboxAchTransferParameters = new IncreaseApi.ReturnASandboxAchTransferParameters(); // ReturnASandboxAchTransferParameters | 
apiInstance.returnASandboxAchTransfer(achTransferId, returnASandboxAchTransferParameters, (error, data, response) => {
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
 **achTransferId** | **String**|  | 
 **returnASandboxAchTransferParameters** | [**ReturnASandboxAchTransferParameters**](ReturnASandboxAchTransferParameters.md)|  | 

### Return type

[**AchTransfer**](AchTransfer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## returnASandboxCheckDeposit

> CheckDeposit returnASandboxCheckDeposit(checkDepositId)

Return a Sandbox Check Deposit

Simulates the return of a [Check Deposit](#check-deposits). This Check Deposit must first have a &#x60;status&#x60; of &#x60;submitted&#x60;.

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let checkDepositId = "check_deposit_f06n9gpg7sxn8t19lfc1"; // String | 
apiInstance.returnASandboxCheckDeposit(checkDepositId, (error, data, response) => {
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
 **checkDepositId** | **String**|  | 

### Return type

[**CheckDeposit**](CheckDeposit.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## returnASandboxCheckTransfer

> CheckTransfer returnASandboxCheckTransfer(checkTransferId, returnASandboxCheckTransferParameters)

Return a Sandbox Check Transfer

Simulates a [Check Transfer](#check-transfers) being returned via USPS to Increase. This transfer must first have a &#x60;status&#x60; of &#x60;mailed&#x60;.

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let checkTransferId = "check_transfer_30b43acfu9vw8fyc4f5"; // String | 
let returnASandboxCheckTransferParameters = new IncreaseApi.ReturnASandboxCheckTransferParameters(); // ReturnASandboxCheckTransferParameters | 
apiInstance.returnASandboxCheckTransfer(checkTransferId, returnASandboxCheckTransferParameters, (error, data, response) => {
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
 **checkTransferId** | **String**|  | 
 **returnASandboxCheckTransferParameters** | [**ReturnASandboxCheckTransferParameters**](ReturnASandboxCheckTransferParameters.md)|  | 

### Return type

[**CheckTransfer**](CheckTransfer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## reverseASandboxWireTransfer

> WireTransfer reverseASandboxWireTransfer(wireTransferId)

Reverse a Sandbox Wire Transfer

Simulates the reversal of a [Wire Transfer](#wire-transfers) by the Federal Reserve due to error conditions. This will also create a [Transaction](#transaction) to account for the returned funds. This Wire Transfer must first have a &#x60;status&#x60; of &#x60;complete&#x60;.&#39;

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let wireTransferId = "wire_transfer_5akynk7dqsq25qwk9q2u"; // String | 
apiInstance.reverseASandboxWireTransfer(wireTransferId, (error, data, response) => {
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
 **wireTransferId** | **String**|  | 

### Return type

[**WireTransfer**](WireTransfer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## simulateARealTimePaymentsTransferToYourAccount

> InboundRealTimePaymentsTransferSimulationResult simulateARealTimePaymentsTransferToYourAccount(simulateARealTimePaymentsTransferToYourAccountParameters)

Simulate a Real Time Payments Transfer to your account

Simulates an inbound Real Time Payments transfer to your account. Real Time Payments are a beta feature.

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let simulateARealTimePaymentsTransferToYourAccountParameters = new IncreaseApi.SimulateARealTimePaymentsTransferToYourAccountParameters(); // SimulateARealTimePaymentsTransferToYourAccountParameters | 
apiInstance.simulateARealTimePaymentsTransferToYourAccount(simulateARealTimePaymentsTransferToYourAccountParameters, (error, data, response) => {
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
 **simulateARealTimePaymentsTransferToYourAccountParameters** | [**SimulateARealTimePaymentsTransferToYourAccountParameters**](SimulateARealTimePaymentsTransferToYourAccountParameters.md)|  | 

### Return type

[**InboundRealTimePaymentsTransferSimulationResult**](InboundRealTimePaymentsTransferSimulationResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## simulateARefundOnACard

> Transaction simulateARefundOnACard(simulateARefundOnACardParameters)

Simulate a refund on a card

Simulates refunding a card transaction. The full value of the original sandbox transaction is refunded.

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let simulateARefundOnACardParameters = new IncreaseApi.SimulateARefundOnACardParameters(); // SimulateARefundOnACardParameters | 
apiInstance.simulateARefundOnACard(simulateARefundOnACardParameters, (error, data, response) => {
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
 **simulateARefundOnACardParameters** | [**SimulateARefundOnACardParameters**](SimulateARefundOnACardParameters.md)|  | 

### Return type

[**Transaction**](Transaction.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## simulateATaxDocumentBeingCreated

> Document simulateATaxDocumentBeingCreated(simulateATaxDocumentBeingCreatedParameters)

Simulate a tax document being created

Simulates an tax document being created for an account.

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let simulateATaxDocumentBeingCreatedParameters = new IncreaseApi.SimulateATaxDocumentBeingCreatedParameters(); // SimulateATaxDocumentBeingCreatedParameters | 
apiInstance.simulateATaxDocumentBeingCreated(simulateATaxDocumentBeingCreatedParameters, (error, data, response) => {
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
 **simulateATaxDocumentBeingCreatedParameters** | [**SimulateATaxDocumentBeingCreatedParameters**](SimulateATaxDocumentBeingCreatedParameters.md)|  | 

### Return type

[**Document**](Document.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## simulateAWireTransferToYourAccount

> InboundWireTransferSimulationResult simulateAWireTransferToYourAccount(simulateAWireTransferToYourAccountParameters)

Simulate a Wire Transfer to your account

Simulates an inbound Wire Transfer to your account.

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let simulateAWireTransferToYourAccountParameters = new IncreaseApi.SimulateAWireTransferToYourAccountParameters(); // SimulateAWireTransferToYourAccountParameters | 
apiInstance.simulateAWireTransferToYourAccount(simulateAWireTransferToYourAccountParameters, (error, data, response) => {
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
 **simulateAWireTransferToYourAccountParameters** | [**SimulateAWireTransferToYourAccountParameters**](SimulateAWireTransferToYourAccountParameters.md)|  | 

### Return type

[**InboundWireTransferSimulationResult**](InboundWireTransferSimulationResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## simulateAnAccountStatementBeingCreated

> AccountStatement simulateAnAccountStatementBeingCreated(simulateAnAccountStatementBeingCreatedParameters)

Simulate an Account Statement being created

Simulates an [Account Statement](#account-statements) being created for an account. In production, Account Statements are generated once per month.

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let simulateAnAccountStatementBeingCreatedParameters = new IncreaseApi.SimulateAnAccountStatementBeingCreatedParameters(); // SimulateAnAccountStatementBeingCreatedParameters | 
apiInstance.simulateAnAccountStatementBeingCreated(simulateAnAccountStatementBeingCreatedParameters, (error, data, response) => {
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
 **simulateAnAccountStatementBeingCreatedParameters** | [**SimulateAnAccountStatementBeingCreatedParameters**](SimulateAnAccountStatementBeingCreatedParameters.md)|  | 

### Return type

[**AccountStatement**](AccountStatement.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## simulateAnAchTransferToYourAccount

> InboundAchTransferSimulationResult simulateAnAchTransferToYourAccount(simulateAnAchTransferToYourAccountParameters)

Simulate an ACH Transfer to your account

Simulates an inbound ACH transfer to your account. This imitates initiating a transaction to an Increase account from a different financial institution. The transfer may be either a credit or a debit depending on if the &#x60;amount&#x60; is positive or negative. The result of calling this API will be either a [Transaction](#transactions) or a [Declined Transaction](#declined-transactions) depending on whether or not the transfer is allowed.

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let simulateAnAchTransferToYourAccountParameters = new IncreaseApi.SimulateAnAchTransferToYourAccountParameters(); // SimulateAnAchTransferToYourAccountParameters | 
apiInstance.simulateAnAchTransferToYourAccount(simulateAnAchTransferToYourAccountParameters, (error, data, response) => {
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
 **simulateAnAchTransferToYourAccountParameters** | [**SimulateAnAchTransferToYourAccountParameters**](SimulateAnAchTransferToYourAccountParameters.md)|  | 

### Return type

[**InboundAchTransferSimulationResult**](InboundAchTransferSimulationResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## simulateAnAuthorizationOnACard

> InboundCardAuthorizationSimulationResult simulateAnAuthorizationOnACard(simulateAnAuthorizationOnACardParameters)

Simulate an authorization on a Card

Simulates a purchase authorization on a [Card](#cards). Depending on the balance available to the card and the &#x60;amount&#x60; submitted, the authorization activity will result in a [Pending Transaction](#pending-transactions) of type &#x60;card_authorization&#x60; or a [Declined Transaction](#declined-transactions) of type &#x60;card_decline&#x60;. You can pass either a Card id or a [Digital Wallet Token](#digital-wallet-tokens) id to simulate the two different ways purchases can be made.

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let simulateAnAuthorizationOnACardParameters = new IncreaseApi.SimulateAnAuthorizationOnACardParameters(); // SimulateAnAuthorizationOnACardParameters | 
apiInstance.simulateAnAuthorizationOnACard(simulateAnAuthorizationOnACardParameters, (error, data, response) => {
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
 **simulateAnAuthorizationOnACardParameters** | [**SimulateAnAuthorizationOnACardParameters**](SimulateAnAuthorizationOnACardParameters.md)|  | 

### Return type

[**InboundCardAuthorizationSimulationResult**](InboundCardAuthorizationSimulationResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## simulateAnInboundWireDrawdownRequestBeingCreated

> InboundWireDrawdownRequest simulateAnInboundWireDrawdownRequestBeingCreated(simulateAnInboundWireDrawdownRequestBeingCreatedParameters)

Simulate an Inbound Wire Drawdown request being created

Simulates the receival of an [Inbound Wire Drawdown Request](#inbound-wire-drawdown-requests).

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let simulateAnInboundWireDrawdownRequestBeingCreatedParameters = new IncreaseApi.SimulateAnInboundWireDrawdownRequestBeingCreatedParameters(); // SimulateAnInboundWireDrawdownRequestBeingCreatedParameters | 
apiInstance.simulateAnInboundWireDrawdownRequestBeingCreated(simulateAnInboundWireDrawdownRequestBeingCreatedParameters, (error, data, response) => {
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
 **simulateAnInboundWireDrawdownRequestBeingCreatedParameters** | [**SimulateAnInboundWireDrawdownRequestBeingCreatedParameters**](SimulateAnInboundWireDrawdownRequestBeingCreatedParameters.md)|  | 

### Return type

[**InboundWireDrawdownRequest**](InboundWireDrawdownRequest.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## simulateAnInterestPaymentToYourAccount

> InterestPaymentSimulationResult simulateAnInterestPaymentToYourAccount(simulateAnInterestPaymentToYourAccountParameters)

Simulate an Interest Payment to your account

Simulates an interest payment to your account. In production, this happens automatically on the first of each month.

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let simulateAnInterestPaymentToYourAccountParameters = new IncreaseApi.SimulateAnInterestPaymentToYourAccountParameters(); // SimulateAnInterestPaymentToYourAccountParameters | 
apiInstance.simulateAnInterestPaymentToYourAccount(simulateAnInterestPaymentToYourAccountParameters, (error, data, response) => {
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
 **simulateAnInterestPaymentToYourAccountParameters** | [**SimulateAnInterestPaymentToYourAccountParameters**](SimulateAnInterestPaymentToYourAccountParameters.md)|  | 

### Return type

[**InterestPaymentSimulationResult**](InterestPaymentSimulationResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## simulateDigitalWalletProvisioningForACard

> InboundDigitalWalletTokenRequestSimulationResult simulateDigitalWalletProvisioningForACard(simulateDigitalWalletProvisioningForACardParameters)

Simulate digital wallet provisioning for a card

Simulates a user attempting add a [Card](#cards) to a digital wallet such as Apple Pay.

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let simulateDigitalWalletProvisioningForACardParameters = new IncreaseApi.SimulateDigitalWalletProvisioningForACardParameters(); // SimulateDigitalWalletProvisioningForACardParameters | 
apiInstance.simulateDigitalWalletProvisioningForACard(simulateDigitalWalletProvisioningForACardParameters, (error, data, response) => {
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
 **simulateDigitalWalletProvisioningForACardParameters** | [**SimulateDigitalWalletProvisioningForACardParameters**](SimulateDigitalWalletProvisioningForACardParameters.md)|  | 

### Return type

[**InboundDigitalWalletTokenRequestSimulationResult**](InboundDigitalWalletTokenRequestSimulationResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## simulateSettlingACardAuthorization

> Transaction simulateSettlingACardAuthorization(simulateSettlingACardAuthorizationParameters)

Simulate settling a card authorization

Simulates the settlement of an authorization by a card acquirer. After a card authorization is created, the merchant will eventually send a settlement. This simulates that event, which may occur many days after the purchase in production. The amount settled can be different from the amount originally authorized, for example, when adding a tip to a restaurant bill.

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let simulateSettlingACardAuthorizationParameters = new IncreaseApi.SimulateSettlingACardAuthorizationParameters(); // SimulateSettlingACardAuthorizationParameters | 
apiInstance.simulateSettlingACardAuthorization(simulateSettlingACardAuthorizationParameters, (error, data, response) => {
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
 **simulateSettlingACardAuthorizationParameters** | [**SimulateSettlingACardAuthorizationParameters**](SimulateSettlingACardAuthorizationParameters.md)|  | 

### Return type

[**Transaction**](Transaction.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## simulatesAdvancingTheStateOfACardDispute

> CardDispute simulatesAdvancingTheStateOfACardDispute(cardDisputeId, simulatesAdvancingTheStateOfACardDisputeParameters)

Simulates advancing the state of a card dispute

After a [Card Dispute](#card-disputes) is created in production, the dispute will be reviewed. Since no review happens in sandbox, this endpoint simulates moving a Card Dispute into a rejected or accepted state. A Card Dispute can only be actioned one time and must have a status of &#x60;pending_reviewing&#x60;.

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let cardDisputeId = "card_dispute_h9sc95nbl1cgltpp7men"; // String | 
let simulatesAdvancingTheStateOfACardDisputeParameters = new IncreaseApi.SimulatesAdvancingTheStateOfACardDisputeParameters(); // SimulatesAdvancingTheStateOfACardDisputeParameters | 
apiInstance.simulatesAdvancingTheStateOfACardDispute(cardDisputeId, simulatesAdvancingTheStateOfACardDisputeParameters, (error, data, response) => {
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
 **cardDisputeId** | **String**|  | 
 **simulatesAdvancingTheStateOfACardDisputeParameters** | [**SimulatesAdvancingTheStateOfACardDisputeParameters**](SimulatesAdvancingTheStateOfACardDisputeParameters.md)|  | 

### Return type

[**CardDispute**](CardDispute.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## submitASandboxAchTransfer

> AchTransfer submitASandboxAchTransfer(achTransferId)

Submit a Sandbox ACH Transfer

Simulates the submission of an [ACH Transfer](#ach-transfers) to the Federal Reserve. This transfer must first have a &#x60;status&#x60; of &#x60;pending_approval&#x60; or &#x60;pending_submission&#x60;. In production, Increase submits ACH Transfers to the Federal Reserve three times per day on weekdays. Since sandbox ACH Transfers are not submitted to the Federal Reserve, this endpoint allows you to skip that delay and transition the ACH Transfer to a status of &#x60;submitted&#x60;.

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let achTransferId = "ach_transfer_uoxatyh3lt5evrsdvo7q"; // String | 
apiInstance.submitASandboxAchTransfer(achTransferId, (error, data, response) => {
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
 **achTransferId** | **String**|  | 

### Return type

[**AchTransfer**](AchTransfer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## submitASandboxCheckDeposit

> CheckDeposit submitASandboxCheckDeposit(checkDepositId)

Submit a Sandbox Check Deposit

Simulates the submission of a [Check Deposit](#check-deposits) to the Federal Reserve. This Check Deposit must first have a &#x60;status&#x60; of &#x60;pending&#x60;.

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let checkDepositId = "check_deposit_f06n9gpg7sxn8t19lfc1"; // String | 
apiInstance.submitASandboxCheckDeposit(checkDepositId, (error, data, response) => {
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
 **checkDepositId** | **String**|  | 

### Return type

[**CheckDeposit**](CheckDeposit.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## submitASandboxWireTransfer

> WireTransfer submitASandboxWireTransfer(wireTransferId)

Submit a Sandbox Wire Transfer

Simulates the submission of a [Wire Transfer](#wire-transfers) to the Federal Reserve. This transfer must first have a &#x60;status&#x60; of &#x60;pending_approval&#x60; or &#x60;pending_creating&#x60;.

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let wireTransferId = "wire_transfer_5akynk7dqsq25qwk9q2u"; // String | 
apiInstance.submitASandboxWireTransfer(wireTransferId, (error, data, response) => {
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
 **wireTransferId** | **String**|  | 

### Return type

[**WireTransfer**](WireTransfer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateACard

> Card updateACard(cardId, updateACardParameters)

Update a Card

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let cardId = "card_oubs0hwk5rn6knuecxg2"; // String | 
let updateACardParameters = new IncreaseApi.UpdateACardParameters(); // UpdateACardParameters | 
apiInstance.updateACard(cardId, updateACardParameters, (error, data, response) => {
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
 **cardId** | **String**|  | 
 **updateACardParameters** | [**UpdateACardParameters**](UpdateACardParameters.md)|  | 

### Return type

[**Card**](Card.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateALimit

> Limit updateALimit(limitId, updateALimitParameters)

Update a Limit

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let limitId = "limit_fku42k0qtc8ulsuas38q"; // String | 
let updateALimitParameters = new IncreaseApi.UpdateALimitParameters(); // UpdateALimitParameters | 
apiInstance.updateALimit(limitId, updateALimitParameters, (error, data, response) => {
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
 **limitId** | **String**|  | 
 **updateALimitParameters** | [**UpdateALimitParameters**](UpdateALimitParameters.md)|  | 

### Return type

[**Limit**](Limit.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateAnAccount

> Account updateAnAccount(accountId, updateAnAccountParameters)

Update an Account

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let accountId = "account_in71c4amph0vgo2qllky"; // String | 
let updateAnAccountParameters = new IncreaseApi.UpdateAnAccountParameters(); // UpdateAnAccountParameters | 
apiInstance.updateAnAccount(accountId, updateAnAccountParameters, (error, data, response) => {
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
 **accountId** | **String**|  | 
 **updateAnAccountParameters** | [**UpdateAnAccountParameters**](UpdateAnAccountParameters.md)|  | 

### Return type

[**Account**](Account.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateAnAccountNumber

> AccountNumber updateAnAccountNumber(accountNumberId, updateAnAccountNumberParameters)

Update an Account Number

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let accountNumberId = "account_number_v18nkfqm6afpsrvy82b2"; // String | 
let updateAnAccountNumberParameters = new IncreaseApi.UpdateAnAccountNumberParameters(); // UpdateAnAccountNumberParameters | 
apiInstance.updateAnAccountNumber(accountNumberId, updateAnAccountNumberParameters, (error, data, response) => {
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
 **accountNumberId** | **String**|  | 
 **updateAnAccountNumberParameters** | [**UpdateAnAccountNumberParameters**](UpdateAnAccountNumberParameters.md)|  | 

### Return type

[**AccountNumber**](AccountNumber.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateAnEventSubscription

> EventSubscription updateAnEventSubscription(eventSubscriptionId, updateAnEventSubscriptionParameters)

Update an Event Subscription

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let eventSubscriptionId = "event_subscription_001dzz0r20rcdxgb013zqb8m04g"; // String | 
let updateAnEventSubscriptionParameters = new IncreaseApi.UpdateAnEventSubscriptionParameters(); // UpdateAnEventSubscriptionParameters | 
apiInstance.updateAnEventSubscription(eventSubscriptionId, updateAnEventSubscriptionParameters, (error, data, response) => {
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
 **eventSubscriptionId** | **String**|  | 
 **updateAnEventSubscriptionParameters** | [**UpdateAnEventSubscriptionParameters**](UpdateAnEventSubscriptionParameters.md)|  | 

### Return type

[**EventSubscription**](EventSubscription.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateAnExternalAccount

> ExternalAccount updateAnExternalAccount(externalAccountId, updateAnExternalAccountParameters)

Update an External Account

### Example

```javascript
import IncreaseApi from 'increase_api';
let defaultClient = IncreaseApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IncreaseApi.DefaultApi();
let externalAccountId = "external_account_ukk55lr923a3ac0pp7iv"; // String | 
let updateAnExternalAccountParameters = new IncreaseApi.UpdateAnExternalAccountParameters(); // UpdateAnExternalAccountParameters | 
apiInstance.updateAnExternalAccount(externalAccountId, updateAnExternalAccountParameters, (error, data, response) => {
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
 **externalAccountId** | **String**|  | 
 **updateAnExternalAccountParameters** | [**UpdateAnExternalAccountParameters**](UpdateAnExternalAccountParameters.md)|  | 

### Return type

[**ExternalAccount**](ExternalAccount.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

