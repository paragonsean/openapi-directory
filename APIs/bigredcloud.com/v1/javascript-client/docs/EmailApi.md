# BigRedCloudApi.EmailApi

All URIs are relative to *https://app.bigredcloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**emailSendEmailStatement**](EmailApi.md#emailSendEmailStatement) | **POST** /v1/email/sendEmailStatement | Sends a Statement email.  If \&quot;toAddress\&quot; is not empty then email will be sent to this address. Otherwise email will be sent to Statement Customer&#39;s address.
[**emailSendQuote**](EmailApi.md#emailSendQuote) | **POST** /v1/email/sendQuote | Sends a Quote email.  If \&quot;toAddress\&quot; is not empty then email will be sent to this address. Otherwise email will be sent to Statement Customer&#39;s address.
[**emailSendSalesInvoice**](EmailApi.md#emailSendSalesInvoice) | **POST** /v1/email/sendSalesInvoice | Sends a Sales Invoice email.  If \&quot;toAddress\&quot; is not empty then email will be sent to this address. Otherwise email will be sent to Sales Invoice Customer&#39;s address.



## emailSendEmailStatement

> Object emailSendEmailStatement(emailStatementDto)

Sends a Statement email.  If \&quot;toAddress\&quot; is not empty then email will be sent to this address. Otherwise email will be sent to Statement Customer&#39;s address.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.EmailApi();
let emailStatementDto = new BigRedCloudApi.EmailStatementDto(); // EmailStatementDto | 
apiInstance.emailSendEmailStatement(emailStatementDto, (error, data, response) => {
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
 **emailStatementDto** | [**EmailStatementDto**](EmailStatementDto.md)|  | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## emailSendQuote

> Object emailSendQuote(emailQuoteDto)

Sends a Quote email.  If \&quot;toAddress\&quot; is not empty then email will be sent to this address. Otherwise email will be sent to Statement Customer&#39;s address.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.EmailApi();
let emailQuoteDto = new BigRedCloudApi.EmailQuoteDto(); // EmailQuoteDto | 
apiInstance.emailSendQuote(emailQuoteDto, (error, data, response) => {
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
 **emailQuoteDto** | [**EmailQuoteDto**](EmailQuoteDto.md)|  | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## emailSendSalesInvoice

> Object emailSendSalesInvoice(salesInvoiceEmailInfoDto)

Sends a Sales Invoice email.  If \&quot;toAddress\&quot; is not empty then email will be sent to this address. Otherwise email will be sent to Sales Invoice Customer&#39;s address.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.EmailApi();
let salesInvoiceEmailInfoDto = new BigRedCloudApi.SalesInvoiceEmailInfoDto(); // SalesInvoiceEmailInfoDto | 
apiInstance.emailSendSalesInvoice(salesInvoiceEmailInfoDto, (error, data, response) => {
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
 **salesInvoiceEmailInfoDto** | [**SalesInvoiceEmailInfoDto**](SalesInvoiceEmailInfoDto.md)|  | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

