# DigiLockerIssuerApis.APIsApi

All URIs are relative to *http://Your API URL*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pullDoc**](APIsApi.md#pullDoc) | **POST** /Your Pull DOC Request API Path | Pull Doc Request API.
[**pullUri**](APIsApi.md#pullUri) | **POST** /Your Pull URI Request API Path | Pull URI Request API .



## pullDoc

> PullDocResponse pullDoc(opts)

Pull Doc Request API.

The Pull Doc Request API has to be implemented by the issuers and will be consumed by Digital Locker system. This API will be invoked when the resident clicks on the URI displayed in the Issued documents section of DigLocker. The issuer API will by sending the certificate data. The certificate data should be sent in one of the two formats depending on the request send by Digital Locker:|- a. PDF document format b. XML format for machine readable metadata

### Example

```javascript
import DigiLockerIssuerApis from 'digi_locker_issuer_apis';

let apiInstance = new DigiLockerIssuerApis.APIsApi();
let opts = {
  'contentType': "contentType_example", // String | application/xml
  'xDigilockerHmac': "xDigilockerHmac_example", // String | This is used for authentication and to verify the integrity of the request. DigiLocker calculates the hash message authentication code (hmac) of the HTTP request body using SHA256 hashing algorithm and the API Key provided by the issuer as the hashing key. The API Key is specified by the issuer while configuring the Pull Doc API in DigiLocker Partner Portal. The resulting hmac is converted to Base64 format and sent in this parameter. It is strongly recommended that the issuer API calculates the hmac of the HTTP request body, convert it to Base64 and match it with this parameter to ensure authenticity of the request.
  'pullDocRequest': new DigiLockerIssuerApis.PullDocRequest() // PullDocRequest | 
};
apiInstance.pullDoc(opts, (error, data, response) => {
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
 **contentType** | **String**| application/xml | [optional] 
 **xDigilockerHmac** | **String**| This is used for authentication and to verify the integrity of the request. DigiLocker calculates the hash message authentication code (hmac) of the HTTP request body using SHA256 hashing algorithm and the API Key provided by the issuer as the hashing key. The API Key is specified by the issuer while configuring the Pull Doc API in DigiLocker Partner Portal. The resulting hmac is converted to Base64 format and sent in this parameter. It is strongly recommended that the issuer API calculates the hmac of the HTTP request body, convert it to Base64 and match it with this parameter to ensure authenticity of the request. | [optional] 
 **pullDocRequest** | [**PullDocRequest**](PullDocRequest.md)|  | [optional] 

### Return type

[**PullDocResponse**](PullDocResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/xml
- **Accept**: application/xml


## pullUri

> PullURIResponse pullUri(opts)

Pull URI Request API .

The Pull URI Request API has to be implemented by the issuers and will be consumed by Digital Locker application. This API will be invoked when a citizen searches the issuer repository for his/her certificate. If the certificate data is Aadhaar seeded, the issuer may choose to use Aadhaar number as the search parameter. Digital Locker provides Aadhaar number, name and date of birth as on Aadhaar to the issuer API as additional parameters. The option for these Aadhaar based parameters can be selected while configuring this API in Digital Locker Partner’s Portal. If the certificate data is not Aadhaar seeded then the issuer may use any other unique parameter e.g. driving license number to search for a driving license. These custom parameters will be passed in the UDF elements as shown in the sample request below. The custom parameter(s) can be configured while configuring the API in the DigiLocker Partner’s Portal. The Digital Locker system will query the issuer repository to fetch the URI for any document that match the search criteria. The citizen can save this URI in his/her Digital Locker. It is strongly recommended that the issuer API validate that the name, date of birth details sent by DigiLocker in Aadhaar parameters match with the corresponding details on the certificate before returning the certificate data. This will ensure that only authentic owners get access to a certificate.

### Example

```javascript
import DigiLockerIssuerApis from 'digi_locker_issuer_apis';

let apiInstance = new DigiLockerIssuerApis.APIsApi();
let opts = {
  'contentType': "contentType_example", // String | application/xml
  'xDigilockerHmac': "xDigilockerHmac_example", // String | This is used for authentication and to verify the integrity of the request. DigiLocker calculates the hash message authentication code (hmac) of the HTTP request body using SHA256 hashing algorithm and the API Key provided by the issuer as the hashing key. The API Key is specified by the issuer while configuring the Pull Doc API in DigiLocker Partner Portal. The resulting hmac is converted to Base64 format and sent in this parameter. It is strongly recommended that the issuer API calculates the hmac of the HTTP request body, convert it to Base64 and match it with this parameter to ensure authenticity of the request.
  'pullURIRequest': new DigiLockerIssuerApis.PullURIRequest() // PullURIRequest | 
};
apiInstance.pullUri(opts, (error, data, response) => {
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
 **contentType** | **String**| application/xml | [optional] 
 **xDigilockerHmac** | **String**| This is used for authentication and to verify the integrity of the request. DigiLocker calculates the hash message authentication code (hmac) of the HTTP request body using SHA256 hashing algorithm and the API Key provided by the issuer as the hashing key. The API Key is specified by the issuer while configuring the Pull Doc API in DigiLocker Partner Portal. The resulting hmac is converted to Base64 format and sent in this parameter. It is strongly recommended that the issuer API calculates the hmac of the HTTP request body, convert it to Base64 and match it with this parameter to ensure authenticity of the request. | [optional] 
 **pullURIRequest** | [**PullURIRequest**](PullURIRequest.md)|  | [optional] 

### Return type

[**PullURIResponse**](PullURIResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/xml
- **Accept**: application/xml

