# openapi-java-client

Rebilly REST API
- API version: 2.1
  - Build date: 2024-10-12T11:20:59.825309-04:00[America/New_York]
  - Generator version: 7.9.0

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


  For more information, please visit [https://www.rebilly.com/contact/](https://www.rebilly.com/contact/)

*Automatically generated by the [OpenAPI Generator](https://openapi-generator.tech)*


## Requirements

Building the API client library requires:
1. Java 1.8+
2. Maven (3.8.3+)/Gradle (7.2+)

## Installation

To install the API client library to your local Maven repository, simply execute:

```shell
mvn clean install
```

To deploy it to a remote Maven repository instead, configure the settings of the repository and execute:

```shell
mvn clean deploy
```

Refer to the [OSSRH Guide](http://central.sonatype.org/pages/ossrh-guide.html) for more information.

### Maven users

Add this dependency to your project's POM:

```xml
<dependency>
  <groupId>org.openapitools</groupId>
  <artifactId>openapi-java-client</artifactId>
  <version>2.1</version>
  <scope>compile</scope>
</dependency>
```

### Gradle users

Add this dependency to your project's build file:

```groovy
  repositories {
    mavenCentral()     // Needed if the 'openapi-java-client' jar has been published to maven central.
    mavenLocal()       // Needed if the 'openapi-java-client' jar has been published to the local maven repo.
  }

  dependencies {
     implementation "org.openapitools:openapi-java-client:2.1"
  }
```

### Others

At first generate the JAR by executing:

```shell
mvn clean package
```

Then manually install the following JARs:

* `target/openapi-java-client-2.1.jar`
* `target/lib/*.jar`

## Getting Started

Please follow the [installation](#installation) instruction and execute the following Java code:

```java

// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.model.*;
import org.openapitools.client.api.AmlApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-sandbox.rebilly.com");
    
    // Configure API key authorization: SecretApiKey
    ApiKeyAuth SecretApiKey = (ApiKeyAuth) defaultClient.getAuthentication("SecretApiKey");
    SecretApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //SecretApiKey.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: JWT
    HttpBearerAuth JWT = (HttpBearerAuth) defaultClient.getAuthentication("JWT");
    JWT.setBearerToken("BEARER TOKEN");

    AmlApi apiInstance = new AmlApi(defaultClient);
    String firstName = "firstName_example"; // String | First name of individual to search.
    String lastName = "lastName_example"; // String | Last name of individual to search.
    String organizationId = "organizationId_example"; // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    String dob = "dob_example"; // String | Date of birth in format YYYY-MM-DD.
    String country = "country_example"; // String | Country of individual as an ISO Alpha-2 code.
    try {
      List<AML> result = apiInstance.getAmlEntry(firstName, lastName, organizationId, dob, country);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AmlApi#getAmlEntry");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

## Documentation for API Endpoints

All URIs are relative to *https://api-sandbox.rebilly.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AmlApi* | [**getAmlEntry**](docs/AmlApi.md#getAmlEntry) | **GET** /aml | Search PEP/Sanctions/Adverse Media lists
*BankAccountsApi* | [**getBankAccount**](docs/BankAccountsApi.md#getBankAccount) | **GET** /bank-accounts/{id} | Retrieve a Bank Account
*BankAccountsApi* | [**getBankAccountCollection**](docs/BankAccountsApi.md#getBankAccountCollection) | **GET** /bank-accounts | Retrieve a list of bank accounts
*BankAccountsApi* | [**patchBankAccount**](docs/BankAccountsApi.md#patchBankAccount) | **PATCH** /bank-accounts/{id} | Update a bank account&#39;s values
*BankAccountsApi* | [**postBankAccount**](docs/BankAccountsApi.md#postBankAccount) | **POST** /bank-accounts | Create a Bank Account
*BankAccountsApi* | [**postBankAccountDeactivation**](docs/BankAccountsApi.md#postBankAccountDeactivation) | **POST** /bank-accounts/{id}/deactivation | Deactivate a Bank Account
*BankAccountsApi* | [**putBankAccount**](docs/BankAccountsApi.md#putBankAccount) | **PUT** /bank-accounts/{id} | Create a Bank Account with predefined ID
*BlocklistsApi* | [**deleteBlocklist**](docs/BlocklistsApi.md#deleteBlocklist) | **DELETE** /blocklists/{id} | Delete a blocklist
*BlocklistsApi* | [**getBlocklist**](docs/BlocklistsApi.md#getBlocklist) | **GET** /blocklists/{id} | Retrieve a blocklist
*BlocklistsApi* | [**getBlocklistCollection**](docs/BlocklistsApi.md#getBlocklistCollection) | **GET** /blocklists | Retrieve a list of blocklists
*BlocklistsApi* | [**postBlocklist**](docs/BlocklistsApi.md#postBlocklist) | **POST** /blocklists | Create a blocklist
*BlocklistsApi* | [**putBlocklist**](docs/BlocklistsApi.md#putBlocklist) | **PUT** /blocklists/{id} | Create a blocklist with predefined ID
*Class3DSecureApi* | [**get3DSecure**](docs/Class3DSecureApi.md#get3DSecure) | **GET** /3dsecure/{id} | Retrieve a ThreeDSecure entry
*Class3DSecureApi* | [**get3DSecureCollection**](docs/Class3DSecureApi.md#get3DSecureCollection) | **GET** /3dsecure | Retrieve a list of ThreeDSecure entries
*Class3DSecureApi* | [**post3DSecure**](docs/Class3DSecureApi.md#post3DSecure) | **POST** /3dsecure | Create a ThreeDSecure entry
*CouponsApi* | [**getCoupon**](docs/CouponsApi.md#getCoupon) | **GET** /coupons/{id} | Retrieve a coupon
*CouponsApi* | [**getCouponCollection**](docs/CouponsApi.md#getCouponCollection) | **GET** /coupons | Retrieve a list of coupons
*CouponsApi* | [**getCouponRedemption**](docs/CouponsApi.md#getCouponRedemption) | **GET** /coupons-redemptions/{id} | Retrieve a coupon redemption with specified identifier string
*CouponsApi* | [**getCouponRedemptionCollection**](docs/CouponsApi.md#getCouponRedemptionCollection) | **GET** /coupons-redemptions | Retrieve a list of coupon redemptions
*CouponsApi* | [**postCoupon**](docs/CouponsApi.md#postCoupon) | **POST** /coupons | Create a coupon
*CouponsApi* | [**postCouponExpiration**](docs/CouponsApi.md#postCouponExpiration) | **POST** /coupons/{id}/expiration | Set a coupon&#39;s expiration time
*CouponsApi* | [**postCouponRedemption**](docs/CouponsApi.md#postCouponRedemption) | **POST** /coupons-redemptions | Redeem a coupon
*CouponsApi* | [**postCouponRedemptionCancellation**](docs/CouponsApi.md#postCouponRedemptionCancellation) | **POST** /coupons-redemptions/{id}/cancel | Cancel a coupon redemption
*CouponsApi* | [**putCoupon**](docs/CouponsApi.md#putCoupon) | **PUT** /coupons/{id} | Create or update a coupon with predefined coupon ID
*CustomFieldsApi* | [**getCustomField**](docs/CustomFieldsApi.md#getCustomField) | **GET** /custom-fields/{resource}/{name} | Retrieve a Custom Field
*CustomFieldsApi* | [**getCustomFieldCollection**](docs/CustomFieldsApi.md#getCustomFieldCollection) | **GET** /custom-fields/{resource} | Retrieve Custom Fields
*CustomFieldsApi* | [**putCustomField**](docs/CustomFieldsApi.md#putCustomField) | **PUT** /custom-fields/{resource}/{name} | Create or alter a Custom Field
*CustomerAuthenticationApi* | [**deleteAuthenticationToken**](docs/CustomerAuthenticationApi.md#deleteAuthenticationToken) | **DELETE** /authentication-tokens/{token} | Logout a customer
*CustomerAuthenticationApi* | [**deleteCredential**](docs/CustomerAuthenticationApi.md#deleteCredential) | **DELETE** /credentials/{id} | Delete a credential
*CustomerAuthenticationApi* | [**deletePasswordToken**](docs/CustomerAuthenticationApi.md#deletePasswordToken) | **DELETE** /password-tokens/{id} | Delete a Reset Password Token
*CustomerAuthenticationApi* | [**getAuthenticationOption**](docs/CustomerAuthenticationApi.md#getAuthenticationOption) | **GET** /authentication-options | Read current authentication options
*CustomerAuthenticationApi* | [**getAuthenticationTokenCollection**](docs/CustomerAuthenticationApi.md#getAuthenticationTokenCollection) | **GET** /authentication-tokens | Retrieve a list of auth tokens
*CustomerAuthenticationApi* | [**getAuthenticationTokenVerification**](docs/CustomerAuthenticationApi.md#getAuthenticationTokenVerification) | **GET** /authentication-tokens/{token} | Verify
*CustomerAuthenticationApi* | [**getCredential**](docs/CustomerAuthenticationApi.md#getCredential) | **GET** /credentials/{id} | Retrieve a credential
*CustomerAuthenticationApi* | [**getCredentialCollection**](docs/CustomerAuthenticationApi.md#getCredentialCollection) | **GET** /credentials | Retrieve a list of credentials
*CustomerAuthenticationApi* | [**getPasswordToken**](docs/CustomerAuthenticationApi.md#getPasswordToken) | **GET** /password-tokens/{id} | Retrieve a Reset Password Token
*CustomerAuthenticationApi* | [**getPasswordTokenCollection**](docs/CustomerAuthenticationApi.md#getPasswordTokenCollection) | **GET** /password-tokens | Retrieve a list of tokens
*CustomerAuthenticationApi* | [**postAuthenticationToken**](docs/CustomerAuthenticationApi.md#postAuthenticationToken) | **POST** /authentication-tokens | Login
*CustomerAuthenticationApi* | [**postAuthenticationTokenExchange**](docs/CustomerAuthenticationApi.md#postAuthenticationTokenExchange) | **POST** /authentication-tokens/{token}/exchange | Exchange
*CustomerAuthenticationApi* | [**postCredential**](docs/CustomerAuthenticationApi.md#postCredential) | **POST** /credentials | Create a credential
*CustomerAuthenticationApi* | [**postPasswordToken**](docs/CustomerAuthenticationApi.md#postPasswordToken) | **POST** /password-tokens | Create a Reset Password Token
*CustomerAuthenticationApi* | [**putAuthenticationOption**](docs/CustomerAuthenticationApi.md#putAuthenticationOption) | **PUT** /authentication-options | Change authentication options
*CustomerAuthenticationApi* | [**putCredential**](docs/CustomerAuthenticationApi.md#putCredential) | **PUT** /credentials/{id} | Create or update a credential with predefined ID
*CustomersApi* | [**deleteCustomer**](docs/CustomersApi.md#deleteCustomer) | **DELETE** /customers/{id} | Merge and delete a customer
*CustomersApi* | [**deleteCustomerLeadSource**](docs/CustomersApi.md#deleteCustomerLeadSource) | **DELETE** /customers/{id}/lead-source | Delete a Lead Source for a customer
*CustomersApi* | [**getCustomer**](docs/CustomersApi.md#getCustomer) | **GET** /customers/{id} | Retrieve a customer
*CustomersApi* | [**getCustomerCollection**](docs/CustomersApi.md#getCustomerCollection) | **GET** /customers | Retrieve a list of customers
*CustomersApi* | [**getCustomerLeadSource**](docs/CustomersApi.md#getCustomerLeadSource) | **GET** /customers/{id}/lead-source | Retrieve a customer&#39;s Lead Source
*CustomersApi* | [**postCustomer**](docs/CustomersApi.md#postCustomer) | **POST** /customers | Create a customer (without an ID)
*CustomersApi* | [**postCustomerTimelineCustomEventType**](docs/CustomersApi.md#postCustomerTimelineCustomEventType) | **POST** /customer-timeline-custom-events | Create Customer Timeline custom event type
*CustomersApi* | [**putCustomer**](docs/CustomersApi.md#putCustomer) | **PUT** /customers/{id} | Upsert a customer with predefined ID
*CustomersApi* | [**putCustomerLeadSource**](docs/CustomersApi.md#putCustomerLeadSource) | **PUT** /customers/{id}/lead-source | Create a Lead Source for a customer
*CustomersTimelineApi* | [**deleteCustomerTimeline**](docs/CustomersTimelineApi.md#deleteCustomerTimeline) | **DELETE** /customers/{id}/timeline/{messageId} | Delete a Customer Timeline message
*CustomersTimelineApi* | [**getCustomerTimeline**](docs/CustomersTimelineApi.md#getCustomerTimeline) | **GET** /customers/{id}/timeline/{messageId} | Retrieve a customer Timeline message
*CustomersTimelineApi* | [**getCustomerTimelineCollection**](docs/CustomersTimelineApi.md#getCustomerTimelineCollection) | **GET** /customers/{id}/timeline | Retrieve a list of customer timeline messages
*CustomersTimelineApi* | [**getCustomerTimelineCustomEventType**](docs/CustomersTimelineApi.md#getCustomerTimelineCustomEventType) | **GET** /customer-timeline-custom-events/{id} | Retrieve customer timeline custom event type with specified identifier string
*CustomersTimelineApi* | [**getCustomerTimelineCustomEventTypeCollection**](docs/CustomersTimelineApi.md#getCustomerTimelineCustomEventTypeCollection) | **GET** /customer-timeline-custom-events | Retrieve a list of customer timeline custom event types
*CustomersTimelineApi* | [**getCustomerTimelineEventCollection**](docs/CustomersTimelineApi.md#getCustomerTimelineEventCollection) | **GET** /customer-timeline-events | Retrieve a list of customer timeline messages for all customers
*CustomersTimelineApi* | [**postCustomerTimeline**](docs/CustomersTimelineApi.md#postCustomerTimeline) | **POST** /customers/{id}/timeline | Create a customer Timeline comment or custom defined event
*DisputesApi* | [**getDispute**](docs/DisputesApi.md#getDispute) | **GET** /disputes/{id} | Retrieve a dispute
*DisputesApi* | [**getDisputeCollection**](docs/DisputesApi.md#getDisputeCollection) | **GET** /disputes | Retrieve a list of disputes
*DisputesApi* | [**postDispute**](docs/DisputesApi.md#postDispute) | **POST** /disputes | Create a dispute
*DisputesApi* | [**putDispute**](docs/DisputesApi.md#putDispute) | **PUT** /disputes/{id} | Create or update a Dispute with predefined ID
*FilesApi* | [**deleteAttachment**](docs/FilesApi.md#deleteAttachment) | **DELETE** /attachments/{id} | Delete an Attachment
*FilesApi* | [**deleteFile**](docs/FilesApi.md#deleteFile) | **DELETE** /files/{id} | Delete a File
*FilesApi* | [**getAttachment**](docs/FilesApi.md#getAttachment) | **GET** /attachments/{id} | Retrieve an Attachment
*FilesApi* | [**getAttachmentCollection**](docs/FilesApi.md#getAttachmentCollection) | **GET** /attachments | Retrieve a list of Attachments
*FilesApi* | [**getFile**](docs/FilesApi.md#getFile) | **GET** /files/{id} | Retrieve a File Record
*FilesApi* | [**getFileCollection**](docs/FilesApi.md#getFileCollection) | **GET** /files | Retrieve a list of files
*FilesApi* | [**getFileDownload**](docs/FilesApi.md#getFileDownload) | **GET** /files/{id}/download | Download a file
*FilesApi* | [**getFileDownloadExtension**](docs/FilesApi.md#getFileDownloadExtension) | **GET** /files/{id}/download{extension} | Download image in specific format
*FilesApi* | [**postAttachment**](docs/FilesApi.md#postAttachment) | **POST** /attachments | Create an Attachment
*FilesApi* | [**postFile**](docs/FilesApi.md#postFile) | **POST** /files | Create a file
*FilesApi* | [**putAttachment**](docs/FilesApi.md#putAttachment) | **PUT** /attachments/{id} | Update the Attachment with predefined ID
*FilesApi* | [**putFile**](docs/FilesApi.md#putFile) | **PUT** /files/{id} | Update the File with predefined ID
*InvoicesApi* | [**deleteInvoiceTimeline**](docs/InvoicesApi.md#deleteInvoiceTimeline) | **DELETE** /invoices/{id}/timeline/{messageId} | Delete an Invoice Timeline message
*InvoicesApi* | [**getCustomerUpcomingInvoiceCollection**](docs/InvoicesApi.md#getCustomerUpcomingInvoiceCollection) | **GET** /customers/{id}/upcoming-invoices | Retrieve customer&#39;s upcoming invoices
*InvoicesApi* | [**getInvoice**](docs/InvoicesApi.md#getInvoice) | **GET** /invoices/{id} | Retrieve an invoice
*InvoicesApi* | [**getInvoiceCollection**](docs/InvoicesApi.md#getInvoiceCollection) | **GET** /invoices | Retrieve a list of invoices
*InvoicesApi* | [**getInvoiceItemCollection**](docs/InvoicesApi.md#getInvoiceItemCollection) | **GET** /invoices/{id}/items | Retrieve invoice items
*InvoicesApi* | [**getInvoiceTimeline**](docs/InvoicesApi.md#getInvoiceTimeline) | **GET** /invoices/{id}/timeline/{messageId} | Retrieve an Invoice Timeline message
*InvoicesApi* | [**getInvoiceTimelineCollection**](docs/InvoicesApi.md#getInvoiceTimelineCollection) | **GET** /invoices/{id}/timeline | Retrieve a list of invoice timeline messages
*InvoicesApi* | [**getInvoiceTransactionAllocationCollection**](docs/InvoicesApi.md#getInvoiceTransactionAllocationCollection) | **GET** /invoices/{id}/transaction-allocations | Get transaction amounts allocated to an invoice
*InvoicesApi* | [**postInvoice**](docs/InvoicesApi.md#postInvoice) | **POST** /invoices | Create an invoice
*InvoicesApi* | [**postInvoiceAbandonment**](docs/InvoicesApi.md#postInvoiceAbandonment) | **POST** /invoices/{id}/abandon | Abandon an invoice
*InvoicesApi* | [**postInvoiceIssuance**](docs/InvoicesApi.md#postInvoiceIssuance) | **POST** /invoices/{id}/issue | Issue an invoice
*InvoicesApi* | [**postInvoiceItem**](docs/InvoicesApi.md#postInvoiceItem) | **POST** /invoices/{id}/items | Create an invoice item
*InvoicesApi* | [**postInvoiceRecalculation**](docs/InvoicesApi.md#postInvoiceRecalculation) | **POST** /invoices/{id}/recalculate | Recalculate an invoice
*InvoicesApi* | [**postInvoiceReissuance**](docs/InvoicesApi.md#postInvoiceReissuance) | **POST** /invoices/{id}/reissue | Reissue an invoice
*InvoicesApi* | [**postInvoiceTimeline**](docs/InvoicesApi.md#postInvoiceTimeline) | **POST** /invoices/{id}/timeline | Create an invoice Timeline comment
*InvoicesApi* | [**postInvoiceTransaction**](docs/InvoicesApi.md#postInvoiceTransaction) | **POST** /invoices/{id}/transaction | Apply a transaction to an invoice
*InvoicesApi* | [**postInvoiceVoid**](docs/InvoicesApi.md#postInvoiceVoid) | **POST** /invoices/{id}/void | Void an invoice
*InvoicesApi* | [**putInvoice**](docs/InvoicesApi.md#putInvoice) | **PUT** /invoices/{id} | Create or update an invoice with predefined ID
*KycDocumentsApi* | [**deleteKycRequest**](docs/KycDocumentsApi.md#deleteKycRequest) | **DELETE** /kyc-requests/{id} | Delete the KYC request
*KycDocumentsApi* | [**getKycDocument**](docs/KycDocumentsApi.md#getKycDocument) | **GET** /kyc-documents/{id} | Retrieve a KYC Document
*KycDocumentsApi* | [**getKycDocumentCollection**](docs/KycDocumentsApi.md#getKycDocumentCollection) | **GET** /kyc-documents | Retrieve a list of KYC documents
*KycDocumentsApi* | [**getKycRequest**](docs/KycDocumentsApi.md#getKycRequest) | **GET** /kyc-requests/{id} | Retrieve a KYC request
*KycDocumentsApi* | [**getKycRequestCollection**](docs/KycDocumentsApi.md#getKycRequestCollection) | **GET** /kyc-requests | Retrieve a list of KYC requests
*KycDocumentsApi* | [**patchKycRequest**](docs/KycDocumentsApi.md#patchKycRequest) | **PATCH** /kyc-requests/{id} | Update a KYC request
*KycDocumentsApi* | [**postKycDocument**](docs/KycDocumentsApi.md#postKycDocument) | **POST** /kyc-documents | Create a KYC Document
*KycDocumentsApi* | [**postKycDocumentAcceptance**](docs/KycDocumentsApi.md#postKycDocumentAcceptance) | **POST** /kyc-documents/{id}/acceptance | Accept a KYC document
*KycDocumentsApi* | [**postKycDocumentMatches**](docs/KycDocumentsApi.md#postKycDocumentMatches) | **POST** /kyc-documents/{id}/matches | Update a KYC document&#39;s documentMatches
*KycDocumentsApi* | [**postKycDocumentRejection**](docs/KycDocumentsApi.md#postKycDocumentRejection) | **POST** /kyc-documents/{id}/rejection | Reject a KYC document
*KycDocumentsApi* | [**postKycDocumentReview**](docs/KycDocumentsApi.md#postKycDocumentReview) | **POST** /kyc-documents/{id}/review | Review a KYC document
*KycDocumentsApi* | [**postKycRequest**](docs/KycDocumentsApi.md#postKycRequest) | **POST** /kyc-requests | Create a KYC Request
*KycDocumentsApi* | [**putKycDocument**](docs/KycDocumentsApi.md#putKycDocument) | **PUT** /kyc-documents/{id} | Create or update a KYC document with predefined ID
*OrdersApi* | [**deleteSubscriptionCancellation**](docs/OrdersApi.md#deleteSubscriptionCancellation) | **DELETE** /subscription-cancellations/{id} | Delete a cancellation
*OrdersApi* | [**deleteSubscriptionTimeline**](docs/OrdersApi.md#deleteSubscriptionTimeline) | **DELETE** /subscriptions/{id}/timeline/{messageId} | Delete an Order Timeline message
*OrdersApi* | [**getSubscription**](docs/OrdersApi.md#getSubscription) | **GET** /subscriptions/{id} | Retrieve an order
*OrdersApi* | [**getSubscriptionCancellation**](docs/OrdersApi.md#getSubscriptionCancellation) | **GET** /subscription-cancellations/{id} | Retrieve an order сancellation
*OrdersApi* | [**getSubscriptionCancellationCollection**](docs/OrdersApi.md#getSubscriptionCancellationCollection) | **GET** /subscription-cancellations | Retrieve a list of cancellations
*OrdersApi* | [**getSubscriptionCollection**](docs/OrdersApi.md#getSubscriptionCollection) | **GET** /subscriptions | Retrieve a list of orders
*OrdersApi* | [**getSubscriptionReactivation**](docs/OrdersApi.md#getSubscriptionReactivation) | **GET** /subscription-reactivations/{id} | Retrieve an order reactivation
*OrdersApi* | [**getSubscriptionReactivationCollection**](docs/OrdersApi.md#getSubscriptionReactivationCollection) | **GET** /subscription-reactivations | Retrieve a list of reactivations
*OrdersApi* | [**getSubscriptionTimeline**](docs/OrdersApi.md#getSubscriptionTimeline) | **GET** /subscriptions/{id}/timeline/{messageId} | Retrieve an Order Timeline message
*OrdersApi* | [**getSubscriptionTimelineCollection**](docs/OrdersApi.md#getSubscriptionTimelineCollection) | **GET** /subscriptions/{id}/timeline | Retrieve a list of order timeline messages
*OrdersApi* | [**getSubscriptionUpcomingInvoiceCollection**](docs/OrdersApi.md#getSubscriptionUpcomingInvoiceCollection) | **GET** /subscriptions/{id}/upcoming-invoices | Retrieve subscription order&#39;s upcoming invoice
*OrdersApi* | [**postSubscription**](docs/OrdersApi.md#postSubscription) | **POST** /subscriptions | Create an order
*OrdersApi* | [**postSubscriptionCancellation**](docs/OrdersApi.md#postSubscriptionCancellation) | **POST** /subscription-cancellations | Cancel an order
*OrdersApi* | [**postSubscriptionInterimInvoice**](docs/OrdersApi.md#postSubscriptionInterimInvoice) | **POST** /subscriptions/{id}/interim-invoice | Issue an interim invoice for a subscription order
*OrdersApi* | [**postSubscriptionItemsChange**](docs/OrdersApi.md#postSubscriptionItemsChange) | **POST** /subscriptions/{id}/change-items | Change an order&#39;s items
*OrdersApi* | [**postSubscriptionReactivation**](docs/OrdersApi.md#postSubscriptionReactivation) | **POST** /subscription-reactivations | Reactivate an order
*OrdersApi* | [**postSubscriptionTimeline**](docs/OrdersApi.md#postSubscriptionTimeline) | **POST** /subscriptions/{id}/timeline | Create an order Timeline comment
*OrdersApi* | [**postUpcomingInvoiceIssuance**](docs/OrdersApi.md#postUpcomingInvoiceIssuance) | **POST** /subscriptions/{id}/upcoming-invoices/{invoiceId}/issue | Issue an upcoming invoice for early pay
*OrdersApi* | [**putSubscription**](docs/OrdersApi.md#putSubscription) | **PUT** /subscriptions/{id} | Upsert an order with predefined ID
*OrdersApi* | [**putSubscriptionCancellation**](docs/OrdersApi.md#putSubscriptionCancellation) | **PUT** /subscription-cancellations/{id} | Cancel an order
*PayPalAccountsApi* | [**getPayPalAccount**](docs/PayPalAccountsApi.md#getPayPalAccount) | **GET** /paypal-accounts/{id} | Retrieve a PayPal Account
*PayPalAccountsApi* | [**getPayPalAccountCollection**](docs/PayPalAccountsApi.md#getPayPalAccountCollection) | **GET** /paypal-accounts | Retrieve a list of PayPal accounts
*PayPalAccountsApi* | [**postPayPalAccount**](docs/PayPalAccountsApi.md#postPayPalAccount) | **POST** /paypal-accounts | Create a PayPal Account
*PayPalAccountsApi* | [**postPayPalAccountDeactivation**](docs/PayPalAccountsApi.md#postPayPalAccountDeactivation) | **POST** /paypal-accounts/{id}/deactivation | Deactivate a PayPal Account
*PayPalAccountsApi* | [**putPayPalAccount**](docs/PayPalAccountsApi.md#putPayPalAccount) | **PUT** /paypal-accounts/{id} | Create a PayPal account with predefined ID
*PaymentCardsApi* | [**getPaymentCard**](docs/PaymentCardsApi.md#getPaymentCard) | **GET** /payment-cards/{id} | Retrieve a Payment Card
*PaymentCardsApi* | [**getPaymentCardCollection**](docs/PaymentCardsApi.md#getPaymentCardCollection) | **GET** /payment-cards | Retrieve a list of Payment Cards
*PaymentCardsApi* | [**patchPaymentCard**](docs/PaymentCardsApi.md#patchPaymentCard) | **PATCH** /payment-cards/{id} | Update a payment card&#39;s values
*PaymentCardsApi* | [**postPaymentCard**](docs/PaymentCardsApi.md#postPaymentCard) | **POST** /payment-cards | Create a Payment Card
*PaymentCardsApi* | [**postPaymentCardDeactivation**](docs/PaymentCardsApi.md#postPaymentCardDeactivation) | **POST** /payment-cards/{id}/deactivation | Deactivate a Payment Card
*PaymentCardsApi* | [**putPaymentCard**](docs/PaymentCardsApi.md#putPaymentCard) | **PUT** /payment-cards/{id} | Create a payment card with predefined ID
*PaymentInstrumentsApi* | [**getPaymentInstrument**](docs/PaymentInstrumentsApi.md#getPaymentInstrument) | **GET** /payment-instruments/{id} | Retrieve a Payment Instrument
*PaymentInstrumentsApi* | [**getPaymentInstrumentCollection**](docs/PaymentInstrumentsApi.md#getPaymentInstrumentCollection) | **GET** /payment-instruments | Retrieve a list of payment instruments
*PaymentInstrumentsApi* | [**patchPaymentInstrument**](docs/PaymentInstrumentsApi.md#patchPaymentInstrument) | **PATCH** /payment-instruments/{id} | Update a Payment Instrument&#39;s values
*PaymentInstrumentsApi* | [**postPaymentInstrument**](docs/PaymentInstrumentsApi.md#postPaymentInstrument) | **POST** /payment-instruments | Create a Payment Instrument
*PaymentInstrumentsApi* | [**postPaymentInstrumentDeactivation**](docs/PaymentInstrumentsApi.md#postPaymentInstrumentDeactivation) | **POST** /payment-instruments/{id}/deactivation | Deactivate a payment instrument
*PaymentTokensApi* | [**getToken**](docs/PaymentTokensApi.md#getToken) | **GET** /tokens/{token} | Retrieve a token
*PaymentTokensApi* | [**getTokenCollection**](docs/PaymentTokensApi.md#getTokenCollection) | **GET** /tokens | Retrieve a list of tokens
*PaymentTokensApi* | [**postDigitalWalletValidation**](docs/PaymentTokensApi.md#postDigitalWalletValidation) | **POST** /digital-wallets/validation | Validate a digital wallet session
*PaymentTokensApi* | [**postToken**](docs/PaymentTokensApi.md#postToken) | **POST** /tokens | Create a payment token
*PlansApi* | [**deletePlan**](docs/PlansApi.md#deletePlan) | **DELETE** /plans/{id} | Delete a Plan
*PlansApi* | [**getPlan**](docs/PlansApi.md#getPlan) | **GET** /plans/{id} | Retrieve a plan
*PlansApi* | [**getPlanCollection**](docs/PlansApi.md#getPlanCollection) | **GET** /plans | Retrieve a list of plans
*PlansApi* | [**postPlan**](docs/PlansApi.md#postPlan) | **POST** /plans | Create a plan
*PlansApi* | [**putPlan**](docs/PlansApi.md#putPlan) | **PUT** /plans/{id} | Create or update a Plan with predefined ID
*ProductsApi* | [**deleteProduct**](docs/ProductsApi.md#deleteProduct) | **DELETE** /products/{id} | Delete a product
*ProductsApi* | [**getProduct**](docs/ProductsApi.md#getProduct) | **GET** /products/{id} | Retrieve a product
*ProductsApi* | [**getProductCollection**](docs/ProductsApi.md#getProductCollection) | **GET** /products | Retrieve a list of products
*ProductsApi* | [**postProduct**](docs/ProductsApi.md#postProduct) | **POST** /products | Create a Product
*ProductsApi* | [**putProduct**](docs/ProductsApi.md#putProduct) | **PUT** /products/{id} | Create a product with predefined ID
*SearchApi* | [**getSearch**](docs/SearchApi.md#getSearch) | **GET** /search | Search merchant data
*ShippingZonesApi* | [**deleteShippingZone**](docs/ShippingZonesApi.md#deleteShippingZone) | **DELETE** /shipping-zones/{id} | Delete a shipping zone
*ShippingZonesApi* | [**getShippingZone**](docs/ShippingZonesApi.md#getShippingZone) | **GET** /shipping-zones/{id} | Retrieve a shipping zone
*ShippingZonesApi* | [**getShippingZoneCollection**](docs/ShippingZonesApi.md#getShippingZoneCollection) | **GET** /shipping-zones | Retrieve a list of shipping zones
*ShippingZonesApi* | [**postShippingZone**](docs/ShippingZonesApi.md#postShippingZone) | **POST** /shipping-zones | Create a Shipping Zone
*ShippingZonesApi* | [**putShippingZone**](docs/ShippingZonesApi.md#putShippingZone) | **PUT** /shipping-zones/{id} | Create a shipping zone with predefined ID
*TagsApi* | [**deleteTag**](docs/TagsApi.md#deleteTag) | **DELETE** /tags/{tag} | Delete a tag
*TagsApi* | [**deleteTagCustomer**](docs/TagsApi.md#deleteTagCustomer) | **DELETE** /tags/{tag}/customers/{customerId} | Untag a customer
*TagsApi* | [**deleteTagCustomerCollection**](docs/TagsApi.md#deleteTagCustomerCollection) | **DELETE** /tags/{tag}/customers | Untag a list of customers
*TagsApi* | [**getTag**](docs/TagsApi.md#getTag) | **GET** /tags/{tag} | Retrieve a tag
*TagsApi* | [**getTagCollection**](docs/TagsApi.md#getTagCollection) | **GET** /tags | Retrieve a list of tags
*TagsApi* | [**patchTag**](docs/TagsApi.md#patchTag) | **PATCH** /tags/{tag} | Update a tag
*TagsApi* | [**postTag**](docs/TagsApi.md#postTag) | **POST** /tags | Create a tag
*TagsApi* | [**postTagCustomer**](docs/TagsApi.md#postTagCustomer) | **POST** /tags/{tag}/customers/{customerId} | Tag a customer
*TagsApi* | [**postTagCustomerCollection**](docs/TagsApi.md#postTagCustomerCollection) | **POST** /tags/{tag}/customers | Tag a list of customers
*TransactionsApi* | [**deleteTransactionTimeline**](docs/TransactionsApi.md#deleteTransactionTimeline) | **DELETE** /transactions/{id}/timeline/{messageId} | Delete a Transaction Timeline message
*TransactionsApi* | [**getTransaction**](docs/TransactionsApi.md#getTransaction) | **GET** /transactions/{id} | Retrieve a Transaction
*TransactionsApi* | [**getTransactionCollection**](docs/TransactionsApi.md#getTransactionCollection) | **GET** /transactions | Retrieve a list of transactions
*TransactionsApi* | [**getTransactionTimeline**](docs/TransactionsApi.md#getTransactionTimeline) | **GET** /transactions/{id}/timeline/{messageId} | Retrieve a transaction Timeline message
*TransactionsApi* | [**getTransactionTimelineCollection**](docs/TransactionsApi.md#getTransactionTimelineCollection) | **GET** /transactions/{id}/timeline | Retrieve a list of transaction timeline messages
*TransactionsApi* | [**patchTransaction**](docs/TransactionsApi.md#patchTransaction) | **PATCH** /transactions/{id} | Update a transaction
*TransactionsApi* | [**postPayout**](docs/TransactionsApi.md#postPayout) | **POST** /payouts | Create a credit transaction
*TransactionsApi* | [**postReadyToPay**](docs/TransactionsApi.md#postReadyToPay) | **POST** /ready-to-pay | Ready to Pay
*TransactionsApi* | [**postTransaction**](docs/TransactionsApi.md#postTransaction) | **POST** /transactions | Create a transaction
*TransactionsApi* | [**postTransactionQuery**](docs/TransactionsApi.md#postTransactionQuery) | **POST** /transactions/{id}/query | Query a Transaction
*TransactionsApi* | [**postTransactionRefund**](docs/TransactionsApi.md#postTransactionRefund) | **POST** /transactions/{id}/refund | Refund a Transaction
*TransactionsApi* | [**postTransactionTimeline**](docs/TransactionsApi.md#postTransactionTimeline) | **POST** /transactions/{id}/timeline | Create a transaction Timeline comment
*TransactionsApi* | [**postTransactionUpdate**](docs/TransactionsApi.md#postTransactionUpdate) | **POST** /transactions/{id}/update | Update a Transaction status


## Documentation for Models

 - [A1Gateway](docs/A1Gateway.md)
 - [A1Gateway3dsServers](docs/A1Gateway3dsServers.md)
 - [A1GatewayAllOfCredentials](docs/A1GatewayAllOfCredentials.md)
 - [AML](docs/AML.md)
 - [AMLAddressInner](docs/AMLAddressInner.md)
 - [AMLAliasesInner](docs/AMLAliasesInner.md)
 - [AMLPassportInner](docs/AMLPassportInner.md)
 - [AchPlaidFeature](docs/AchPlaidFeature.md)
 - [AclInner](docs/AclInner.md)
 - [AcquirerName](docs/AcquirerName.md)
 - [AddressMatches](docs/AddressMatches.md)
 - [Adyen](docs/Adyen.md)
 - [AdyenAllOfCredentials](docs/AdyenAllOfCredentials.md)
 - [AdyenAllOfSettings](docs/AdyenAllOfSettings.md)
 - [Airpay](docs/Airpay.md)
 - [AirpayAllOfCredentials](docs/AirpayAllOfCredentials.md)
 - [AlternativePaymentInstrument](docs/AlternativePaymentInstrument.md)
 - [AlternativePaymentInstrument2](docs/AlternativePaymentInstrument2.md)
 - [AlternativePaymentInstrument2EmbeddedInner](docs/AlternativePaymentInstrument2EmbeddedInner.md)
 - [AlternativePaymentInstrument2LinksInner](docs/AlternativePaymentInstrument2LinksInner.md)
 - [AlternativePaymentMethods](docs/AlternativePaymentMethods.md)
 - [AlternativePaymentToken](docs/AlternativePaymentToken.md)
 - [AmexVPC](docs/AmexVPC.md)
 - [AmexVPCAllOfCredentials](docs/AmexVPCAllOfCredentials.md)
 - [AmexVPCAllOfSettings](docs/AmexVPCAllOfSettings.md)
 - [AmountAdjustment](docs/AmountAdjustment.md)
 - [ApcoPay](docs/ApcoPay.md)
 - [ApcoPayAllOfCredentials](docs/ApcoPayAllOfCredentials.md)
 - [ApcoPayAllOfSettings](docs/ApcoPayAllOfSettings.md)
 - [ApiKeyScope](docs/ApiKeyScope.md)
 - [ApplePayValidation](docs/ApplePayValidation.md)
 - [ApplePayValidationAllOfValidationRequest](docs/ApplePayValidationAllOfValidationRequest.md)
 - [ApprovalUrlLink](docs/ApprovalUrlLink.md)
 - [AsiaPaymentGateway](docs/AsiaPaymentGateway.md)
 - [AsiaPaymentGatewayAllOfCredentials](docs/AsiaPaymentGatewayAllOfCredentials.md)
 - [AstroPayCard](docs/AstroPayCard.md)
 - [AstroPayCardAllOfCredentials](docs/AstroPayCardAllOfCredentials.md)
 - [AstroPayCardAllOfSettings](docs/AstroPayCardAllOfSettings.md)
 - [Attachment](docs/Attachment.md)
 - [AttachmentEmbeddedInner](docs/AttachmentEmbeddedInner.md)
 - [AttachmentLinksInner](docs/AttachmentLinksInner.md)
 - [AttachmentResourceLink](docs/AttachmentResourceLink.md)
 - [AuthTransactionEmbed](docs/AuthTransactionEmbed.md)
 - [AuthTransactionLink](docs/AuthTransactionLink.md)
 - [AuthenticationOptions](docs/AuthenticationOptions.md)
 - [AuthenticationToken](docs/AuthenticationToken.md)
 - [AuthenticationTokenMetadata](docs/AuthenticationTokenMetadata.md)
 - [AuthorizeNet](docs/AuthorizeNet.md)
 - [AuthorizeNetAllOfCredentials](docs/AuthorizeNetAllOfCredentials.md)
 - [Auto](docs/Auto.md)
 - [BBANInstrument](docs/BBANInstrument.md)
 - [BBANType](docs/BBANType.md)
 - [Bambora](docs/Bambora.md)
 - [BamboraAllOfCredentials](docs/BamboraAllOfCredentials.md)
 - [BankAccount](docs/BankAccount.md)
 - [BankAccountAllOfEmbedded](docs/BankAccountAllOfEmbedded.md)
 - [BankAccountAllOfLinks](docs/BankAccountAllOfLinks.md)
 - [BankAccountCreatePlain](docs/BankAccountCreatePlain.md)
 - [BankAccountCreateToken](docs/BankAccountCreateToken.md)
 - [BankAccountEmbed](docs/BankAccountEmbed.md)
 - [BankAccountInstrument](docs/BankAccountInstrument.md)
 - [BankAccountToken](docs/BankAccountToken.md)
 - [BankAccountUpdatePlain](docs/BankAccountUpdatePlain.md)
 - [BitPay](docs/BitPay.md)
 - [BitPayAllOfCredentials](docs/BitPayAllOfCredentials.md)
 - [BlankProblem](docs/BlankProblem.md)
 - [Blocklist](docs/Blocklist.md)
 - [BlueSnap](docs/BlueSnap.md)
 - [BlueSnapAllOfCredentials](docs/BlueSnapAllOfCredentials.md)
 - [BraintreePayments](docs/BraintreePayments.md)
 - [BraintreePaymentsAllOfCredentials](docs/BraintreePaymentsAllOfCredentials.md)
 - [BrowserData](docs/BrowserData.md)
 - [CASHlib](docs/CASHlib.md)
 - [CASHlibAllOfCredentials](docs/CASHlibAllOfCredentials.md)
 - [CCAvenue](docs/CCAvenue.md)
 - [CCAvenueAllOfCredentials](docs/CCAvenueAllOfCredentials.md)
 - [CODVoucher](docs/CODVoucher.md)
 - [CODVoucherAllOfCredentials](docs/CODVoucherAllOfCredentials.md)
 - [CardinalCommerce3dsServer](docs/CardinalCommerce3dsServer.md)
 - [Cardknox](docs/Cardknox.md)
 - [CardknoxAllOfCredentials](docs/CardknoxAllOfCredentials.md)
 - [CashInstrument](docs/CashInstrument.md)
 - [CashToCode](docs/CashToCode.md)
 - [CashToCodeAllOfCredentials](docs/CashToCodeAllOfCredentials.md)
 - [CashToCodeAllOfSettings](docs/CashToCodeAllOfSettings.md)
 - [Cashflows](docs/Cashflows.md)
 - [CashflowsAllOfCredentials](docs/CashflowsAllOfCredentials.md)
 - [CauriPayment](docs/CauriPayment.md)
 - [CauriPaymentAllOfCredentials](docs/CauriPaymentAllOfCredentials.md)
 - [Cayan](docs/Cayan.md)
 - [CayanAllOfCredentials](docs/CayanAllOfCredentials.md)
 - [Chase](docs/Chase.md)
 - [ChaseAllOfCredentials](docs/ChaseAllOfCredentials.md)
 - [CheckInstrument](docs/CheckInstrument.md)
 - [Circle](docs/Circle.md)
 - [CircleAllOfCredentials](docs/CircleAllOfCredentials.md)
 - [Citadel](docs/Citadel.md)
 - [CitadelAllOfCredentials](docs/CitadelAllOfCredentials.md)
 - [Clearhaus](docs/Clearhaus.md)
 - [Clearhaus3dsServer](docs/Clearhaus3dsServer.md)
 - [Clearhaus3dsServers](docs/Clearhaus3dsServers.md)
 - [ClearhausAllOfCredentials](docs/ClearhausAllOfCredentials.md)
 - [CoinPayments](docs/CoinPayments.md)
 - [CoinPaymentsAllOfCredentials](docs/CoinPaymentsAllOfCredentials.md)
 - [CommonBankAccount](docs/CommonBankAccount.md)
 - [CommonInvoice](docs/CommonInvoice.md)
 - [CommonKycDocument](docs/CommonKycDocument.md)
 - [CommonKycDocumentLinksInner](docs/CommonKycDocumentLinksInner.md)
 - [CommonKycRequest](docs/CommonKycRequest.md)
 - [CommonKycRequestDocumentsInner](docs/CommonKycRequestDocumentsInner.md)
 - [CommonOneTimeOrder](docs/CommonOneTimeOrder.md)
 - [CommonPayPalAccount](docs/CommonPayPalAccount.md)
 - [CommonPaymentCard](docs/CommonPaymentCard.md)
 - [CommonPaymentToken](docs/CommonPaymentToken.md)
 - [CommonPlan](docs/CommonPlan.md)
 - [CommonPlanRecurringInterval](docs/CommonPlanRecurringInterval.md)
 - [CommonPlanSetup](docs/CommonPlanSetup.md)
 - [CommonPlanTrial](docs/CommonPlanTrial.md)
 - [CommonProduct](docs/CommonProduct.md)
 - [CommonScheduleInstruction](docs/CommonScheduleInstruction.md)
 - [CommonSubscription](docs/CommonSubscription.md)
 - [CommonSubscriptionItemsInner](docs/CommonSubscriptionItemsInner.md)
 - [CommonSubscriptionOrder](docs/CommonSubscriptionOrder.md)
 - [CommonSubscriptionOrderAllOfLineItemSubtotal](docs/CommonSubscriptionOrderAllOfLineItemSubtotal.md)
 - [CommonSubscriptionOrderAllOfRecurringInterval](docs/CommonSubscriptionOrderAllOfRecurringInterval.md)
 - [CommonSubscriptionOrderAllOfTrial](docs/CommonSubscriptionOrderAllOfTrial.md)
 - [CommonTransaction](docs/CommonTransaction.md)
 - [CommonTransactionRequest](docs/CommonTransactionRequest.md)
 - [CompositeToken](docs/CompositeToken.md)
 - [Conekta](docs/Conekta.md)
 - [ConektaAllOfCredentials](docs/ConektaAllOfCredentials.md)
 - [ContactEmailsInner](docs/ContactEmailsInner.md)
 - [ContactObject](docs/ContactObject.md)
 - [ContactPhoneNumbersInner](docs/ContactPhoneNumbersInner.md)
 - [Coppr](docs/Coppr.md)
 - [CopprAllOfCredentials](docs/CopprAllOfCredentials.md)
 - [CopprAllOfSettings](docs/CopprAllOfSettings.md)
 - [CoreReadyToPay](docs/CoreReadyToPay.md)
 - [Coupon](docs/Coupon.md)
 - [CouponExpiration](docs/CouponExpiration.md)
 - [CouponRedemption](docs/CouponRedemption.md)
 - [CouponRestriction](docs/CouponRestriction.md)
 - [Credential](docs/Credential.md)
 - [Credorax](docs/Credorax.md)
 - [CredoraxAllOfCredentials](docs/CredoraxAllOfCredentials.md)
 - [Cryptonator](docs/Cryptonator.md)
 - [CryptonatorAllOfCredentials](docs/CryptonatorAllOfCredentials.md)
 - [CustomEventScheduleInstruction](docs/CustomEventScheduleInstruction.md)
 - [CustomField](docs/CustomField.md)
 - [Customer](docs/Customer.md)
 - [CustomerAverageValue](docs/CustomerAverageValue.md)
 - [CustomerEmbed](docs/CustomerEmbed.md)
 - [CustomerEmbeddedInner](docs/CustomerEmbeddedInner.md)
 - [CustomerJWT](docs/CustomerJWT.md)
 - [CustomerLifetimeRevenue](docs/CustomerLifetimeRevenue.md)
 - [CustomerLink](docs/CustomerLink.md)
 - [CustomerLinksInner](docs/CustomerLinksInner.md)
 - [CustomerTimeline](docs/CustomerTimeline.md)
 - [CustomerTimelineCustomEvent](docs/CustomerTimelineCustomEvent.md)
 - [CyberSource](docs/CyberSource.md)
 - [CyberSourceAllOfCredentials](docs/CyberSourceAllOfCredentials.md)
 - [DLocal](docs/DLocal.md)
 - [DLocalAllOfCredentials](docs/DLocalAllOfCredentials.md)
 - [DLocalAllOfSettings](docs/DLocalAllOfSettings.md)
 - [DataCash](docs/DataCash.md)
 - [DataCash3dsServer](docs/DataCash3dsServer.md)
 - [DataCash3dsServers](docs/DataCash3dsServers.md)
 - [DataCashAllOfCredentials](docs/DataCashAllOfCredentials.md)
 - [DataCashAllOfSettings](docs/DataCashAllOfSettings.md)
 - [DateInterval](docs/DateInterval.md)
 - [DateIntervalAllOfUnit](docs/DateIntervalAllOfUnit.md)
 - [DayOfMonth](docs/DayOfMonth.md)
 - [DayOfWeek](docs/DayOfWeek.md)
 - [DayOfWeekLong](docs/DayOfWeekLong.md)
 - [DefaultPaymentInstrumentLink](docs/DefaultPaymentInstrumentLink.md)
 - [Dengi](docs/Dengi.md)
 - [DengiAllOfCredentials](docs/DengiAllOfCredentials.md)
 - [DetailedProblem](docs/DetailedProblem.md)
 - [DigitalWalletToken](docs/DigitalWalletToken.md)
 - [DigitalWalletValidation](docs/DigitalWalletValidation.md)
 - [DigitalWallets](docs/DigitalWallets.md)
 - [DigitalWalletsApplePay](docs/DigitalWalletsApplePay.md)
 - [DigitalWalletsGooglePay](docs/DigitalWalletsGooglePay.md)
 - [Directa24](docs/Directa24.md)
 - [Directa24AllOfCredentials](docs/Directa24AllOfCredentials.md)
 - [Directa24AllOfSettings](docs/Directa24AllOfSettings.md)
 - [Directa24Banks](docs/Directa24Banks.md)
 - [Discount](docs/Discount.md)
 - [DiscountsPerRedemption](docs/DiscountsPerRedemption.md)
 - [Dispute](docs/Dispute.md)
 - [DisputeEmbeddedInner](docs/DisputeEmbeddedInner.md)
 - [DisputeLink](docs/DisputeLink.md)
 - [DisputeLinksInner](docs/DisputeLinksInner.md)
 - [DocumentedProblem](docs/DocumentedProblem.md)
 - [Dragonphoenix](docs/Dragonphoenix.md)
 - [DragonphoenixAllOfCredentials](docs/DragonphoenixAllOfCredentials.md)
 - [DueTimeShiftInstruction](docs/DueTimeShiftInstruction.md)
 - [DueTimeShiftInstructionUnit](docs/DueTimeShiftInstructionUnit.md)
 - [DynamicIpnLink](docs/DynamicIpnLink.md)
 - [EBANX](docs/EBANX.md)
 - [EBANXAllOfCredentials](docs/EBANXAllOfCredentials.md)
 - [EMS](docs/EMS.md)
 - [EMS3dsServers](docs/EMS3dsServers.md)
 - [EMSAllOfCredentials](docs/EMSAllOfCredentials.md)
 - [EMSAllOfSettings](docs/EMSAllOfSettings.md)
 - [EMerchantPay](docs/EMerchantPay.md)
 - [EMerchantPay3dsServer](docs/EMerchantPay3dsServer.md)
 - [EMerchantPay3dsServers](docs/EMerchantPay3dsServers.md)
 - [EMerchantPayAllOfCredentials](docs/EMerchantPayAllOfCredentials.md)
 - [EMerchantPayAllOfSettings](docs/EMerchantPayAllOfSettings.md)
 - [EPG](docs/EPG.md)
 - [EPGAllOfCredentials](docs/EPGAllOfCredentials.md)
 - [EPro](docs/EPro.md)
 - [EProAllOfCredentials](docs/EProAllOfCredentials.md)
 - [EZeeWallet](docs/EZeeWallet.md)
 - [EZeeWalletAllOfCredentials](docs/EZeeWalletAllOfCredentials.md)
 - [EcoPayz](docs/EcoPayz.md)
 - [EcoPayzAllOfCredentials](docs/EcoPayzAllOfCredentials.md)
 - [EcoPayzAllOfSettings](docs/EcoPayzAllOfSettings.md)
 - [EcorePay](docs/EcorePay.md)
 - [EcorePayAllOfCredentials](docs/EcorePayAllOfCredentials.md)
 - [Elavon](docs/Elavon.md)
 - [ElavonAllOfCredentials](docs/ElavonAllOfCredentials.md)
 - [Error](docs/Error.md)
 - [Euteller](docs/Euteller.md)
 - [EutellerAllOfCredentials](docs/EutellerAllOfCredentials.md)
 - [EzyEFT](docs/EzyEFT.md)
 - [EzyEFTAllOfCredentials](docs/EzyEFTAllOfCredentials.md)
 - [FileCreateFromInline](docs/FileCreateFromInline.md)
 - [FileCreateFromUrl](docs/FileCreateFromUrl.md)
 - [FileDownloadLink](docs/FileDownloadLink.md)
 - [FileEmbed](docs/FileEmbed.md)
 - [FileLink](docs/FileLink.md)
 - [FileLinksInner](docs/FileLinksInner.md)
 - [FinTecSystems](docs/FinTecSystems.md)
 - [FinTecSystemsAllOfCredentials](docs/FinTecSystemsAllOfCredentials.md)
 - [FinTecSystemsAllOfSettings](docs/FinTecSystemsAllOfSettings.md)
 - [Finrax](docs/Finrax.md)
 - [FinraxAllOfCredentials](docs/FinraxAllOfCredentials.md)
 - [FinraxAllOfSettings](docs/FinraxAllOfSettings.md)
 - [Fixed](docs/Fixed.md)
 - [FixedFee](docs/FixedFee.md)
 - [FlatRate](docs/FlatRate.md)
 - [Flexepin](docs/Flexepin.md)
 - [FlexepinAllOfCredentials](docs/FlexepinAllOfCredentials.md)
 - [FlexiblePlan](docs/FlexiblePlan.md)
 - [Forte](docs/Forte.md)
 - [ForteAllOfCredentials](docs/ForteAllOfCredentials.md)
 - [FundSend](docs/FundSend.md)
 - [FundSendAllOfCredentials](docs/FundSendAllOfCredentials.md)
 - [GET](docs/GET.md)
 - [GET3dsServers](docs/GET3dsServers.md)
 - [GETAllOfCredentials](docs/GETAllOfCredentials.md)
 - [GatewayAccount](docs/GatewayAccount.md)
 - [GatewayAccountEmbed](docs/GatewayAccountEmbed.md)
 - [GatewayAccountLimit](docs/GatewayAccountLimit.md)
 - [GatewayAccountLimitLink](docs/GatewayAccountLimitLink.md)
 - [GatewayAccountLink](docs/GatewayAccountLink.md)
 - [GatewayAccountLinksInner](docs/GatewayAccountLinksInner.md)
 - [GatewayName](docs/GatewayName.md)
 - [Gigadat](docs/Gigadat.md)
 - [GigadatAllOfCredentials](docs/GigadatAllOfCredentials.md)
 - [GigadatAllOfSettings](docs/GigadatAllOfSettings.md)
 - [GlobalOne](docs/GlobalOne.md)
 - [GlobalOneAllOfCredentials](docs/GlobalOneAllOfCredentials.md)
 - [GlobalWebhookEventType](docs/GlobalWebhookEventType.md)
 - [Gooney](docs/Gooney.md)
 - [GooneyAllOfCredentials](docs/GooneyAllOfCredentials.md)
 - [Gpaysafe](docs/Gpaysafe.md)
 - [GpaysafeAllOfCredentials](docs/GpaysafeAllOfCredentials.md)
 - [Greenbox](docs/Greenbox.md)
 - [GreenboxAllOfCredentials](docs/GreenboxAllOfCredentials.md)
 - [HiPay](docs/HiPay.md)
 - [HiPayAllOfCredentials](docs/HiPayAllOfCredentials.md)
 - [IBANInstrument](docs/IBANInstrument.md)
 - [IBANType](docs/IBANType.md)
 - [ICEPAY](docs/ICEPAY.md)
 - [ICEPAYAllOfCredentials](docs/ICEPAYAllOfCredentials.md)
 - [ICanPay](docs/ICanPay.md)
 - [ICanPayAllOfCredentials](docs/ICanPayAllOfCredentials.md)
 - [ICheque](docs/ICheque.md)
 - [IChequeAllOfCredentials](docs/IChequeAllOfCredentials.md)
 - [IDebit](docs/IDebit.md)
 - [IDebitAllOfCredentials](docs/IDebitAllOfCredentials.md)
 - [INOVAPAY](docs/INOVAPAY.md)
 - [INOVAPAYAllOfCredentials](docs/INOVAPAYAllOfCredentials.md)
 - [IdentityMatches](docs/IdentityMatches.md)
 - [Ilixium](docs/Ilixium.md)
 - [Ilixium3dsServer](docs/Ilixium3dsServer.md)
 - [Ilixium3dsServers](docs/Ilixium3dsServers.md)
 - [IlixiumAllOfCredentials](docs/IlixiumAllOfCredentials.md)
 - [IlixiumAllOfSettings](docs/IlixiumAllOfSettings.md)
 - [Immediately](docs/Immediately.md)
 - [Ingenico](docs/Ingenico.md)
 - [Ingenico3dsServer](docs/Ingenico3dsServer.md)
 - [Ingenico3dsServers](docs/Ingenico3dsServers.md)
 - [IngenicoAllOfCredentials](docs/IngenicoAllOfCredentials.md)
 - [InitialInvoiceEmbed](docs/InitialInvoiceEmbed.md)
 - [InitialInvoiceLink](docs/InitialInvoiceLink.md)
 - [Inovio](docs/Inovio.md)
 - [Inovio3dsServer](docs/Inovio3dsServer.md)
 - [Inovio3dsServers](docs/Inovio3dsServers.md)
 - [InovioAllOfCredentials](docs/InovioAllOfCredentials.md)
 - [InovioAllOfSettings](docs/InovioAllOfSettings.md)
 - [InstaDebit](docs/InstaDebit.md)
 - [InstaDebitAllOfCredentials](docs/InstaDebitAllOfCredentials.md)
 - [InstrumentReference](docs/InstrumentReference.md)
 - [Intelligent](docs/Intelligent.md)
 - [IntelligentAllOfUnit](docs/IntelligentAllOfUnit.md)
 - [Intuit](docs/Intuit.md)
 - [IntuitAllOfCredentials](docs/IntuitAllOfCredentials.md)
 - [InvalidError](docs/InvalidError.md)
 - [Invoice](docs/Invoice.md)
 - [InvoiceAllOfEmbedded](docs/InvoiceAllOfEmbedded.md)
 - [InvoiceAllOfLinks](docs/InvoiceAllOfLinks.md)
 - [InvoiceAllOfRetryInstruction](docs/InvoiceAllOfRetryInstruction.md)
 - [InvoiceAllOfRetryInstructionAttempts](docs/InvoiceAllOfRetryInstructionAttempts.md)
 - [InvoiceDiscount](docs/InvoiceDiscount.md)
 - [InvoiceIssue](docs/InvoiceIssue.md)
 - [InvoiceItem](docs/InvoiceItem.md)
 - [InvoiceItemEmbeddedInner](docs/InvoiceItemEmbeddedInner.md)
 - [InvoiceItemLinksInner](docs/InvoiceItemLinksInner.md)
 - [InvoiceLink](docs/InvoiceLink.md)
 - [InvoiceReissue](docs/InvoiceReissue.md)
 - [InvoiceRetryScheduleInstruction](docs/InvoiceRetryScheduleInstruction.md)
 - [InvoiceShipping](docs/InvoiceShipping.md)
 - [InvoiceTax](docs/InvoiceTax.md)
 - [InvoiceTaxItem](docs/InvoiceTaxItem.md)
 - [InvoiceTimeShift](docs/InvoiceTimeShift.md)
 - [InvoiceTimeline](docs/InvoiceTimeline.md)
 - [InvoiceTransaction](docs/InvoiceTransaction.md)
 - [InvoiceTransactionAllocation](docs/InvoiceTransactionAllocation.md)
 - [InvoiceTransactionAllocationLinksInner](docs/InvoiceTransactionAllocationLinksInner.md)
 - [InvoicesEmbed](docs/InvoicesEmbed.md)
 - [InvoicesLink](docs/InvoicesLink.md)
 - [IpayOptions](docs/IpayOptions.md)
 - [IpayOptionsAllOfCredentials](docs/IpayOptionsAllOfCredentials.md)
 - [IpayOptionsAllOfSettings](docs/IpayOptionsAllOfSettings.md)
 - [IssueTimeShiftInstruction](docs/IssueTimeShiftInstruction.md)
 - [JetPay](docs/JetPay.md)
 - [JetPayAllOfCredentials](docs/JetPayAllOfCredentials.md)
 - [Jeton](docs/Jeton.md)
 - [JetonAllOfCredentials](docs/JetonAllOfCredentials.md)
 - [JetonAllOfSettings](docs/JetonAllOfSettings.md)
 - [Khelocard](docs/Khelocard.md)
 - [KhelocardAllOfCredentials](docs/KhelocardAllOfCredentials.md)
 - [KhelocardCard](docs/KhelocardCard.md)
 - [KhelocardCardToken](docs/KhelocardCardToken.md)
 - [Konnektive](docs/Konnektive.md)
 - [KonnektiveAllOfCredentials](docs/KonnektiveAllOfCredentials.md)
 - [KonnektiveAllOfSettings](docs/KonnektiveAllOfSettings.md)
 - [KycDocument](docs/KycDocument.md)
 - [KycDocument2](docs/KycDocument2.md)
 - [KycDocumentLink](docs/KycDocumentLink.md)
 - [KycDocumentRejection](docs/KycDocumentRejection.md)
 - [KycDocumentSubtypes](docs/KycDocumentSubtypes.md)
 - [KycDocumentTypes](docs/KycDocumentTypes.md)
 - [KycDocumentsLink](docs/KycDocumentsLink.md)
 - [KycGathererLink](docs/KycGathererLink.md)
 - [KycRequest](docs/KycRequest.md)
 - [KycRequestAllOfLinks](docs/KycRequestAllOfLinks.md)
 - [LPG](docs/LPG.md)
 - [LPGAllOfCredentials](docs/LPGAllOfCredentials.md)
 - [LeadSource](docs/LeadSource.md)
 - [LeadSourceData](docs/LeadSourceData.md)
 - [LeadSourceEmbed](docs/LeadSourceEmbed.md)
 - [LeadSourceLink](docs/LeadSourceLink.md)
 - [Link](docs/Link.md)
 - [Loonie](docs/Loonie.md)
 - [LoonieAllOfCredentials](docs/LoonieAllOfCredentials.md)
 - [Manual](docs/Manual.md)
 - [Manual2](docs/Manual2.md)
 - [Manual2AllOfItems](docs/Manual2AllOfItems.md)
 - [MiFinity](docs/MiFinity.md)
 - [MiFinityAllOfCredentials](docs/MiFinityAllOfCredentials.md)
 - [MinimumOrderAmount](docs/MinimumOrderAmount.md)
 - [ModelFile](docs/ModelFile.md)
 - [ModelList](docs/ModelList.md)
 - [Moneris](docs/Moneris.md)
 - [MonerisAllOfCredentials](docs/MonerisAllOfCredentials.md)
 - [Money](docs/Money.md)
 - [MtaPay](docs/MtaPay.md)
 - [MtaPayAllOfCredentials](docs/MtaPayAllOfCredentials.md)
 - [MtaPayAllOfSettings](docs/MtaPayAllOfSettings.md)
 - [MuchBetter](docs/MuchBetter.md)
 - [MuchBetterAllOfCredentials](docs/MuchBetterAllOfCredentials.md)
 - [MuchBetterAllOfSettings](docs/MuchBetterAllOfSettings.md)
 - [MyFatoorah](docs/MyFatoorah.md)
 - [MyFatoorahAllOfCredentials](docs/MyFatoorahAllOfCredentials.md)
 - [NGenius](docs/NGenius.md)
 - [NGenius3dsServer](docs/NGenius3dsServer.md)
 - [NGenius3dsServers](docs/NGenius3dsServers.md)
 - [NGeniusAllOfCredentials](docs/NGeniusAllOfCredentials.md)
 - [NMI](docs/NMI.md)
 - [NMI3dsServers](docs/NMI3dsServers.md)
 - [NMIAllOfCredentials](docs/NMIAllOfCredentials.md)
 - [NMIAllOfSettings](docs/NMIAllOfSettings.md)
 - [Neosurf](docs/Neosurf.md)
 - [NeosurfAllOfCredentials](docs/NeosurfAllOfCredentials.md)
 - [Netbanking](docs/Netbanking.md)
 - [NetbankingAllOfCredentials](docs/NetbankingAllOfCredentials.md)
 - [Neteller](docs/Neteller.md)
 - [NetellerAllOfCredentials](docs/NetellerAllOfCredentials.md)
 - [NetellerAllOfSettings](docs/NetellerAllOfSettings.md)
 - [NinjaWallet](docs/NinjaWallet.md)
 - [NinjaWalletAllOfCredentials](docs/NinjaWalletAllOfCredentials.md)
 - [NuaPay](docs/NuaPay.md)
 - [NuaPayAllOfCredentials](docs/NuaPayAllOfCredentials.md)
 - [OchaPay](docs/OchaPay.md)
 - [OchaPayAllOfCredentials](docs/OchaPayAllOfCredentials.md)
 - [OnBoardingUrlLink](docs/OnBoardingUrlLink.md)
 - [OnRamp](docs/OnRamp.md)
 - [OnRampAllOfCredentials](docs/OnRampAllOfCredentials.md)
 - [OneColumn](docs/OneColumn.md)
 - [OneColumnAllOfData](docs/OneColumnAllOfData.md)
 - [OneTimeOrder](docs/OneTimeOrder.md)
 - [Onlineueberweisen](docs/Onlineueberweisen.md)
 - [OnlineueberweisenAllOfCredentials](docs/OnlineueberweisenAllOfCredentials.md)
 - [OnlineueberweisenAllOfSettings](docs/OnlineueberweisenAllOfSettings.md)
 - [OrderTimeline](docs/OrderTimeline.md)
 - [Organization](docs/Organization.md)
 - [OrganizationEmbed](docs/OrganizationEmbed.md)
 - [OrganizationLink](docs/OrganizationLink.md)
 - [OrganizationQuestionnaire](docs/OrganizationQuestionnaire.md)
 - [Other](docs/Other.md)
 - [Paay3dsServer](docs/Paay3dsServer.md)
 - [Pagsmile](docs/Pagsmile.md)
 - [PagsmileAllOfCredentials](docs/PagsmileAllOfCredentials.md)
 - [PaidByTime](docs/PaidByTime.md)
 - [Panamerican](docs/Panamerican.md)
 - [Panamerican3dsServer](docs/Panamerican3dsServer.md)
 - [Panamerican3dsServers](docs/Panamerican3dsServers.md)
 - [PanamericanAllOfCredentials](docs/PanamericanAllOfCredentials.md)
 - [PanamericanAllOfSettings](docs/PanamericanAllOfSettings.md)
 - [PandaGateway](docs/PandaGateway.md)
 - [PandaGatewayAllOfCredentials](docs/PandaGatewayAllOfCredentials.md)
 - [ParamountEft](docs/ParamountEft.md)
 - [ParamountEftAllOfCredentials](docs/ParamountEftAllOfCredentials.md)
 - [ParamountInterac](docs/ParamountInterac.md)
 - [ParamountInteracAllOfCredentials](docs/ParamountInteracAllOfCredentials.md)
 - [ParentTransactionEmbed](docs/ParentTransactionEmbed.md)
 - [ParentTransactionLink](docs/ParentTransactionLink.md)
 - [Partial](docs/Partial.md)
 - [Password](docs/Password.md)
 - [Passwordless](docs/Passwordless.md)
 - [PatchKycRequestRequest](docs/PatchKycRequestRequest.md)
 - [PatchPaymentInstrumentRequest](docs/PatchPaymentInstrumentRequest.md)
 - [PatchTransactionRequest](docs/PatchTransactionRequest.md)
 - [Pay4Fun](docs/Pay4Fun.md)
 - [Pay4FunAllOfCredentials](docs/Pay4FunAllOfCredentials.md)
 - [PayCash](docs/PayCash.md)
 - [PayCashAllOfCredentials](docs/PayCashAllOfCredentials.md)
 - [PayClub](docs/PayClub.md)
 - [PayClubAllOfCredentials](docs/PayClubAllOfCredentials.md)
 - [PayClubAllOfSettings](docs/PayClubAllOfSettings.md)
 - [PayPal](docs/PayPal.md)
 - [PayPalAccount](docs/PayPalAccount.md)
 - [PayPalAccountAllOfEmbedded](docs/PayPalAccountAllOfEmbedded.md)
 - [PayPalAccountAllOfLinks](docs/PayPalAccountAllOfLinks.md)
 - [PayPalAllOfSettings](docs/PayPalAllOfSettings.md)
 - [PayTabs](docs/PayTabs.md)
 - [PayTabsAllOfCredentials](docs/PayTabsAllOfCredentials.md)
 - [PayULatam](docs/PayULatam.md)
 - [PayULatamAllOfCredentials](docs/PayULatamAllOfCredentials.md)
 - [Payeezy](docs/Payeezy.md)
 - [PayeezyAllOfCredentials](docs/PayeezyAllOfCredentials.md)
 - [Payflow](docs/Payflow.md)
 - [PayflowAllOfCredentials](docs/PayflowAllOfCredentials.md)
 - [PaymenTechnologies](docs/PaymenTechnologies.md)
 - [PaymenTechnologiesAllOfCredentials](docs/PaymenTechnologiesAllOfCredentials.md)
 - [PaymenTechnologiesAllOfSettings](docs/PaymenTechnologiesAllOfSettings.md)
 - [PaymentAsia](docs/PaymentAsia.md)
 - [PaymentAsiaAllOfCredentials](docs/PaymentAsiaAllOfCredentials.md)
 - [PaymentCard](docs/PaymentCard.md)
 - [PaymentCardAllOfEmbedded](docs/PaymentCardAllOfEmbedded.md)
 - [PaymentCardAllOfLinks](docs/PaymentCardAllOfLinks.md)
 - [PaymentCardBrand](docs/PaymentCardBrand.md)
 - [PaymentCardCreatePlain](docs/PaymentCardCreatePlain.md)
 - [PaymentCardCreateToken](docs/PaymentCardCreateToken.md)
 - [PaymentCardDigitalWalletFeature](docs/PaymentCardDigitalWalletFeature.md)
 - [PaymentCardEmbed](docs/PaymentCardEmbed.md)
 - [PaymentCardLink](docs/PaymentCardLink.md)
 - [PaymentCardToken](docs/PaymentCardToken.md)
 - [PaymentCardUpdatePlain](docs/PaymentCardUpdatePlain.md)
 - [PaymentInstruction](docs/PaymentInstruction.md)
 - [PaymentInstrument](docs/PaymentInstrument.md)
 - [PaymentInstrument2](docs/PaymentInstrument2.md)
 - [PaymentInstrument3](docs/PaymentInstrument3.md)
 - [PaymentInstrumentCreateToken](docs/PaymentInstrumentCreateToken.md)
 - [PaymentInstrumentUpdateToken](docs/PaymentInstrumentUpdateToken.md)
 - [PaymentMethod](docs/PaymentMethod.md)
 - [PaymentMethods](docs/PaymentMethods.md)
 - [PaymentRetry](docs/PaymentRetry.md)
 - [PaymentRetryAttemptsInner](docs/PaymentRetryAttemptsInner.md)
 - [PaymentToken](docs/PaymentToken.md)
 - [PaymentsOS](docs/PaymentsOS.md)
 - [PaymentsOSAllOfCredentials](docs/PaymentsOSAllOfCredentials.md)
 - [Paymero](docs/Paymero.md)
 - [PaymeroAllOfCredentials](docs/PaymeroAllOfCredentials.md)
 - [PaymeroAllOfSettings](docs/PaymeroAllOfSettings.md)
 - [PayoutRequest](docs/PayoutRequest.md)
 - [Payr](docs/Payr.md)
 - [PayrAllOfCredentials](docs/PayrAllOfCredentials.md)
 - [Paysafe](docs/Paysafe.md)
 - [Paysafe3dsServer](docs/Paysafe3dsServer.md)
 - [Paysafe3dsServers](docs/Paysafe3dsServers.md)
 - [PaysafeAllOfCredentials](docs/PaysafeAllOfCredentials.md)
 - [Paysafecash](docs/Paysafecash.md)
 - [PaysafecashAllOfCredentials](docs/PaysafecashAllOfCredentials.md)
 - [Payvision](docs/Payvision.md)
 - [Payvision3dsServer](docs/Payvision3dsServer.md)
 - [Payvision3dsServers](docs/Payvision3dsServers.md)
 - [PayvisionAllOfCredentials](docs/PayvisionAllOfCredentials.md)
 - [PayvisionAllOfSettings](docs/PayvisionAllOfSettings.md)
 - [Percent](docs/Percent.md)
 - [PermalinkLink](docs/PermalinkLink.md)
 - [Piastrix](docs/Piastrix.md)
 - [Piastrix3dsServer](docs/Piastrix3dsServer.md)
 - [Piastrix3dsServers](docs/Piastrix3dsServers.md)
 - [PiastrixAllOfCredentials](docs/PiastrixAllOfCredentials.md)
 - [PiastrixAllOfSettings](docs/PiastrixAllOfSettings.md)
 - [PlaidAccountToken](docs/PlaidAccountToken.md)
 - [Plan](docs/Plan.md)
 - [PlanBillingTiming](docs/PlanBillingTiming.md)
 - [PlanEmbed](docs/PlanEmbed.md)
 - [PlanPeriod](docs/PlanPeriod.md)
 - [PlanPriceFormula](docs/PlanPriceFormula.md)
 - [Plugnpay](docs/Plugnpay.md)
 - [PlugnpayAllOfCredentials](docs/PlugnpayAllOfCredentials.md)
 - [PostBankAccountRequest](docs/PostBankAccountRequest.md)
 - [PostFileRequest](docs/PostFileRequest.md)
 - [PostFinance](docs/PostFinance.md)
 - [PostFinanceAllOfCredentials](docs/PostFinanceAllOfCredentials.md)
 - [PostKycDocumentMatchesRequest](docs/PostKycDocumentMatchesRequest.md)
 - [PostPaymentCardRequest](docs/PostPaymentCardRequest.md)
 - [PostPaymentInstrumentRequest](docs/PostPaymentInstrumentRequest.md)
 - [PostTagCustomerCollectionRequest](docs/PostTagCustomerCollectionRequest.md)
 - [PriceBasedShippingRate](docs/PriceBasedShippingRate.md)
 - [Problem](docs/Problem.md)
 - [Product](docs/Product.md)
 - [ProductEmbed](docs/ProductEmbed.md)
 - [ProductLink](docs/ProductLink.md)
 - [ProofOfAddress](docs/ProofOfAddress.md)
 - [ProofOfAddressAllOfDocumentMatches](docs/ProofOfAddressAllOfDocumentMatches.md)
 - [ProofOfAddressAllOfLinks](docs/ProofOfAddressAllOfLinks.md)
 - [ProofOfFunds](docs/ProofOfFunds.md)
 - [ProofOfIdentity](docs/ProofOfIdentity.md)
 - [ProofOfIdentityAllOfDocumentMatches](docs/ProofOfIdentityAllOfDocumentMatches.md)
 - [ProofOfIdentityAllOfLinks](docs/ProofOfIdentityAllOfLinks.md)
 - [ProofOfPurchase](docs/ProofOfPurchase.md)
 - [Prosa](docs/Prosa.md)
 - [ProsaAllOfCredentials](docs/ProsaAllOfCredentials.md)
 - [PurchaseBumpOffer](docs/PurchaseBumpOffer.md)
 - [PurchaseBumpStatus](docs/PurchaseBumpStatus.md)
 - [QueryUrlLink](docs/QueryUrlLink.md)
 - [RPN](docs/RPN.md)
 - [RPNAllOfCredentials](docs/RPNAllOfCredentials.md)
 - [Rapyd](docs/Rapyd.md)
 - [RapydAllOfCredentials](docs/RapydAllOfCredentials.md)
 - [ReadyToPay](docs/ReadyToPay.md)
 - [ReadyToPayAchMethod](docs/ReadyToPayAchMethod.md)
 - [ReadyToPayAchMethodFeature](docs/ReadyToPayAchMethodFeature.md)
 - [ReadyToPayAmount](docs/ReadyToPayAmount.md)
 - [ReadyToPayGenericMethod](docs/ReadyToPayGenericMethod.md)
 - [ReadyToPayItems](docs/ReadyToPayItems.md)
 - [ReadyToPayItemsItemsInner](docs/ReadyToPayItemsItemsInner.md)
 - [ReadyToPayMethodsInner](docs/ReadyToPayMethodsInner.md)
 - [ReadyToPayPaymentCardMethod](docs/ReadyToPayPaymentCardMethod.md)
 - [ReadyToPayPaymentCardMethodFeature](docs/ReadyToPayPaymentCardMethodFeature.md)
 - [Realex](docs/Realex.md)
 - [RealexAllOfCredentials](docs/RealexAllOfCredentials.md)
 - [Realtime](docs/Realtime.md)
 - [RealtimeAllOfCredentials](docs/RealtimeAllOfCredentials.md)
 - [Rebilly](docs/Rebilly.md)
 - [RebillyTaxjar](docs/RebillyTaxjar.md)
 - [RebillyTaxjarAllOfItems](docs/RebillyTaxjarAllOfItems.md)
 - [RecalculateInvoiceLink](docs/RecalculateInvoiceLink.md)
 - [RecentInvoiceEmbed](docs/RecentInvoiceEmbed.md)
 - [RecentInvoiceLink](docs/RecentInvoiceLink.md)
 - [RedemptionCancel](docs/RedemptionCancel.md)
 - [RedemptionRestriction](docs/RedemptionRestriction.md)
 - [RedemptionsPerCustomer](docs/RedemptionsPerCustomer.md)
 - [Redsys](docs/Redsys.md)
 - [RedsysAllOfCredentials](docs/RedsysAllOfCredentials.md)
 - [RefundUrlLink](docs/RefundUrlLink.md)
 - [ResendEmail](docs/ResendEmail.md)
 - [ResetPasswordToken](docs/ResetPasswordToken.md)
 - [RestrictToInvoices](docs/RestrictToInvoices.md)
 - [RestrictToPlans](docs/RestrictToPlans.md)
 - [RestrictToProducts](docs/RestrictToProducts.md)
 - [RestrictToSubscriptions](docs/RestrictToSubscriptions.md)
 - [RetriedTransactionEmbed](docs/RetriedTransactionEmbed.md)
 - [RetriedTransactionLink](docs/RetriedTransactionLink.md)
 - [RiskMetadata](docs/RiskMetadata.md)
 - [Rotessa](docs/Rotessa.md)
 - [RotessaAllOfCredentials](docs/RotessaAllOfCredentials.md)
 - [RotessaAllOfSettings](docs/RotessaAllOfSettings.md)
 - [RulesetRestore](docs/RulesetRestore.md)
 - [SMSVoucher](docs/SMSVoucher.md)
 - [SMSVoucherAllOfCredentials](docs/SMSVoucherAllOfCredentials.md)
 - [Sagepay](docs/Sagepay.md)
 - [SagepayAllOfCredentials](docs/SagepayAllOfCredentials.md)
 - [SaltarPay](docs/SaltarPay.md)
 - [SaltarPayAllOfCredentials](docs/SaltarPayAllOfCredentials.md)
 - [SeamlessChex](docs/SeamlessChex.md)
 - [SeamlessChexAllOfCredentials](docs/SeamlessChexAllOfCredentials.md)
 - [Search](docs/Search.md)
 - [SecureTrading](docs/SecureTrading.md)
 - [SecureTrading3dsServer](docs/SecureTrading3dsServer.md)
 - [SecureTrading3dsServers](docs/SecureTrading3dsServers.md)
 - [SecureTradingAllOfCredentials](docs/SecureTradingAllOfCredentials.md)
 - [SecurionPay](docs/SecurionPay.md)
 - [SecurionPay3dsServers](docs/SecurionPay3dsServers.md)
 - [SecurionPayAllOfCredentials](docs/SecurionPayAllOfCredentials.md)
 - [SelfLink](docs/SelfLink.md)
 - [ServicePeriodAnchorInstruction](docs/ServicePeriodAnchorInstruction.md)
 - [ShippingZone](docs/ShippingZone.md)
 - [SignedLinkLink](docs/SignedLinkLink.md)
 - [Skrill](docs/Skrill.md)
 - [SkrillAllOfCredentials](docs/SkrillAllOfCredentials.md)
 - [SmartInvoice](docs/SmartInvoice.md)
 - [SmartInvoice3dsServer](docs/SmartInvoice3dsServer.md)
 - [SmartInvoice3dsServers](docs/SmartInvoice3dsServers.md)
 - [SmartInvoiceAllOfCredentials](docs/SmartInvoiceAllOfCredentials.md)
 - [Sofort](docs/Sofort.md)
 - [SofortAllOfCredentials](docs/SofortAllOfCredentials.md)
 - [SparkPay](docs/SparkPay.md)
 - [SparkPayAllOfCredentials](docs/SparkPayAllOfCredentials.md)
 - [Stairstep](docs/Stairstep.md)
 - [StairstepAllOfBrackets](docs/StairstepAllOfBrackets.md)
 - [StaticGateway](docs/StaticGateway.md)
 - [StaticIpnLink](docs/StaticIpnLink.md)
 - [Stripe](docs/Stripe.md)
 - [Stripe3dsServer](docs/Stripe3dsServer.md)
 - [Stripe3dsServers](docs/Stripe3dsServers.md)
 - [StripeAllOfSettings](docs/StripeAllOfSettings.md)
 - [Subscription](docs/Subscription.md)
 - [SubscriptionCancellation](docs/SubscriptionCancellation.md)
 - [SubscriptionCancellationState](docs/SubscriptionCancellationState.md)
 - [SubscriptionChange](docs/SubscriptionChange.md)
 - [SubscriptionChangeItemsInner](docs/SubscriptionChangeItemsInner.md)
 - [SubscriptionInvoice](docs/SubscriptionInvoice.md)
 - [SubscriptionLink](docs/SubscriptionLink.md)
 - [SubscriptionMetadata](docs/SubscriptionMetadata.md)
 - [SubscriptionMetadataEmbeddedInner](docs/SubscriptionMetadataEmbeddedInner.md)
 - [SubscriptionMetadataLinksInner](docs/SubscriptionMetadataLinksInner.md)
 - [SubscriptionOrder](docs/SubscriptionOrder.md)
 - [SubscriptionReactivation](docs/SubscriptionReactivation.md)
 - [TWINT](docs/TWINT.md)
 - [TWINTAllOfCredentials](docs/TWINTAllOfCredentials.md)
 - [TWINTAllOfSettings](docs/TWINTAllOfSettings.md)
 - [Tag](docs/Tag.md)
 - [TestProcessor](docs/TestProcessor.md)
 - [TestProcessor3dsServer](docs/TestProcessor3dsServer.md)
 - [TestProcessor3dsServers](docs/TestProcessor3dsServers.md)
 - [ThreeColumns](docs/ThreeColumns.md)
 - [ThreeColumnsAllOfData](docs/ThreeColumnsAllOfData.md)
 - [ThreeDSecure](docs/ThreeDSecure.md)
 - [ThreeDSecureIO3dsServer](docs/ThreeDSecureIO3dsServer.md)
 - [ThreeDSecureResult](docs/ThreeDSecureResult.md)
 - [ThreeDSecureServerName](docs/ThreeDSecureServerName.md)
 - [Tiered](docs/Tiered.md)
 - [TimePluralUnit](docs/TimePluralUnit.md)
 - [TimeUnit](docs/TimeUnit.md)
 - [TimelineAction](docs/TimelineAction.md)
 - [TimelineExtraData](docs/TimelineExtraData.md)
 - [TimelineExtraDataAuthor](docs/TimelineExtraDataAuthor.md)
 - [TimelineExtraDataLinksInner](docs/TimelineExtraDataLinksInner.md)
 - [TimelineTable](docs/TimelineTable.md)
 - [ToditoCash](docs/ToditoCash.md)
 - [ToditoCashAllOfCredentials](docs/ToditoCashAllOfCredentials.md)
 - [TotalRedemptions](docs/TotalRedemptions.md)
 - [Transaction](docs/Transaction.md)
 - [TransactionAllOfBumpOffer](docs/TransactionAllOfBumpOffer.md)
 - [TransactionAllOfDcc](docs/TransactionAllOfDcc.md)
 - [TransactionAllOfEmbedded](docs/TransactionAllOfEmbedded.md)
 - [TransactionAllOfGateway](docs/TransactionAllOfGateway.md)
 - [TransactionAllOfGatewayAvsResponse](docs/TransactionAllOfGatewayAvsResponse.md)
 - [TransactionAllOfGatewayCvvResponse](docs/TransactionAllOfGatewayCvvResponse.md)
 - [TransactionAllOfGatewayResponse](docs/TransactionAllOfGatewayResponse.md)
 - [TransactionAllOfLinks](docs/TransactionAllOfLinks.md)
 - [TransactionAllocationsLink](docs/TransactionAllocationsLink.md)
 - [TransactionEmbed](docs/TransactionEmbed.md)
 - [TransactionLink](docs/TransactionLink.md)
 - [TransactionQuery](docs/TransactionQuery.md)
 - [TransactionRefund](docs/TransactionRefund.md)
 - [TransactionRequest](docs/TransactionRequest.md)
 - [TransactionTimeline](docs/TransactionTimeline.md)
 - [TransactionUpdate](docs/TransactionUpdate.md)
 - [TransactionUpdateUrlLink](docs/TransactionUpdateUrlLink.md)
 - [TrustPay](docs/TrustPay.md)
 - [TrustPayAllOfCredentials](docs/TrustPayAllOfCredentials.md)
 - [Trustly](docs/Trustly.md)
 - [TrustlyAllOfCredentials](docs/TrustlyAllOfCredentials.md)
 - [TrustsPay](docs/TrustsPay.md)
 - [TrustsPayAllOfCredentials](docs/TrustsPayAllOfCredentials.md)
 - [TwoColumns](docs/TwoColumns.md)
 - [UPayCard](docs/UPayCard.md)
 - [UPayCardAllOfCredentials](docs/UPayCardAllOfCredentials.md)
 - [UPayCardAllOfSettings](docs/UPayCardAllOfSettings.md)
 - [USAePay](docs/USAePay.md)
 - [USAePayAllOfCredentials](docs/USAePayAllOfCredentials.md)
 - [UpcomingInvoiceItem](docs/UpcomingInvoiceItem.md)
 - [VCreditos](docs/VCreditos.md)
 - [VCreditosAllOfCredentials](docs/VCreditosAllOfCredentials.md)
 - [ValidationErrorExtensions](docs/ValidationErrorExtensions.md)
 - [ValidationErrorExtensionsInvalidFieldsInner](docs/ValidationErrorExtensionsInvalidFieldsInner.md)
 - [VantivLitle](docs/VantivLitle.md)
 - [VantivLitle3dsServers](docs/VantivLitle3dsServers.md)
 - [VantivLitleAllOfCredentials](docs/VantivLitleAllOfCredentials.md)
 - [VaultedInstrument](docs/VaultedInstrument.md)
 - [VegaaH](docs/VegaaH.md)
 - [VegaaHAllOfCredentials](docs/VegaaHAllOfCredentials.md)
 - [Volume](docs/Volume.md)
 - [Wallet88](docs/Wallet88.md)
 - [Wallet88AllOfCredentials](docs/Wallet88AllOfCredentials.md)
 - [Walpay](docs/Walpay.md)
 - [Walpay3dsServers](docs/Walpay3dsServers.md)
 - [WalpayAllOfCredentials](docs/WalpayAllOfCredentials.md)
 - [WebsiteEmbed](docs/WebsiteEmbed.md)
 - [WebsiteLink](docs/WebsiteLink.md)
 - [Wirecard](docs/Wirecard.md)
 - [Wirecard3dsServer](docs/Wirecard3dsServer.md)
 - [Wirecard3dsServers](docs/Wirecard3dsServers.md)
 - [WirecardAllOfCredentials](docs/WirecardAllOfCredentials.md)
 - [WorldlineAtosFrankfurt](docs/WorldlineAtosFrankfurt.md)
 - [WorldlineAtosFrankfurt3dsServers](docs/WorldlineAtosFrankfurt3dsServers.md)
 - [WorldlineAtosFrankfurtAllOfCredentials](docs/WorldlineAtosFrankfurtAllOfCredentials.md)
 - [WorldlineAtosFrankfurtAllOfSettings](docs/WorldlineAtosFrankfurtAllOfSettings.md)
 - [Worldpay](docs/Worldpay.md)
 - [Worldpay3dsServers](docs/Worldpay3dsServers.md)
 - [WorldpayAllOfCredentials](docs/WorldpayAllOfCredentials.md)
 - [WorldpayAllOfSettings](docs/WorldpayAllOfSettings.md)
 - [XPay](docs/XPay.md)
 - [XPayAllOfCredentials](docs/XPayAllOfCredentials.md)
 - [Zimpler](docs/Zimpler.md)
 - [ZimplerAllOfCredentials](docs/ZimplerAllOfCredentials.md)
 - [Zotapay](docs/Zotapay.md)
 - [ZotapayAllOfCredentials](docs/ZotapayAllOfCredentials.md)


<a id="documentation-for-authorization"></a>
## Documentation for Authorization


Authentication schemes defined for the API:
<a id="JWT"></a>
### JWT

- **Type**: HTTP Bearer Token authentication (JWT)

<a id="PublishableApiKey"></a>
### PublishableApiKey

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header

<a id="SecretApiKey"></a>
### SecretApiKey

- **Type**: API key
- **API key parameter name**: REB-APIKEY
- **Location**: HTTP header


## Recommendation

It's recommended to create an instance of `ApiClient` per thread in a multithreaded environment to avoid any potential issues.

## Author

integrations@rebilly.com

