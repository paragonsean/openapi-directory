# AuthorizedPartnerApiSpecification.FileAPIsApi

All URIs are relative to *https://betaapi.digitallocker.gov.in/public*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getCertificateDataInXMLFormatFromURIId**](FileAPIsApi.md#getCertificateDataInXMLFormatFromURIId) | **GET** /oauth2/1/xml/{uri} | Get Certificate Data in XML Format from URI
[**getEAadhaarDataInXMLFormatId**](FileAPIsApi.md#getEAadhaarDataInXMLFormatId) | **GET** /oauth2/2/xml/eaadhaar | Get e-Aadhaar Data in XML Format
[**getFileFromURIId**](FileAPIsApi.md#getFileFromURIId) | **GET** /oauth2/1/file/{uri} | Get File from URI
[**getListOfIssuedDocumentsId**](FileAPIsApi.md#getListOfIssuedDocumentsId) | **GET** /oauth2/2/files/issued | Issued Documents
[**getListOfIssuedDocumentsVersion1Id**](FileAPIsApi.md#getListOfIssuedDocumentsVersion1Id) | **GET** /oauth2/1/files/issued | Issued Documents
[**getListOfSelfUploadedDocuments**](FileAPIsApi.md#getListOfSelfUploadedDocuments) | **GET** /oauth2/1/files/ | Get List of Self Uploaded Documents
[**getListOfSelfUploadedDocumentsId**](FileAPIsApi.md#getListOfSelfUploadedDocumentsId) | **GET** /oauth2/1/files/{id} | Get List of Self Uploaded Documents
[**pullDocumentId**](FileAPIsApi.md#pullDocumentId) | **POST** /oauth2/1/pull/pulldocument | Pull Document
[**uploadFileToLockerId**](FileAPIsApi.md#uploadFileToLockerId) | **POST** /oauth2/1/file/upload | Upload file to locker



## getCertificateDataInXMLFormatFromURIId

> XMLFormatSchema getCertificateDataInXMLFormatFromURIId(uri)

Get Certificate Data in XML Format from URI

Returns the certificate data in machine readable XML format for a URI. This API can be used to only for issued documents. The XML data may not be available for all documents. If the XML data is available for a particular document, the mime parameter in Get List of Issued Documents API will contain application/xml. Please refer to Digital Locker XML Certificate Formats for more details of XML formats of various documents.

### Example

```javascript
import AuthorizedPartnerApiSpecification from 'authorized_partner_api_specification';
let defaultClient = AuthorizedPartnerApiSpecification.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AuthorizedPartnerApiSpecification.FileAPIsApi();
let uri = "uri_example"; // String | 
apiInstance.getCertificateDataInXMLFormatFromURIId(uri, (error, data, response) => {
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
 **uri** | **String**|  | 

### Return type

[**XMLFormatSchema**](XMLFormatSchema.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/xml, application/json


## getEAadhaarDataInXMLFormatId

> EaadharXamlSchema getEAadhaarDataInXMLFormatId()

Get e-Aadhaar Data in XML Format

Returns e-Aadhaar data in XML format for the account.

### Example

```javascript
import AuthorizedPartnerApiSpecification from 'authorized_partner_api_specification';
let defaultClient = AuthorizedPartnerApiSpecification.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AuthorizedPartnerApiSpecification.FileAPIsApi();
apiInstance.getEAadhaarDataInXMLFormatId((error, data, response) => {
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

[**EaadharXamlSchema**](EaadharXamlSchema.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/xml, application/json


## getFileFromURIId

> String getFileFromURIId(uri)

Get File from URI

Returns a file from URI. This API can be used to fetch both issued document and uploaded document.

### Example

```javascript
import AuthorizedPartnerApiSpecification from 'authorized_partner_api_specification';
let defaultClient = AuthorizedPartnerApiSpecification.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AuthorizedPartnerApiSpecification.FileAPIsApi();
let uri = "uri_example"; // String | This is the unique identifier of the document.
apiInstance.getFileFromURIId(uri, (error, data, response) => {
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
 **uri** | **String**| This is the unique identifier of the document. | 

### Return type

**String**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/pdf, image/jpeg, image/jpg, image/png, application/json


## getListOfIssuedDocumentsId

> GetListOfIssuedDocumentsId200Response getListOfIssuedDocumentsId()

Issued Documents

Returns the list of meta-data about issued documents in user’s DigiLocker.

### Example

```javascript
import AuthorizedPartnerApiSpecification from 'authorized_partner_api_specification';

let apiInstance = new AuthorizedPartnerApiSpecification.FileAPIsApi();
apiInstance.getListOfIssuedDocumentsId((error, data, response) => {
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

[**GetListOfIssuedDocumentsId200Response**](GetListOfIssuedDocumentsId200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getListOfIssuedDocumentsVersion1Id

> Sample2 getListOfIssuedDocumentsVersion1Id()

Issued Documents

Returns the list of meta-data about issued documents in user’s DigiLocker.

### Example

```javascript
import AuthorizedPartnerApiSpecification from 'authorized_partner_api_specification';
let defaultClient = AuthorizedPartnerApiSpecification.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AuthorizedPartnerApiSpecification.FileAPIsApi();
apiInstance.getListOfIssuedDocumentsVersion1Id((error, data, response) => {
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

[**Sample2**](Sample2.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getListOfSelfUploadedDocuments

> Sample1 getListOfSelfUploadedDocuments()

Get List of Self Uploaded Documents

Returns the list of meta-data about documents or folders in user’s DigiLocker in a specific location.

### Example

```javascript
import AuthorizedPartnerApiSpecification from 'authorized_partner_api_specification';
let defaultClient = AuthorizedPartnerApiSpecification.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AuthorizedPartnerApiSpecification.FileAPIsApi();
apiInstance.getListOfSelfUploadedDocuments((error, data, response) => {
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

[**Sample1**](Sample1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getListOfSelfUploadedDocumentsId

> Sample3 getListOfSelfUploadedDocumentsId(id)

Get List of Self Uploaded Documents

Returns the list of meta-data about documents or folders in user’s DigiLocker in a specific location.

### Example

```javascript
import AuthorizedPartnerApiSpecification from 'authorized_partner_api_specification';
let defaultClient = AuthorizedPartnerApiSpecification.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AuthorizedPartnerApiSpecification.FileAPIsApi();
let id = "id_example"; // String | The id of the folder to list. To list the files of root folder of a user’s locker, do not send this parameter. This is sent as a part of the URL.
apiInstance.getListOfSelfUploadedDocumentsId(id, (error, data, response) => {
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
 **id** | **String**| The id of the folder to list. To list the files of root folder of a user’s locker, do not send this parameter. This is sent as a part of the URL. | 

### Return type

[**Sample3**](Sample3.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## pullDocumentId

> Sample4 pullDocumentId(opts)

Pull Document

This API allows a client application to search a document/certificate from issuer’s repository using the parameters provided by a user. The searched document is saved in user’s issued document section of DigiLocker if the search is successful.

### Example

```javascript
import AuthorizedPartnerApiSpecification from 'authorized_partner_api_specification';
let defaultClient = AuthorizedPartnerApiSpecification.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AuthorizedPartnerApiSpecification.FileAPIsApi();
let opts = {
  'chasisNo': "chasisNo_example", // String | Other parameters required for fetching a document as listed in paramname field of Get Search Parameters API.
  'consent': "consent_example", // String | The consent indicator from the user for performing demographic authentication using Aadhaar details. This Partner Application must capture the user consent for performing the Aadhaar demographic authentication. The possible values are ‘Y’ and ‘N’. The sign up request will be processed only when this indicator is ‘Y’.
  'doctype': "doctype_example", // String | A 5 character unique document type provided by DigiLocker.
  'orgid': "orgid_example", // String | The organization id for the issuer in DigiLocker. This organization id is returned in Get List of Issuers API mentioned above.
  'regNo': "regNo_example" // String | Other parameters required for fetching a document as listed in paramname field of Get Search Parameters API.
};
apiInstance.pullDocumentId(opts, (error, data, response) => {
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
 **chasisNo** | **String**| Other parameters required for fetching a document as listed in paramname field of Get Search Parameters API. | [optional] 
 **consent** | **String**| The consent indicator from the user for performing demographic authentication using Aadhaar details. This Partner Application must capture the user consent for performing the Aadhaar demographic authentication. The possible values are ‘Y’ and ‘N’. The sign up request will be processed only when this indicator is ‘Y’. | [optional] 
 **doctype** | **String**| A 5 character unique document type provided by DigiLocker. | [optional] 
 **orgid** | **String**| The organization id for the issuer in DigiLocker. This organization id is returned in Get List of Issuers API mentioned above. | [optional] 
 **regNo** | **String**| Other parameters required for fetching a document as listed in paramname field of Get Search Parameters API. | [optional] 

### Return type

[**Sample4**](Sample4.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## uploadFileToLockerId

> FileUploadResponse uploadFileToLockerId(opts)

Upload file to locker

This API can be used to save/upload a file to uploaded documents in DigiLocker. The allowed file types are JPG, JPEG, PNG and PDF. The file size must not exceed 10MB.

### Example

```javascript
import AuthorizedPartnerApiSpecification from 'authorized_partner_api_specification';
let defaultClient = AuthorizedPartnerApiSpecification.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AuthorizedPartnerApiSpecification.FileAPIsApi();
let opts = {
  'path': "path_example", // String | The destination path of the file in DigiLocker including filename.
  'hmac': "hmac_example", // String | This is used to verify the integrity of the file data. The client app calculates the hash message authentication code (HMAC) of the file content using SHA256 hashing algorithm and the client secret as the hashing key. The resulting HMAC is converted to Base64 format and sent in this parameter. Upon upload of file, DigiLocker calculates the HMAC of the file data and compares it with this HMAC..
  'fileUpload': new AuthorizedPartnerApiSpecification.FileUpload() // FileUpload | 
};
apiInstance.uploadFileToLockerId(opts, (error, data, response) => {
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
 **path** | **String**| The destination path of the file in DigiLocker including filename. | [optional] 
 **hmac** | **String**| This is used to verify the integrity of the file data. The client app calculates the hash message authentication code (HMAC) of the file content using SHA256 hashing algorithm and the client secret as the hashing key. The resulting HMAC is converted to Base64 format and sent in this parameter. Upon upload of file, DigiLocker calculates the HMAC of the file data and compares it with this HMAC.. | [optional] 
 **fileUpload** | [**FileUpload**](FileUpload.md)|  | [optional] 

### Return type

[**FileUploadResponse**](FileUploadResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/octet-stream, image/jpeg, image/jpg, image/pdf, image/png
- **Accept**: application/json

