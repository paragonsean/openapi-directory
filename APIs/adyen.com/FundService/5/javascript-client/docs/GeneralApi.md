# FundApi.GeneralApi

All URIs are relative to *https://cal-test.adyen.com/cal/services/Fund/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postAccountHolderBalance**](GeneralApi.md#postAccountHolderBalance) | **POST** /accountHolderBalance | Get the balances of an account holder
[**postAccountHolderTransactionList**](GeneralApi.md#postAccountHolderTransactionList) | **POST** /accountHolderTransactionList | Get a list of transactions
[**postDebitAccountHolder**](GeneralApi.md#postDebitAccountHolder) | **POST** /debitAccountHolder | Send a direct debit request
[**postPayoutAccountHolder**](GeneralApi.md#postPayoutAccountHolder) | **POST** /payoutAccountHolder | Pay out from an account to the account holder
[**postRefundFundsTransfer**](GeneralApi.md#postRefundFundsTransfer) | **POST** /refundFundsTransfer | Refund a funds transfer
[**postRefundNotPaidOutTransfers**](GeneralApi.md#postRefundNotPaidOutTransfers) | **POST** /refundNotPaidOutTransfers | Refund all transactions of an account since the most recent payout
[**postSetupBeneficiary**](GeneralApi.md#postSetupBeneficiary) | **POST** /setupBeneficiary | Designate a beneficiary account and transfer the benefactor&#39;s current balance
[**postTransferFunds**](GeneralApi.md#postTransferFunds) | **POST** /transferFunds | Transfer funds between platform accounts



## postAccountHolderBalance

> AccountHolderBalanceResponse postAccountHolderBalance(opts)

Get the balances of an account holder

Returns the account balances of an account holder. An account&#39;s balances are organized according by currencies. This mean that an account may have multiple balances: one for each currency.

### Example

```javascript
import FundApi from 'fund_api';
let defaultClient = FundApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new FundApi.GeneralApi();
let opts = {
  'accountHolderBalanceRequest': new FundApi.AccountHolderBalanceRequest() // AccountHolderBalanceRequest | 
};
apiInstance.postAccountHolderBalance(opts, (error, data, response) => {
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
 **accountHolderBalanceRequest** | [**AccountHolderBalanceRequest**](AccountHolderBalanceRequest.md)|  | [optional] 

### Return type

[**AccountHolderBalanceResponse**](AccountHolderBalanceResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postAccountHolderTransactionList

> AccountHolderTransactionListResponse postAccountHolderTransactionList(opts)

Get a list of transactions

Returns a list of transactions for an account holder&#39;s accounts. You can specify the accounts and transaction statuses to be included on the list. The call returns a maximum of 50 transactions for each account. To retrieve all transactions, you must make another call with the &#39;page&#39; value incremented. Transactions are listed in chronological order, with the most recent transaction first.

### Example

```javascript
import FundApi from 'fund_api';
let defaultClient = FundApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new FundApi.GeneralApi();
let opts = {
  'accountHolderTransactionListRequest': new FundApi.AccountHolderTransactionListRequest() // AccountHolderTransactionListRequest | 
};
apiInstance.postAccountHolderTransactionList(opts, (error, data, response) => {
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
 **accountHolderTransactionListRequest** | [**AccountHolderTransactionListRequest**](AccountHolderTransactionListRequest.md)|  | [optional] 

### Return type

[**AccountHolderTransactionListResponse**](AccountHolderTransactionListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postDebitAccountHolder

> DebitAccountHolderResponse postDebitAccountHolder(opts)

Send a direct debit request

Sends a direct debit request to an account holder&#39;s bank account. If the direct debit is successful, the funds are settled in the accounts specified in the split instructions. Adyen sends the result of the direct debit in a [&#x60;DIRECT_DEBIT_INITIATED&#x60;](https://docs.adyen.com/api-explorer/#/NotificationService/latest/post/DIRECT_DEBIT_INITIATED) notification webhook.   To learn more about direct debits, see [Top up accounts](https://docs.adyen.com/marketplaces-and-platforms/classic/top-up-accounts).

### Example

```javascript
import FundApi from 'fund_api';
let defaultClient = FundApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new FundApi.GeneralApi();
let opts = {
  'debitAccountHolderRequest': new FundApi.DebitAccountHolderRequest() // DebitAccountHolderRequest | 
};
apiInstance.postDebitAccountHolder(opts, (error, data, response) => {
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
 **debitAccountHolderRequest** | [**DebitAccountHolderRequest**](DebitAccountHolderRequest.md)|  | [optional] 

### Return type

[**DebitAccountHolderResponse**](DebitAccountHolderResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postPayoutAccountHolder

> PayoutAccountHolderResponse postPayoutAccountHolder(opts)

Pay out from an account to the account holder

Pays out a specified amount from an account to the bank account of account holder.

### Example

```javascript
import FundApi from 'fund_api';
let defaultClient = FundApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new FundApi.GeneralApi();
let opts = {
  'payoutAccountHolderRequest': new FundApi.PayoutAccountHolderRequest() // PayoutAccountHolderRequest | 
};
apiInstance.postPayoutAccountHolder(opts, (error, data, response) => {
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
 **payoutAccountHolderRequest** | [**PayoutAccountHolderRequest**](PayoutAccountHolderRequest.md)|  | [optional] 

### Return type

[**PayoutAccountHolderResponse**](PayoutAccountHolderResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postRefundFundsTransfer

> RefundFundsTransferResponse postRefundFundsTransfer(opts)

Refund a funds transfer

Refunds funds transferred from one account to another. Both accounts must be in the same platform, but can have different account holders. 

### Example

```javascript
import FundApi from 'fund_api';
let defaultClient = FundApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new FundApi.GeneralApi();
let opts = {
  'refundFundsTransferRequest': new FundApi.RefundFundsTransferRequest() // RefundFundsTransferRequest | 
};
apiInstance.postRefundFundsTransfer(opts, (error, data, response) => {
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
 **refundFundsTransferRequest** | [**RefundFundsTransferRequest**](RefundFundsTransferRequest.md)|  | [optional] 

### Return type

[**RefundFundsTransferResponse**](RefundFundsTransferResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postRefundNotPaidOutTransfers

> RefundNotPaidOutTransfersResponse postRefundNotPaidOutTransfers(opts)

Refund all transactions of an account since the most recent payout

Refunds all the transactions of an account that have taken place since the most recent payout. This request is on a account basis (as opposed to a payment basis), so only the portion of the payment that was made to the specified account is refunded. The commissions, fees, and payments to other accounts remain in the accounts to which they were sent as designated by the original payment&#39;s split details.

### Example

```javascript
import FundApi from 'fund_api';
let defaultClient = FundApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new FundApi.GeneralApi();
let opts = {
  'refundNotPaidOutTransfersRequest': new FundApi.RefundNotPaidOutTransfersRequest() // RefundNotPaidOutTransfersRequest | 
};
apiInstance.postRefundNotPaidOutTransfers(opts, (error, data, response) => {
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
 **refundNotPaidOutTransfersRequest** | [**RefundNotPaidOutTransfersRequest**](RefundNotPaidOutTransfersRequest.md)|  | [optional] 

### Return type

[**RefundNotPaidOutTransfersResponse**](RefundNotPaidOutTransfersResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postSetupBeneficiary

> SetupBeneficiaryResponse postSetupBeneficiary(opts)

Designate a beneficiary account and transfer the benefactor&#39;s current balance

Defines a benefactor and a beneficiary relationship between two accounts. At the time of benefactor/beneficiary setup, the funds in the benefactor account are transferred to the beneficiary account, and any further payments to the benefactor account are automatically sent to the beneficiary account. A series of benefactor/beneficiaries may not exceed four beneficiaries and may not have a cycle in it.

### Example

```javascript
import FundApi from 'fund_api';
let defaultClient = FundApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new FundApi.GeneralApi();
let opts = {
  'setupBeneficiaryRequest': new FundApi.SetupBeneficiaryRequest() // SetupBeneficiaryRequest | 
};
apiInstance.postSetupBeneficiary(opts, (error, data, response) => {
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
 **setupBeneficiaryRequest** | [**SetupBeneficiaryRequest**](SetupBeneficiaryRequest.md)|  | [optional] 

### Return type

[**SetupBeneficiaryResponse**](SetupBeneficiaryResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postTransferFunds

> TransferFundsResponse postTransferFunds(opts)

Transfer funds between platform accounts

Transfers funds from one account to another account. Both accounts must be in the same platform, but can have different account holders. The transfer must include a transfer code, which should be determined by the platform, in compliance with local regulations.

### Example

```javascript
import FundApi from 'fund_api';
let defaultClient = FundApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new FundApi.GeneralApi();
let opts = {
  'transferFundsRequest': new FundApi.TransferFundsRequest() // TransferFundsRequest | 
};
apiInstance.postTransferFunds(opts, (error, data, response) => {
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
 **transferFundsRequest** | [**TransferFundsRequest**](TransferFundsRequest.md)|  | [optional] 

### Return type

[**TransferFundsResponse**](TransferFundsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

