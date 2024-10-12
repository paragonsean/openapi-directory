/**
 * Accounting API
 * Welcome to the Accounting API.  You can use this API to access all Accounting API endpoints.  ## Base URL  The base URL for all API requests is `https://unify.apideck.com`  ## Headers  Custom headers that are expected as part of the request. Note that [RFC7230](https://tools.ietf.org/html/rfc7230) states header names are case insensitive.  | Name                  | Type    | Required | Description                                                                                                                                                    | | --------------------- | ------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | | x-apideck-consumer-id | String  | Yes      | The id of the customer stored inside Apideck Vault. This can be a user id, account id, device id or whatever entity that can have integration within your app. | | x-apideck-service-id  | String  | No       | Describe the service you want to call (e.g., pipedrive). Only needed when a customer has activated multiple integrations for the same Unified API.             | | x-apideck-raw         | Boolean | No       | Include raw response. Mostly used for debugging purposes.                                                                                                      | | x-apideck-app-id      | String  | Yes      | The application id of your Unify application. Available at https://app.apideck.com/unify/api-keys.                                                             | | Authorization         | String  | Yes      | Bearer API KEY                                                                                                                                                 |  ## Authorization  You can interact with the API through the authorization methods below.  <!-- ReDoc-Inject: <security-definitions> -->  ## Pagination  All API resources have support for bulk retrieval via list APIs.  Apideck uses cursor-based pagination via the optional `cursor` and `limit` parameters.  To fetch the first page of results, call the list API without a `cursor` parameter. Afterwards you can fetch subsequent pages by providing a cursor parameter. You will find the next cursor in the response body in `meta.cursors.next`. If `meta.cursors.next` is `null` you're at the end of the list.  In the REST API you can also use the `links` from the response for added convenience. Simply call the URL in `links.next` to get the next page of results.  ### Query Parameters  | Name   | Type   | Required | Description                                                                                                        | | ------ | ------ | -------- | ------------------------------------------------------------------------------------------------------------------ | | cursor | String | No       | Cursor to start from. You can find cursors for next & previous pages in the meta.cursors property of the response. | | limit  | Number | No       | Number of results to return. Minimum 1, Maximum 200, Default 20                                                    |  ### Response Body  | Name                  | Type   | Description                                                        | | --------------------- | ------ | ------------------------------------------------------------------ | | meta.cursors.previous | String | Cursor to navigate to the previous page of results through the API | | meta.cursors.current  | String | Cursor to navigate to the current page of results through the API  | | meta.cursors.next     | String | Cursor to navigate to the next page of results through the API     | | meta.items_on_page    | Number | Number of items returned in the data property of the response      | | links.previous        | String | Link to navigate to the previous page of results through the API   | | links.current         | String | Link to navigate to the current page of results through the API    | | links.next            | String | Link to navigate to the next page of results through the API       |  ⚠️ `meta.cursors.previous`/`links.previous` is not available for all connectors.  ## SDKs and API Clients  We currently offer a [Node.js](https://developers.apideck.com/sdks/node), [PHP](https://developers.apideck.com/sdks/php) and [.NET](https://developers.apideck.com/sdks/dot-net) SDK. Need another SDK? [Request the SDK of your choice](https://integrations.apideck.com/request).  ## Debugging  Because of the nature of the abstraction we do in Apideck Unify we still provide the option to the receive raw requests and responses being handled underlying. By including the raw flag `?raw=true` in your requests you can still receive the full request. Please note that this increases the response size and can introduce extra latency.  ## Errors  The API returns standard HTTP response codes to indicate success or failure of the API requests. For errors, we also return a customized error message inside the JSON response. You can see the returned HTTP status codes below.  | Code | Title                | Description                                                                                                                                                                                              | | ---- | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | | 200  | OK                   | The request message has been successfully processed, and it has produced a response. The response message varies, depending on the request method and the requested data.                                | | 201  | Created              | The request has been fulfilled and has resulted in one or more new resources being created.                                                                                                              | | 204  | No Content           | The server has successfully fulfilled the request and that there is no additional content to send in the response payload body.                                                                          | | 400  | Bad Request          | The receiving server cannot understand the request because of malformed syntax. Do not repeat the request without first modifying it; check the request for errors, fix them and then retry the request. | | 401  | Unauthorized         | The request has not been applied because it lacks valid authentication credentials for the target resource.                                                                                              | | 402  | Payment Required     | Subscription data is incomplete or out of date. You'll need to provide payment details to continue.                                                                                                      | | 403  | Forbidden            | You do not have the appropriate user rights to access the request. Do not repeat the request.                                                                                                            | | 404  | Not Found            | The origin server did not find a current representation for the target resource or is not willing to disclose that one exists.                                                                           | | 409  | Conflict             | The request could not be completed due to a conflict with the current state of the target resource.                                                                                                      | | 422  | Unprocessable Entity | The server understands the content type of the request entity, and the syntax of the request entity is correct but was unable to process the contained instructions.                                     | | 429  | Too Many Requests    | You sent too many requests in a given amount of time (\"rate limit\"). Try again later                                                                                                                     | | 5xx  | Server Errors        | Something went wrong with the Unify API. These errors are logged on our side. You can contact our team to resolve the issue.                                                                             |  ### Handling errors  The Unify API and SDKs can produce errors for many reasons, such as a failed requests due to misconfigured integrations, invalid parameters, authentication errors, and network unavailability.  ### Error Types  #### RequestValidationError  Request is not valid for the current endpoint. The response body will include details on the validation error. Check the spelling and types of your attributes, and ensure you are not passing data that is outside of the specification.  #### UnsupportedFiltersError  Filters in the request are valid, but not supported by the connector. Remove the unsupported filter(s) to get a successful response.  #### UnsupportedSortFieldError  Sort field (`sort[by]`) in the request is valid, but not supported by the connector. Replace or remove the sort field to get a successful response.  #### InvalidCursorError  Pagination cursor in the request is not valid for the current connector. Make sure to use a cursor returned from the API, for the same connector.  #### ConnectorExecutionError  A Unified API request made via one of our downstream connectors returned an unexpected error. The `status_code` returned is proxied through to error response along with their original response via the error detail.  #### UnauthorizedError  We were unable to authorize the request as made. This can happen for a number of reasons, from missing header params to passing an incorrect authorization token. Verify your Api Key is being set correctly in the authorization header. ie: `Authorization: 'Bearer sk_live_***'`  #### ConnectorCredentialsError  A request using a given connector has not been authorized. Ensure the connector you are trying to use has been configured correctly and been authorized for use.  #### ConnectorDisabledError  A request has been made to a connector that has since been disabled. This may be temporary - You can contact our team to resolve the issue.  #### ConnectorRateLimitError  You sent too many request to a connector. These rate limits vary from connector to connector. You will need to try again later.  #### RequestLimitError  You have reached the number of requests included in your Free Tier Subscription. You will no be able to make further requests until this limit resets at the end of the month, or talk to us about upgrading your subscription to continue immediately.  #### EntityNotFoundError  You've made a request for a resource or route that does not exist. Verify your path parameters or any identifiers used to fetch this resource.  #### OAuthCredentialsNotFoundError  When adding a connector integration that implements OAuth, both a `client_id` and `client_secret` must be provided before any authorizations can be performed. Verify the integration has been configured properly before continuing.  #### IntegrationNotFoundError  The requested connector integration could not be found associated to your `application_id`. Verify your `application_id` is correct, and that this connector has been added and configured for your application.  #### ConnectionNotFoundError  A valid connection could not be found associated to your `application_id`. Something _may_ have interrupted the authorization flow. You may need to start the connector authorization process again.  #### ConnectionSettingsError  The connector has required settings that were not supplied. Verify `connection.settings` contains all required settings for the connector to be callable.  #### ConnectorNotFoundError  A request was made for an unknown connector. Verify your `service_id` is spelled correctly, and that this connector is enabled for your provided `unified_api`.  #### OAuthRedirectUriError  A request was made either in a connector authorization flow, or attempting to revoke connector access without a valid `redirect_uri`. This is the url the user should be returned to on completion of process.  #### OAuthInvalidStateError  The state param is required and is used to ensure the outgoing authorization state has not been altered before the user is redirected back. It also contains required params needed to identify the connector being used. If this has been altered, the authorization will not succeed.  #### OAuthCodeExchangeError  When attempting to exchange the authorization code for an `access_token` during an OAuth flow, an error occurred. This may be temporary. You can reattempt authorization or contact our team to resolve the issue.  #### OAuthConnectorError  It seems something went wrong on the connector side. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### MappingError  There was an error attempting to retrieve the mapping for a given attribute. We've been notified and are working to fix this issue.  #### ConnectorMappingNotFoundError  It seems the implementation for this connector is incomplete. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorResponseMappingNotFoundError  We were unable to retrieve the response mapping for this connector. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorOperationMappingNotFoundError  Connector mapping has not been implemented for the requested operation. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorWorkflowMappingError  The composite api calls required for this operation have not been mapped entirely. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorOperationUnsupportedError  You're attempting a call that is not supported by the connector. It's likely this operation is supported by another connector, but we're unable to implement for this one.  #### PaginationNotSupportedError  Pagination is not yet supported for this connector, try removing limit and/or cursor from the query. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  ## API Design  ### API Styles and data formats  #### REST API  The API is organized around [REST](https://restfulapi.net/), providing simple and predictable URIs to access and modify objects. Requests support standard HTTP methods like GET, PUT, POST, and DELETE and standard status codes. JSON is returned by all API responses, including errors. In all API requests, you must set the content-type HTTP header to application/json. All API requests must be made over HTTPS. Calls made over HTTP will fail.  ##### Available HTTP methods  The Apideck API uses HTTP verbs to understand if you want to read (GET), delete (DELETE) or create (POST) an object. When your web application cannot do a POST or DELETE, we provide the ability to set the method through the query parameter \\_method.  ``` POST /messages GET /messages GET /messages/{messageId} PATCH /messages/{messageId} DELETE /messages/{messageId} ```  Response bodies are always UTF-8 encoded JSON objects, unless explicitly documented otherwise. For some endpoints and use cases we divert from REST to provide a better developer experience.  ### Schema  All API requests and response bodies adhere to a common JSON format representing individual items, collections of items, links to related items and additional meta data.  ### Meta  Meta data can be represented as a top level member named “meta”. Any information may be provided in the meta data. It’s most common use is to return the total number of records when requesting a collection of resources.  ### Idempotence (upcoming)  To prevent the creation of duplicate resources, every POST method (such as one that creates a consumer record) must specify a unique value for the X-Unique-Transaction-ID header name. Uniquely identifying each unique POST request ensures that the API processes a given request once and only once.  Uniquely identifying new resource-creation POSTs is especially important when the outcome of a response is ambiguous because of a transient service interruption, such as a server-side timeout or network disruption. If a service interruption occurs, then the client application can safely retry the uniquely identified request without creating duplicate operations. (API endpoints that guarantee that every uniquely identified request is processed only once no matter how many times that uniquely identifiable request is made are described as idempotent.)  ### Request IDs  Each API request has an associated request identifier. You can find this value in the response headers, under Request-Id. You can also find request identifiers in the URLs of individual request logs in your Dashboard. If you need to contact us about a specific request, providing the request identifier will ensure the fastest possible resolution.  ### Fixed field types  #### Dates  The dates returned by the API are all represented in UTC (ISO8601 format).  This example `2019-11-14T00:55:31.820Z` is defined by the ISO 8601 standard. The T in the middle separates the year-month-day portion from the hour-minute-second portion. The Z on the end means UTC, that is, an offset-from-UTC of zero hours-minutes-seconds. The Z is pronounced \"Zulu\" per military/aviation tradition.  The ISO 8601 standard is more modern. The formats are wisely designed to be easy to parse by machine as well as easy to read by humans across cultures.  #### Prices and Currencies  All prices returned by the API are represented as integer amounts in a currency’s smallest unit. For example, $5 USD would be returned as 500 (i.e, 500 cents).  For zero-decimal currencies, amounts will still be provided as an integer but without the need to divide by 100. For example, an amount of ¥5 (JPY) would be returned as 5.  All currency codes conform to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217).  ## Support  If you have problems or need help with your case, you can always reach out to our Support.  
 *
 * The version of the OpenAPI document: 10.0.0
 * Contact: hello@apideck.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from './ApiClient';
import AccountingEventType from './model/AccountingEventType';
import AccountingWebhookEvent from './model/AccountingWebhookEvent';
import Address from './model/Address';
import BadRequestResponse from './model/BadRequestResponse';
import BadRequestResponseDetail from './model/BadRequestResponseDetail';
import BalanceSheet from './model/BalanceSheet';
import BalanceSheetAssets from './model/BalanceSheetAssets';
import BalanceSheetAssetsCurrentAssets from './model/BalanceSheetAssetsCurrentAssets';
import BalanceSheetAssetsCurrentAssetsAccountsInner from './model/BalanceSheetAssetsCurrentAssetsAccountsInner';
import BalanceSheetAssetsFixedAssets from './model/BalanceSheetAssetsFixedAssets';
import BalanceSheetAssetsFixedAssetsAccountsInner from './model/BalanceSheetAssetsFixedAssetsAccountsInner';
import BalanceSheetEquity from './model/BalanceSheetEquity';
import BalanceSheetEquityItemsInner from './model/BalanceSheetEquityItemsInner';
import BalanceSheetFilter from './model/BalanceSheetFilter';
import BalanceSheetLiabilities from './model/BalanceSheetLiabilities';
import BalanceSheetLiabilitiesAccountsInner from './model/BalanceSheetLiabilitiesAccountsInner';
import BankAccount from './model/BankAccount';
import Bill from './model/Bill';
import BillLineItem from './model/BillLineItem';
import BillsSort from './model/BillsSort';
import CategoriesInner from './model/CategoriesInner';
import Company from './model/Company';
import CompanyInfo from './model/CompanyInfo';
import CompanyRowType from './model/CompanyRowType';
import Contact from './model/Contact';
import CreateBillResponse from './model/CreateBillResponse';
import CreateCreditNoteResponse from './model/CreateCreditNoteResponse';
import CreateCustomerResponse from './model/CreateCustomerResponse';
import CreateInvoiceItemResponse from './model/CreateInvoiceItemResponse';
import CreateInvoiceResponse from './model/CreateInvoiceResponse';
import CreateJournalEntryResponse from './model/CreateJournalEntryResponse';
import CreateLedgerAccountResponse from './model/CreateLedgerAccountResponse';
import CreatePaymentResponse from './model/CreatePaymentResponse';
import CreatePurchaseOrderResponse from './model/CreatePurchaseOrderResponse';
import CreateSupplierResponse from './model/CreateSupplierResponse';
import CreateTaxRateResponse from './model/CreateTaxRateResponse';
import CreditNote from './model/CreditNote';
import CreditNoteAllocationsInner from './model/CreditNoteAllocationsInner';
import Currency from './model/Currency';
import CustomField from './model/CustomField';
import CustomFieldValue from './model/CustomFieldValue';
import Customer from './model/Customer';
import CustomersFilter from './model/CustomersFilter';
import DeleteBillResponse from './model/DeleteBillResponse';
import DeleteCreditNoteResponse from './model/DeleteCreditNoteResponse';
import DeleteCustomerResponse from './model/DeleteCustomerResponse';
import DeleteInvoiceResponse from './model/DeleteInvoiceResponse';
import DeleteJournalEntryResponse from './model/DeleteJournalEntryResponse';
import DeleteLedgerAccountResponse from './model/DeleteLedgerAccountResponse';
import DeletePaymentResponse from './model/DeletePaymentResponse';
import DeletePurchaseOrderResponse from './model/DeletePurchaseOrderResponse';
import DeleteSupplierResponse from './model/DeleteSupplierResponse';
import DeleteTaxRateResponse from './model/DeleteTaxRateResponse';
import Email from './model/Email';
import GetBalanceSheetResponse from './model/GetBalanceSheetResponse';
import GetBillResponse from './model/GetBillResponse';
import GetBillsResponse from './model/GetBillsResponse';
import GetCompanyInfoResponse from './model/GetCompanyInfoResponse';
import GetCreditNoteResponse from './model/GetCreditNoteResponse';
import GetCreditNotesResponse from './model/GetCreditNotesResponse';
import GetCustomerResponse from './model/GetCustomerResponse';
import GetCustomersResponse from './model/GetCustomersResponse';
import GetInvoiceItemResponse from './model/GetInvoiceItemResponse';
import GetInvoiceItemsResponse from './model/GetInvoiceItemsResponse';
import GetInvoiceResponse from './model/GetInvoiceResponse';
import GetInvoicesResponse from './model/GetInvoicesResponse';
import GetJournalEntriesResponse from './model/GetJournalEntriesResponse';
import GetJournalEntryResponse from './model/GetJournalEntryResponse';
import GetLedgerAccountResponse from './model/GetLedgerAccountResponse';
import GetLedgerAccountsResponse from './model/GetLedgerAccountsResponse';
import GetPaymentResponse from './model/GetPaymentResponse';
import GetPaymentsResponse from './model/GetPaymentsResponse';
import GetProfitAndLossResponse from './model/GetProfitAndLossResponse';
import GetPurchaseOrderResponse from './model/GetPurchaseOrderResponse';
import GetPurchaseOrdersResponse from './model/GetPurchaseOrdersResponse';
import GetSupplierResponse from './model/GetSupplierResponse';
import GetSuppliersResponse from './model/GetSuppliersResponse';
import GetTaxRateResponse from './model/GetTaxRateResponse';
import GetTaxRatesResponse from './model/GetTaxRatesResponse';
import Invoice from './model/Invoice';
import InvoiceItem from './model/InvoiceItem';
import InvoiceItemPurchaseDetails from './model/InvoiceItemPurchaseDetails';
import InvoiceItemsFilter from './model/InvoiceItemsFilter';
import InvoiceLineItem from './model/InvoiceLineItem';
import InvoiceResponse from './model/InvoiceResponse';
import InvoicesSort from './model/InvoicesSort';
import JournalEntry from './model/JournalEntry';
import JournalEntryLineItem from './model/JournalEntryLineItem';
import LedgerAccount from './model/LedgerAccount';
import LedgerAccountParentAccount from './model/LedgerAccountParentAccount';
import LinkedCustomer from './model/LinkedCustomer';
import LinkedInvoiceItem from './model/LinkedInvoiceItem';
import LinkedLedgerAccount from './model/LinkedLedgerAccount';
import LinkedParentCustomer from './model/LinkedParentCustomer';
import LinkedSupplier from './model/LinkedSupplier';
import LinkedTaxRate from './model/LinkedTaxRate';
import LinkedTrackingCategory from './model/LinkedTrackingCategory';
import Links from './model/Links';
import Meta from './model/Meta';
import MetaCursors from './model/MetaCursors';
import NotFoundResponse from './model/NotFoundResponse';
import NotFoundResponseDetail from './model/NotFoundResponseDetail';
import NotImplementedResponse from './model/NotImplementedResponse';
import NotImplementedResponseDetail from './model/NotImplementedResponseDetail';
import PassThroughQuery from './model/PassThroughQuery';
import Payment from './model/Payment';
import PaymentAllocationsInner from './model/PaymentAllocationsInner';
import PaymentRequiredResponse from './model/PaymentRequiredResponse';
import PaymentsFilter from './model/PaymentsFilter';
import PhoneNumber from './model/PhoneNumber';
import ProfitAndLoss from './model/ProfitAndLoss';
import ProfitAndLossExpenses from './model/ProfitAndLossExpenses';
import ProfitAndLossFilter from './model/ProfitAndLossFilter';
import ProfitAndLossGrossProfit from './model/ProfitAndLossGrossProfit';
import ProfitAndLossIncome from './model/ProfitAndLossIncome';
import ProfitAndLossNetIncome from './model/ProfitAndLossNetIncome';
import ProfitAndLossNetOperatingIncome from './model/ProfitAndLossNetOperatingIncome';
import ProfitAndLossRecord from './model/ProfitAndLossRecord';
import ProfitAndLossRecordsInner from './model/ProfitAndLossRecordsInner';
import ProfitAndLossSection from './model/ProfitAndLossSection';
import PurchaseOrder from './model/PurchaseOrder';
import SocialLink from './model/SocialLink';
import SortDirection from './model/SortDirection';
import SubAccountsInner from './model/SubAccountsInner';
import Supplier from './model/Supplier';
import SuppliersFilter from './model/SuppliersFilter';
import TaxComponentsInner from './model/TaxComponentsInner';
import TaxRate from './model/TaxRate';
import TaxRatesFilter from './model/TaxRatesFilter';
import TooManyRequestsResponse from './model/TooManyRequestsResponse';
import TooManyRequestsResponseDetail from './model/TooManyRequestsResponseDetail';
import UnauthorizedResponse from './model/UnauthorizedResponse';
import UnexpectedErrorResponse from './model/UnexpectedErrorResponse';
import UnexpectedErrorResponseDetail from './model/UnexpectedErrorResponseDetail';
import UnifiedId from './model/UnifiedId';
import UnprocessableResponse from './model/UnprocessableResponse';
import UpdateBillResponse from './model/UpdateBillResponse';
import UpdateCreditNoteResponse from './model/UpdateCreditNoteResponse';
import UpdateCustomerResponse from './model/UpdateCustomerResponse';
import UpdateInvoiceItemsResponse from './model/UpdateInvoiceItemsResponse';
import UpdateInvoiceResponse from './model/UpdateInvoiceResponse';
import UpdateJournalEntryResponse from './model/UpdateJournalEntryResponse';
import UpdateLedgerAccountResponse from './model/UpdateLedgerAccountResponse';
import UpdatePaymentResponse from './model/UpdatePaymentResponse';
import UpdatePurchaseOrderResponse from './model/UpdatePurchaseOrderResponse';
import UpdateSupplierResponse from './model/UpdateSupplierResponse';
import UpdateTaxRateResponse from './model/UpdateTaxRateResponse';
import Website from './model/Website';
import BalanceSheetApi from './api/BalanceSheetApi';
import BillsApi from './api/BillsApi';
import CompanyInfoApi from './api/CompanyInfoApi';
import CreditNotesApi from './api/CreditNotesApi';
import CustomersApi from './api/CustomersApi';
import InvoiceItemsApi from './api/InvoiceItemsApi';
import InvoicesApi from './api/InvoicesApi';
import JournalEntriesApi from './api/JournalEntriesApi';
import LedgerAccountsApi from './api/LedgerAccountsApi';
import PaymentsApi from './api/PaymentsApi';
import ProfitAndLossApi from './api/ProfitAndLossApi';
import PurchaseOrdersApi from './api/PurchaseOrdersApi';
import SuppliersApi from './api/SuppliersApi';
import TaxRatesApi from './api/TaxRatesApi';


/**
* Welcome to the Accounting API.  You can use this API to access all Accounting API endpoints.  ## Base URL  The base URL for all API requests is &#x60;https://unify.apideck.com&#x60;  ## Headers  Custom headers that are expected as part of the request. Note that [RFC7230](https://tools.ietf.org/html/rfc7230) states header names are case insensitive.  | Name                  | Type    | Required | Description                                                                                                                                                    | | --------------------- | ------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | | x-apideck-consumer-id | String  | Yes      | The id of the customer stored inside Apideck Vault. This can be a user id, account id, device id or whatever entity that can have integration within your app. | | x-apideck-service-id  | String  | No       | Describe the service you want to call (e.g., pipedrive). Only needed when a customer has activated multiple integrations for the same Unified API.             | | x-apideck-raw         | Boolean | No       | Include raw response. Mostly used for debugging purposes.                                                                                                      | | x-apideck-app-id      | String  | Yes      | The application id of your Unify application. Available at https://app.apideck.com/unify/api-keys.                                                             | | Authorization         | String  | Yes      | Bearer API KEY                                                                                                                                                 |  ## Authorization  You can interact with the API through the authorization methods below.  &lt;!-- ReDoc-Inject: &lt;security-definitions&gt; --&gt;  ## Pagination  All API resources have support for bulk retrieval via list APIs.  Apideck uses cursor-based pagination via the optional &#x60;cursor&#x60; and &#x60;limit&#x60; parameters.  To fetch the first page of results, call the list API without a &#x60;cursor&#x60; parameter. Afterwards you can fetch subsequent pages by providing a cursor parameter. You will find the next cursor in the response body in &#x60;meta.cursors.next&#x60;. If &#x60;meta.cursors.next&#x60; is &#x60;null&#x60; you&#39;re at the end of the list.  In the REST API you can also use the &#x60;links&#x60; from the response for added convenience. Simply call the URL in &#x60;links.next&#x60; to get the next page of results.  ### Query Parameters  | Name   | Type   | Required | Description                                                                                                        | | ------ | ------ | -------- | ------------------------------------------------------------------------------------------------------------------ | | cursor | String | No       | Cursor to start from. You can find cursors for next &amp; previous pages in the meta.cursors property of the response. | | limit  | Number | No       | Number of results to return. Minimum 1, Maximum 200, Default 20                                                    |  ### Response Body  | Name                  | Type   | Description                                                        | | --------------------- | ------ | ------------------------------------------------------------------ | | meta.cursors.previous | String | Cursor to navigate to the previous page of results through the API | | meta.cursors.current  | String | Cursor to navigate to the current page of results through the API  | | meta.cursors.next     | String | Cursor to navigate to the next page of results through the API     | | meta.items_on_page    | Number | Number of items returned in the data property of the response      | | links.previous        | String | Link to navigate to the previous page of results through the API   | | links.current         | String | Link to navigate to the current page of results through the API    | | links.next            | String | Link to navigate to the next page of results through the API       |  ⚠️ &#x60;meta.cursors.previous&#x60;/&#x60;links.previous&#x60; is not available for all connectors.  ## SDKs and API Clients  We currently offer a [Node.js](https://developers.apideck.com/sdks/node), [PHP](https://developers.apideck.com/sdks/php) and [.NET](https://developers.apideck.com/sdks/dot-net) SDK. Need another SDK? [Request the SDK of your choice](https://integrations.apideck.com/request).  ## Debugging  Because of the nature of the abstraction we do in Apideck Unify we still provide the option to the receive raw requests and responses being handled underlying. By including the raw flag &#x60;?raw&#x3D;true&#x60; in your requests you can still receive the full request. Please note that this increases the response size and can introduce extra latency.  ## Errors  The API returns standard HTTP response codes to indicate success or failure of the API requests. For errors, we also return a customized error message inside the JSON response. You can see the returned HTTP status codes below.  | Code | Title                | Description                                                                                                                                                                                              | | ---- | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | | 200  | OK                   | The request message has been successfully processed, and it has produced a response. The response message varies, depending on the request method and the requested data.                                | | 201  | Created              | The request has been fulfilled and has resulted in one or more new resources being created.                                                                                                              | | 204  | No Content           | The server has successfully fulfilled the request and that there is no additional content to send in the response payload body.                                                                          | | 400  | Bad Request          | The receiving server cannot understand the request because of malformed syntax. Do not repeat the request without first modifying it; check the request for errors, fix them and then retry the request. | | 401  | Unauthorized         | The request has not been applied because it lacks valid authentication credentials for the target resource.                                                                                              | | 402  | Payment Required     | Subscription data is incomplete or out of date. You&#39;ll need to provide payment details to continue.                                                                                                      | | 403  | Forbidden            | You do not have the appropriate user rights to access the request. Do not repeat the request.                                                                                                            | | 404  | Not Found            | The origin server did not find a current representation for the target resource or is not willing to disclose that one exists.                                                                           | | 409  | Conflict             | The request could not be completed due to a conflict with the current state of the target resource.                                                                                                      | | 422  | Unprocessable Entity | The server understands the content type of the request entity, and the syntax of the request entity is correct but was unable to process the contained instructions.                                     | | 429  | Too Many Requests    | You sent too many requests in a given amount of time (\&quot;rate limit\&quot;). Try again later                                                                                                                     | | 5xx  | Server Errors        | Something went wrong with the Unify API. These errors are logged on our side. You can contact our team to resolve the issue.                                                                             |  ### Handling errors  The Unify API and SDKs can produce errors for many reasons, such as a failed requests due to misconfigured integrations, invalid parameters, authentication errors, and network unavailability.  ### Error Types  #### RequestValidationError  Request is not valid for the current endpoint. The response body will include details on the validation error. Check the spelling and types of your attributes, and ensure you are not passing data that is outside of the specification.  #### UnsupportedFiltersError  Filters in the request are valid, but not supported by the connector. Remove the unsupported filter(s) to get a successful response.  #### UnsupportedSortFieldError  Sort field (&#x60;sort[by]&#x60;) in the request is valid, but not supported by the connector. Replace or remove the sort field to get a successful response.  #### InvalidCursorError  Pagination cursor in the request is not valid for the current connector. Make sure to use a cursor returned from the API, for the same connector.  #### ConnectorExecutionError  A Unified API request made via one of our downstream connectors returned an unexpected error. The &#x60;status_code&#x60; returned is proxied through to error response along with their original response via the error detail.  #### UnauthorizedError  We were unable to authorize the request as made. This can happen for a number of reasons, from missing header params to passing an incorrect authorization token. Verify your Api Key is being set correctly in the authorization header. ie: &#x60;Authorization: &#39;Bearer sk_live_***&#39;&#x60;  #### ConnectorCredentialsError  A request using a given connector has not been authorized. Ensure the connector you are trying to use has been configured correctly and been authorized for use.  #### ConnectorDisabledError  A request has been made to a connector that has since been disabled. This may be temporary - You can contact our team to resolve the issue.  #### ConnectorRateLimitError  You sent too many request to a connector. These rate limits vary from connector to connector. You will need to try again later.  #### RequestLimitError  You have reached the number of requests included in your Free Tier Subscription. You will no be able to make further requests until this limit resets at the end of the month, or talk to us about upgrading your subscription to continue immediately.  #### EntityNotFoundError  You&#39;ve made a request for a resource or route that does not exist. Verify your path parameters or any identifiers used to fetch this resource.  #### OAuthCredentialsNotFoundError  When adding a connector integration that implements OAuth, both a &#x60;client_id&#x60; and &#x60;client_secret&#x60; must be provided before any authorizations can be performed. Verify the integration has been configured properly before continuing.  #### IntegrationNotFoundError  The requested connector integration could not be found associated to your &#x60;application_id&#x60;. Verify your &#x60;application_id&#x60; is correct, and that this connector has been added and configured for your application.  #### ConnectionNotFoundError  A valid connection could not be found associated to your &#x60;application_id&#x60;. Something _may_ have interrupted the authorization flow. You may need to start the connector authorization process again.  #### ConnectionSettingsError  The connector has required settings that were not supplied. Verify &#x60;connection.settings&#x60; contains all required settings for the connector to be callable.  #### ConnectorNotFoundError  A request was made for an unknown connector. Verify your &#x60;service_id&#x60; is spelled correctly, and that this connector is enabled for your provided &#x60;unified_api&#x60;.  #### OAuthRedirectUriError  A request was made either in a connector authorization flow, or attempting to revoke connector access without a valid &#x60;redirect_uri&#x60;. This is the url the user should be returned to on completion of process.  #### OAuthInvalidStateError  The state param is required and is used to ensure the outgoing authorization state has not been altered before the user is redirected back. It also contains required params needed to identify the connector being used. If this has been altered, the authorization will not succeed.  #### OAuthCodeExchangeError  When attempting to exchange the authorization code for an &#x60;access_token&#x60; during an OAuth flow, an error occurred. This may be temporary. You can reattempt authorization or contact our team to resolve the issue.  #### OAuthConnectorError  It seems something went wrong on the connector side. It&#39;s possible this connector is in &#x60;beta&#x60; or still under development. We&#39;ve been notified and are working to fix this issue.  #### MappingError  There was an error attempting to retrieve the mapping for a given attribute. We&#39;ve been notified and are working to fix this issue.  #### ConnectorMappingNotFoundError  It seems the implementation for this connector is incomplete. It&#39;s possible this connector is in &#x60;beta&#x60; or still under development. We&#39;ve been notified and are working to fix this issue.  #### ConnectorResponseMappingNotFoundError  We were unable to retrieve the response mapping for this connector. It&#39;s possible this connector is in &#x60;beta&#x60; or still under development. We&#39;ve been notified and are working to fix this issue.  #### ConnectorOperationMappingNotFoundError  Connector mapping has not been implemented for the requested operation. It&#39;s possible this connector is in &#x60;beta&#x60; or still under development. We&#39;ve been notified and are working to fix this issue.  #### ConnectorWorkflowMappingError  The composite api calls required for this operation have not been mapped entirely. It&#39;s possible this connector is in &#x60;beta&#x60; or still under development. We&#39;ve been notified and are working to fix this issue.  #### ConnectorOperationUnsupportedError  You&#39;re attempting a call that is not supported by the connector. It&#39;s likely this operation is supported by another connector, but we&#39;re unable to implement for this one.  #### PaginationNotSupportedError  Pagination is not yet supported for this connector, try removing limit and/or cursor from the query. It&#39;s possible this connector is in &#x60;beta&#x60; or still under development. We&#39;ve been notified and are working to fix this issue.  ## API Design  ### API Styles and data formats  #### REST API  The API is organized around [REST](https://restfulapi.net/), providing simple and predictable URIs to access and modify objects. Requests support standard HTTP methods like GET, PUT, POST, and DELETE and standard status codes. JSON is returned by all API responses, including errors. In all API requests, you must set the content-type HTTP header to application/json. All API requests must be made over HTTPS. Calls made over HTTP will fail.  ##### Available HTTP methods  The Apideck API uses HTTP verbs to understand if you want to read (GET), delete (DELETE) or create (POST) an object. When your web application cannot do a POST or DELETE, we provide the ability to set the method through the query parameter \\_method.  &#x60;&#x60;&#x60; POST /messages GET /messages GET /messages/{messageId} PATCH /messages/{messageId} DELETE /messages/{messageId} &#x60;&#x60;&#x60;  Response bodies are always UTF-8 encoded JSON objects, unless explicitly documented otherwise. For some endpoints and use cases we divert from REST to provide a better developer experience.  ### Schema  All API requests and response bodies adhere to a common JSON format representing individual items, collections of items, links to related items and additional meta data.  ### Meta  Meta data can be represented as a top level member named “meta”. Any information may be provided in the meta data. It’s most common use is to return the total number of records when requesting a collection of resources.  ### Idempotence (upcoming)  To prevent the creation of duplicate resources, every POST method (such as one that creates a consumer record) must specify a unique value for the X-Unique-Transaction-ID header name. Uniquely identifying each unique POST request ensures that the API processes a given request once and only once.  Uniquely identifying new resource-creation POSTs is especially important when the outcome of a response is ambiguous because of a transient service interruption, such as a server-side timeout or network disruption. If a service interruption occurs, then the client application can safely retry the uniquely identified request without creating duplicate operations. (API endpoints that guarantee that every uniquely identified request is processed only once no matter how many times that uniquely identifiable request is made are described as idempotent.)  ### Request IDs  Each API request has an associated request identifier. You can find this value in the response headers, under Request-Id. You can also find request identifiers in the URLs of individual request logs in your Dashboard. If you need to contact us about a specific request, providing the request identifier will ensure the fastest possible resolution.  ### Fixed field types  #### Dates  The dates returned by the API are all represented in UTC (ISO8601 format).  This example &#x60;2019-11-14T00:55:31.820Z&#x60; is defined by the ISO 8601 standard. The T in the middle separates the year-month-day portion from the hour-minute-second portion. The Z on the end means UTC, that is, an offset-from-UTC of zero hours-minutes-seconds. The Z is pronounced \&quot;Zulu\&quot; per military/aviation tradition.  The ISO 8601 standard is more modern. The formats are wisely designed to be easy to parse by machine as well as easy to read by humans across cultures.  #### Prices and Currencies  All prices returned by the API are represented as integer amounts in a currency’s smallest unit. For example, $5 USD would be returned as 500 (i.e, 500 cents).  For zero-decimal currencies, amounts will still be provided as an integer but without the need to divide by 100. For example, an amount of ¥5 (JPY) would be returned as 5.  All currency codes conform to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217).  ## Support  If you have problems or need help with your case, you can always reach out to our Support.  .<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var AccountingApi = require('index'); // See note below*.
* var xxxSvc = new AccountingApi.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new AccountingApi.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* <em>*NOTE: For a top-level AMD script, use require(['index'], function(){...})
* and put the application logic within the callback function.</em>
* </p>
* <p>
* A non-AMD browser application (discouraged) might do something like this:
* <pre>
* var xxxSvc = new AccountingApi.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new AccountingApi.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 10.0.0
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The AccountingEventType model constructor.
     * @property {module:model/AccountingEventType}
     */
    AccountingEventType,

    /**
     * The AccountingWebhookEvent model constructor.
     * @property {module:model/AccountingWebhookEvent}
     */
    AccountingWebhookEvent,

    /**
     * The Address model constructor.
     * @property {module:model/Address}
     */
    Address,

    /**
     * The BadRequestResponse model constructor.
     * @property {module:model/BadRequestResponse}
     */
    BadRequestResponse,

    /**
     * The BadRequestResponseDetail model constructor.
     * @property {module:model/BadRequestResponseDetail}
     */
    BadRequestResponseDetail,

    /**
     * The BalanceSheet model constructor.
     * @property {module:model/BalanceSheet}
     */
    BalanceSheet,

    /**
     * The BalanceSheetAssets model constructor.
     * @property {module:model/BalanceSheetAssets}
     */
    BalanceSheetAssets,

    /**
     * The BalanceSheetAssetsCurrentAssets model constructor.
     * @property {module:model/BalanceSheetAssetsCurrentAssets}
     */
    BalanceSheetAssetsCurrentAssets,

    /**
     * The BalanceSheetAssetsCurrentAssetsAccountsInner model constructor.
     * @property {module:model/BalanceSheetAssetsCurrentAssetsAccountsInner}
     */
    BalanceSheetAssetsCurrentAssetsAccountsInner,

    /**
     * The BalanceSheetAssetsFixedAssets model constructor.
     * @property {module:model/BalanceSheetAssetsFixedAssets}
     */
    BalanceSheetAssetsFixedAssets,

    /**
     * The BalanceSheetAssetsFixedAssetsAccountsInner model constructor.
     * @property {module:model/BalanceSheetAssetsFixedAssetsAccountsInner}
     */
    BalanceSheetAssetsFixedAssetsAccountsInner,

    /**
     * The BalanceSheetEquity model constructor.
     * @property {module:model/BalanceSheetEquity}
     */
    BalanceSheetEquity,

    /**
     * The BalanceSheetEquityItemsInner model constructor.
     * @property {module:model/BalanceSheetEquityItemsInner}
     */
    BalanceSheetEquityItemsInner,

    /**
     * The BalanceSheetFilter model constructor.
     * @property {module:model/BalanceSheetFilter}
     */
    BalanceSheetFilter,

    /**
     * The BalanceSheetLiabilities model constructor.
     * @property {module:model/BalanceSheetLiabilities}
     */
    BalanceSheetLiabilities,

    /**
     * The BalanceSheetLiabilitiesAccountsInner model constructor.
     * @property {module:model/BalanceSheetLiabilitiesAccountsInner}
     */
    BalanceSheetLiabilitiesAccountsInner,

    /**
     * The BankAccount model constructor.
     * @property {module:model/BankAccount}
     */
    BankAccount,

    /**
     * The Bill model constructor.
     * @property {module:model/Bill}
     */
    Bill,

    /**
     * The BillLineItem model constructor.
     * @property {module:model/BillLineItem}
     */
    BillLineItem,

    /**
     * The BillsSort model constructor.
     * @property {module:model/BillsSort}
     */
    BillsSort,

    /**
     * The CategoriesInner model constructor.
     * @property {module:model/CategoriesInner}
     */
    CategoriesInner,

    /**
     * The Company model constructor.
     * @property {module:model/Company}
     */
    Company,

    /**
     * The CompanyInfo model constructor.
     * @property {module:model/CompanyInfo}
     */
    CompanyInfo,

    /**
     * The CompanyRowType model constructor.
     * @property {module:model/CompanyRowType}
     */
    CompanyRowType,

    /**
     * The Contact model constructor.
     * @property {module:model/Contact}
     */
    Contact,

    /**
     * The CreateBillResponse model constructor.
     * @property {module:model/CreateBillResponse}
     */
    CreateBillResponse,

    /**
     * The CreateCreditNoteResponse model constructor.
     * @property {module:model/CreateCreditNoteResponse}
     */
    CreateCreditNoteResponse,

    /**
     * The CreateCustomerResponse model constructor.
     * @property {module:model/CreateCustomerResponse}
     */
    CreateCustomerResponse,

    /**
     * The CreateInvoiceItemResponse model constructor.
     * @property {module:model/CreateInvoiceItemResponse}
     */
    CreateInvoiceItemResponse,

    /**
     * The CreateInvoiceResponse model constructor.
     * @property {module:model/CreateInvoiceResponse}
     */
    CreateInvoiceResponse,

    /**
     * The CreateJournalEntryResponse model constructor.
     * @property {module:model/CreateJournalEntryResponse}
     */
    CreateJournalEntryResponse,

    /**
     * The CreateLedgerAccountResponse model constructor.
     * @property {module:model/CreateLedgerAccountResponse}
     */
    CreateLedgerAccountResponse,

    /**
     * The CreatePaymentResponse model constructor.
     * @property {module:model/CreatePaymentResponse}
     */
    CreatePaymentResponse,

    /**
     * The CreatePurchaseOrderResponse model constructor.
     * @property {module:model/CreatePurchaseOrderResponse}
     */
    CreatePurchaseOrderResponse,

    /**
     * The CreateSupplierResponse model constructor.
     * @property {module:model/CreateSupplierResponse}
     */
    CreateSupplierResponse,

    /**
     * The CreateTaxRateResponse model constructor.
     * @property {module:model/CreateTaxRateResponse}
     */
    CreateTaxRateResponse,

    /**
     * The CreditNote model constructor.
     * @property {module:model/CreditNote}
     */
    CreditNote,

    /**
     * The CreditNoteAllocationsInner model constructor.
     * @property {module:model/CreditNoteAllocationsInner}
     */
    CreditNoteAllocationsInner,

    /**
     * The Currency model constructor.
     * @property {module:model/Currency}
     */
    Currency,

    /**
     * The CustomField model constructor.
     * @property {module:model/CustomField}
     */
    CustomField,

    /**
     * The CustomFieldValue model constructor.
     * @property {module:model/CustomFieldValue}
     */
    CustomFieldValue,

    /**
     * The Customer model constructor.
     * @property {module:model/Customer}
     */
    Customer,

    /**
     * The CustomersFilter model constructor.
     * @property {module:model/CustomersFilter}
     */
    CustomersFilter,

    /**
     * The DeleteBillResponse model constructor.
     * @property {module:model/DeleteBillResponse}
     */
    DeleteBillResponse,

    /**
     * The DeleteCreditNoteResponse model constructor.
     * @property {module:model/DeleteCreditNoteResponse}
     */
    DeleteCreditNoteResponse,

    /**
     * The DeleteCustomerResponse model constructor.
     * @property {module:model/DeleteCustomerResponse}
     */
    DeleteCustomerResponse,

    /**
     * The DeleteInvoiceResponse model constructor.
     * @property {module:model/DeleteInvoiceResponse}
     */
    DeleteInvoiceResponse,

    /**
     * The DeleteJournalEntryResponse model constructor.
     * @property {module:model/DeleteJournalEntryResponse}
     */
    DeleteJournalEntryResponse,

    /**
     * The DeleteLedgerAccountResponse model constructor.
     * @property {module:model/DeleteLedgerAccountResponse}
     */
    DeleteLedgerAccountResponse,

    /**
     * The DeletePaymentResponse model constructor.
     * @property {module:model/DeletePaymentResponse}
     */
    DeletePaymentResponse,

    /**
     * The DeletePurchaseOrderResponse model constructor.
     * @property {module:model/DeletePurchaseOrderResponse}
     */
    DeletePurchaseOrderResponse,

    /**
     * The DeleteSupplierResponse model constructor.
     * @property {module:model/DeleteSupplierResponse}
     */
    DeleteSupplierResponse,

    /**
     * The DeleteTaxRateResponse model constructor.
     * @property {module:model/DeleteTaxRateResponse}
     */
    DeleteTaxRateResponse,

    /**
     * The Email model constructor.
     * @property {module:model/Email}
     */
    Email,

    /**
     * The GetBalanceSheetResponse model constructor.
     * @property {module:model/GetBalanceSheetResponse}
     */
    GetBalanceSheetResponse,

    /**
     * The GetBillResponse model constructor.
     * @property {module:model/GetBillResponse}
     */
    GetBillResponse,

    /**
     * The GetBillsResponse model constructor.
     * @property {module:model/GetBillsResponse}
     */
    GetBillsResponse,

    /**
     * The GetCompanyInfoResponse model constructor.
     * @property {module:model/GetCompanyInfoResponse}
     */
    GetCompanyInfoResponse,

    /**
     * The GetCreditNoteResponse model constructor.
     * @property {module:model/GetCreditNoteResponse}
     */
    GetCreditNoteResponse,

    /**
     * The GetCreditNotesResponse model constructor.
     * @property {module:model/GetCreditNotesResponse}
     */
    GetCreditNotesResponse,

    /**
     * The GetCustomerResponse model constructor.
     * @property {module:model/GetCustomerResponse}
     */
    GetCustomerResponse,

    /**
     * The GetCustomersResponse model constructor.
     * @property {module:model/GetCustomersResponse}
     */
    GetCustomersResponse,

    /**
     * The GetInvoiceItemResponse model constructor.
     * @property {module:model/GetInvoiceItemResponse}
     */
    GetInvoiceItemResponse,

    /**
     * The GetInvoiceItemsResponse model constructor.
     * @property {module:model/GetInvoiceItemsResponse}
     */
    GetInvoiceItemsResponse,

    /**
     * The GetInvoiceResponse model constructor.
     * @property {module:model/GetInvoiceResponse}
     */
    GetInvoiceResponse,

    /**
     * The GetInvoicesResponse model constructor.
     * @property {module:model/GetInvoicesResponse}
     */
    GetInvoicesResponse,

    /**
     * The GetJournalEntriesResponse model constructor.
     * @property {module:model/GetJournalEntriesResponse}
     */
    GetJournalEntriesResponse,

    /**
     * The GetJournalEntryResponse model constructor.
     * @property {module:model/GetJournalEntryResponse}
     */
    GetJournalEntryResponse,

    /**
     * The GetLedgerAccountResponse model constructor.
     * @property {module:model/GetLedgerAccountResponse}
     */
    GetLedgerAccountResponse,

    /**
     * The GetLedgerAccountsResponse model constructor.
     * @property {module:model/GetLedgerAccountsResponse}
     */
    GetLedgerAccountsResponse,

    /**
     * The GetPaymentResponse model constructor.
     * @property {module:model/GetPaymentResponse}
     */
    GetPaymentResponse,

    /**
     * The GetPaymentsResponse model constructor.
     * @property {module:model/GetPaymentsResponse}
     */
    GetPaymentsResponse,

    /**
     * The GetProfitAndLossResponse model constructor.
     * @property {module:model/GetProfitAndLossResponse}
     */
    GetProfitAndLossResponse,

    /**
     * The GetPurchaseOrderResponse model constructor.
     * @property {module:model/GetPurchaseOrderResponse}
     */
    GetPurchaseOrderResponse,

    /**
     * The GetPurchaseOrdersResponse model constructor.
     * @property {module:model/GetPurchaseOrdersResponse}
     */
    GetPurchaseOrdersResponse,

    /**
     * The GetSupplierResponse model constructor.
     * @property {module:model/GetSupplierResponse}
     */
    GetSupplierResponse,

    /**
     * The GetSuppliersResponse model constructor.
     * @property {module:model/GetSuppliersResponse}
     */
    GetSuppliersResponse,

    /**
     * The GetTaxRateResponse model constructor.
     * @property {module:model/GetTaxRateResponse}
     */
    GetTaxRateResponse,

    /**
     * The GetTaxRatesResponse model constructor.
     * @property {module:model/GetTaxRatesResponse}
     */
    GetTaxRatesResponse,

    /**
     * The Invoice model constructor.
     * @property {module:model/Invoice}
     */
    Invoice,

    /**
     * The InvoiceItem model constructor.
     * @property {module:model/InvoiceItem}
     */
    InvoiceItem,

    /**
     * The InvoiceItemPurchaseDetails model constructor.
     * @property {module:model/InvoiceItemPurchaseDetails}
     */
    InvoiceItemPurchaseDetails,

    /**
     * The InvoiceItemsFilter model constructor.
     * @property {module:model/InvoiceItemsFilter}
     */
    InvoiceItemsFilter,

    /**
     * The InvoiceLineItem model constructor.
     * @property {module:model/InvoiceLineItem}
     */
    InvoiceLineItem,

    /**
     * The InvoiceResponse model constructor.
     * @property {module:model/InvoiceResponse}
     */
    InvoiceResponse,

    /**
     * The InvoicesSort model constructor.
     * @property {module:model/InvoicesSort}
     */
    InvoicesSort,

    /**
     * The JournalEntry model constructor.
     * @property {module:model/JournalEntry}
     */
    JournalEntry,

    /**
     * The JournalEntryLineItem model constructor.
     * @property {module:model/JournalEntryLineItem}
     */
    JournalEntryLineItem,

    /**
     * The LedgerAccount model constructor.
     * @property {module:model/LedgerAccount}
     */
    LedgerAccount,

    /**
     * The LedgerAccountParentAccount model constructor.
     * @property {module:model/LedgerAccountParentAccount}
     */
    LedgerAccountParentAccount,

    /**
     * The LinkedCustomer model constructor.
     * @property {module:model/LinkedCustomer}
     */
    LinkedCustomer,

    /**
     * The LinkedInvoiceItem model constructor.
     * @property {module:model/LinkedInvoiceItem}
     */
    LinkedInvoiceItem,

    /**
     * The LinkedLedgerAccount model constructor.
     * @property {module:model/LinkedLedgerAccount}
     */
    LinkedLedgerAccount,

    /**
     * The LinkedParentCustomer model constructor.
     * @property {module:model/LinkedParentCustomer}
     */
    LinkedParentCustomer,

    /**
     * The LinkedSupplier model constructor.
     * @property {module:model/LinkedSupplier}
     */
    LinkedSupplier,

    /**
     * The LinkedTaxRate model constructor.
     * @property {module:model/LinkedTaxRate}
     */
    LinkedTaxRate,

    /**
     * The LinkedTrackingCategory model constructor.
     * @property {module:model/LinkedTrackingCategory}
     */
    LinkedTrackingCategory,

    /**
     * The Links model constructor.
     * @property {module:model/Links}
     */
    Links,

    /**
     * The Meta model constructor.
     * @property {module:model/Meta}
     */
    Meta,

    /**
     * The MetaCursors model constructor.
     * @property {module:model/MetaCursors}
     */
    MetaCursors,

    /**
     * The NotFoundResponse model constructor.
     * @property {module:model/NotFoundResponse}
     */
    NotFoundResponse,

    /**
     * The NotFoundResponseDetail model constructor.
     * @property {module:model/NotFoundResponseDetail}
     */
    NotFoundResponseDetail,

    /**
     * The NotImplementedResponse model constructor.
     * @property {module:model/NotImplementedResponse}
     */
    NotImplementedResponse,

    /**
     * The NotImplementedResponseDetail model constructor.
     * @property {module:model/NotImplementedResponseDetail}
     */
    NotImplementedResponseDetail,

    /**
     * The PassThroughQuery model constructor.
     * @property {module:model/PassThroughQuery}
     */
    PassThroughQuery,

    /**
     * The Payment model constructor.
     * @property {module:model/Payment}
     */
    Payment,

    /**
     * The PaymentAllocationsInner model constructor.
     * @property {module:model/PaymentAllocationsInner}
     */
    PaymentAllocationsInner,

    /**
     * The PaymentRequiredResponse model constructor.
     * @property {module:model/PaymentRequiredResponse}
     */
    PaymentRequiredResponse,

    /**
     * The PaymentsFilter model constructor.
     * @property {module:model/PaymentsFilter}
     */
    PaymentsFilter,

    /**
     * The PhoneNumber model constructor.
     * @property {module:model/PhoneNumber}
     */
    PhoneNumber,

    /**
     * The ProfitAndLoss model constructor.
     * @property {module:model/ProfitAndLoss}
     */
    ProfitAndLoss,

    /**
     * The ProfitAndLossExpenses model constructor.
     * @property {module:model/ProfitAndLossExpenses}
     */
    ProfitAndLossExpenses,

    /**
     * The ProfitAndLossFilter model constructor.
     * @property {module:model/ProfitAndLossFilter}
     */
    ProfitAndLossFilter,

    /**
     * The ProfitAndLossGrossProfit model constructor.
     * @property {module:model/ProfitAndLossGrossProfit}
     */
    ProfitAndLossGrossProfit,

    /**
     * The ProfitAndLossIncome model constructor.
     * @property {module:model/ProfitAndLossIncome}
     */
    ProfitAndLossIncome,

    /**
     * The ProfitAndLossNetIncome model constructor.
     * @property {module:model/ProfitAndLossNetIncome}
     */
    ProfitAndLossNetIncome,

    /**
     * The ProfitAndLossNetOperatingIncome model constructor.
     * @property {module:model/ProfitAndLossNetOperatingIncome}
     */
    ProfitAndLossNetOperatingIncome,

    /**
     * The ProfitAndLossRecord model constructor.
     * @property {module:model/ProfitAndLossRecord}
     */
    ProfitAndLossRecord,

    /**
     * The ProfitAndLossRecordsInner model constructor.
     * @property {module:model/ProfitAndLossRecordsInner}
     */
    ProfitAndLossRecordsInner,

    /**
     * The ProfitAndLossSection model constructor.
     * @property {module:model/ProfitAndLossSection}
     */
    ProfitAndLossSection,

    /**
     * The PurchaseOrder model constructor.
     * @property {module:model/PurchaseOrder}
     */
    PurchaseOrder,

    /**
     * The SocialLink model constructor.
     * @property {module:model/SocialLink}
     */
    SocialLink,

    /**
     * The SortDirection model constructor.
     * @property {module:model/SortDirection}
     */
    SortDirection,

    /**
     * The SubAccountsInner model constructor.
     * @property {module:model/SubAccountsInner}
     */
    SubAccountsInner,

    /**
     * The Supplier model constructor.
     * @property {module:model/Supplier}
     */
    Supplier,

    /**
     * The SuppliersFilter model constructor.
     * @property {module:model/SuppliersFilter}
     */
    SuppliersFilter,

    /**
     * The TaxComponentsInner model constructor.
     * @property {module:model/TaxComponentsInner}
     */
    TaxComponentsInner,

    /**
     * The TaxRate model constructor.
     * @property {module:model/TaxRate}
     */
    TaxRate,

    /**
     * The TaxRatesFilter model constructor.
     * @property {module:model/TaxRatesFilter}
     */
    TaxRatesFilter,

    /**
     * The TooManyRequestsResponse model constructor.
     * @property {module:model/TooManyRequestsResponse}
     */
    TooManyRequestsResponse,

    /**
     * The TooManyRequestsResponseDetail model constructor.
     * @property {module:model/TooManyRequestsResponseDetail}
     */
    TooManyRequestsResponseDetail,

    /**
     * The UnauthorizedResponse model constructor.
     * @property {module:model/UnauthorizedResponse}
     */
    UnauthorizedResponse,

    /**
     * The UnexpectedErrorResponse model constructor.
     * @property {module:model/UnexpectedErrorResponse}
     */
    UnexpectedErrorResponse,

    /**
     * The UnexpectedErrorResponseDetail model constructor.
     * @property {module:model/UnexpectedErrorResponseDetail}
     */
    UnexpectedErrorResponseDetail,

    /**
     * The UnifiedId model constructor.
     * @property {module:model/UnifiedId}
     */
    UnifiedId,

    /**
     * The UnprocessableResponse model constructor.
     * @property {module:model/UnprocessableResponse}
     */
    UnprocessableResponse,

    /**
     * The UpdateBillResponse model constructor.
     * @property {module:model/UpdateBillResponse}
     */
    UpdateBillResponse,

    /**
     * The UpdateCreditNoteResponse model constructor.
     * @property {module:model/UpdateCreditNoteResponse}
     */
    UpdateCreditNoteResponse,

    /**
     * The UpdateCustomerResponse model constructor.
     * @property {module:model/UpdateCustomerResponse}
     */
    UpdateCustomerResponse,

    /**
     * The UpdateInvoiceItemsResponse model constructor.
     * @property {module:model/UpdateInvoiceItemsResponse}
     */
    UpdateInvoiceItemsResponse,

    /**
     * The UpdateInvoiceResponse model constructor.
     * @property {module:model/UpdateInvoiceResponse}
     */
    UpdateInvoiceResponse,

    /**
     * The UpdateJournalEntryResponse model constructor.
     * @property {module:model/UpdateJournalEntryResponse}
     */
    UpdateJournalEntryResponse,

    /**
     * The UpdateLedgerAccountResponse model constructor.
     * @property {module:model/UpdateLedgerAccountResponse}
     */
    UpdateLedgerAccountResponse,

    /**
     * The UpdatePaymentResponse model constructor.
     * @property {module:model/UpdatePaymentResponse}
     */
    UpdatePaymentResponse,

    /**
     * The UpdatePurchaseOrderResponse model constructor.
     * @property {module:model/UpdatePurchaseOrderResponse}
     */
    UpdatePurchaseOrderResponse,

    /**
     * The UpdateSupplierResponse model constructor.
     * @property {module:model/UpdateSupplierResponse}
     */
    UpdateSupplierResponse,

    /**
     * The UpdateTaxRateResponse model constructor.
     * @property {module:model/UpdateTaxRateResponse}
     */
    UpdateTaxRateResponse,

    /**
     * The Website model constructor.
     * @property {module:model/Website}
     */
    Website,

    /**
    * The BalanceSheetApi service constructor.
    * @property {module:api/BalanceSheetApi}
    */
    BalanceSheetApi,

    /**
    * The BillsApi service constructor.
    * @property {module:api/BillsApi}
    */
    BillsApi,

    /**
    * The CompanyInfoApi service constructor.
    * @property {module:api/CompanyInfoApi}
    */
    CompanyInfoApi,

    /**
    * The CreditNotesApi service constructor.
    * @property {module:api/CreditNotesApi}
    */
    CreditNotesApi,

    /**
    * The CustomersApi service constructor.
    * @property {module:api/CustomersApi}
    */
    CustomersApi,

    /**
    * The InvoiceItemsApi service constructor.
    * @property {module:api/InvoiceItemsApi}
    */
    InvoiceItemsApi,

    /**
    * The InvoicesApi service constructor.
    * @property {module:api/InvoicesApi}
    */
    InvoicesApi,

    /**
    * The JournalEntriesApi service constructor.
    * @property {module:api/JournalEntriesApi}
    */
    JournalEntriesApi,

    /**
    * The LedgerAccountsApi service constructor.
    * @property {module:api/LedgerAccountsApi}
    */
    LedgerAccountsApi,

    /**
    * The PaymentsApi service constructor.
    * @property {module:api/PaymentsApi}
    */
    PaymentsApi,

    /**
    * The ProfitAndLossApi service constructor.
    * @property {module:api/ProfitAndLossApi}
    */
    ProfitAndLossApi,

    /**
    * The PurchaseOrdersApi service constructor.
    * @property {module:api/PurchaseOrdersApi}
    */
    PurchaseOrdersApi,

    /**
    * The SuppliersApi service constructor.
    * @property {module:api/SuppliersApi}
    */
    SuppliersApi,

    /**
    * The TaxRatesApi service constructor.
    * @property {module:api/TaxRatesApi}
    */
    TaxRatesApi
};
