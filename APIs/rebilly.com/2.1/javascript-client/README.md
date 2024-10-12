# rebilly_rest_api

RebillyRestApi - JavaScript client for rebilly_rest_api
# Introduction
The Rebilly API is built on HTTP.  Our API is RESTful.  It has predictable
resource URLs.  It returns HTTP response codes to indicate errors.  It also
accepts and returns JSON in the HTTP body.  You can use your favorite
HTTP/REST library for your programming language to use Rebilly's API, or
you can use one of our SDKs (currently available in [PHP](https://github.com/Rebilly/rebilly-php)
and [Javascript](https://github.com/Rebilly/rebilly-js-sdk)).

We have other APIs that are also available.  Every action from our [app](https://app.rebilly.com)
is supported by an API which is documented and available for use so that you
may automate any workflows necessary.  This document contains the most commonly
integrated resources.

# Authentication

When you sign up for an account, you are given your first secret API key.
You can generate additional API keys, and delete API keys (as you may
need to rotate your keys in the future). You authenticate to the
Rebilly API by providing your secret key in the request header.

Rebilly offers three forms of authentication:  secret key, publishable key, JSON Web Tokens, and public signature key.
- [Secret API key](#section/Authentication/SecretApiKey): used for requests made
  from the server side. Never share these keys. Keep them guarded and secure.
- [Publishable API key](#section/Authentication/PublishableApiKey): used for 
  requests from the client side. For now can only be used to create 
  a [Payment Token](#operation/PostToken) and 
  a [File token](#operation/PostFile).
- [JWT](#section/Authentication/JWT): short lifetime tokens that can be assigned a specific expiration time.

Never share your secret keys. Keep them guarded and secure.

&lt;!-- ReDoc-Inject: &lt;security-definitions&gt; --&gt;

# Errors
Rebilly follow's the error response format proposed in [RFC 7807](https://tools.ietf.org/html/rfc7807) also known as Problem Details for HTTP APIs.  As with our normal API responses, your client must be prepared to gracefully handle additional members of the response.

## Forbidden
&lt;RedocResponse pointer={\"#/components/responses/Forbidden\"} /&gt;

## Conflict
&lt;RedocResponse pointer={\"#/components/responses/Conflict\"} /&gt;

## NotFound
&lt;RedocResponse pointer={\"#/components/responses/NotFound\"} /&gt;

## Unauthorized
&lt;RedocResponse pointer={\"#/components/responses/Unauthorized\"} /&gt;

## ValidationError
&lt;RedocResponse pointer={\"#/components/responses/ValidationError\"} /&gt;

# SDKs

Rebilly offers a Javascript SDK and a PHP SDK to help interact with
the API.  However, no SDK is required to use the API.

Rebilly also offers [FramePay](https://docs.rebilly.com/docs/developer-docs/framepay/),
 a client-side iFrame-based solution to help
create payment tokens while minimizing PCI DSS compliance burdens
and maximizing the customizability. [FramePay](https://docs.rebilly.com/docs/developer-docs/framepay/)
is interacting with the [payment tokens creation operation](#operation/PostToken).

## Javascript SDK

Installation and usage instructions can be found [here](https://docs.rebilly.com/docs/developer-docs/sdks).
SDK code examples are included in these docs.

## PHP SDK
For all PHP SDK examples provided in these docs you will need to configure the `$client`.
You may do it like this:

```php
$client = new Rebilly\\Client([
    'apiKey' =&gt; 'YourApiKeyHere',
    'baseUrl' =&gt; 'https://api.rebilly.com',
]);
```

# Using filter with collections
Rebilly provides collections filtering. You can use `?filter` param on collections to define which records should be shown in the response.

Here is filter format description:

- Fields and values in filter are separated with `:`: `?filter=firstName:John`.

- Sub-fields are separated with `.`: `?filter=billingAddress.country:US`.

- Multiple filters are separated with `;`: `?filter=firstName:John;lastName:Doe`. They will be joined with `AND` logic. In this example: `firstName:John` AND `lastName:Doe`.

- You can use multiple values using `,` as values separator: `?filter=firstName:John,Bob`. Multiple values specified for a field will be joined with `OR` logic. In this example: `firstName:John` OR `firstName:Bob`.

- To negate the filter use `!`: `?filter=firstName:!John`. Note that you can negate multiple values like this: `?filter=firstName:!John,!Bob`. This filter rule will exclude all Johns and Bobs from the response.

- You can use range filters like this: `?filter=amount:1..10`.

- You can use gte (greater than or equals) filter like this: `?filter=amount:1..`, or lte (less than or equals) than filter like this: `?filter=amount:..10`. This also works for datetime-based fields.

- You can create some [predefined values lists](https://user-api-docs.rebilly.com/#tag/Lists) and use them in filter: `?filter=firstName:@yourListName`. You can also exclude list values: `?filter=firstName:!@yourListName`.

- Datetime-based fields accept values formatted using RFC 3339 like this: `?filter=createdTime:2021-02-14T13:30:00Z`. 

# Expand to include embedded objects
Rebilly provides the ability to pre-load additional 
objects with a request. 

You can use `?expand` param on most requests to expand
and include embedded objects within the
`_embedded` property of the response.

The `_embedded` property contains an array of 
objects keyed by the expand parameter value(s).

You may expand multiple objects by passing them
as comma-separated to the expand value like so:

```
?expand=recentInvoice,customer
```

And in the response, you would see:

```
\"_embedded\": [
    \"recentInvoice\": {...},
    \"customer\": {...}
]
```
Expand may be utilitized not only on `GET` requests but also on `PATCH`, `POST`, `PUT` requests too.


# Getting started guide

Rebilly's API has over 300 operations.  That's more than you'll 
need to implement your use cases.  If you have a use 
case you would like to implement, please consult us for
feedback on the best API operations for the task.

Our getting started guide will demonstrate a basic order form use
case.  It will allow us to highlight core resources
in Rebilly that will be helpful for many other use cases
too.

Within 25 minutes, you'll have sent API requests (via our console)
to create a subscription order.

This SDK is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 2.1
- Package version: 2.1
- Generator version: 7.9.0
- Build package: org.openapitools.codegen.languages.JavascriptClientCodegen
For more information, please visit [https://www.rebilly.com/contact/](https://www.rebilly.com/contact/)

## Installation

### For [Node.js](https://nodejs.org/)

#### npm

To publish the library as a [npm](https://www.npmjs.com/), please follow the procedure in ["Publishing npm packages"](https://docs.npmjs.com/getting-started/publishing-npm-packages).

Then install it via:

```shell
npm install rebilly_rest_api --save
```

Finally, you need to build the module:

```shell
npm run build
```

##### Local development

To use the library locally without publishing to a remote npm registry, first install the dependencies by changing into the directory containing `package.json` (and this README). Let's call this `JAVASCRIPT_CLIENT_DIR`. Then run:

```shell
npm install
```

Next, [link](https://docs.npmjs.com/cli/link) it globally in npm with the following, also from `JAVASCRIPT_CLIENT_DIR`:

```shell
npm link
```

To use the link you just defined in your project, switch to the directory you want to use your rebilly_rest_api from, and run:

```shell
npm link /path/to/<JAVASCRIPT_CLIENT_DIR>
```

Finally, you need to build the module:

```shell
npm run build
```

#### git

If the library is hosted at a git repository, e.g.https://github.com/GIT_USER_ID/GIT_REPO_ID
then install it via:

```shell
    npm install GIT_USER_ID/GIT_REPO_ID --save
```

### For browser

The library also works in the browser environment via npm and [browserify](http://browserify.org/). After following
the above steps with Node.js and installing browserify with `npm install -g browserify`,
perform the following (assuming *main.js* is your entry file):

```shell
browserify main.js > bundle.js
```

Then include *bundle.js* in the HTML pages.

### Webpack Configuration

Using Webpack you may encounter the following error: "Module not found: Error:
Cannot resolve module", most certainly you should disable AMD loader. Add/merge
the following section to your webpack config:

```javascript
module: {
  rules: [
    {
      parser: {
        amd: false
      }
    }
  ]
}
```

## Getting Started

Please follow the [installation](#installation) instruction and execute the following JS code:

```javascript
var RebillyRestApi = require('rebilly_rest_api');

var defaultClient = RebillyRestApi.ApiClient.instance;
// Configure API key authorization: SecretApiKey
var SecretApiKey = defaultClient.authentications['SecretApiKey'];
SecretApiKey.apiKey = "YOUR API KEY"
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//SecretApiKey.apiKeyPrefix['REB-APIKEY'] = "Token"
// Configure Bearer (JWT) access token for authorization: JWT
var JWT = defaultClient.authentications['JWT'];
JWT.accessToken = "YOUR ACCESS TOKEN"

var api = new RebillyRestApi.AMLApi()
var firstName = "firstName_example"; // {String} First name of individual to search.
var lastName = "lastName_example"; // {String} Last name of individual to search.
var opts = {
  'organizationId': "organizationId_example", // {String} Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
  'dob': "dob_example", // {String} Date of birth in format YYYY-MM-DD.
  'country': "country_example" // {String} Country of individual as an ISO Alpha-2 code.
};
var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
api.getAmlEntry(firstName, lastName, opts, callback);

```

## Documentation for API Endpoints

All URIs are relative to *https://api-sandbox.rebilly.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*RebillyRestApi.AMLApi* | [**getAmlEntry**](docs/AMLApi.md#getAmlEntry) | **GET** /aml | Search PEP/Sanctions/Adverse Media lists
*RebillyRestApi.BankAccountsApi* | [**getBankAccount**](docs/BankAccountsApi.md#getBankAccount) | **GET** /bank-accounts/{id} | Retrieve a Bank Account
*RebillyRestApi.BankAccountsApi* | [**getBankAccountCollection**](docs/BankAccountsApi.md#getBankAccountCollection) | **GET** /bank-accounts | Retrieve a list of bank accounts
*RebillyRestApi.BankAccountsApi* | [**patchBankAccount**](docs/BankAccountsApi.md#patchBankAccount) | **PATCH** /bank-accounts/{id} | Update a bank account&#39;s values
*RebillyRestApi.BankAccountsApi* | [**postBankAccount**](docs/BankAccountsApi.md#postBankAccount) | **POST** /bank-accounts | Create a Bank Account
*RebillyRestApi.BankAccountsApi* | [**postBankAccountDeactivation**](docs/BankAccountsApi.md#postBankAccountDeactivation) | **POST** /bank-accounts/{id}/deactivation | Deactivate a Bank Account
*RebillyRestApi.BankAccountsApi* | [**putBankAccount**](docs/BankAccountsApi.md#putBankAccount) | **PUT** /bank-accounts/{id} | Create a Bank Account with predefined ID
*RebillyRestApi.BlocklistsApi* | [**deleteBlocklist**](docs/BlocklistsApi.md#deleteBlocklist) | **DELETE** /blocklists/{id} | Delete a blocklist
*RebillyRestApi.BlocklistsApi* | [**getBlocklist**](docs/BlocklistsApi.md#getBlocklist) | **GET** /blocklists/{id} | Retrieve a blocklist
*RebillyRestApi.BlocklistsApi* | [**getBlocklistCollection**](docs/BlocklistsApi.md#getBlocklistCollection) | **GET** /blocklists | Retrieve a list of blocklists
*RebillyRestApi.BlocklistsApi* | [**postBlocklist**](docs/BlocklistsApi.md#postBlocklist) | **POST** /blocklists | Create a blocklist
*RebillyRestApi.BlocklistsApi* | [**putBlocklist**](docs/BlocklistsApi.md#putBlocklist) | **PUT** /blocklists/{id} | Create a blocklist with predefined ID
*RebillyRestApi.Class3DSecureApi* | [**get3DSecure**](docs/Class3DSecureApi.md#get3DSecure) | **GET** /3dsecure/{id} | Retrieve a ThreeDSecure entry
*RebillyRestApi.Class3DSecureApi* | [**get3DSecureCollection**](docs/Class3DSecureApi.md#get3DSecureCollection) | **GET** /3dsecure | Retrieve a list of ThreeDSecure entries
*RebillyRestApi.Class3DSecureApi* | [**post3DSecure**](docs/Class3DSecureApi.md#post3DSecure) | **POST** /3dsecure | Create a ThreeDSecure entry
*RebillyRestApi.CouponsApi* | [**getCoupon**](docs/CouponsApi.md#getCoupon) | **GET** /coupons/{id} | Retrieve a coupon
*RebillyRestApi.CouponsApi* | [**getCouponCollection**](docs/CouponsApi.md#getCouponCollection) | **GET** /coupons | Retrieve a list of coupons
*RebillyRestApi.CouponsApi* | [**getCouponRedemption**](docs/CouponsApi.md#getCouponRedemption) | **GET** /coupons-redemptions/{id} | Retrieve a coupon redemption with specified identifier string
*RebillyRestApi.CouponsApi* | [**getCouponRedemptionCollection**](docs/CouponsApi.md#getCouponRedemptionCollection) | **GET** /coupons-redemptions | Retrieve a list of coupon redemptions
*RebillyRestApi.CouponsApi* | [**postCoupon**](docs/CouponsApi.md#postCoupon) | **POST** /coupons | Create a coupon
*RebillyRestApi.CouponsApi* | [**postCouponExpiration**](docs/CouponsApi.md#postCouponExpiration) | **POST** /coupons/{id}/expiration | Set a coupon&#39;s expiration time
*RebillyRestApi.CouponsApi* | [**postCouponRedemption**](docs/CouponsApi.md#postCouponRedemption) | **POST** /coupons-redemptions | Redeem a coupon
*RebillyRestApi.CouponsApi* | [**postCouponRedemptionCancellation**](docs/CouponsApi.md#postCouponRedemptionCancellation) | **POST** /coupons-redemptions/{id}/cancel | Cancel a coupon redemption
*RebillyRestApi.CouponsApi* | [**putCoupon**](docs/CouponsApi.md#putCoupon) | **PUT** /coupons/{id} | Create or update a coupon with predefined coupon ID
*RebillyRestApi.CustomFieldsApi* | [**getCustomField**](docs/CustomFieldsApi.md#getCustomField) | **GET** /custom-fields/{resource}/{name} | Retrieve a Custom Field
*RebillyRestApi.CustomFieldsApi* | [**getCustomFieldCollection**](docs/CustomFieldsApi.md#getCustomFieldCollection) | **GET** /custom-fields/{resource} | Retrieve Custom Fields
*RebillyRestApi.CustomFieldsApi* | [**putCustomField**](docs/CustomFieldsApi.md#putCustomField) | **PUT** /custom-fields/{resource}/{name} | Create or alter a Custom Field
*RebillyRestApi.CustomerAuthenticationApi* | [**deleteAuthenticationToken**](docs/CustomerAuthenticationApi.md#deleteAuthenticationToken) | **DELETE** /authentication-tokens/{token} | Logout a customer
*RebillyRestApi.CustomerAuthenticationApi* | [**deleteCredential**](docs/CustomerAuthenticationApi.md#deleteCredential) | **DELETE** /credentials/{id} | Delete a credential
*RebillyRestApi.CustomerAuthenticationApi* | [**deletePasswordToken**](docs/CustomerAuthenticationApi.md#deletePasswordToken) | **DELETE** /password-tokens/{id} | Delete a Reset Password Token
*RebillyRestApi.CustomerAuthenticationApi* | [**getAuthenticationOption**](docs/CustomerAuthenticationApi.md#getAuthenticationOption) | **GET** /authentication-options | Read current authentication options
*RebillyRestApi.CustomerAuthenticationApi* | [**getAuthenticationTokenCollection**](docs/CustomerAuthenticationApi.md#getAuthenticationTokenCollection) | **GET** /authentication-tokens | Retrieve a list of auth tokens
*RebillyRestApi.CustomerAuthenticationApi* | [**getAuthenticationTokenVerification**](docs/CustomerAuthenticationApi.md#getAuthenticationTokenVerification) | **GET** /authentication-tokens/{token} | Verify
*RebillyRestApi.CustomerAuthenticationApi* | [**getCredential**](docs/CustomerAuthenticationApi.md#getCredential) | **GET** /credentials/{id} | Retrieve a credential
*RebillyRestApi.CustomerAuthenticationApi* | [**getCredentialCollection**](docs/CustomerAuthenticationApi.md#getCredentialCollection) | **GET** /credentials | Retrieve a list of credentials
*RebillyRestApi.CustomerAuthenticationApi* | [**getPasswordToken**](docs/CustomerAuthenticationApi.md#getPasswordToken) | **GET** /password-tokens/{id} | Retrieve a Reset Password Token
*RebillyRestApi.CustomerAuthenticationApi* | [**getPasswordTokenCollection**](docs/CustomerAuthenticationApi.md#getPasswordTokenCollection) | **GET** /password-tokens | Retrieve a list of tokens
*RebillyRestApi.CustomerAuthenticationApi* | [**postAuthenticationToken**](docs/CustomerAuthenticationApi.md#postAuthenticationToken) | **POST** /authentication-tokens | Login
*RebillyRestApi.CustomerAuthenticationApi* | [**postAuthenticationTokenExchange**](docs/CustomerAuthenticationApi.md#postAuthenticationTokenExchange) | **POST** /authentication-tokens/{token}/exchange | Exchange
*RebillyRestApi.CustomerAuthenticationApi* | [**postCredential**](docs/CustomerAuthenticationApi.md#postCredential) | **POST** /credentials | Create a credential
*RebillyRestApi.CustomerAuthenticationApi* | [**postPasswordToken**](docs/CustomerAuthenticationApi.md#postPasswordToken) | **POST** /password-tokens | Create a Reset Password Token
*RebillyRestApi.CustomerAuthenticationApi* | [**putAuthenticationOption**](docs/CustomerAuthenticationApi.md#putAuthenticationOption) | **PUT** /authentication-options | Change authentication options
*RebillyRestApi.CustomerAuthenticationApi* | [**putCredential**](docs/CustomerAuthenticationApi.md#putCredential) | **PUT** /credentials/{id} | Create or update a credential with predefined ID
*RebillyRestApi.CustomersApi* | [**deleteCustomer**](docs/CustomersApi.md#deleteCustomer) | **DELETE** /customers/{id} | Merge and delete a customer
*RebillyRestApi.CustomersApi* | [**deleteCustomerLeadSource**](docs/CustomersApi.md#deleteCustomerLeadSource) | **DELETE** /customers/{id}/lead-source | Delete a Lead Source for a customer
*RebillyRestApi.CustomersApi* | [**getCustomer**](docs/CustomersApi.md#getCustomer) | **GET** /customers/{id} | Retrieve a customer
*RebillyRestApi.CustomersApi* | [**getCustomerCollection**](docs/CustomersApi.md#getCustomerCollection) | **GET** /customers | Retrieve a list of customers
*RebillyRestApi.CustomersApi* | [**getCustomerLeadSource**](docs/CustomersApi.md#getCustomerLeadSource) | **GET** /customers/{id}/lead-source | Retrieve a customer&#39;s Lead Source
*RebillyRestApi.CustomersApi* | [**postCustomer**](docs/CustomersApi.md#postCustomer) | **POST** /customers | Create a customer (without an ID)
*RebillyRestApi.CustomersApi* | [**postCustomerTimelineCustomEventType**](docs/CustomersApi.md#postCustomerTimelineCustomEventType) | **POST** /customer-timeline-custom-events | Create Customer Timeline custom event type
*RebillyRestApi.CustomersApi* | [**putCustomer**](docs/CustomersApi.md#putCustomer) | **PUT** /customers/{id} | Upsert a customer with predefined ID
*RebillyRestApi.CustomersApi* | [**putCustomerLeadSource**](docs/CustomersApi.md#putCustomerLeadSource) | **PUT** /customers/{id}/lead-source | Create a Lead Source for a customer
*RebillyRestApi.CustomersTimelineApi* | [**deleteCustomerTimeline**](docs/CustomersTimelineApi.md#deleteCustomerTimeline) | **DELETE** /customers/{id}/timeline/{messageId} | Delete a Customer Timeline message
*RebillyRestApi.CustomersTimelineApi* | [**getCustomerTimeline**](docs/CustomersTimelineApi.md#getCustomerTimeline) | **GET** /customers/{id}/timeline/{messageId} | Retrieve a customer Timeline message
*RebillyRestApi.CustomersTimelineApi* | [**getCustomerTimelineCollection**](docs/CustomersTimelineApi.md#getCustomerTimelineCollection) | **GET** /customers/{id}/timeline | Retrieve a list of customer timeline messages
*RebillyRestApi.CustomersTimelineApi* | [**getCustomerTimelineCustomEventType**](docs/CustomersTimelineApi.md#getCustomerTimelineCustomEventType) | **GET** /customer-timeline-custom-events/{id} | Retrieve customer timeline custom event type with specified identifier string
*RebillyRestApi.CustomersTimelineApi* | [**getCustomerTimelineCustomEventTypeCollection**](docs/CustomersTimelineApi.md#getCustomerTimelineCustomEventTypeCollection) | **GET** /customer-timeline-custom-events | Retrieve a list of customer timeline custom event types
*RebillyRestApi.CustomersTimelineApi* | [**getCustomerTimelineEventCollection**](docs/CustomersTimelineApi.md#getCustomerTimelineEventCollection) | **GET** /customer-timeline-events | Retrieve a list of customer timeline messages for all customers
*RebillyRestApi.CustomersTimelineApi* | [**postCustomerTimeline**](docs/CustomersTimelineApi.md#postCustomerTimeline) | **POST** /customers/{id}/timeline | Create a customer Timeline comment or custom defined event
*RebillyRestApi.DisputesApi* | [**getDispute**](docs/DisputesApi.md#getDispute) | **GET** /disputes/{id} | Retrieve a dispute
*RebillyRestApi.DisputesApi* | [**getDisputeCollection**](docs/DisputesApi.md#getDisputeCollection) | **GET** /disputes | Retrieve a list of disputes
*RebillyRestApi.DisputesApi* | [**postDispute**](docs/DisputesApi.md#postDispute) | **POST** /disputes | Create a dispute
*RebillyRestApi.DisputesApi* | [**putDispute**](docs/DisputesApi.md#putDispute) | **PUT** /disputes/{id} | Create or update a Dispute with predefined ID
*RebillyRestApi.FilesApi* | [**deleteAttachment**](docs/FilesApi.md#deleteAttachment) | **DELETE** /attachments/{id} | Delete an Attachment
*RebillyRestApi.FilesApi* | [**deleteFile**](docs/FilesApi.md#deleteFile) | **DELETE** /files/{id} | Delete a File
*RebillyRestApi.FilesApi* | [**getAttachment**](docs/FilesApi.md#getAttachment) | **GET** /attachments/{id} | Retrieve an Attachment
*RebillyRestApi.FilesApi* | [**getAttachmentCollection**](docs/FilesApi.md#getAttachmentCollection) | **GET** /attachments | Retrieve a list of Attachments
*RebillyRestApi.FilesApi* | [**getFile**](docs/FilesApi.md#getFile) | **GET** /files/{id} | Retrieve a File Record
*RebillyRestApi.FilesApi* | [**getFileCollection**](docs/FilesApi.md#getFileCollection) | **GET** /files | Retrieve a list of files
*RebillyRestApi.FilesApi* | [**getFileDownload**](docs/FilesApi.md#getFileDownload) | **GET** /files/{id}/download | Download a file
*RebillyRestApi.FilesApi* | [**getFileDownloadExtension**](docs/FilesApi.md#getFileDownloadExtension) | **GET** /files/{id}/download{extension} | Download image in specific format
*RebillyRestApi.FilesApi* | [**postAttachment**](docs/FilesApi.md#postAttachment) | **POST** /attachments | Create an Attachment
*RebillyRestApi.FilesApi* | [**postFile**](docs/FilesApi.md#postFile) | **POST** /files | Create a file
*RebillyRestApi.FilesApi* | [**putAttachment**](docs/FilesApi.md#putAttachment) | **PUT** /attachments/{id} | Update the Attachment with predefined ID
*RebillyRestApi.FilesApi* | [**putFile**](docs/FilesApi.md#putFile) | **PUT** /files/{id} | Update the File with predefined ID
*RebillyRestApi.InvoicesApi* | [**deleteInvoiceTimeline**](docs/InvoicesApi.md#deleteInvoiceTimeline) | **DELETE** /invoices/{id}/timeline/{messageId} | Delete an Invoice Timeline message
*RebillyRestApi.InvoicesApi* | [**getCustomerUpcomingInvoiceCollection**](docs/InvoicesApi.md#getCustomerUpcomingInvoiceCollection) | **GET** /customers/{id}/upcoming-invoices | Retrieve customer&#39;s upcoming invoices
*RebillyRestApi.InvoicesApi* | [**getInvoice**](docs/InvoicesApi.md#getInvoice) | **GET** /invoices/{id} | Retrieve an invoice
*RebillyRestApi.InvoicesApi* | [**getInvoiceCollection**](docs/InvoicesApi.md#getInvoiceCollection) | **GET** /invoices | Retrieve a list of invoices
*RebillyRestApi.InvoicesApi* | [**getInvoiceItemCollection**](docs/InvoicesApi.md#getInvoiceItemCollection) | **GET** /invoices/{id}/items | Retrieve invoice items
*RebillyRestApi.InvoicesApi* | [**getInvoiceTimeline**](docs/InvoicesApi.md#getInvoiceTimeline) | **GET** /invoices/{id}/timeline/{messageId} | Retrieve an Invoice Timeline message
*RebillyRestApi.InvoicesApi* | [**getInvoiceTimelineCollection**](docs/InvoicesApi.md#getInvoiceTimelineCollection) | **GET** /invoices/{id}/timeline | Retrieve a list of invoice timeline messages
*RebillyRestApi.InvoicesApi* | [**getInvoiceTransactionAllocationCollection**](docs/InvoicesApi.md#getInvoiceTransactionAllocationCollection) | **GET** /invoices/{id}/transaction-allocations | Get transaction amounts allocated to an invoice
*RebillyRestApi.InvoicesApi* | [**postInvoice**](docs/InvoicesApi.md#postInvoice) | **POST** /invoices | Create an invoice
*RebillyRestApi.InvoicesApi* | [**postInvoiceAbandonment**](docs/InvoicesApi.md#postInvoiceAbandonment) | **POST** /invoices/{id}/abandon | Abandon an invoice
*RebillyRestApi.InvoicesApi* | [**postInvoiceIssuance**](docs/InvoicesApi.md#postInvoiceIssuance) | **POST** /invoices/{id}/issue | Issue an invoice
*RebillyRestApi.InvoicesApi* | [**postInvoiceItem**](docs/InvoicesApi.md#postInvoiceItem) | **POST** /invoices/{id}/items | Create an invoice item
*RebillyRestApi.InvoicesApi* | [**postInvoiceRecalculation**](docs/InvoicesApi.md#postInvoiceRecalculation) | **POST** /invoices/{id}/recalculate | Recalculate an invoice
*RebillyRestApi.InvoicesApi* | [**postInvoiceReissuance**](docs/InvoicesApi.md#postInvoiceReissuance) | **POST** /invoices/{id}/reissue | Reissue an invoice
*RebillyRestApi.InvoicesApi* | [**postInvoiceTimeline**](docs/InvoicesApi.md#postInvoiceTimeline) | **POST** /invoices/{id}/timeline | Create an invoice Timeline comment
*RebillyRestApi.InvoicesApi* | [**postInvoiceTransaction**](docs/InvoicesApi.md#postInvoiceTransaction) | **POST** /invoices/{id}/transaction | Apply a transaction to an invoice
*RebillyRestApi.InvoicesApi* | [**postInvoiceVoid**](docs/InvoicesApi.md#postInvoiceVoid) | **POST** /invoices/{id}/void | Void an invoice
*RebillyRestApi.InvoicesApi* | [**putInvoice**](docs/InvoicesApi.md#putInvoice) | **PUT** /invoices/{id} | Create or update an invoice with predefined ID
*RebillyRestApi.KYCDocumentsApi* | [**deleteKycRequest**](docs/KYCDocumentsApi.md#deleteKycRequest) | **DELETE** /kyc-requests/{id} | Delete the KYC request
*RebillyRestApi.KYCDocumentsApi* | [**getKycDocument**](docs/KYCDocumentsApi.md#getKycDocument) | **GET** /kyc-documents/{id} | Retrieve a KYC Document
*RebillyRestApi.KYCDocumentsApi* | [**getKycDocumentCollection**](docs/KYCDocumentsApi.md#getKycDocumentCollection) | **GET** /kyc-documents | Retrieve a list of KYC documents
*RebillyRestApi.KYCDocumentsApi* | [**getKycRequest**](docs/KYCDocumentsApi.md#getKycRequest) | **GET** /kyc-requests/{id} | Retrieve a KYC request
*RebillyRestApi.KYCDocumentsApi* | [**getKycRequestCollection**](docs/KYCDocumentsApi.md#getKycRequestCollection) | **GET** /kyc-requests | Retrieve a list of KYC requests
*RebillyRestApi.KYCDocumentsApi* | [**patchKycRequest**](docs/KYCDocumentsApi.md#patchKycRequest) | **PATCH** /kyc-requests/{id} | Update a KYC request
*RebillyRestApi.KYCDocumentsApi* | [**postKycDocument**](docs/KYCDocumentsApi.md#postKycDocument) | **POST** /kyc-documents | Create a KYC Document
*RebillyRestApi.KYCDocumentsApi* | [**postKycDocumentAcceptance**](docs/KYCDocumentsApi.md#postKycDocumentAcceptance) | **POST** /kyc-documents/{id}/acceptance | Accept a KYC document
*RebillyRestApi.KYCDocumentsApi* | [**postKycDocumentMatches**](docs/KYCDocumentsApi.md#postKycDocumentMatches) | **POST** /kyc-documents/{id}/matches | Update a KYC document&#39;s documentMatches
*RebillyRestApi.KYCDocumentsApi* | [**postKycDocumentRejection**](docs/KYCDocumentsApi.md#postKycDocumentRejection) | **POST** /kyc-documents/{id}/rejection | Reject a KYC document
*RebillyRestApi.KYCDocumentsApi* | [**postKycDocumentReview**](docs/KYCDocumentsApi.md#postKycDocumentReview) | **POST** /kyc-documents/{id}/review | Review a KYC document
*RebillyRestApi.KYCDocumentsApi* | [**postKycRequest**](docs/KYCDocumentsApi.md#postKycRequest) | **POST** /kyc-requests | Create a KYC Request
*RebillyRestApi.KYCDocumentsApi* | [**putKycDocument**](docs/KYCDocumentsApi.md#putKycDocument) | **PUT** /kyc-documents/{id} | Create or update a KYC document with predefined ID
*RebillyRestApi.OrdersApi* | [**deleteSubscriptionCancellation**](docs/OrdersApi.md#deleteSubscriptionCancellation) | **DELETE** /subscription-cancellations/{id} | Delete a cancellation
*RebillyRestApi.OrdersApi* | [**deleteSubscriptionTimeline**](docs/OrdersApi.md#deleteSubscriptionTimeline) | **DELETE** /subscriptions/{id}/timeline/{messageId} | Delete an Order Timeline message
*RebillyRestApi.OrdersApi* | [**getSubscription**](docs/OrdersApi.md#getSubscription) | **GET** /subscriptions/{id} | Retrieve an order
*RebillyRestApi.OrdersApi* | [**getSubscriptionCancellation**](docs/OrdersApi.md#getSubscriptionCancellation) | **GET** /subscription-cancellations/{id} | Retrieve an order сancellation
*RebillyRestApi.OrdersApi* | [**getSubscriptionCancellationCollection**](docs/OrdersApi.md#getSubscriptionCancellationCollection) | **GET** /subscription-cancellations | Retrieve a list of cancellations
*RebillyRestApi.OrdersApi* | [**getSubscriptionCollection**](docs/OrdersApi.md#getSubscriptionCollection) | **GET** /subscriptions | Retrieve a list of orders
*RebillyRestApi.OrdersApi* | [**getSubscriptionReactivation**](docs/OrdersApi.md#getSubscriptionReactivation) | **GET** /subscription-reactivations/{id} | Retrieve an order reactivation
*RebillyRestApi.OrdersApi* | [**getSubscriptionReactivationCollection**](docs/OrdersApi.md#getSubscriptionReactivationCollection) | **GET** /subscription-reactivations | Retrieve a list of reactivations
*RebillyRestApi.OrdersApi* | [**getSubscriptionTimeline**](docs/OrdersApi.md#getSubscriptionTimeline) | **GET** /subscriptions/{id}/timeline/{messageId} | Retrieve an Order Timeline message
*RebillyRestApi.OrdersApi* | [**getSubscriptionTimelineCollection**](docs/OrdersApi.md#getSubscriptionTimelineCollection) | **GET** /subscriptions/{id}/timeline | Retrieve a list of order timeline messages
*RebillyRestApi.OrdersApi* | [**getSubscriptionUpcomingInvoiceCollection**](docs/OrdersApi.md#getSubscriptionUpcomingInvoiceCollection) | **GET** /subscriptions/{id}/upcoming-invoices | Retrieve subscription order&#39;s upcoming invoice
*RebillyRestApi.OrdersApi* | [**postSubscription**](docs/OrdersApi.md#postSubscription) | **POST** /subscriptions | Create an order
*RebillyRestApi.OrdersApi* | [**postSubscriptionCancellation**](docs/OrdersApi.md#postSubscriptionCancellation) | **POST** /subscription-cancellations | Cancel an order
*RebillyRestApi.OrdersApi* | [**postSubscriptionInterimInvoice**](docs/OrdersApi.md#postSubscriptionInterimInvoice) | **POST** /subscriptions/{id}/interim-invoice | Issue an interim invoice for a subscription order
*RebillyRestApi.OrdersApi* | [**postSubscriptionItemsChange**](docs/OrdersApi.md#postSubscriptionItemsChange) | **POST** /subscriptions/{id}/change-items | Change an order&#39;s items
*RebillyRestApi.OrdersApi* | [**postSubscriptionReactivation**](docs/OrdersApi.md#postSubscriptionReactivation) | **POST** /subscription-reactivations | Reactivate an order
*RebillyRestApi.OrdersApi* | [**postSubscriptionTimeline**](docs/OrdersApi.md#postSubscriptionTimeline) | **POST** /subscriptions/{id}/timeline | Create an order Timeline comment
*RebillyRestApi.OrdersApi* | [**postUpcomingInvoiceIssuance**](docs/OrdersApi.md#postUpcomingInvoiceIssuance) | **POST** /subscriptions/{id}/upcoming-invoices/{invoiceId}/issue | Issue an upcoming invoice for early pay
*RebillyRestApi.OrdersApi* | [**putSubscription**](docs/OrdersApi.md#putSubscription) | **PUT** /subscriptions/{id} | Upsert an order with predefined ID
*RebillyRestApi.OrdersApi* | [**putSubscriptionCancellation**](docs/OrdersApi.md#putSubscriptionCancellation) | **PUT** /subscription-cancellations/{id} | Cancel an order
*RebillyRestApi.PayPalAccountsApi* | [**getPayPalAccount**](docs/PayPalAccountsApi.md#getPayPalAccount) | **GET** /paypal-accounts/{id} | Retrieve a PayPal Account
*RebillyRestApi.PayPalAccountsApi* | [**getPayPalAccountCollection**](docs/PayPalAccountsApi.md#getPayPalAccountCollection) | **GET** /paypal-accounts | Retrieve a list of PayPal accounts
*RebillyRestApi.PayPalAccountsApi* | [**postPayPalAccount**](docs/PayPalAccountsApi.md#postPayPalAccount) | **POST** /paypal-accounts | Create a PayPal Account
*RebillyRestApi.PayPalAccountsApi* | [**postPayPalAccountDeactivation**](docs/PayPalAccountsApi.md#postPayPalAccountDeactivation) | **POST** /paypal-accounts/{id}/deactivation | Deactivate a PayPal Account
*RebillyRestApi.PayPalAccountsApi* | [**putPayPalAccount**](docs/PayPalAccountsApi.md#putPayPalAccount) | **PUT** /paypal-accounts/{id} | Create a PayPal account with predefined ID
*RebillyRestApi.PaymentCardsApi* | [**getPaymentCard**](docs/PaymentCardsApi.md#getPaymentCard) | **GET** /payment-cards/{id} | Retrieve a Payment Card
*RebillyRestApi.PaymentCardsApi* | [**getPaymentCardCollection**](docs/PaymentCardsApi.md#getPaymentCardCollection) | **GET** /payment-cards | Retrieve a list of Payment Cards
*RebillyRestApi.PaymentCardsApi* | [**patchPaymentCard**](docs/PaymentCardsApi.md#patchPaymentCard) | **PATCH** /payment-cards/{id} | Update a payment card&#39;s values
*RebillyRestApi.PaymentCardsApi* | [**postPaymentCard**](docs/PaymentCardsApi.md#postPaymentCard) | **POST** /payment-cards | Create a Payment Card
*RebillyRestApi.PaymentCardsApi* | [**postPaymentCardDeactivation**](docs/PaymentCardsApi.md#postPaymentCardDeactivation) | **POST** /payment-cards/{id}/deactivation | Deactivate a Payment Card
*RebillyRestApi.PaymentCardsApi* | [**putPaymentCard**](docs/PaymentCardsApi.md#putPaymentCard) | **PUT** /payment-cards/{id} | Create a payment card with predefined ID
*RebillyRestApi.PaymentInstrumentsApi* | [**getPaymentInstrument**](docs/PaymentInstrumentsApi.md#getPaymentInstrument) | **GET** /payment-instruments/{id} | Retrieve a Payment Instrument
*RebillyRestApi.PaymentInstrumentsApi* | [**getPaymentInstrumentCollection**](docs/PaymentInstrumentsApi.md#getPaymentInstrumentCollection) | **GET** /payment-instruments | Retrieve a list of payment instruments
*RebillyRestApi.PaymentInstrumentsApi* | [**patchPaymentInstrument**](docs/PaymentInstrumentsApi.md#patchPaymentInstrument) | **PATCH** /payment-instruments/{id} | Update a Payment Instrument&#39;s values
*RebillyRestApi.PaymentInstrumentsApi* | [**postPaymentInstrument**](docs/PaymentInstrumentsApi.md#postPaymentInstrument) | **POST** /payment-instruments | Create a Payment Instrument
*RebillyRestApi.PaymentInstrumentsApi* | [**postPaymentInstrumentDeactivation**](docs/PaymentInstrumentsApi.md#postPaymentInstrumentDeactivation) | **POST** /payment-instruments/{id}/deactivation | Deactivate a payment instrument
*RebillyRestApi.PaymentTokensApi* | [**getToken**](docs/PaymentTokensApi.md#getToken) | **GET** /tokens/{token} | Retrieve a token
*RebillyRestApi.PaymentTokensApi* | [**getTokenCollection**](docs/PaymentTokensApi.md#getTokenCollection) | **GET** /tokens | Retrieve a list of tokens
*RebillyRestApi.PaymentTokensApi* | [**postDigitalWalletValidation**](docs/PaymentTokensApi.md#postDigitalWalletValidation) | **POST** /digital-wallets/validation | Validate a digital wallet session
*RebillyRestApi.PaymentTokensApi* | [**postToken**](docs/PaymentTokensApi.md#postToken) | **POST** /tokens | Create a payment token
*RebillyRestApi.PlansApi* | [**deletePlan**](docs/PlansApi.md#deletePlan) | **DELETE** /plans/{id} | Delete a Plan
*RebillyRestApi.PlansApi* | [**getPlan**](docs/PlansApi.md#getPlan) | **GET** /plans/{id} | Retrieve a plan
*RebillyRestApi.PlansApi* | [**getPlanCollection**](docs/PlansApi.md#getPlanCollection) | **GET** /plans | Retrieve a list of plans
*RebillyRestApi.PlansApi* | [**postPlan**](docs/PlansApi.md#postPlan) | **POST** /plans | Create a plan
*RebillyRestApi.PlansApi* | [**putPlan**](docs/PlansApi.md#putPlan) | **PUT** /plans/{id} | Create or update a Plan with predefined ID
*RebillyRestApi.ProductsApi* | [**deleteProduct**](docs/ProductsApi.md#deleteProduct) | **DELETE** /products/{id} | Delete a product
*RebillyRestApi.ProductsApi* | [**getProduct**](docs/ProductsApi.md#getProduct) | **GET** /products/{id} | Retrieve a product
*RebillyRestApi.ProductsApi* | [**getProductCollection**](docs/ProductsApi.md#getProductCollection) | **GET** /products | Retrieve a list of products
*RebillyRestApi.ProductsApi* | [**postProduct**](docs/ProductsApi.md#postProduct) | **POST** /products | Create a Product
*RebillyRestApi.ProductsApi* | [**putProduct**](docs/ProductsApi.md#putProduct) | **PUT** /products/{id} | Create a product with predefined ID
*RebillyRestApi.SearchApi* | [**getSearch**](docs/SearchApi.md#getSearch) | **GET** /search | Search merchant data
*RebillyRestApi.ShippingZonesApi* | [**deleteShippingZone**](docs/ShippingZonesApi.md#deleteShippingZone) | **DELETE** /shipping-zones/{id} | Delete a shipping zone
*RebillyRestApi.ShippingZonesApi* | [**getShippingZone**](docs/ShippingZonesApi.md#getShippingZone) | **GET** /shipping-zones/{id} | Retrieve a shipping zone
*RebillyRestApi.ShippingZonesApi* | [**getShippingZoneCollection**](docs/ShippingZonesApi.md#getShippingZoneCollection) | **GET** /shipping-zones | Retrieve a list of shipping zones
*RebillyRestApi.ShippingZonesApi* | [**postShippingZone**](docs/ShippingZonesApi.md#postShippingZone) | **POST** /shipping-zones | Create a Shipping Zone
*RebillyRestApi.ShippingZonesApi* | [**putShippingZone**](docs/ShippingZonesApi.md#putShippingZone) | **PUT** /shipping-zones/{id} | Create a shipping zone with predefined ID
*RebillyRestApi.TagsApi* | [**deleteTag**](docs/TagsApi.md#deleteTag) | **DELETE** /tags/{tag} | Delete a tag
*RebillyRestApi.TagsApi* | [**deleteTagCustomer**](docs/TagsApi.md#deleteTagCustomer) | **DELETE** /tags/{tag}/customers/{customerId} | Untag a customer
*RebillyRestApi.TagsApi* | [**deleteTagCustomerCollection**](docs/TagsApi.md#deleteTagCustomerCollection) | **DELETE** /tags/{tag}/customers | Untag a list of customers
*RebillyRestApi.TagsApi* | [**getTag**](docs/TagsApi.md#getTag) | **GET** /tags/{tag} | Retrieve a tag
*RebillyRestApi.TagsApi* | [**getTagCollection**](docs/TagsApi.md#getTagCollection) | **GET** /tags | Retrieve a list of tags
*RebillyRestApi.TagsApi* | [**patchTag**](docs/TagsApi.md#patchTag) | **PATCH** /tags/{tag} | Update a tag
*RebillyRestApi.TagsApi* | [**postTag**](docs/TagsApi.md#postTag) | **POST** /tags | Create a tag
*RebillyRestApi.TagsApi* | [**postTagCustomer**](docs/TagsApi.md#postTagCustomer) | **POST** /tags/{tag}/customers/{customerId} | Tag a customer
*RebillyRestApi.TagsApi* | [**postTagCustomerCollection**](docs/TagsApi.md#postTagCustomerCollection) | **POST** /tags/{tag}/customers | Tag a list of customers
*RebillyRestApi.TransactionsApi* | [**deleteTransactionTimeline**](docs/TransactionsApi.md#deleteTransactionTimeline) | **DELETE** /transactions/{id}/timeline/{messageId} | Delete a Transaction Timeline message
*RebillyRestApi.TransactionsApi* | [**getTransaction**](docs/TransactionsApi.md#getTransaction) | **GET** /transactions/{id} | Retrieve a Transaction
*RebillyRestApi.TransactionsApi* | [**getTransactionCollection**](docs/TransactionsApi.md#getTransactionCollection) | **GET** /transactions | Retrieve a list of transactions
*RebillyRestApi.TransactionsApi* | [**getTransactionTimeline**](docs/TransactionsApi.md#getTransactionTimeline) | **GET** /transactions/{id}/timeline/{messageId} | Retrieve a transaction Timeline message
*RebillyRestApi.TransactionsApi* | [**getTransactionTimelineCollection**](docs/TransactionsApi.md#getTransactionTimelineCollection) | **GET** /transactions/{id}/timeline | Retrieve a list of transaction timeline messages
*RebillyRestApi.TransactionsApi* | [**patchTransaction**](docs/TransactionsApi.md#patchTransaction) | **PATCH** /transactions/{id} | Update a transaction
*RebillyRestApi.TransactionsApi* | [**postPayout**](docs/TransactionsApi.md#postPayout) | **POST** /payouts | Create a credit transaction
*RebillyRestApi.TransactionsApi* | [**postReadyToPay**](docs/TransactionsApi.md#postReadyToPay) | **POST** /ready-to-pay | Ready to Pay
*RebillyRestApi.TransactionsApi* | [**postTransaction**](docs/TransactionsApi.md#postTransaction) | **POST** /transactions | Create a transaction
*RebillyRestApi.TransactionsApi* | [**postTransactionQuery**](docs/TransactionsApi.md#postTransactionQuery) | **POST** /transactions/{id}/query | Query a Transaction
*RebillyRestApi.TransactionsApi* | [**postTransactionRefund**](docs/TransactionsApi.md#postTransactionRefund) | **POST** /transactions/{id}/refund | Refund a Transaction
*RebillyRestApi.TransactionsApi* | [**postTransactionTimeline**](docs/TransactionsApi.md#postTransactionTimeline) | **POST** /transactions/{id}/timeline | Create a transaction Timeline comment
*RebillyRestApi.TransactionsApi* | [**postTransactionUpdate**](docs/TransactionsApi.md#postTransactionUpdate) | **POST** /transactions/{id}/update | Update a Transaction status


## Documentation for Models

 - [RebillyRestApi.A1Gateway](docs/A1Gateway.md)
 - [RebillyRestApi.A1Gateway3dsServers](docs/A1Gateway3dsServers.md)
 - [RebillyRestApi.A1GatewayAllOfCredentials](docs/A1GatewayAllOfCredentials.md)
 - [RebillyRestApi.AML](docs/AML.md)
 - [RebillyRestApi.AMLAddressInner](docs/AMLAddressInner.md)
 - [RebillyRestApi.AMLAliasesInner](docs/AMLAliasesInner.md)
 - [RebillyRestApi.AMLPassportInner](docs/AMLPassportInner.md)
 - [RebillyRestApi.AchPlaidFeature](docs/AchPlaidFeature.md)
 - [RebillyRestApi.AclInner](docs/AclInner.md)
 - [RebillyRestApi.AcquirerName](docs/AcquirerName.md)
 - [RebillyRestApi.AddressMatches](docs/AddressMatches.md)
 - [RebillyRestApi.Adyen](docs/Adyen.md)
 - [RebillyRestApi.AdyenAllOfCredentials](docs/AdyenAllOfCredentials.md)
 - [RebillyRestApi.AdyenAllOfSettings](docs/AdyenAllOfSettings.md)
 - [RebillyRestApi.Airpay](docs/Airpay.md)
 - [RebillyRestApi.AirpayAllOfCredentials](docs/AirpayAllOfCredentials.md)
 - [RebillyRestApi.AlternativePaymentInstrument](docs/AlternativePaymentInstrument.md)
 - [RebillyRestApi.AlternativePaymentInstrument2](docs/AlternativePaymentInstrument2.md)
 - [RebillyRestApi.AlternativePaymentInstrument2EmbeddedInner](docs/AlternativePaymentInstrument2EmbeddedInner.md)
 - [RebillyRestApi.AlternativePaymentInstrument2LinksInner](docs/AlternativePaymentInstrument2LinksInner.md)
 - [RebillyRestApi.AlternativePaymentMethods](docs/AlternativePaymentMethods.md)
 - [RebillyRestApi.AlternativePaymentToken](docs/AlternativePaymentToken.md)
 - [RebillyRestApi.AmexVPC](docs/AmexVPC.md)
 - [RebillyRestApi.AmexVPCAllOfCredentials](docs/AmexVPCAllOfCredentials.md)
 - [RebillyRestApi.AmexVPCAllOfSettings](docs/AmexVPCAllOfSettings.md)
 - [RebillyRestApi.AmountAdjustment](docs/AmountAdjustment.md)
 - [RebillyRestApi.ApcoPay](docs/ApcoPay.md)
 - [RebillyRestApi.ApcoPayAllOfCredentials](docs/ApcoPayAllOfCredentials.md)
 - [RebillyRestApi.ApcoPayAllOfSettings](docs/ApcoPayAllOfSettings.md)
 - [RebillyRestApi.ApiKeyScope](docs/ApiKeyScope.md)
 - [RebillyRestApi.ApplePayValidation](docs/ApplePayValidation.md)
 - [RebillyRestApi.ApplePayValidationAllOfValidationRequest](docs/ApplePayValidationAllOfValidationRequest.md)
 - [RebillyRestApi.ApprovalUrlLink](docs/ApprovalUrlLink.md)
 - [RebillyRestApi.AsiaPaymentGateway](docs/AsiaPaymentGateway.md)
 - [RebillyRestApi.AsiaPaymentGatewayAllOfCredentials](docs/AsiaPaymentGatewayAllOfCredentials.md)
 - [RebillyRestApi.AstroPayCard](docs/AstroPayCard.md)
 - [RebillyRestApi.AstroPayCardAllOfCredentials](docs/AstroPayCardAllOfCredentials.md)
 - [RebillyRestApi.AstroPayCardAllOfSettings](docs/AstroPayCardAllOfSettings.md)
 - [RebillyRestApi.Attachment](docs/Attachment.md)
 - [RebillyRestApi.AttachmentEmbeddedInner](docs/AttachmentEmbeddedInner.md)
 - [RebillyRestApi.AttachmentLinksInner](docs/AttachmentLinksInner.md)
 - [RebillyRestApi.AttachmentResourceLink](docs/AttachmentResourceLink.md)
 - [RebillyRestApi.AuthTransactionEmbed](docs/AuthTransactionEmbed.md)
 - [RebillyRestApi.AuthTransactionLink](docs/AuthTransactionLink.md)
 - [RebillyRestApi.AuthenticationOptions](docs/AuthenticationOptions.md)
 - [RebillyRestApi.AuthenticationToken](docs/AuthenticationToken.md)
 - [RebillyRestApi.AuthenticationTokenMetadata](docs/AuthenticationTokenMetadata.md)
 - [RebillyRestApi.AuthorizeNet](docs/AuthorizeNet.md)
 - [RebillyRestApi.AuthorizeNetAllOfCredentials](docs/AuthorizeNetAllOfCredentials.md)
 - [RebillyRestApi.Auto](docs/Auto.md)
 - [RebillyRestApi.BBANInstrument](docs/BBANInstrument.md)
 - [RebillyRestApi.BBANType](docs/BBANType.md)
 - [RebillyRestApi.Bambora](docs/Bambora.md)
 - [RebillyRestApi.BamboraAllOfCredentials](docs/BamboraAllOfCredentials.md)
 - [RebillyRestApi.BankAccount](docs/BankAccount.md)
 - [RebillyRestApi.BankAccountAllOfEmbedded](docs/BankAccountAllOfEmbedded.md)
 - [RebillyRestApi.BankAccountAllOfLinks](docs/BankAccountAllOfLinks.md)
 - [RebillyRestApi.BankAccountCreatePlain](docs/BankAccountCreatePlain.md)
 - [RebillyRestApi.BankAccountCreateToken](docs/BankAccountCreateToken.md)
 - [RebillyRestApi.BankAccountEmbed](docs/BankAccountEmbed.md)
 - [RebillyRestApi.BankAccountInstrument](docs/BankAccountInstrument.md)
 - [RebillyRestApi.BankAccountToken](docs/BankAccountToken.md)
 - [RebillyRestApi.BankAccountUpdatePlain](docs/BankAccountUpdatePlain.md)
 - [RebillyRestApi.BitPay](docs/BitPay.md)
 - [RebillyRestApi.BitPayAllOfCredentials](docs/BitPayAllOfCredentials.md)
 - [RebillyRestApi.BlankProblem](docs/BlankProblem.md)
 - [RebillyRestApi.Blocklist](docs/Blocklist.md)
 - [RebillyRestApi.BlueSnap](docs/BlueSnap.md)
 - [RebillyRestApi.BlueSnapAllOfCredentials](docs/BlueSnapAllOfCredentials.md)
 - [RebillyRestApi.BraintreePayments](docs/BraintreePayments.md)
 - [RebillyRestApi.BraintreePaymentsAllOfCredentials](docs/BraintreePaymentsAllOfCredentials.md)
 - [RebillyRestApi.BrowserData](docs/BrowserData.md)
 - [RebillyRestApi.CASHlib](docs/CASHlib.md)
 - [RebillyRestApi.CASHlibAllOfCredentials](docs/CASHlibAllOfCredentials.md)
 - [RebillyRestApi.CCAvenue](docs/CCAvenue.md)
 - [RebillyRestApi.CCAvenueAllOfCredentials](docs/CCAvenueAllOfCredentials.md)
 - [RebillyRestApi.CODVoucher](docs/CODVoucher.md)
 - [RebillyRestApi.CODVoucherAllOfCredentials](docs/CODVoucherAllOfCredentials.md)
 - [RebillyRestApi.CardinalCommerce3dsServer](docs/CardinalCommerce3dsServer.md)
 - [RebillyRestApi.Cardknox](docs/Cardknox.md)
 - [RebillyRestApi.CardknoxAllOfCredentials](docs/CardknoxAllOfCredentials.md)
 - [RebillyRestApi.CashInstrument](docs/CashInstrument.md)
 - [RebillyRestApi.CashToCode](docs/CashToCode.md)
 - [RebillyRestApi.CashToCodeAllOfCredentials](docs/CashToCodeAllOfCredentials.md)
 - [RebillyRestApi.CashToCodeAllOfSettings](docs/CashToCodeAllOfSettings.md)
 - [RebillyRestApi.Cashflows](docs/Cashflows.md)
 - [RebillyRestApi.CashflowsAllOfCredentials](docs/CashflowsAllOfCredentials.md)
 - [RebillyRestApi.CauriPayment](docs/CauriPayment.md)
 - [RebillyRestApi.CauriPaymentAllOfCredentials](docs/CauriPaymentAllOfCredentials.md)
 - [RebillyRestApi.Cayan](docs/Cayan.md)
 - [RebillyRestApi.CayanAllOfCredentials](docs/CayanAllOfCredentials.md)
 - [RebillyRestApi.Chase](docs/Chase.md)
 - [RebillyRestApi.ChaseAllOfCredentials](docs/ChaseAllOfCredentials.md)
 - [RebillyRestApi.CheckInstrument](docs/CheckInstrument.md)
 - [RebillyRestApi.Circle](docs/Circle.md)
 - [RebillyRestApi.CircleAllOfCredentials](docs/CircleAllOfCredentials.md)
 - [RebillyRestApi.Citadel](docs/Citadel.md)
 - [RebillyRestApi.CitadelAllOfCredentials](docs/CitadelAllOfCredentials.md)
 - [RebillyRestApi.Clearhaus](docs/Clearhaus.md)
 - [RebillyRestApi.Clearhaus3dsServer](docs/Clearhaus3dsServer.md)
 - [RebillyRestApi.Clearhaus3dsServers](docs/Clearhaus3dsServers.md)
 - [RebillyRestApi.ClearhausAllOfCredentials](docs/ClearhausAllOfCredentials.md)
 - [RebillyRestApi.CoinPayments](docs/CoinPayments.md)
 - [RebillyRestApi.CoinPaymentsAllOfCredentials](docs/CoinPaymentsAllOfCredentials.md)
 - [RebillyRestApi.CommonBankAccount](docs/CommonBankAccount.md)
 - [RebillyRestApi.CommonInvoice](docs/CommonInvoice.md)
 - [RebillyRestApi.CommonKycDocument](docs/CommonKycDocument.md)
 - [RebillyRestApi.CommonKycDocumentLinksInner](docs/CommonKycDocumentLinksInner.md)
 - [RebillyRestApi.CommonKycRequest](docs/CommonKycRequest.md)
 - [RebillyRestApi.CommonKycRequestDocumentsInner](docs/CommonKycRequestDocumentsInner.md)
 - [RebillyRestApi.CommonOneTimeOrder](docs/CommonOneTimeOrder.md)
 - [RebillyRestApi.CommonPayPalAccount](docs/CommonPayPalAccount.md)
 - [RebillyRestApi.CommonPaymentCard](docs/CommonPaymentCard.md)
 - [RebillyRestApi.CommonPaymentToken](docs/CommonPaymentToken.md)
 - [RebillyRestApi.CommonPlan](docs/CommonPlan.md)
 - [RebillyRestApi.CommonPlanRecurringInterval](docs/CommonPlanRecurringInterval.md)
 - [RebillyRestApi.CommonPlanSetup](docs/CommonPlanSetup.md)
 - [RebillyRestApi.CommonPlanTrial](docs/CommonPlanTrial.md)
 - [RebillyRestApi.CommonProduct](docs/CommonProduct.md)
 - [RebillyRestApi.CommonScheduleInstruction](docs/CommonScheduleInstruction.md)
 - [RebillyRestApi.CommonSubscription](docs/CommonSubscription.md)
 - [RebillyRestApi.CommonSubscriptionItemsInner](docs/CommonSubscriptionItemsInner.md)
 - [RebillyRestApi.CommonSubscriptionOrder](docs/CommonSubscriptionOrder.md)
 - [RebillyRestApi.CommonSubscriptionOrderAllOfLineItemSubtotal](docs/CommonSubscriptionOrderAllOfLineItemSubtotal.md)
 - [RebillyRestApi.CommonSubscriptionOrderAllOfRecurringInterval](docs/CommonSubscriptionOrderAllOfRecurringInterval.md)
 - [RebillyRestApi.CommonSubscriptionOrderAllOfTrial](docs/CommonSubscriptionOrderAllOfTrial.md)
 - [RebillyRestApi.CommonTransaction](docs/CommonTransaction.md)
 - [RebillyRestApi.CommonTransactionRequest](docs/CommonTransactionRequest.md)
 - [RebillyRestApi.CompositeToken](docs/CompositeToken.md)
 - [RebillyRestApi.Conekta](docs/Conekta.md)
 - [RebillyRestApi.ConektaAllOfCredentials](docs/ConektaAllOfCredentials.md)
 - [RebillyRestApi.ContactEmailsInner](docs/ContactEmailsInner.md)
 - [RebillyRestApi.ContactObject](docs/ContactObject.md)
 - [RebillyRestApi.ContactPhoneNumbersInner](docs/ContactPhoneNumbersInner.md)
 - [RebillyRestApi.Coppr](docs/Coppr.md)
 - [RebillyRestApi.CopprAllOfCredentials](docs/CopprAllOfCredentials.md)
 - [RebillyRestApi.CopprAllOfSettings](docs/CopprAllOfSettings.md)
 - [RebillyRestApi.CoreReadyToPay](docs/CoreReadyToPay.md)
 - [RebillyRestApi.Coupon](docs/Coupon.md)
 - [RebillyRestApi.CouponExpiration](docs/CouponExpiration.md)
 - [RebillyRestApi.CouponRedemption](docs/CouponRedemption.md)
 - [RebillyRestApi.CouponRestriction](docs/CouponRestriction.md)
 - [RebillyRestApi.Credential](docs/Credential.md)
 - [RebillyRestApi.Credorax](docs/Credorax.md)
 - [RebillyRestApi.CredoraxAllOfCredentials](docs/CredoraxAllOfCredentials.md)
 - [RebillyRestApi.Cryptonator](docs/Cryptonator.md)
 - [RebillyRestApi.CryptonatorAllOfCredentials](docs/CryptonatorAllOfCredentials.md)
 - [RebillyRestApi.CustomEventScheduleInstruction](docs/CustomEventScheduleInstruction.md)
 - [RebillyRestApi.CustomField](docs/CustomField.md)
 - [RebillyRestApi.Customer](docs/Customer.md)
 - [RebillyRestApi.CustomerAverageValue](docs/CustomerAverageValue.md)
 - [RebillyRestApi.CustomerEmbed](docs/CustomerEmbed.md)
 - [RebillyRestApi.CustomerEmbeddedInner](docs/CustomerEmbeddedInner.md)
 - [RebillyRestApi.CustomerJWT](docs/CustomerJWT.md)
 - [RebillyRestApi.CustomerLifetimeRevenue](docs/CustomerLifetimeRevenue.md)
 - [RebillyRestApi.CustomerLink](docs/CustomerLink.md)
 - [RebillyRestApi.CustomerLinksInner](docs/CustomerLinksInner.md)
 - [RebillyRestApi.CustomerTimeline](docs/CustomerTimeline.md)
 - [RebillyRestApi.CustomerTimelineCustomEvent](docs/CustomerTimelineCustomEvent.md)
 - [RebillyRestApi.CyberSource](docs/CyberSource.md)
 - [RebillyRestApi.CyberSourceAllOfCredentials](docs/CyberSourceAllOfCredentials.md)
 - [RebillyRestApi.DLocal](docs/DLocal.md)
 - [RebillyRestApi.DLocalAllOfCredentials](docs/DLocalAllOfCredentials.md)
 - [RebillyRestApi.DLocalAllOfSettings](docs/DLocalAllOfSettings.md)
 - [RebillyRestApi.DataCash](docs/DataCash.md)
 - [RebillyRestApi.DataCash3dsServer](docs/DataCash3dsServer.md)
 - [RebillyRestApi.DataCash3dsServers](docs/DataCash3dsServers.md)
 - [RebillyRestApi.DataCashAllOfCredentials](docs/DataCashAllOfCredentials.md)
 - [RebillyRestApi.DataCashAllOfSettings](docs/DataCashAllOfSettings.md)
 - [RebillyRestApi.DateInterval](docs/DateInterval.md)
 - [RebillyRestApi.DateIntervalAllOfUnit](docs/DateIntervalAllOfUnit.md)
 - [RebillyRestApi.DayOfMonth](docs/DayOfMonth.md)
 - [RebillyRestApi.DayOfWeek](docs/DayOfWeek.md)
 - [RebillyRestApi.DayOfWeekLong](docs/DayOfWeekLong.md)
 - [RebillyRestApi.DefaultPaymentInstrumentLink](docs/DefaultPaymentInstrumentLink.md)
 - [RebillyRestApi.Dengi](docs/Dengi.md)
 - [RebillyRestApi.DengiAllOfCredentials](docs/DengiAllOfCredentials.md)
 - [RebillyRestApi.DetailedProblem](docs/DetailedProblem.md)
 - [RebillyRestApi.DigitalWalletToken](docs/DigitalWalletToken.md)
 - [RebillyRestApi.DigitalWalletValidation](docs/DigitalWalletValidation.md)
 - [RebillyRestApi.DigitalWallets](docs/DigitalWallets.md)
 - [RebillyRestApi.DigitalWalletsApplePay](docs/DigitalWalletsApplePay.md)
 - [RebillyRestApi.DigitalWalletsGooglePay](docs/DigitalWalletsGooglePay.md)
 - [RebillyRestApi.Directa24](docs/Directa24.md)
 - [RebillyRestApi.Directa24AllOfCredentials](docs/Directa24AllOfCredentials.md)
 - [RebillyRestApi.Directa24AllOfSettings](docs/Directa24AllOfSettings.md)
 - [RebillyRestApi.Directa24Banks](docs/Directa24Banks.md)
 - [RebillyRestApi.Discount](docs/Discount.md)
 - [RebillyRestApi.DiscountsPerRedemption](docs/DiscountsPerRedemption.md)
 - [RebillyRestApi.Dispute](docs/Dispute.md)
 - [RebillyRestApi.DisputeEmbeddedInner](docs/DisputeEmbeddedInner.md)
 - [RebillyRestApi.DisputeLink](docs/DisputeLink.md)
 - [RebillyRestApi.DisputeLinksInner](docs/DisputeLinksInner.md)
 - [RebillyRestApi.DocumentedProblem](docs/DocumentedProblem.md)
 - [RebillyRestApi.Dragonphoenix](docs/Dragonphoenix.md)
 - [RebillyRestApi.DragonphoenixAllOfCredentials](docs/DragonphoenixAllOfCredentials.md)
 - [RebillyRestApi.DueTimeShiftInstruction](docs/DueTimeShiftInstruction.md)
 - [RebillyRestApi.DueTimeShiftInstructionUnit](docs/DueTimeShiftInstructionUnit.md)
 - [RebillyRestApi.DynamicIpnLink](docs/DynamicIpnLink.md)
 - [RebillyRestApi.EBANX](docs/EBANX.md)
 - [RebillyRestApi.EBANXAllOfCredentials](docs/EBANXAllOfCredentials.md)
 - [RebillyRestApi.EMS](docs/EMS.md)
 - [RebillyRestApi.EMS3dsServers](docs/EMS3dsServers.md)
 - [RebillyRestApi.EMSAllOfCredentials](docs/EMSAllOfCredentials.md)
 - [RebillyRestApi.EMSAllOfSettings](docs/EMSAllOfSettings.md)
 - [RebillyRestApi.EMerchantPay](docs/EMerchantPay.md)
 - [RebillyRestApi.EMerchantPay3dsServer](docs/EMerchantPay3dsServer.md)
 - [RebillyRestApi.EMerchantPay3dsServers](docs/EMerchantPay3dsServers.md)
 - [RebillyRestApi.EMerchantPayAllOfCredentials](docs/EMerchantPayAllOfCredentials.md)
 - [RebillyRestApi.EMerchantPayAllOfSettings](docs/EMerchantPayAllOfSettings.md)
 - [RebillyRestApi.EPG](docs/EPG.md)
 - [RebillyRestApi.EPGAllOfCredentials](docs/EPGAllOfCredentials.md)
 - [RebillyRestApi.EPro](docs/EPro.md)
 - [RebillyRestApi.EProAllOfCredentials](docs/EProAllOfCredentials.md)
 - [RebillyRestApi.EZeeWallet](docs/EZeeWallet.md)
 - [RebillyRestApi.EZeeWalletAllOfCredentials](docs/EZeeWalletAllOfCredentials.md)
 - [RebillyRestApi.EcoPayz](docs/EcoPayz.md)
 - [RebillyRestApi.EcoPayzAllOfCredentials](docs/EcoPayzAllOfCredentials.md)
 - [RebillyRestApi.EcoPayzAllOfSettings](docs/EcoPayzAllOfSettings.md)
 - [RebillyRestApi.EcorePay](docs/EcorePay.md)
 - [RebillyRestApi.EcorePayAllOfCredentials](docs/EcorePayAllOfCredentials.md)
 - [RebillyRestApi.Elavon](docs/Elavon.md)
 - [RebillyRestApi.ElavonAllOfCredentials](docs/ElavonAllOfCredentials.md)
 - [RebillyRestApi.Error](docs/Error.md)
 - [RebillyRestApi.Euteller](docs/Euteller.md)
 - [RebillyRestApi.EutellerAllOfCredentials](docs/EutellerAllOfCredentials.md)
 - [RebillyRestApi.EzyEFT](docs/EzyEFT.md)
 - [RebillyRestApi.EzyEFTAllOfCredentials](docs/EzyEFTAllOfCredentials.md)
 - [RebillyRestApi.File](docs/File.md)
 - [RebillyRestApi.FileCreateFromInline](docs/FileCreateFromInline.md)
 - [RebillyRestApi.FileCreateFromUrl](docs/FileCreateFromUrl.md)
 - [RebillyRestApi.FileDownloadLink](docs/FileDownloadLink.md)
 - [RebillyRestApi.FileEmbed](docs/FileEmbed.md)
 - [RebillyRestApi.FileLink](docs/FileLink.md)
 - [RebillyRestApi.FileLinksInner](docs/FileLinksInner.md)
 - [RebillyRestApi.FinTecSystems](docs/FinTecSystems.md)
 - [RebillyRestApi.FinTecSystemsAllOfCredentials](docs/FinTecSystemsAllOfCredentials.md)
 - [RebillyRestApi.FinTecSystemsAllOfSettings](docs/FinTecSystemsAllOfSettings.md)
 - [RebillyRestApi.Finrax](docs/Finrax.md)
 - [RebillyRestApi.FinraxAllOfCredentials](docs/FinraxAllOfCredentials.md)
 - [RebillyRestApi.FinraxAllOfSettings](docs/FinraxAllOfSettings.md)
 - [RebillyRestApi.Fixed](docs/Fixed.md)
 - [RebillyRestApi.FixedFee](docs/FixedFee.md)
 - [RebillyRestApi.FlatRate](docs/FlatRate.md)
 - [RebillyRestApi.Flexepin](docs/Flexepin.md)
 - [RebillyRestApi.FlexepinAllOfCredentials](docs/FlexepinAllOfCredentials.md)
 - [RebillyRestApi.FlexiblePlan](docs/FlexiblePlan.md)
 - [RebillyRestApi.Forte](docs/Forte.md)
 - [RebillyRestApi.ForteAllOfCredentials](docs/ForteAllOfCredentials.md)
 - [RebillyRestApi.FundSend](docs/FundSend.md)
 - [RebillyRestApi.FundSendAllOfCredentials](docs/FundSendAllOfCredentials.md)
 - [RebillyRestApi.GET](docs/GET.md)
 - [RebillyRestApi.GET3dsServers](docs/GET3dsServers.md)
 - [RebillyRestApi.GETAllOfCredentials](docs/GETAllOfCredentials.md)
 - [RebillyRestApi.GatewayAccount](docs/GatewayAccount.md)
 - [RebillyRestApi.GatewayAccountEmbed](docs/GatewayAccountEmbed.md)
 - [RebillyRestApi.GatewayAccountLimit](docs/GatewayAccountLimit.md)
 - [RebillyRestApi.GatewayAccountLimitLink](docs/GatewayAccountLimitLink.md)
 - [RebillyRestApi.GatewayAccountLink](docs/GatewayAccountLink.md)
 - [RebillyRestApi.GatewayAccountLinksInner](docs/GatewayAccountLinksInner.md)
 - [RebillyRestApi.GatewayName](docs/GatewayName.md)
 - [RebillyRestApi.Gigadat](docs/Gigadat.md)
 - [RebillyRestApi.GigadatAllOfCredentials](docs/GigadatAllOfCredentials.md)
 - [RebillyRestApi.GigadatAllOfSettings](docs/GigadatAllOfSettings.md)
 - [RebillyRestApi.GlobalOne](docs/GlobalOne.md)
 - [RebillyRestApi.GlobalOneAllOfCredentials](docs/GlobalOneAllOfCredentials.md)
 - [RebillyRestApi.GlobalWebhookEventType](docs/GlobalWebhookEventType.md)
 - [RebillyRestApi.Gooney](docs/Gooney.md)
 - [RebillyRestApi.GooneyAllOfCredentials](docs/GooneyAllOfCredentials.md)
 - [RebillyRestApi.Gpaysafe](docs/Gpaysafe.md)
 - [RebillyRestApi.GpaysafeAllOfCredentials](docs/GpaysafeAllOfCredentials.md)
 - [RebillyRestApi.Greenbox](docs/Greenbox.md)
 - [RebillyRestApi.GreenboxAllOfCredentials](docs/GreenboxAllOfCredentials.md)
 - [RebillyRestApi.HiPay](docs/HiPay.md)
 - [RebillyRestApi.HiPayAllOfCredentials](docs/HiPayAllOfCredentials.md)
 - [RebillyRestApi.IBANInstrument](docs/IBANInstrument.md)
 - [RebillyRestApi.IBANType](docs/IBANType.md)
 - [RebillyRestApi.ICEPAY](docs/ICEPAY.md)
 - [RebillyRestApi.ICEPAYAllOfCredentials](docs/ICEPAYAllOfCredentials.md)
 - [RebillyRestApi.ICanPay](docs/ICanPay.md)
 - [RebillyRestApi.ICanPayAllOfCredentials](docs/ICanPayAllOfCredentials.md)
 - [RebillyRestApi.ICheque](docs/ICheque.md)
 - [RebillyRestApi.IChequeAllOfCredentials](docs/IChequeAllOfCredentials.md)
 - [RebillyRestApi.IDebit](docs/IDebit.md)
 - [RebillyRestApi.IDebitAllOfCredentials](docs/IDebitAllOfCredentials.md)
 - [RebillyRestApi.INOVAPAY](docs/INOVAPAY.md)
 - [RebillyRestApi.INOVAPAYAllOfCredentials](docs/INOVAPAYAllOfCredentials.md)
 - [RebillyRestApi.IdentityMatches](docs/IdentityMatches.md)
 - [RebillyRestApi.Ilixium](docs/Ilixium.md)
 - [RebillyRestApi.Ilixium3dsServer](docs/Ilixium3dsServer.md)
 - [RebillyRestApi.Ilixium3dsServers](docs/Ilixium3dsServers.md)
 - [RebillyRestApi.IlixiumAllOfCredentials](docs/IlixiumAllOfCredentials.md)
 - [RebillyRestApi.IlixiumAllOfSettings](docs/IlixiumAllOfSettings.md)
 - [RebillyRestApi.Immediately](docs/Immediately.md)
 - [RebillyRestApi.Ingenico](docs/Ingenico.md)
 - [RebillyRestApi.Ingenico3dsServer](docs/Ingenico3dsServer.md)
 - [RebillyRestApi.Ingenico3dsServers](docs/Ingenico3dsServers.md)
 - [RebillyRestApi.IngenicoAllOfCredentials](docs/IngenicoAllOfCredentials.md)
 - [RebillyRestApi.InitialInvoiceEmbed](docs/InitialInvoiceEmbed.md)
 - [RebillyRestApi.InitialInvoiceLink](docs/InitialInvoiceLink.md)
 - [RebillyRestApi.Inovio](docs/Inovio.md)
 - [RebillyRestApi.Inovio3dsServer](docs/Inovio3dsServer.md)
 - [RebillyRestApi.Inovio3dsServers](docs/Inovio3dsServers.md)
 - [RebillyRestApi.InovioAllOfCredentials](docs/InovioAllOfCredentials.md)
 - [RebillyRestApi.InovioAllOfSettings](docs/InovioAllOfSettings.md)
 - [RebillyRestApi.InstaDebit](docs/InstaDebit.md)
 - [RebillyRestApi.InstaDebitAllOfCredentials](docs/InstaDebitAllOfCredentials.md)
 - [RebillyRestApi.InstrumentReference](docs/InstrumentReference.md)
 - [RebillyRestApi.Intelligent](docs/Intelligent.md)
 - [RebillyRestApi.IntelligentAllOfUnit](docs/IntelligentAllOfUnit.md)
 - [RebillyRestApi.Intuit](docs/Intuit.md)
 - [RebillyRestApi.IntuitAllOfCredentials](docs/IntuitAllOfCredentials.md)
 - [RebillyRestApi.InvalidError](docs/InvalidError.md)
 - [RebillyRestApi.Invoice](docs/Invoice.md)
 - [RebillyRestApi.InvoiceAllOfEmbedded](docs/InvoiceAllOfEmbedded.md)
 - [RebillyRestApi.InvoiceAllOfLinks](docs/InvoiceAllOfLinks.md)
 - [RebillyRestApi.InvoiceAllOfRetryInstruction](docs/InvoiceAllOfRetryInstruction.md)
 - [RebillyRestApi.InvoiceAllOfRetryInstructionAttempts](docs/InvoiceAllOfRetryInstructionAttempts.md)
 - [RebillyRestApi.InvoiceDiscount](docs/InvoiceDiscount.md)
 - [RebillyRestApi.InvoiceIssue](docs/InvoiceIssue.md)
 - [RebillyRestApi.InvoiceItem](docs/InvoiceItem.md)
 - [RebillyRestApi.InvoiceItemEmbeddedInner](docs/InvoiceItemEmbeddedInner.md)
 - [RebillyRestApi.InvoiceItemLinksInner](docs/InvoiceItemLinksInner.md)
 - [RebillyRestApi.InvoiceLink](docs/InvoiceLink.md)
 - [RebillyRestApi.InvoiceReissue](docs/InvoiceReissue.md)
 - [RebillyRestApi.InvoiceRetryScheduleInstruction](docs/InvoiceRetryScheduleInstruction.md)
 - [RebillyRestApi.InvoiceShipping](docs/InvoiceShipping.md)
 - [RebillyRestApi.InvoiceTax](docs/InvoiceTax.md)
 - [RebillyRestApi.InvoiceTaxItem](docs/InvoiceTaxItem.md)
 - [RebillyRestApi.InvoiceTimeShift](docs/InvoiceTimeShift.md)
 - [RebillyRestApi.InvoiceTimeline](docs/InvoiceTimeline.md)
 - [RebillyRestApi.InvoiceTransaction](docs/InvoiceTransaction.md)
 - [RebillyRestApi.InvoiceTransactionAllocation](docs/InvoiceTransactionAllocation.md)
 - [RebillyRestApi.InvoiceTransactionAllocationLinksInner](docs/InvoiceTransactionAllocationLinksInner.md)
 - [RebillyRestApi.InvoicesEmbed](docs/InvoicesEmbed.md)
 - [RebillyRestApi.InvoicesLink](docs/InvoicesLink.md)
 - [RebillyRestApi.IpayOptions](docs/IpayOptions.md)
 - [RebillyRestApi.IpayOptionsAllOfCredentials](docs/IpayOptionsAllOfCredentials.md)
 - [RebillyRestApi.IpayOptionsAllOfSettings](docs/IpayOptionsAllOfSettings.md)
 - [RebillyRestApi.IssueTimeShiftInstruction](docs/IssueTimeShiftInstruction.md)
 - [RebillyRestApi.JetPay](docs/JetPay.md)
 - [RebillyRestApi.JetPayAllOfCredentials](docs/JetPayAllOfCredentials.md)
 - [RebillyRestApi.Jeton](docs/Jeton.md)
 - [RebillyRestApi.JetonAllOfCredentials](docs/JetonAllOfCredentials.md)
 - [RebillyRestApi.JetonAllOfSettings](docs/JetonAllOfSettings.md)
 - [RebillyRestApi.Khelocard](docs/Khelocard.md)
 - [RebillyRestApi.KhelocardAllOfCredentials](docs/KhelocardAllOfCredentials.md)
 - [RebillyRestApi.KhelocardCard](docs/KhelocardCard.md)
 - [RebillyRestApi.KhelocardCardToken](docs/KhelocardCardToken.md)
 - [RebillyRestApi.Konnektive](docs/Konnektive.md)
 - [RebillyRestApi.KonnektiveAllOfCredentials](docs/KonnektiveAllOfCredentials.md)
 - [RebillyRestApi.KonnektiveAllOfSettings](docs/KonnektiveAllOfSettings.md)
 - [RebillyRestApi.KycDocument](docs/KycDocument.md)
 - [RebillyRestApi.KycDocument2](docs/KycDocument2.md)
 - [RebillyRestApi.KycDocumentLink](docs/KycDocumentLink.md)
 - [RebillyRestApi.KycDocumentRejection](docs/KycDocumentRejection.md)
 - [RebillyRestApi.KycDocumentSubtypes](docs/KycDocumentSubtypes.md)
 - [RebillyRestApi.KycDocumentTypes](docs/KycDocumentTypes.md)
 - [RebillyRestApi.KycDocumentsLink](docs/KycDocumentsLink.md)
 - [RebillyRestApi.KycGathererLink](docs/KycGathererLink.md)
 - [RebillyRestApi.KycRequest](docs/KycRequest.md)
 - [RebillyRestApi.KycRequestAllOfLinks](docs/KycRequestAllOfLinks.md)
 - [RebillyRestApi.LPG](docs/LPG.md)
 - [RebillyRestApi.LPGAllOfCredentials](docs/LPGAllOfCredentials.md)
 - [RebillyRestApi.LeadSource](docs/LeadSource.md)
 - [RebillyRestApi.LeadSourceData](docs/LeadSourceData.md)
 - [RebillyRestApi.LeadSourceEmbed](docs/LeadSourceEmbed.md)
 - [RebillyRestApi.LeadSourceLink](docs/LeadSourceLink.md)
 - [RebillyRestApi.Link](docs/Link.md)
 - [RebillyRestApi.List](docs/List.md)
 - [RebillyRestApi.Loonie](docs/Loonie.md)
 - [RebillyRestApi.LoonieAllOfCredentials](docs/LoonieAllOfCredentials.md)
 - [RebillyRestApi.Manual](docs/Manual.md)
 - [RebillyRestApi.Manual2](docs/Manual2.md)
 - [RebillyRestApi.Manual2AllOfItems](docs/Manual2AllOfItems.md)
 - [RebillyRestApi.MiFinity](docs/MiFinity.md)
 - [RebillyRestApi.MiFinityAllOfCredentials](docs/MiFinityAllOfCredentials.md)
 - [RebillyRestApi.MinimumOrderAmount](docs/MinimumOrderAmount.md)
 - [RebillyRestApi.Moneris](docs/Moneris.md)
 - [RebillyRestApi.MonerisAllOfCredentials](docs/MonerisAllOfCredentials.md)
 - [RebillyRestApi.Money](docs/Money.md)
 - [RebillyRestApi.MtaPay](docs/MtaPay.md)
 - [RebillyRestApi.MtaPayAllOfCredentials](docs/MtaPayAllOfCredentials.md)
 - [RebillyRestApi.MtaPayAllOfSettings](docs/MtaPayAllOfSettings.md)
 - [RebillyRestApi.MuchBetter](docs/MuchBetter.md)
 - [RebillyRestApi.MuchBetterAllOfCredentials](docs/MuchBetterAllOfCredentials.md)
 - [RebillyRestApi.MuchBetterAllOfSettings](docs/MuchBetterAllOfSettings.md)
 - [RebillyRestApi.MyFatoorah](docs/MyFatoorah.md)
 - [RebillyRestApi.MyFatoorahAllOfCredentials](docs/MyFatoorahAllOfCredentials.md)
 - [RebillyRestApi.NGenius](docs/NGenius.md)
 - [RebillyRestApi.NGenius3dsServer](docs/NGenius3dsServer.md)
 - [RebillyRestApi.NGenius3dsServers](docs/NGenius3dsServers.md)
 - [RebillyRestApi.NGeniusAllOfCredentials](docs/NGeniusAllOfCredentials.md)
 - [RebillyRestApi.NMI](docs/NMI.md)
 - [RebillyRestApi.NMI3dsServers](docs/NMI3dsServers.md)
 - [RebillyRestApi.NMIAllOfCredentials](docs/NMIAllOfCredentials.md)
 - [RebillyRestApi.NMIAllOfSettings](docs/NMIAllOfSettings.md)
 - [RebillyRestApi.Neosurf](docs/Neosurf.md)
 - [RebillyRestApi.NeosurfAllOfCredentials](docs/NeosurfAllOfCredentials.md)
 - [RebillyRestApi.Netbanking](docs/Netbanking.md)
 - [RebillyRestApi.NetbankingAllOfCredentials](docs/NetbankingAllOfCredentials.md)
 - [RebillyRestApi.Neteller](docs/Neteller.md)
 - [RebillyRestApi.NetellerAllOfCredentials](docs/NetellerAllOfCredentials.md)
 - [RebillyRestApi.NetellerAllOfSettings](docs/NetellerAllOfSettings.md)
 - [RebillyRestApi.NinjaWallet](docs/NinjaWallet.md)
 - [RebillyRestApi.NinjaWalletAllOfCredentials](docs/NinjaWalletAllOfCredentials.md)
 - [RebillyRestApi.NuaPay](docs/NuaPay.md)
 - [RebillyRestApi.NuaPayAllOfCredentials](docs/NuaPayAllOfCredentials.md)
 - [RebillyRestApi.OchaPay](docs/OchaPay.md)
 - [RebillyRestApi.OchaPayAllOfCredentials](docs/OchaPayAllOfCredentials.md)
 - [RebillyRestApi.OnBoardingUrlLink](docs/OnBoardingUrlLink.md)
 - [RebillyRestApi.OnRamp](docs/OnRamp.md)
 - [RebillyRestApi.OnRampAllOfCredentials](docs/OnRampAllOfCredentials.md)
 - [RebillyRestApi.OneColumn](docs/OneColumn.md)
 - [RebillyRestApi.OneColumnAllOfData](docs/OneColumnAllOfData.md)
 - [RebillyRestApi.OneTimeOrder](docs/OneTimeOrder.md)
 - [RebillyRestApi.Onlineueberweisen](docs/Onlineueberweisen.md)
 - [RebillyRestApi.OnlineueberweisenAllOfCredentials](docs/OnlineueberweisenAllOfCredentials.md)
 - [RebillyRestApi.OnlineueberweisenAllOfSettings](docs/OnlineueberweisenAllOfSettings.md)
 - [RebillyRestApi.OrderTimeline](docs/OrderTimeline.md)
 - [RebillyRestApi.Organization](docs/Organization.md)
 - [RebillyRestApi.OrganizationEmbed](docs/OrganizationEmbed.md)
 - [RebillyRestApi.OrganizationLink](docs/OrganizationLink.md)
 - [RebillyRestApi.OrganizationQuestionnaire](docs/OrganizationQuestionnaire.md)
 - [RebillyRestApi.Other](docs/Other.md)
 - [RebillyRestApi.Paay3dsServer](docs/Paay3dsServer.md)
 - [RebillyRestApi.Pagsmile](docs/Pagsmile.md)
 - [RebillyRestApi.PagsmileAllOfCredentials](docs/PagsmileAllOfCredentials.md)
 - [RebillyRestApi.PaidByTime](docs/PaidByTime.md)
 - [RebillyRestApi.Panamerican](docs/Panamerican.md)
 - [RebillyRestApi.Panamerican3dsServer](docs/Panamerican3dsServer.md)
 - [RebillyRestApi.Panamerican3dsServers](docs/Panamerican3dsServers.md)
 - [RebillyRestApi.PanamericanAllOfCredentials](docs/PanamericanAllOfCredentials.md)
 - [RebillyRestApi.PanamericanAllOfSettings](docs/PanamericanAllOfSettings.md)
 - [RebillyRestApi.PandaGateway](docs/PandaGateway.md)
 - [RebillyRestApi.PandaGatewayAllOfCredentials](docs/PandaGatewayAllOfCredentials.md)
 - [RebillyRestApi.ParamountEft](docs/ParamountEft.md)
 - [RebillyRestApi.ParamountEftAllOfCredentials](docs/ParamountEftAllOfCredentials.md)
 - [RebillyRestApi.ParamountInterac](docs/ParamountInterac.md)
 - [RebillyRestApi.ParamountInteracAllOfCredentials](docs/ParamountInteracAllOfCredentials.md)
 - [RebillyRestApi.ParentTransactionEmbed](docs/ParentTransactionEmbed.md)
 - [RebillyRestApi.ParentTransactionLink](docs/ParentTransactionLink.md)
 - [RebillyRestApi.Partial](docs/Partial.md)
 - [RebillyRestApi.Password](docs/Password.md)
 - [RebillyRestApi.Passwordless](docs/Passwordless.md)
 - [RebillyRestApi.PatchKycRequestRequest](docs/PatchKycRequestRequest.md)
 - [RebillyRestApi.PatchPaymentInstrumentRequest](docs/PatchPaymentInstrumentRequest.md)
 - [RebillyRestApi.PatchTransactionRequest](docs/PatchTransactionRequest.md)
 - [RebillyRestApi.Pay4Fun](docs/Pay4Fun.md)
 - [RebillyRestApi.Pay4FunAllOfCredentials](docs/Pay4FunAllOfCredentials.md)
 - [RebillyRestApi.PayCash](docs/PayCash.md)
 - [RebillyRestApi.PayCashAllOfCredentials](docs/PayCashAllOfCredentials.md)
 - [RebillyRestApi.PayClub](docs/PayClub.md)
 - [RebillyRestApi.PayClubAllOfCredentials](docs/PayClubAllOfCredentials.md)
 - [RebillyRestApi.PayClubAllOfSettings](docs/PayClubAllOfSettings.md)
 - [RebillyRestApi.PayPal](docs/PayPal.md)
 - [RebillyRestApi.PayPalAccount](docs/PayPalAccount.md)
 - [RebillyRestApi.PayPalAccountAllOfEmbedded](docs/PayPalAccountAllOfEmbedded.md)
 - [RebillyRestApi.PayPalAccountAllOfLinks](docs/PayPalAccountAllOfLinks.md)
 - [RebillyRestApi.PayPalAllOfSettings](docs/PayPalAllOfSettings.md)
 - [RebillyRestApi.PayTabs](docs/PayTabs.md)
 - [RebillyRestApi.PayTabsAllOfCredentials](docs/PayTabsAllOfCredentials.md)
 - [RebillyRestApi.PayULatam](docs/PayULatam.md)
 - [RebillyRestApi.PayULatamAllOfCredentials](docs/PayULatamAllOfCredentials.md)
 - [RebillyRestApi.Payeezy](docs/Payeezy.md)
 - [RebillyRestApi.PayeezyAllOfCredentials](docs/PayeezyAllOfCredentials.md)
 - [RebillyRestApi.Payflow](docs/Payflow.md)
 - [RebillyRestApi.PayflowAllOfCredentials](docs/PayflowAllOfCredentials.md)
 - [RebillyRestApi.PaymenTechnologies](docs/PaymenTechnologies.md)
 - [RebillyRestApi.PaymenTechnologiesAllOfCredentials](docs/PaymenTechnologiesAllOfCredentials.md)
 - [RebillyRestApi.PaymenTechnologiesAllOfSettings](docs/PaymenTechnologiesAllOfSettings.md)
 - [RebillyRestApi.PaymentAsia](docs/PaymentAsia.md)
 - [RebillyRestApi.PaymentAsiaAllOfCredentials](docs/PaymentAsiaAllOfCredentials.md)
 - [RebillyRestApi.PaymentCard](docs/PaymentCard.md)
 - [RebillyRestApi.PaymentCardAllOfEmbedded](docs/PaymentCardAllOfEmbedded.md)
 - [RebillyRestApi.PaymentCardAllOfLinks](docs/PaymentCardAllOfLinks.md)
 - [RebillyRestApi.PaymentCardBrand](docs/PaymentCardBrand.md)
 - [RebillyRestApi.PaymentCardCreatePlain](docs/PaymentCardCreatePlain.md)
 - [RebillyRestApi.PaymentCardCreateToken](docs/PaymentCardCreateToken.md)
 - [RebillyRestApi.PaymentCardDigitalWalletFeature](docs/PaymentCardDigitalWalletFeature.md)
 - [RebillyRestApi.PaymentCardEmbed](docs/PaymentCardEmbed.md)
 - [RebillyRestApi.PaymentCardLink](docs/PaymentCardLink.md)
 - [RebillyRestApi.PaymentCardToken](docs/PaymentCardToken.md)
 - [RebillyRestApi.PaymentCardUpdatePlain](docs/PaymentCardUpdatePlain.md)
 - [RebillyRestApi.PaymentInstruction](docs/PaymentInstruction.md)
 - [RebillyRestApi.PaymentInstrument](docs/PaymentInstrument.md)
 - [RebillyRestApi.PaymentInstrument2](docs/PaymentInstrument2.md)
 - [RebillyRestApi.PaymentInstrument3](docs/PaymentInstrument3.md)
 - [RebillyRestApi.PaymentInstrumentCreateToken](docs/PaymentInstrumentCreateToken.md)
 - [RebillyRestApi.PaymentInstrumentUpdateToken](docs/PaymentInstrumentUpdateToken.md)
 - [RebillyRestApi.PaymentMethod](docs/PaymentMethod.md)
 - [RebillyRestApi.PaymentMethods](docs/PaymentMethods.md)
 - [RebillyRestApi.PaymentRetry](docs/PaymentRetry.md)
 - [RebillyRestApi.PaymentRetryAttemptsInner](docs/PaymentRetryAttemptsInner.md)
 - [RebillyRestApi.PaymentToken](docs/PaymentToken.md)
 - [RebillyRestApi.PaymentsOS](docs/PaymentsOS.md)
 - [RebillyRestApi.PaymentsOSAllOfCredentials](docs/PaymentsOSAllOfCredentials.md)
 - [RebillyRestApi.Paymero](docs/Paymero.md)
 - [RebillyRestApi.PaymeroAllOfCredentials](docs/PaymeroAllOfCredentials.md)
 - [RebillyRestApi.PaymeroAllOfSettings](docs/PaymeroAllOfSettings.md)
 - [RebillyRestApi.PayoutRequest](docs/PayoutRequest.md)
 - [RebillyRestApi.Payr](docs/Payr.md)
 - [RebillyRestApi.PayrAllOfCredentials](docs/PayrAllOfCredentials.md)
 - [RebillyRestApi.Paysafe](docs/Paysafe.md)
 - [RebillyRestApi.Paysafe3dsServer](docs/Paysafe3dsServer.md)
 - [RebillyRestApi.Paysafe3dsServers](docs/Paysafe3dsServers.md)
 - [RebillyRestApi.PaysafeAllOfCredentials](docs/PaysafeAllOfCredentials.md)
 - [RebillyRestApi.Paysafecash](docs/Paysafecash.md)
 - [RebillyRestApi.PaysafecashAllOfCredentials](docs/PaysafecashAllOfCredentials.md)
 - [RebillyRestApi.Payvision](docs/Payvision.md)
 - [RebillyRestApi.Payvision3dsServer](docs/Payvision3dsServer.md)
 - [RebillyRestApi.Payvision3dsServers](docs/Payvision3dsServers.md)
 - [RebillyRestApi.PayvisionAllOfCredentials](docs/PayvisionAllOfCredentials.md)
 - [RebillyRestApi.PayvisionAllOfSettings](docs/PayvisionAllOfSettings.md)
 - [RebillyRestApi.Percent](docs/Percent.md)
 - [RebillyRestApi.PermalinkLink](docs/PermalinkLink.md)
 - [RebillyRestApi.Piastrix](docs/Piastrix.md)
 - [RebillyRestApi.Piastrix3dsServer](docs/Piastrix3dsServer.md)
 - [RebillyRestApi.Piastrix3dsServers](docs/Piastrix3dsServers.md)
 - [RebillyRestApi.PiastrixAllOfCredentials](docs/PiastrixAllOfCredentials.md)
 - [RebillyRestApi.PiastrixAllOfSettings](docs/PiastrixAllOfSettings.md)
 - [RebillyRestApi.PlaidAccountToken](docs/PlaidAccountToken.md)
 - [RebillyRestApi.Plan](docs/Plan.md)
 - [RebillyRestApi.PlanBillingTiming](docs/PlanBillingTiming.md)
 - [RebillyRestApi.PlanEmbed](docs/PlanEmbed.md)
 - [RebillyRestApi.PlanPeriod](docs/PlanPeriod.md)
 - [RebillyRestApi.PlanPriceFormula](docs/PlanPriceFormula.md)
 - [RebillyRestApi.Plugnpay](docs/Plugnpay.md)
 - [RebillyRestApi.PlugnpayAllOfCredentials](docs/PlugnpayAllOfCredentials.md)
 - [RebillyRestApi.PostBankAccountRequest](docs/PostBankAccountRequest.md)
 - [RebillyRestApi.PostFileRequest](docs/PostFileRequest.md)
 - [RebillyRestApi.PostFinance](docs/PostFinance.md)
 - [RebillyRestApi.PostFinanceAllOfCredentials](docs/PostFinanceAllOfCredentials.md)
 - [RebillyRestApi.PostKycDocumentMatchesRequest](docs/PostKycDocumentMatchesRequest.md)
 - [RebillyRestApi.PostPaymentCardRequest](docs/PostPaymentCardRequest.md)
 - [RebillyRestApi.PostPaymentInstrumentRequest](docs/PostPaymentInstrumentRequest.md)
 - [RebillyRestApi.PostTagCustomerCollectionRequest](docs/PostTagCustomerCollectionRequest.md)
 - [RebillyRestApi.PriceBasedShippingRate](docs/PriceBasedShippingRate.md)
 - [RebillyRestApi.Problem](docs/Problem.md)
 - [RebillyRestApi.Product](docs/Product.md)
 - [RebillyRestApi.ProductEmbed](docs/ProductEmbed.md)
 - [RebillyRestApi.ProductLink](docs/ProductLink.md)
 - [RebillyRestApi.ProofOfAddress](docs/ProofOfAddress.md)
 - [RebillyRestApi.ProofOfAddressAllOfDocumentMatches](docs/ProofOfAddressAllOfDocumentMatches.md)
 - [RebillyRestApi.ProofOfAddressAllOfLinks](docs/ProofOfAddressAllOfLinks.md)
 - [RebillyRestApi.ProofOfFunds](docs/ProofOfFunds.md)
 - [RebillyRestApi.ProofOfIdentity](docs/ProofOfIdentity.md)
 - [RebillyRestApi.ProofOfIdentityAllOfDocumentMatches](docs/ProofOfIdentityAllOfDocumentMatches.md)
 - [RebillyRestApi.ProofOfIdentityAllOfLinks](docs/ProofOfIdentityAllOfLinks.md)
 - [RebillyRestApi.ProofOfPurchase](docs/ProofOfPurchase.md)
 - [RebillyRestApi.Prosa](docs/Prosa.md)
 - [RebillyRestApi.ProsaAllOfCredentials](docs/ProsaAllOfCredentials.md)
 - [RebillyRestApi.PurchaseBumpOffer](docs/PurchaseBumpOffer.md)
 - [RebillyRestApi.PurchaseBumpStatus](docs/PurchaseBumpStatus.md)
 - [RebillyRestApi.QueryUrlLink](docs/QueryUrlLink.md)
 - [RebillyRestApi.RPN](docs/RPN.md)
 - [RebillyRestApi.RPNAllOfCredentials](docs/RPNAllOfCredentials.md)
 - [RebillyRestApi.Rapyd](docs/Rapyd.md)
 - [RebillyRestApi.RapydAllOfCredentials](docs/RapydAllOfCredentials.md)
 - [RebillyRestApi.ReadyToPay](docs/ReadyToPay.md)
 - [RebillyRestApi.ReadyToPayAchMethod](docs/ReadyToPayAchMethod.md)
 - [RebillyRestApi.ReadyToPayAchMethodFeature](docs/ReadyToPayAchMethodFeature.md)
 - [RebillyRestApi.ReadyToPayAmount](docs/ReadyToPayAmount.md)
 - [RebillyRestApi.ReadyToPayGenericMethod](docs/ReadyToPayGenericMethod.md)
 - [RebillyRestApi.ReadyToPayItems](docs/ReadyToPayItems.md)
 - [RebillyRestApi.ReadyToPayItemsItemsInner](docs/ReadyToPayItemsItemsInner.md)
 - [RebillyRestApi.ReadyToPayMethodsInner](docs/ReadyToPayMethodsInner.md)
 - [RebillyRestApi.ReadyToPayPaymentCardMethod](docs/ReadyToPayPaymentCardMethod.md)
 - [RebillyRestApi.ReadyToPayPaymentCardMethodFeature](docs/ReadyToPayPaymentCardMethodFeature.md)
 - [RebillyRestApi.Realex](docs/Realex.md)
 - [RebillyRestApi.RealexAllOfCredentials](docs/RealexAllOfCredentials.md)
 - [RebillyRestApi.Realtime](docs/Realtime.md)
 - [RebillyRestApi.RealtimeAllOfCredentials](docs/RealtimeAllOfCredentials.md)
 - [RebillyRestApi.Rebilly](docs/Rebilly.md)
 - [RebillyRestApi.RebillyTaxjar](docs/RebillyTaxjar.md)
 - [RebillyRestApi.RebillyTaxjarAllOfItems](docs/RebillyTaxjarAllOfItems.md)
 - [RebillyRestApi.RecalculateInvoiceLink](docs/RecalculateInvoiceLink.md)
 - [RebillyRestApi.RecentInvoiceEmbed](docs/RecentInvoiceEmbed.md)
 - [RebillyRestApi.RecentInvoiceLink](docs/RecentInvoiceLink.md)
 - [RebillyRestApi.RedemptionCancel](docs/RedemptionCancel.md)
 - [RebillyRestApi.RedemptionRestriction](docs/RedemptionRestriction.md)
 - [RebillyRestApi.RedemptionsPerCustomer](docs/RedemptionsPerCustomer.md)
 - [RebillyRestApi.Redsys](docs/Redsys.md)
 - [RebillyRestApi.RedsysAllOfCredentials](docs/RedsysAllOfCredentials.md)
 - [RebillyRestApi.RefundUrlLink](docs/RefundUrlLink.md)
 - [RebillyRestApi.ResendEmail](docs/ResendEmail.md)
 - [RebillyRestApi.ResetPasswordToken](docs/ResetPasswordToken.md)
 - [RebillyRestApi.RestrictToInvoices](docs/RestrictToInvoices.md)
 - [RebillyRestApi.RestrictToPlans](docs/RestrictToPlans.md)
 - [RebillyRestApi.RestrictToProducts](docs/RestrictToProducts.md)
 - [RebillyRestApi.RestrictToSubscriptions](docs/RestrictToSubscriptions.md)
 - [RebillyRestApi.RetriedTransactionEmbed](docs/RetriedTransactionEmbed.md)
 - [RebillyRestApi.RetriedTransactionLink](docs/RetriedTransactionLink.md)
 - [RebillyRestApi.RiskMetadata](docs/RiskMetadata.md)
 - [RebillyRestApi.Rotessa](docs/Rotessa.md)
 - [RebillyRestApi.RotessaAllOfCredentials](docs/RotessaAllOfCredentials.md)
 - [RebillyRestApi.RotessaAllOfSettings](docs/RotessaAllOfSettings.md)
 - [RebillyRestApi.RulesetRestore](docs/RulesetRestore.md)
 - [RebillyRestApi.SMSVoucher](docs/SMSVoucher.md)
 - [RebillyRestApi.SMSVoucherAllOfCredentials](docs/SMSVoucherAllOfCredentials.md)
 - [RebillyRestApi.Sagepay](docs/Sagepay.md)
 - [RebillyRestApi.SagepayAllOfCredentials](docs/SagepayAllOfCredentials.md)
 - [RebillyRestApi.SaltarPay](docs/SaltarPay.md)
 - [RebillyRestApi.SaltarPayAllOfCredentials](docs/SaltarPayAllOfCredentials.md)
 - [RebillyRestApi.SeamlessChex](docs/SeamlessChex.md)
 - [RebillyRestApi.SeamlessChexAllOfCredentials](docs/SeamlessChexAllOfCredentials.md)
 - [RebillyRestApi.Search](docs/Search.md)
 - [RebillyRestApi.SecureTrading](docs/SecureTrading.md)
 - [RebillyRestApi.SecureTrading3dsServer](docs/SecureTrading3dsServer.md)
 - [RebillyRestApi.SecureTrading3dsServers](docs/SecureTrading3dsServers.md)
 - [RebillyRestApi.SecureTradingAllOfCredentials](docs/SecureTradingAllOfCredentials.md)
 - [RebillyRestApi.SecurionPay](docs/SecurionPay.md)
 - [RebillyRestApi.SecurionPay3dsServers](docs/SecurionPay3dsServers.md)
 - [RebillyRestApi.SecurionPayAllOfCredentials](docs/SecurionPayAllOfCredentials.md)
 - [RebillyRestApi.SelfLink](docs/SelfLink.md)
 - [RebillyRestApi.ServicePeriodAnchorInstruction](docs/ServicePeriodAnchorInstruction.md)
 - [RebillyRestApi.ShippingZone](docs/ShippingZone.md)
 - [RebillyRestApi.SignedLinkLink](docs/SignedLinkLink.md)
 - [RebillyRestApi.Skrill](docs/Skrill.md)
 - [RebillyRestApi.SkrillAllOfCredentials](docs/SkrillAllOfCredentials.md)
 - [RebillyRestApi.SmartInvoice](docs/SmartInvoice.md)
 - [RebillyRestApi.SmartInvoice3dsServer](docs/SmartInvoice3dsServer.md)
 - [RebillyRestApi.SmartInvoice3dsServers](docs/SmartInvoice3dsServers.md)
 - [RebillyRestApi.SmartInvoiceAllOfCredentials](docs/SmartInvoiceAllOfCredentials.md)
 - [RebillyRestApi.Sofort](docs/Sofort.md)
 - [RebillyRestApi.SofortAllOfCredentials](docs/SofortAllOfCredentials.md)
 - [RebillyRestApi.SparkPay](docs/SparkPay.md)
 - [RebillyRestApi.SparkPayAllOfCredentials](docs/SparkPayAllOfCredentials.md)
 - [RebillyRestApi.Stairstep](docs/Stairstep.md)
 - [RebillyRestApi.StairstepAllOfBrackets](docs/StairstepAllOfBrackets.md)
 - [RebillyRestApi.StaticGateway](docs/StaticGateway.md)
 - [RebillyRestApi.StaticIpnLink](docs/StaticIpnLink.md)
 - [RebillyRestApi.Stripe](docs/Stripe.md)
 - [RebillyRestApi.Stripe3dsServer](docs/Stripe3dsServer.md)
 - [RebillyRestApi.Stripe3dsServers](docs/Stripe3dsServers.md)
 - [RebillyRestApi.StripeAllOfSettings](docs/StripeAllOfSettings.md)
 - [RebillyRestApi.Subscription](docs/Subscription.md)
 - [RebillyRestApi.SubscriptionCancellation](docs/SubscriptionCancellation.md)
 - [RebillyRestApi.SubscriptionCancellationState](docs/SubscriptionCancellationState.md)
 - [RebillyRestApi.SubscriptionChange](docs/SubscriptionChange.md)
 - [RebillyRestApi.SubscriptionChangeItemsInner](docs/SubscriptionChangeItemsInner.md)
 - [RebillyRestApi.SubscriptionInvoice](docs/SubscriptionInvoice.md)
 - [RebillyRestApi.SubscriptionLink](docs/SubscriptionLink.md)
 - [RebillyRestApi.SubscriptionMetadata](docs/SubscriptionMetadata.md)
 - [RebillyRestApi.SubscriptionMetadataEmbeddedInner](docs/SubscriptionMetadataEmbeddedInner.md)
 - [RebillyRestApi.SubscriptionMetadataLinksInner](docs/SubscriptionMetadataLinksInner.md)
 - [RebillyRestApi.SubscriptionOrder](docs/SubscriptionOrder.md)
 - [RebillyRestApi.SubscriptionReactivation](docs/SubscriptionReactivation.md)
 - [RebillyRestApi.TWINT](docs/TWINT.md)
 - [RebillyRestApi.TWINTAllOfCredentials](docs/TWINTAllOfCredentials.md)
 - [RebillyRestApi.TWINTAllOfSettings](docs/TWINTAllOfSettings.md)
 - [RebillyRestApi.Tag](docs/Tag.md)
 - [RebillyRestApi.TestProcessor](docs/TestProcessor.md)
 - [RebillyRestApi.TestProcessor3dsServer](docs/TestProcessor3dsServer.md)
 - [RebillyRestApi.TestProcessor3dsServers](docs/TestProcessor3dsServers.md)
 - [RebillyRestApi.ThreeColumns](docs/ThreeColumns.md)
 - [RebillyRestApi.ThreeColumnsAllOfData](docs/ThreeColumnsAllOfData.md)
 - [RebillyRestApi.ThreeDSecure](docs/ThreeDSecure.md)
 - [RebillyRestApi.ThreeDSecureIO3dsServer](docs/ThreeDSecureIO3dsServer.md)
 - [RebillyRestApi.ThreeDSecureResult](docs/ThreeDSecureResult.md)
 - [RebillyRestApi.ThreeDSecureServerName](docs/ThreeDSecureServerName.md)
 - [RebillyRestApi.Tiered](docs/Tiered.md)
 - [RebillyRestApi.TimePluralUnit](docs/TimePluralUnit.md)
 - [RebillyRestApi.TimeUnit](docs/TimeUnit.md)
 - [RebillyRestApi.TimelineAction](docs/TimelineAction.md)
 - [RebillyRestApi.TimelineExtraData](docs/TimelineExtraData.md)
 - [RebillyRestApi.TimelineExtraDataAuthor](docs/TimelineExtraDataAuthor.md)
 - [RebillyRestApi.TimelineExtraDataLinksInner](docs/TimelineExtraDataLinksInner.md)
 - [RebillyRestApi.TimelineTable](docs/TimelineTable.md)
 - [RebillyRestApi.ToditoCash](docs/ToditoCash.md)
 - [RebillyRestApi.ToditoCashAllOfCredentials](docs/ToditoCashAllOfCredentials.md)
 - [RebillyRestApi.TotalRedemptions](docs/TotalRedemptions.md)
 - [RebillyRestApi.Transaction](docs/Transaction.md)
 - [RebillyRestApi.TransactionAllOfBumpOffer](docs/TransactionAllOfBumpOffer.md)
 - [RebillyRestApi.TransactionAllOfDcc](docs/TransactionAllOfDcc.md)
 - [RebillyRestApi.TransactionAllOfEmbedded](docs/TransactionAllOfEmbedded.md)
 - [RebillyRestApi.TransactionAllOfGateway](docs/TransactionAllOfGateway.md)
 - [RebillyRestApi.TransactionAllOfGatewayAvsResponse](docs/TransactionAllOfGatewayAvsResponse.md)
 - [RebillyRestApi.TransactionAllOfGatewayCvvResponse](docs/TransactionAllOfGatewayCvvResponse.md)
 - [RebillyRestApi.TransactionAllOfGatewayResponse](docs/TransactionAllOfGatewayResponse.md)
 - [RebillyRestApi.TransactionAllOfLinks](docs/TransactionAllOfLinks.md)
 - [RebillyRestApi.TransactionAllocationsLink](docs/TransactionAllocationsLink.md)
 - [RebillyRestApi.TransactionEmbed](docs/TransactionEmbed.md)
 - [RebillyRestApi.TransactionLink](docs/TransactionLink.md)
 - [RebillyRestApi.TransactionQuery](docs/TransactionQuery.md)
 - [RebillyRestApi.TransactionRefund](docs/TransactionRefund.md)
 - [RebillyRestApi.TransactionRequest](docs/TransactionRequest.md)
 - [RebillyRestApi.TransactionTimeline](docs/TransactionTimeline.md)
 - [RebillyRestApi.TransactionUpdate](docs/TransactionUpdate.md)
 - [RebillyRestApi.TransactionUpdateUrlLink](docs/TransactionUpdateUrlLink.md)
 - [RebillyRestApi.TrustPay](docs/TrustPay.md)
 - [RebillyRestApi.TrustPayAllOfCredentials](docs/TrustPayAllOfCredentials.md)
 - [RebillyRestApi.Trustly](docs/Trustly.md)
 - [RebillyRestApi.TrustlyAllOfCredentials](docs/TrustlyAllOfCredentials.md)
 - [RebillyRestApi.TrustsPay](docs/TrustsPay.md)
 - [RebillyRestApi.TrustsPayAllOfCredentials](docs/TrustsPayAllOfCredentials.md)
 - [RebillyRestApi.TwoColumns](docs/TwoColumns.md)
 - [RebillyRestApi.UPayCard](docs/UPayCard.md)
 - [RebillyRestApi.UPayCardAllOfCredentials](docs/UPayCardAllOfCredentials.md)
 - [RebillyRestApi.UPayCardAllOfSettings](docs/UPayCardAllOfSettings.md)
 - [RebillyRestApi.USAePay](docs/USAePay.md)
 - [RebillyRestApi.USAePayAllOfCredentials](docs/USAePayAllOfCredentials.md)
 - [RebillyRestApi.UpcomingInvoiceItem](docs/UpcomingInvoiceItem.md)
 - [RebillyRestApi.VCreditos](docs/VCreditos.md)
 - [RebillyRestApi.VCreditosAllOfCredentials](docs/VCreditosAllOfCredentials.md)
 - [RebillyRestApi.ValidationErrorExtensions](docs/ValidationErrorExtensions.md)
 - [RebillyRestApi.ValidationErrorExtensionsInvalidFieldsInner](docs/ValidationErrorExtensionsInvalidFieldsInner.md)
 - [RebillyRestApi.VantivLitle](docs/VantivLitle.md)
 - [RebillyRestApi.VantivLitle3dsServers](docs/VantivLitle3dsServers.md)
 - [RebillyRestApi.VantivLitleAllOfCredentials](docs/VantivLitleAllOfCredentials.md)
 - [RebillyRestApi.VaultedInstrument](docs/VaultedInstrument.md)
 - [RebillyRestApi.VegaaH](docs/VegaaH.md)
 - [RebillyRestApi.VegaaHAllOfCredentials](docs/VegaaHAllOfCredentials.md)
 - [RebillyRestApi.Volume](docs/Volume.md)
 - [RebillyRestApi.Wallet88](docs/Wallet88.md)
 - [RebillyRestApi.Wallet88AllOfCredentials](docs/Wallet88AllOfCredentials.md)
 - [RebillyRestApi.Walpay](docs/Walpay.md)
 - [RebillyRestApi.Walpay3dsServers](docs/Walpay3dsServers.md)
 - [RebillyRestApi.WalpayAllOfCredentials](docs/WalpayAllOfCredentials.md)
 - [RebillyRestApi.WebsiteEmbed](docs/WebsiteEmbed.md)
 - [RebillyRestApi.WebsiteLink](docs/WebsiteLink.md)
 - [RebillyRestApi.Wirecard](docs/Wirecard.md)
 - [RebillyRestApi.Wirecard3dsServer](docs/Wirecard3dsServer.md)
 - [RebillyRestApi.Wirecard3dsServers](docs/Wirecard3dsServers.md)
 - [RebillyRestApi.WirecardAllOfCredentials](docs/WirecardAllOfCredentials.md)
 - [RebillyRestApi.WorldlineAtosFrankfurt](docs/WorldlineAtosFrankfurt.md)
 - [RebillyRestApi.WorldlineAtosFrankfurt3dsServers](docs/WorldlineAtosFrankfurt3dsServers.md)
 - [RebillyRestApi.WorldlineAtosFrankfurtAllOfCredentials](docs/WorldlineAtosFrankfurtAllOfCredentials.md)
 - [RebillyRestApi.WorldlineAtosFrankfurtAllOfSettings](docs/WorldlineAtosFrankfurtAllOfSettings.md)
 - [RebillyRestApi.Worldpay](docs/Worldpay.md)
 - [RebillyRestApi.Worldpay3dsServers](docs/Worldpay3dsServers.md)
 - [RebillyRestApi.WorldpayAllOfCredentials](docs/WorldpayAllOfCredentials.md)
 - [RebillyRestApi.WorldpayAllOfSettings](docs/WorldpayAllOfSettings.md)
 - [RebillyRestApi.XPay](docs/XPay.md)
 - [RebillyRestApi.XPayAllOfCredentials](docs/XPayAllOfCredentials.md)
 - [RebillyRestApi.Zimpler](docs/Zimpler.md)
 - [RebillyRestApi.ZimplerAllOfCredentials](docs/ZimplerAllOfCredentials.md)
 - [RebillyRestApi.Zotapay](docs/Zotapay.md)
 - [RebillyRestApi.ZotapayAllOfCredentials](docs/ZotapayAllOfCredentials.md)


## Documentation for Authorization


Authentication schemes defined for the API:
### JWT

- **Type**: Bearer authentication (JWT)

### PublishableApiKey


- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header

### SecretApiKey


- **Type**: API key
- **API key parameter name**: REB-APIKEY
- **Location**: HTTP header

