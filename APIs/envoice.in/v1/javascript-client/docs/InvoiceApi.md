# ApiV100.InvoiceApi

All URIs are relative to *https://www.envoice.in*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiInvoiceAllcategoriesGet**](InvoiceApi.md#apiInvoiceAllcategoriesGet) | **GET** /api/invoice/allcategories | Return all invoice categories for the account
[**apiInvoiceDeletecategoryPost**](InvoiceApi.md#apiInvoiceDeletecategoryPost) | **POST** /api/invoice/deletecategory | Delete an existing invoice category
[**apiInvoiceNewcategoryPost**](InvoiceApi.md#apiInvoiceNewcategoryPost) | **POST** /api/invoice/newcategory | Create an invoice category
[**apiInvoiceUpdatecategoryPost**](InvoiceApi.md#apiInvoiceUpdatecategoryPost) | **POST** /api/invoice/updatecategory | Update an existing invoice category
[**invoiceApiAll**](InvoiceApi.md#invoiceApiAll) | **GET** /api/invoice/all | Return all invoices for the account
[**invoiceApiChangeStatus**](InvoiceApi.md#invoiceApiChangeStatus) | **POST** /api/invoice/changestatus | Change invoice status
[**invoiceApiDelete**](InvoiceApi.md#invoiceApiDelete) | **POST** /api/invoice/delete | Delete an existing invoice
[**invoiceApiDetails**](InvoiceApi.md#invoiceApiDetails) | **GET** /api/invoice/details | Return invoice data
[**invoiceApiNew**](InvoiceApi.md#invoiceApiNew) | **POST** /api/invoice/new | Create an invoice
[**invoiceApiPdf**](InvoiceApi.md#invoiceApiPdf) | **GET** /api/invoice/pdf | Return the PDF for the invoice
[**invoiceApiSendToAccountant**](InvoiceApi.md#invoiceApiSendToAccountant) | **POST** /api/invoice/sendtoaccountant | Send the provided invoice to the accountant
[**invoiceApiSendToClient**](InvoiceApi.md#invoiceApiSendToClient) | **POST** /api/invoice/sendtoclient | Send the provided invoice to the client
[**invoiceApiStatus**](InvoiceApi.md#invoiceApiStatus) | **GET** /api/invoice/status | Retrieve the status of the invoice
[**invoiceApiUpdate**](InvoiceApi.md#invoiceApiUpdate) | **POST** /api/invoice/update | Update an existing invoice
[**invoiceApiUri**](InvoiceApi.md#invoiceApiUri) | **GET** /api/invoice/uri | Return the unique url to the client&#39;s invoice



## apiInvoiceAllcategoriesGet

> ListResultInvoiceCategoryApiModel apiInvoiceAllcategoriesGet(xAuthKey, xAuthSecret, opts)

Return all invoice categories for the account

### Example

```javascript
import ApiV100 from 'api_v1_0_0';

let apiInstance = new ApiV100.InvoiceApi();
let xAuthKey = "'[authentication key]'"; // String | 
let xAuthSecret = "'[authentication secret]'"; // String | 
let opts = {
  'query': "query_example" // String | 
};
apiInstance.apiInvoiceAllcategoriesGet(xAuthKey, xAuthSecret, opts, (error, data, response) => {
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
 **xAuthKey** | **String**|  | [default to &#39;[authentication key]&#39;]
 **xAuthSecret** | **String**|  | [default to &#39;[authentication secret]&#39;]
 **query** | **String**|  | [optional] 

### Return type

[**ListResultInvoiceCategoryApiModel**](ListResultInvoiceCategoryApiModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/html, text/json, text/xml


## apiInvoiceDeletecategoryPost

> Number apiInvoiceDeletecategoryPost(xAuthKey, xAuthSecret, invoiceCategoryDeleteApiModel)

Delete an existing invoice category

### Example

```javascript
import ApiV100 from 'api_v1_0_0';

let apiInstance = new ApiV100.InvoiceApi();
let xAuthKey = "'[authentication key]'"; // String | 
let xAuthSecret = "'[authentication secret]'"; // String | 
let invoiceCategoryDeleteApiModel = new ApiV100.InvoiceCategoryDeleteApiModel(); // InvoiceCategoryDeleteApiModel | 
apiInstance.apiInvoiceDeletecategoryPost(xAuthKey, xAuthSecret, invoiceCategoryDeleteApiModel, (error, data, response) => {
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
 **xAuthKey** | **String**|  | [default to &#39;[authentication key]&#39;]
 **xAuthSecret** | **String**|  | [default to &#39;[authentication secret]&#39;]
 **invoiceCategoryDeleteApiModel** | [**InvoiceCategoryDeleteApiModel**](InvoiceCategoryDeleteApiModel.md)|  | 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/html, text/json, text/xml
- **Accept**: application/json, application/xml, text/html, text/json, text/xml


## apiInvoiceNewcategoryPost

> InvoiceCategoryApiModel apiInvoiceNewcategoryPost(xAuthKey, xAuthSecret, invoiceCategoryCreateApiModel)

Create an invoice category

### Example

```javascript
import ApiV100 from 'api_v1_0_0';

let apiInstance = new ApiV100.InvoiceApi();
let xAuthKey = "'[authentication key]'"; // String | 
let xAuthSecret = "'[authentication secret]'"; // String | 
let invoiceCategoryCreateApiModel = new ApiV100.InvoiceCategoryCreateApiModel(); // InvoiceCategoryCreateApiModel | 
apiInstance.apiInvoiceNewcategoryPost(xAuthKey, xAuthSecret, invoiceCategoryCreateApiModel, (error, data, response) => {
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
 **xAuthKey** | **String**|  | [default to &#39;[authentication key]&#39;]
 **xAuthSecret** | **String**|  | [default to &#39;[authentication secret]&#39;]
 **invoiceCategoryCreateApiModel** | [**InvoiceCategoryCreateApiModel**](InvoiceCategoryCreateApiModel.md)|  | 

### Return type

[**InvoiceCategoryApiModel**](InvoiceCategoryApiModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/html, text/json, text/xml
- **Accept**: application/json, application/xml, text/html, text/json, text/xml


## apiInvoiceUpdatecategoryPost

> InvoiceCategoryApiModel apiInvoiceUpdatecategoryPost(xAuthKey, xAuthSecret, invoiceCategoryUpdateApiModel)

Update an existing invoice category

### Example

```javascript
import ApiV100 from 'api_v1_0_0';

let apiInstance = new ApiV100.InvoiceApi();
let xAuthKey = "'[authentication key]'"; // String | 
let xAuthSecret = "'[authentication secret]'"; // String | 
let invoiceCategoryUpdateApiModel = new ApiV100.InvoiceCategoryUpdateApiModel(); // InvoiceCategoryUpdateApiModel | 
apiInstance.apiInvoiceUpdatecategoryPost(xAuthKey, xAuthSecret, invoiceCategoryUpdateApiModel, (error, data, response) => {
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
 **xAuthKey** | **String**|  | [default to &#39;[authentication key]&#39;]
 **xAuthSecret** | **String**|  | [default to &#39;[authentication secret]&#39;]
 **invoiceCategoryUpdateApiModel** | [**InvoiceCategoryUpdateApiModel**](InvoiceCategoryUpdateApiModel.md)|  | 

### Return type

[**InvoiceCategoryApiModel**](InvoiceCategoryApiModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/html, text/json, text/xml
- **Accept**: application/json, application/xml, text/html, text/json, text/xml


## invoiceApiAll

> ListResultInvoiceDetailsApiModel invoiceApiAll(xAuthKey, xAuthSecret, opts)

Return all invoices for the account

### Example

```javascript
import ApiV100 from 'api_v1_0_0';

let apiInstance = new ApiV100.InvoiceApi();
let xAuthKey = "'[authentication key]'"; // String | 
let xAuthSecret = "'[authentication secret]'"; // String | 
let opts = {
  'queryOptionsPage': 56, // Number | 
  'queryOptionsPageSize': 56 // Number | 
};
apiInstance.invoiceApiAll(xAuthKey, xAuthSecret, opts, (error, data, response) => {
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
 **xAuthKey** | **String**|  | [default to &#39;[authentication key]&#39;]
 **xAuthSecret** | **String**|  | [default to &#39;[authentication secret]&#39;]
 **queryOptionsPage** | **Number**|  | [optional] 
 **queryOptionsPageSize** | **Number**|  | [optional] 

### Return type

[**ListResultInvoiceDetailsApiModel**](ListResultInvoiceDetailsApiModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/html, text/json, text/xml


## invoiceApiChangeStatus

> Boolean invoiceApiChangeStatus(xAuthKey, xAuthSecret, changeStatusApiModel)

Change invoice status

### Example

```javascript
import ApiV100 from 'api_v1_0_0';

let apiInstance = new ApiV100.InvoiceApi();
let xAuthKey = "'[authentication key]'"; // String | 
let xAuthSecret = "'[authentication secret]'"; // String | 
let changeStatusApiModel = new ApiV100.ChangeStatusApiModel(); // ChangeStatusApiModel | 
apiInstance.invoiceApiChangeStatus(xAuthKey, xAuthSecret, changeStatusApiModel, (error, data, response) => {
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
 **xAuthKey** | **String**|  | [default to &#39;[authentication key]&#39;]
 **xAuthSecret** | **String**|  | [default to &#39;[authentication secret]&#39;]
 **changeStatusApiModel** | [**ChangeStatusApiModel**](ChangeStatusApiModel.md)|  | 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/html, text/json, text/xml
- **Accept**: application/json, application/xml, text/html, text/json, text/xml


## invoiceApiDelete

> Number invoiceApiDelete(xAuthKey, xAuthSecret, invoiceDeleteApiModel)

Delete an existing invoice

### Example

```javascript
import ApiV100 from 'api_v1_0_0';

let apiInstance = new ApiV100.InvoiceApi();
let xAuthKey = "'[authentication key]'"; // String | 
let xAuthSecret = "'[authentication secret]'"; // String | 
let invoiceDeleteApiModel = new ApiV100.InvoiceDeleteApiModel(); // InvoiceDeleteApiModel | 
apiInstance.invoiceApiDelete(xAuthKey, xAuthSecret, invoiceDeleteApiModel, (error, data, response) => {
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
 **xAuthKey** | **String**|  | [default to &#39;[authentication key]&#39;]
 **xAuthSecret** | **String**|  | [default to &#39;[authentication secret]&#39;]
 **invoiceDeleteApiModel** | [**InvoiceDeleteApiModel**](InvoiceDeleteApiModel.md)|  | 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/html, text/json, text/xml
- **Accept**: application/json, application/xml, text/html, text/json, text/xml


## invoiceApiDetails

> InvoiceFullDetailsApiModel invoiceApiDetails(id, xAuthKey, xAuthSecret)

Return invoice data

### Example

```javascript
import ApiV100 from 'api_v1_0_0';

let apiInstance = new ApiV100.InvoiceApi();
let id = 56; // Number | 
let xAuthKey = "'[authentication key]'"; // String | 
let xAuthSecret = "'[authentication secret]'"; // String | 
apiInstance.invoiceApiDetails(id, xAuthKey, xAuthSecret, (error, data, response) => {
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
 **id** | **Number**|  | 
 **xAuthKey** | **String**|  | [default to &#39;[authentication key]&#39;]
 **xAuthSecret** | **String**|  | [default to &#39;[authentication secret]&#39;]

### Return type

[**InvoiceFullDetailsApiModel**](InvoiceFullDetailsApiModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/html, text/json, text/xml


## invoiceApiNew

> InvoiceFullDetailsApiModel invoiceApiNew(xAuthKey, xAuthSecret, invoiceCreateApiModel)

Create an invoice

### Example

```javascript
import ApiV100 from 'api_v1_0_0';

let apiInstance = new ApiV100.InvoiceApi();
let xAuthKey = "'[authentication key]'"; // String | 
let xAuthSecret = "'[authentication secret]'"; // String | 
let invoiceCreateApiModel = new ApiV100.InvoiceCreateApiModel(); // InvoiceCreateApiModel | 
apiInstance.invoiceApiNew(xAuthKey, xAuthSecret, invoiceCreateApiModel, (error, data, response) => {
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
 **xAuthKey** | **String**|  | [default to &#39;[authentication key]&#39;]
 **xAuthSecret** | **String**|  | [default to &#39;[authentication secret]&#39;]
 **invoiceCreateApiModel** | [**InvoiceCreateApiModel**](InvoiceCreateApiModel.md)|  | 

### Return type

[**InvoiceFullDetailsApiModel**](InvoiceFullDetailsApiModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/html, text/json, text/xml
- **Accept**: application/json, application/xml, text/html, text/json, text/xml


## invoiceApiPdf

> InvoiceUriApiModel invoiceApiPdf(id, xAuthKey, xAuthSecret, opts)

Return the PDF for the invoice

### Example

```javascript
import ApiV100 from 'api_v1_0_0';

let apiInstance = new ApiV100.InvoiceApi();
let id = 56; // Number | 
let xAuthKey = "'[authentication key]'"; // String | 
let xAuthSecret = "'[authentication secret]'"; // String | 
let opts = {
  'signedVersion': true // Boolean | 
};
apiInstance.invoiceApiPdf(id, xAuthKey, xAuthSecret, opts, (error, data, response) => {
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
 **id** | **Number**|  | 
 **xAuthKey** | **String**|  | [default to &#39;[authentication key]&#39;]
 **xAuthSecret** | **String**|  | [default to &#39;[authentication secret]&#39;]
 **signedVersion** | **Boolean**|  | [optional] 

### Return type

[**InvoiceUriApiModel**](InvoiceUriApiModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/html, text/json, text/xml


## invoiceApiSendToAccountant

> Number invoiceApiSendToAccountant(xAuthKey, xAuthSecret, sendInvoiceToAccountantApiModel)

Send the provided invoice to the accountant

### Example

```javascript
import ApiV100 from 'api_v1_0_0';

let apiInstance = new ApiV100.InvoiceApi();
let xAuthKey = "'[authentication key]'"; // String | 
let xAuthSecret = "'[authentication secret]'"; // String | 
let sendInvoiceToAccountantApiModel = new ApiV100.SendInvoiceToAccountantApiModel(); // SendInvoiceToAccountantApiModel | 
apiInstance.invoiceApiSendToAccountant(xAuthKey, xAuthSecret, sendInvoiceToAccountantApiModel, (error, data, response) => {
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
 **xAuthKey** | **String**|  | [default to &#39;[authentication key]&#39;]
 **xAuthSecret** | **String**|  | [default to &#39;[authentication secret]&#39;]
 **sendInvoiceToAccountantApiModel** | [**SendInvoiceToAccountantApiModel**](SendInvoiceToAccountantApiModel.md)|  | 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/html, text/json, text/xml
- **Accept**: application/json, application/xml, text/html, text/json, text/xml


## invoiceApiSendToClient

> Number invoiceApiSendToClient(xAuthKey, xAuthSecret, sendInvoiceToClientApiModel)

Send the provided invoice to the client

### Example

```javascript
import ApiV100 from 'api_v1_0_0';

let apiInstance = new ApiV100.InvoiceApi();
let xAuthKey = "'[authentication key]'"; // String | 
let xAuthSecret = "'[authentication secret]'"; // String | 
let sendInvoiceToClientApiModel = new ApiV100.SendInvoiceToClientApiModel(); // SendInvoiceToClientApiModel | 
apiInstance.invoiceApiSendToClient(xAuthKey, xAuthSecret, sendInvoiceToClientApiModel, (error, data, response) => {
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
 **xAuthKey** | **String**|  | [default to &#39;[authentication key]&#39;]
 **xAuthSecret** | **String**|  | [default to &#39;[authentication secret]&#39;]
 **sendInvoiceToClientApiModel** | [**SendInvoiceToClientApiModel**](SendInvoiceToClientApiModel.md)|  | 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/html, text/json, text/xml
- **Accept**: application/json, application/xml, text/html, text/json, text/xml


## invoiceApiStatus

> String invoiceApiStatus(id, xAuthKey, xAuthSecret)

Retrieve the status of the invoice

### Example

```javascript
import ApiV100 from 'api_v1_0_0';

let apiInstance = new ApiV100.InvoiceApi();
let id = 56; // Number | 
let xAuthKey = "'[authentication key]'"; // String | 
let xAuthSecret = "'[authentication secret]'"; // String | 
apiInstance.invoiceApiStatus(id, xAuthKey, xAuthSecret, (error, data, response) => {
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
 **id** | **Number**|  | 
 **xAuthKey** | **String**|  | [default to &#39;[authentication key]&#39;]
 **xAuthSecret** | **String**|  | [default to &#39;[authentication secret]&#39;]

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/html, text/json, text/xml


## invoiceApiUpdate

> InvoiceFullDetailsApiModel invoiceApiUpdate(xAuthKey, xAuthSecret, invoiceUpdateApiModel)

Update an existing invoice

### Example

```javascript
import ApiV100 from 'api_v1_0_0';

let apiInstance = new ApiV100.InvoiceApi();
let xAuthKey = "'[authentication key]'"; // String | 
let xAuthSecret = "'[authentication secret]'"; // String | 
let invoiceUpdateApiModel = new ApiV100.InvoiceUpdateApiModel(); // InvoiceUpdateApiModel | 
apiInstance.invoiceApiUpdate(xAuthKey, xAuthSecret, invoiceUpdateApiModel, (error, data, response) => {
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
 **xAuthKey** | **String**|  | [default to &#39;[authentication key]&#39;]
 **xAuthSecret** | **String**|  | [default to &#39;[authentication secret]&#39;]
 **invoiceUpdateApiModel** | [**InvoiceUpdateApiModel**](InvoiceUpdateApiModel.md)|  | 

### Return type

[**InvoiceFullDetailsApiModel**](InvoiceFullDetailsApiModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/html, text/json, text/xml
- **Accept**: application/json, application/xml, text/html, text/json, text/xml


## invoiceApiUri

> InvoiceUriApiModel invoiceApiUri(id, xAuthKey, xAuthSecret)

Return the unique url to the client&#39;s invoice

### Example

```javascript
import ApiV100 from 'api_v1_0_0';

let apiInstance = new ApiV100.InvoiceApi();
let id = 56; // Number | 
let xAuthKey = "'[authentication key]'"; // String | 
let xAuthSecret = "'[authentication secret]'"; // String | 
apiInstance.invoiceApiUri(id, xAuthKey, xAuthSecret, (error, data, response) => {
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
 **id** | **Number**|  | 
 **xAuthKey** | **String**|  | [default to &#39;[authentication key]&#39;]
 **xAuthSecret** | **String**|  | [default to &#39;[authentication secret]&#39;]

### Return type

[**InvoiceUriApiModel**](InvoiceUriApiModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/html, text/json, text/xml

