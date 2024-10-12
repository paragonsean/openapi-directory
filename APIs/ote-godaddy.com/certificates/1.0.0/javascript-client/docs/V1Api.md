# OpenapiJsClient.V1Api

All URIs are relative to *http://api.ote-godaddy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**certificateActionRetrieve**](V1Api.md#certificateActionRetrieve) | **GET** /v1/certificates/{certificateId}/actions | Retrieve all certificate actions
[**certificateAlternateEmailAddress**](V1Api.md#certificateAlternateEmailAddress) | **POST** /v1/certificates/{certificateId}/email/resend/{emailAddress} | Add alternate email address
[**certificateCallbackDelete**](V1Api.md#certificateCallbackDelete) | **DELETE** /v1/certificates/{certificateId}/callback | Unregister system callback
[**certificateCallbackGet**](V1Api.md#certificateCallbackGet) | **GET** /v1/certificates/{certificateId}/callback | Retrieve system stateful action callback url
[**certificateCallbackReplace**](V1Api.md#certificateCallbackReplace) | **PUT** /v1/certificates/{certificateId}/callback | Register of certificate action callback
[**certificateCancel**](V1Api.md#certificateCancel) | **POST** /v1/certificates/{certificateId}/cancel | Cancel a pending certificate
[**certificateCreate**](V1Api.md#certificateCreate) | **POST** /v1/certificates | Create a pending order for certificate
[**certificateDownload**](V1Api.md#certificateDownload) | **GET** /v1/certificates/{certificateId}/download | Download certificate
[**certificateDownloadEntitlement**](V1Api.md#certificateDownloadEntitlement) | **GET** /v2/certificates/download | Download certificate by entitlement
[**certificateEmailHistory**](V1Api.md#certificateEmailHistory) | **GET** /v1/certificates/{certificateId}/email/history | Retrieve email history
[**certificateGet**](V1Api.md#certificateGet) | **GET** /v1/certificates/{certificateId} | Retrieve certificate details
[**certificateGetEntitlement**](V1Api.md#certificateGetEntitlement) | **GET** /v2/certificates | Search for certificate details by entitlement
[**certificateReissue**](V1Api.md#certificateReissue) | **POST** /v1/certificates/{certificateId}/reissue | Reissue active certificate
[**certificateRenew**](V1Api.md#certificateRenew) | **POST** /v1/certificates/{certificateId}/renew | Renew active certificate
[**certificateResendEmail**](V1Api.md#certificateResendEmail) | **POST** /v1/certificates/{certificateId}/email/{emailId}/resend | Resend an email
[**certificateResendEmailAddress**](V1Api.md#certificateResendEmailAddress) | **POST** /v1/certificates/{certificateId}/email/{emailId}/resend/{emailAddress} | Resend email to email address
[**certificateRevoke**](V1Api.md#certificateRevoke) | **POST** /v1/certificates/{certificateId}/revoke | Revoke active certificate
[**certificateSitesealGet**](V1Api.md#certificateSitesealGet) | **GET** /v1/certificates/{certificateId}/siteSeal | Get Site seal
[**certificateValidate**](V1Api.md#certificateValidate) | **POST** /v1/certificates/validate | Validate a pending order for certificate
[**certificateVerifydomaincontrol**](V1Api.md#certificateVerifydomaincontrol) | **POST** /v1/certificates/{certificateId}/verifyDomainControl | Check Domain Control



## certificateActionRetrieve

> [CertificateAction] certificateActionRetrieve(certificateId)

Retrieve all certificate actions

This method is used to retrieve all stateful actions relating to a certificate lifecycle.

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';

let apiInstance = new OpenapiJsClient.V1Api();
let certificateId = "certificateId_example"; // String | Certificate id to register for callback
apiInstance.certificateActionRetrieve(certificateId, (error, data, response) => {
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
 **certificateId** | **String**| Certificate id to register for callback | 

### Return type

[**[CertificateAction]**](CertificateAction.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## certificateAlternateEmailAddress

> CertificateEmailHistory certificateAlternateEmailAddress(certificateId, emailAddress)

Add alternate email address

This method adds an alternate email address to a certificate order and re-sends all existing request emails to that address.

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';

let apiInstance = new OpenapiJsClient.V1Api();
let certificateId = "certificateId_example"; // String | Certificate id to resend emails
let emailAddress = "emailAddress_example"; // String | Specific email address to resend email
apiInstance.certificateAlternateEmailAddress(certificateId, emailAddress, (error, data, response) => {
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
 **certificateId** | **String**| Certificate id to resend emails | 
 **emailAddress** | **String**| Specific email address to resend email | 

### Return type

[**CertificateEmailHistory**](CertificateEmailHistory.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## certificateCallbackDelete

> certificateCallbackDelete(certificateId)

Unregister system callback

Unregister the callback for a particular certificate.

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';

let apiInstance = new OpenapiJsClient.V1Api();
let certificateId = "certificateId_example"; // String | Certificate id to unregister callback
apiInstance.certificateCallbackDelete(certificateId, (error, data, response) => {
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
 **certificateId** | **String**| Certificate id to unregister callback | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## certificateCallbackGet

> CertificateCallback certificateCallbackGet(certificateId)

Retrieve system stateful action callback url

This method is used to retrieve the registered callback url for a certificate.

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';

let apiInstance = new OpenapiJsClient.V1Api();
let certificateId = "certificateId_example"; // String | Certificate id to register for stateful action callback
apiInstance.certificateCallbackGet(certificateId, (error, data, response) => {
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
 **certificateId** | **String**| Certificate id to register for stateful action callback | 

### Return type

[**CertificateCallback**](CertificateCallback.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## certificateCallbackReplace

> certificateCallbackReplace(certificateId, callbackUrl)

Register of certificate action callback

This method is used to register/replace url for callbacks for stateful actions relating to a certificate lifecycle. The callback url is a Webhook style pattern and will receive POST http requests with json body defined in the CertificateAction model definition for each certificate action.  Only one callback URL is allowed to be registered for each certificateId, so it will replace a previous registration.

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';

let apiInstance = new OpenapiJsClient.V1Api();
let certificateId = "certificateId_example"; // String | Certificate id to register/replace for callback
let callbackUrl = "callbackUrl_example"; // String | Callback url registered/replaced to receive stateful actions
apiInstance.certificateCallbackReplace(certificateId, callbackUrl, (error, data, response) => {
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
 **certificateId** | **String**| Certificate id to register/replace for callback | 
 **callbackUrl** | **String**| Callback url registered/replaced to receive stateful actions | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## certificateCancel

> certificateCancel(certificateId)

Cancel a pending certificate

Use the cancel call to cancel a pending certificate order.

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';

let apiInstance = new OpenapiJsClient.V1Api();
let certificateId = "certificateId_example"; // String | Certificate id to cancel
apiInstance.certificateCancel(certificateId, (error, data, response) => {
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
 **certificateId** | **String**| Certificate id to cancel | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## certificateCreate

> CertificateIdentifier certificateCreate(certificateCreate, opts)

Create a pending order for certificate

&lt;p&gt;Creating a certificate order can be a long running asynchronous operation in the PKI workflow. The PKI API supports 2 options for getting the completion stateful actions for this asynchronous operations: 1) by polling operations -- see /v1/certificates/{certificateId}/actions 2) via WebHook style callback -- see &#39;/v1/certificates/{certificateId}/callback&#39;.&lt;/p&gt;

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';

let apiInstance = new OpenapiJsClient.V1Api();
let certificateCreate = new OpenapiJsClient.CertificateCreate(); // CertificateCreate | The certificate order information
let opts = {
  'xMarketId': "'Default locale for shopper account'" // String | Setting locale for communications such as emails and error messages
};
apiInstance.certificateCreate(certificateCreate, opts, (error, data, response) => {
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
 **certificateCreate** | [**CertificateCreate**](CertificateCreate.md)| The certificate order information | 
 **xMarketId** | **String**| Setting locale for communications such as emails and error messages | [optional] [default to &#39;Default locale for shopper account&#39;]

### Return type

[**CertificateIdentifier**](CertificateIdentifier.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## certificateDownload

> CertificateBundle certificateDownload(certificateId)

Download certificate

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';

let apiInstance = new OpenapiJsClient.V1Api();
let certificateId = "certificateId_example"; // String | Certificate id to download
apiInstance.certificateDownload(certificateId, (error, data, response) => {
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
 **certificateId** | **String**| Certificate id to download | 

### Return type

[**CertificateBundle**](CertificateBundle.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## certificateDownloadEntitlement

> CertificateBundle certificateDownloadEntitlement(entitlementId)

Download certificate by entitlement

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';

let apiInstance = new OpenapiJsClient.V1Api();
let entitlementId = "entitlementId_example"; // String | Entitlement id to download
apiInstance.certificateDownloadEntitlement(entitlementId, (error, data, response) => {
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
 **entitlementId** | **String**| Entitlement id to download | 

### Return type

[**CertificateBundle**](CertificateBundle.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## certificateEmailHistory

> CertificateEmailHistory certificateEmailHistory(certificateId)

Retrieve email history

This method can be used to retrieve all emails sent for a certificate.

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';

let apiInstance = new OpenapiJsClient.V1Api();
let certificateId = "certificateId_example"; // String | Certificate id to retrieve email history
apiInstance.certificateEmailHistory(certificateId, (error, data, response) => {
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
 **certificateId** | **String**| Certificate id to retrieve email history | 

### Return type

[**CertificateEmailHistory**](CertificateEmailHistory.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## certificateGet

> Certificate certificateGet(certificateId)

Retrieve certificate details

Once the certificate order has been created, this method can be used to check the status of the certificate. This method can also be used to retrieve details of the certificate.

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';

let apiInstance = new OpenapiJsClient.V1Api();
let certificateId = "certificateId_example"; // String | Certificate id to lookup
apiInstance.certificateGet(certificateId, (error, data, response) => {
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
 **certificateId** | **String**| Certificate id to lookup | 

### Return type

[**Certificate**](Certificate.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## certificateGetEntitlement

> [Certificate] certificateGetEntitlement(entitlementId, opts)

Search for certificate details by entitlement

Once the certificate order has been created, this method can be used to check the status of the certificate. This method can also be used to retrieve details of the certificates associated to an entitlement.

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';

let apiInstance = new OpenapiJsClient.V1Api();
let entitlementId = "entitlementId_example"; // String | Entitlement id to lookup
let opts = {
  'latest': true // Boolean | Fetch only the most recent certificate
};
apiInstance.certificateGetEntitlement(entitlementId, opts, (error, data, response) => {
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
 **entitlementId** | **String**| Entitlement id to lookup | 
 **latest** | **Boolean**| Fetch only the most recent certificate | [optional] [default to true]

### Return type

[**[Certificate]**](Certificate.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## certificateReissue

> certificateReissue(certificateId, certificateReissue)

Reissue active certificate

&lt;p&gt;Rekeying is the process by which the private and public key is changed for a certificate. It is a simplified reissue,where only the CSR is changed. Reissuing is the process by which domain names are added or removed from a certificate.Once a request is validated and approved, the certificate will be reissued with the new common name and sans specified. Unlimited reissues are available during the lifetime of the certificate.New names added to a certificate that do not share the base domain of the common name may take additional time to validate. If this API call is made before a previous pending reissue has been validated and issued, the previous reissue request is automatically rejected and replaced with the current request.&lt;/p&gt;

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';

let apiInstance = new OpenapiJsClient.V1Api();
let certificateId = "certificateId_example"; // String | Certificate id to reissue
let certificateReissue = new OpenapiJsClient.CertificateReissue(); // CertificateReissue | The reissue request info
apiInstance.certificateReissue(certificateId, certificateReissue, (error, data, response) => {
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
 **certificateId** | **String**| Certificate id to reissue | 
 **certificateReissue** | [**CertificateReissue**](CertificateReissue.md)| The reissue request info | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## certificateRenew

> certificateRenew(certificateId, certificateRenew)

Renew active certificate

Renewal is the process by which the validity of a certificate is extended. Renewal is only available 60 days prior to expiration of the previous certificate and 30 days after the expiration of the previous certificate. The renewal supports modifying a set of the original certificate order information. Once a request is validated and approved, the certificate will be issued with extended validity. Since subject alternative names can be removed during a renewal, we require that you provide the subject alternative names you expect in the renewed certificate. New names added to a certificate that do not share the base domain of the common name may take additional time to validate. &lt;/p&gt;

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';

let apiInstance = new OpenapiJsClient.V1Api();
let certificateId = "certificateId_example"; // String | Certificate id to renew
let certificateRenew = new OpenapiJsClient.CertificateRenew(); // CertificateRenew | The renew request info
apiInstance.certificateRenew(certificateId, certificateRenew, (error, data, response) => {
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
 **certificateId** | **String**| Certificate id to renew | 
 **certificateRenew** | [**CertificateRenew**](CertificateRenew.md)| The renew request info | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## certificateResendEmail

> certificateResendEmail(certificateId, emailId)

Resend an email

This method can be used to resend emails by providing the certificate id and the email id

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';

let apiInstance = new OpenapiJsClient.V1Api();
let certificateId = "certificateId_example"; // String | Certificate id to resend email
let emailId = "emailId_example"; // String | Email id for email to resend
apiInstance.certificateResendEmail(certificateId, emailId, (error, data, response) => {
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
 **certificateId** | **String**| Certificate id to resend email | 
 **emailId** | **String**| Email id for email to resend | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## certificateResendEmailAddress

> certificateResendEmailAddress(certificateId, emailId, emailAddress)

Resend email to email address

This method can be used to resend emails by providing the certificate id, the email id, and the recipient email address

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';

let apiInstance = new OpenapiJsClient.V1Api();
let certificateId = "certificateId_example"; // String | Certificate id to resend emails
let emailId = "emailId_example"; // String | Email id for email to resend
let emailAddress = "emailAddress_example"; // String | Specific email address to resend email
apiInstance.certificateResendEmailAddress(certificateId, emailId, emailAddress, (error, data, response) => {
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
 **certificateId** | **String**| Certificate id to resend emails | 
 **emailId** | **String**| Email id for email to resend | 
 **emailAddress** | **String**| Specific email address to resend email | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## certificateRevoke

> certificateRevoke(certificateId, certificateRevoke)

Revoke active certificate

Use revoke call to revoke an active certificate, if the certificate has not been issued a 404 response will be returned.

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';

let apiInstance = new OpenapiJsClient.V1Api();
let certificateId = "certificateId_example"; // String | Certificate id to revoke
let certificateRevoke = new OpenapiJsClient.CertificateRevoke(); // CertificateRevoke | The certificate revocation request
apiInstance.certificateRevoke(certificateId, certificateRevoke, (error, data, response) => {
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
 **certificateId** | **String**| Certificate id to revoke | 
 **certificateRevoke** | [**CertificateRevoke**](CertificateRevoke.md)| The certificate revocation request | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## certificateSitesealGet

> CertificateSiteSeal certificateSitesealGet(certificateId, opts)

Get Site seal

&lt;p&gt;This method is used to obtain the site seal information for an issued certificate. A site seal is a graphic that the certificate purchaser can embed on their web site to show their visitors information about their SSL certificate. If a web site visitor clicks on the site seal image, a pop-up page is displayed that contains detailed information about the SSL certificate. The site seal token is used to link the site seal graphic image to the appropriate certificate details pop-up page display when a user clicks on the site seal. The site seal images are expected to be static images and hosted on the reseller&#39;s website, to minimize delays for customer page load times.&lt;/p&gt;

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';

let apiInstance = new OpenapiJsClient.V1Api();
let certificateId = "certificateId_example"; // String | Certificate id
let opts = {
  'theme': "'LIGHT'", // String | This value represents the visual theme of the seal. If seal doesn't exist, default values are used if params not present. If seal does exist, default values will not be used to update unless params present.
  'locale': "'en'" // String | Determine locale for text displayed in seal image and verification page. If seal doesn't exist, default values are used if params not present. If seal does exist, default values will not be used to update unless params present.
};
apiInstance.certificateSitesealGet(certificateId, opts, (error, data, response) => {
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
 **certificateId** | **String**| Certificate id | 
 **theme** | **String**| This value represents the visual theme of the seal. If seal doesn&#39;t exist, default values are used if params not present. If seal does exist, default values will not be used to update unless params present. | [optional] [default to &#39;LIGHT&#39;]
 **locale** | **String**| Determine locale for text displayed in seal image and verification page. If seal doesn&#39;t exist, default values are used if params not present. If seal does exist, default values will not be used to update unless params present. | [optional] [default to &#39;en&#39;]

### Return type

[**CertificateSiteSeal**](CertificateSiteSeal.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## certificateValidate

> certificateValidate(certificateCreate, opts)

Validate a pending order for certificate

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';

let apiInstance = new OpenapiJsClient.V1Api();
let certificateCreate = new OpenapiJsClient.CertificateCreate(); // CertificateCreate | The certificate order info
let opts = {
  'xMarketId': "'Default locale for shopper account'" // String | Setting locale for communications such as emails and error messages
};
apiInstance.certificateValidate(certificateCreate, opts, (error, data, response) => {
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
 **certificateCreate** | [**CertificateCreate**](CertificateCreate.md)| The certificate order info | 
 **xMarketId** | **String**| Setting locale for communications such as emails and error messages | [optional] [default to &#39;Default locale for shopper account&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## certificateVerifydomaincontrol

> certificateVerifydomaincontrol(certificateId)

Check Domain Control

Domain control is a means for verifying the domain included in the certificate order. This resource is useful for resellers that control the domains for their customers, and can expedite the verification process. See https://www.godaddy.com/help/verifying-your-domain-ownership-for-ssl-certificate-requests-html-or-dns-7452

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';

let apiInstance = new OpenapiJsClient.V1Api();
let certificateId = "certificateId_example"; // String | Certificate id to lookup
apiInstance.certificateVerifydomaincontrol(certificateId, (error, data, response) => {
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
 **certificateId** | **String**| Certificate id to lookup | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

