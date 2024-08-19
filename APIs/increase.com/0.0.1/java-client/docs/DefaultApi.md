# DefaultApi

All URIs are relative to *https://api.increase.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**actionARealTimeDecision**](DefaultApi.md#actionARealTimeDecision) | **POST** /real_time_decisions/{real_time_decision_id}/action | Action a Real-Time Decision |
| [**approveACheckTransfer**](DefaultApi.md#approveACheckTransfer) | **POST** /check_transfers/{check_transfer_id}/approve | Approve a Check Transfer |
| [**approveAWireTransfer**](DefaultApi.md#approveAWireTransfer) | **POST** /wire_transfers/{wire_transfer_id}/approve | Approve a Wire Transfer |
| [**approveAnAccountTransfer**](DefaultApi.md#approveAnAccountTransfer) | **POST** /account_transfers/{account_transfer_id}/approve | Approve an Account Transfer |
| [**approveAnAchTransfer**](DefaultApi.md#approveAnAchTransfer) | **POST** /ach_transfers/{ach_transfer_id}/approve | Approve an ACH Transfer |
| [**cancelAPendingAchTransfer**](DefaultApi.md#cancelAPendingAchTransfer) | **POST** /ach_transfers/{ach_transfer_id}/cancel | Cancel a pending ACH Transfer |
| [**cancelAPendingCheckTransfer**](DefaultApi.md#cancelAPendingCheckTransfer) | **POST** /check_transfers/{check_transfer_id}/cancel | Cancel a pending Check Transfer |
| [**cancelAPendingWireTransfer**](DefaultApi.md#cancelAPendingWireTransfer) | **POST** /wire_transfers/{wire_transfer_id}/cancel | Cancel a pending Wire Transfer |
| [**cancelAnAccountTransfer**](DefaultApi.md#cancelAnAccountTransfer) | **POST** /account_transfers/{account_transfer_id}/cancel | Cancel an Account Transfer |
| [**closeAnAccount**](DefaultApi.md#closeAnAccount) | **POST** /accounts/{account_id}/close | Close an Account |
| [**completeASandboxAccountTransfer**](DefaultApi.md#completeASandboxAccountTransfer) | **POST** /simulations/account_transfers/{account_transfer_id}/complete | Complete a Sandbox Account Transfer |
| [**completeASandboxRealTimePaymentsTransfer**](DefaultApi.md#completeASandboxRealTimePaymentsTransfer) | **POST** /simulations/real_time_payments_transfers/{real_time_payments_transfer_id}/complete | Complete a Sandbox Real Time Payments Transfer |
| [**createABookkeepingAccount**](DefaultApi.md#createABookkeepingAccount) | **POST** /bookkeeping_accounts | Create a Bookkeeping Account |
| [**createABookkeepingEntrySet**](DefaultApi.md#createABookkeepingEntrySet) | **POST** /bookkeeping_entry_sets | Create a Bookkeeping Entry Set |
| [**createACard**](DefaultApi.md#createACard) | **POST** /cards | Create a Card |
| [**createACardDispute**](DefaultApi.md#createACardDispute) | **POST** /card_disputes | Create a Card Dispute |
| [**createACardProfile**](DefaultApi.md#createACardProfile) | **POST** /card_profiles | Create a Card Profile |
| [**createACheckDeposit**](DefaultApi.md#createACheckDeposit) | **POST** /check_deposits | Create a Check Deposit |
| [**createACheckTransfer**](DefaultApi.md#createACheckTransfer) | **POST** /check_transfers | Create a Check Transfer |
| [**createAFile**](DefaultApi.md#createAFile) | **POST** /files | Create a File |
| [**createALimit**](DefaultApi.md#createALimit) | **POST** /limits | Create a Limit |
| [**createARealTimePaymentsTransfer**](DefaultApi.md#createARealTimePaymentsTransfer) | **POST** /real_time_payments_transfers | Create a Real Time Payments Transfer |
| [**createASupplementalDocumentForAnEntity**](DefaultApi.md#createASupplementalDocumentForAnEntity) | **POST** /entities/{entity_id}/supplemental_documents | Create a supplemental document for an Entity |
| [**createAWireDrawdownRequest**](DefaultApi.md#createAWireDrawdownRequest) | **POST** /wire_drawdown_requests | Create a Wire Drawdown Request |
| [**createAWireTransfer**](DefaultApi.md#createAWireTransfer) | **POST** /wire_transfers | Create a Wire Transfer |
| [**createAnAccount**](DefaultApi.md#createAnAccount) | **POST** /accounts | Create an Account |
| [**createAnAccountNumber**](DefaultApi.md#createAnAccountNumber) | **POST** /account_numbers | Create an Account Number |
| [**createAnAccountTransfer**](DefaultApi.md#createAnAccountTransfer) | **POST** /account_transfers | Create an Account Transfer |
| [**createAnAchPrenotification**](DefaultApi.md#createAnAchPrenotification) | **POST** /ach_prenotifications | Create an ACH Prenotification |
| [**createAnAchReturn**](DefaultApi.md#createAnAchReturn) | **POST** /inbound_ach_transfer_returns | Create an ACH Return |
| [**createAnAchTransfer**](DefaultApi.md#createAnAchTransfer) | **POST** /ach_transfers | Create an ACH Transfer |
| [**createAnEntity**](DefaultApi.md#createAnEntity) | **POST** /entities | Create an Entity |
| [**createAnEventSubscription**](DefaultApi.md#createAnEventSubscription) | **POST** /event_subscriptions | Create an Event Subscription |
| [**createAnExport**](DefaultApi.md#createAnExport) | **POST** /exports | Create an Export |
| [**createAnExternalAccount**](DefaultApi.md#createAnExternalAccount) | **POST** /external_accounts | Create an External Account |
| [**depositASandboxCheckTransfer**](DefaultApi.md#depositASandboxCheckTransfer) | **POST** /simulations/check_transfers/{check_transfer_id}/deposit | Deposit a Sandbox Check Transfer |
| [**listAccountNumbers**](DefaultApi.md#listAccountNumbers) | **GET** /account_numbers | List Account Numbers |
| [**listAccountStatements**](DefaultApi.md#listAccountStatements) | **GET** /account_statements | List Account Statements |
| [**listAccountTransfers**](DefaultApi.md#listAccountTransfers) | **GET** /account_transfers | List Account Transfers |
| [**listAccounts**](DefaultApi.md#listAccounts) | **GET** /accounts | List Accounts |
| [**listAchPrenotifications**](DefaultApi.md#listAchPrenotifications) | **GET** /ach_prenotifications | List ACH Prenotifications |
| [**listAchTransfers**](DefaultApi.md#listAchTransfers) | **GET** /ach_transfers | List ACH Transfers |
| [**listBookkeepingAccounts**](DefaultApi.md#listBookkeepingAccounts) | **GET** /bookkeeping_accounts | List Bookkeeping Accounts |
| [**listBookkeepingEntries**](DefaultApi.md#listBookkeepingEntries) | **GET** /bookkeeping_entries | List Bookkeeping Entries |
| [**listCardDisputes**](DefaultApi.md#listCardDisputes) | **GET** /card_disputes | List Card Disputes |
| [**listCardProfiles**](DefaultApi.md#listCardProfiles) | **GET** /card_profiles | List Card Profiles |
| [**listCards**](DefaultApi.md#listCards) | **GET** /cards | List Cards |
| [**listCheckDeposits**](DefaultApi.md#listCheckDeposits) | **GET** /check_deposits | List Check Deposits |
| [**listCheckTransfers**](DefaultApi.md#listCheckTransfers) | **GET** /check_transfers | List Check Transfers |
| [**listDeclinedTransactions**](DefaultApi.md#listDeclinedTransactions) | **GET** /declined_transactions | List Declined Transactions |
| [**listDigitalWalletTokens**](DefaultApi.md#listDigitalWalletTokens) | **GET** /digital_wallet_tokens | List Digital Wallet Tokens |
| [**listDocuments**](DefaultApi.md#listDocuments) | **GET** /documents | List Documents |
| [**listEntities**](DefaultApi.md#listEntities) | **GET** /entities | List Entities |
| [**listEventSubscriptions**](DefaultApi.md#listEventSubscriptions) | **GET** /event_subscriptions | List Event Subscriptions |
| [**listEvents**](DefaultApi.md#listEvents) | **GET** /events | List Events |
| [**listExports**](DefaultApi.md#listExports) | **GET** /exports | List Exports |
| [**listExternalAccounts**](DefaultApi.md#listExternalAccounts) | **GET** /external_accounts | List External Accounts |
| [**listFiles**](DefaultApi.md#listFiles) | **GET** /files | List Files |
| [**listInboundAchTransferReturns**](DefaultApi.md#listInboundAchTransferReturns) | **GET** /inbound_ach_transfer_returns | List Inbound ACH Transfer Returns |
| [**listInboundWireDrawdownRequests**](DefaultApi.md#listInboundWireDrawdownRequests) | **GET** /inbound_wire_drawdown_requests | List Inbound Wire Drawdown Requests |
| [**listLimits**](DefaultApi.md#listLimits) | **GET** /limits | List Limits |
| [**listOauthConnections**](DefaultApi.md#listOauthConnections) | **GET** /oauth_connections | List OAuth Connections |
| [**listPendingTransactions**](DefaultApi.md#listPendingTransactions) | **GET** /pending_transactions | List Pending Transactions |
| [**listPrograms**](DefaultApi.md#listPrograms) | **GET** /programs | List Programs |
| [**listRealTimePaymentsTransfers**](DefaultApi.md#listRealTimePaymentsTransfers) | **GET** /real_time_payments_transfers | List Real Time Payments Transfers |
| [**listRoutingNumbers**](DefaultApi.md#listRoutingNumbers) | **GET** /routing_numbers | List Routing Numbers |
| [**listTransactions**](DefaultApi.md#listTransactions) | **GET** /transactions | List Transactions |
| [**listWireDrawdownRequests**](DefaultApi.md#listWireDrawdownRequests) | **GET** /wire_drawdown_requests | List Wire Drawdown Requests |
| [**listWireTransfers**](DefaultApi.md#listWireTransfers) | **GET** /wire_transfers | List Wire Transfers |
| [**lookUpTheBalanceForAnAccount**](DefaultApi.md#lookUpTheBalanceForAnAccount) | **POST** /balance_lookups | Look up the balance for an Account |
| [**mailASandboxCheckTransfer**](DefaultApi.md#mailASandboxCheckTransfer) | **POST** /simulations/check_transfers/{check_transfer_id}/mail | Mail a Sandbox Check Transfer |
| [**rejectASandboxCheckDeposit**](DefaultApi.md#rejectASandboxCheckDeposit) | **POST** /simulations/check_deposits/{check_deposit_id}/reject | Reject a Sandbox Check Deposit |
| [**requestAStopPaymentOnACheckTransfer**](DefaultApi.md#requestAStopPaymentOnACheckTransfer) | **POST** /check_transfers/{check_transfer_id}/stop_payment | Request a stop payment on a Check Transfer |
| [**retrieveACard**](DefaultApi.md#retrieveACard) | **GET** /cards/{card_id} | Retrieve a Card |
| [**retrieveACardDispute**](DefaultApi.md#retrieveACardDispute) | **GET** /card_disputes/{card_dispute_id} | Retrieve a Card Dispute |
| [**retrieveACardProfile**](DefaultApi.md#retrieveACardProfile) | **GET** /card_profiles/{card_profile_id} | Retrieve a Card Profile |
| [**retrieveACheckDeposit**](DefaultApi.md#retrieveACheckDeposit) | **GET** /check_deposits/{check_deposit_id} | Retrieve a Check Deposit |
| [**retrieveACheckTransfer**](DefaultApi.md#retrieveACheckTransfer) | **GET** /check_transfers/{check_transfer_id} | Retrieve a Check Transfer |
| [**retrieveADeclinedTransaction**](DefaultApi.md#retrieveADeclinedTransaction) | **GET** /declined_transactions/{declined_transaction_id} | Retrieve a Declined Transaction |
| [**retrieveADigitalWalletToken**](DefaultApi.md#retrieveADigitalWalletToken) | **GET** /digital_wallet_tokens/{digital_wallet_token_id} | Retrieve a Digital Wallet Token |
| [**retrieveADocument**](DefaultApi.md#retrieveADocument) | **GET** /documents/{document_id} | Retrieve a Document |
| [**retrieveAFile**](DefaultApi.md#retrieveAFile) | **GET** /files/{file_id} | Retrieve a File |
| [**retrieveALimit**](DefaultApi.md#retrieveALimit) | **GET** /limits/{limit_id} | Retrieve a Limit |
| [**retrieveAPendingTransaction**](DefaultApi.md#retrieveAPendingTransaction) | **GET** /pending_transactions/{pending_transaction_id} | Retrieve a Pending Transaction |
| [**retrieveAProgram**](DefaultApi.md#retrieveAProgram) | **GET** /programs/{program_id} | Retrieve a Program |
| [**retrieveARealTimeDecision**](DefaultApi.md#retrieveARealTimeDecision) | **GET** /real_time_decisions/{real_time_decision_id} | Retrieve a Real-Time Decision |
| [**retrieveARealTimePaymentsTransfer**](DefaultApi.md#retrieveARealTimePaymentsTransfer) | **GET** /real_time_payments_transfers/{real_time_payments_transfer_id} | Retrieve a Real Time Payments Transfer |
| [**retrieveATransaction**](DefaultApi.md#retrieveATransaction) | **GET** /transactions/{transaction_id} | Retrieve a Transaction |
| [**retrieveAWireDrawdownRequest**](DefaultApi.md#retrieveAWireDrawdownRequest) | **GET** /wire_drawdown_requests/{wire_drawdown_request_id} | Retrieve a Wire Drawdown Request |
| [**retrieveAWireTransfer**](DefaultApi.md#retrieveAWireTransfer) | **GET** /wire_transfers/{wire_transfer_id} | Retrieve a Wire Transfer |
| [**retrieveAnAccount**](DefaultApi.md#retrieveAnAccount) | **GET** /accounts/{account_id} | Retrieve an Account |
| [**retrieveAnAccountNumber**](DefaultApi.md#retrieveAnAccountNumber) | **GET** /account_numbers/{account_number_id} | Retrieve an Account Number |
| [**retrieveAnAccountStatement**](DefaultApi.md#retrieveAnAccountStatement) | **GET** /account_statements/{account_statement_id} | Retrieve an Account Statement |
| [**retrieveAnAccountTransfer**](DefaultApi.md#retrieveAnAccountTransfer) | **GET** /account_transfers/{account_transfer_id} | Retrieve an Account Transfer |
| [**retrieveAnAchPrenotification**](DefaultApi.md#retrieveAnAchPrenotification) | **GET** /ach_prenotifications/{ach_prenotification_id} | Retrieve an ACH Prenotification |
| [**retrieveAnAchTransfer**](DefaultApi.md#retrieveAnAchTransfer) | **GET** /ach_transfers/{ach_transfer_id} | Retrieve an ACH Transfer |
| [**retrieveAnEntity**](DefaultApi.md#retrieveAnEntity) | **GET** /entities/{entity_id} | Retrieve an Entity |
| [**retrieveAnEvent**](DefaultApi.md#retrieveAnEvent) | **GET** /events/{event_id} | Retrieve an Event |
| [**retrieveAnEventSubscription**](DefaultApi.md#retrieveAnEventSubscription) | **GET** /event_subscriptions/{event_subscription_id} | Retrieve an Event Subscription |
| [**retrieveAnExport**](DefaultApi.md#retrieveAnExport) | **GET** /exports/{export_id} | Retrieve an Export |
| [**retrieveAnExternalAccount**](DefaultApi.md#retrieveAnExternalAccount) | **GET** /external_accounts/{external_account_id} | Retrieve an External Account |
| [**retrieveAnInboundAchTransferReturn**](DefaultApi.md#retrieveAnInboundAchTransferReturn) | **GET** /inbound_ach_transfer_returns/{inbound_ach_transfer_return_id} | Retrieve an Inbound ACH Transfer Return |
| [**retrieveAnInboundWireDrawdownRequest**](DefaultApi.md#retrieveAnInboundWireDrawdownRequest) | **GET** /inbound_wire_drawdown_requests/{inbound_wire_drawdown_request_id} | Retrieve an Inbound Wire Drawdown Request |
| [**retrieveAnOauthConnection**](DefaultApi.md#retrieveAnOauthConnection) | **GET** /oauth_connections/{oauth_connection_id} | Retrieve an OAuth Connection |
| [**retrieveGroupDetails**](DefaultApi.md#retrieveGroupDetails) | **GET** /groups/current | Retrieve Group details |
| [**retrieveSensitiveDetailsForACard**](DefaultApi.md#retrieveSensitiveDetailsForACard) | **GET** /cards/{card_id}/details | Retrieve sensitive details for a Card |
| [**returnASandboxAchTransfer**](DefaultApi.md#returnASandboxAchTransfer) | **POST** /simulations/ach_transfers/{ach_transfer_id}/return | Return a Sandbox ACH Transfer |
| [**returnASandboxCheckDeposit**](DefaultApi.md#returnASandboxCheckDeposit) | **POST** /simulations/check_deposits/{check_deposit_id}/return | Return a Sandbox Check Deposit |
| [**returnASandboxCheckTransfer**](DefaultApi.md#returnASandboxCheckTransfer) | **POST** /simulations/check_transfers/{check_transfer_id}/return | Return a Sandbox Check Transfer |
| [**reverseASandboxWireTransfer**](DefaultApi.md#reverseASandboxWireTransfer) | **POST** /simulations/wire_transfers/{wire_transfer_id}/reverse | Reverse a Sandbox Wire Transfer |
| [**simulateARealTimePaymentsTransferToYourAccount**](DefaultApi.md#simulateARealTimePaymentsTransferToYourAccount) | **POST** /simulations/inbound_real_time_payments_transfers | Simulate a Real Time Payments Transfer to your account |
| [**simulateARefundOnACard**](DefaultApi.md#simulateARefundOnACard) | **POST** /simulations/card_refunds | Simulate a refund on a card |
| [**simulateATaxDocumentBeingCreated**](DefaultApi.md#simulateATaxDocumentBeingCreated) | **POST** /simulations/documents | Simulate a tax document being created |
| [**simulateAWireTransferToYourAccount**](DefaultApi.md#simulateAWireTransferToYourAccount) | **POST** /simulations/inbound_wire_transfers | Simulate a Wire Transfer to your account |
| [**simulateAnAccountStatementBeingCreated**](DefaultApi.md#simulateAnAccountStatementBeingCreated) | **POST** /simulations/account_statements | Simulate an Account Statement being created |
| [**simulateAnAchTransferToYourAccount**](DefaultApi.md#simulateAnAchTransferToYourAccount) | **POST** /simulations/inbound_ach_transfers | Simulate an ACH Transfer to your account |
| [**simulateAnAuthorizationOnACard**](DefaultApi.md#simulateAnAuthorizationOnACard) | **POST** /simulations/card_authorizations | Simulate an authorization on a Card |
| [**simulateAnInboundWireDrawdownRequestBeingCreated**](DefaultApi.md#simulateAnInboundWireDrawdownRequestBeingCreated) | **POST** /simulations/inbound_wire_drawdown_requests | Simulate an Inbound Wire Drawdown request being created |
| [**simulateAnInterestPaymentToYourAccount**](DefaultApi.md#simulateAnInterestPaymentToYourAccount) | **POST** /simulations/interest_payment | Simulate an Interest Payment to your account |
| [**simulateDigitalWalletProvisioningForACard**](DefaultApi.md#simulateDigitalWalletProvisioningForACard) | **POST** /simulations/digital_wallet_token_requests | Simulate digital wallet provisioning for a card |
| [**simulateSettlingACardAuthorization**](DefaultApi.md#simulateSettlingACardAuthorization) | **POST** /simulations/card_settlements | Simulate settling a card authorization |
| [**simulatesAdvancingTheStateOfACardDispute**](DefaultApi.md#simulatesAdvancingTheStateOfACardDispute) | **POST** /simulations/card_disputes/{card_dispute_id}/action | Simulates advancing the state of a card dispute |
| [**submitASandboxAchTransfer**](DefaultApi.md#submitASandboxAchTransfer) | **POST** /simulations/ach_transfers/{ach_transfer_id}/submit | Submit a Sandbox ACH Transfer |
| [**submitASandboxCheckDeposit**](DefaultApi.md#submitASandboxCheckDeposit) | **POST** /simulations/check_deposits/{check_deposit_id}/submit | Submit a Sandbox Check Deposit |
| [**submitASandboxWireTransfer**](DefaultApi.md#submitASandboxWireTransfer) | **POST** /simulations/wire_transfers/{wire_transfer_id}/submit | Submit a Sandbox Wire Transfer |
| [**updateACard**](DefaultApi.md#updateACard) | **PATCH** /cards/{card_id} | Update a Card |
| [**updateALimit**](DefaultApi.md#updateALimit) | **PATCH** /limits/{limit_id} | Update a Limit |
| [**updateAnAccount**](DefaultApi.md#updateAnAccount) | **PATCH** /accounts/{account_id} | Update an Account |
| [**updateAnAccountNumber**](DefaultApi.md#updateAnAccountNumber) | **PATCH** /account_numbers/{account_number_id} | Update an Account Number |
| [**updateAnEventSubscription**](DefaultApi.md#updateAnEventSubscription) | **PATCH** /event_subscriptions/{event_subscription_id} | Update an Event Subscription |
| [**updateAnExternalAccount**](DefaultApi.md#updateAnExternalAccount) | **PATCH** /external_accounts/{external_account_id} | Update an External Account |


<a id="actionARealTimeDecision"></a>
# **actionARealTimeDecision**
> RealTimeDecision actionARealTimeDecision(realTimeDecisionId, actionARealTimeDecisionParameters)

Action a Real-Time Decision

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String realTimeDecisionId = "real_time_decision_j76n2e810ezcg3zh5qtn"; // String | 
    ActionARealTimeDecisionParameters actionARealTimeDecisionParameters = new ActionARealTimeDecisionParameters(); // ActionARealTimeDecisionParameters | 
    try {
      RealTimeDecision result = apiInstance.actionARealTimeDecision(realTimeDecisionId, actionARealTimeDecisionParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#actionARealTimeDecision");
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
| **realTimeDecisionId** | **String**|  | |
| **actionARealTimeDecisionParameters** | [**ActionARealTimeDecisionParameters**](ActionARealTimeDecisionParameters.md)|  | |

### Return type

[**RealTimeDecision**](RealTimeDecision.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Real-Time Decision |  -  |
| **0** | Error |  -  |

<a id="approveACheckTransfer"></a>
# **approveACheckTransfer**
> CheckTransfer approveACheckTransfer(checkTransferId)

Approve a Check Transfer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String checkTransferId = "check_transfer_30b43acfu9vw8fyc4f5"; // String | 
    try {
      CheckTransfer result = apiInstance.approveACheckTransfer(checkTransferId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#approveACheckTransfer");
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
| **checkTransferId** | **String**|  | |

### Return type

[**CheckTransfer**](CheckTransfer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Check Transfer |  -  |
| **0** | Error |  -  |

<a id="approveAWireTransfer"></a>
# **approveAWireTransfer**
> WireTransfer approveAWireTransfer(wireTransferId)

Approve a Wire Transfer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String wireTransferId = "wire_transfer_5akynk7dqsq25qwk9q2u"; // String | 
    try {
      WireTransfer result = apiInstance.approveAWireTransfer(wireTransferId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#approveAWireTransfer");
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
| **wireTransferId** | **String**|  | |

### Return type

[**WireTransfer**](WireTransfer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Wire Transfer |  -  |
| **0** | Error |  -  |

<a id="approveAnAccountTransfer"></a>
# **approveAnAccountTransfer**
> AccountTransfer approveAnAccountTransfer(accountTransferId)

Approve an Account Transfer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountTransferId = "account_transfer_7k9qe1ysdgqztnt63l7n"; // String | 
    try {
      AccountTransfer result = apiInstance.approveAnAccountTransfer(accountTransferId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#approveAnAccountTransfer");
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
| **accountTransferId** | **String**|  | |

### Return type

[**AccountTransfer**](AccountTransfer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Account Transfer |  -  |
| **0** | Error |  -  |

<a id="approveAnAchTransfer"></a>
# **approveAnAchTransfer**
> AchTransfer approveAnAchTransfer(achTransferId)

Approve an ACH Transfer

Approves an ACH Transfer in a pending_approval state.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String achTransferId = "ach_transfer_uoxatyh3lt5evrsdvo7q"; // String | 
    try {
      AchTransfer result = apiInstance.approveAnAchTransfer(achTransferId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#approveAnAchTransfer");
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
| **achTransferId** | **String**|  | |

### Return type

[**AchTransfer**](AchTransfer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ACH Transfer |  -  |
| **0** | Error |  -  |

<a id="cancelAPendingAchTransfer"></a>
# **cancelAPendingAchTransfer**
> AchTransfer cancelAPendingAchTransfer(achTransferId)

Cancel a pending ACH Transfer

Cancels an ACH Transfer in a pending_approval state.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String achTransferId = "ach_transfer_uoxatyh3lt5evrsdvo7q"; // String | 
    try {
      AchTransfer result = apiInstance.cancelAPendingAchTransfer(achTransferId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#cancelAPendingAchTransfer");
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
| **achTransferId** | **String**|  | |

### Return type

[**AchTransfer**](AchTransfer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ACH Transfer |  -  |
| **0** | Error |  -  |

<a id="cancelAPendingCheckTransfer"></a>
# **cancelAPendingCheckTransfer**
> CheckTransfer cancelAPendingCheckTransfer(checkTransferId)

Cancel a pending Check Transfer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String checkTransferId = "check_transfer_30b43acfu9vw8fyc4f5"; // String | 
    try {
      CheckTransfer result = apiInstance.cancelAPendingCheckTransfer(checkTransferId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#cancelAPendingCheckTransfer");
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
| **checkTransferId** | **String**|  | |

### Return type

[**CheckTransfer**](CheckTransfer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Check Transfer |  -  |
| **0** | Error |  -  |

<a id="cancelAPendingWireTransfer"></a>
# **cancelAPendingWireTransfer**
> WireTransfer cancelAPendingWireTransfer(wireTransferId)

Cancel a pending Wire Transfer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String wireTransferId = "wire_transfer_5akynk7dqsq25qwk9q2u"; // String | 
    try {
      WireTransfer result = apiInstance.cancelAPendingWireTransfer(wireTransferId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#cancelAPendingWireTransfer");
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
| **wireTransferId** | **String**|  | |

### Return type

[**WireTransfer**](WireTransfer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Wire Transfer |  -  |
| **0** | Error |  -  |

<a id="cancelAnAccountTransfer"></a>
# **cancelAnAccountTransfer**
> AccountTransfer cancelAnAccountTransfer(accountTransferId)

Cancel an Account Transfer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountTransferId = "account_transfer_7k9qe1ysdgqztnt63l7n"; // String | 
    try {
      AccountTransfer result = apiInstance.cancelAnAccountTransfer(accountTransferId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#cancelAnAccountTransfer");
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
| **accountTransferId** | **String**|  | |

### Return type

[**AccountTransfer**](AccountTransfer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Account Transfer |  -  |
| **0** | Error |  -  |

<a id="closeAnAccount"></a>
# **closeAnAccount**
> Account closeAnAccount(accountId)

Close an Account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "account_in71c4amph0vgo2qllky"; // String | 
    try {
      Account result = apiInstance.closeAnAccount(accountId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#closeAnAccount");
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
| **accountId** | **String**|  | |

### Return type

[**Account**](Account.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Account |  -  |
| **0** | Error |  -  |

<a id="completeASandboxAccountTransfer"></a>
# **completeASandboxAccountTransfer**
> AccountTransfer completeASandboxAccountTransfer(accountTransferId)

Complete a Sandbox Account Transfer

If your account is configured to require approval for each transfer, this endpoint simulates the approval of an [Account Transfer](#account-transfers). You can also approve sandbox Account Transfers in the dashboard. This transfer must first have a &#x60;status&#x60; of &#x60;pending_approval&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountTransferId = "account_transfer_7k9qe1ysdgqztnt63l7n"; // String | 
    try {
      AccountTransfer result = apiInstance.completeASandboxAccountTransfer(accountTransferId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#completeASandboxAccountTransfer");
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
| **accountTransferId** | **String**|  | |

### Return type

[**AccountTransfer**](AccountTransfer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Account Transfer |  -  |
| **0** | Error |  -  |

<a id="completeASandboxRealTimePaymentsTransfer"></a>
# **completeASandboxRealTimePaymentsTransfer**
> RealTimePaymentsTransfer completeASandboxRealTimePaymentsTransfer(realTimePaymentsTransferId, completeASandboxRealTimePaymentsTransferParameters)

Complete a Sandbox Real Time Payments Transfer

Simulates submission of a Real Time Payments transfer and handling the response from the destination financial institution. This transfer must first have a &#x60;status&#x60; of &#x60;pending_submission&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String realTimePaymentsTransferId = "real_time_payments_transfer_iyuhl5kdn7ssmup83mvq"; // String | 
    CompleteASandboxRealTimePaymentsTransferParameters completeASandboxRealTimePaymentsTransferParameters = new CompleteASandboxRealTimePaymentsTransferParameters(); // CompleteASandboxRealTimePaymentsTransferParameters | 
    try {
      RealTimePaymentsTransfer result = apiInstance.completeASandboxRealTimePaymentsTransfer(realTimePaymentsTransferId, completeASandboxRealTimePaymentsTransferParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#completeASandboxRealTimePaymentsTransfer");
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
| **realTimePaymentsTransferId** | **String**|  | |
| **completeASandboxRealTimePaymentsTransferParameters** | [**CompleteASandboxRealTimePaymentsTransferParameters**](CompleteASandboxRealTimePaymentsTransferParameters.md)|  | |

### Return type

[**RealTimePaymentsTransfer**](RealTimePaymentsTransfer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Real Time Payments Transfer |  -  |
| **0** | Error |  -  |

<a id="createABookkeepingAccount"></a>
# **createABookkeepingAccount**
> BookkeepingAccount createABookkeepingAccount(createABookkeepingAccountParameters)

Create a Bookkeeping Account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateABookkeepingAccountParameters createABookkeepingAccountParameters = new CreateABookkeepingAccountParameters(); // CreateABookkeepingAccountParameters | 
    try {
      BookkeepingAccount result = apiInstance.createABookkeepingAccount(createABookkeepingAccountParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createABookkeepingAccount");
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
| **createABookkeepingAccountParameters** | [**CreateABookkeepingAccountParameters**](CreateABookkeepingAccountParameters.md)|  | |

### Return type

[**BookkeepingAccount**](BookkeepingAccount.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Bookkeeping Account |  -  |
| **0** | Error |  -  |

<a id="createABookkeepingEntrySet"></a>
# **createABookkeepingEntrySet**
> BookkeepingEntrySet createABookkeepingEntrySet(createABookkeepingEntrySetParameters)

Create a Bookkeeping Entry Set

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateABookkeepingEntrySetParameters createABookkeepingEntrySetParameters = new CreateABookkeepingEntrySetParameters(); // CreateABookkeepingEntrySetParameters | 
    try {
      BookkeepingEntrySet result = apiInstance.createABookkeepingEntrySet(createABookkeepingEntrySetParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createABookkeepingEntrySet");
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
| **createABookkeepingEntrySetParameters** | [**CreateABookkeepingEntrySetParameters**](CreateABookkeepingEntrySetParameters.md)|  | |

### Return type

[**BookkeepingEntrySet**](BookkeepingEntrySet.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Bookkeeping Entry Set |  -  |
| **0** | Error |  -  |

<a id="createACard"></a>
# **createACard**
> Card createACard(createACardParameters)

Create a Card

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateACardParameters createACardParameters = new CreateACardParameters(); // CreateACardParameters | 
    try {
      Card result = apiInstance.createACard(createACardParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createACard");
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
| **createACardParameters** | [**CreateACardParameters**](CreateACardParameters.md)|  | |

### Return type

[**Card**](Card.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Card |  -  |
| **0** | Error |  -  |

<a id="createACardDispute"></a>
# **createACardDispute**
> CardDispute createACardDispute(createACardDisputeParameters)

Create a Card Dispute

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateACardDisputeParameters createACardDisputeParameters = new CreateACardDisputeParameters(); // CreateACardDisputeParameters | 
    try {
      CardDispute result = apiInstance.createACardDispute(createACardDisputeParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createACardDispute");
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
| **createACardDisputeParameters** | [**CreateACardDisputeParameters**](CreateACardDisputeParameters.md)|  | |

### Return type

[**CardDispute**](CardDispute.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Card Dispute |  -  |
| **0** | Error |  -  |

<a id="createACardProfile"></a>
# **createACardProfile**
> CardProfile createACardProfile(createACardProfileParameters)

Create a Card Profile

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateACardProfileParameters createACardProfileParameters = new CreateACardProfileParameters(); // CreateACardProfileParameters | 
    try {
      CardProfile result = apiInstance.createACardProfile(createACardProfileParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createACardProfile");
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
| **createACardProfileParameters** | [**CreateACardProfileParameters**](CreateACardProfileParameters.md)|  | |

### Return type

[**CardProfile**](CardProfile.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Card Profile |  -  |
| **0** | Error |  -  |

<a id="createACheckDeposit"></a>
# **createACheckDeposit**
> CheckDeposit createACheckDeposit(createACheckDepositParameters)

Create a Check Deposit

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateACheckDepositParameters createACheckDepositParameters = new CreateACheckDepositParameters(); // CreateACheckDepositParameters | 
    try {
      CheckDeposit result = apiInstance.createACheckDeposit(createACheckDepositParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createACheckDeposit");
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
| **createACheckDepositParameters** | [**CreateACheckDepositParameters**](CreateACheckDepositParameters.md)|  | |

### Return type

[**CheckDeposit**](CheckDeposit.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Check Deposit |  -  |
| **0** | Error |  -  |

<a id="createACheckTransfer"></a>
# **createACheckTransfer**
> CheckTransfer createACheckTransfer(createACheckTransferParameters)

Create a Check Transfer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateACheckTransferParameters createACheckTransferParameters = new CreateACheckTransferParameters(); // CreateACheckTransferParameters | 
    try {
      CheckTransfer result = apiInstance.createACheckTransfer(createACheckTransferParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createACheckTransfer");
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
| **createACheckTransferParameters** | [**CreateACheckTransferParameters**](CreateACheckTransferParameters.md)|  | |

### Return type

[**CheckTransfer**](CheckTransfer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Check Transfer |  -  |
| **0** | Error |  -  |

<a id="createAFile"></a>
# **createAFile**
> File createAFile(_file, purpose, description)

Create a File

To upload a file to Increase, you&#39;ll need to send a request of Content-Type &#x60;multipart/form-data&#x60;. The request should contain the file you would like to upload, as well as the parameters for creating a file.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    File _file = new File("/path/to/file"); // File | The file contents. This should follow the specifications of [RFC 7578](https://datatracker.ietf.org/doc/html/rfc7578) which defines file transfers for the multipart/form-data protocol.
    String purpose = "check_image_front"; // String | What the File will be used for in Increase's systems.
    String description = "description_example"; // String | The description you choose to give the File.
    try {
      File result = apiInstance.createAFile(_file, purpose, description);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createAFile");
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
| **_file** | **File**| The file contents. This should follow the specifications of [RFC 7578](https://datatracker.ietf.org/doc/html/rfc7578) which defines file transfers for the multipart/form-data protocol. | |
| **purpose** | **String**| What the File will be used for in Increase&#39;s systems. | [enum: check_image_front, check_image_back, form_ss_4, identity_document, other, trust_formation_document, digital_wallet_artwork, digital_wallet_app_icon, document_request, entity_supplemental_document] |
| **description** | **String**| The description you choose to give the File. | [optional] |

### Return type

[**File**](File.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | File |  -  |
| **0** | Error |  -  |

<a id="createALimit"></a>
# **createALimit**
> Limit createALimit(createALimitParameters)

Create a Limit

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateALimitParameters createALimitParameters = new CreateALimitParameters(); // CreateALimitParameters | 
    try {
      Limit result = apiInstance.createALimit(createALimitParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createALimit");
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
| **createALimitParameters** | [**CreateALimitParameters**](CreateALimitParameters.md)|  | |

### Return type

[**Limit**](Limit.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Limit |  -  |
| **0** | Error |  -  |

<a id="createARealTimePaymentsTransfer"></a>
# **createARealTimePaymentsTransfer**
> RealTimePaymentsTransfer createARealTimePaymentsTransfer(createARealTimePaymentsTransferParameters)

Create a Real Time Payments Transfer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateARealTimePaymentsTransferParameters createARealTimePaymentsTransferParameters = new CreateARealTimePaymentsTransferParameters(); // CreateARealTimePaymentsTransferParameters | 
    try {
      RealTimePaymentsTransfer result = apiInstance.createARealTimePaymentsTransfer(createARealTimePaymentsTransferParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createARealTimePaymentsTransfer");
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
| **createARealTimePaymentsTransferParameters** | [**CreateARealTimePaymentsTransferParameters**](CreateARealTimePaymentsTransferParameters.md)|  | |

### Return type

[**RealTimePaymentsTransfer**](RealTimePaymentsTransfer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Real Time Payments Transfer |  -  |
| **0** | Error |  -  |

<a id="createASupplementalDocumentForAnEntity"></a>
# **createASupplementalDocumentForAnEntity**
> Entity createASupplementalDocumentForAnEntity(entityId, createASupplementalDocumentForAnEntityParameters)

Create a supplemental document for an Entity

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String entityId = "entity_n8y8tnk2p9339ti393yi"; // String | 
    CreateASupplementalDocumentForAnEntityParameters createASupplementalDocumentForAnEntityParameters = new CreateASupplementalDocumentForAnEntityParameters(); // CreateASupplementalDocumentForAnEntityParameters | 
    try {
      Entity result = apiInstance.createASupplementalDocumentForAnEntity(entityId, createASupplementalDocumentForAnEntityParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createASupplementalDocumentForAnEntity");
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
| **entityId** | **String**|  | |
| **createASupplementalDocumentForAnEntityParameters** | [**CreateASupplementalDocumentForAnEntityParameters**](CreateASupplementalDocumentForAnEntityParameters.md)|  | |

### Return type

[**Entity**](Entity.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Entity |  -  |
| **0** | Error |  -  |

<a id="createAWireDrawdownRequest"></a>
# **createAWireDrawdownRequest**
> WireDrawdownRequest createAWireDrawdownRequest(createAWireDrawdownRequestParameters)

Create a Wire Drawdown Request

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateAWireDrawdownRequestParameters createAWireDrawdownRequestParameters = new CreateAWireDrawdownRequestParameters(); // CreateAWireDrawdownRequestParameters | 
    try {
      WireDrawdownRequest result = apiInstance.createAWireDrawdownRequest(createAWireDrawdownRequestParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createAWireDrawdownRequest");
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
| **createAWireDrawdownRequestParameters** | [**CreateAWireDrawdownRequestParameters**](CreateAWireDrawdownRequestParameters.md)|  | |

### Return type

[**WireDrawdownRequest**](WireDrawdownRequest.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Wire Drawdown Request |  -  |
| **0** | Error |  -  |

<a id="createAWireTransfer"></a>
# **createAWireTransfer**
> WireTransfer createAWireTransfer(createAWireTransferParameters)

Create a Wire Transfer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateAWireTransferParameters createAWireTransferParameters = new CreateAWireTransferParameters(); // CreateAWireTransferParameters | 
    try {
      WireTransfer result = apiInstance.createAWireTransfer(createAWireTransferParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createAWireTransfer");
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
| **createAWireTransferParameters** | [**CreateAWireTransferParameters**](CreateAWireTransferParameters.md)|  | |

### Return type

[**WireTransfer**](WireTransfer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Wire Transfer |  -  |
| **0** | Error |  -  |

<a id="createAnAccount"></a>
# **createAnAccount**
> Account createAnAccount(createAnAccountParameters)

Create an Account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateAnAccountParameters createAnAccountParameters = new CreateAnAccountParameters(); // CreateAnAccountParameters | 
    try {
      Account result = apiInstance.createAnAccount(createAnAccountParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createAnAccount");
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
| **createAnAccountParameters** | [**CreateAnAccountParameters**](CreateAnAccountParameters.md)|  | |

### Return type

[**Account**](Account.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Account |  -  |
| **0** | Error |  -  |

<a id="createAnAccountNumber"></a>
# **createAnAccountNumber**
> AccountNumber createAnAccountNumber(createAnAccountNumberParameters)

Create an Account Number

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateAnAccountNumberParameters createAnAccountNumberParameters = new CreateAnAccountNumberParameters(); // CreateAnAccountNumberParameters | 
    try {
      AccountNumber result = apiInstance.createAnAccountNumber(createAnAccountNumberParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createAnAccountNumber");
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
| **createAnAccountNumberParameters** | [**CreateAnAccountNumberParameters**](CreateAnAccountNumberParameters.md)|  | |

### Return type

[**AccountNumber**](AccountNumber.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Account Number |  -  |
| **0** | Error |  -  |

<a id="createAnAccountTransfer"></a>
# **createAnAccountTransfer**
> AccountTransfer createAnAccountTransfer(createAnAccountTransferParameters)

Create an Account Transfer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateAnAccountTransferParameters createAnAccountTransferParameters = new CreateAnAccountTransferParameters(); // CreateAnAccountTransferParameters | 
    try {
      AccountTransfer result = apiInstance.createAnAccountTransfer(createAnAccountTransferParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createAnAccountTransfer");
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
| **createAnAccountTransferParameters** | [**CreateAnAccountTransferParameters**](CreateAnAccountTransferParameters.md)|  | |

### Return type

[**AccountTransfer**](AccountTransfer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Account Transfer |  -  |
| **0** | Error |  -  |

<a id="createAnAchPrenotification"></a>
# **createAnAchPrenotification**
> AchPrenotification createAnAchPrenotification(createAnAchPrenotificationParameters)

Create an ACH Prenotification

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateAnAchPrenotificationParameters createAnAchPrenotificationParameters = new CreateAnAchPrenotificationParameters(); // CreateAnAchPrenotificationParameters | 
    try {
      AchPrenotification result = apiInstance.createAnAchPrenotification(createAnAchPrenotificationParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createAnAchPrenotification");
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
| **createAnAchPrenotificationParameters** | [**CreateAnAchPrenotificationParameters**](CreateAnAchPrenotificationParameters.md)|  | |

### Return type

[**AchPrenotification**](AchPrenotification.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ACH Prenotification |  -  |
| **0** | Error |  -  |

<a id="createAnAchReturn"></a>
# **createAnAchReturn**
> InboundAchTransferReturn createAnAchReturn(createAnAchReturnParameters)

Create an ACH Return

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateAnAchReturnParameters createAnAchReturnParameters = new CreateAnAchReturnParameters(); // CreateAnAchReturnParameters | 
    try {
      InboundAchTransferReturn result = apiInstance.createAnAchReturn(createAnAchReturnParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createAnAchReturn");
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
| **createAnAchReturnParameters** | [**CreateAnAchReturnParameters**](CreateAnAchReturnParameters.md)|  | |

### Return type

[**InboundAchTransferReturn**](InboundAchTransferReturn.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Inbound ACH Transfer Return |  -  |
| **0** | Error |  -  |

<a id="createAnAchTransfer"></a>
# **createAnAchTransfer**
> AchTransfer createAnAchTransfer(createAnAchTransferParameters)

Create an ACH Transfer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateAnAchTransferParameters createAnAchTransferParameters = new CreateAnAchTransferParameters(); // CreateAnAchTransferParameters | 
    try {
      AchTransfer result = apiInstance.createAnAchTransfer(createAnAchTransferParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createAnAchTransfer");
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
| **createAnAchTransferParameters** | [**CreateAnAchTransferParameters**](CreateAnAchTransferParameters.md)|  | |

### Return type

[**AchTransfer**](AchTransfer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ACH Transfer |  -  |
| **0** | Error |  -  |

<a id="createAnEntity"></a>
# **createAnEntity**
> Entity createAnEntity(createAnEntityParameters)

Create an Entity

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateAnEntityParameters createAnEntityParameters = new CreateAnEntityParameters(); // CreateAnEntityParameters | 
    try {
      Entity result = apiInstance.createAnEntity(createAnEntityParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createAnEntity");
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
| **createAnEntityParameters** | [**CreateAnEntityParameters**](CreateAnEntityParameters.md)|  | |

### Return type

[**Entity**](Entity.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Entity |  -  |
| **0** | Error |  -  |

<a id="createAnEventSubscription"></a>
# **createAnEventSubscription**
> EventSubscription createAnEventSubscription(createAnEventSubscriptionParameters)

Create an Event Subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateAnEventSubscriptionParameters createAnEventSubscriptionParameters = new CreateAnEventSubscriptionParameters(); // CreateAnEventSubscriptionParameters | 
    try {
      EventSubscription result = apiInstance.createAnEventSubscription(createAnEventSubscriptionParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createAnEventSubscription");
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
| **createAnEventSubscriptionParameters** | [**CreateAnEventSubscriptionParameters**](CreateAnEventSubscriptionParameters.md)|  | |

### Return type

[**EventSubscription**](EventSubscription.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Event Subscription |  -  |
| **0** | Error |  -  |

<a id="createAnExport"></a>
# **createAnExport**
> Export createAnExport(createAnExportParameters)

Create an Export

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateAnExportParameters createAnExportParameters = new CreateAnExportParameters(); // CreateAnExportParameters | 
    try {
      Export result = apiInstance.createAnExport(createAnExportParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createAnExport");
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
| **createAnExportParameters** | [**CreateAnExportParameters**](CreateAnExportParameters.md)|  | |

### Return type

[**Export**](Export.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Export |  -  |
| **0** | Error |  -  |

<a id="createAnExternalAccount"></a>
# **createAnExternalAccount**
> ExternalAccount createAnExternalAccount(createAnExternalAccountParameters)

Create an External Account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateAnExternalAccountParameters createAnExternalAccountParameters = new CreateAnExternalAccountParameters(); // CreateAnExternalAccountParameters | 
    try {
      ExternalAccount result = apiInstance.createAnExternalAccount(createAnExternalAccountParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createAnExternalAccount");
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
| **createAnExternalAccountParameters** | [**CreateAnExternalAccountParameters**](CreateAnExternalAccountParameters.md)|  | |

### Return type

[**ExternalAccount**](ExternalAccount.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | External Account |  -  |
| **0** | Error |  -  |

<a id="depositASandboxCheckTransfer"></a>
# **depositASandboxCheckTransfer**
> CheckTransfer depositASandboxCheckTransfer(checkTransferId)

Deposit a Sandbox Check Transfer

Simulates a [Check Transfer](#check-transfers) being deposited at a bank. This transfer must first have a &#x60;status&#x60; of &#x60;mailed&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String checkTransferId = "check_transfer_30b43acfu9vw8fyc4f5"; // String | 
    try {
      CheckTransfer result = apiInstance.depositASandboxCheckTransfer(checkTransferId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#depositASandboxCheckTransfer");
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
| **checkTransferId** | **String**|  | |

### Return type

[**CheckTransfer**](CheckTransfer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Check Transfer |  -  |
| **0** | Error |  -  |

<a id="listAccountNumbers"></a>
# **listAccountNumbers**
> AccountNumberList listAccountNumbers(cursor, limit, status, accountId, createdAtAfter, createdAtBefore, createdAtOnOrAfter, createdAtOnOrBefore)

List Account Numbers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String cursor = "cursor_example"; // String | 
    Integer limit = 56; // Integer | 
    String status = "active"; // String | 
    String accountId = "accountId_example"; // String | 
    OffsetDateTime createdAtAfter = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime createdAtBefore = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime createdAtOnOrAfter = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime createdAtOnOrBefore = OffsetDateTime.now(); // OffsetDateTime | 
    try {
      AccountNumberList result = apiInstance.listAccountNumbers(cursor, limit, status, accountId, createdAtAfter, createdAtBefore, createdAtOnOrAfter, createdAtOnOrBefore);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listAccountNumbers");
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
| **cursor** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] |
| **status** | **String**|  | [optional] [enum: active, disabled, canceled] |
| **accountId** | **String**|  | [optional] |
| **createdAtAfter** | **OffsetDateTime**|  | [optional] |
| **createdAtBefore** | **OffsetDateTime**|  | [optional] |
| **createdAtOnOrAfter** | **OffsetDateTime**|  | [optional] |
| **createdAtOnOrBefore** | **OffsetDateTime**|  | [optional] |

### Return type

[**AccountNumberList**](AccountNumberList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Account Number List |  -  |
| **0** | Error |  -  |

<a id="listAccountStatements"></a>
# **listAccountStatements**
> AccountStatementList listAccountStatements(cursor, limit, accountId, statementPeriodStartAfter, statementPeriodStartBefore, statementPeriodStartOnOrAfter, statementPeriodStartOnOrBefore)

List Account Statements

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String cursor = "cursor_example"; // String | 
    Integer limit = 56; // Integer | 
    String accountId = "account_in71c4amph0vgo2qllky"; // String | 
    OffsetDateTime statementPeriodStartAfter = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime statementPeriodStartBefore = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime statementPeriodStartOnOrAfter = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime statementPeriodStartOnOrBefore = OffsetDateTime.now(); // OffsetDateTime | 
    try {
      AccountStatementList result = apiInstance.listAccountStatements(cursor, limit, accountId, statementPeriodStartAfter, statementPeriodStartBefore, statementPeriodStartOnOrAfter, statementPeriodStartOnOrBefore);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listAccountStatements");
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
| **cursor** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] |
| **accountId** | **String**|  | [optional] |
| **statementPeriodStartAfter** | **OffsetDateTime**|  | [optional] |
| **statementPeriodStartBefore** | **OffsetDateTime**|  | [optional] |
| **statementPeriodStartOnOrAfter** | **OffsetDateTime**|  | [optional] |
| **statementPeriodStartOnOrBefore** | **OffsetDateTime**|  | [optional] |

### Return type

[**AccountStatementList**](AccountStatementList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Account Statement List |  -  |
| **0** | Error |  -  |

<a id="listAccountTransfers"></a>
# **listAccountTransfers**
> AccountTransferList listAccountTransfers(cursor, limit, accountId, createdAtAfter, createdAtBefore, createdAtOnOrAfter, createdAtOnOrBefore)

List Account Transfers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String cursor = "cursor_example"; // String | 
    Integer limit = 56; // Integer | 
    String accountId = "account_in71c4amph0vgo2qllky"; // String | 
    OffsetDateTime createdAtAfter = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime createdAtBefore = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime createdAtOnOrAfter = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime createdAtOnOrBefore = OffsetDateTime.now(); // OffsetDateTime | 
    try {
      AccountTransferList result = apiInstance.listAccountTransfers(cursor, limit, accountId, createdAtAfter, createdAtBefore, createdAtOnOrAfter, createdAtOnOrBefore);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listAccountTransfers");
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
| **cursor** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] |
| **accountId** | **String**|  | [optional] |
| **createdAtAfter** | **OffsetDateTime**|  | [optional] |
| **createdAtBefore** | **OffsetDateTime**|  | [optional] |
| **createdAtOnOrAfter** | **OffsetDateTime**|  | [optional] |
| **createdAtOnOrBefore** | **OffsetDateTime**|  | [optional] |

### Return type

[**AccountTransferList**](AccountTransferList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Account Transfer List |  -  |
| **0** | Error |  -  |

<a id="listAccounts"></a>
# **listAccounts**
> AccountList listAccounts(cursor, limit, entityId, status, createdAtAfter, createdAtBefore, createdAtOnOrAfter, createdAtOnOrBefore)

List Accounts

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String cursor = "cursor_example"; // String | 
    Integer limit = 56; // Integer | 
    String entityId = "entity_n8y8tnk2p9339ti393yi"; // String | 
    String status = "open"; // String | 
    OffsetDateTime createdAtAfter = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime createdAtBefore = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime createdAtOnOrAfter = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime createdAtOnOrBefore = OffsetDateTime.now(); // OffsetDateTime | 
    try {
      AccountList result = apiInstance.listAccounts(cursor, limit, entityId, status, createdAtAfter, createdAtBefore, createdAtOnOrAfter, createdAtOnOrBefore);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listAccounts");
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
| **cursor** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] |
| **entityId** | **String**|  | [optional] |
| **status** | **String**|  | [optional] [enum: open, closed] |
| **createdAtAfter** | **OffsetDateTime**|  | [optional] |
| **createdAtBefore** | **OffsetDateTime**|  | [optional] |
| **createdAtOnOrAfter** | **OffsetDateTime**|  | [optional] |
| **createdAtOnOrBefore** | **OffsetDateTime**|  | [optional] |

### Return type

[**AccountList**](AccountList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Account List |  -  |
| **0** | Error |  -  |

<a id="listAchPrenotifications"></a>
# **listAchPrenotifications**
> AchPrenotificationList listAchPrenotifications(cursor, limit, createdAtAfter, createdAtBefore, createdAtOnOrAfter, createdAtOnOrBefore)

List ACH Prenotifications

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String cursor = "cursor_example"; // String | 
    Integer limit = 56; // Integer | 
    OffsetDateTime createdAtAfter = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime createdAtBefore = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime createdAtOnOrAfter = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime createdAtOnOrBefore = OffsetDateTime.now(); // OffsetDateTime | 
    try {
      AchPrenotificationList result = apiInstance.listAchPrenotifications(cursor, limit, createdAtAfter, createdAtBefore, createdAtOnOrAfter, createdAtOnOrBefore);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listAchPrenotifications");
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
| **cursor** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] |
| **createdAtAfter** | **OffsetDateTime**|  | [optional] |
| **createdAtBefore** | **OffsetDateTime**|  | [optional] |
| **createdAtOnOrAfter** | **OffsetDateTime**|  | [optional] |
| **createdAtOnOrBefore** | **OffsetDateTime**|  | [optional] |

### Return type

[**AchPrenotificationList**](AchPrenotificationList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ACH Prenotification List |  -  |
| **0** | Error |  -  |

<a id="listAchTransfers"></a>
# **listAchTransfers**
> AchTransferList listAchTransfers(cursor, limit, accountId, externalAccountId, createdAtAfter, createdAtBefore, createdAtOnOrAfter, createdAtOnOrBefore)

List ACH Transfers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String cursor = "cursor_example"; // String | 
    Integer limit = 56; // Integer | 
    String accountId = "account_in71c4amph0vgo2qllky"; // String | 
    String externalAccountId = "externalAccountId_example"; // String | 
    OffsetDateTime createdAtAfter = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime createdAtBefore = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime createdAtOnOrAfter = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime createdAtOnOrBefore = OffsetDateTime.now(); // OffsetDateTime | 
    try {
      AchTransferList result = apiInstance.listAchTransfers(cursor, limit, accountId, externalAccountId, createdAtAfter, createdAtBefore, createdAtOnOrAfter, createdAtOnOrBefore);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listAchTransfers");
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
| **cursor** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] |
| **accountId** | **String**|  | [optional] |
| **externalAccountId** | **String**|  | [optional] |
| **createdAtAfter** | **OffsetDateTime**|  | [optional] |
| **createdAtBefore** | **OffsetDateTime**|  | [optional] |
| **createdAtOnOrAfter** | **OffsetDateTime**|  | [optional] |
| **createdAtOnOrBefore** | **OffsetDateTime**|  | [optional] |

### Return type

[**AchTransferList**](AchTransferList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ACH Transfer List |  -  |
| **0** | Error |  -  |

<a id="listBookkeepingAccounts"></a>
# **listBookkeepingAccounts**
> BookkeepingAccountList listBookkeepingAccounts(cursor, limit)

List Bookkeeping Accounts

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String cursor = "cursor_example"; // String | 
    Integer limit = 56; // Integer | 
    try {
      BookkeepingAccountList result = apiInstance.listBookkeepingAccounts(cursor, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listBookkeepingAccounts");
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
| **cursor** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] |

### Return type

[**BookkeepingAccountList**](BookkeepingAccountList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Bookkeeping Account List |  -  |
| **0** | Error |  -  |

<a id="listBookkeepingEntries"></a>
# **listBookkeepingEntries**
> BookkeepingEntryList listBookkeepingEntries(cursor, limit)

List Bookkeeping Entries

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String cursor = "cursor_example"; // String | 
    Integer limit = 56; // Integer | 
    try {
      BookkeepingEntryList result = apiInstance.listBookkeepingEntries(cursor, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listBookkeepingEntries");
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
| **cursor** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] |

### Return type

[**BookkeepingEntryList**](BookkeepingEntryList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Bookkeeping Entry List |  -  |
| **0** | Error |  -  |

<a id="listCardDisputes"></a>
# **listCardDisputes**
> CardDisputeList listCardDisputes(cursor, limit, createdAtAfter, createdAtBefore, createdAtOnOrAfter, createdAtOnOrBefore, statusIn)

List Card Disputes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String cursor = "cursor_example"; // String | 
    Integer limit = 56; // Integer | 
    OffsetDateTime createdAtAfter = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime createdAtBefore = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime createdAtOnOrAfter = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime createdAtOnOrBefore = OffsetDateTime.now(); // OffsetDateTime | 
    List<String> statusIn = Arrays.asList(); // List<String> | 
    try {
      CardDisputeList result = apiInstance.listCardDisputes(cursor, limit, createdAtAfter, createdAtBefore, createdAtOnOrAfter, createdAtOnOrBefore, statusIn);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listCardDisputes");
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
| **cursor** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] |
| **createdAtAfter** | **OffsetDateTime**|  | [optional] |
| **createdAtBefore** | **OffsetDateTime**|  | [optional] |
| **createdAtOnOrAfter** | **OffsetDateTime**|  | [optional] |
| **createdAtOnOrBefore** | **OffsetDateTime**|  | [optional] |
| **statusIn** | [**List&lt;String&gt;**](String.md)|  | [optional] [enum: pending_reviewing, accepted, rejected] |

### Return type

[**CardDisputeList**](CardDisputeList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Card Dispute List |  -  |
| **0** | Error |  -  |

<a id="listCardProfiles"></a>
# **listCardProfiles**
> CardProfileList listCardProfiles(cursor, limit, statusIn)

List Card Profiles

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String cursor = "cursor_example"; // String | 
    Integer limit = 56; // Integer | 
    List<String> statusIn = Arrays.asList(); // List<String> | 
    try {
      CardProfileList result = apiInstance.listCardProfiles(cursor, limit, statusIn);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listCardProfiles");
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
| **cursor** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] |
| **statusIn** | [**List&lt;String&gt;**](String.md)|  | [optional] [enum: pending, rejected, active, archived] |

### Return type

[**CardProfileList**](CardProfileList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Card Profile List |  -  |
| **0** | Error |  -  |

<a id="listCards"></a>
# **listCards**
> CardList listCards(cursor, limit, accountId, createdAtAfter, createdAtBefore, createdAtOnOrAfter, createdAtOnOrBefore)

List Cards

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String cursor = "cursor_example"; // String | 
    Integer limit = 56; // Integer | 
    String accountId = "account_in71c4amph0vgo2qllky"; // String | 
    OffsetDateTime createdAtAfter = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime createdAtBefore = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime createdAtOnOrAfter = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime createdAtOnOrBefore = OffsetDateTime.now(); // OffsetDateTime | 
    try {
      CardList result = apiInstance.listCards(cursor, limit, accountId, createdAtAfter, createdAtBefore, createdAtOnOrAfter, createdAtOnOrBefore);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listCards");
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
| **cursor** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] |
| **accountId** | **String**|  | [optional] |
| **createdAtAfter** | **OffsetDateTime**|  | [optional] |
| **createdAtBefore** | **OffsetDateTime**|  | [optional] |
| **createdAtOnOrAfter** | **OffsetDateTime**|  | [optional] |
| **createdAtOnOrBefore** | **OffsetDateTime**|  | [optional] |

### Return type

[**CardList**](CardList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Card List |  -  |
| **0** | Error |  -  |

<a id="listCheckDeposits"></a>
# **listCheckDeposits**
> CheckDepositList listCheckDeposits(cursor, limit, accountId, createdAtAfter, createdAtBefore, createdAtOnOrAfter, createdAtOnOrBefore)

List Check Deposits

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String cursor = "cursor_example"; // String | 
    Integer limit = 56; // Integer | 
    String accountId = "account_in71c4amph0vgo2qllky"; // String | 
    OffsetDateTime createdAtAfter = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime createdAtBefore = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime createdAtOnOrAfter = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime createdAtOnOrBefore = OffsetDateTime.now(); // OffsetDateTime | 
    try {
      CheckDepositList result = apiInstance.listCheckDeposits(cursor, limit, accountId, createdAtAfter, createdAtBefore, createdAtOnOrAfter, createdAtOnOrBefore);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listCheckDeposits");
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
| **cursor** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] |
| **accountId** | **String**|  | [optional] |
| **createdAtAfter** | **OffsetDateTime**|  | [optional] |
| **createdAtBefore** | **OffsetDateTime**|  | [optional] |
| **createdAtOnOrAfter** | **OffsetDateTime**|  | [optional] |
| **createdAtOnOrBefore** | **OffsetDateTime**|  | [optional] |

### Return type

[**CheckDepositList**](CheckDepositList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Check Deposit List |  -  |
| **0** | Error |  -  |

<a id="listCheckTransfers"></a>
# **listCheckTransfers**
> CheckTransferList listCheckTransfers(cursor, limit, accountId, createdAtAfter, createdAtBefore, createdAtOnOrAfter, createdAtOnOrBefore)

List Check Transfers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String cursor = "cursor_example"; // String | 
    Integer limit = 56; // Integer | 
    String accountId = "account_in71c4amph0vgo2qllky"; // String | 
    OffsetDateTime createdAtAfter = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime createdAtBefore = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime createdAtOnOrAfter = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime createdAtOnOrBefore = OffsetDateTime.now(); // OffsetDateTime | 
    try {
      CheckTransferList result = apiInstance.listCheckTransfers(cursor, limit, accountId, createdAtAfter, createdAtBefore, createdAtOnOrAfter, createdAtOnOrBefore);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listCheckTransfers");
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
| **cursor** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] |
| **accountId** | **String**|  | [optional] |
| **createdAtAfter** | **OffsetDateTime**|  | [optional] |
| **createdAtBefore** | **OffsetDateTime**|  | [optional] |
| **createdAtOnOrAfter** | **OffsetDateTime**|  | [optional] |
| **createdAtOnOrBefore** | **OffsetDateTime**|  | [optional] |

### Return type

[**CheckTransferList**](CheckTransferList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Check Transfer List |  -  |
| **0** | Error |  -  |

<a id="listDeclinedTransactions"></a>
# **listDeclinedTransactions**
> DeclinedTransactionList listDeclinedTransactions(cursor, limit, accountId, createdAtAfter, createdAtBefore, createdAtOnOrAfter, createdAtOnOrBefore, routeId)

List Declined Transactions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String cursor = "cursor_example"; // String | 
    Integer limit = 56; // Integer | 
    String accountId = "accountId_example"; // String | 
    OffsetDateTime createdAtAfter = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime createdAtBefore = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime createdAtOnOrAfter = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime createdAtOnOrBefore = OffsetDateTime.now(); // OffsetDateTime | 
    String routeId = "routeId_example"; // String | 
    try {
      DeclinedTransactionList result = apiInstance.listDeclinedTransactions(cursor, limit, accountId, createdAtAfter, createdAtBefore, createdAtOnOrAfter, createdAtOnOrBefore, routeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listDeclinedTransactions");
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
| **cursor** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] |
| **accountId** | **String**|  | [optional] |
| **createdAtAfter** | **OffsetDateTime**|  | [optional] |
| **createdAtBefore** | **OffsetDateTime**|  | [optional] |
| **createdAtOnOrAfter** | **OffsetDateTime**|  | [optional] |
| **createdAtOnOrBefore** | **OffsetDateTime**|  | [optional] |
| **routeId** | **String**|  | [optional] |

### Return type

[**DeclinedTransactionList**](DeclinedTransactionList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Declined Transaction List |  -  |
| **0** | Error |  -  |

<a id="listDigitalWalletTokens"></a>
# **listDigitalWalletTokens**
> DigitalWalletTokenList listDigitalWalletTokens(cursor, limit, cardId, createdAtAfter, createdAtBefore, createdAtOnOrAfter, createdAtOnOrBefore)

List Digital Wallet Tokens

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String cursor = "cursor_example"; // String | 
    Integer limit = 56; // Integer | 
    String cardId = "card_oubs0hwk5rn6knuecxg2"; // String | 
    OffsetDateTime createdAtAfter = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime createdAtBefore = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime createdAtOnOrAfter = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime createdAtOnOrBefore = OffsetDateTime.now(); // OffsetDateTime | 
    try {
      DigitalWalletTokenList result = apiInstance.listDigitalWalletTokens(cursor, limit, cardId, createdAtAfter, createdAtBefore, createdAtOnOrAfter, createdAtOnOrBefore);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listDigitalWalletTokens");
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
| **cursor** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] |
| **cardId** | **String**|  | [optional] |
| **createdAtAfter** | **OffsetDateTime**|  | [optional] |
| **createdAtBefore** | **OffsetDateTime**|  | [optional] |
| **createdAtOnOrAfter** | **OffsetDateTime**|  | [optional] |
| **createdAtOnOrBefore** | **OffsetDateTime**|  | [optional] |

### Return type

[**DigitalWalletTokenList**](DigitalWalletTokenList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Digital Wallet Token List |  -  |
| **0** | Error |  -  |

<a id="listDocuments"></a>
# **listDocuments**
> DocumentList listDocuments(cursor, limit, entityId, categoryIn, createdAtAfter, createdAtBefore, createdAtOnOrAfter, createdAtOnOrBefore)

List Documents

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String cursor = "cursor_example"; // String | 
    Integer limit = 56; // Integer | 
    String entityId = "entityId_example"; // String | 
    List<String> categoryIn = Arrays.asList(); // List<String> | 
    OffsetDateTime createdAtAfter = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime createdAtBefore = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime createdAtOnOrAfter = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime createdAtOnOrBefore = OffsetDateTime.now(); // OffsetDateTime | 
    try {
      DocumentList result = apiInstance.listDocuments(cursor, limit, entityId, categoryIn, createdAtAfter, createdAtBefore, createdAtOnOrAfter, createdAtOnOrBefore);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listDocuments");
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
| **cursor** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] |
| **entityId** | **String**|  | [optional] |
| **categoryIn** | [**List&lt;String&gt;**](String.md)|  | [optional] [enum: account_opening_disclosures, anti_money_laundering_policy, anti_money_laundering_procedures, audit_report, background_checks, business_continuity_plan, collections_policy, complaints_policy, complaint_report, compliance_report, compliance_staffing_plan, compliance_management_system_policy, consumer_privacy_notice, consumer_protection_policy, corporate_formation_document, credit_monitoring_report, customer_information_program_policy, electronic_funds_tranfer_act_policy, employee_overview, end_user_terms_of_service, e_sign_policy, financial_statement, form_1099_int, fraud_prevention_policy, funds_availability_policy, funds_availability_disclosure, funds_flow_diagram, gramm_leach_bliley_act_policy, information_security_policy, insurance_policy, investor_presentation, loan_application_processing_policy, management_biography, marketing_and_advertising_policy, network_security_diagram, onboarding_questionnaire, penetration_test_report, program_risk_assessment, security_audit_report, servicing_policy, transaction_monitoring_report, truth_in_savings_act_policy, underwriting_policy, vendor_list, vendor_management_policy, vendor_risk_management_report, volume_forecast] |
| **createdAtAfter** | **OffsetDateTime**|  | [optional] |
| **createdAtBefore** | **OffsetDateTime**|  | [optional] |
| **createdAtOnOrAfter** | **OffsetDateTime**|  | [optional] |
| **createdAtOnOrBefore** | **OffsetDateTime**|  | [optional] |

### Return type

[**DocumentList**](DocumentList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Document List |  -  |
| **0** | Error |  -  |

<a id="listEntities"></a>
# **listEntities**
> EntityList listEntities(cursor, limit, createdAtAfter, createdAtBefore, createdAtOnOrAfter, createdAtOnOrBefore)

List Entities

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String cursor = "cursor_example"; // String | 
    Integer limit = 56; // Integer | 
    OffsetDateTime createdAtAfter = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime createdAtBefore = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime createdAtOnOrAfter = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime createdAtOnOrBefore = OffsetDateTime.now(); // OffsetDateTime | 
    try {
      EntityList result = apiInstance.listEntities(cursor, limit, createdAtAfter, createdAtBefore, createdAtOnOrAfter, createdAtOnOrBefore);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listEntities");
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
| **cursor** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] |
| **createdAtAfter** | **OffsetDateTime**|  | [optional] |
| **createdAtBefore** | **OffsetDateTime**|  | [optional] |
| **createdAtOnOrAfter** | **OffsetDateTime**|  | [optional] |
| **createdAtOnOrBefore** | **OffsetDateTime**|  | [optional] |

### Return type

[**EntityList**](EntityList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Entity List |  -  |
| **0** | Error |  -  |

<a id="listEventSubscriptions"></a>
# **listEventSubscriptions**
> EventSubscriptionList listEventSubscriptions(cursor, limit)

List Event Subscriptions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String cursor = "cursor_example"; // String | 
    Integer limit = 56; // Integer | 
    try {
      EventSubscriptionList result = apiInstance.listEventSubscriptions(cursor, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listEventSubscriptions");
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
| **cursor** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] |

### Return type

[**EventSubscriptionList**](EventSubscriptionList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Event Subscription List |  -  |
| **0** | Error |  -  |

<a id="listEvents"></a>
# **listEvents**
> EventList listEvents(cursor, limit, createdAtAfter, createdAtBefore, createdAtOnOrAfter, createdAtOnOrBefore, categoryIn, associatedObjectId)

List Events

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String cursor = "cursor_example"; // String | 
    Integer limit = 56; // Integer | 
    OffsetDateTime createdAtAfter = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime createdAtBefore = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime createdAtOnOrAfter = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime createdAtOnOrBefore = OffsetDateTime.now(); // OffsetDateTime | 
    List<String> categoryIn = Arrays.asList(); // List<String> | 
    String associatedObjectId = "associatedObjectId_example"; // String | 
    try {
      EventList result = apiInstance.listEvents(cursor, limit, createdAtAfter, createdAtBefore, createdAtOnOrAfter, createdAtOnOrBefore, categoryIn, associatedObjectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listEvents");
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
| **cursor** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] |
| **createdAtAfter** | **OffsetDateTime**|  | [optional] |
| **createdAtBefore** | **OffsetDateTime**|  | [optional] |
| **createdAtOnOrAfter** | **OffsetDateTime**|  | [optional] |
| **createdAtOnOrBefore** | **OffsetDateTime**|  | [optional] |
| **categoryIn** | [**List&lt;String&gt;**](String.md)|  | [optional] [enum: account.created, account.updated, account_number.created, account_number.updated, account_statement.created, account_transfer.created, account_transfer.updated, ach_prenotification.created, ach_prenotification.updated, ach_transfer.created, ach_transfer.updated, card.created, card.updated, card_payment.created, card_payment.updated, card_dispute.created, card_dispute.updated, check_deposit.created, check_deposit.updated, check_transfer.created, check_transfer.updated, declined_transaction.created, digital_wallet_token.created, digital_wallet_token.updated, document.created, entity.created, entity.updated, external_account.created, file.created, group.updated, group.heartbeat, inbound_ach_transfer_return.created, inbound_ach_transfer_return.updated, inbound_wire_drawdown_request.created, oauth_connection.created, oauth_connection.deactivated, pending_transaction.created, pending_transaction.updated, real_time_decision.card_authorization_requested, real_time_decision.digital_wallet_token_requested, real_time_decision.digital_wallet_authentication_requested, real_time_payments_transfer.created, real_time_payments_transfer.updated, real_time_payments_request_for_payment.created, real_time_payments_request_for_payment.updated, transaction.created, wire_drawdown_request.created, wire_drawdown_request.updated, wire_transfer.created, wire_transfer.updated] |
| **associatedObjectId** | **String**|  | [optional] |

### Return type

[**EventList**](EventList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Event List |  -  |
| **0** | Error |  -  |

<a id="listExports"></a>
# **listExports**
> ExportList listExports(cursor, limit)

List Exports

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String cursor = "cursor_example"; // String | 
    Integer limit = 56; // Integer | 
    try {
      ExportList result = apiInstance.listExports(cursor, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listExports");
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
| **cursor** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] |

### Return type

[**ExportList**](ExportList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Export List |  -  |
| **0** | Error |  -  |

<a id="listExternalAccounts"></a>
# **listExternalAccounts**
> ExternalAccountList listExternalAccounts(cursor, limit, statusIn)

List External Accounts

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String cursor = "cursor_example"; // String | 
    Integer limit = 56; // Integer | 
    List<String> statusIn = Arrays.asList(); // List<String> | 
    try {
      ExternalAccountList result = apiInstance.listExternalAccounts(cursor, limit, statusIn);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listExternalAccounts");
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
| **cursor** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] |
| **statusIn** | [**List&lt;String&gt;**](String.md)|  | [optional] [enum: active, archived] |

### Return type

[**ExternalAccountList**](ExternalAccountList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | External Account List |  -  |
| **0** | Error |  -  |

<a id="listFiles"></a>
# **listFiles**
> FileList listFiles(cursor, limit, createdAtAfter, createdAtBefore, createdAtOnOrAfter, createdAtOnOrBefore, purposeIn)

List Files

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String cursor = "cursor_example"; // String | 
    Integer limit = 56; // Integer | 
    OffsetDateTime createdAtAfter = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime createdAtBefore = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime createdAtOnOrAfter = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime createdAtOnOrBefore = OffsetDateTime.now(); // OffsetDateTime | 
    List<String> purposeIn = Arrays.asList(); // List<String> | 
    try {
      FileList result = apiInstance.listFiles(cursor, limit, createdAtAfter, createdAtBefore, createdAtOnOrAfter, createdAtOnOrBefore, purposeIn);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listFiles");
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
| **cursor** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] |
| **createdAtAfter** | **OffsetDateTime**|  | [optional] |
| **createdAtBefore** | **OffsetDateTime**|  | [optional] |
| **createdAtOnOrAfter** | **OffsetDateTime**|  | [optional] |
| **createdAtOnOrBefore** | **OffsetDateTime**|  | [optional] |
| **purposeIn** | [**List&lt;String&gt;**](String.md)|  | [optional] [enum: check_image_front, check_image_back, form_1099_int, form_ss_4, identity_document, increase_statement, other, trust_formation_document, digital_wallet_artwork, digital_wallet_app_icon, document_request, entity_supplemental_document, export] |

### Return type

[**FileList**](FileList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | File List |  -  |
| **0** | Error |  -  |

<a id="listInboundAchTransferReturns"></a>
# **listInboundAchTransferReturns**
> InboundAchTransferReturnList listInboundAchTransferReturns(cursor, limit)

List Inbound ACH Transfer Returns

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String cursor = "cursor_example"; // String | 
    Integer limit = 56; // Integer | 
    try {
      InboundAchTransferReturnList result = apiInstance.listInboundAchTransferReturns(cursor, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listInboundAchTransferReturns");
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
| **cursor** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] |

### Return type

[**InboundAchTransferReturnList**](InboundAchTransferReturnList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Inbound ACH Transfer Return List |  -  |
| **0** | Error |  -  |

<a id="listInboundWireDrawdownRequests"></a>
# **listInboundWireDrawdownRequests**
> InboundWireDrawdownRequestList listInboundWireDrawdownRequests(cursor, limit)

List Inbound Wire Drawdown Requests

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String cursor = "cursor_example"; // String | 
    Integer limit = 56; // Integer | 
    try {
      InboundWireDrawdownRequestList result = apiInstance.listInboundWireDrawdownRequests(cursor, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listInboundWireDrawdownRequests");
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
| **cursor** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] |

### Return type

[**InboundWireDrawdownRequestList**](InboundWireDrawdownRequestList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Inbound Wire Drawdown Request List |  -  |
| **0** | Error |  -  |

<a id="listLimits"></a>
# **listLimits**
> LimitList listLimits(cursor, limit, modelId, status)

List Limits

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String cursor = "cursor_example"; // String | 
    Integer limit = 56; // Integer | 
    String modelId = "account_number_v18nkfqm6afpsrvy82b2"; // String | 
    String status = "active"; // String | 
    try {
      LimitList result = apiInstance.listLimits(cursor, limit, modelId, status);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listLimits");
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
| **cursor** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] |
| **modelId** | **String**|  | [optional] |
| **status** | **String**|  | [optional] |

### Return type

[**LimitList**](LimitList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Limit List |  -  |
| **0** | Error |  -  |

<a id="listOauthConnections"></a>
# **listOauthConnections**
> OauthConnectionList listOauthConnections(cursor, limit)

List OAuth Connections

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String cursor = "cursor_example"; // String | 
    Integer limit = 56; // Integer | 
    try {
      OauthConnectionList result = apiInstance.listOauthConnections(cursor, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listOauthConnections");
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
| **cursor** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] |

### Return type

[**OauthConnectionList**](OauthConnectionList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OAuth Connection List |  -  |
| **0** | Error |  -  |

<a id="listPendingTransactions"></a>
# **listPendingTransactions**
> PendingTransactionList listPendingTransactions(cursor, limit, accountId, routeId, sourceId, statusIn, createdAtAfter, createdAtBefore, createdAtOnOrAfter, createdAtOnOrBefore)

List Pending Transactions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String cursor = "cursor_example"; // String | 
    Integer limit = 56; // Integer | 
    String accountId = "accountId_example"; // String | 
    String routeId = "routeId_example"; // String | 
    String sourceId = "sourceId_example"; // String | 
    List<String> statusIn = Arrays.asList(); // List<String> | 
    OffsetDateTime createdAtAfter = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime createdAtBefore = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime createdAtOnOrAfter = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime createdAtOnOrBefore = OffsetDateTime.now(); // OffsetDateTime | 
    try {
      PendingTransactionList result = apiInstance.listPendingTransactions(cursor, limit, accountId, routeId, sourceId, statusIn, createdAtAfter, createdAtBefore, createdAtOnOrAfter, createdAtOnOrBefore);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listPendingTransactions");
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
| **cursor** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] |
| **accountId** | **String**|  | [optional] |
| **routeId** | **String**|  | [optional] |
| **sourceId** | **String**|  | [optional] |
| **statusIn** | [**List&lt;String&gt;**](String.md)|  | [optional] [enum: pending, complete] |
| **createdAtAfter** | **OffsetDateTime**|  | [optional] |
| **createdAtBefore** | **OffsetDateTime**|  | [optional] |
| **createdAtOnOrAfter** | **OffsetDateTime**|  | [optional] |
| **createdAtOnOrBefore** | **OffsetDateTime**|  | [optional] |

### Return type

[**PendingTransactionList**](PendingTransactionList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Pending Transaction List |  -  |
| **0** | Error |  -  |

<a id="listPrograms"></a>
# **listPrograms**
> ProgramList listPrograms(cursor, limit)

List Programs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String cursor = "cursor_example"; // String | 
    Integer limit = 56; // Integer | 
    try {
      ProgramList result = apiInstance.listPrograms(cursor, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listPrograms");
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
| **cursor** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] |

### Return type

[**ProgramList**](ProgramList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Program List |  -  |
| **0** | Error |  -  |

<a id="listRealTimePaymentsTransfers"></a>
# **listRealTimePaymentsTransfers**
> RealTimePaymentsTransferList listRealTimePaymentsTransfers(cursor, limit, accountId, externalAccountId, createdAtAfter, createdAtBefore, createdAtOnOrAfter, createdAtOnOrBefore)

List Real Time Payments Transfers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String cursor = "cursor_example"; // String | 
    Integer limit = 56; // Integer | 
    String accountId = "account_in71c4amph0vgo2qllky"; // String | 
    String externalAccountId = "externalAccountId_example"; // String | 
    OffsetDateTime createdAtAfter = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime createdAtBefore = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime createdAtOnOrAfter = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime createdAtOnOrBefore = OffsetDateTime.now(); // OffsetDateTime | 
    try {
      RealTimePaymentsTransferList result = apiInstance.listRealTimePaymentsTransfers(cursor, limit, accountId, externalAccountId, createdAtAfter, createdAtBefore, createdAtOnOrAfter, createdAtOnOrBefore);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listRealTimePaymentsTransfers");
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
| **cursor** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] |
| **accountId** | **String**|  | [optional] |
| **externalAccountId** | **String**|  | [optional] |
| **createdAtAfter** | **OffsetDateTime**|  | [optional] |
| **createdAtBefore** | **OffsetDateTime**|  | [optional] |
| **createdAtOnOrAfter** | **OffsetDateTime**|  | [optional] |
| **createdAtOnOrBefore** | **OffsetDateTime**|  | [optional] |

### Return type

[**RealTimePaymentsTransferList**](RealTimePaymentsTransferList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Real Time Payments Transfer List |  -  |
| **0** | Error |  -  |

<a id="listRoutingNumbers"></a>
# **listRoutingNumbers**
> RoutingNumberList listRoutingNumbers(routingNumber, cursor, limit)

List Routing Numbers

You can use this API to confirm if a routing number is valid, such as when a user is providing you with bank account details. Since routing numbers uniquely identify a bank, this will always return 0 or 1 entry. In Sandbox, the only valid routing number for this method is 110000000.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String routingNumber = "021000021"; // String | 
    String cursor = "cursor_example"; // String | 
    Integer limit = 56; // Integer | 
    try {
      RoutingNumberList result = apiInstance.listRoutingNumbers(routingNumber, cursor, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listRoutingNumbers");
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
| **routingNumber** | **String**|  | |
| **cursor** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] |

### Return type

[**RoutingNumberList**](RoutingNumberList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Routing Number List |  -  |
| **0** | Error |  -  |

<a id="listTransactions"></a>
# **listTransactions**
> TransactionList listTransactions(cursor, limit, accountId, createdAtAfter, createdAtBefore, createdAtOnOrAfter, createdAtOnOrBefore, categoryIn, routeId)

List Transactions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String cursor = "cursor_example"; // String | 
    Integer limit = 56; // Integer | 
    String accountId = "accountId_example"; // String | 
    OffsetDateTime createdAtAfter = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime createdAtBefore = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime createdAtOnOrAfter = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime createdAtOnOrBefore = OffsetDateTime.now(); // OffsetDateTime | 
    List<String> categoryIn = Arrays.asList(); // List<String> | 
    String routeId = "routeId_example"; // String | 
    try {
      TransactionList result = apiInstance.listTransactions(cursor, limit, accountId, createdAtAfter, createdAtBefore, createdAtOnOrAfter, createdAtOnOrBefore, categoryIn, routeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listTransactions");
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
| **cursor** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] |
| **accountId** | **String**|  | [optional] |
| **createdAtAfter** | **OffsetDateTime**|  | [optional] |
| **createdAtBefore** | **OffsetDateTime**|  | [optional] |
| **createdAtOnOrAfter** | **OffsetDateTime**|  | [optional] |
| **createdAtOnOrBefore** | **OffsetDateTime**|  | [optional] |
| **categoryIn** | [**List&lt;String&gt;**](String.md)|  | [optional] [enum: account_transfer_intention, ach_check_conversion_return, ach_check_conversion, ach_transfer_intention, ach_transfer_rejection, ach_transfer_return, card_dispute_acceptance, card_refund, card_settlement, card_revenue_payment, check_deposit_acceptance, check_deposit_return, check_transfer_intention, check_transfer_return, check_transfer_rejection, check_transfer_stop_payment_request, dispute_resolution, empyreal_cash_deposit, fee_payment, inbound_ach_transfer, inbound_ach_transfer_return_intention, inbound_check, inbound_international_ach_transfer, inbound_real_time_payments_transfer_confirmation, inbound_wire_drawdown_payment_reversal, inbound_wire_drawdown_payment, inbound_wire_reversal, inbound_wire_transfer, interest_payment, internal_general_ledger_transaction, internal_source, card_route_refund, card_route_settlement, real_time_payments_transfer_acknowledgement, sample_funds, wire_drawdown_payment_intention, wire_drawdown_payment_rejection, wire_transfer_intention, wire_transfer_rejection, other] |
| **routeId** | **String**|  | [optional] |

### Return type

[**TransactionList**](TransactionList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Transaction List |  -  |
| **0** | Error |  -  |

<a id="listWireDrawdownRequests"></a>
# **listWireDrawdownRequests**
> WireDrawdownRequestList listWireDrawdownRequests(cursor, limit)

List Wire Drawdown Requests

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String cursor = "cursor_example"; // String | 
    Integer limit = 56; // Integer | 
    try {
      WireDrawdownRequestList result = apiInstance.listWireDrawdownRequests(cursor, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listWireDrawdownRequests");
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
| **cursor** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] |

### Return type

[**WireDrawdownRequestList**](WireDrawdownRequestList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Wire Drawdown Request List |  -  |
| **0** | Error |  -  |

<a id="listWireTransfers"></a>
# **listWireTransfers**
> WireTransferList listWireTransfers(cursor, limit, accountId, externalAccountId, createdAtAfter, createdAtBefore, createdAtOnOrAfter, createdAtOnOrBefore)

List Wire Transfers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String cursor = "cursor_example"; // String | 
    Integer limit = 56; // Integer | 
    String accountId = "account_in71c4amph0vgo2qllky"; // String | 
    String externalAccountId = "externalAccountId_example"; // String | 
    OffsetDateTime createdAtAfter = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime createdAtBefore = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime createdAtOnOrAfter = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime createdAtOnOrBefore = OffsetDateTime.now(); // OffsetDateTime | 
    try {
      WireTransferList result = apiInstance.listWireTransfers(cursor, limit, accountId, externalAccountId, createdAtAfter, createdAtBefore, createdAtOnOrAfter, createdAtOnOrBefore);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listWireTransfers");
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
| **cursor** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] |
| **accountId** | **String**|  | [optional] |
| **externalAccountId** | **String**|  | [optional] |
| **createdAtAfter** | **OffsetDateTime**|  | [optional] |
| **createdAtBefore** | **OffsetDateTime**|  | [optional] |
| **createdAtOnOrAfter** | **OffsetDateTime**|  | [optional] |
| **createdAtOnOrBefore** | **OffsetDateTime**|  | [optional] |

### Return type

[**WireTransferList**](WireTransferList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Wire Transfer List |  -  |
| **0** | Error |  -  |

<a id="lookUpTheBalanceForAnAccount"></a>
# **lookUpTheBalanceForAnAccount**
> BalanceLookup lookUpTheBalanceForAnAccount(lookUpTheBalanceForAnAccountParameters)

Look up the balance for an Account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    LookUpTheBalanceForAnAccountParameters lookUpTheBalanceForAnAccountParameters = new LookUpTheBalanceForAnAccountParameters(); // LookUpTheBalanceForAnAccountParameters | 
    try {
      BalanceLookup result = apiInstance.lookUpTheBalanceForAnAccount(lookUpTheBalanceForAnAccountParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#lookUpTheBalanceForAnAccount");
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
| **lookUpTheBalanceForAnAccountParameters** | [**LookUpTheBalanceForAnAccountParameters**](LookUpTheBalanceForAnAccountParameters.md)|  | |

### Return type

[**BalanceLookup**](BalanceLookup.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Balance Lookup |  -  |
| **0** | Error |  -  |

<a id="mailASandboxCheckTransfer"></a>
# **mailASandboxCheckTransfer**
> CheckTransfer mailASandboxCheckTransfer(checkTransferId)

Mail a Sandbox Check Transfer

Simulates the mailing of a [Check Transfer](#check-transfers), which happens once per weekday in production but can be sped up in sandbox. This transfer must first have a &#x60;status&#x60; of &#x60;pending_approval&#x60; or &#x60;pending_submission&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String checkTransferId = "check_transfer_30b43acfu9vw8fyc4f5"; // String | 
    try {
      CheckTransfer result = apiInstance.mailASandboxCheckTransfer(checkTransferId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#mailASandboxCheckTransfer");
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
| **checkTransferId** | **String**|  | |

### Return type

[**CheckTransfer**](CheckTransfer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Check Transfer |  -  |
| **0** | Error |  -  |

<a id="rejectASandboxCheckDeposit"></a>
# **rejectASandboxCheckDeposit**
> CheckDeposit rejectASandboxCheckDeposit(checkDepositId)

Reject a Sandbox Check Deposit

Simulates the rejection of a [Check Deposit](#check-deposits) by Increase due to factors like poor image quality. This Check Deposit must first have a &#x60;status&#x60; of &#x60;pending&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String checkDepositId = "check_deposit_f06n9gpg7sxn8t19lfc1"; // String | 
    try {
      CheckDeposit result = apiInstance.rejectASandboxCheckDeposit(checkDepositId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#rejectASandboxCheckDeposit");
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
| **checkDepositId** | **String**|  | |

### Return type

[**CheckDeposit**](CheckDeposit.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Check Deposit |  -  |
| **0** | Error |  -  |

<a id="requestAStopPaymentOnACheckTransfer"></a>
# **requestAStopPaymentOnACheckTransfer**
> CheckTransfer requestAStopPaymentOnACheckTransfer(checkTransferId)

Request a stop payment on a Check Transfer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String checkTransferId = "check_transfer_30b43acfu9vw8fyc4f5"; // String | 
    try {
      CheckTransfer result = apiInstance.requestAStopPaymentOnACheckTransfer(checkTransferId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#requestAStopPaymentOnACheckTransfer");
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
| **checkTransferId** | **String**|  | |

### Return type

[**CheckTransfer**](CheckTransfer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Check Transfer |  -  |
| **0** | Error |  -  |

<a id="retrieveACard"></a>
# **retrieveACard**
> Card retrieveACard(cardId)

Retrieve a Card

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String cardId = "card_oubs0hwk5rn6knuecxg2"; // String | 
    try {
      Card result = apiInstance.retrieveACard(cardId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#retrieveACard");
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
| **cardId** | **String**|  | |

### Return type

[**Card**](Card.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Card |  -  |
| **0** | Error |  -  |

<a id="retrieveACardDispute"></a>
# **retrieveACardDispute**
> CardDispute retrieveACardDispute(cardDisputeId)

Retrieve a Card Dispute

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String cardDisputeId = "card_dispute_h9sc95nbl1cgltpp7men"; // String | 
    try {
      CardDispute result = apiInstance.retrieveACardDispute(cardDisputeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#retrieveACardDispute");
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
| **cardDisputeId** | **String**|  | |

### Return type

[**CardDispute**](CardDispute.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Card Dispute |  -  |
| **0** | Error |  -  |

<a id="retrieveACardProfile"></a>
# **retrieveACardProfile**
> CardProfile retrieveACardProfile(cardProfileId)

Retrieve a Card Profile

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String cardProfileId = "card_profile_cox5y73lob2eqly18piy"; // String | 
    try {
      CardProfile result = apiInstance.retrieveACardProfile(cardProfileId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#retrieveACardProfile");
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
| **cardProfileId** | **String**|  | |

### Return type

[**CardProfile**](CardProfile.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Card Profile |  -  |
| **0** | Error |  -  |

<a id="retrieveACheckDeposit"></a>
# **retrieveACheckDeposit**
> CheckDeposit retrieveACheckDeposit(checkDepositId)

Retrieve a Check Deposit

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String checkDepositId = "check_deposit_instruction_q2shv7x9qhevfm71kor8"; // String | 
    try {
      CheckDeposit result = apiInstance.retrieveACheckDeposit(checkDepositId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#retrieveACheckDeposit");
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
| **checkDepositId** | **String**|  | |

### Return type

[**CheckDeposit**](CheckDeposit.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Check Deposit |  -  |
| **0** | Error |  -  |

<a id="retrieveACheckTransfer"></a>
# **retrieveACheckTransfer**
> CheckTransfer retrieveACheckTransfer(checkTransferId)

Retrieve a Check Transfer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String checkTransferId = "check_transfer_30b43acfu9vw8fyc4f5"; // String | 
    try {
      CheckTransfer result = apiInstance.retrieveACheckTransfer(checkTransferId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#retrieveACheckTransfer");
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
| **checkTransferId** | **String**|  | |

### Return type

[**CheckTransfer**](CheckTransfer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Check Transfer |  -  |
| **0** | Error |  -  |

<a id="retrieveADeclinedTransaction"></a>
# **retrieveADeclinedTransaction**
> DeclinedTransaction retrieveADeclinedTransaction(declinedTransactionId)

Retrieve a Declined Transaction

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String declinedTransactionId = "declined_transaction_17jbn0yyhvkt4v4ooym8"; // String | 
    try {
      DeclinedTransaction result = apiInstance.retrieveADeclinedTransaction(declinedTransactionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#retrieveADeclinedTransaction");
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
| **declinedTransactionId** | **String**|  | |

### Return type

[**DeclinedTransaction**](DeclinedTransaction.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Declined Transaction |  -  |
| **0** | Error |  -  |

<a id="retrieveADigitalWalletToken"></a>
# **retrieveADigitalWalletToken**
> DigitalWalletToken retrieveADigitalWalletToken(digitalWalletTokenId)

Retrieve a Digital Wallet Token

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String digitalWalletTokenId = "digital_wallet_token_izi62go3h51p369jrie0"; // String | 
    try {
      DigitalWalletToken result = apiInstance.retrieveADigitalWalletToken(digitalWalletTokenId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#retrieveADigitalWalletToken");
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
| **digitalWalletTokenId** | **String**|  | |

### Return type

[**DigitalWalletToken**](DigitalWalletToken.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Digital Wallet Token |  -  |
| **0** | Error |  -  |

<a id="retrieveADocument"></a>
# **retrieveADocument**
> Document retrieveADocument(documentId)

Retrieve a Document

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String documentId = "document_qjtqc6s4c14ve2q89izm"; // String | 
    try {
      Document result = apiInstance.retrieveADocument(documentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#retrieveADocument");
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
| **documentId** | **String**|  | |

### Return type

[**Document**](Document.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Document |  -  |
| **0** | Error |  -  |

<a id="retrieveAFile"></a>
# **retrieveAFile**
> File retrieveAFile(fileId)

Retrieve a File

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String fileId = "file_makxrc67oh9l6sg7w9yc"; // String | 
    try {
      File result = apiInstance.retrieveAFile(fileId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#retrieveAFile");
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
| **fileId** | **String**|  | |

### Return type

[**File**](File.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | File |  -  |
| **0** | Error |  -  |

<a id="retrieveALimit"></a>
# **retrieveALimit**
> Limit retrieveALimit(limitId)

Retrieve a Limit

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String limitId = "limit_fku42k0qtc8ulsuas38q"; // String | 
    try {
      Limit result = apiInstance.retrieveALimit(limitId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#retrieveALimit");
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
| **limitId** | **String**|  | |

### Return type

[**Limit**](Limit.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Limit |  -  |
| **0** | Error |  -  |

<a id="retrieveAPendingTransaction"></a>
# **retrieveAPendingTransaction**
> PendingTransaction retrieveAPendingTransaction(pendingTransactionId)

Retrieve a Pending Transaction

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String pendingTransactionId = "pending_transaction_k1sfetcau2qbvjbzgju4"; // String | 
    try {
      PendingTransaction result = apiInstance.retrieveAPendingTransaction(pendingTransactionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#retrieveAPendingTransaction");
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
| **pendingTransactionId** | **String**|  | |

### Return type

[**PendingTransaction**](PendingTransaction.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Pending Transaction |  -  |
| **0** | Error |  -  |

<a id="retrieveAProgram"></a>
# **retrieveAProgram**
> Program retrieveAProgram(programId)

Retrieve a Program

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String programId = "program_i2v2os4mwza1oetokh9i"; // String | 
    try {
      Program result = apiInstance.retrieveAProgram(programId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#retrieveAProgram");
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
| **programId** | **String**|  | |

### Return type

[**Program**](Program.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Program |  -  |
| **0** | Error |  -  |

<a id="retrieveARealTimeDecision"></a>
# **retrieveARealTimeDecision**
> RealTimeDecision retrieveARealTimeDecision(realTimeDecisionId)

Retrieve a Real-Time Decision

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String realTimeDecisionId = "real_time_decision_j76n2e810ezcg3zh5qtn"; // String | 
    try {
      RealTimeDecision result = apiInstance.retrieveARealTimeDecision(realTimeDecisionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#retrieveARealTimeDecision");
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
| **realTimeDecisionId** | **String**|  | |

### Return type

[**RealTimeDecision**](RealTimeDecision.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Real-Time Decision |  -  |
| **0** | Error |  -  |

<a id="retrieveARealTimePaymentsTransfer"></a>
# **retrieveARealTimePaymentsTransfer**
> RealTimePaymentsTransfer retrieveARealTimePaymentsTransfer(realTimePaymentsTransferId)

Retrieve a Real Time Payments Transfer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String realTimePaymentsTransferId = "real_time_payments_transfer_iyuhl5kdn7ssmup83mvq"; // String | 
    try {
      RealTimePaymentsTransfer result = apiInstance.retrieveARealTimePaymentsTransfer(realTimePaymentsTransferId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#retrieveARealTimePaymentsTransfer");
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
| **realTimePaymentsTransferId** | **String**|  | |

### Return type

[**RealTimePaymentsTransfer**](RealTimePaymentsTransfer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Real Time Payments Transfer |  -  |
| **0** | Error |  -  |

<a id="retrieveATransaction"></a>
# **retrieveATransaction**
> Transaction retrieveATransaction(transactionId)

Retrieve a Transaction

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String transactionId = "transaction_uyrp7fld2ium70oa7oi"; // String | 
    try {
      Transaction result = apiInstance.retrieveATransaction(transactionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#retrieveATransaction");
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
| **transactionId** | **String**|  | |

### Return type

[**Transaction**](Transaction.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Transaction |  -  |
| **0** | Error |  -  |

<a id="retrieveAWireDrawdownRequest"></a>
# **retrieveAWireDrawdownRequest**
> WireDrawdownRequest retrieveAWireDrawdownRequest(wireDrawdownRequestId)

Retrieve a Wire Drawdown Request

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String wireDrawdownRequestId = "wire_drawdown_request_q6lmocus3glo0lr2bfv3"; // String | 
    try {
      WireDrawdownRequest result = apiInstance.retrieveAWireDrawdownRequest(wireDrawdownRequestId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#retrieveAWireDrawdownRequest");
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
| **wireDrawdownRequestId** | **String**|  | |

### Return type

[**WireDrawdownRequest**](WireDrawdownRequest.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Wire Drawdown Request |  -  |
| **0** | Error |  -  |

<a id="retrieveAWireTransfer"></a>
# **retrieveAWireTransfer**
> WireTransfer retrieveAWireTransfer(wireTransferId)

Retrieve a Wire Transfer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String wireTransferId = "wire_transfer_5akynk7dqsq25qwk9q2u"; // String | 
    try {
      WireTransfer result = apiInstance.retrieveAWireTransfer(wireTransferId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#retrieveAWireTransfer");
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
| **wireTransferId** | **String**|  | |

### Return type

[**WireTransfer**](WireTransfer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Wire Transfer |  -  |
| **0** | Error |  -  |

<a id="retrieveAnAccount"></a>
# **retrieveAnAccount**
> Account retrieveAnAccount(accountId)

Retrieve an Account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "account_in71c4amph0vgo2qllky"; // String | 
    try {
      Account result = apiInstance.retrieveAnAccount(accountId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#retrieveAnAccount");
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
| **accountId** | **String**|  | |

### Return type

[**Account**](Account.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Account |  -  |
| **0** | Error |  -  |

<a id="retrieveAnAccountNumber"></a>
# **retrieveAnAccountNumber**
> AccountNumber retrieveAnAccountNumber(accountNumberId)

Retrieve an Account Number

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountNumberId = "account_number_v18nkfqm6afpsrvy82b2"; // String | 
    try {
      AccountNumber result = apiInstance.retrieveAnAccountNumber(accountNumberId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#retrieveAnAccountNumber");
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
| **accountNumberId** | **String**|  | |

### Return type

[**AccountNumber**](AccountNumber.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Account Number |  -  |
| **0** | Error |  -  |

<a id="retrieveAnAccountStatement"></a>
# **retrieveAnAccountStatement**
> AccountStatement retrieveAnAccountStatement(accountStatementId)

Retrieve an Account Statement

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountStatementId = "account_statement_lkc03a4skm2k7f38vj15"; // String | 
    try {
      AccountStatement result = apiInstance.retrieveAnAccountStatement(accountStatementId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#retrieveAnAccountStatement");
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
| **accountStatementId** | **String**|  | |

### Return type

[**AccountStatement**](AccountStatement.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Account Statement |  -  |
| **0** | Error |  -  |

<a id="retrieveAnAccountTransfer"></a>
# **retrieveAnAccountTransfer**
> AccountTransfer retrieveAnAccountTransfer(accountTransferId)

Retrieve an Account Transfer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountTransferId = "account_transfer_7k9qe1ysdgqztnt63l7n"; // String | 
    try {
      AccountTransfer result = apiInstance.retrieveAnAccountTransfer(accountTransferId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#retrieveAnAccountTransfer");
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
| **accountTransferId** | **String**|  | |

### Return type

[**AccountTransfer**](AccountTransfer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Account Transfer |  -  |
| **0** | Error |  -  |

<a id="retrieveAnAchPrenotification"></a>
# **retrieveAnAchPrenotification**
> AchPrenotification retrieveAnAchPrenotification(achPrenotificationId)

Retrieve an ACH Prenotification

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String achPrenotificationId = "ach_prenotification_ubjf9qqsxl3obbcn1u34"; // String | 
    try {
      AchPrenotification result = apiInstance.retrieveAnAchPrenotification(achPrenotificationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#retrieveAnAchPrenotification");
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
| **achPrenotificationId** | **String**|  | |

### Return type

[**AchPrenotification**](AchPrenotification.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ACH Prenotification |  -  |
| **0** | Error |  -  |

<a id="retrieveAnAchTransfer"></a>
# **retrieveAnAchTransfer**
> AchTransfer retrieveAnAchTransfer(achTransferId)

Retrieve an ACH Transfer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String achTransferId = "ach_transfer_uoxatyh3lt5evrsdvo7q"; // String | 
    try {
      AchTransfer result = apiInstance.retrieveAnAchTransfer(achTransferId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#retrieveAnAchTransfer");
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
| **achTransferId** | **String**|  | |

### Return type

[**AchTransfer**](AchTransfer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ACH Transfer |  -  |
| **0** | Error |  -  |

<a id="retrieveAnEntity"></a>
# **retrieveAnEntity**
> Entity retrieveAnEntity(entityId)

Retrieve an Entity

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String entityId = "entity_n8y8tnk2p9339ti393yi"; // String | 
    try {
      Entity result = apiInstance.retrieveAnEntity(entityId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#retrieveAnEntity");
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
| **entityId** | **String**|  | |

### Return type

[**Entity**](Entity.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Entity |  -  |
| **0** | Error |  -  |

<a id="retrieveAnEvent"></a>
# **retrieveAnEvent**
> Event retrieveAnEvent(eventId)

Retrieve an Event

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String eventId = "event_001dzz0r20rzr4zrhrr1364hy80"; // String | 
    try {
      Event result = apiInstance.retrieveAnEvent(eventId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#retrieveAnEvent");
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
| **eventId** | **String**|  | |

### Return type

[**Event**](Event.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Event |  -  |
| **0** | Error |  -  |

<a id="retrieveAnEventSubscription"></a>
# **retrieveAnEventSubscription**
> EventSubscription retrieveAnEventSubscription(eventSubscriptionId)

Retrieve an Event Subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String eventSubscriptionId = "event_subscription_001dzz0r20rcdxgb013zqb8m04g"; // String | 
    try {
      EventSubscription result = apiInstance.retrieveAnEventSubscription(eventSubscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#retrieveAnEventSubscription");
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
| **eventSubscriptionId** | **String**|  | |

### Return type

[**EventSubscription**](EventSubscription.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Event Subscription |  -  |
| **0** | Error |  -  |

<a id="retrieveAnExport"></a>
# **retrieveAnExport**
> Export retrieveAnExport(exportId)

Retrieve an Export

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String exportId = "export_8s4m48qz3bclzje0zwh9"; // String | 
    try {
      Export result = apiInstance.retrieveAnExport(exportId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#retrieveAnExport");
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
| **exportId** | **String**|  | |

### Return type

[**Export**](Export.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Export |  -  |
| **0** | Error |  -  |

<a id="retrieveAnExternalAccount"></a>
# **retrieveAnExternalAccount**
> ExternalAccount retrieveAnExternalAccount(externalAccountId)

Retrieve an External Account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String externalAccountId = "external_account_ukk55lr923a3ac0pp7iv"; // String | 
    try {
      ExternalAccount result = apiInstance.retrieveAnExternalAccount(externalAccountId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#retrieveAnExternalAccount");
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
| **externalAccountId** | **String**|  | |

### Return type

[**ExternalAccount**](ExternalAccount.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | External Account |  -  |
| **0** | Error |  -  |

<a id="retrieveAnInboundAchTransferReturn"></a>
# **retrieveAnInboundAchTransferReturn**
> InboundAchTransferReturn retrieveAnInboundAchTransferReturn(inboundAchTransferReturnId)

Retrieve an Inbound ACH Transfer Return

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String inboundAchTransferReturnId = "inbound_ach_transfer_return_fhcxk5huskwhmt7iz0gk"; // String | 
    try {
      InboundAchTransferReturn result = apiInstance.retrieveAnInboundAchTransferReturn(inboundAchTransferReturnId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#retrieveAnInboundAchTransferReturn");
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
| **inboundAchTransferReturnId** | **String**|  | |

### Return type

[**InboundAchTransferReturn**](InboundAchTransferReturn.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Inbound ACH Transfer Return |  -  |
| **0** | Error |  -  |

<a id="retrieveAnInboundWireDrawdownRequest"></a>
# **retrieveAnInboundWireDrawdownRequest**
> InboundWireDrawdownRequest retrieveAnInboundWireDrawdownRequest(inboundWireDrawdownRequestId)

Retrieve an Inbound Wire Drawdown Request

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String inboundWireDrawdownRequestId = "inbound_wire_drawdown_request_u5a92ikqhz1ytphn799e"; // String | 
    try {
      InboundWireDrawdownRequest result = apiInstance.retrieveAnInboundWireDrawdownRequest(inboundWireDrawdownRequestId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#retrieveAnInboundWireDrawdownRequest");
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
| **inboundWireDrawdownRequestId** | **String**|  | |

### Return type

[**InboundWireDrawdownRequest**](InboundWireDrawdownRequest.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Inbound Wire Drawdown Request |  -  |
| **0** | Error |  -  |

<a id="retrieveAnOauthConnection"></a>
# **retrieveAnOauthConnection**
> OauthConnection retrieveAnOauthConnection(oauthConnectionId)

Retrieve an OAuth Connection

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String oauthConnectionId = "connection_dauknoksyr4wilz4e6my"; // String | 
    try {
      OauthConnection result = apiInstance.retrieveAnOauthConnection(oauthConnectionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#retrieveAnOauthConnection");
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
| **oauthConnectionId** | **String**|  | |

### Return type

[**OauthConnection**](OauthConnection.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OAuth Connection |  -  |
| **0** | Error |  -  |

<a id="retrieveGroupDetails"></a>
# **retrieveGroupDetails**
> Group retrieveGroupDetails()

Retrieve Group details

Returns details for the currently authenticated Group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      Group result = apiInstance.retrieveGroupDetails();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#retrieveGroupDetails");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Group |  -  |
| **0** | Error |  -  |

<a id="retrieveSensitiveDetailsForACard"></a>
# **retrieveSensitiveDetailsForACard**
> CardDetails retrieveSensitiveDetailsForACard(cardId)

Retrieve sensitive details for a Card

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String cardId = "card_oubs0hwk5rn6knuecxg2"; // String | 
    try {
      CardDetails result = apiInstance.retrieveSensitiveDetailsForACard(cardId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#retrieveSensitiveDetailsForACard");
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
| **cardId** | **String**|  | |

### Return type

[**CardDetails**](CardDetails.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Card Details |  -  |
| **0** | Error |  -  |

<a id="returnASandboxAchTransfer"></a>
# **returnASandboxAchTransfer**
> AchTransfer returnASandboxAchTransfer(achTransferId, returnASandboxAchTransferParameters)

Return a Sandbox ACH Transfer

Simulates the return of an [ACH Transfer](#ach-transfers) by the Federal Reserve due to an error condition. This will also create a Transaction to account for the returned funds. This transfer must first have a &#x60;status&#x60; of &#x60;submitted&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String achTransferId = "ach_transfer_uoxatyh3lt5evrsdvo7q"; // String | 
    ReturnASandboxAchTransferParameters returnASandboxAchTransferParameters = new ReturnASandboxAchTransferParameters(); // ReturnASandboxAchTransferParameters | 
    try {
      AchTransfer result = apiInstance.returnASandboxAchTransfer(achTransferId, returnASandboxAchTransferParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#returnASandboxAchTransfer");
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
| **achTransferId** | **String**|  | |
| **returnASandboxAchTransferParameters** | [**ReturnASandboxAchTransferParameters**](ReturnASandboxAchTransferParameters.md)|  | |

### Return type

[**AchTransfer**](AchTransfer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ACH Transfer |  -  |
| **0** | Error |  -  |

<a id="returnASandboxCheckDeposit"></a>
# **returnASandboxCheckDeposit**
> CheckDeposit returnASandboxCheckDeposit(checkDepositId)

Return a Sandbox Check Deposit

Simulates the return of a [Check Deposit](#check-deposits). This Check Deposit must first have a &#x60;status&#x60; of &#x60;submitted&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String checkDepositId = "check_deposit_f06n9gpg7sxn8t19lfc1"; // String | 
    try {
      CheckDeposit result = apiInstance.returnASandboxCheckDeposit(checkDepositId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#returnASandboxCheckDeposit");
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
| **checkDepositId** | **String**|  | |

### Return type

[**CheckDeposit**](CheckDeposit.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Check Deposit |  -  |
| **0** | Error |  -  |

<a id="returnASandboxCheckTransfer"></a>
# **returnASandboxCheckTransfer**
> CheckTransfer returnASandboxCheckTransfer(checkTransferId, returnASandboxCheckTransferParameters)

Return a Sandbox Check Transfer

Simulates a [Check Transfer](#check-transfers) being returned via USPS to Increase. This transfer must first have a &#x60;status&#x60; of &#x60;mailed&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String checkTransferId = "check_transfer_30b43acfu9vw8fyc4f5"; // String | 
    ReturnASandboxCheckTransferParameters returnASandboxCheckTransferParameters = new ReturnASandboxCheckTransferParameters(); // ReturnASandboxCheckTransferParameters | 
    try {
      CheckTransfer result = apiInstance.returnASandboxCheckTransfer(checkTransferId, returnASandboxCheckTransferParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#returnASandboxCheckTransfer");
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
| **checkTransferId** | **String**|  | |
| **returnASandboxCheckTransferParameters** | [**ReturnASandboxCheckTransferParameters**](ReturnASandboxCheckTransferParameters.md)|  | |

### Return type

[**CheckTransfer**](CheckTransfer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Check Transfer |  -  |
| **0** | Error |  -  |

<a id="reverseASandboxWireTransfer"></a>
# **reverseASandboxWireTransfer**
> WireTransfer reverseASandboxWireTransfer(wireTransferId)

Reverse a Sandbox Wire Transfer

Simulates the reversal of a [Wire Transfer](#wire-transfers) by the Federal Reserve due to error conditions. This will also create a [Transaction](#transaction) to account for the returned funds. This Wire Transfer must first have a &#x60;status&#x60; of &#x60;complete&#x60;.&#39;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String wireTransferId = "wire_transfer_5akynk7dqsq25qwk9q2u"; // String | 
    try {
      WireTransfer result = apiInstance.reverseASandboxWireTransfer(wireTransferId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#reverseASandboxWireTransfer");
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
| **wireTransferId** | **String**|  | |

### Return type

[**WireTransfer**](WireTransfer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Wire Transfer |  -  |
| **0** | Error |  -  |

<a id="simulateARealTimePaymentsTransferToYourAccount"></a>
# **simulateARealTimePaymentsTransferToYourAccount**
> InboundRealTimePaymentsTransferSimulationResult simulateARealTimePaymentsTransferToYourAccount(simulateARealTimePaymentsTransferToYourAccountParameters)

Simulate a Real Time Payments Transfer to your account

Simulates an inbound Real Time Payments transfer to your account. Real Time Payments are a beta feature.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    SimulateARealTimePaymentsTransferToYourAccountParameters simulateARealTimePaymentsTransferToYourAccountParameters = new SimulateARealTimePaymentsTransferToYourAccountParameters(); // SimulateARealTimePaymentsTransferToYourAccountParameters | 
    try {
      InboundRealTimePaymentsTransferSimulationResult result = apiInstance.simulateARealTimePaymentsTransferToYourAccount(simulateARealTimePaymentsTransferToYourAccountParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#simulateARealTimePaymentsTransferToYourAccount");
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
| **simulateARealTimePaymentsTransferToYourAccountParameters** | [**SimulateARealTimePaymentsTransferToYourAccountParameters**](SimulateARealTimePaymentsTransferToYourAccountParameters.md)|  | |

### Return type

[**InboundRealTimePaymentsTransferSimulationResult**](InboundRealTimePaymentsTransferSimulationResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Inbound Real Time Payments Transfer Simulation Result |  -  |
| **0** | Error |  -  |

<a id="simulateARefundOnACard"></a>
# **simulateARefundOnACard**
> Transaction simulateARefundOnACard(simulateARefundOnACardParameters)

Simulate a refund on a card

Simulates refunding a card transaction. The full value of the original sandbox transaction is refunded.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    SimulateARefundOnACardParameters simulateARefundOnACardParameters = new SimulateARefundOnACardParameters(); // SimulateARefundOnACardParameters | 
    try {
      Transaction result = apiInstance.simulateARefundOnACard(simulateARefundOnACardParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#simulateARefundOnACard");
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
| **simulateARefundOnACardParameters** | [**SimulateARefundOnACardParameters**](SimulateARefundOnACardParameters.md)|  | |

### Return type

[**Transaction**](Transaction.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Transaction |  -  |
| **0** | Error |  -  |

<a id="simulateATaxDocumentBeingCreated"></a>
# **simulateATaxDocumentBeingCreated**
> Document simulateATaxDocumentBeingCreated(simulateATaxDocumentBeingCreatedParameters)

Simulate a tax document being created

Simulates an tax document being created for an account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    SimulateATaxDocumentBeingCreatedParameters simulateATaxDocumentBeingCreatedParameters = new SimulateATaxDocumentBeingCreatedParameters(); // SimulateATaxDocumentBeingCreatedParameters | 
    try {
      Document result = apiInstance.simulateATaxDocumentBeingCreated(simulateATaxDocumentBeingCreatedParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#simulateATaxDocumentBeingCreated");
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
| **simulateATaxDocumentBeingCreatedParameters** | [**SimulateATaxDocumentBeingCreatedParameters**](SimulateATaxDocumentBeingCreatedParameters.md)|  | |

### Return type

[**Document**](Document.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Document |  -  |
| **0** | Error |  -  |

<a id="simulateAWireTransferToYourAccount"></a>
# **simulateAWireTransferToYourAccount**
> InboundWireTransferSimulationResult simulateAWireTransferToYourAccount(simulateAWireTransferToYourAccountParameters)

Simulate a Wire Transfer to your account

Simulates an inbound Wire Transfer to your account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    SimulateAWireTransferToYourAccountParameters simulateAWireTransferToYourAccountParameters = new SimulateAWireTransferToYourAccountParameters(); // SimulateAWireTransferToYourAccountParameters | 
    try {
      InboundWireTransferSimulationResult result = apiInstance.simulateAWireTransferToYourAccount(simulateAWireTransferToYourAccountParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#simulateAWireTransferToYourAccount");
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
| **simulateAWireTransferToYourAccountParameters** | [**SimulateAWireTransferToYourAccountParameters**](SimulateAWireTransferToYourAccountParameters.md)|  | |

### Return type

[**InboundWireTransferSimulationResult**](InboundWireTransferSimulationResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Inbound Wire Transfer Simulation Result |  -  |
| **0** | Error |  -  |

<a id="simulateAnAccountStatementBeingCreated"></a>
# **simulateAnAccountStatementBeingCreated**
> AccountStatement simulateAnAccountStatementBeingCreated(simulateAnAccountStatementBeingCreatedParameters)

Simulate an Account Statement being created

Simulates an [Account Statement](#account-statements) being created for an account. In production, Account Statements are generated once per month.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    SimulateAnAccountStatementBeingCreatedParameters simulateAnAccountStatementBeingCreatedParameters = new SimulateAnAccountStatementBeingCreatedParameters(); // SimulateAnAccountStatementBeingCreatedParameters | 
    try {
      AccountStatement result = apiInstance.simulateAnAccountStatementBeingCreated(simulateAnAccountStatementBeingCreatedParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#simulateAnAccountStatementBeingCreated");
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
| **simulateAnAccountStatementBeingCreatedParameters** | [**SimulateAnAccountStatementBeingCreatedParameters**](SimulateAnAccountStatementBeingCreatedParameters.md)|  | |

### Return type

[**AccountStatement**](AccountStatement.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Account Statement |  -  |
| **0** | Error |  -  |

<a id="simulateAnAchTransferToYourAccount"></a>
# **simulateAnAchTransferToYourAccount**
> InboundAchTransferSimulationResult simulateAnAchTransferToYourAccount(simulateAnAchTransferToYourAccountParameters)

Simulate an ACH Transfer to your account

Simulates an inbound ACH transfer to your account. This imitates initiating a transaction to an Increase account from a different financial institution. The transfer may be either a credit or a debit depending on if the &#x60;amount&#x60; is positive or negative. The result of calling this API will be either a [Transaction](#transactions) or a [Declined Transaction](#declined-transactions) depending on whether or not the transfer is allowed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    SimulateAnAchTransferToYourAccountParameters simulateAnAchTransferToYourAccountParameters = new SimulateAnAchTransferToYourAccountParameters(); // SimulateAnAchTransferToYourAccountParameters | 
    try {
      InboundAchTransferSimulationResult result = apiInstance.simulateAnAchTransferToYourAccount(simulateAnAchTransferToYourAccountParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#simulateAnAchTransferToYourAccount");
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
| **simulateAnAchTransferToYourAccountParameters** | [**SimulateAnAchTransferToYourAccountParameters**](SimulateAnAchTransferToYourAccountParameters.md)|  | |

### Return type

[**InboundAchTransferSimulationResult**](InboundAchTransferSimulationResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Inbound ACH Transfer Simulation Result |  -  |
| **0** | Error |  -  |

<a id="simulateAnAuthorizationOnACard"></a>
# **simulateAnAuthorizationOnACard**
> InboundCardAuthorizationSimulationResult simulateAnAuthorizationOnACard(simulateAnAuthorizationOnACardParameters)

Simulate an authorization on a Card

Simulates a purchase authorization on a [Card](#cards). Depending on the balance available to the card and the &#x60;amount&#x60; submitted, the authorization activity will result in a [Pending Transaction](#pending-transactions) of type &#x60;card_authorization&#x60; or a [Declined Transaction](#declined-transactions) of type &#x60;card_decline&#x60;. You can pass either a Card id or a [Digital Wallet Token](#digital-wallet-tokens) id to simulate the two different ways purchases can be made.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    SimulateAnAuthorizationOnACardParameters simulateAnAuthorizationOnACardParameters = new SimulateAnAuthorizationOnACardParameters(); // SimulateAnAuthorizationOnACardParameters | 
    try {
      InboundCardAuthorizationSimulationResult result = apiInstance.simulateAnAuthorizationOnACard(simulateAnAuthorizationOnACardParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#simulateAnAuthorizationOnACard");
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
| **simulateAnAuthorizationOnACardParameters** | [**SimulateAnAuthorizationOnACardParameters**](SimulateAnAuthorizationOnACardParameters.md)|  | |

### Return type

[**InboundCardAuthorizationSimulationResult**](InboundCardAuthorizationSimulationResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Inbound Card Authorization Simulation Result |  -  |
| **0** | Error |  -  |

<a id="simulateAnInboundWireDrawdownRequestBeingCreated"></a>
# **simulateAnInboundWireDrawdownRequestBeingCreated**
> InboundWireDrawdownRequest simulateAnInboundWireDrawdownRequestBeingCreated(simulateAnInboundWireDrawdownRequestBeingCreatedParameters)

Simulate an Inbound Wire Drawdown request being created

Simulates the receival of an [Inbound Wire Drawdown Request](#inbound-wire-drawdown-requests).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    SimulateAnInboundWireDrawdownRequestBeingCreatedParameters simulateAnInboundWireDrawdownRequestBeingCreatedParameters = new SimulateAnInboundWireDrawdownRequestBeingCreatedParameters(); // SimulateAnInboundWireDrawdownRequestBeingCreatedParameters | 
    try {
      InboundWireDrawdownRequest result = apiInstance.simulateAnInboundWireDrawdownRequestBeingCreated(simulateAnInboundWireDrawdownRequestBeingCreatedParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#simulateAnInboundWireDrawdownRequestBeingCreated");
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
| **simulateAnInboundWireDrawdownRequestBeingCreatedParameters** | [**SimulateAnInboundWireDrawdownRequestBeingCreatedParameters**](SimulateAnInboundWireDrawdownRequestBeingCreatedParameters.md)|  | |

### Return type

[**InboundWireDrawdownRequest**](InboundWireDrawdownRequest.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Inbound Wire Drawdown Request |  -  |
| **0** | Error |  -  |

<a id="simulateAnInterestPaymentToYourAccount"></a>
# **simulateAnInterestPaymentToYourAccount**
> InterestPaymentSimulationResult simulateAnInterestPaymentToYourAccount(simulateAnInterestPaymentToYourAccountParameters)

Simulate an Interest Payment to your account

Simulates an interest payment to your account. In production, this happens automatically on the first of each month.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    SimulateAnInterestPaymentToYourAccountParameters simulateAnInterestPaymentToYourAccountParameters = new SimulateAnInterestPaymentToYourAccountParameters(); // SimulateAnInterestPaymentToYourAccountParameters | 
    try {
      InterestPaymentSimulationResult result = apiInstance.simulateAnInterestPaymentToYourAccount(simulateAnInterestPaymentToYourAccountParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#simulateAnInterestPaymentToYourAccount");
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
| **simulateAnInterestPaymentToYourAccountParameters** | [**SimulateAnInterestPaymentToYourAccountParameters**](SimulateAnInterestPaymentToYourAccountParameters.md)|  | |

### Return type

[**InterestPaymentSimulationResult**](InterestPaymentSimulationResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Interest Payment Simulation Result |  -  |
| **0** | Error |  -  |

<a id="simulateDigitalWalletProvisioningForACard"></a>
# **simulateDigitalWalletProvisioningForACard**
> InboundDigitalWalletTokenRequestSimulationResult simulateDigitalWalletProvisioningForACard(simulateDigitalWalletProvisioningForACardParameters)

Simulate digital wallet provisioning for a card

Simulates a user attempting add a [Card](#cards) to a digital wallet such as Apple Pay.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    SimulateDigitalWalletProvisioningForACardParameters simulateDigitalWalletProvisioningForACardParameters = new SimulateDigitalWalletProvisioningForACardParameters(); // SimulateDigitalWalletProvisioningForACardParameters | 
    try {
      InboundDigitalWalletTokenRequestSimulationResult result = apiInstance.simulateDigitalWalletProvisioningForACard(simulateDigitalWalletProvisioningForACardParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#simulateDigitalWalletProvisioningForACard");
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
| **simulateDigitalWalletProvisioningForACardParameters** | [**SimulateDigitalWalletProvisioningForACardParameters**](SimulateDigitalWalletProvisioningForACardParameters.md)|  | |

### Return type

[**InboundDigitalWalletTokenRequestSimulationResult**](InboundDigitalWalletTokenRequestSimulationResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Inbound Digital Wallet Token Request Simulation Result |  -  |
| **0** | Error |  -  |

<a id="simulateSettlingACardAuthorization"></a>
# **simulateSettlingACardAuthorization**
> Transaction simulateSettlingACardAuthorization(simulateSettlingACardAuthorizationParameters)

Simulate settling a card authorization

Simulates the settlement of an authorization by a card acquirer. After a card authorization is created, the merchant will eventually send a settlement. This simulates that event, which may occur many days after the purchase in production. The amount settled can be different from the amount originally authorized, for example, when adding a tip to a restaurant bill.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    SimulateSettlingACardAuthorizationParameters simulateSettlingACardAuthorizationParameters = new SimulateSettlingACardAuthorizationParameters(); // SimulateSettlingACardAuthorizationParameters | 
    try {
      Transaction result = apiInstance.simulateSettlingACardAuthorization(simulateSettlingACardAuthorizationParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#simulateSettlingACardAuthorization");
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
| **simulateSettlingACardAuthorizationParameters** | [**SimulateSettlingACardAuthorizationParameters**](SimulateSettlingACardAuthorizationParameters.md)|  | |

### Return type

[**Transaction**](Transaction.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Transaction |  -  |
| **0** | Error |  -  |

<a id="simulatesAdvancingTheStateOfACardDispute"></a>
# **simulatesAdvancingTheStateOfACardDispute**
> CardDispute simulatesAdvancingTheStateOfACardDispute(cardDisputeId, simulatesAdvancingTheStateOfACardDisputeParameters)

Simulates advancing the state of a card dispute

After a [Card Dispute](#card-disputes) is created in production, the dispute will be reviewed. Since no review happens in sandbox, this endpoint simulates moving a Card Dispute into a rejected or accepted state. A Card Dispute can only be actioned one time and must have a status of &#x60;pending_reviewing&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String cardDisputeId = "card_dispute_h9sc95nbl1cgltpp7men"; // String | 
    SimulatesAdvancingTheStateOfACardDisputeParameters simulatesAdvancingTheStateOfACardDisputeParameters = new SimulatesAdvancingTheStateOfACardDisputeParameters(); // SimulatesAdvancingTheStateOfACardDisputeParameters | 
    try {
      CardDispute result = apiInstance.simulatesAdvancingTheStateOfACardDispute(cardDisputeId, simulatesAdvancingTheStateOfACardDisputeParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#simulatesAdvancingTheStateOfACardDispute");
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
| **cardDisputeId** | **String**|  | |
| **simulatesAdvancingTheStateOfACardDisputeParameters** | [**SimulatesAdvancingTheStateOfACardDisputeParameters**](SimulatesAdvancingTheStateOfACardDisputeParameters.md)|  | |

### Return type

[**CardDispute**](CardDispute.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Card Dispute |  -  |
| **0** | Error |  -  |

<a id="submitASandboxAchTransfer"></a>
# **submitASandboxAchTransfer**
> AchTransfer submitASandboxAchTransfer(achTransferId)

Submit a Sandbox ACH Transfer

Simulates the submission of an [ACH Transfer](#ach-transfers) to the Federal Reserve. This transfer must first have a &#x60;status&#x60; of &#x60;pending_approval&#x60; or &#x60;pending_submission&#x60;. In production, Increase submits ACH Transfers to the Federal Reserve three times per day on weekdays. Since sandbox ACH Transfers are not submitted to the Federal Reserve, this endpoint allows you to skip that delay and transition the ACH Transfer to a status of &#x60;submitted&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String achTransferId = "ach_transfer_uoxatyh3lt5evrsdvo7q"; // String | 
    try {
      AchTransfer result = apiInstance.submitASandboxAchTransfer(achTransferId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#submitASandboxAchTransfer");
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
| **achTransferId** | **String**|  | |

### Return type

[**AchTransfer**](AchTransfer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ACH Transfer |  -  |
| **0** | Error |  -  |

<a id="submitASandboxCheckDeposit"></a>
# **submitASandboxCheckDeposit**
> CheckDeposit submitASandboxCheckDeposit(checkDepositId)

Submit a Sandbox Check Deposit

Simulates the submission of a [Check Deposit](#check-deposits) to the Federal Reserve. This Check Deposit must first have a &#x60;status&#x60; of &#x60;pending&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String checkDepositId = "check_deposit_f06n9gpg7sxn8t19lfc1"; // String | 
    try {
      CheckDeposit result = apiInstance.submitASandboxCheckDeposit(checkDepositId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#submitASandboxCheckDeposit");
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
| **checkDepositId** | **String**|  | |

### Return type

[**CheckDeposit**](CheckDeposit.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Check Deposit |  -  |
| **0** | Error |  -  |

<a id="submitASandboxWireTransfer"></a>
# **submitASandboxWireTransfer**
> WireTransfer submitASandboxWireTransfer(wireTransferId)

Submit a Sandbox Wire Transfer

Simulates the submission of a [Wire Transfer](#wire-transfers) to the Federal Reserve. This transfer must first have a &#x60;status&#x60; of &#x60;pending_approval&#x60; or &#x60;pending_creating&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String wireTransferId = "wire_transfer_5akynk7dqsq25qwk9q2u"; // String | 
    try {
      WireTransfer result = apiInstance.submitASandboxWireTransfer(wireTransferId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#submitASandboxWireTransfer");
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
| **wireTransferId** | **String**|  | |

### Return type

[**WireTransfer**](WireTransfer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Wire Transfer |  -  |
| **0** | Error |  -  |

<a id="updateACard"></a>
# **updateACard**
> Card updateACard(cardId, updateACardParameters)

Update a Card

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String cardId = "card_oubs0hwk5rn6knuecxg2"; // String | 
    UpdateACardParameters updateACardParameters = new UpdateACardParameters(); // UpdateACardParameters | 
    try {
      Card result = apiInstance.updateACard(cardId, updateACardParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateACard");
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
| **cardId** | **String**|  | |
| **updateACardParameters** | [**UpdateACardParameters**](UpdateACardParameters.md)|  | |

### Return type

[**Card**](Card.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Card |  -  |
| **0** | Error |  -  |

<a id="updateALimit"></a>
# **updateALimit**
> Limit updateALimit(limitId, updateALimitParameters)

Update a Limit

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String limitId = "limit_fku42k0qtc8ulsuas38q"; // String | 
    UpdateALimitParameters updateALimitParameters = new UpdateALimitParameters(); // UpdateALimitParameters | 
    try {
      Limit result = apiInstance.updateALimit(limitId, updateALimitParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateALimit");
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
| **limitId** | **String**|  | |
| **updateALimitParameters** | [**UpdateALimitParameters**](UpdateALimitParameters.md)|  | |

### Return type

[**Limit**](Limit.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Limit |  -  |
| **0** | Error |  -  |

<a id="updateAnAccount"></a>
# **updateAnAccount**
> Account updateAnAccount(accountId, updateAnAccountParameters)

Update an Account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "account_in71c4amph0vgo2qllky"; // String | 
    UpdateAnAccountParameters updateAnAccountParameters = new UpdateAnAccountParameters(); // UpdateAnAccountParameters | 
    try {
      Account result = apiInstance.updateAnAccount(accountId, updateAnAccountParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateAnAccount");
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
| **accountId** | **String**|  | |
| **updateAnAccountParameters** | [**UpdateAnAccountParameters**](UpdateAnAccountParameters.md)|  | |

### Return type

[**Account**](Account.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Account |  -  |
| **0** | Error |  -  |

<a id="updateAnAccountNumber"></a>
# **updateAnAccountNumber**
> AccountNumber updateAnAccountNumber(accountNumberId, updateAnAccountNumberParameters)

Update an Account Number

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountNumberId = "account_number_v18nkfqm6afpsrvy82b2"; // String | 
    UpdateAnAccountNumberParameters updateAnAccountNumberParameters = new UpdateAnAccountNumberParameters(); // UpdateAnAccountNumberParameters | 
    try {
      AccountNumber result = apiInstance.updateAnAccountNumber(accountNumberId, updateAnAccountNumberParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateAnAccountNumber");
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
| **accountNumberId** | **String**|  | |
| **updateAnAccountNumberParameters** | [**UpdateAnAccountNumberParameters**](UpdateAnAccountNumberParameters.md)|  | |

### Return type

[**AccountNumber**](AccountNumber.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Account Number |  -  |
| **0** | Error |  -  |

<a id="updateAnEventSubscription"></a>
# **updateAnEventSubscription**
> EventSubscription updateAnEventSubscription(eventSubscriptionId, updateAnEventSubscriptionParameters)

Update an Event Subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String eventSubscriptionId = "event_subscription_001dzz0r20rcdxgb013zqb8m04g"; // String | 
    UpdateAnEventSubscriptionParameters updateAnEventSubscriptionParameters = new UpdateAnEventSubscriptionParameters(); // UpdateAnEventSubscriptionParameters | 
    try {
      EventSubscription result = apiInstance.updateAnEventSubscription(eventSubscriptionId, updateAnEventSubscriptionParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateAnEventSubscription");
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
| **eventSubscriptionId** | **String**|  | |
| **updateAnEventSubscriptionParameters** | [**UpdateAnEventSubscriptionParameters**](UpdateAnEventSubscriptionParameters.md)|  | |

### Return type

[**EventSubscription**](EventSubscription.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Event Subscription |  -  |
| **0** | Error |  -  |

<a id="updateAnExternalAccount"></a>
# **updateAnExternalAccount**
> ExternalAccount updateAnExternalAccount(externalAccountId, updateAnExternalAccountParameters)

Update an External Account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.increase.com");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String externalAccountId = "external_account_ukk55lr923a3ac0pp7iv"; // String | 
    UpdateAnExternalAccountParameters updateAnExternalAccountParameters = new UpdateAnExternalAccountParameters(); // UpdateAnExternalAccountParameters | 
    try {
      ExternalAccount result = apiInstance.updateAnExternalAccount(externalAccountId, updateAnExternalAccountParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateAnExternalAccount");
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
| **externalAccountId** | **String**|  | |
| **updateAnExternalAccountParameters** | [**UpdateAnExternalAccountParameters**](UpdateAnExternalAccountParameters.md)|  | |

### Return type

[**ExternalAccount**](ExternalAccount.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | External Account |  -  |
| **0** | Error |  -  |

