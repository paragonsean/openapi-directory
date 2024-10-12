# checks_api

ChecksApi - JavaScript client for checks_api
**NOTE:** This is a preview of the API and it is not considered stable since refinements are still being made.

# Introduction

Welcome to the  **Truora Check** [**RESTful API**](https://en.wikipedia.org/wiki/Representational_state_transfer) reference. You may also want to check out our [**Validations API docs**](https://docs.validations.truora.com/) or our [**Signals API docs**](https://docs.signals.truora.com/).

Truora Check API allows performing full background checks on people, vehicles and companies. There are three main types of background checks:

- **Personal background check**: Verifies national IDs in multiple databases of public and legal entities in the LATAM region. For every national ID, returns information on: personal identity, criminal records, international background check, and professional background.

- **Vehicle background check**: Verifies the vehicle documents and the owner identity in multiple databases of public and legal entities in the LATAM region. For every vehicle and owner type, returns information on: personal identity, driving records, criminal records, and vehicle information.  

- **Company background check**: Verifies the tax ID or a company name in multiple databases of public and legal entities in the LATAM region. For every company, returns the associated: business status, legal and criminal records, and media reports.

# API Key V1 is live!

API key version 1 is now live. Users with version 0 API keys are not immediately required to upgrade to V1 but should plan to do so at their earliest convenience. The changes for integration with API keys v1 are as follows:

- The field ``user_authorized`` is now required to perform person checks. This field indicates the API user has authorization to perform the check in compliance with data protection law.
- The field ``homonym_scores`` is no longer included in our person check response as its results are already included in the body of the check and keeping them duplicated is generating unnecessary confusion.


# API composition

## Endpoints

- **Check endpoints**: Provide an easy way to create and search for a background check. They also allow inserting groups of checks into reports. Each check contains scores, datasets and databases.
 
```plain
https://api.truora.com/v1/checks
```

- **Report endpoints**: Support batch uploads and grouping multiple checks together. Excel and .csv files are supported for batch uploads.
 
```plain
https://api.truora.com/v1/reports
```

- **Configuration endpoints**: Allows personalizing data sets and scores for customized background checks.

```plain
https://api.truora.com/v1/config
```

- **Continuous check endpoints**: Allows creating recurring checks and get notified whenever a change in the check score occurs.

```plain
https://api.truora.com/v1/continuous_checks
```

- **Behavior endpoints**: Allows sharing anonymous feedback about a person behavior when interacting with the company.

```plain
https://api.truora.com/v1/behaviour
```

- **Hooks endpoints**: Allows sending notifications via requests to your service or another third-party service whenever certain events occur.

```plain
https://api.truora.com/v1/hooks
```

## Datasets

Categories that group the resulting information for background checks from databases are called datasets. Datasets are divided in:

- **Personal identity**: Corroborates the existence and validates personal identity documents. 

- **Criminal record**: Checks for crimes according to each country penal code or criminal code. Keep in mind that data aged less than 10 years is usually more consistent.

- **Legal background**: Checks for lawsuits filed. Keep in mind that data aged less than 10 years is usually more consistent.

- **International background**: Checks international lists for crimes related to identity theft, money laundering, terrorist financing, and high crimes.

- **Professional background**: Checks professional regulatory entities for relevant information.

- **Affiliations and insurances**: Checks the history and status of social security affiliations.

- **Alert in media**: Checks major media agencies for relevant news related to violent actions.    

- **Vehicle information**: Checks for the physical characteristics of the vehicle, technical status, insurance history, and other relevant information.

- **Traffic fines**: Checks for outstanding traffic fines.

- **Driving licenses**: Shows information relevant to the driver. Such as license status and driver certificates.

- **Business background**: Checks for business status, legal and criminal history, and other relevant information.

- **Taxes and Finances**: Checks for the information related to personal finances, liabilities, and taxes.

## Requests Format

The POST requests receive a body that must be encoded in `www-x-form-urlencoded`, for instance:

```plain
type=person&national_id=123456&country=CO
```

The responses are always encoded in `JSON` format.

## Errors

Whenever there is an error, a JSON with the following format is returned:

```json
{
    \"code\": <Truora error code>,
    \"http_code\": <The HTTP status of the response>,
    \"message\": <The error message>
}
```

for instance:

```json
{
    \"code\": 10404,
    \"http_code\": 404,
    \"message\": \"The Check was not found\"
}
```

## SDKs

If your favorite language was not on the next list, You can use our [OpenAPI 3 spec](https://docs.truora.com/openapi.json) to generate it using the [Open API Generator](https://openapi-generator.tech/docs/installation).

To download the SDK click on the desired programming language:

- [C# .Net Core](https://truora-sdk.s3.amazonaws.com/checks/checks_csharp-netcore_latest.zip)

- [Elixir](https://truora-sdk.s3.amazonaws.com/checks/checks_elixir_latest.zip)

- [Go](https://truora-sdk.s3.amazonaws.com/checks/checks_go_latest.zip)

- [Java](https://truora-sdk.s3.amazonaws.com/checks/checks_java_latest.zip)

- [JavaScript](https://truora-sdk.s3.amazonaws.com/checks/checks_javascript_latest.zip)

- [Objc](https://truora-sdk.s3.amazonaws.com/checks/checks_objc_latest.zip)

- [Php](https://truora-sdk.s3.amazonaws.com/checks/checks_php_latest.zip)

- [Python](https://truora-sdk.s3.amazonaws.com/checks/checks_python_latest.zip)

- [Ruby](https://truora-sdk.s3.amazonaws.com/checks/checks_ruby_latest.zip)

You can see the full list of supported platforms here:

https://openapi-generator.tech/docs/generators



This SDK is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Generator version: 7.9.0
- Build package: org.openapitools.codegen.languages.JavascriptClientCodegen
For more information, please visit [https://www.truora.com](https://www.truora.com)

## Installation

### For [Node.js](https://nodejs.org/)

#### npm

To publish the library as a [npm](https://www.npmjs.com/), please follow the procedure in ["Publishing npm packages"](https://docs.npmjs.com/getting-started/publishing-npm-packages).

Then install it via:

```shell
npm install checks_api --save
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

To use the link you just defined in your project, switch to the directory you want to use your checks_api from, and run:

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
var ChecksApi = require('checks_api');

var defaultClient = ChecksApi.ApiClient.instance;
// Configure API key authorization: api-key
var api-key = defaultClient.authentications['api-key'];
api-key.apiKey = "YOUR API KEY"
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix['Truora-API-Key'] = "Token"

var api = new ChecksApi.BehaviorApi()
var birthDate = new Date("2013-10-20T19:20:30+01:00"); // {Date} Birth date of reported person
var country = "country_example"; // {String} Document country
var documentId = "documentId_example"; // {String} Person document ID
var documentType = "documentType_example"; // {String} Document type associated with the background check
var email = "email_example"; // {String} Reported person e-mail
var feedbackDate = new Date("2013-10-20T19:20:30+01:00"); // {Date} Behavior report date
var firstName = "firstName_example"; // {String} Person first name
var lastName = "lastName_example"; // {String} Person last name
var reason = "reason_example"; // {String} Report reason
var opts = {
  'phoneNumber': "phoneNumber_example" // {String} Phone number of the reported person
};
var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
api.reportBehavior(birthDate, country, documentId, documentType, email, feedbackDate, firstName, lastName, reason, opts, callback);

```

## Documentation for API Endpoints

All URIs are relative to *https://api.truora.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ChecksApi.BehaviorApi* | [**reportBehavior**](docs/BehaviorApi.md#reportBehavior) | **POST** /v1/behavior | Report Behavior
*ChecksApi.ChecksApi* | [**createCheck**](docs/ChecksApi.md#createCheck) | **POST** /v1/checks | Create a background check
*ChecksApi.ChecksApi* | [**getCheck**](docs/ChecksApi.md#getCheck) | **GET** /v1/checks/{check_id} | Get Background Check
*ChecksApi.ChecksApi* | [**getHealthDashboard**](docs/ChecksApi.md#getHealthDashboard) | **GET** /v1/checks/health | Get Health Dashboard
*ChecksApi.ChecksApi* | [**listCheckDetails**](docs/ChecksApi.md#listCheckDetails) | **GET** /v1/checks/{check_id}/details | List Check Details
*ChecksApi.ChecksApi* | [**listChecks**](docs/ChecksApi.md#listChecks) | **GET** /v1/checks | List Checks
*ChecksApi.ContinuousApi* | [**createContinuousCheck**](docs/ContinuousApi.md#createContinuousCheck) | **POST** /v1/continuous-checks | 
*ChecksApi.ContinuousApi* | [**getContinuousCheck**](docs/ContinuousApi.md#getContinuousCheck) | **GET** /v1/continuous-checks/{continuous_check_id} | 
*ChecksApi.ContinuousApi* | [**listContinuousChecks**](docs/ContinuousApi.md#listContinuousChecks) | **GET** /v1/continuous-checks | 
*ChecksApi.ContinuousApi* | [**updateContinuousCheck**](docs/ContinuousApi.md#updateContinuousCheck) | **PUT** /v1/continuous-checks/{continuous_check_id} | 
*ChecksApi.ContinuousApi* | [**v1ContinuousChecksContinuousCheckIdHistoryGet**](docs/ContinuousApi.md#v1ContinuousChecksContinuousCheckIdHistoryGet) | **GET** /v1/continuous-checks/{continuous_check_id}/history | 
*ChecksApi.CustomTypeApi* | [**createScoreConfig**](docs/CustomTypeApi.md#createScoreConfig) | **POST** /v1/config | Create Score Configurations
*ChecksApi.CustomTypeApi* | [**deleteCustomType**](docs/CustomTypeApi.md#deleteCustomType) | **DELETE** /v1/config | Delete Custom Type
*ChecksApi.CustomTypeApi* | [**listScoreConfigs**](docs/CustomTypeApi.md#listScoreConfigs) | **GET** /v1/config | List Score Configurations
*ChecksApi.CustomTypeApi* | [**updateCustomType**](docs/CustomTypeApi.md#updateCustomType) | **PUT** /v1/config | Update Custom Type
*ChecksApi.HooksApi* | [**createHook**](docs/HooksApi.md#createHook) | **POST** /v1/hooks | Creates a hook subscription
*ChecksApi.HooksApi* | [**deletHook**](docs/HooksApi.md#deletHook) | **DELETE** /v1/hooks/{hook_id} | Deletes hook
*ChecksApi.HooksApi* | [**listHook**](docs/HooksApi.md#listHook) | **GET** /v1/hooks | Lists all hooks
*ChecksApi.HooksApi* | [**updateHook**](docs/HooksApi.md#updateHook) | **PUT** /v1/hooks/{hook_id} | Updates hook
*ChecksApi.PdfApi* | [**createPDF**](docs/PdfApi.md#createPDF) | **POST** /v1/checks/{check_id}/pdf | Create PDF
*ChecksApi.PdfApi* | [**getPDF**](docs/PdfApi.md#getPDF) | **GET** /v1/checks/{check_id}/pdf | Get PDF
*ChecksApi.ReportsApi* | [**batchUpload**](docs/ReportsApi.md#batchUpload) | **POST** /v1/reports/{report_id}/upload | Batch Upload
*ChecksApi.ReportsApi* | [**createReport**](docs/ReportsApi.md#createReport) | **POST** /v1/reports | Create Report
*ChecksApi.ReportsApi* | [**getReport**](docs/ReportsApi.md#getReport) | **GET** /v1/reports/{report_id} | Get Report
*ChecksApi.ReportsApi* | [**listReports**](docs/ReportsApi.md#listReports) | **GET** /v1/reports | List Reports


## Documentation for Models

 - [ChecksApi.APIKey](docs/APIKey.md)
 - [ChecksApi.APIKeyVersion](docs/APIKeyVersion.md)
 - [ChecksApi.APIKeyVersionChangelog](docs/APIKeyVersionChangelog.md)
 - [ChecksApi.Behavior](docs/Behavior.md)
 - [ChecksApi.BehaviourOutput](docs/BehaviourOutput.md)
 - [ChecksApi.Change](docs/Change.md)
 - [ChecksApi.Check](docs/Check.md)
 - [ChecksApi.CheckDetails](docs/CheckDetails.md)
 - [ChecksApi.CheckDetailsOutput](docs/CheckDetailsOutput.md)
 - [ChecksApi.CheckOutput](docs/CheckOutput.md)
 - [ChecksApi.ChecksOutput](docs/ChecksOutput.md)
 - [ChecksApi.Comment](docs/Comment.md)
 - [ChecksApi.CommentOutput](docs/CommentOutput.md)
 - [ChecksApi.CommentsOutput](docs/CommentsOutput.md)
 - [ChecksApi.CompanySummary](docs/CompanySummary.md)
 - [ChecksApi.Config](docs/Config.md)
 - [ChecksApi.ContinuousCheck](docs/ContinuousCheck.md)
 - [ChecksApi.ContinuousCheckEntry](docs/ContinuousCheckEntry.md)
 - [ChecksApi.CreateAPIKeyInput](docs/CreateAPIKeyInput.md)
 - [ChecksApi.CreateCommentInput](docs/CreateCommentInput.md)
 - [ChecksApi.CreateRuleInput](docs/CreateRuleInput.md)
 - [ChecksApi.CreateUserInput](docs/CreateUserInput.md)
 - [ChecksApi.Database](docs/Database.md)
 - [ChecksApi.DeleteAPIKeyInput](docs/DeleteAPIKeyInput.md)
 - [ChecksApi.DeleteUserInput](docs/DeleteUserInput.md)
 - [ChecksApi.Error](docs/Error.md)
 - [ChecksApi.GetContiuousCheckHistoryOutput](docs/GetContiuousCheckHistoryOutput.md)
 - [ChecksApi.GetHealthDashboardInput](docs/GetHealthDashboardInput.md)
 - [ChecksApi.Hook](docs/Hook.md)
 - [ChecksApi.HookOutput](docs/HookOutput.md)
 - [ChecksApi.ListContinuousChecksOutput](docs/ListContinuousChecksOutput.md)
 - [ChecksApi.NameFound](docs/NameFound.md)
 - [ChecksApi.Report](docs/Report.md)
 - [ChecksApi.ReportOutput](docs/ReportOutput.md)
 - [ChecksApi.ReportsOutput](docs/ReportsOutput.md)
 - [ChecksApi.Rule](docs/Rule.md)
 - [ChecksApi.RuleOutput](docs/RuleOutput.md)
 - [ChecksApi.Score](docs/Score.md)
 - [ChecksApi.ScoreConfig](docs/ScoreConfig.md)
 - [ChecksApi.ScoreConfigOutput](docs/ScoreConfigOutput.md)
 - [ChecksApi.ScoreConfigsOutput](docs/ScoreConfigsOutput.md)
 - [ChecksApi.ScoreDetail](docs/ScoreDetail.md)
 - [ChecksApi.Status](docs/Status.md)
 - [ChecksApi.Subscriber](docs/Subscriber.md)
 - [ChecksApi.Summary](docs/Summary.md)
 - [ChecksApi.Table](docs/Table.md)
 - [ChecksApi.TableCell](docs/TableCell.md)
 - [ChecksApi.TableRow](docs/TableRow.md)
 - [ChecksApi.UpdateAPIKeyInput](docs/UpdateAPIKeyInput.md)
 - [ChecksApi.User](docs/User.md)
 - [ChecksApi.VehicleSummary](docs/VehicleSummary.md)
 - [ChecksApi.WrongInput](docs/WrongInput.md)


## Documentation for Authorization


Authentication schemes defined for the API:
### api-key


- **Type**: API key
- **API key parameter name**: Truora-API-Key
- **Location**: HTTP header

