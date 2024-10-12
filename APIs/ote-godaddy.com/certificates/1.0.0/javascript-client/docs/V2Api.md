# OpenapiJsClient.V2Api

All URIs are relative to *http://api.ote-godaddy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAcmeExternalAccountBinding**](V2Api.md#getAcmeExternalAccountBinding) | **GET** /v2/customers/{customerId}/certificates/acme/externalAccountBinding | Retrieves the external account binding for the specified customer
[**getCertificateDetailByCertIdentifier**](V2Api.md#getCertificateDetailByCertIdentifier) | **GET** /v2/customers/{customerId}/certificates/{certificateId} | Retrieve individual certificate details
[**getCustomerCertificatesByCustomerId**](V2Api.md#getCustomerCertificatesByCustomerId) | **GET** /v2/customers/{customerId}/certificates | Retrieve customer&#39;s certificates
[**getDomainDetailsByDomain**](V2Api.md#getDomainDetailsByDomain) | **GET** /v2/customers/{customerId}/certificates/{certificateId}/domainVerifications/{domain} | Retrieve detailed information for supplied domain
[**getDomainInformationByCertificateId**](V2Api.md#getDomainInformationByCertificateId) | **GET** /v2/customers/{customerId}/certificates/{certificateId}/domainVerifications | Retrieve domain verification status



## getAcmeExternalAccountBinding

> ExternalAccountBinding getAcmeExternalAccountBinding(customerId)

Retrieves the external account binding for the specified customer

Use this endpoint to retrieve a key identifier and Hash-based Message Authentication Code (HMAC) key for Automated Certificate Management Environment (ACME) External Account Binding (EAB). These credentials can be used with an ACME client that supports EAB (ex. CertBot) to automate the issuance request and deployment of DV SSL certificates

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';

let apiInstance = new OpenapiJsClient.V2Api();
let customerId = "customerId_example"; // String | An identifier for a customer
apiInstance.getAcmeExternalAccountBinding(customerId, (error, data, response) => {
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
 **customerId** | **String**| An identifier for a customer | 

### Return type

[**ExternalAccountBinding**](ExternalAccountBinding.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, */*


## getCertificateDetailByCertIdentifier

> CertificateDetailV2 getCertificateDetailByCertIdentifier(customerId, certificateId)

Retrieve individual certificate details

Once the certificate order has been created, this method can be used to check the status of the certificate. This method can also be used to retrieve details of the certificate. &lt;ul&gt;&lt;li&gt;**shopperId** is **not the same** as **customerId**. **shopperId** is a number of max length 10 digits (*ex:* 1234567890) whereas **customerId** is a UUIDv4 (*ex:* 295e3bc3-b3b9-4d95-aae5-ede41a994d13)&lt;/li&gt;&lt;/ul&gt;

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';

let apiInstance = new OpenapiJsClient.V2Api();
let customerId = "customerId_example"; // String | An identifier for a customer
let certificateId = "certificateId_example"; // String | Certificate id to lookup
apiInstance.getCertificateDetailByCertIdentifier(customerId, certificateId, (error, data, response) => {
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
 **customerId** | **String**| An identifier for a customer | 
 **certificateId** | **String**| Certificate id to lookup | 

### Return type

[**CertificateDetailV2**](CertificateDetailV2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, */*


## getCustomerCertificatesByCustomerId

> CertificateSummariesV2 getCustomerCertificatesByCustomerId(customerId, opts)

Retrieve customer&#39;s certificates

This method can be used to retrieve a list of certificates for a specified customer. &lt;ul&gt;&lt;li&gt;**shopperId** is **not the same** as **customerId**.  **shopperId** is a number of max length 10 digits (*ex:* 1234567890) whereas **customerId** is a UUIDv4 (*ex:* 295e3bc3-b3b9-4d95-aae5-ede41a994d13)&lt;/li&gt;&lt;/ul&gt;

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';

let apiInstance = new OpenapiJsClient.V2Api();
let customerId = "customerId_example"; // String | An identifier for a customer
let opts = {
  'offset': 56, // Number | Number of results to skip for pagination
  'limit': 56 // Number | Maximum number of items to return
};
apiInstance.getCustomerCertificatesByCustomerId(customerId, opts, (error, data, response) => {
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
 **customerId** | **String**| An identifier for a customer | 
 **offset** | **Number**| Number of results to skip for pagination | [optional] 
 **limit** | **Number**| Maximum number of items to return | [optional] 

### Return type

[**CertificateSummariesV2**](CertificateSummariesV2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, */*


## getDomainDetailsByDomain

> DomainVerificationDetail getDomainDetailsByDomain(customerId, certificateId, domain)

Retrieve detailed information for supplied domain

Retrieve detailed information for supplied domain, including domain verification details and Certificate Authority Authorization (CAA) verification details. &lt;ul&gt;&lt;li&gt;**shopperId** is **not the same** as **customerId**.  **shopperId** is a number of max length 10 digits (*ex:* 1234567890) whereas **customerId** is a UUIDv4 (*ex:* 295e3bc3-b3b9-4d95-aae5-ede41a994d13)&lt;/li&gt;&lt;/ul&gt;

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';

let apiInstance = new OpenapiJsClient.V2Api();
let customerId = "customerId_example"; // String | An identifier for a customer
let certificateId = "certificateId_example"; // String | Certificate id to lookup
let domain = "domain_example"; // String | A valid domain name in the certificate request
apiInstance.getDomainDetailsByDomain(customerId, certificateId, domain, (error, data, response) => {
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
 **customerId** | **String**| An identifier for a customer | 
 **certificateId** | **String**| Certificate id to lookup | 
 **domain** | **String**| A valid domain name in the certificate request | 

### Return type

[**DomainVerificationDetail**](DomainVerificationDetail.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, */*


## getDomainInformationByCertificateId

> [DomainVerificationSummary] getDomainInformationByCertificateId(customerId, certificateId)

Retrieve domain verification status

This method can be used to retrieve the domain verification status for a certificate request.&lt;ul&gt;&lt;li&gt;**shopperId** is **not the same** as **customerId**.  **shopperId** is a number of max length 10 digits (*ex:* 1234567890) whereas **customerId** is a UUIDv4 (*ex:* 295e3bc3-b3b9-4d95-aae5-ede41a994d13)&lt;/li&gt;&lt;/ul&gt;\&quot;

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';

let apiInstance = new OpenapiJsClient.V2Api();
let customerId = "customerId_example"; // String | An identifier for a customer
let certificateId = "certificateId_example"; // String | Certificate id to lookup
apiInstance.getDomainInformationByCertificateId(customerId, certificateId, (error, data, response) => {
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
 **customerId** | **String**| An identifier for a customer | 
 **certificateId** | **String**| Certificate id to lookup | 

### Return type

[**[DomainVerificationSummary]**](DomainVerificationSummary.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, */*

