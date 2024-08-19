# AdyenTerminalApi.DefaultApi

All URIs are relative to *https://terminal-api-test.adyen.com/sync*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adminPost**](DefaultApi.md#adminPost) | **POST** /admin | Admin Request
[**balanceinquiryPost**](DefaultApi.md#balanceinquiryPost) | **POST** /balanceinquiry | BalanceInquiry Request
[**cardacquisitionPost**](DefaultApi.md#cardacquisitionPost) | **POST** /cardacquisition | CardAcquisition Request
[**cardreaderapduPost**](DefaultApi.md#cardreaderapduPost) | **POST** /cardreaderapdu | CardReaderAPDU Request
[**diagnosisPost**](DefaultApi.md#diagnosisPost) | **POST** /diagnosis | Diagnosis Request
[**displayPost**](DefaultApi.md#displayPost) | **POST** /display | Display Request
[**enableservicePost**](DefaultApi.md#enableservicePost) | **POST** /enableservice | EnableService Request
[**gettotalsPost**](DefaultApi.md#gettotalsPost) | **POST** /gettotals | GetTotals Request
[**inputPost**](DefaultApi.md#inputPost) | **POST** /input | Input Request
[**loginPost**](DefaultApi.md#loginPost) | **POST** /login | Login Request
[**logoutPost**](DefaultApi.md#logoutPost) | **POST** /logout | Logout Request
[**loyaltyPost**](DefaultApi.md#loyaltyPost) | **POST** /loyalty | Loyalty Request
[**paymentPost**](DefaultApi.md#paymentPost) | **POST** /payment | Payment Request
[**printPost**](DefaultApi.md#printPost) | **POST** /print | Print Request
[**reconciliationPost**](DefaultApi.md#reconciliationPost) | **POST** /reconciliation | Reconciliation Request
[**reversalPost**](DefaultApi.md#reversalPost) | **POST** /reversal | Reversal Request
[**storedvaluePost**](DefaultApi.md#storedvaluePost) | **POST** /storedvalue | StoredValue Request
[**transactionstatusPost**](DefaultApi.md#transactionstatusPost) | **POST** /transactionstatus | TransactionStatus Request



## adminPost

> AdminResponse adminPost(opts)

Admin Request

Empty. Content of the Custom Admin Request message.

### Example

```javascript
import AdyenTerminalApi from 'adyen_terminal_api';
let defaultClient = AdyenTerminalApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AdyenTerminalApi.DefaultApi();
let opts = {
  'adminRequest': new AdyenTerminalApi.AdminRequest() // AdminRequest | 
};
apiInstance.adminPost(opts, (error, data, response) => {
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
 **adminRequest** | [**AdminRequest**](AdminRequest.md)|  | [optional] 

### Return type

[**AdminResponse**](AdminResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## balanceinquiryPost

> BalanceInquiryResponse balanceinquiryPost(opts)

BalanceInquiry Request

It conveys Information related to the account for which a Balance Inquiry is requested. Content of the Balance Inquiry Request message.

### Example

```javascript
import AdyenTerminalApi from 'adyen_terminal_api';
let defaultClient = AdyenTerminalApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AdyenTerminalApi.DefaultApi();
let opts = {
  'balanceInquiryRequest': new AdyenTerminalApi.BalanceInquiryRequest() // BalanceInquiryRequest | 
};
apiInstance.balanceinquiryPost(opts, (error, data, response) => {
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
 **balanceInquiryRequest** | [**BalanceInquiryRequest**](BalanceInquiryRequest.md)|  | [optional] 

### Return type

[**BalanceInquiryResponse**](BalanceInquiryResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## cardacquisitionPost

> CardAcquisitionResponse cardacquisitionPost(opts)

CardAcquisition Request

It conveys Information related to the payment and loyalty cards to read and analyse. This message pair is usually followed by a message pair (e.g. payment or loyalty) which refers to this Card Acquisition message pair. Content of the Card Acquisition Request message.

### Example

```javascript
import AdyenTerminalApi from 'adyen_terminal_api';
let defaultClient = AdyenTerminalApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AdyenTerminalApi.DefaultApi();
let opts = {
  'cardAcquisitionRequest': new AdyenTerminalApi.CardAcquisitionRequest() // CardAcquisitionRequest | 
};
apiInstance.cardacquisitionPost(opts, (error, data, response) => {
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
 **cardAcquisitionRequest** | [**CardAcquisitionRequest**](CardAcquisitionRequest.md)|  | [optional] 

### Return type

[**CardAcquisitionResponse**](CardAcquisitionResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## cardreaderapduPost

> CardReaderAPDUResponse cardreaderapduPost(opts)

CardReaderAPDU Request

It contains the APDU request to send to the chip of the card, and a possible invitation message to display on the CashierInterface or the CustomerInterface. Content of the Card Reader APDU Request message.

### Example

```javascript
import AdyenTerminalApi from 'adyen_terminal_api';
let defaultClient = AdyenTerminalApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AdyenTerminalApi.DefaultApi();
let opts = {
  'cardReaderAPDURequest': new AdyenTerminalApi.CardReaderAPDURequest() // CardReaderAPDURequest | 
};
apiInstance.cardreaderapduPost(opts, (error, data, response) => {
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
 **cardReaderAPDURequest** | [**CardReaderAPDURequest**](CardReaderAPDURequest.md)|  | [optional] 

### Return type

[**CardReaderAPDUResponse**](CardReaderAPDUResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## diagnosisPost

> DiagnosisResponse diagnosisPost(opts)

Diagnosis Request

It conveys Information related to the target POI for which the diagnosis is requested. Content of the Diagnosis Request message.

### Example

```javascript
import AdyenTerminalApi from 'adyen_terminal_api';
let defaultClient = AdyenTerminalApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AdyenTerminalApi.DefaultApi();
let opts = {
  'diagnosisRequest': new AdyenTerminalApi.DiagnosisRequest() // DiagnosisRequest | 
};
apiInstance.diagnosisPost(opts, (error, data, response) => {
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
 **diagnosisRequest** | [**DiagnosisRequest**](DiagnosisRequest.md)|  | [optional] 

### Return type

[**DiagnosisResponse**](DiagnosisResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## displayPost

> DisplayResponse displayPost(opts)

Display Request

It conveys the data to display and the way to process the display. It contains the complete content to display. It might contain an operation (the DisplayOutput element) per Display Device type. Content of the Display Request message.

### Example

```javascript
import AdyenTerminalApi from 'adyen_terminal_api';
let defaultClient = AdyenTerminalApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AdyenTerminalApi.DefaultApi();
let opts = {
  'displayRequest': new AdyenTerminalApi.DisplayRequest() // DisplayRequest | 
};
apiInstance.displayPost(opts, (error, data, response) => {
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
 **displayRequest** | [**DisplayRequest**](DisplayRequest.md)|  | [optional] 

### Return type

[**DisplayResponse**](DisplayResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## enableservicePost

> EnableServiceResponse enableservicePost(opts)

EnableService Request

It conveys the services that will be enabled for the  POI Terminal without the request of the Sale System, and a possible invitation for the Customer to start the services. Content of the Enable Service Request message.

### Example

```javascript
import AdyenTerminalApi from 'adyen_terminal_api';
let defaultClient = AdyenTerminalApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AdyenTerminalApi.DefaultApi();
let opts = {
  'enableServiceRequest': new AdyenTerminalApi.EnableServiceRequest() // EnableServiceRequest | 
};
apiInstance.enableservicePost(opts, (error, data, response) => {
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
 **enableServiceRequest** | [**EnableServiceRequest**](EnableServiceRequest.md)|  | [optional] 

### Return type

[**EnableServiceResponse**](EnableServiceResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## gettotalsPost

> GetTotalsResponse gettotalsPost(opts)

GetTotals Request

It conveys information from the Sale System related to the scope and the format of the totals to be computed by the POI System. Content of the Get Totals Request message.

### Example

```javascript
import AdyenTerminalApi from 'adyen_terminal_api';
let defaultClient = AdyenTerminalApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AdyenTerminalApi.DefaultApi();
let opts = {
  'getTotalsRequest': new AdyenTerminalApi.GetTotalsRequest() // GetTotalsRequest | 
};
apiInstance.gettotalsPost(opts, (error, data, response) => {
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
 **getTotalsRequest** | [**GetTotalsRequest**](GetTotalsRequest.md)|  | [optional] 

### Return type

[**GetTotalsResponse**](GetTotalsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## inputPost

> InputResponse inputPost(opts)

Input Request

It conveys data to display and the way to process the display, and contains the complete content to display. In addition to the display on the Input Device, it might contain an operation (the DisplayOutput element) per Display Device type. Content of the Input Request message.

### Example

```javascript
import AdyenTerminalApi from 'adyen_terminal_api';
let defaultClient = AdyenTerminalApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AdyenTerminalApi.DefaultApi();
let opts = {
  'inputRequest': new AdyenTerminalApi.InputRequest() // InputRequest | 
};
apiInstance.inputPost(opts, (error, data, response) => {
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
 **inputRequest** | [**InputRequest**](InputRequest.md)|  | [optional] 

### Return type

[**InputResponse**](InputResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## loginPost

> LoginResponse loginPost(opts)

Login Request

It conveys Information related to the session (period between a Login and the following Logout) to process. Content of the Login Request message.

### Example

```javascript
import AdyenTerminalApi from 'adyen_terminal_api';
let defaultClient = AdyenTerminalApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AdyenTerminalApi.DefaultApi();
let opts = {
  'loginRequest': new AdyenTerminalApi.LoginRequest() // LoginRequest | 
};
apiInstance.loginPost(opts, (error, data, response) => {
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
 **loginRequest** | [**LoginRequest**](LoginRequest.md)|  | [optional] 

### Return type

[**LoginResponse**](LoginResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## logoutPost

> LogoutResponse logoutPost(opts)

Logout Request

Empty. Content of the Logout Request message.

### Example

```javascript
import AdyenTerminalApi from 'adyen_terminal_api';
let defaultClient = AdyenTerminalApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AdyenTerminalApi.DefaultApi();
let opts = {
  'logoutRequest': new AdyenTerminalApi.LogoutRequest() // LogoutRequest | 
};
apiInstance.logoutPost(opts, (error, data, response) => {
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
 **logoutRequest** | [**LogoutRequest**](LogoutRequest.md)|  | [optional] 

### Return type

[**LogoutResponse**](LogoutResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## loyaltyPost

> LoyaltyResponse loyaltyPost(opts)

Loyalty Request

It conveys Information related to the Loyalty transaction to process. Content of the Loyalty Request message.

### Example

```javascript
import AdyenTerminalApi from 'adyen_terminal_api';
let defaultClient = AdyenTerminalApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AdyenTerminalApi.DefaultApi();
let opts = {
  'loyaltyRequest': new AdyenTerminalApi.LoyaltyRequest() // LoyaltyRequest | 
};
apiInstance.loyaltyPost(opts, (error, data, response) => {
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
 **loyaltyRequest** | [**LoyaltyRequest**](LoyaltyRequest.md)|  | [optional] 

### Return type

[**LoyaltyResponse**](LoyaltyResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## paymentPost

> PaymentResponse paymentPost(opts)

Payment Request

Request sent to terminal to initiate payment.  It conveys Information related to the Payment transaction to process. Content of the Payment Request message.

### Example

```javascript
import AdyenTerminalApi from 'adyen_terminal_api';
let defaultClient = AdyenTerminalApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AdyenTerminalApi.DefaultApi();
let opts = {
  'paymentRequest': new AdyenTerminalApi.PaymentRequest() // PaymentRequest | 
};
apiInstance.paymentPost(opts, (error, data, response) => {
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
 **paymentRequest** | [**PaymentRequest**](PaymentRequest.md)|  | [optional] 

### Return type

[**PaymentResponse**](PaymentResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## printPost

> PrintResponse printPost(opts)

Print Request

It conveys the data to print and the way to process the print. It contains the complete content to print. Content of the Print Request message.

### Example

```javascript
import AdyenTerminalApi from 'adyen_terminal_api';
let defaultClient = AdyenTerminalApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AdyenTerminalApi.DefaultApi();
let opts = {
  'printRequest': new AdyenTerminalApi.PrintRequest() // PrintRequest | 
};
apiInstance.printPost(opts, (error, data, response) => {
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
 **printRequest** | [**PrintRequest**](PrintRequest.md)|  | [optional] 

### Return type

[**PrintResponse**](PrintResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## reconciliationPost

> ReconciliationResponse reconciliationPost(opts)

Reconciliation Request

It conveys Information related to the Reconciliation requested by the Sale System. Content of the Reconciliation Request message.

### Example

```javascript
import AdyenTerminalApi from 'adyen_terminal_api';
let defaultClient = AdyenTerminalApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AdyenTerminalApi.DefaultApi();
let opts = {
  'reconciliationRequest': new AdyenTerminalApi.ReconciliationRequest() // ReconciliationRequest | 
};
apiInstance.reconciliationPost(opts, (error, data, response) => {
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
 **reconciliationRequest** | [**ReconciliationRequest**](ReconciliationRequest.md)|  | [optional] 

### Return type

[**ReconciliationResponse**](ReconciliationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## reversalPost

> ReversalResponse reversalPost(opts)

Reversal Request

It conveys Information related to the reversal of a previous payment or a loyalty transaction. Content of the Reversal Request message.

### Example

```javascript
import AdyenTerminalApi from 'adyen_terminal_api';
let defaultClient = AdyenTerminalApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AdyenTerminalApi.DefaultApi();
let opts = {
  'reversalRequest': new AdyenTerminalApi.ReversalRequest() // ReversalRequest | 
};
apiInstance.reversalPost(opts, (error, data, response) => {
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
 **reversalRequest** | [**ReversalRequest**](ReversalRequest.md)|  | [optional] 

### Return type

[**ReversalResponse**](ReversalResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## storedvaluePost

> StoredValueResponse storedvaluePost(opts)

StoredValue Request

It conveys Information related to the Stored Value transaction to process. Content of the Stored Value Request message.

### Example

```javascript
import AdyenTerminalApi from 'adyen_terminal_api';
let defaultClient = AdyenTerminalApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AdyenTerminalApi.DefaultApi();
let opts = {
  'storedValueRequest': new AdyenTerminalApi.StoredValueRequest() // StoredValueRequest | 
};
apiInstance.storedvaluePost(opts, (error, data, response) => {
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
 **storedValueRequest** | [**StoredValueRequest**](StoredValueRequest.md)|  | [optional] 

### Return type

[**StoredValueResponse**](StoredValueResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## transactionstatusPost

> TransactionStatusResponse transactionstatusPost(opts)

TransactionStatus Request

It conveys Information requested for status of the last or current Payment, Loyalty or Reversal transaction. Content of the TransactionStatus Request message.

### Example

```javascript
import AdyenTerminalApi from 'adyen_terminal_api';
let defaultClient = AdyenTerminalApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AdyenTerminalApi.DefaultApi();
let opts = {
  'transactionStatusRequest': new AdyenTerminalApi.TransactionStatusRequest() // TransactionStatusRequest | 
};
apiInstance.transactionstatusPost(opts, (error, data, response) => {
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
 **transactionStatusRequest** | [**TransactionStatusRequest**](TransactionStatusRequest.md)|  | [optional] 

### Return type

[**TransactionStatusResponse**](TransactionStatusResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

