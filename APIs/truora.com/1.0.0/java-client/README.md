# openapi-java-client

Checks API
- API version: 1.0.0
  - Build date: 2024-10-12T10:02:35.353156-04:00[America/New_York]
  - Generator version: 7.9.0

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




  For more information, please visit [https://www.truora.com](https://www.truora.com)

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
  <version>1.0.0</version>
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
     implementation "org.openapitools:openapi-java-client:1.0.0"
  }
```

### Others

At first generate the JAR by executing:

```shell
mvn clean package
```

Then manually install the following JARs:

* `target/openapi-java-client-1.0.0.jar`
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
import org.openapitools.client.api.BehaviorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.truora.com");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    BehaviorApi apiInstance = new BehaviorApi(defaultClient);
    OffsetDateTime birthDate = OffsetDateTime.now(); // OffsetDateTime | Birth date of reported person
    String country = "co"; // String | Document country
    String documentId = "documentId_example"; // String | Person document ID
    String documentType = "national-id"; // String | Document type associated with the background check
    String email = "email_example"; // String | Reported person e-mail
    OffsetDateTime feedbackDate = OffsetDateTime.now(); // OffsetDateTime | Behavior report date
    String firstName = "firstName_example"; // String | Person first name
    String lastName = "lastName_example"; // String | Person last name
    String reason = "rape"; // String | Report reason
    String phoneNumber = "phoneNumber_example"; // String | Phone number of the reported person
    try {
      BehaviourOutput result = apiInstance.reportBehavior(birthDate, country, documentId, documentType, email, feedbackDate, firstName, lastName, reason, phoneNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BehaviorApi#reportBehavior");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

## Documentation for API Endpoints

All URIs are relative to *https://api.truora.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BehaviorApi* | [**reportBehavior**](docs/BehaviorApi.md#reportBehavior) | **POST** /v1/behavior | Report Behavior
*ChecksApi* | [**createCheck**](docs/ChecksApi.md#createCheck) | **POST** /v1/checks | Create a background check
*ChecksApi* | [**getCheck**](docs/ChecksApi.md#getCheck) | **GET** /v1/checks/{check_id} | Get Background Check
*ChecksApi* | [**getHealthDashboard**](docs/ChecksApi.md#getHealthDashboard) | **GET** /v1/checks/health | Get Health Dashboard
*ChecksApi* | [**listCheckDetails**](docs/ChecksApi.md#listCheckDetails) | **GET** /v1/checks/{check_id}/details | List Check Details
*ChecksApi* | [**listChecks**](docs/ChecksApi.md#listChecks) | **GET** /v1/checks | List Checks
*ContinuousApi* | [**createContinuousCheck**](docs/ContinuousApi.md#createContinuousCheck) | **POST** /v1/continuous-checks | 
*ContinuousApi* | [**getContinuousCheck**](docs/ContinuousApi.md#getContinuousCheck) | **GET** /v1/continuous-checks/{continuous_check_id} | 
*ContinuousApi* | [**listContinuousChecks**](docs/ContinuousApi.md#listContinuousChecks) | **GET** /v1/continuous-checks | 
*ContinuousApi* | [**updateContinuousCheck**](docs/ContinuousApi.md#updateContinuousCheck) | **PUT** /v1/continuous-checks/{continuous_check_id} | 
*ContinuousApi* | [**v1ContinuousChecksContinuousCheckIdHistoryGet**](docs/ContinuousApi.md#v1ContinuousChecksContinuousCheckIdHistoryGet) | **GET** /v1/continuous-checks/{continuous_check_id}/history | 
*CustomTypeApi* | [**createScoreConfig**](docs/CustomTypeApi.md#createScoreConfig) | **POST** /v1/config | Create Score Configurations
*CustomTypeApi* | [**deleteCustomType**](docs/CustomTypeApi.md#deleteCustomType) | **DELETE** /v1/config | Delete Custom Type
*CustomTypeApi* | [**listScoreConfigs**](docs/CustomTypeApi.md#listScoreConfigs) | **GET** /v1/config | List Score Configurations
*CustomTypeApi* | [**updateCustomType**](docs/CustomTypeApi.md#updateCustomType) | **PUT** /v1/config | Update Custom Type
*HooksApi* | [**createHook**](docs/HooksApi.md#createHook) | **POST** /v1/hooks | Creates a hook subscription
*HooksApi* | [**deletHook**](docs/HooksApi.md#deletHook) | **DELETE** /v1/hooks/{hook_id} | Deletes hook
*HooksApi* | [**listHook**](docs/HooksApi.md#listHook) | **GET** /v1/hooks | Lists all hooks
*HooksApi* | [**updateHook**](docs/HooksApi.md#updateHook) | **PUT** /v1/hooks/{hook_id} | Updates hook
*PdfApi* | [**createPDF**](docs/PdfApi.md#createPDF) | **POST** /v1/checks/{check_id}/pdf | Create PDF
*PdfApi* | [**getPDF**](docs/PdfApi.md#getPDF) | **GET** /v1/checks/{check_id}/pdf | Get PDF
*ReportsApi* | [**batchUpload**](docs/ReportsApi.md#batchUpload) | **POST** /v1/reports/{report_id}/upload | Batch Upload
*ReportsApi* | [**createReport**](docs/ReportsApi.md#createReport) | **POST** /v1/reports | Create Report
*ReportsApi* | [**getReport**](docs/ReportsApi.md#getReport) | **GET** /v1/reports/{report_id} | Get Report
*ReportsApi* | [**listReports**](docs/ReportsApi.md#listReports) | **GET** /v1/reports | List Reports


## Documentation for Models

 - [APIKey](docs/APIKey.md)
 - [APIKeyVersion](docs/APIKeyVersion.md)
 - [APIKeyVersionChangelog](docs/APIKeyVersionChangelog.md)
 - [Behavior](docs/Behavior.md)
 - [BehaviourOutput](docs/BehaviourOutput.md)
 - [Change](docs/Change.md)
 - [Check](docs/Check.md)
 - [CheckDetails](docs/CheckDetails.md)
 - [CheckDetailsOutput](docs/CheckDetailsOutput.md)
 - [CheckOutput](docs/CheckOutput.md)
 - [ChecksOutput](docs/ChecksOutput.md)
 - [Comment](docs/Comment.md)
 - [CommentOutput](docs/CommentOutput.md)
 - [CommentsOutput](docs/CommentsOutput.md)
 - [CompanySummary](docs/CompanySummary.md)
 - [Config](docs/Config.md)
 - [ContinuousCheck](docs/ContinuousCheck.md)
 - [ContinuousCheckEntry](docs/ContinuousCheckEntry.md)
 - [CreateAPIKeyInput](docs/CreateAPIKeyInput.md)
 - [CreateCommentInput](docs/CreateCommentInput.md)
 - [CreateRuleInput](docs/CreateRuleInput.md)
 - [CreateUserInput](docs/CreateUserInput.md)
 - [Database](docs/Database.md)
 - [DeleteAPIKeyInput](docs/DeleteAPIKeyInput.md)
 - [DeleteUserInput](docs/DeleteUserInput.md)
 - [Error](docs/Error.md)
 - [GetContiuousCheckHistoryOutput](docs/GetContiuousCheckHistoryOutput.md)
 - [GetHealthDashboardInput](docs/GetHealthDashboardInput.md)
 - [Hook](docs/Hook.md)
 - [HookOutput](docs/HookOutput.md)
 - [ListContinuousChecksOutput](docs/ListContinuousChecksOutput.md)
 - [NameFound](docs/NameFound.md)
 - [Report](docs/Report.md)
 - [ReportOutput](docs/ReportOutput.md)
 - [ReportsOutput](docs/ReportsOutput.md)
 - [Rule](docs/Rule.md)
 - [RuleOutput](docs/RuleOutput.md)
 - [Score](docs/Score.md)
 - [ScoreConfig](docs/ScoreConfig.md)
 - [ScoreConfigOutput](docs/ScoreConfigOutput.md)
 - [ScoreConfigsOutput](docs/ScoreConfigsOutput.md)
 - [ScoreDetail](docs/ScoreDetail.md)
 - [Status](docs/Status.md)
 - [Subscriber](docs/Subscriber.md)
 - [Summary](docs/Summary.md)
 - [Table](docs/Table.md)
 - [TableCell](docs/TableCell.md)
 - [TableRow](docs/TableRow.md)
 - [UpdateAPIKeyInput](docs/UpdateAPIKeyInput.md)
 - [User](docs/User.md)
 - [VehicleSummary](docs/VehicleSummary.md)
 - [WrongInput](docs/WrongInput.md)


<a id="documentation-for-authorization"></a>
## Documentation for Authorization


Authentication schemes defined for the API:
<a id="api-key"></a>
### api-key

- **Type**: API key
- **API key parameter name**: Truora-API-Key
- **Location**: HTTP header


## Recommendation

It's recommended to create an instance of `ApiClient` per thread in a multithreaded environment to avoid any potential issues.

## Author

api@truora.com

