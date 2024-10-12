/**
 * HRIS API
 * Welcome to the HRIS API.  You can use this API to access all HRIS API endpoints.  ## Base URL  The base URL for all API requests is `https://unify.apideck.com`  ## Headers  Custom headers that are expected as part of the request. Note that [RFC7230](https://tools.ietf.org/html/rfc7230) states header names are case insensitive.  | Name                  | Type    | Required | Description                                                                                                                                                    | | --------------------- | ------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | | x-apideck-consumer-id | String  | Yes      | The id of the customer stored inside Apideck Vault. This can be a user id, account id, device id or whatever entity that can have integration within your app. | | x-apideck-service-id  | String  | No       | Describe the service you want to call (e.g., pipedrive). Only needed when a customer has activated multiple integrations for the same Unified API.             | | x-apideck-raw         | Boolean | No       | Include raw response. Mostly used for debugging purposes.                                                                                                      | | x-apideck-app-id      | String  | Yes      | The application id of your Unify application. Available at https://app.apideck.com/unify/api-keys.                                                             | | Authorization         | String  | Yes      | Bearer API KEY                                                                                                                                                 |  ## Authorization  You can interact with the API through the authorization methods below.  <!-- ReDoc-Inject: <security-definitions> -->  ## Pagination  All API resources have support for bulk retrieval via list APIs.  Apideck uses cursor-based pagination via the optional `cursor` and `limit` parameters.  To fetch the first page of results, call the list API without a `cursor` parameter. Afterwards you can fetch subsequent pages by providing a cursor parameter. You will find the next cursor in the response body in `meta.cursors.next`. If `meta.cursors.next` is `null` you're at the end of the list.  In the REST API you can also use the `links` from the response for added convenience. Simply call the URL in `links.next` to get the next page of results.  ### Query Parameters  | Name   | Type   | Required | Description                                                                                                        | | ------ | ------ | -------- | ------------------------------------------------------------------------------------------------------------------ | | cursor | String | No       | Cursor to start from. You can find cursors for next & previous pages in the meta.cursors property of the response. | | limit  | Number | No       | Number of results to return. Minimum 1, Maximum 200, Default 20                                                    |  ### Response Body  | Name                  | Type   | Description                                                        | | --------------------- | ------ | ------------------------------------------------------------------ | | meta.cursors.previous | String | Cursor to navigate to the previous page of results through the API | | meta.cursors.current  | String | Cursor to navigate to the current page of results through the API  | | meta.cursors.next     | String | Cursor to navigate to the next page of results through the API     | | meta.items_on_page    | Number | Number of items returned in the data property of the response      | | links.previous        | String | Link to navigate to the previous page of results through the API   | | links.current         | String | Link to navigate to the current page of results through the API    | | links.next            | String | Link to navigate to the next page of results through the API       |  ⚠️ `meta.cursors.previous`/`links.previous` is not available for all connectors.  ## SDKs and API Clients  We currently offer a [Node.js](https://developers.apideck.com/sdks/node), [PHP](https://developers.apideck.com/sdks/php) and [.NET](https://developers.apideck.com/sdks/dot-net) SDK. Need another SDK? [Request the SDK of your choice](https://integrations.apideck.com/request).  ## Debugging  Because of the nature of the abstraction we do in Apideck Unify we still provide the option to the receive raw requests and responses being handled underlying. By including the raw flag `?raw=true` in your requests you can still receive the full request. Please note that this increases the response size and can introduce extra latency.  ## Errors  The API returns standard HTTP response codes to indicate success or failure of the API requests. For errors, we also return a customized error message inside the JSON response. You can see the returned HTTP status codes below.  | Code | Title                | Description                                                                                                                                                                                              | | ---- | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | | 200  | OK                   | The request message has been successfully processed, and it has produced a response. The response message varies, depending on the request method and the requested data.                                | | 201  | Created              | The request has been fulfilled and has resulted in one or more new resources being created.                                                                                                              | | 204  | No Content           | The server has successfully fulfilled the request and that there is no additional content to send in the response payload body.                                                                          | | 400  | Bad Request          | The receiving server cannot understand the request because of malformed syntax. Do not repeat the request without first modifying it; check the request for errors, fix them and then retry the request. | | 401  | Unauthorized         | The request has not been applied because it lacks valid authentication credentials for the target resource.                                                                                              | | 402  | Payment Required     | Subscription data is incomplete or out of date. You'll need to provide payment details to continue.                                                                                                      | | 403  | Forbidden            | You do not have the appropriate user rights to access the request. Do not repeat the request.                                                                                                            | | 404  | Not Found            | The origin server did not find a current representation for the target resource or is not willing to disclose that one exists.                                                                           | | 409  | Conflict             | The request could not be completed due to a conflict with the current state of the target resource.                                                                                                      | | 422  | Unprocessable Entity | The server understands the content type of the request entity, and the syntax of the request entity is correct but was unable to process the contained instructions.                                     | | 429  | Too Many Requests    | You sent too many requests in a given amount of time (\"rate limit\"). Try again later                                                                                                                     | | 5xx  | Server Errors        | Something went wrong with the Unify API. These errors are logged on our side. You can contact our team to resolve the issue.                                                                             |  ### Handling errors  The Unify API and SDKs can produce errors for many reasons, such as a failed requests due to misconfigured integrations, invalid parameters, authentication errors, and network unavailability.  ### Error Types  #### RequestValidationError  Request is not valid for the current endpoint. The response body will include details on the validation error. Check the spelling and types of your attributes, and ensure you are not passing data that is outside of the specification.  #### UnsupportedFiltersError  Filters in the request are valid, but not supported by the connector. Remove the unsupported filter(s) to get a successful response.  #### UnsupportedSortFieldError  Sort field (`sort[by]`) in the request is valid, but not supported by the connector. Replace or remove the sort field to get a successful response.  #### InvalidCursorError  Pagination cursor in the request is not valid for the current connector. Make sure to use a cursor returned from the API, for the same connector.  #### ConnectorExecutionError  A Unified API request made via one of our downstream connectors returned an unexpected error. The `status_code` returned is proxied through to error response along with their original response via the error detail.  #### UnauthorizedError  We were unable to authorize the request as made. This can happen for a number of reasons, from missing header params to passing an incorrect authorization token. Verify your Api Key is being set correctly in the authorization header. ie: `Authorization: 'Bearer sk_live_***'`  #### ConnectorCredentialsError  A request using a given connector has not been authorized. Ensure the connector you are trying to use has been configured correctly and been authorized for use.  #### ConnectorDisabledError  A request has been made to a connector that has since been disabled. This may be temporary - You can contact our team to resolve the issue.  #### ConnectorRateLimitError  You sent too many request to a connector. These rate limits vary from connector to connector. You will need to try again later.  #### RequestLimitError  You have reached the number of requests included in your Free Tier Subscription. You will no be able to make further requests until this limit resets at the end of the month, or talk to us about upgrading your subscription to continue immediately.  #### EntityNotFoundError  You've made a request for a resource or route that does not exist. Verify your path parameters or any identifiers used to fetch this resource.  #### OAuthCredentialsNotFoundError  When adding a connector integration that implements OAuth, both a `client_id` and `client_secret` must be provided before any authorizations can be performed. Verify the integration has been configured properly before continuing.  #### IntegrationNotFoundError  The requested connector integration could not be found associated to your `application_id`. Verify your `application_id` is correct, and that this connector has been added and configured for your application.  #### ConnectionNotFoundError  A valid connection could not be found associated to your `application_id`. Something _may_ have interrupted the authorization flow. You may need to start the connector authorization process again.  #### ConnectionSettingsError  The connector has required settings that were not supplied. Verify `connection.settings` contains all required settings for the connector to be callable.  #### ConnectorNotFoundError  A request was made for an unknown connector. Verify your `service_id` is spelled correctly, and that this connector is enabled for your provided `unified_api`.  #### OAuthRedirectUriError  A request was made either in a connector authorization flow, or attempting to revoke connector access without a valid `redirect_uri`. This is the url the user should be returned to on completion of process.  #### OAuthInvalidStateError  The state param is required and is used to ensure the outgoing authorization state has not been altered before the user is redirected back. It also contains required params needed to identify the connector being used. If this has been altered, the authorization will not succeed.  #### OAuthCodeExchangeError  When attempting to exchange the authorization code for an `access_token` during an OAuth flow, an error occurred. This may be temporary. You can reattempt authorization or contact our team to resolve the issue.  #### OAuthConnectorError  It seems something went wrong on the connector side. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### MappingError  There was an error attempting to retrieve the mapping for a given attribute. We've been notified and are working to fix this issue.  #### ConnectorMappingNotFoundError  It seems the implementation for this connector is incomplete. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorResponseMappingNotFoundError  We were unable to retrieve the response mapping for this connector. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorOperationMappingNotFoundError  Connector mapping has not been implemented for the requested operation. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorWorkflowMappingError  The composite api calls required for this operation have not been mapped entirely. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorOperationUnsupportedError  You're attempting a call that is not supported by the connector. It's likely this operation is supported by another connector, but we're unable to implement for this one.  #### PaginationNotSupportedError  Pagination is not yet supported for this connector, try removing limit and/or cursor from the query. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  ## API Design  ### API Styles and data formats  #### REST API  The API is organized around [REST](https://restfulapi.net/), providing simple and predictable URIs to access and modify objects. Requests support standard HTTP methods like GET, PUT, POST, and DELETE and standard status codes. JSON is returned by all API responses, including errors. In all API requests, you must set the content-type HTTP header to application/json. All API requests must be made over HTTPS. Calls made over HTTP will fail.  ##### Available HTTP methods  The Apideck API uses HTTP verbs to understand if you want to read (GET), delete (DELETE) or create (POST) an object. When your web application cannot do a POST or DELETE, we provide the ability to set the method through the query parameter \\_method.  ``` POST /messages GET /messages GET /messages/{messageId} PATCH /messages/{messageId} DELETE /messages/{messageId} ```  Response bodies are always UTF-8 encoded JSON objects, unless explicitly documented otherwise. For some endpoints and use cases we divert from REST to provide a better developer experience.  ### Schema  All API requests and response bodies adhere to a common JSON format representing individual items, collections of items, links to related items and additional meta data.  ### Meta  Meta data can be represented as a top level member named “meta”. Any information may be provided in the meta data. It’s most common use is to return the total number of records when requesting a collection of resources.  ### Idempotence (upcoming)  To prevent the creation of duplicate resources, every POST method (such as one that creates a consumer record) must specify a unique value for the X-Unique-Transaction-ID header name. Uniquely identifying each unique POST request ensures that the API processes a given request once and only once.  Uniquely identifying new resource-creation POSTs is especially important when the outcome of a response is ambiguous because of a transient service interruption, such as a server-side timeout or network disruption. If a service interruption occurs, then the client application can safely retry the uniquely identified request without creating duplicate operations. (API endpoints that guarantee that every uniquely identified request is processed only once no matter how many times that uniquely identifiable request is made are described as idempotent.)  ### Request IDs  Each API request has an associated request identifier. You can find this value in the response headers, under Request-Id. You can also find request identifiers in the URLs of individual request logs in your Dashboard. If you need to contact us about a specific request, providing the request identifier will ensure the fastest possible resolution.  ### Fixed field types  #### Dates  The dates returned by the API are all represented in UTC (ISO8601 format).  This example `2019-11-14T00:55:31.820Z` is defined by the ISO 8601 standard. The T in the middle separates the year-month-day portion from the hour-minute-second portion. The Z on the end means UTC, that is, an offset-from-UTC of zero hours-minutes-seconds. The Z is pronounced \"Zulu\" per military/aviation tradition.  The ISO 8601 standard is more modern. The formats are wisely designed to be easy to parse by machine as well as easy to read by humans across cultures.  #### Prices and Currencies  All prices returned by the API are represented as integer amounts in a currency’s smallest unit. For example, $5 USD would be returned as 500 (i.e, 500 cents).  For zero-decimal currencies, amounts will still be provided as an integer but without the need to divide by 100. For example, an amount of ¥5 (JPY) would be returned as 5.  All currency codes conform to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217).  ## Support  If you have problems or need help with your case, you can always reach out to our Support.  
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
import Address from './model/Address';
import BadRequestResponse from './model/BadRequestResponse';
import BadRequestResponseDetail from './model/BadRequestResponseDetail';
import BankAccount from './model/BankAccount';
import Benefit from './model/Benefit';
import Compensation from './model/Compensation';
import CreateDepartmentResponse from './model/CreateDepartmentResponse';
import CreateEmployeeResponse from './model/CreateEmployeeResponse';
import CreateHrisCompanyResponse from './model/CreateHrisCompanyResponse';
import CreateTimeOffRequestResponse from './model/CreateTimeOffRequestResponse';
import Currency from './model/Currency';
import CustomField from './model/CustomField';
import CustomFieldValue from './model/CustomFieldValue';
import Deduction from './model/Deduction';
import DeleteDepartmentResponse from './model/DeleteDepartmentResponse';
import DeleteEmployeeResponse from './model/DeleteEmployeeResponse';
import DeleteHrisCompanyResponse from './model/DeleteHrisCompanyResponse';
import DeleteTimeOffRequestResponse from './model/DeleteTimeOffRequestResponse';
import Department from './model/Department';
import Email from './model/Email';
import Employee from './model/Employee';
import EmployeeCompensation from './model/EmployeeCompensation';
import EmployeeEmploymentRole from './model/EmployeeEmploymentRole';
import EmployeeJob from './model/EmployeeJob';
import EmployeeList from './model/EmployeeList';
import EmployeeManager from './model/EmployeeManager';
import EmployeePayroll from './model/EmployeePayroll';
import EmployeeSchedules from './model/EmployeeSchedules';
import EmployeesFilter from './model/EmployeesFilter';
import EmployeesSort from './model/EmployeesSort';
import EmploymentStatus from './model/EmploymentStatus';
import Gender from './model/Gender';
import GetDepartmentResponse from './model/GetDepartmentResponse';
import GetDepartmentsResponse from './model/GetDepartmentsResponse';
import GetEmployeePayrollResponse from './model/GetEmployeePayrollResponse';
import GetEmployeePayrollsResponse from './model/GetEmployeePayrollsResponse';
import GetEmployeeResponse from './model/GetEmployeeResponse';
import GetEmployeeSchedulesResponse from './model/GetEmployeeSchedulesResponse';
import GetEmployeesResponse from './model/GetEmployeesResponse';
import GetHrisCompaniesResponse from './model/GetHrisCompaniesResponse';
import GetHrisCompanyResponse from './model/GetHrisCompanyResponse';
import GetHrisJobResponse from './model/GetHrisJobResponse';
import GetHrisJobsResponse from './model/GetHrisJobsResponse';
import GetPayrollResponse from './model/GetPayrollResponse';
import GetPayrollsResponse from './model/GetPayrollsResponse';
import GetTimeOffRequestResponse from './model/GetTimeOffRequestResponse';
import GetTimeOffRequestsResponse from './model/GetTimeOffRequestsResponse';
import HrisCompany from './model/HrisCompany';
import HrisEventType from './model/HrisEventType';
import HrisJob from './model/HrisJob';
import HrisJobLocation from './model/HrisJobLocation';
import HrisJobs from './model/HrisJobs';
import HrisWebhookEvent from './model/HrisWebhookEvent';
import Links from './model/Links';
import Meta from './model/Meta';
import MetaCursors from './model/MetaCursors';
import NotFoundResponse from './model/NotFoundResponse';
import NotFoundResponseDetail from './model/NotFoundResponseDetail';
import NotImplementedResponse from './model/NotImplementedResponse';
import NotImplementedResponseDetail from './model/NotImplementedResponseDetail';
import PassThroughQuery from './model/PassThroughQuery';
import PaymentFrequency from './model/PaymentFrequency';
import PaymentRequiredResponse from './model/PaymentRequiredResponse';
import PaymentUnit from './model/PaymentUnit';
import Payroll from './model/Payroll';
import PayrollTotals from './model/PayrollTotals';
import PayrollsFilter from './model/PayrollsFilter';
import Person from './model/Person';
import PhoneNumber from './model/PhoneNumber';
import ProbationPeriod from './model/ProbationPeriod';
import Schedule from './model/Schedule';
import ScheduleWorkPattern from './model/ScheduleWorkPattern';
import ScheduleWorkPatternEvenWeeks from './model/ScheduleWorkPatternEvenWeeks';
import SocialLink from './model/SocialLink';
import SortDirection from './model/SortDirection';
import Tax from './model/Tax';
import Team from './model/Team';
import TimeOffRequest from './model/TimeOffRequest';
import TimeOffRequestNotes from './model/TimeOffRequestNotes';
import TimeOffRequestsFilter from './model/TimeOffRequestsFilter';
import TooManyRequestsResponse from './model/TooManyRequestsResponse';
import TooManyRequestsResponseDetail from './model/TooManyRequestsResponseDetail';
import UnauthorizedResponse from './model/UnauthorizedResponse';
import UnexpectedErrorResponse from './model/UnexpectedErrorResponse';
import UnexpectedErrorResponseDetail from './model/UnexpectedErrorResponseDetail';
import UnifiedId from './model/UnifiedId';
import UnprocessableResponse from './model/UnprocessableResponse';
import UpdateDepartmentResponse from './model/UpdateDepartmentResponse';
import UpdateEmployeeResponse from './model/UpdateEmployeeResponse';
import UpdateHrisCompanyResponse from './model/UpdateHrisCompanyResponse';
import UpdateTimeOffRequestResponse from './model/UpdateTimeOffRequestResponse';
import WebhookEvent from './model/WebhookEvent';
import Website from './model/Website';
import CompaniesApi from './api/CompaniesApi';
import DepartmentsApi from './api/DepartmentsApi';
import EmployeePayrollsApi from './api/EmployeePayrollsApi';
import EmployeeSchedulesApi from './api/EmployeeSchedulesApi';
import EmployeesApi from './api/EmployeesApi';
import PayrollsApi from './api/PayrollsApi';
import TimeOffRequestsApi from './api/TimeOffRequestsApi';


/**
* Welcome to the HRIS API.  You can use this API to access all HRIS API endpoints.  ## Base URL  The base URL for all API requests is &#x60;https://unify.apideck.com&#x60;  ## Headers  Custom headers that are expected as part of the request. Note that [RFC7230](https://tools.ietf.org/html/rfc7230) states header names are case insensitive.  | Name                  | Type    | Required | Description                                                                                                                                                    | | --------------------- | ------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | | x-apideck-consumer-id | String  | Yes      | The id of the customer stored inside Apideck Vault. This can be a user id, account id, device id or whatever entity that can have integration within your app. | | x-apideck-service-id  | String  | No       | Describe the service you want to call (e.g., pipedrive). Only needed when a customer has activated multiple integrations for the same Unified API.             | | x-apideck-raw         | Boolean | No       | Include raw response. Mostly used for debugging purposes.                                                                                                      | | x-apideck-app-id      | String  | Yes      | The application id of your Unify application. Available at https://app.apideck.com/unify/api-keys.                                                             | | Authorization         | String  | Yes      | Bearer API KEY                                                                                                                                                 |  ## Authorization  You can interact with the API through the authorization methods below.  &lt;!-- ReDoc-Inject: &lt;security-definitions&gt; --&gt;  ## Pagination  All API resources have support for bulk retrieval via list APIs.  Apideck uses cursor-based pagination via the optional &#x60;cursor&#x60; and &#x60;limit&#x60; parameters.  To fetch the first page of results, call the list API without a &#x60;cursor&#x60; parameter. Afterwards you can fetch subsequent pages by providing a cursor parameter. You will find the next cursor in the response body in &#x60;meta.cursors.next&#x60;. If &#x60;meta.cursors.next&#x60; is &#x60;null&#x60; you&#39;re at the end of the list.  In the REST API you can also use the &#x60;links&#x60; from the response for added convenience. Simply call the URL in &#x60;links.next&#x60; to get the next page of results.  ### Query Parameters  | Name   | Type   | Required | Description                                                                                                        | | ------ | ------ | -------- | ------------------------------------------------------------------------------------------------------------------ | | cursor | String | No       | Cursor to start from. You can find cursors for next &amp; previous pages in the meta.cursors property of the response. | | limit  | Number | No       | Number of results to return. Minimum 1, Maximum 200, Default 20                                                    |  ### Response Body  | Name                  | Type   | Description                                                        | | --------------------- | ------ | ------------------------------------------------------------------ | | meta.cursors.previous | String | Cursor to navigate to the previous page of results through the API | | meta.cursors.current  | String | Cursor to navigate to the current page of results through the API  | | meta.cursors.next     | String | Cursor to navigate to the next page of results through the API     | | meta.items_on_page    | Number | Number of items returned in the data property of the response      | | links.previous        | String | Link to navigate to the previous page of results through the API   | | links.current         | String | Link to navigate to the current page of results through the API    | | links.next            | String | Link to navigate to the next page of results through the API       |  ⚠️ &#x60;meta.cursors.previous&#x60;/&#x60;links.previous&#x60; is not available for all connectors.  ## SDKs and API Clients  We currently offer a [Node.js](https://developers.apideck.com/sdks/node), [PHP](https://developers.apideck.com/sdks/php) and [.NET](https://developers.apideck.com/sdks/dot-net) SDK. Need another SDK? [Request the SDK of your choice](https://integrations.apideck.com/request).  ## Debugging  Because of the nature of the abstraction we do in Apideck Unify we still provide the option to the receive raw requests and responses being handled underlying. By including the raw flag &#x60;?raw&#x3D;true&#x60; in your requests you can still receive the full request. Please note that this increases the response size and can introduce extra latency.  ## Errors  The API returns standard HTTP response codes to indicate success or failure of the API requests. For errors, we also return a customized error message inside the JSON response. You can see the returned HTTP status codes below.  | Code | Title                | Description                                                                                                                                                                                              | | ---- | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | | 200  | OK                   | The request message has been successfully processed, and it has produced a response. The response message varies, depending on the request method and the requested data.                                | | 201  | Created              | The request has been fulfilled and has resulted in one or more new resources being created.                                                                                                              | | 204  | No Content           | The server has successfully fulfilled the request and that there is no additional content to send in the response payload body.                                                                          | | 400  | Bad Request          | The receiving server cannot understand the request because of malformed syntax. Do not repeat the request without first modifying it; check the request for errors, fix them and then retry the request. | | 401  | Unauthorized         | The request has not been applied because it lacks valid authentication credentials for the target resource.                                                                                              | | 402  | Payment Required     | Subscription data is incomplete or out of date. You&#39;ll need to provide payment details to continue.                                                                                                      | | 403  | Forbidden            | You do not have the appropriate user rights to access the request. Do not repeat the request.                                                                                                            | | 404  | Not Found            | The origin server did not find a current representation for the target resource or is not willing to disclose that one exists.                                                                           | | 409  | Conflict             | The request could not be completed due to a conflict with the current state of the target resource.                                                                                                      | | 422  | Unprocessable Entity | The server understands the content type of the request entity, and the syntax of the request entity is correct but was unable to process the contained instructions.                                     | | 429  | Too Many Requests    | You sent too many requests in a given amount of time (\&quot;rate limit\&quot;). Try again later                                                                                                                     | | 5xx  | Server Errors        | Something went wrong with the Unify API. These errors are logged on our side. You can contact our team to resolve the issue.                                                                             |  ### Handling errors  The Unify API and SDKs can produce errors for many reasons, such as a failed requests due to misconfigured integrations, invalid parameters, authentication errors, and network unavailability.  ### Error Types  #### RequestValidationError  Request is not valid for the current endpoint. The response body will include details on the validation error. Check the spelling and types of your attributes, and ensure you are not passing data that is outside of the specification.  #### UnsupportedFiltersError  Filters in the request are valid, but not supported by the connector. Remove the unsupported filter(s) to get a successful response.  #### UnsupportedSortFieldError  Sort field (&#x60;sort[by]&#x60;) in the request is valid, but not supported by the connector. Replace or remove the sort field to get a successful response.  #### InvalidCursorError  Pagination cursor in the request is not valid for the current connector. Make sure to use a cursor returned from the API, for the same connector.  #### ConnectorExecutionError  A Unified API request made via one of our downstream connectors returned an unexpected error. The &#x60;status_code&#x60; returned is proxied through to error response along with their original response via the error detail.  #### UnauthorizedError  We were unable to authorize the request as made. This can happen for a number of reasons, from missing header params to passing an incorrect authorization token. Verify your Api Key is being set correctly in the authorization header. ie: &#x60;Authorization: &#39;Bearer sk_live_***&#39;&#x60;  #### ConnectorCredentialsError  A request using a given connector has not been authorized. Ensure the connector you are trying to use has been configured correctly and been authorized for use.  #### ConnectorDisabledError  A request has been made to a connector that has since been disabled. This may be temporary - You can contact our team to resolve the issue.  #### ConnectorRateLimitError  You sent too many request to a connector. These rate limits vary from connector to connector. You will need to try again later.  #### RequestLimitError  You have reached the number of requests included in your Free Tier Subscription. You will no be able to make further requests until this limit resets at the end of the month, or talk to us about upgrading your subscription to continue immediately.  #### EntityNotFoundError  You&#39;ve made a request for a resource or route that does not exist. Verify your path parameters or any identifiers used to fetch this resource.  #### OAuthCredentialsNotFoundError  When adding a connector integration that implements OAuth, both a &#x60;client_id&#x60; and &#x60;client_secret&#x60; must be provided before any authorizations can be performed. Verify the integration has been configured properly before continuing.  #### IntegrationNotFoundError  The requested connector integration could not be found associated to your &#x60;application_id&#x60;. Verify your &#x60;application_id&#x60; is correct, and that this connector has been added and configured for your application.  #### ConnectionNotFoundError  A valid connection could not be found associated to your &#x60;application_id&#x60;. Something _may_ have interrupted the authorization flow. You may need to start the connector authorization process again.  #### ConnectionSettingsError  The connector has required settings that were not supplied. Verify &#x60;connection.settings&#x60; contains all required settings for the connector to be callable.  #### ConnectorNotFoundError  A request was made for an unknown connector. Verify your &#x60;service_id&#x60; is spelled correctly, and that this connector is enabled for your provided &#x60;unified_api&#x60;.  #### OAuthRedirectUriError  A request was made either in a connector authorization flow, or attempting to revoke connector access without a valid &#x60;redirect_uri&#x60;. This is the url the user should be returned to on completion of process.  #### OAuthInvalidStateError  The state param is required and is used to ensure the outgoing authorization state has not been altered before the user is redirected back. It also contains required params needed to identify the connector being used. If this has been altered, the authorization will not succeed.  #### OAuthCodeExchangeError  When attempting to exchange the authorization code for an &#x60;access_token&#x60; during an OAuth flow, an error occurred. This may be temporary. You can reattempt authorization or contact our team to resolve the issue.  #### OAuthConnectorError  It seems something went wrong on the connector side. It&#39;s possible this connector is in &#x60;beta&#x60; or still under development. We&#39;ve been notified and are working to fix this issue.  #### MappingError  There was an error attempting to retrieve the mapping for a given attribute. We&#39;ve been notified and are working to fix this issue.  #### ConnectorMappingNotFoundError  It seems the implementation for this connector is incomplete. It&#39;s possible this connector is in &#x60;beta&#x60; or still under development. We&#39;ve been notified and are working to fix this issue.  #### ConnectorResponseMappingNotFoundError  We were unable to retrieve the response mapping for this connector. It&#39;s possible this connector is in &#x60;beta&#x60; or still under development. We&#39;ve been notified and are working to fix this issue.  #### ConnectorOperationMappingNotFoundError  Connector mapping has not been implemented for the requested operation. It&#39;s possible this connector is in &#x60;beta&#x60; or still under development. We&#39;ve been notified and are working to fix this issue.  #### ConnectorWorkflowMappingError  The composite api calls required for this operation have not been mapped entirely. It&#39;s possible this connector is in &#x60;beta&#x60; or still under development. We&#39;ve been notified and are working to fix this issue.  #### ConnectorOperationUnsupportedError  You&#39;re attempting a call that is not supported by the connector. It&#39;s likely this operation is supported by another connector, but we&#39;re unable to implement for this one.  #### PaginationNotSupportedError  Pagination is not yet supported for this connector, try removing limit and/or cursor from the query. It&#39;s possible this connector is in &#x60;beta&#x60; or still under development. We&#39;ve been notified and are working to fix this issue.  ## API Design  ### API Styles and data formats  #### REST API  The API is organized around [REST](https://restfulapi.net/), providing simple and predictable URIs to access and modify objects. Requests support standard HTTP methods like GET, PUT, POST, and DELETE and standard status codes. JSON is returned by all API responses, including errors. In all API requests, you must set the content-type HTTP header to application/json. All API requests must be made over HTTPS. Calls made over HTTP will fail.  ##### Available HTTP methods  The Apideck API uses HTTP verbs to understand if you want to read (GET), delete (DELETE) or create (POST) an object. When your web application cannot do a POST or DELETE, we provide the ability to set the method through the query parameter \\_method.  &#x60;&#x60;&#x60; POST /messages GET /messages GET /messages/{messageId} PATCH /messages/{messageId} DELETE /messages/{messageId} &#x60;&#x60;&#x60;  Response bodies are always UTF-8 encoded JSON objects, unless explicitly documented otherwise. For some endpoints and use cases we divert from REST to provide a better developer experience.  ### Schema  All API requests and response bodies adhere to a common JSON format representing individual items, collections of items, links to related items and additional meta data.  ### Meta  Meta data can be represented as a top level member named “meta”. Any information may be provided in the meta data. It’s most common use is to return the total number of records when requesting a collection of resources.  ### Idempotence (upcoming)  To prevent the creation of duplicate resources, every POST method (such as one that creates a consumer record) must specify a unique value for the X-Unique-Transaction-ID header name. Uniquely identifying each unique POST request ensures that the API processes a given request once and only once.  Uniquely identifying new resource-creation POSTs is especially important when the outcome of a response is ambiguous because of a transient service interruption, such as a server-side timeout or network disruption. If a service interruption occurs, then the client application can safely retry the uniquely identified request without creating duplicate operations. (API endpoints that guarantee that every uniquely identified request is processed only once no matter how many times that uniquely identifiable request is made are described as idempotent.)  ### Request IDs  Each API request has an associated request identifier. You can find this value in the response headers, under Request-Id. You can also find request identifiers in the URLs of individual request logs in your Dashboard. If you need to contact us about a specific request, providing the request identifier will ensure the fastest possible resolution.  ### Fixed field types  #### Dates  The dates returned by the API are all represented in UTC (ISO8601 format).  This example &#x60;2019-11-14T00:55:31.820Z&#x60; is defined by the ISO 8601 standard. The T in the middle separates the year-month-day portion from the hour-minute-second portion. The Z on the end means UTC, that is, an offset-from-UTC of zero hours-minutes-seconds. The Z is pronounced \&quot;Zulu\&quot; per military/aviation tradition.  The ISO 8601 standard is more modern. The formats are wisely designed to be easy to parse by machine as well as easy to read by humans across cultures.  #### Prices and Currencies  All prices returned by the API are represented as integer amounts in a currency’s smallest unit. For example, $5 USD would be returned as 500 (i.e, 500 cents).  For zero-decimal currencies, amounts will still be provided as an integer but without the need to divide by 100. For example, an amount of ¥5 (JPY) would be returned as 5.  All currency codes conform to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217).  ## Support  If you have problems or need help with your case, you can always reach out to our Support.  .<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var HrisApi = require('index'); // See note below*.
* var xxxSvc = new HrisApi.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new HrisApi.Yyy(); // Construct a model instance.
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
* var xxxSvc = new HrisApi.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new HrisApi.Yyy(); // Construct a model instance.
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
     * The BankAccount model constructor.
     * @property {module:model/BankAccount}
     */
    BankAccount,

    /**
     * The Benefit model constructor.
     * @property {module:model/Benefit}
     */
    Benefit,

    /**
     * The Compensation model constructor.
     * @property {module:model/Compensation}
     */
    Compensation,

    /**
     * The CreateDepartmentResponse model constructor.
     * @property {module:model/CreateDepartmentResponse}
     */
    CreateDepartmentResponse,

    /**
     * The CreateEmployeeResponse model constructor.
     * @property {module:model/CreateEmployeeResponse}
     */
    CreateEmployeeResponse,

    /**
     * The CreateHrisCompanyResponse model constructor.
     * @property {module:model/CreateHrisCompanyResponse}
     */
    CreateHrisCompanyResponse,

    /**
     * The CreateTimeOffRequestResponse model constructor.
     * @property {module:model/CreateTimeOffRequestResponse}
     */
    CreateTimeOffRequestResponse,

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
     * The Deduction model constructor.
     * @property {module:model/Deduction}
     */
    Deduction,

    /**
     * The DeleteDepartmentResponse model constructor.
     * @property {module:model/DeleteDepartmentResponse}
     */
    DeleteDepartmentResponse,

    /**
     * The DeleteEmployeeResponse model constructor.
     * @property {module:model/DeleteEmployeeResponse}
     */
    DeleteEmployeeResponse,

    /**
     * The DeleteHrisCompanyResponse model constructor.
     * @property {module:model/DeleteHrisCompanyResponse}
     */
    DeleteHrisCompanyResponse,

    /**
     * The DeleteTimeOffRequestResponse model constructor.
     * @property {module:model/DeleteTimeOffRequestResponse}
     */
    DeleteTimeOffRequestResponse,

    /**
     * The Department model constructor.
     * @property {module:model/Department}
     */
    Department,

    /**
     * The Email model constructor.
     * @property {module:model/Email}
     */
    Email,

    /**
     * The Employee model constructor.
     * @property {module:model/Employee}
     */
    Employee,

    /**
     * The EmployeeCompensation model constructor.
     * @property {module:model/EmployeeCompensation}
     */
    EmployeeCompensation,

    /**
     * The EmployeeEmploymentRole model constructor.
     * @property {module:model/EmployeeEmploymentRole}
     */
    EmployeeEmploymentRole,

    /**
     * The EmployeeJob model constructor.
     * @property {module:model/EmployeeJob}
     */
    EmployeeJob,

    /**
     * The EmployeeList model constructor.
     * @property {module:model/EmployeeList}
     */
    EmployeeList,

    /**
     * The EmployeeManager model constructor.
     * @property {module:model/EmployeeManager}
     */
    EmployeeManager,

    /**
     * The EmployeePayroll model constructor.
     * @property {module:model/EmployeePayroll}
     */
    EmployeePayroll,

    /**
     * The EmployeeSchedules model constructor.
     * @property {module:model/EmployeeSchedules}
     */
    EmployeeSchedules,

    /**
     * The EmployeesFilter model constructor.
     * @property {module:model/EmployeesFilter}
     */
    EmployeesFilter,

    /**
     * The EmployeesSort model constructor.
     * @property {module:model/EmployeesSort}
     */
    EmployeesSort,

    /**
     * The EmploymentStatus model constructor.
     * @property {module:model/EmploymentStatus}
     */
    EmploymentStatus,

    /**
     * The Gender model constructor.
     * @property {module:model/Gender}
     */
    Gender,

    /**
     * The GetDepartmentResponse model constructor.
     * @property {module:model/GetDepartmentResponse}
     */
    GetDepartmentResponse,

    /**
     * The GetDepartmentsResponse model constructor.
     * @property {module:model/GetDepartmentsResponse}
     */
    GetDepartmentsResponse,

    /**
     * The GetEmployeePayrollResponse model constructor.
     * @property {module:model/GetEmployeePayrollResponse}
     */
    GetEmployeePayrollResponse,

    /**
     * The GetEmployeePayrollsResponse model constructor.
     * @property {module:model/GetEmployeePayrollsResponse}
     */
    GetEmployeePayrollsResponse,

    /**
     * The GetEmployeeResponse model constructor.
     * @property {module:model/GetEmployeeResponse}
     */
    GetEmployeeResponse,

    /**
     * The GetEmployeeSchedulesResponse model constructor.
     * @property {module:model/GetEmployeeSchedulesResponse}
     */
    GetEmployeeSchedulesResponse,

    /**
     * The GetEmployeesResponse model constructor.
     * @property {module:model/GetEmployeesResponse}
     */
    GetEmployeesResponse,

    /**
     * The GetHrisCompaniesResponse model constructor.
     * @property {module:model/GetHrisCompaniesResponse}
     */
    GetHrisCompaniesResponse,

    /**
     * The GetHrisCompanyResponse model constructor.
     * @property {module:model/GetHrisCompanyResponse}
     */
    GetHrisCompanyResponse,

    /**
     * The GetHrisJobResponse model constructor.
     * @property {module:model/GetHrisJobResponse}
     */
    GetHrisJobResponse,

    /**
     * The GetHrisJobsResponse model constructor.
     * @property {module:model/GetHrisJobsResponse}
     */
    GetHrisJobsResponse,

    /**
     * The GetPayrollResponse model constructor.
     * @property {module:model/GetPayrollResponse}
     */
    GetPayrollResponse,

    /**
     * The GetPayrollsResponse model constructor.
     * @property {module:model/GetPayrollsResponse}
     */
    GetPayrollsResponse,

    /**
     * The GetTimeOffRequestResponse model constructor.
     * @property {module:model/GetTimeOffRequestResponse}
     */
    GetTimeOffRequestResponse,

    /**
     * The GetTimeOffRequestsResponse model constructor.
     * @property {module:model/GetTimeOffRequestsResponse}
     */
    GetTimeOffRequestsResponse,

    /**
     * The HrisCompany model constructor.
     * @property {module:model/HrisCompany}
     */
    HrisCompany,

    /**
     * The HrisEventType model constructor.
     * @property {module:model/HrisEventType}
     */
    HrisEventType,

    /**
     * The HrisJob model constructor.
     * @property {module:model/HrisJob}
     */
    HrisJob,

    /**
     * The HrisJobLocation model constructor.
     * @property {module:model/HrisJobLocation}
     */
    HrisJobLocation,

    /**
     * The HrisJobs model constructor.
     * @property {module:model/HrisJobs}
     */
    HrisJobs,

    /**
     * The HrisWebhookEvent model constructor.
     * @property {module:model/HrisWebhookEvent}
     */
    HrisWebhookEvent,

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
     * The PaymentFrequency model constructor.
     * @property {module:model/PaymentFrequency}
     */
    PaymentFrequency,

    /**
     * The PaymentRequiredResponse model constructor.
     * @property {module:model/PaymentRequiredResponse}
     */
    PaymentRequiredResponse,

    /**
     * The PaymentUnit model constructor.
     * @property {module:model/PaymentUnit}
     */
    PaymentUnit,

    /**
     * The Payroll model constructor.
     * @property {module:model/Payroll}
     */
    Payroll,

    /**
     * The PayrollTotals model constructor.
     * @property {module:model/PayrollTotals}
     */
    PayrollTotals,

    /**
     * The PayrollsFilter model constructor.
     * @property {module:model/PayrollsFilter}
     */
    PayrollsFilter,

    /**
     * The Person model constructor.
     * @property {module:model/Person}
     */
    Person,

    /**
     * The PhoneNumber model constructor.
     * @property {module:model/PhoneNumber}
     */
    PhoneNumber,

    /**
     * The ProbationPeriod model constructor.
     * @property {module:model/ProbationPeriod}
     */
    ProbationPeriod,

    /**
     * The Schedule model constructor.
     * @property {module:model/Schedule}
     */
    Schedule,

    /**
     * The ScheduleWorkPattern model constructor.
     * @property {module:model/ScheduleWorkPattern}
     */
    ScheduleWorkPattern,

    /**
     * The ScheduleWorkPatternEvenWeeks model constructor.
     * @property {module:model/ScheduleWorkPatternEvenWeeks}
     */
    ScheduleWorkPatternEvenWeeks,

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
     * The Tax model constructor.
     * @property {module:model/Tax}
     */
    Tax,

    /**
     * The Team model constructor.
     * @property {module:model/Team}
     */
    Team,

    /**
     * The TimeOffRequest model constructor.
     * @property {module:model/TimeOffRequest}
     */
    TimeOffRequest,

    /**
     * The TimeOffRequestNotes model constructor.
     * @property {module:model/TimeOffRequestNotes}
     */
    TimeOffRequestNotes,

    /**
     * The TimeOffRequestsFilter model constructor.
     * @property {module:model/TimeOffRequestsFilter}
     */
    TimeOffRequestsFilter,

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
     * The UpdateDepartmentResponse model constructor.
     * @property {module:model/UpdateDepartmentResponse}
     */
    UpdateDepartmentResponse,

    /**
     * The UpdateEmployeeResponse model constructor.
     * @property {module:model/UpdateEmployeeResponse}
     */
    UpdateEmployeeResponse,

    /**
     * The UpdateHrisCompanyResponse model constructor.
     * @property {module:model/UpdateHrisCompanyResponse}
     */
    UpdateHrisCompanyResponse,

    /**
     * The UpdateTimeOffRequestResponse model constructor.
     * @property {module:model/UpdateTimeOffRequestResponse}
     */
    UpdateTimeOffRequestResponse,

    /**
     * The WebhookEvent model constructor.
     * @property {module:model/WebhookEvent}
     */
    WebhookEvent,

    /**
     * The Website model constructor.
     * @property {module:model/Website}
     */
    Website,

    /**
    * The CompaniesApi service constructor.
    * @property {module:api/CompaniesApi}
    */
    CompaniesApi,

    /**
    * The DepartmentsApi service constructor.
    * @property {module:api/DepartmentsApi}
    */
    DepartmentsApi,

    /**
    * The EmployeePayrollsApi service constructor.
    * @property {module:api/EmployeePayrollsApi}
    */
    EmployeePayrollsApi,

    /**
    * The EmployeeSchedulesApi service constructor.
    * @property {module:api/EmployeeSchedulesApi}
    */
    EmployeeSchedulesApi,

    /**
    * The EmployeesApi service constructor.
    * @property {module:api/EmployeesApi}
    */
    EmployeesApi,

    /**
    * The PayrollsApi service constructor.
    * @property {module:api/PayrollsApi}
    */
    PayrollsApi,

    /**
    * The TimeOffRequestsApi service constructor.
    * @property {module:api/TimeOffRequestsApi}
    */
    TimeOffRequestsApi
};
