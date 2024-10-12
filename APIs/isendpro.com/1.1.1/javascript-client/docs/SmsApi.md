# ApiISendPro.SmsApi

All URIs are relative to *https://apirest.isendpro.com/cgi-bin*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sendSms**](SmsApi.md#sendSms) | **POST** /sms | Envoyer un sms
[**sendSmsMulti**](SmsApi.md#sendSmsMulti) | **POST** /smsmulti | Envoyer des SMS



## sendSms

> SMSReponse sendSms(smsUniqueRequest)

Envoyer un sms

Envoi un sms vers un unique destinataire

### Example

```javascript
import ApiISendPro from 'api_i_send_pro';

let apiInstance = new ApiISendPro.SmsApi();
let smsUniqueRequest = new ApiISendPro.SmsUniqueRequest(); // SmsUniqueRequest | sms request
apiInstance.sendSms(smsUniqueRequest, (error, data, response) => {
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
 **smsUniqueRequest** | [**SmsUniqueRequest**](SmsUniqueRequest.md)| sms request | 

### Return type

[**SMSReponse**](SMSReponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, etat


## sendSmsMulti

> SMSReponse sendSmsMulti(sMSRequest)

Envoyer des SMS

Envoi de SMS vers 1 ou plusieurs destinataires 

### Example

```javascript
import ApiISendPro from 'api_i_send_pro';

let apiInstance = new ApiISendPro.SmsApi();
let sMSRequest = new ApiISendPro.SMSRequest(); // SMSRequest | sms request
apiInstance.sendSmsMulti(sMSRequest, (error, data, response) => {
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
 **sMSRequest** | [**SMSRequest**](SMSRequest.md)| sms request | 

### Return type

[**SMSReponse**](SMSReponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, etat

