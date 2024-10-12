# crm_api

CrmApi - JavaScript client for crm_api
Welcome to the CRM API.

You can use this API to access all CRM API endpoints.

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
npm install crm_api --save
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

To use the link you just defined in your project, switch to the directory you want to use your crm_api from, and run:

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
var CrmApi = require('crm_api');

var defaultClient = CrmApi.ApiClient.instance;
// Configure API key authorization: apiKey
var apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = "YOUR API KEY"
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix['Authorization'] = "Token"

var api = new CrmApi.ActivitiesApi()
var xApideckConsumerId = "xApideckConsumerId_example"; // {String} ID of the consumer which you want to get or push data from
var xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // {String} The ID of your Unify application
var activity = new CrmApi.Activity(); // {Activity} 
var opts = {
  'raw': false, // {Boolean} Include raw response. Mostly used for debugging purposes
  'xApideckServiceId': "xApideckServiceId_example" // {String} Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
};
var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
api.activitiesAdd(xApideckConsumerId, xApideckAppId, activity, opts, callback);

```

## Documentation for API Endpoints

All URIs are relative to *https://unify.apideck.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CrmApi.ActivitiesApi* | [**activitiesAdd**](docs/ActivitiesApi.md#activitiesAdd) | **POST** /crm/activities | Create activity
*CrmApi.ActivitiesApi* | [**activitiesAll**](docs/ActivitiesApi.md#activitiesAll) | **GET** /crm/activities | List activities
*CrmApi.ActivitiesApi* | [**activitiesDelete**](docs/ActivitiesApi.md#activitiesDelete) | **DELETE** /crm/activities/{id} | Delete activity
*CrmApi.ActivitiesApi* | [**activitiesOne**](docs/ActivitiesApi.md#activitiesOne) | **GET** /crm/activities/{id} | Get activity
*CrmApi.ActivitiesApi* | [**activitiesUpdate**](docs/ActivitiesApi.md#activitiesUpdate) | **PATCH** /crm/activities/{id} | Update activity
*CrmApi.CompaniesApi* | [**companiesAdd**](docs/CompaniesApi.md#companiesAdd) | **POST** /crm/companies | Create company
*CrmApi.CompaniesApi* | [**companiesAll**](docs/CompaniesApi.md#companiesAll) | **GET** /crm/companies | List companies
*CrmApi.CompaniesApi* | [**companiesDelete**](docs/CompaniesApi.md#companiesDelete) | **DELETE** /crm/companies/{id} | Delete company
*CrmApi.CompaniesApi* | [**companiesOne**](docs/CompaniesApi.md#companiesOne) | **GET** /crm/companies/{id} | Get company
*CrmApi.CompaniesApi* | [**companiesUpdate**](docs/CompaniesApi.md#companiesUpdate) | **PATCH** /crm/companies/{id} | Update company
*CrmApi.ContactsApi* | [**contactsAdd**](docs/ContactsApi.md#contactsAdd) | **POST** /crm/contacts | Create contact
*CrmApi.ContactsApi* | [**contactsAll**](docs/ContactsApi.md#contactsAll) | **GET** /crm/contacts | List contacts
*CrmApi.ContactsApi* | [**contactsDelete**](docs/ContactsApi.md#contactsDelete) | **DELETE** /crm/contacts/{id} | Delete contact
*CrmApi.ContactsApi* | [**contactsOne**](docs/ContactsApi.md#contactsOne) | **GET** /crm/contacts/{id} | Get contact
*CrmApi.ContactsApi* | [**contactsUpdate**](docs/ContactsApi.md#contactsUpdate) | **PATCH** /crm/contacts/{id} | Update contact
*CrmApi.LeadsApi* | [**leadsAdd**](docs/LeadsApi.md#leadsAdd) | **POST** /crm/leads | Create lead
*CrmApi.LeadsApi* | [**leadsAll**](docs/LeadsApi.md#leadsAll) | **GET** /crm/leads | List leads
*CrmApi.LeadsApi* | [**leadsDelete**](docs/LeadsApi.md#leadsDelete) | **DELETE** /crm/leads/{id} | Delete lead
*CrmApi.LeadsApi* | [**leadsOne**](docs/LeadsApi.md#leadsOne) | **GET** /crm/leads/{id} | Get lead
*CrmApi.LeadsApi* | [**leadsUpdate**](docs/LeadsApi.md#leadsUpdate) | **PATCH** /crm/leads/{id} | Update lead
*CrmApi.NotesApi* | [**notesAdd**](docs/NotesApi.md#notesAdd) | **POST** /crm/notes | Create note
*CrmApi.NotesApi* | [**notesAll**](docs/NotesApi.md#notesAll) | **GET** /crm/notes | List notes
*CrmApi.NotesApi* | [**notesDelete**](docs/NotesApi.md#notesDelete) | **DELETE** /crm/notes/{id} | Delete note
*CrmApi.NotesApi* | [**notesOne**](docs/NotesApi.md#notesOne) | **GET** /crm/notes/{id} | Get note
*CrmApi.NotesApi* | [**notesUpdate**](docs/NotesApi.md#notesUpdate) | **PATCH** /crm/notes/{id} | Update note
*CrmApi.OpportunitiesApi* | [**opportunitiesAdd**](docs/OpportunitiesApi.md#opportunitiesAdd) | **POST** /crm/opportunities | Create opportunity
*CrmApi.OpportunitiesApi* | [**opportunitiesAll**](docs/OpportunitiesApi.md#opportunitiesAll) | **GET** /crm/opportunities | List opportunities
*CrmApi.OpportunitiesApi* | [**opportunitiesDelete**](docs/OpportunitiesApi.md#opportunitiesDelete) | **DELETE** /crm/opportunities/{id} | Delete opportunity
*CrmApi.OpportunitiesApi* | [**opportunitiesOne**](docs/OpportunitiesApi.md#opportunitiesOne) | **GET** /crm/opportunities/{id} | Get opportunity
*CrmApi.OpportunitiesApi* | [**opportunitiesUpdate**](docs/OpportunitiesApi.md#opportunitiesUpdate) | **PATCH** /crm/opportunities/{id} | Update opportunity
*CrmApi.PipelinesApi* | [**pipelinesAdd**](docs/PipelinesApi.md#pipelinesAdd) | **POST** /crm/pipelines | Create pipeline
*CrmApi.PipelinesApi* | [**pipelinesAll**](docs/PipelinesApi.md#pipelinesAll) | **GET** /crm/pipelines | List pipelines
*CrmApi.PipelinesApi* | [**pipelinesDelete**](docs/PipelinesApi.md#pipelinesDelete) | **DELETE** /crm/pipelines/{id} | Delete pipeline
*CrmApi.PipelinesApi* | [**pipelinesOne**](docs/PipelinesApi.md#pipelinesOne) | **GET** /crm/pipelines/{id} | Get pipeline
*CrmApi.PipelinesApi* | [**pipelinesUpdate**](docs/PipelinesApi.md#pipelinesUpdate) | **PATCH** /crm/pipelines/{id} | Update pipeline
*CrmApi.UsersApi* | [**usersAdd**](docs/UsersApi.md#usersAdd) | **POST** /crm/users | Create user
*CrmApi.UsersApi* | [**usersAll**](docs/UsersApi.md#usersAll) | **GET** /crm/users | List users
*CrmApi.UsersApi* | [**usersDelete**](docs/UsersApi.md#usersDelete) | **DELETE** /crm/users/{id} | Delete user
*CrmApi.UsersApi* | [**usersOne**](docs/UsersApi.md#usersOne) | **GET** /crm/users/{id} | Get user
*CrmApi.UsersApi* | [**usersUpdate**](docs/UsersApi.md#usersUpdate) | **PATCH** /crm/users/{id} | Update user


## Documentation for Models

 - [CrmApi.ActivitiesFilter](docs/ActivitiesFilter.md)
 - [CrmApi.Activity](docs/Activity.md)
 - [CrmApi.ActivityAttendee](docs/ActivityAttendee.md)
 - [CrmApi.Address](docs/Address.md)
 - [CrmApi.BadRequestResponse](docs/BadRequestResponse.md)
 - [CrmApi.BadRequestResponseDetail](docs/BadRequestResponseDetail.md)
 - [CrmApi.BankAccount](docs/BankAccount.md)
 - [CrmApi.CompaniesFilter](docs/CompaniesFilter.md)
 - [CrmApi.CompaniesSort](docs/CompaniesSort.md)
 - [CrmApi.Company](docs/Company.md)
 - [CrmApi.CompanyRowType](docs/CompanyRowType.md)
 - [CrmApi.Contact](docs/Contact.md)
 - [CrmApi.ContactsFilter](docs/ContactsFilter.md)
 - [CrmApi.ContactsSort](docs/ContactsSort.md)
 - [CrmApi.CreateActivityResponse](docs/CreateActivityResponse.md)
 - [CrmApi.CreateCompanyResponse](docs/CreateCompanyResponse.md)
 - [CrmApi.CreateContactResponse](docs/CreateContactResponse.md)
 - [CrmApi.CreateLeadResponse](docs/CreateLeadResponse.md)
 - [CrmApi.CreateNoteResponse](docs/CreateNoteResponse.md)
 - [CrmApi.CreateOpportunityResponse](docs/CreateOpportunityResponse.md)
 - [CrmApi.CreatePipelineResponse](docs/CreatePipelineResponse.md)
 - [CrmApi.CreateUserResponse](docs/CreateUserResponse.md)
 - [CrmApi.CrmEventType](docs/CrmEventType.md)
 - [CrmApi.CrmWebhookEvent](docs/CrmWebhookEvent.md)
 - [CrmApi.Currency](docs/Currency.md)
 - [CrmApi.CustomField](docs/CustomField.md)
 - [CrmApi.CustomFieldValue](docs/CustomFieldValue.md)
 - [CrmApi.DeleteActivityResponse](docs/DeleteActivityResponse.md)
 - [CrmApi.DeleteCompanyResponse](docs/DeleteCompanyResponse.md)
 - [CrmApi.DeleteContactResponse](docs/DeleteContactResponse.md)
 - [CrmApi.DeleteLeadResponse](docs/DeleteLeadResponse.md)
 - [CrmApi.DeleteNoteResponse](docs/DeleteNoteResponse.md)
 - [CrmApi.DeleteOpportunityResponse](docs/DeleteOpportunityResponse.md)
 - [CrmApi.DeletePipelineResponse](docs/DeletePipelineResponse.md)
 - [CrmApi.DeleteUserResponse](docs/DeleteUserResponse.md)
 - [CrmApi.Email](docs/Email.md)
 - [CrmApi.GetActivitiesResponse](docs/GetActivitiesResponse.md)
 - [CrmApi.GetActivityResponse](docs/GetActivityResponse.md)
 - [CrmApi.GetCompaniesResponse](docs/GetCompaniesResponse.md)
 - [CrmApi.GetCompanyResponse](docs/GetCompanyResponse.md)
 - [CrmApi.GetContactResponse](docs/GetContactResponse.md)
 - [CrmApi.GetContactsResponse](docs/GetContactsResponse.md)
 - [CrmApi.GetLeadResponse](docs/GetLeadResponse.md)
 - [CrmApi.GetLeadsResponse](docs/GetLeadsResponse.md)
 - [CrmApi.GetNoteResponse](docs/GetNoteResponse.md)
 - [CrmApi.GetNotesResponse](docs/GetNotesResponse.md)
 - [CrmApi.GetOpportunitiesResponse](docs/GetOpportunitiesResponse.md)
 - [CrmApi.GetOpportunityResponse](docs/GetOpportunityResponse.md)
 - [CrmApi.GetPipelineResponse](docs/GetPipelineResponse.md)
 - [CrmApi.GetPipelinesResponse](docs/GetPipelinesResponse.md)
 - [CrmApi.GetUserResponse](docs/GetUserResponse.md)
 - [CrmApi.GetUsersResponse](docs/GetUsersResponse.md)
 - [CrmApi.Lead](docs/Lead.md)
 - [CrmApi.LeadsFilter](docs/LeadsFilter.md)
 - [CrmApi.LeadsSort](docs/LeadsSort.md)
 - [CrmApi.Links](docs/Links.md)
 - [CrmApi.Meta](docs/Meta.md)
 - [CrmApi.MetaCursors](docs/MetaCursors.md)
 - [CrmApi.NotFoundResponse](docs/NotFoundResponse.md)
 - [CrmApi.NotFoundResponseDetail](docs/NotFoundResponseDetail.md)
 - [CrmApi.NotImplementedResponse](docs/NotImplementedResponse.md)
 - [CrmApi.NotImplementedResponseDetail](docs/NotImplementedResponseDetail.md)
 - [CrmApi.Note](docs/Note.md)
 - [CrmApi.OpportunitiesFilter](docs/OpportunitiesFilter.md)
 - [CrmApi.OpportunitiesSort](docs/OpportunitiesSort.md)
 - [CrmApi.Opportunity](docs/Opportunity.md)
 - [CrmApi.PassThroughQuery](docs/PassThroughQuery.md)
 - [CrmApi.PaymentRequiredResponse](docs/PaymentRequiredResponse.md)
 - [CrmApi.PhoneNumber](docs/PhoneNumber.md)
 - [CrmApi.Pipeline](docs/Pipeline.md)
 - [CrmApi.PipelineStagesInner](docs/PipelineStagesInner.md)
 - [CrmApi.SocialLink](docs/SocialLink.md)
 - [CrmApi.SortDirection](docs/SortDirection.md)
 - [CrmApi.TooManyRequestsResponse](docs/TooManyRequestsResponse.md)
 - [CrmApi.TooManyRequestsResponseDetail](docs/TooManyRequestsResponseDetail.md)
 - [CrmApi.UnauthorizedResponse](docs/UnauthorizedResponse.md)
 - [CrmApi.UnexpectedErrorResponse](docs/UnexpectedErrorResponse.md)
 - [CrmApi.UnexpectedErrorResponseDetail](docs/UnexpectedErrorResponseDetail.md)
 - [CrmApi.UnifiedId](docs/UnifiedId.md)
 - [CrmApi.UnprocessableResponse](docs/UnprocessableResponse.md)
 - [CrmApi.UpdateActivityResponse](docs/UpdateActivityResponse.md)
 - [CrmApi.UpdateCompanyResponse](docs/UpdateCompanyResponse.md)
 - [CrmApi.UpdateContactResponse](docs/UpdateContactResponse.md)
 - [CrmApi.UpdateLeadResponse](docs/UpdateLeadResponse.md)
 - [CrmApi.UpdateNoteResponse](docs/UpdateNoteResponse.md)
 - [CrmApi.UpdateOpportunityResponse](docs/UpdateOpportunityResponse.md)
 - [CrmApi.UpdatePipelineResponse](docs/UpdatePipelineResponse.md)
 - [CrmApi.UpdateUserResponse](docs/UpdateUserResponse.md)
 - [CrmApi.User](docs/User.md)
 - [CrmApi.Website](docs/Website.md)


## Documentation for Authorization


Authentication schemes defined for the API:
### apiKey


- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header

### applicationId


- **Type**: API key
- **API key parameter name**: x-apideck-app-id
- **Location**: HTTP header

### consumerId


- **Type**: API key
- **API key parameter name**: x-apideck-consumer-id
- **Location**: HTTP header

