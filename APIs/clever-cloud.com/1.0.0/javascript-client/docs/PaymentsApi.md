# CleverCloudApi.PaymentsApi

All URIs are relative to *https://api.clever-cloud.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteOrganisationsIdPaymentsBillingsBid_1**](PaymentsApi.md#deleteOrganisationsIdPaymentsBillingsBid_1) | **DELETE** /organisations/{id}/payments/billings/{bid} | 
[**deleteOrganisationsIdPaymentsRecurring_1**](PaymentsApi.md#deleteOrganisationsIdPaymentsRecurring_1) | **DELETE** /organisations/{id}/payments/recurring | 
[**deleteSelfPaymentsBillingsBid_0**](PaymentsApi.md#deleteSelfPaymentsBillingsBid_0) | **DELETE** /self/payments/billings/{bid} | 
[**deleteSelfPaymentsMethodsMId_0**](PaymentsApi.md#deleteSelfPaymentsMethodsMId_0) | **DELETE** /self/payments/methods/{mId} | 
[**deleteSelfPaymentsRecurring_0**](PaymentsApi.md#deleteSelfPaymentsRecurring_0) | **DELETE** /self/payments/recurring | 
[**getOrganisationsIdPaymentsBillingsBidPdf_1**](PaymentsApi.md#getOrganisationsIdPaymentsBillingsBidPdf_1) | **GET** /organisations/{id}/payments/billings/{bid}.pdf | 
[**getOrganisationsIdPaymentsBillingsBid_1**](PaymentsApi.md#getOrganisationsIdPaymentsBillingsBid_1) | **GET** /organisations/{id}/payments/billings/{bid} | 
[**getOrganisationsIdPaymentsBillings_1**](PaymentsApi.md#getOrganisationsIdPaymentsBillings_1) | **GET** /organisations/{id}/payments/billings | 
[**getOrganisationsIdPaymentsFullPricePrice_1**](PaymentsApi.md#getOrganisationsIdPaymentsFullPricePrice_1) | **GET** /organisations/{id}/payments/fullprice/{price} | 
[**getPaymentsCouponsName_0**](PaymentsApi.md#getPaymentsCouponsName_0) | **GET** /payments/coupons/{name} | 
[**getPaymentsProviders_0**](PaymentsApi.md#getPaymentsProviders_0) | **GET** /payments/providers | 
[**getPaymentsTokensStripe_0**](PaymentsApi.md#getPaymentsTokensStripe_0) | **GET** /payments/tokens/stripe | 
[**getSelfPaymentsBillingsBidPdf_0**](PaymentsApi.md#getSelfPaymentsBillingsBidPdf_0) | **GET** /self/payments/billings/{bid}.pdf | 
[**getSelfPaymentsBillingsBid_0**](PaymentsApi.md#getSelfPaymentsBillingsBid_0) | **GET** /self/payments/billings/{bid} | 
[**getSelfPaymentsBillings_0**](PaymentsApi.md#getSelfPaymentsBillings_0) | **GET** /self/payments/billings | 
[**getSelfPaymentsFullpricePrice_0**](PaymentsApi.md#getSelfPaymentsFullpricePrice_0) | **GET** /self/payments/fullprice/{price} | 
[**getSelfPaymentsMethods_0**](PaymentsApi.md#getSelfPaymentsMethods_0) | **GET** /self/payments/methods | 
[**organisationsIdPaymentsBillingsUnpaidGet_1**](PaymentsApi.md#organisationsIdPaymentsBillingsUnpaidGet_1) | **GET** /organisations/{id}/payments/billings/unpaid | 
[**organisationsIdPaymentsMethodsDefaultGet_1**](PaymentsApi.md#organisationsIdPaymentsMethodsDefaultGet_1) | **GET** /organisations/{id}/payments/methods/default | 
[**organisationsIdPaymentsMethodsDefaultPut_1**](PaymentsApi.md#organisationsIdPaymentsMethodsDefaultPut_1) | **PUT** /organisations/{id}/payments/methods/default | 
[**organisationsIdPaymentsMethodsGet_1**](PaymentsApi.md#organisationsIdPaymentsMethodsGet_1) | **GET** /organisations/{id}/payments/methods | 
[**organisationsIdPaymentsMethodsMIdDelete_1**](PaymentsApi.md#organisationsIdPaymentsMethodsMIdDelete_1) | **DELETE** /organisations/{id}/payments/methods/{mId} | 
[**organisationsIdPaymentsMethodsPost_1**](PaymentsApi.md#organisationsIdPaymentsMethodsPost_1) | **POST** /organisations/{id}/payments/methods | 
[**organisationsIdPaymentsMonthlyinvoiceGet_1**](PaymentsApi.md#organisationsIdPaymentsMonthlyinvoiceGet_1) | **GET** /organisations/{id}/payments/monthlyinvoice | 
[**organisationsIdPaymentsMonthlyinvoiceMaxcreditPut_1**](PaymentsApi.md#organisationsIdPaymentsMonthlyinvoiceMaxcreditPut_1) | **PUT** /organisations/{id}/payments/monthlyinvoice/maxcredit | 
[**organisationsIdPaymentsRecurringGet_1**](PaymentsApi.md#organisationsIdPaymentsRecurringGet_1) | **GET** /organisations/{id}/payments/recurring | 
[**paymentsAssetsPayButtonTokenButtonPngGet_0**](PaymentsApi.md#paymentsAssetsPayButtonTokenButtonPngGet_0) | **GET** /payments/assets/pay_button/{token}/button.png | 
[**paymentsBidEndStripePost_0**](PaymentsApi.md#paymentsBidEndStripePost_0) | **POST** /payments/{bid}/end/stripe | 
[**postOrganisationsIdPaymentsBillings_1**](PaymentsApi.md#postOrganisationsIdPaymentsBillings_1) | **POST** /organisations/{id}/payments/billings | 
[**postSelfPaymentsBillings_0**](PaymentsApi.md#postSelfPaymentsBillings_0) | **POST** /self/payments/billings | 
[**postSelfPaymentsMethods_0**](PaymentsApi.md#postSelfPaymentsMethods_0) | **POST** /self/payments/methods | 
[**putOrganisationsIdPaymentsBillingsBid_1**](PaymentsApi.md#putOrganisationsIdPaymentsBillingsBid_1) | **PUT** /organisations/{id}/payments/billings/{bid} | 
[**putSelfPaymentsBillingsBid_0**](PaymentsApi.md#putSelfPaymentsBillingsBid_0) | **PUT** /self/payments/billings/{bid} | 
[**selfPaymentsMethodsDefaultGet_0**](PaymentsApi.md#selfPaymentsMethodsDefaultGet_0) | **GET** /self/payments/methods/default | 
[**selfPaymentsMethodsDefaultPut_0**](PaymentsApi.md#selfPaymentsMethodsDefaultPut_0) | **PUT** /self/payments/methods/default | 
[**selfPaymentsMonthlyinvoiceGet_0**](PaymentsApi.md#selfPaymentsMonthlyinvoiceGet_0) | **GET** /self/payments/monthlyinvoice | 
[**selfPaymentsMonthlyinvoiceMaxcreditPut_0**](PaymentsApi.md#selfPaymentsMonthlyinvoiceMaxcreditPut_0) | **PUT** /self/payments/monthlyinvoice/maxcredit | 
[**selfPaymentsRecurringGet_0**](PaymentsApi.md#selfPaymentsRecurringGet_0) | **GET** /self/payments/recurring | 
[**selfPaymentsTokensStripeGet_0**](PaymentsApi.md#selfPaymentsTokensStripeGet_0) | **GET** /self/payments/tokens/stripe | 



## deleteOrganisationsIdPaymentsBillingsBid_1

> deleteOrganisationsIdPaymentsBillingsBid_1(id, bid)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.PaymentsApi();
let id = "id_example"; // String | 
let bid = "bid_example"; // String | 
apiInstance.deleteOrganisationsIdPaymentsBillingsBid_1(id, bid, (error, data, response) => {
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
 **id** | **String**|  | 
 **bid** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteOrganisationsIdPaymentsRecurring_1

> deleteOrganisationsIdPaymentsRecurring_1(id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.PaymentsApi();
let id = "id_example"; // String | 
apiInstance.deleteOrganisationsIdPaymentsRecurring_1(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteSelfPaymentsBillingsBid_0

> deleteSelfPaymentsBillingsBid_0(bid)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.PaymentsApi();
let bid = "bid_example"; // String | 
apiInstance.deleteSelfPaymentsBillingsBid_0(bid, (error, data, response) => {
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
 **bid** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteSelfPaymentsMethodsMId_0

> deleteSelfPaymentsMethodsMId_0(mId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.PaymentsApi();
let mId = "mId_example"; // String | 
apiInstance.deleteSelfPaymentsMethodsMId_0(mId, (error, data, response) => {
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
 **mId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteSelfPaymentsRecurring_0

> deleteSelfPaymentsRecurring_0()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.PaymentsApi();
apiInstance.deleteSelfPaymentsRecurring_0((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getOrganisationsIdPaymentsBillingsBidPdf_1

> getOrganisationsIdPaymentsBillingsBidPdf_1(id, bid, opts)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.PaymentsApi();
let id = "id_example"; // String | 
let bid = "bid_example"; // String | 
let opts = {
  'token': "token_example" // String | 
};
apiInstance.getOrganisationsIdPaymentsBillingsBidPdf_1(id, bid, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **bid** | **String**|  | 
 **token** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getOrganisationsIdPaymentsBillingsBid_1

> getOrganisationsIdPaymentsBillingsBid_1(id, bid)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.PaymentsApi();
let id = "id_example"; // String | 
let bid = "bid_example"; // String | 
apiInstance.getOrganisationsIdPaymentsBillingsBid_1(id, bid, (error, data, response) => {
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
 **id** | **String**|  | 
 **bid** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getOrganisationsIdPaymentsBillings_1

> getOrganisationsIdPaymentsBillings_1(id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.PaymentsApi();
let id = "id_example"; // String | 
apiInstance.getOrganisationsIdPaymentsBillings_1(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getOrganisationsIdPaymentsFullPricePrice_1

> getOrganisationsIdPaymentsFullPricePrice_1(id, price)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.PaymentsApi();
let id = "id_example"; // String | 
let price = "price_example"; // String | 
apiInstance.getOrganisationsIdPaymentsFullPricePrice_1(id, price, (error, data, response) => {
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
 **id** | **String**|  | 
 **price** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getPaymentsCouponsName_0

> getPaymentsCouponsName_0(name)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.PaymentsApi();
let name = "name_example"; // String | 
apiInstance.getPaymentsCouponsName_0(name, (error, data, response) => {
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
 **name** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getPaymentsProviders_0

> [PaymentProvider] getPaymentsProviders_0()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.PaymentsApi();
apiInstance.getPaymentsProviders_0((error, data, response) => {
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

[**[PaymentProvider]**](PaymentProvider.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPaymentsTokensStripe_0

> getPaymentsTokensStripe_0()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.PaymentsApi();
apiInstance.getPaymentsTokensStripe_0((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getSelfPaymentsBillingsBidPdf_0

> getSelfPaymentsBillingsBidPdf_0(bid, opts)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.PaymentsApi();
let bid = "bid_example"; // String | 
let opts = {
  'token': "token_example" // String | 
};
apiInstance.getSelfPaymentsBillingsBidPdf_0(bid, opts, (error, data, response) => {
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
 **bid** | **String**|  | 
 **token** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getSelfPaymentsBillingsBid_0

> getSelfPaymentsBillingsBid_0(bid)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.PaymentsApi();
let bid = "bid_example"; // String | 
apiInstance.getSelfPaymentsBillingsBid_0(bid, (error, data, response) => {
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
 **bid** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getSelfPaymentsBillings_0

> getSelfPaymentsBillings_0()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.PaymentsApi();
apiInstance.getSelfPaymentsBillings_0((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getSelfPaymentsFullpricePrice_0

> getSelfPaymentsFullpricePrice_0(price)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.PaymentsApi();
let price = "price_example"; // String | 
apiInstance.getSelfPaymentsFullpricePrice_0(price, (error, data, response) => {
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
 **price** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getSelfPaymentsMethods_0

> getSelfPaymentsMethods_0()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.PaymentsApi();
apiInstance.getSelfPaymentsMethods_0((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## organisationsIdPaymentsBillingsUnpaidGet_1

> organisationsIdPaymentsBillingsUnpaidGet_1(id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.PaymentsApi();
let id = "id_example"; // String | 
apiInstance.organisationsIdPaymentsBillingsUnpaidGet_1(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## organisationsIdPaymentsMethodsDefaultGet_1

> organisationsIdPaymentsMethodsDefaultGet_1(id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.PaymentsApi();
let id = "id_example"; // String | 
apiInstance.organisationsIdPaymentsMethodsDefaultGet_1(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## organisationsIdPaymentsMethodsDefaultPut_1

> organisationsIdPaymentsMethodsDefaultPut_1(id, paymentData)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.PaymentsApi();
let id = "id_example"; // String | 
let paymentData = new CleverCloudApi.PaymentData(); // PaymentData | 
apiInstance.organisationsIdPaymentsMethodsDefaultPut_1(id, paymentData, (error, data, response) => {
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
 **id** | **String**|  | 
 **paymentData** | [**PaymentData**](PaymentData.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## organisationsIdPaymentsMethodsGet_1

> organisationsIdPaymentsMethodsGet_1(id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.PaymentsApi();
let id = "id_example"; // String | 
apiInstance.organisationsIdPaymentsMethodsGet_1(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## organisationsIdPaymentsMethodsMIdDelete_1

> organisationsIdPaymentsMethodsMIdDelete_1(mId, id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.PaymentsApi();
let mId = "mId_example"; // String | 
let id = "id_example"; // String | 
apiInstance.organisationsIdPaymentsMethodsMIdDelete_1(mId, id, (error, data, response) => {
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
 **mId** | **String**|  | 
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## organisationsIdPaymentsMethodsPost_1

> organisationsIdPaymentsMethodsPost_1(id, body)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.PaymentsApi();
let id = "id_example"; // String | 
let body = new CleverCloudApi.Body(); // Body | 
apiInstance.organisationsIdPaymentsMethodsPost_1(id, body, (error, data, response) => {
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
 **id** | **String**|  | 
 **body** | [**Body**](Body.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## organisationsIdPaymentsMonthlyinvoiceGet_1

> organisationsIdPaymentsMonthlyinvoiceGet_1(id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.PaymentsApi();
let id = "id_example"; // String | 
apiInstance.organisationsIdPaymentsMonthlyinvoiceGet_1(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## organisationsIdPaymentsMonthlyinvoiceMaxcreditPut_1

> organisationsIdPaymentsMonthlyinvoiceMaxcreditPut_1(id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.PaymentsApi();
let id = "id_example"; // String | 
apiInstance.organisationsIdPaymentsMonthlyinvoiceMaxcreditPut_1(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## organisationsIdPaymentsRecurringGet_1

> organisationsIdPaymentsRecurringGet_1(id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.PaymentsApi();
let id = "id_example"; // String | 
apiInstance.organisationsIdPaymentsRecurringGet_1(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## paymentsAssetsPayButtonTokenButtonPngGet_0

> paymentsAssetsPayButtonTokenButtonPngGet_0(token)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.PaymentsApi();
let token = "token_example"; // String | 
apiInstance.paymentsAssetsPayButtonTokenButtonPngGet_0(token, (error, data, response) => {
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
 **token** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## paymentsBidEndStripePost_0

> paymentsBidEndStripePost_0(bid)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.PaymentsApi();
let bid = "bid_example"; // String | 
apiInstance.paymentsBidEndStripePost_0(bid, (error, data, response) => {
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
 **bid** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## postOrganisationsIdPaymentsBillings_1

> postOrganisationsIdPaymentsBillings_1(id)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.PaymentsApi();
let id = "id_example"; // String | 
apiInstance.postOrganisationsIdPaymentsBillings_1(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## postSelfPaymentsBillings_0

> postSelfPaymentsBillings_0()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.PaymentsApi();
apiInstance.postSelfPaymentsBillings_0((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## postSelfPaymentsMethods_0

> postSelfPaymentsMethods_0()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.PaymentsApi();
apiInstance.postSelfPaymentsMethods_0((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## putOrganisationsIdPaymentsBillingsBid_1

> putOrganisationsIdPaymentsBillingsBid_1(id, bid)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.PaymentsApi();
let id = "id_example"; // String | 
let bid = "bid_example"; // String | 
apiInstance.putOrganisationsIdPaymentsBillingsBid_1(id, bid, (error, data, response) => {
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
 **id** | **String**|  | 
 **bid** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## putSelfPaymentsBillingsBid_0

> putSelfPaymentsBillingsBid_0(bid)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.PaymentsApi();
let bid = "bid_example"; // String | 
apiInstance.putSelfPaymentsBillingsBid_0(bid, (error, data, response) => {
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
 **bid** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## selfPaymentsMethodsDefaultGet_0

> selfPaymentsMethodsDefaultGet_0()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.PaymentsApi();
apiInstance.selfPaymentsMethodsDefaultGet_0((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## selfPaymentsMethodsDefaultPut_0

> selfPaymentsMethodsDefaultPut_0()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.PaymentsApi();
apiInstance.selfPaymentsMethodsDefaultPut_0((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## selfPaymentsMonthlyinvoiceGet_0

> selfPaymentsMonthlyinvoiceGet_0()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.PaymentsApi();
apiInstance.selfPaymentsMonthlyinvoiceGet_0((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## selfPaymentsMonthlyinvoiceMaxcreditPut_0

> selfPaymentsMonthlyinvoiceMaxcreditPut_0()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.PaymentsApi();
apiInstance.selfPaymentsMonthlyinvoiceMaxcreditPut_0((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## selfPaymentsRecurringGet_0

> selfPaymentsRecurringGet_0()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.PaymentsApi();
apiInstance.selfPaymentsRecurringGet_0((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## selfPaymentsTokensStripeGet_0

> selfPaymentsTokensStripeGet_0()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.PaymentsApi();
apiInstance.selfPaymentsTokensStripeGet_0((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

