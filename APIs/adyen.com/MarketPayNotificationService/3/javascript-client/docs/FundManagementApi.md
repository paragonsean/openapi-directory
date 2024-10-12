# ClassicPlatformsNotifications.FundManagementApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postACCOUNTFUNDSBELOWTHRESHOLD**](FundManagementApi.md#postACCOUNTFUNDSBELOWTHRESHOLD) | **POST** /ACCOUNT_FUNDS_BELOW_THRESHOLD | Liable account&#39;s funds are below configured threshold
[**postACCOUNTHOLDERPAYOUT**](FundManagementApi.md#postACCOUNTHOLDERPAYOUT) | **POST** /ACCOUNT_HOLDER_PAYOUT | Paid out to account holder
[**postBENEFICIARYSETUP**](FundManagementApi.md#postBENEFICIARYSETUP) | **POST** /BENEFICIARY_SETUP | Beneficiary defined
[**postCOMPENSATENEGATIVEBALANCE**](FundManagementApi.md#postCOMPENSATENEGATIVEBALANCE) | **POST** /COMPENSATE_NEGATIVE_BALANCE | Negative account balances compensated
[**postDIRECTDEBITINITIATED**](FundManagementApi.md#postDIRECTDEBITINITIATED) | **POST** /DIRECT_DEBIT_INITIATED | Automated direct debit initiated
[**postREFUNDFUNDSTRANSFER**](FundManagementApi.md#postREFUNDFUNDSTRANSFER) | **POST** /REFUND_FUNDS_TRANSFER | Funds transfer between accounts refunded
[**postSCHEDULEDREFUNDS**](FundManagementApi.md#postSCHEDULEDREFUNDS) | **POST** /SCHEDULED_REFUNDS | &#39;Refund Transfers Not Paid Out&#39; call processed and refunds scheduled
[**postTRANSFERFUNDS**](FundManagementApi.md#postTRANSFERFUNDS) | **POST** /TRANSFER_FUNDS | Funds transferred between accounts



## postACCOUNTFUNDSBELOWTHRESHOLD

> NotificationResponse postACCOUNTFUNDSBELOWTHRESHOLD(opts)

Liable account&#39;s funds are below configured threshold

Adyen sends this notification when the current funds of your liable account are below the configured threshold.

### Example

```javascript
import ClassicPlatformsNotifications from 'classic_platforms_notifications';
let defaultClient = ClassicPlatformsNotifications.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';

let apiInstance = new ClassicPlatformsNotifications.FundManagementApi();
let opts = {
  'accountFundsBelowThresholdNotification': new ClassicPlatformsNotifications.AccountFundsBelowThresholdNotification() // AccountFundsBelowThresholdNotification | 
};
apiInstance.postACCOUNTFUNDSBELOWTHRESHOLD(opts, (error, data, response) => {
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
 **accountFundsBelowThresholdNotification** | [**AccountFundsBelowThresholdNotification**](AccountFundsBelowThresholdNotification.md)|  | [optional] 

### Return type

[**NotificationResponse**](NotificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postACCOUNTHOLDERPAYOUT

> NotificationResponse postACCOUNTHOLDERPAYOUT(opts)

Paid out to account holder

Adyen sends this notification when a [payout request](https://docs.adyen.com/api-explorer/#/Fund/latest/post/payoutAccountHolder) to an account holder is processed and the payout is scheduled.

### Example

```javascript
import ClassicPlatformsNotifications from 'classic_platforms_notifications';
let defaultClient = ClassicPlatformsNotifications.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';

let apiInstance = new ClassicPlatformsNotifications.FundManagementApi();
let opts = {
  'accountHolderPayoutNotification': new ClassicPlatformsNotifications.AccountHolderPayoutNotification() // AccountHolderPayoutNotification | 
};
apiInstance.postACCOUNTHOLDERPAYOUT(opts, (error, data, response) => {
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
 **accountHolderPayoutNotification** | [**AccountHolderPayoutNotification**](AccountHolderPayoutNotification.md)|  | [optional] 

### Return type

[**NotificationResponse**](NotificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postBENEFICIARYSETUP

> NotificationResponse postBENEFICIARYSETUP(opts)

Beneficiary defined

Adyen sends this notification when a [benefactor/beneficiary relationship is created](https://docs.adyen.com/api-explorer/#/Fund/latest/post/transferFunds).

### Example

```javascript
import ClassicPlatformsNotifications from 'classic_platforms_notifications';
let defaultClient = ClassicPlatformsNotifications.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';

let apiInstance = new ClassicPlatformsNotifications.FundManagementApi();
let opts = {
  'beneficiarySetupNotification': new ClassicPlatformsNotifications.BeneficiarySetupNotification() // BeneficiarySetupNotification | 
};
apiInstance.postBENEFICIARYSETUP(opts, (error, data, response) => {
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
 **beneficiarySetupNotification** | [**BeneficiarySetupNotification**](BeneficiarySetupNotification.md)|  | [optional] 

### Return type

[**NotificationResponse**](NotificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postCOMPENSATENEGATIVEBALANCE

> NotificationResponse postCOMPENSATENEGATIVEBALANCE(opts)

Negative account balances compensated

Adyen sends this notification when funds are transferred from your platform&#39;s liable account to an overdrawn account to compensate for the overdraft.

### Example

```javascript
import ClassicPlatformsNotifications from 'classic_platforms_notifications';
let defaultClient = ClassicPlatformsNotifications.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';

let apiInstance = new ClassicPlatformsNotifications.FundManagementApi();
let opts = {
  'compensateNegativeBalanceNotification': new ClassicPlatformsNotifications.CompensateNegativeBalanceNotification() // CompensateNegativeBalanceNotification | 
};
apiInstance.postCOMPENSATENEGATIVEBALANCE(opts, (error, data, response) => {
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
 **compensateNegativeBalanceNotification** | [**CompensateNegativeBalanceNotification**](CompensateNegativeBalanceNotification.md)|  | [optional] 

### Return type

[**NotificationResponse**](NotificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postDIRECTDEBITINITIATED

> NotificationResponse postDIRECTDEBITINITIATED(opts)

Automated direct debit initiated

Adyen sends this notification when a [direct debit is initiated](https://docs.adyen.com/api-explorer/#/Fund/latest/post/debitAccountHolder).

### Example

```javascript
import ClassicPlatformsNotifications from 'classic_platforms_notifications';
let defaultClient = ClassicPlatformsNotifications.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';

let apiInstance = new ClassicPlatformsNotifications.FundManagementApi();
let opts = {
  'directDebitInitiatedNotification': new ClassicPlatformsNotifications.DirectDebitInitiatedNotification() // DirectDebitInitiatedNotification | 
};
apiInstance.postDIRECTDEBITINITIATED(opts, (error, data, response) => {
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
 **directDebitInitiatedNotification** | [**DirectDebitInitiatedNotification**](DirectDebitInitiatedNotification.md)|  | [optional] 

### Return type

[**NotificationResponse**](NotificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postREFUNDFUNDSTRANSFER

> NotificationResponse postREFUNDFUNDSTRANSFER(opts)

Funds transfer between accounts refunded

Adyen sends this notification when [funds transferred between accounts are refunded](https://docs.adyen.com/api-explorer/#/Fund/v6/latest/refundFundsTransfer).

### Example

```javascript
import ClassicPlatformsNotifications from 'classic_platforms_notifications';
let defaultClient = ClassicPlatformsNotifications.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';

let apiInstance = new ClassicPlatformsNotifications.FundManagementApi();
let opts = {
  'refundFundsTransferNotification': new ClassicPlatformsNotifications.RefundFundsTransferNotification() // RefundFundsTransferNotification | 
};
apiInstance.postREFUNDFUNDSTRANSFER(opts, (error, data, response) => {
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
 **refundFundsTransferNotification** | [**RefundFundsTransferNotification**](RefundFundsTransferNotification.md)|  | [optional] 

### Return type

[**NotificationResponse**](NotificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postSCHEDULEDREFUNDS

> NotificationResponse postSCHEDULEDREFUNDS(opts)

&#39;Refund Transfers Not Paid Out&#39; call processed and refunds scheduled

Adyen sends this notification when a request to [refund transfers that are not yet paid out](https://docs.adyen.com/api-explorer/#/Fund/latest/refundNotPaidOutTransfers) is processed and the associated refunds are scheduled.

### Example

```javascript
import ClassicPlatformsNotifications from 'classic_platforms_notifications';
let defaultClient = ClassicPlatformsNotifications.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';

let apiInstance = new ClassicPlatformsNotifications.FundManagementApi();
let opts = {
  'scheduledRefundsNotification': new ClassicPlatformsNotifications.ScheduledRefundsNotification() // ScheduledRefundsNotification | 
};
apiInstance.postSCHEDULEDREFUNDS(opts, (error, data, response) => {
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
 **scheduledRefundsNotification** | [**ScheduledRefundsNotification**](ScheduledRefundsNotification.md)|  | [optional] 

### Return type

[**NotificationResponse**](NotificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postTRANSFERFUNDS

> NotificationResponse postTRANSFERFUNDS(opts)

Funds transferred between accounts

Adyen sends this notification when [funds are transferred between accounts](https://docs.adyen.com/api-explorer/#/Fund/latest/post/transferFunds).

### Example

```javascript
import ClassicPlatformsNotifications from 'classic_platforms_notifications';
let defaultClient = ClassicPlatformsNotifications.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';

let apiInstance = new ClassicPlatformsNotifications.FundManagementApi();
let opts = {
  'transferFundsNotification': new ClassicPlatformsNotifications.TransferFundsNotification() // TransferFundsNotification | 
};
apiInstance.postTRANSFERFUNDS(opts, (error, data, response) => {
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
 **transferFundsNotification** | [**TransferFundsNotification**](TransferFundsNotification.md)|  | [optional] 

### Return type

[**NotificationResponse**](NotificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

