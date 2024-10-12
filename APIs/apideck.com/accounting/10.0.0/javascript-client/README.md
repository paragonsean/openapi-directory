# accounting_api

AccountingApi - JavaScript client for accounting_api
Welcome to the Accounting API.

You can use this API to access all Accounting API endpoints.

## Base URL

The base URL for all API requests is `https://unify.apideck.com`

## Headers

Custom headers that are expected as part of the request. Note that [RFC7230](https://tools.ietf.org/html/rfc7230) states header names are case insensitive.

| Name                  | Type    | Required | Description                                                                                                                                                    |
| --------------------- | ------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| x-apideck-consumer-id | String  | Yes      | The id of the customer stored inside Apideck Vault. This can be a user id, account id, device id or whatever entity that can have integration within your app. |
| x-apideck-service-id  | String  | No       | Describe the service you want to call (e.g., pipedrive). Only needed when a customer has activated multiple integrations for the same Unified API.             |
| x-apideck-raw         | Boolean | No       | Include raw response. Mostly used for debugging purposes.                                                                                                      |
| x-apideck-app-id      | String  | Yes      | The application id of your Unify application. Available at https://app.apideck.com/unify/api-keys.                                                             |
| Authorization         | String  | Yes      | Bearer API KEY                                                                                                                                                 |

## Authorization

You can interact with the API through the authorization methods below.

<!-- ReDoc-Inject: <security-definitions> -->

## Pagination

All API resources have support for bulk retrieval via list APIs.  Apideck uses cursor-based pagination via the optional `cursor` and `limit` parameters.

To fetch the first page of results, call the list API without a `cursor` parameter. Afterwards you can fetch subsequent pages by providing a cursor parameter. You will find the next cursor in the response body in `meta.cursors.next`. If `meta.cursors.next` is `null` you're at the end of the list.

In the REST API you can also use the `links` from the response for added convenience. Simply call the URL in `links.next` to get the next page of results.

### Query Parameters

| Name   | Type   | Required | Description                                                                                                        |
| ------ | ------ | -------- | ------------------------------------------------------------------------------------------------------------------ |
| cursor | String | No       | Cursor to start from. You can find cursors for next & previous pages in the meta.cursors property of the response. |
| limit  | Number | No       | Number of results to return. Minimum 1, Maximum 200, Default 20                                                    |

### Response Body

| Name                  | Type   | Description                                                        |
| --------------------- | ------ | ------------------------------------------------------------------ |
| meta.cursors.previous | String | Cursor to navigate to the previous page of results through the API |
| meta.cursors.current  | String | Cursor to navigate to the current page of results through the API  |
| meta.cursors.next     | String | Cursor to navigate to the next page of results through the API     |
| meta.items_on_page    | Number | Number of items returned in the data property of the response      |
| links.previous        | String | Link to navigate to the previous page of results through the API   |
| links.current         | String | Link to navigate to the current page of results through the API    |
| links.next            | String | Link to navigate to the next page of results through the API       |

⚠️ `meta.cursors.previous`/`links.previous` is not available for all connectors.

## SDKs and API Clients

We currently offer a [Node.js](https://developers.apideck.com/sdks/node), [PHP](https://developers.apideck.com/sdks/php) and [.NET](https://developers.apideck.com/sdks/dot-net) SDK.
Need another SDK? [Request the SDK of your choice](https://integrations.apideck.com/request).

## Debugging

Because of the nature of the abstraction we do in Apideck Unify we still provide the option to the receive raw requests and responses being handled underlying. By including the raw flag `?raw=true` in your requests you can still receive the full request. Please note that this increases the response size and can introduce extra latency.

## Errors

The API returns standard HTTP response codes to indicate success or failure of the API requests. For errors, we also return a customized error message inside the JSON response. You can see the returned HTTP status codes below.

| Code | Title                | Description                                                                                                                                                                                              |
| ---- | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 200  | OK                   | The request message has been successfully processed, and it has produced a response. The response message varies, depending on the request method and the requested data.                                |
| 201  | Created              | The request has been fulfilled and has resulted in one or more new resources being created.                                                                                                              |
| 204  | No Content           | The server has successfully fulfilled the request and that there is no additional content to send in the response payload body.                                                                          |
| 400  | Bad Request          | The receiving server cannot understand the request because of malformed syntax. Do not repeat the request without first modifying it; check the request for errors, fix them and then retry the request. |
| 401  | Unauthorized         | The request has not been applied because it lacks valid authentication credentials for the target resource.                                                                                              |
| 402  | Payment Required     | Subscription data is incomplete or out of date. You'll need to provide payment details to continue.                                                                                                      |
| 403  | Forbidden            | You do not have the appropriate user rights to access the request. Do not repeat the request.                                                                                                            |
| 404  | Not Found            | The origin server did not find a current representation for the target resource or is not willing to disclose that one exists.                                                                           |
| 409  | Conflict             | The request could not be completed due to a conflict with the current state of the target resource.                                                                                                      |
| 422  | Unprocessable Entity | The server understands the content type of the request entity, and the syntax of the request entity is correct but was unable to process the contained instructions.                                     |
| 429  | Too Many Requests    | You sent too many requests in a given amount of time (\"rate limit\"). Try again later                                                                                                                     |
| 5xx  | Server Errors        | Something went wrong with the Unify API. These errors are logged on our side. You can contact our team to resolve the issue.                                                                             |

### Handling errors

The Unify API and SDKs can produce errors for many reasons, such as a failed requests due to misconfigured integrations, invalid parameters, authentication errors, and network unavailability.

### Error Types

#### RequestValidationError

Request is not valid for the current endpoint. The response body will include details on the validation error. Check the spelling and types of your attributes, and ensure you are not passing data that is outside of the specification.

#### UnsupportedFiltersError

Filters in the request are valid, but not supported by the connector. Remove the unsupported filter(s) to get a successful response.

#### UnsupportedSortFieldError

Sort field (`sort[by]`) in the request is valid, but not supported by the connector. Replace or remove the sort field to get a successful response.

#### InvalidCursorError

Pagination cursor in the request is not valid for the current connector. Make sure to use a cursor returned from the API, for the same connector.

#### ConnectorExecutionError

A Unified API request made via one of our downstream connectors returned an unexpected error. The `status_code` returned is proxied through to error response along with their original response via the error detail.

#### UnauthorizedError

We were unable to authorize the request as made. This can happen for a number of reasons, from missing header params to passing an incorrect authorization token. Verify your Api Key is being set correctly in the authorization header. ie: `Authorization: 'Bearer sk_live_***'`

#### ConnectorCredentialsError

A request using a given connector has not been authorized. Ensure the connector you are trying to use has been configured correctly and been authorized for use.

#### ConnectorDisabledError

A request has been made to a connector that has since been disabled. This may be temporary - You can contact our team to resolve the issue.

#### ConnectorRateLimitError

You sent too many request to a connector. These rate limits vary from connector to connector. You will need to try again later.

#### RequestLimitError

You have reached the number of requests included in your Free Tier Subscription. You will no be able to make further requests until this limit resets at the end of the month, or talk to us about upgrading your subscription to continue immediately.

#### EntityNotFoundError

You've made a request for a resource or route that does not exist. Verify your path parameters or any identifiers used to fetch this resource.

#### OAuthCredentialsNotFoundError

When adding a connector integration that implements OAuth, both a `client_id` and `client_secret` must be provided before any authorizations can be performed. Verify the integration has been configured properly before continuing.

#### IntegrationNotFoundError

The requested connector integration could not be found associated to your `application_id`. Verify your `application_id` is correct, and that this connector has been added and configured for your application.

#### ConnectionNotFoundError

A valid connection could not be found associated to your `application_id`. Something _may_ have interrupted the authorization flow. You may need to start the connector authorization process again.

#### ConnectionSettingsError

The connector has required settings that were not supplied. Verify `connection.settings` contains all required settings for the connector to be callable.

#### ConnectorNotFoundError

A request was made for an unknown connector. Verify your `service_id` is spelled correctly, and that this connector is enabled for your provided `unified_api`.

#### OAuthRedirectUriError

A request was made either in a connector authorization flow, or attempting to revoke connector access without a valid `redirect_uri`. This is the url the user should be returned to on completion of process.

#### OAuthInvalidStateError

The state param is required and is used to ensure the outgoing authorization state has not been altered before the user is redirected back. It also contains required params needed to identify the connector being used. If this has been altered, the authorization will not succeed.

#### OAuthCodeExchangeError

When attempting to exchange the authorization code for an `access_token` during an OAuth flow, an error occurred. This may be temporary. You can reattempt authorization or contact our team to resolve the issue.

#### OAuthConnectorError

It seems something went wrong on the connector side. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.

#### MappingError

There was an error attempting to retrieve the mapping for a given attribute. We've been notified and are working to fix this issue.

#### ConnectorMappingNotFoundError

It seems the implementation for this connector is incomplete. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.

#### ConnectorResponseMappingNotFoundError

We were unable to retrieve the response mapping for this connector. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.

#### ConnectorOperationMappingNotFoundError

Connector mapping has not been implemented for the requested operation. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.

#### ConnectorWorkflowMappingError

The composite api calls required for this operation have not been mapped entirely. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.

#### ConnectorOperationUnsupportedError

You're attempting a call that is not supported by the connector. It's likely this operation is supported by another connector, but we're unable to implement for this one.

#### PaginationNotSupportedError

Pagination is not yet supported for this connector, try removing limit and/or cursor from the query. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.

## API Design

### API Styles and data formats

#### REST API

The API is organized around [REST](https://restfulapi.net/), providing simple and predictable URIs to access and modify objects. Requests support standard HTTP methods like GET, PUT, POST, and DELETE and standard status codes. JSON is returned by all API responses, including errors. In all API requests, you must set the content-type HTTP header to application/json. All API requests must be made over HTTPS. Calls made over HTTP will fail.

##### Available HTTP methods

The Apideck API uses HTTP verbs to understand if you want to read (GET), delete (DELETE) or create (POST) an object. When your web application cannot do a POST or DELETE, we provide the ability to set the method through the query parameter \\_method.

```
POST /messages
GET /messages
GET /messages/{messageId}
PATCH /messages/{messageId}
DELETE /messages/{messageId}
```

Response bodies are always UTF-8 encoded JSON objects, unless explicitly documented otherwise. For some endpoints and use cases we divert from REST to provide a better developer experience.

### Schema

All API requests and response bodies adhere to a common JSON format representing individual items, collections of items, links to related items and additional meta data.

### Meta

Meta data can be represented as a top level member named “meta”. Any information may be provided in the meta data. It’s most common use is to return the total number of records when requesting a collection of resources.

### Idempotence (upcoming)

To prevent the creation of duplicate resources, every POST method (such as one that creates a consumer record) must specify a unique value for the X-Unique-Transaction-ID header name. Uniquely identifying each unique POST request ensures that the API processes a given request once and only once.

Uniquely identifying new resource-creation POSTs is especially important when the outcome of a response is ambiguous because of a transient service interruption, such as a server-side timeout or network disruption. If a service interruption occurs, then the client application can safely retry the uniquely identified request without creating duplicate operations. (API endpoints that guarantee that every uniquely identified request is processed only once no matter how many times that uniquely identifiable request is made are described as idempotent.)

### Request IDs

Each API request has an associated request identifier. You can find this value in the response headers, under Request-Id. You can also find request identifiers in the URLs of individual request logs in your Dashboard. If you need to contact us about a specific request, providing the request identifier will ensure the fastest possible resolution.

### Fixed field types

#### Dates

The dates returned by the API are all represented in UTC (ISO8601 format).

This example `2019-11-14T00:55:31.820Z` is defined by the ISO 8601 standard. The T in the middle separates the year-month-day portion from the hour-minute-second portion. The Z on the end means UTC, that is, an offset-from-UTC of zero hours-minutes-seconds. The Z is pronounced \"Zulu\" per military/aviation tradition.

The ISO 8601 standard is more modern. The formats are wisely designed to be easy to parse by machine as well as easy to read by humans across cultures.

#### Prices and Currencies

All prices returned by the API are represented as integer amounts in a currency’s smallest unit. For example, $5 USD would be returned as 500 (i.e, 500 cents).

For zero-decimal currencies, amounts will still be provided as an integer but without the need to divide by 100. For example, an amount of ¥5 (JPY) would be returned as 5.

All currency codes conform to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217).

## Support

If you have problems or need help with your case, you can always reach out to our Support.


This SDK is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 10.0.0
- Package version: 10.0.0
- Generator version: 7.9.0
- Build package: org.openapitools.codegen.languages.JavascriptClientCodegen
For more information, please visit [https://developers.apideck.com](https://developers.apideck.com)

## Installation

### For [Node.js](https://nodejs.org/)

#### npm

To publish the library as a [npm](https://www.npmjs.com/), please follow the procedure in ["Publishing npm packages"](https://docs.npmjs.com/getting-started/publishing-npm-packages).

Then install it via:

```shell
npm install accounting_api --save
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

To use the link you just defined in your project, switch to the directory you want to use your accounting_api from, and run:

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
var AccountingApi = require('accounting_api');

var defaultClient = AccountingApi.ApiClient.instance;
// Configure API key authorization: apiKey
var apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = "YOUR API KEY"
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix['Authorization'] = "Token"

var api = new AccountingApi.BalanceSheetApi()
var xApideckConsumerId = "xApideckConsumerId_example"; // {String} ID of the consumer which you want to get or push data from
var xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // {String} The ID of your Unify application
var opts = {
  'xApideckServiceId': "xApideckServiceId_example", // {String} Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
  'passThrough': {key: {"search":"San Francisco"}}, // {PassThroughQuery} Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]=leads becomes ?search=leads
  'filter': new AccountingApi.BalanceSheetFilter(), // {BalanceSheetFilter} Apply filters
  'raw': false // {Boolean} Include raw response. Mostly used for debugging purposes
};
var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
api.balanceSheetOne(xApideckConsumerId, xApideckAppId, opts, callback);

```

## Documentation for API Endpoints

All URIs are relative to *https://unify.apideck.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountingApi.BalanceSheetApi* | [**balanceSheetOne**](docs/BalanceSheetApi.md#balanceSheetOne) | **GET** /accounting/balance-sheet | Get BalanceSheet
*AccountingApi.BillsApi* | [**billsAdd**](docs/BillsApi.md#billsAdd) | **POST** /accounting/bills | Create Bill
*AccountingApi.BillsApi* | [**billsAll**](docs/BillsApi.md#billsAll) | **GET** /accounting/bills | List Bills
*AccountingApi.BillsApi* | [**billsDelete**](docs/BillsApi.md#billsDelete) | **DELETE** /accounting/bills/{id} | Delete Bill
*AccountingApi.BillsApi* | [**billsOne**](docs/BillsApi.md#billsOne) | **GET** /accounting/bills/{id} | Get Bill
*AccountingApi.BillsApi* | [**billsUpdate**](docs/BillsApi.md#billsUpdate) | **PATCH** /accounting/bills/{id} | Update Bill
*AccountingApi.CompanyInfoApi* | [**companyInfoOne**](docs/CompanyInfoApi.md#companyInfoOne) | **GET** /accounting/company-info | Get company info
*AccountingApi.CreditNotesApi* | [**creditNotesAdd**](docs/CreditNotesApi.md#creditNotesAdd) | **POST** /accounting/credit-notes | Create Credit Note
*AccountingApi.CreditNotesApi* | [**creditNotesAll**](docs/CreditNotesApi.md#creditNotesAll) | **GET** /accounting/credit-notes | List Credit Notes
*AccountingApi.CreditNotesApi* | [**creditNotesDelete**](docs/CreditNotesApi.md#creditNotesDelete) | **DELETE** /accounting/credit-notes/{id} | Delete Credit Note
*AccountingApi.CreditNotesApi* | [**creditNotesOne**](docs/CreditNotesApi.md#creditNotesOne) | **GET** /accounting/credit-notes/{id} | Get Credit Note
*AccountingApi.CreditNotesApi* | [**creditNotesUpdate**](docs/CreditNotesApi.md#creditNotesUpdate) | **PATCH** /accounting/credit-notes/{id} | Update Credit Note
*AccountingApi.CustomersApi* | [**customersAdd**](docs/CustomersApi.md#customersAdd) | **POST** /accounting/customers | Create Customer
*AccountingApi.CustomersApi* | [**customersAll**](docs/CustomersApi.md#customersAll) | **GET** /accounting/customers | List Customers
*AccountingApi.CustomersApi* | [**customersDelete**](docs/CustomersApi.md#customersDelete) | **DELETE** /accounting/customers/{id} | Delete Customer
*AccountingApi.CustomersApi* | [**customersOne**](docs/CustomersApi.md#customersOne) | **GET** /accounting/customers/{id} | Get Customer
*AccountingApi.CustomersApi* | [**customersUpdate**](docs/CustomersApi.md#customersUpdate) | **PATCH** /accounting/customers/{id} | Update Customer
*AccountingApi.InvoiceItemsApi* | [**invoiceItemsAdd**](docs/InvoiceItemsApi.md#invoiceItemsAdd) | **POST** /accounting/invoice-items | Create Invoice Item
*AccountingApi.InvoiceItemsApi* | [**invoiceItemsAll**](docs/InvoiceItemsApi.md#invoiceItemsAll) | **GET** /accounting/invoice-items | List Invoice Items
*AccountingApi.InvoiceItemsApi* | [**invoiceItemsDelete**](docs/InvoiceItemsApi.md#invoiceItemsDelete) | **DELETE** /accounting/invoice-items/{id} | Delete Invoice Item
*AccountingApi.InvoiceItemsApi* | [**invoiceItemsOne**](docs/InvoiceItemsApi.md#invoiceItemsOne) | **GET** /accounting/invoice-items/{id} | Get Invoice Item
*AccountingApi.InvoiceItemsApi* | [**invoiceItemsUpdate**](docs/InvoiceItemsApi.md#invoiceItemsUpdate) | **PATCH** /accounting/invoice-items/{id} | Update Invoice Item
*AccountingApi.InvoicesApi* | [**invoicesAdd**](docs/InvoicesApi.md#invoicesAdd) | **POST** /accounting/invoices | Create Invoice
*AccountingApi.InvoicesApi* | [**invoicesAll**](docs/InvoicesApi.md#invoicesAll) | **GET** /accounting/invoices | List Invoices
*AccountingApi.InvoicesApi* | [**invoicesDelete**](docs/InvoicesApi.md#invoicesDelete) | **DELETE** /accounting/invoices/{id} | Delete Invoice
*AccountingApi.InvoicesApi* | [**invoicesOne**](docs/InvoicesApi.md#invoicesOne) | **GET** /accounting/invoices/{id} | Get Invoice
*AccountingApi.InvoicesApi* | [**invoicesUpdate**](docs/InvoicesApi.md#invoicesUpdate) | **PATCH** /accounting/invoices/{id} | Update Invoice
*AccountingApi.JournalEntriesApi* | [**journalEntriesAdd**](docs/JournalEntriesApi.md#journalEntriesAdd) | **POST** /accounting/journal-entries | Create Journal Entry
*AccountingApi.JournalEntriesApi* | [**journalEntriesAll**](docs/JournalEntriesApi.md#journalEntriesAll) | **GET** /accounting/journal-entries | List Journal Entries
*AccountingApi.JournalEntriesApi* | [**journalEntriesDelete**](docs/JournalEntriesApi.md#journalEntriesDelete) | **DELETE** /accounting/journal-entries/{id} | Delete Journal Entry
*AccountingApi.JournalEntriesApi* | [**journalEntriesOne**](docs/JournalEntriesApi.md#journalEntriesOne) | **GET** /accounting/journal-entries/{id} | Get Journal Entry
*AccountingApi.JournalEntriesApi* | [**journalEntriesUpdate**](docs/JournalEntriesApi.md#journalEntriesUpdate) | **PATCH** /accounting/journal-entries/{id} | Update Journal Entry
*AccountingApi.LedgerAccountsApi* | [**ledgerAccountsAdd**](docs/LedgerAccountsApi.md#ledgerAccountsAdd) | **POST** /accounting/ledger-accounts | Create Ledger Account
*AccountingApi.LedgerAccountsApi* | [**ledgerAccountsAll**](docs/LedgerAccountsApi.md#ledgerAccountsAll) | **GET** /accounting/ledger-accounts | List Ledger Accounts
*AccountingApi.LedgerAccountsApi* | [**ledgerAccountsDelete**](docs/LedgerAccountsApi.md#ledgerAccountsDelete) | **DELETE** /accounting/ledger-accounts/{id} | Delete Ledger Account
*AccountingApi.LedgerAccountsApi* | [**ledgerAccountsOne**](docs/LedgerAccountsApi.md#ledgerAccountsOne) | **GET** /accounting/ledger-accounts/{id} | Get Ledger Account
*AccountingApi.LedgerAccountsApi* | [**ledgerAccountsUpdate**](docs/LedgerAccountsApi.md#ledgerAccountsUpdate) | **PATCH** /accounting/ledger-accounts/{id} | Update Ledger Account
*AccountingApi.PaymentsApi* | [**paymentsAdd**](docs/PaymentsApi.md#paymentsAdd) | **POST** /accounting/payments | Create Payment
*AccountingApi.PaymentsApi* | [**paymentsAll**](docs/PaymentsApi.md#paymentsAll) | **GET** /accounting/payments | List Payments
*AccountingApi.PaymentsApi* | [**paymentsDelete**](docs/PaymentsApi.md#paymentsDelete) | **DELETE** /accounting/payments/{id} | Delete Payment
*AccountingApi.PaymentsApi* | [**paymentsOne**](docs/PaymentsApi.md#paymentsOne) | **GET** /accounting/payments/{id} | Get Payment
*AccountingApi.PaymentsApi* | [**paymentsUpdate**](docs/PaymentsApi.md#paymentsUpdate) | **PATCH** /accounting/payments/{id} | Update Payment
*AccountingApi.ProfitAndLossApi* | [**profitAndLossOne**](docs/ProfitAndLossApi.md#profitAndLossOne) | **GET** /accounting/profit-and-loss | Get Profit and Loss
*AccountingApi.PurchaseOrdersApi* | [**purchaseOrdersAdd**](docs/PurchaseOrdersApi.md#purchaseOrdersAdd) | **POST** /accounting/purchase-orders | Create Purchase Order
*AccountingApi.PurchaseOrdersApi* | [**purchaseOrdersAll**](docs/PurchaseOrdersApi.md#purchaseOrdersAll) | **GET** /accounting/purchase-orders | List Purchase Orders
*AccountingApi.PurchaseOrdersApi* | [**purchaseOrdersDelete**](docs/PurchaseOrdersApi.md#purchaseOrdersDelete) | **DELETE** /accounting/purchase-orders/{id} | Delete Purchase Order
*AccountingApi.PurchaseOrdersApi* | [**purchaseOrdersOne**](docs/PurchaseOrdersApi.md#purchaseOrdersOne) | **GET** /accounting/purchase-orders/{id} | Get Purchase Order
*AccountingApi.PurchaseOrdersApi* | [**purchaseOrdersUpdate**](docs/PurchaseOrdersApi.md#purchaseOrdersUpdate) | **PATCH** /accounting/purchase-orders/{id} | Update Purchase Order
*AccountingApi.SuppliersApi* | [**suppliersAdd**](docs/SuppliersApi.md#suppliersAdd) | **POST** /accounting/suppliers | Create Supplier
*AccountingApi.SuppliersApi* | [**suppliersAll**](docs/SuppliersApi.md#suppliersAll) | **GET** /accounting/suppliers | List Suppliers
*AccountingApi.SuppliersApi* | [**suppliersDelete**](docs/SuppliersApi.md#suppliersDelete) | **DELETE** /accounting/suppliers/{id} | Delete Supplier
*AccountingApi.SuppliersApi* | [**suppliersOne**](docs/SuppliersApi.md#suppliersOne) | **GET** /accounting/suppliers/{id} | Get Supplier
*AccountingApi.SuppliersApi* | [**suppliersUpdate**](docs/SuppliersApi.md#suppliersUpdate) | **PATCH** /accounting/suppliers/{id} | Update Supplier
*AccountingApi.TaxRatesApi* | [**taxRatesAdd**](docs/TaxRatesApi.md#taxRatesAdd) | **POST** /accounting/tax-rates | Create Tax Rate
*AccountingApi.TaxRatesApi* | [**taxRatesAll**](docs/TaxRatesApi.md#taxRatesAll) | **GET** /accounting/tax-rates | List Tax Rates
*AccountingApi.TaxRatesApi* | [**taxRatesDelete**](docs/TaxRatesApi.md#taxRatesDelete) | **DELETE** /accounting/tax-rates/{id} | Delete Tax Rate
*AccountingApi.TaxRatesApi* | [**taxRatesOne**](docs/TaxRatesApi.md#taxRatesOne) | **GET** /accounting/tax-rates/{id} | Get Tax Rate
*AccountingApi.TaxRatesApi* | [**taxRatesUpdate**](docs/TaxRatesApi.md#taxRatesUpdate) | **PATCH** /accounting/tax-rates/{id} | Update Tax Rate


## Documentation for Models

 - [AccountingApi.AccountingEventType](docs/AccountingEventType.md)
 - [AccountingApi.AccountingWebhookEvent](docs/AccountingWebhookEvent.md)
 - [AccountingApi.Address](docs/Address.md)
 - [AccountingApi.BadRequestResponse](docs/BadRequestResponse.md)
 - [AccountingApi.BadRequestResponseDetail](docs/BadRequestResponseDetail.md)
 - [AccountingApi.BalanceSheet](docs/BalanceSheet.md)
 - [AccountingApi.BalanceSheetAssets](docs/BalanceSheetAssets.md)
 - [AccountingApi.BalanceSheetAssetsCurrentAssets](docs/BalanceSheetAssetsCurrentAssets.md)
 - [AccountingApi.BalanceSheetAssetsCurrentAssetsAccountsInner](docs/BalanceSheetAssetsCurrentAssetsAccountsInner.md)
 - [AccountingApi.BalanceSheetAssetsFixedAssets](docs/BalanceSheetAssetsFixedAssets.md)
 - [AccountingApi.BalanceSheetAssetsFixedAssetsAccountsInner](docs/BalanceSheetAssetsFixedAssetsAccountsInner.md)
 - [AccountingApi.BalanceSheetEquity](docs/BalanceSheetEquity.md)
 - [AccountingApi.BalanceSheetEquityItemsInner](docs/BalanceSheetEquityItemsInner.md)
 - [AccountingApi.BalanceSheetFilter](docs/BalanceSheetFilter.md)
 - [AccountingApi.BalanceSheetLiabilities](docs/BalanceSheetLiabilities.md)
 - [AccountingApi.BalanceSheetLiabilitiesAccountsInner](docs/BalanceSheetLiabilitiesAccountsInner.md)
 - [AccountingApi.BankAccount](docs/BankAccount.md)
 - [AccountingApi.Bill](docs/Bill.md)
 - [AccountingApi.BillLineItem](docs/BillLineItem.md)
 - [AccountingApi.BillsSort](docs/BillsSort.md)
 - [AccountingApi.CategoriesInner](docs/CategoriesInner.md)
 - [AccountingApi.Company](docs/Company.md)
 - [AccountingApi.CompanyInfo](docs/CompanyInfo.md)
 - [AccountingApi.CompanyRowType](docs/CompanyRowType.md)
 - [AccountingApi.Contact](docs/Contact.md)
 - [AccountingApi.CreateBillResponse](docs/CreateBillResponse.md)
 - [AccountingApi.CreateCreditNoteResponse](docs/CreateCreditNoteResponse.md)
 - [AccountingApi.CreateCustomerResponse](docs/CreateCustomerResponse.md)
 - [AccountingApi.CreateInvoiceItemResponse](docs/CreateInvoiceItemResponse.md)
 - [AccountingApi.CreateInvoiceResponse](docs/CreateInvoiceResponse.md)
 - [AccountingApi.CreateJournalEntryResponse](docs/CreateJournalEntryResponse.md)
 - [AccountingApi.CreateLedgerAccountResponse](docs/CreateLedgerAccountResponse.md)
 - [AccountingApi.CreatePaymentResponse](docs/CreatePaymentResponse.md)
 - [AccountingApi.CreatePurchaseOrderResponse](docs/CreatePurchaseOrderResponse.md)
 - [AccountingApi.CreateSupplierResponse](docs/CreateSupplierResponse.md)
 - [AccountingApi.CreateTaxRateResponse](docs/CreateTaxRateResponse.md)
 - [AccountingApi.CreditNote](docs/CreditNote.md)
 - [AccountingApi.CreditNoteAllocationsInner](docs/CreditNoteAllocationsInner.md)
 - [AccountingApi.Currency](docs/Currency.md)
 - [AccountingApi.CustomField](docs/CustomField.md)
 - [AccountingApi.CustomFieldValue](docs/CustomFieldValue.md)
 - [AccountingApi.Customer](docs/Customer.md)
 - [AccountingApi.CustomersFilter](docs/CustomersFilter.md)
 - [AccountingApi.DeleteBillResponse](docs/DeleteBillResponse.md)
 - [AccountingApi.DeleteCreditNoteResponse](docs/DeleteCreditNoteResponse.md)
 - [AccountingApi.DeleteCustomerResponse](docs/DeleteCustomerResponse.md)
 - [AccountingApi.DeleteInvoiceResponse](docs/DeleteInvoiceResponse.md)
 - [AccountingApi.DeleteJournalEntryResponse](docs/DeleteJournalEntryResponse.md)
 - [AccountingApi.DeleteLedgerAccountResponse](docs/DeleteLedgerAccountResponse.md)
 - [AccountingApi.DeletePaymentResponse](docs/DeletePaymentResponse.md)
 - [AccountingApi.DeletePurchaseOrderResponse](docs/DeletePurchaseOrderResponse.md)
 - [AccountingApi.DeleteSupplierResponse](docs/DeleteSupplierResponse.md)
 - [AccountingApi.DeleteTaxRateResponse](docs/DeleteTaxRateResponse.md)
 - [AccountingApi.Email](docs/Email.md)
 - [AccountingApi.GetBalanceSheetResponse](docs/GetBalanceSheetResponse.md)
 - [AccountingApi.GetBillResponse](docs/GetBillResponse.md)
 - [AccountingApi.GetBillsResponse](docs/GetBillsResponse.md)
 - [AccountingApi.GetCompanyInfoResponse](docs/GetCompanyInfoResponse.md)
 - [AccountingApi.GetCreditNoteResponse](docs/GetCreditNoteResponse.md)
 - [AccountingApi.GetCreditNotesResponse](docs/GetCreditNotesResponse.md)
 - [AccountingApi.GetCustomerResponse](docs/GetCustomerResponse.md)
 - [AccountingApi.GetCustomersResponse](docs/GetCustomersResponse.md)
 - [AccountingApi.GetInvoiceItemResponse](docs/GetInvoiceItemResponse.md)
 - [AccountingApi.GetInvoiceItemsResponse](docs/GetInvoiceItemsResponse.md)
 - [AccountingApi.GetInvoiceResponse](docs/GetInvoiceResponse.md)
 - [AccountingApi.GetInvoicesResponse](docs/GetInvoicesResponse.md)
 - [AccountingApi.GetJournalEntriesResponse](docs/GetJournalEntriesResponse.md)
 - [AccountingApi.GetJournalEntryResponse](docs/GetJournalEntryResponse.md)
 - [AccountingApi.GetLedgerAccountResponse](docs/GetLedgerAccountResponse.md)
 - [AccountingApi.GetLedgerAccountsResponse](docs/GetLedgerAccountsResponse.md)
 - [AccountingApi.GetPaymentResponse](docs/GetPaymentResponse.md)
 - [AccountingApi.GetPaymentsResponse](docs/GetPaymentsResponse.md)
 - [AccountingApi.GetProfitAndLossResponse](docs/GetProfitAndLossResponse.md)
 - [AccountingApi.GetPurchaseOrderResponse](docs/GetPurchaseOrderResponse.md)
 - [AccountingApi.GetPurchaseOrdersResponse](docs/GetPurchaseOrdersResponse.md)
 - [AccountingApi.GetSupplierResponse](docs/GetSupplierResponse.md)
 - [AccountingApi.GetSuppliersResponse](docs/GetSuppliersResponse.md)
 - [AccountingApi.GetTaxRateResponse](docs/GetTaxRateResponse.md)
 - [AccountingApi.GetTaxRatesResponse](docs/GetTaxRatesResponse.md)
 - [AccountingApi.Invoice](docs/Invoice.md)
 - [AccountingApi.InvoiceItem](docs/InvoiceItem.md)
 - [AccountingApi.InvoiceItemPurchaseDetails](docs/InvoiceItemPurchaseDetails.md)
 - [AccountingApi.InvoiceItemsFilter](docs/InvoiceItemsFilter.md)
 - [AccountingApi.InvoiceLineItem](docs/InvoiceLineItem.md)
 - [AccountingApi.InvoiceResponse](docs/InvoiceResponse.md)
 - [AccountingApi.InvoicesSort](docs/InvoicesSort.md)
 - [AccountingApi.JournalEntry](docs/JournalEntry.md)
 - [AccountingApi.JournalEntryLineItem](docs/JournalEntryLineItem.md)
 - [AccountingApi.LedgerAccount](docs/LedgerAccount.md)
 - [AccountingApi.LedgerAccountParentAccount](docs/LedgerAccountParentAccount.md)
 - [AccountingApi.LinkedCustomer](docs/LinkedCustomer.md)
 - [AccountingApi.LinkedInvoiceItem](docs/LinkedInvoiceItem.md)
 - [AccountingApi.LinkedLedgerAccount](docs/LinkedLedgerAccount.md)
 - [AccountingApi.LinkedParentCustomer](docs/LinkedParentCustomer.md)
 - [AccountingApi.LinkedSupplier](docs/LinkedSupplier.md)
 - [AccountingApi.LinkedTaxRate](docs/LinkedTaxRate.md)
 - [AccountingApi.LinkedTrackingCategory](docs/LinkedTrackingCategory.md)
 - [AccountingApi.Links](docs/Links.md)
 - [AccountingApi.Meta](docs/Meta.md)
 - [AccountingApi.MetaCursors](docs/MetaCursors.md)
 - [AccountingApi.NotFoundResponse](docs/NotFoundResponse.md)
 - [AccountingApi.NotFoundResponseDetail](docs/NotFoundResponseDetail.md)
 - [AccountingApi.NotImplementedResponse](docs/NotImplementedResponse.md)
 - [AccountingApi.NotImplementedResponseDetail](docs/NotImplementedResponseDetail.md)
 - [AccountingApi.PassThroughQuery](docs/PassThroughQuery.md)
 - [AccountingApi.Payment](docs/Payment.md)
 - [AccountingApi.PaymentAllocationsInner](docs/PaymentAllocationsInner.md)
 - [AccountingApi.PaymentRequiredResponse](docs/PaymentRequiredResponse.md)
 - [AccountingApi.PaymentsFilter](docs/PaymentsFilter.md)
 - [AccountingApi.PhoneNumber](docs/PhoneNumber.md)
 - [AccountingApi.ProfitAndLoss](docs/ProfitAndLoss.md)
 - [AccountingApi.ProfitAndLossExpenses](docs/ProfitAndLossExpenses.md)
 - [AccountingApi.ProfitAndLossFilter](docs/ProfitAndLossFilter.md)
 - [AccountingApi.ProfitAndLossGrossProfit](docs/ProfitAndLossGrossProfit.md)
 - [AccountingApi.ProfitAndLossIncome](docs/ProfitAndLossIncome.md)
 - [AccountingApi.ProfitAndLossNetIncome](docs/ProfitAndLossNetIncome.md)
 - [AccountingApi.ProfitAndLossNetOperatingIncome](docs/ProfitAndLossNetOperatingIncome.md)
 - [AccountingApi.ProfitAndLossRecord](docs/ProfitAndLossRecord.md)
 - [AccountingApi.ProfitAndLossRecordsInner](docs/ProfitAndLossRecordsInner.md)
 - [AccountingApi.ProfitAndLossSection](docs/ProfitAndLossSection.md)
 - [AccountingApi.PurchaseOrder](docs/PurchaseOrder.md)
 - [AccountingApi.SocialLink](docs/SocialLink.md)
 - [AccountingApi.SortDirection](docs/SortDirection.md)
 - [AccountingApi.SubAccountsInner](docs/SubAccountsInner.md)
 - [AccountingApi.Supplier](docs/Supplier.md)
 - [AccountingApi.SuppliersFilter](docs/SuppliersFilter.md)
 - [AccountingApi.TaxComponentsInner](docs/TaxComponentsInner.md)
 - [AccountingApi.TaxRate](docs/TaxRate.md)
 - [AccountingApi.TaxRatesFilter](docs/TaxRatesFilter.md)
 - [AccountingApi.TooManyRequestsResponse](docs/TooManyRequestsResponse.md)
 - [AccountingApi.TooManyRequestsResponseDetail](docs/TooManyRequestsResponseDetail.md)
 - [AccountingApi.UnauthorizedResponse](docs/UnauthorizedResponse.md)
 - [AccountingApi.UnexpectedErrorResponse](docs/UnexpectedErrorResponse.md)
 - [AccountingApi.UnexpectedErrorResponseDetail](docs/UnexpectedErrorResponseDetail.md)
 - [AccountingApi.UnifiedId](docs/UnifiedId.md)
 - [AccountingApi.UnprocessableResponse](docs/UnprocessableResponse.md)
 - [AccountingApi.UpdateBillResponse](docs/UpdateBillResponse.md)
 - [AccountingApi.UpdateCreditNoteResponse](docs/UpdateCreditNoteResponse.md)
 - [AccountingApi.UpdateCustomerResponse](docs/UpdateCustomerResponse.md)
 - [AccountingApi.UpdateInvoiceItemsResponse](docs/UpdateInvoiceItemsResponse.md)
 - [AccountingApi.UpdateInvoiceResponse](docs/UpdateInvoiceResponse.md)
 - [AccountingApi.UpdateJournalEntryResponse](docs/UpdateJournalEntryResponse.md)
 - [AccountingApi.UpdateLedgerAccountResponse](docs/UpdateLedgerAccountResponse.md)
 - [AccountingApi.UpdatePaymentResponse](docs/UpdatePaymentResponse.md)
 - [AccountingApi.UpdatePurchaseOrderResponse](docs/UpdatePurchaseOrderResponse.md)
 - [AccountingApi.UpdateSupplierResponse](docs/UpdateSupplierResponse.md)
 - [AccountingApi.UpdateTaxRateResponse](docs/UpdateTaxRateResponse.md)
 - [AccountingApi.Website](docs/Website.md)


## Documentation for Authorization


Authentication schemes defined for the API:
### apiKey


- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header

