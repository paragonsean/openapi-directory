# openapi-java-client

Visma e-conomic OpenAPI
- API version: v20.0.0
  - Build date: 2024-10-12T10:10:24.018579-04:00[America/New_York]
  - Generator version: 7.9.0

# Changelog

<details>
  <summary>Click to see changelog.</summary>

| Version | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|---------| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 20.0.0  | Customer contacts and delivery locations endpoints deprecated. You can find the same enpoints in [`Customers API`](https://apis.e-conomic.com/#Customers) 
| 19.0.0  | Page-based endpoints were moved under /paged url and cursor-based endpoints dropped the /all.
| 18.0.0  | Added isDeleted flag to [`customer-contacts`](#tag/Customer-contacts) and included deleted contacts in the response. <br> Deleted contacts can be used for history purposes, but cannot be set as reference persons on sales documents. <br> In previous versions only customer-contacts/id returns deleted contacts as well.
| 17.0.2  | `TimeEntryEmployeeNumberCannotBeUpdated` and `MileageEmployeeNumberCannotBeUpdated` error codes removed. The change affects all versions, but we bumped the version for transparency.
| 17.0.1  | New custom [`OpenAPI extension`](#section/Retrieving-data/Custom-extensions-in-OpenAPI-specification) added in the specification: `x-error-codes`. Existing `x-required-roles` extension converted to an array of strings.
| 17.0.0  | Improved the error model. Added `code` and `property` fields to the model. `code` represents the error code. `property` is the field name on which the input validation failed.
| 16.4.0  | [`customer-deliverylocations`](#tag/Customer-delivery-locations) endpoints added.
| 16.3.0  | [`customer-contacts`](#tag/Customer-contacts) endpoints added.  
| 16.2.2  | Added input validations for required string properties, if a string property is required it can't be empty, it should contain at least 1 character.
| 16.2.1  | Error codes extended for [`mileages`](#tag/Mileage-entries) and [`timeentries`](#tag/Time-entries). Affects all the exisiting versions.
| 16.2.0  | - [`employeegroups`](#operation/DeleteEmployeeGroupById) DELETE endpoint added. <br>- [`employees`](#operation/DeleteEmployeeById) DELETE endpoint added. <br>- [`project-employeegroups`](#operation/DeleteProjectEmployeeGroupById) DELETE endpoint added. <br>- [`project-employees`](#operation/DeleteProjectEmployeeById) DELETE endpoint added.
| 16.1.0  | [`Time entry prices`](#tag/Time-entry-prices) and [`Mileage entry prices`](#tag/Mileage-entry-prices) endpoints added.
| 16.0.0  | Changed parameter schema for [`mileages`](#operation/ApproveMileageEntries) and [`timeentries`](#operation/ApproveTimeEntries) approve endpoints.
| 15.0.0  | Added cost and sales accounts properties in [`activitygroups`](#tag/Activity-Groups) endpoints.
| 14.1.3  | - Added new filter for `IsAccessible` in [`activities`](#tag/Activities) endpoints. <br>- Added new filter for `IsBarred` in [`costtypes`](#tag/Cost-Types) endpoints.
| 14.1.2  | - Added input validations for [`activitygroups`](#tag/Activity-Groups). <br>- Updated description for [`projectgroups`](#operation/CreateProjectGroup) properties.
| 14.1.1  | Added input validations for [`projectgroups`](#operation/CreateProjectGroup).
| 14.1.0  | [`project-employees-count`](#operation/GetNumberOfProjectEmployees) endpoint added.                                                                                                                                                                                                                                             
| 14.0.0  | - [`project-activities`](#tag/Project-Activities) endpoints added. <br>- `projects/activities` have been deprecated.|
| 13.2.0  | [`costtypegroups`](#tag/Cost-Type-Groups) endpoints added.|
| 13.1.0  | [`costtypes`](#tag/Cost-Types) endpoints added.|
| 13.0.0  | - [`projectgroups`](#operation/CreateProjectGroup) POST endpoint added, `Number` made non-required,<br>- [`activitygroups`](#operation/CreateActivityGroup) POST endpoint added, `Number` made non-required.|
| 12.0.0  | [`projects`](#tag/Projects) `Number` made non-required.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 11.0.0  | [`employees`](#tag/Employees) `Number` made required.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 10.1.2  | API version number moved to the server URL.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 10.1.1  | - [`activities`](#operation/GetAllowedActivities) `employeeNumber` maximum value changed to 999999. <br>- [`projects`](#operation/GetPagedListOfProjectUnderEmployee) `employeeNumber` maximum value changed to 999999.                                                                                                                                                                                                                                                                                                                                                                                             |
| 10.1.0  | [`project-employees`](#operation/CreateProjectEmployee) POST endpoint added.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 10.0.0  | - [`activities`](#tag/Activities) POST and PUT endpoints added. <br>- [`activitygroups`](#tag/Activity-Groups) GET endpoints added. <br>- Object version field added to `activities`, `projectstatuses` and `projectgroups` endpoints.                                                                                                                                                                                                                                                                                                                                                                              |
| 9.0.0   | `Project related settings for employee` resource renamed as `Project employee`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 8.1.0   | [`project-customers`](#tag/Project-Customers) endpoints added.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 8.0.0   | - [`employeegroups`](#tag/Employee-groups) endpoints added: GET all paginated, GET count, POST and PUT. <br>- [`project-employeegroups`](#tag/Project-employee-groups) endpoints added: GET all paginated, GET all cursor-based, GET count, GET by number, POST and PUT. <br> - Object version field added to employee groups endpoints.                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 7.0.0   | [Projects related settings for employee](#tag/Project-employees) extended with new fields for Name, GroupNumber and IsBarred.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 6.0.0   | Readonly property `IsReconciled` added to `TimeEntries` endpoint.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 5.1.0   | [Project delete](#operation/DeleteProjectById) endpoint added.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 5.0.0   | - Project-related properties such as `isUser`, `userId`, `canApprove`, `canInvoice`, `employeeType` in `/employees` moved to `/project-employees`. <br>- Properties `lastUpdated`, `costPrice`, `salesPrice` and `invoicedtotal` in `/projects` changed to readonly.<br>- Property `date` in `/timeentries` changed to mandatory.<br>- Access permission to `/employees` changed to requiring access to `Sales`.<br>- PUT endpoints for `/timeentries/{number}`, `/employees/{number}`, `/employeeprojectrelatedsettings/{number}` have been deprecated and new ones without `{number}` in the URL have been added. |
| 4.0.0   | `project.CustomerNumber` made non-required, range check introduced.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 3.1.0   | Error messages of time entry approval improved, `timeEntry.IsApproved`, `mileage.IsApproved` and `mileage.IncludeApproval` made read-only.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 3.0.0   | `mileage.Date` made required. Verification for `mileage.EmployeeNumber` and `mileage.Distance` added.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 2.2.2   | Range check introduced in `projects.Number`, `employee.Number` and `employeeGroup.Number`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 2.2.1   | Employees PATCH endpoint deprecated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 2.2.0   | [`employeegroups/all`](#operation/GetAllEmployeeGroups) and [`employeegroups/{number}`](#operation/GetEmployeeGroupById) endpoints added.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 2.1.0   | [`/activities/allowed`](#operation/GetAllowedActivities) endpoint added to get allowed activities for an employee and project.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 2.0.0   | Open API released! Endpoints related to Projects module added.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

</details>

# TL;DR

**Add these three headers to your requests.**

| Header                | Value                      | What is this?                                                |
| :-------------------- | :------------------------- | :----------------------------------------------------------- |
| X-AppSecretToken      | YOUR_PRIVATE_TOKEN         | This identifies your app. This is your secret token. Try using the value `demo`. |
| X-AgreementGrantToken | YOUR_AGREEMENT_GRANT_TOKEN | This identifies the grant issued by an agreement, to allow your app to access the agreements data. Try using the value `demo`. |
| Content-Type          | application/json           | We’re a JSON based API. This tells us that you agree with us on using JSON. |

### Examples

#### jQuery

```javascript/jQuery
$.ajax({
    url: \"https://apis.e-conomic.com/api/v20.0.0/projects\",
    dataType: \"json\",
    headers: {
        'X-AppSecretToken': \"demo\",
        'X-AgreementGrantToken': \"demo\",
        'Content-Type': \"application/json\"
    },
    type: \"GET\"
})
    .always(function (data) {
    $(\"#output\").text(JSON.stringify(data, null, 4));
});
```

#### cURL

```curl
curl -H \"X-AppSecretToken: demo\" -H \"X-AgreementGrantToken: demo\" https://apis.e-conomic.com/api/v20.0.0/projects
```



# Introduction

Welcome to the **Visma e-conomic OpenAPI** documentation!

The e-conomic API is a document-based JSON REST API. 

For more in-depth information about e-conomic itself, please have a look at the e-copedia [http://wiki.e-conomic.dk](http://wiki.e-conomic.dk/).

## Usage

- **Generating a client** can easily be done using tools like [swagger-codegen](https://github.com/swagger-api/swagger-codegen) or others that work with [OpenAPI Specification](https://github.com/OAI/OpenAPI-Specification) specs.


## Versioning

API releases are versioned using a three-part versioning scheme: `{major version}.{minor version}.{patch version}`.

We broadly follow [Semantic Versioning](https://semver.org/) principles when versioning the API. The major version number is incremented when a breaking change occurs. 

The format is:

`/api/v{major version}.{minor version}.{patch version}/{resource-name}`

Each value of the above are integers and you should configure the specific version in each API call. 

An example could be: `/api/v2.2.1/projects`

To track the changes of versions, please see our [changelog](#section/Changelog).

We reserve the right to deprecate versions at intervals since this allows for moving into a friendly environment for you faster.

## Demo authentication

If you wish to try out the API before registering a developer agreement, you can do this by using the demo agreement, which mimics the authentication flow you will have to use when you create your app. All you have to do is specify HTTP header tokens `X-AgreementGrantToken: demo` and `X-AppSecretToken: demo`. Note however that you can only do GET requests with the demo agreement. If you want full access to our API's, you will need to register.

# Retrieving data

Our data is exposed as collections of items. Each item has many properties, with one property as a unique identifier, usually called `number` or `id`. You can always get a single item if you already know the unique identifier. In case the unique identifier is not known, you can always search the collection and retrieve an array of items that satisfy the search criteria, or retrieve only the count of items that satisfy the search criteria. When you search for items in a collection, you can always use filtering, sorting and pagination. When it comes to pagination, we offer two distinct approaches available on separate endpoints. You can read more about filtering, sorting and pagination in the following sections. 

## Filtering

Filtering is enabled on all collection endpoints but not on all properties.

Filtering on collections can be done using the query string parameter `filter`. A filter is made up of a set of predicates and follows a syntax inspired by mongoDB. A predicate is made up of a property name, an operator, and a value.

Example: `?filter=name$eq:Joe`

This matches all resources with the value Joe in the property name.

Predicates can be chained using either of the logical operators AND and OR.

Example: `?filter=name$eq:Joe$and:city$like:*port`

Filtering on strings is case insensitive.

#### Filterable properties
Information about what properties allow filtering and on what operators can be found in the property in the schema for the collection. Each property that allows filtering has the property `\"x-filterable\"` in combination with `operators` set. If you try to filter on something that isn’t allowed the server will respond with a status code 400.

#### Specifying Operator affinity
If you want to control the operator affinity then you can use parentheses.

An example is: `?filter=name$eq:Joe$and:(city$like:*port$or:age$lt:40)`

#### URL Encoding
URL parameter values should always be URL compatible. Always URL encode filter strings.

#### Filter Operators
The possible filtering operators are:

| Operator   | Syntax |
| --------   | ------ |
|Equals | $eq:|
|Not equals | $ne:|
|Greater than | $gt:|
|Greater than or equal | $gte:|
|Less than | $lt:|
|Less than or equal | $lte:|
|Substring match | $like:|
|And also | $and:|
|Or else | $or:|
|In | $in:|
|Not In | $nin:|

#### Substring matching

The `$like:` operator supports both using wildcards (*) and not using wildcards. If no wildcards are used, the expression is considered a `contains` expression and effectively becomes a filter with a wildcard at the start of the string and one at the end of the string. This operator is only allowed on some properties.

#### Escaping special characters in your filter
To not interfere with the parsing of the filter expression, certain escape sequences are necessary.

- “$” is escaped with “$$”
- “(” is escaped with “$(”
- “)” is escaped with “$)”
- “*” is escaped with “$*”
- “,” is escaped with “$,”
- “[” is escaped with “$[”
- “]” is escaped with “$]”

#### Using null values in your filter
Should you want to filter for the nonexistence of a property (i.e. null value) you can use the null escape sequence.

`$null:`

#### Using in and not in operators
To determine whether a specified value matches any value in (or not in) a list you filter using the `$in:` or `$nin:` operator. The list to filter by has to be enclosed in brackets and values separated by commas.

`customerNumber$in:[2,5,7,22,45]`


It is possible to also use the `$null:` keyword if you wish to include that in the filter. The max supported length of an array using the `$in:` or `$nin:` operator is 200.


## Sorting

Sorting on strings is case insensitive.

### Sort ascending

Sorting on collections can be done using the query string parameter ‘sort’.

```
?sort=name
```

### Sort descending

The default sort direction is ascending, but this can be turned by prepending a minus (-).

```
?sort=-name
```

### Sort by multiple properties

If you need to sort by multiple properties these can just be separated by commas. Mixing of directions is allowed.

```
?sort=-name,age
```

### Sort alphabetically

In certain cases, you might want to enforce that even numeric values are sorted alphabetically, so 1000 is less than 30. In those cases, you can prepend the sort property with a tilde (~).

```
?sort=~name
```

#### Sortable properties
Information about what properties are sortable can be found in the schema for the collection. Each property that allows sorting has the property `\"x-sortable\": true` set.


## Pagination

When it comes to retrieving a collection of items, you can use two distinct approaches:

* **Cursor-based pagination** (continued loading of items using a `cursor` as a query parameter to get the next page of items)
  * This is the recommended approach, and the one you should use by default.
  * The endpoint naming scheme is **\"Retrieve all `Items`\"**. (Usage: `/{ITEM}?cursor={CURSOR_VALUE}`)


* **Classic pagination** (limited functionality*. Specify `skippages` and `pagesize ` as query parameters to get a specific page of items)
  * You should only consider using classic pagination, if you rely on loading pages (i.e. for list views or table/grid-based UI's).
  * The endpoint naming scheme is **\"Retrieve a page of `Items`\"**. (Usage: `/{ITEM}/paged?skippages=0&pagesize=20`)  
    \\* It's important to note that there is a limit of 10.000 items using this approach. Any items outside of the first 10.000 items will not be loaded.

Please bear in mind that the two approaches are supported by **separate endpoints**. To use classic pagination, add `/paged` to your request URL.

If you need to know the total count of items that you can expect to get from your search, you can use a separate endpoint called **\"Retrieve the number of `Items`\"**.  
You can also use the result of this endpoint to calculate the pagination navigation buttons for a table/grid-based UI.


### Which approach should you use?
We highly recommend that you use cursor-based pagination because:
- It is more performant and offers much faster retrieval of items;
- It can be used for very large collections of many thousands or millions of items, whereas classic pagination is limited to only returning 10.000 results, everything else is ignored;  
  Classic pagination is only appropriate when you have an app with a table/grid-based UI.

### Cursor-based pagination

#### How it works

When you search for items in a large collection, the response will contain the first 1.000 items and a `cursor` that you can use in a subsequent request to get the next series of items. This way you can retrieve the next set of items only when needed (if 1.000 items suffice, you don't need to send a second request).

Please note that the cursor is currently the `id` of the first `item` on the next set and it should not be mistaken for the number of items which are yet to be displayed.
Also, if the cursor is not present in the response, it means that there are no more items in the results.

##### Real world example

I want to retrieve all projects.

1) I send a request to `https://apis.e-conomic.com/api/v20.0.0/projects`
   and get back an array of 1.000 projects, and a `cursor` with value `34781`


2) I send a request for the next items in the resulting collection:  
   `https://apis.e-conomic.com/api/v20.0.0/projects?cursor=34781`  
   and get back an array of 1.000 projects and a cursor with value `87695`


3) I send a request for the next items in the result:  
   `https://apis.e-conomic.com/api/v20.0.0/projects?cursor=87695`  
   and get back an array of 56 items and no cursor.  
   No cursor means I have retrieved all the projects, i.e. I have reached the end of the list.


### Classic pagination

If no parameters are used, the collection endpoint returns 20 items at a time. URL parameters allow you to increase this to up to 100 items or to skip pages if necessary.

##### Real world example

I want to show a grid with page size of 50 and pagination navigation buttons.

1) I send a request to see how many projects there are in the collection:  
   `https://apis.e-conomic.com/api/v20.0.0/projects/count`  
   I get the number of projects in the collection, `2056`, and I can calculate the number of pages to be 2056 divided by 50 = 40 with 6 as remainder, meaning I have 41 pages total. I can then use this to present the user the navigation buttons.


2) I send a request to retrieve the first page of projects that my user will see:  
   `https://apis.e-conomic.com/api/v20.0.0/projects/paged?pagesize=50&sort=name`  
   with this I get back an array of 50 projects, sorted alphabetically by the project name.


3) Now if the user wants to see page number 6, I'll send a new request, skipping the first 5 pages to get the projects from page number 6:  
   `https://apis.e-conomic.com/api/v20.0.0/projects/paged?pagesize=50&skippages=5&sort=name`  
   I get back an array of 50 projects, that belong to page number 6 when sorting alphabetically by the project name.



### Number of items in a collection

As mentioned before we offer endpoint to get the count of items in the collection. You can also use this info for calculation of pagination navigation in case of classic pagination.

Example `https://apis.e-conomic.com/api/v20.0.0/projects/count`


## HTTP Status Codes

The Open API returns these HTTP status codes.

| Code | Text                   | Description                                                  |
| :--- | :--------------------- | :----------------------------------------------------------- |
| 200  | OK                     | Everything is OK                                             |
| 201  | Created                | When you create resources, this is what you get. This will be accompanied by the created resource in the body and a location header with a link to the created resource. |
| 204  | No Content             | In certain cases there is nothing to return. So we will let you know by returning a 204. |
| 400  | Bad Request            | The request you made was somehow malformed. A malformed request could be failed validation on creation or updating. If you try to filter on something that isn’t filterable this is also what you’ll see. Whenever possible we will also try to include a developer hint to help you get around this issue. |
| 401  | Unauthorized           | The credentials you supplied us with weren’t correct, or perhaps you forgot them altogether. If an agreement has revoked the grant they gave your app, this is what you will see. |
| 403  | Forbidden              | You won’t necessarily have access to everything. So even though you were authorized we might still deny access to certain resources. This depends on the roles asked for when the grant was issued. |
| 404  | Not Found              | This is returned when you try to request something that doesn’t exist. This could be a resource that has been deleted or just a URL you tried to hack. If you see a lot of these, it could be an indication that you aren’t using the links provided by the API. You should never need to concatenate any URLs. The API should provide you with the links needed. |
| 405  | Method Not Allowed     | Not all endpoints support all HTTP methods. If you try issue a PUT request to a collection resource this is what you get. |
| 415  | Unsupported Media Type | Our API is a JSON api. If you ask us to give you anything else, we give you this, and tell you why in the JSON body of the response. |
| 500  | Internal Server Error  | We don’t like to see these, and they are flagged in our logs. When you see this, something went wrong on our end. Either try again, or contact our support. |


## Required and Readonly Properties

Since OpenAPI allows client generation based on the specification, we decided to use the same model/schema in our for both read and write endpoints where possible.

This led us to chose not to have the Id/Number in the URL parameter for PUT requests, but to use the one from the body, so there is no confusion.

When a property is marked as `required` it means you need to provide a value on each POST and PUT requests.

When a property is marked as `readonly` it means you should provide the same value you get in the GET requests, or do not send the property in the JSON at all (skip it).

## Custom resource encoding

For some resource ids (the direct URL path to a resource) the question of non-alphanumeric characters must be solved in REST APIs by either encoding or replacement to ensure URL compatibility.

In the e-conomic REST API a subset of non-alphanumeric characters are replaced using a custom scheme for resource URLs:

| Character        | Replacement |
| :--------------- | :---------- |
| “<”              | *0*         |
| “>”              | *1*         |
| “*”              | *2*         |
| “%”              | *3*         |
| “:”              | *4*         |
| “&”              | *5*         |
| “/”              | *6*         |
| “\\”              | *7*         |
| “_”              | *8*         |
| “ ” (whitespace) | *9*         |
| “?”              | *10*        |
| “.”              | *11*        |
| “#”              | *12*        |
| “+”              | *13*        |

Example: Product “My Awesome Product_Discount5%” Resource URL (self): https://apis.e-conomic.com/products/My_9_Awesome_9_Product_8_Discount5_3_

All other non-alphanumeric characters in resource URLs are standard URL encoded. Please refer to standard URL encoding for characters not mentioned above.

## Implementation specifics

Helpful details to know when implementing e-conomic REST.

### Booleans

Booleans should only be expected to be represented in responses when true. A false boolean is omitted from response body. The same logic applies to write operations such as POST and PUT.

### Null values

Null values are omitted from the response body.

### Nulling

We do not generally accept null as a value and a validation exception should be expected. To null a property you must exclude it from your JSON on the write operation.

## Object version

ObjectVersion is the mechanism that enforces updates only on latest state of an object.
ObjectVersion property is mandatory in Put Requests.
ObjectVersion property is retrieved on Get Request and needs to be included in Put Request.
If object was modified between Get and Put requests, Put request will fail with error code `409 Conflict`

```
{
  \"message\": \"Update conflict. Version does not match.\",
  \"developerHint\": \"The resource has been updated by another user. Retrieve the resource/object and try the update again. This is needed in order to prevent you from rolling back another user's update.\",
  \"logId\": \"09580053-1141-4e7f-85e1-bed8600e0278\",
  \"logTimeUtc\": \"2021-11-04T09:07:56\",
  \"property\": \"version\"
}
```

## Custom extensions in OpenAPI specification

In the specification file, there are some custom extensions that developers can make use of when consuming endpoints. 
Those extensions are always prefixed by `x-`.

1) `x-required-roles`: The list of roles that are required for each group of endpoints.
2) `x-error-codes`: The list of error codes that are potentially returned from each group of endpoints.


  For more information, please visit [https://www.e-conomic.com/](https://www.e-conomic.com/)

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
  <version>v20.0.0</version>
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
     implementation "org.openapitools:openapi-java-client:v20.0.0"
  }
```

### Others

At first generate the JAR by executing:

```shell
mvn clean package
```

Then manually install the following JARs:

* `target/openapi-java-client-v20.0.0.jar`
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
import org.openapitools.client.api.ActivitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apis.e-conomic.com/api/v20.0.0");
    
    // Configure API key authorization: X-AgreementGrantToken
    ApiKeyAuth X-AgreementGrantToken = (ApiKeyAuth) defaultClient.getAuthentication("X-AgreementGrantToken");
    X-AgreementGrantToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AgreementGrantToken.setApiKeyPrefix("Token");

    // Configure API key authorization: X-AppSecretToken
    ApiKeyAuth X-AppSecretToken = (ApiKeyAuth) defaultClient.getAuthentication("X-AppSecretToken");
    X-AppSecretToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AppSecretToken.setApiKeyPrefix("Token");

    ActivitiesApi apiInstance = new ActivitiesApi(defaultClient);
    Activity activity = new Activity(); // Activity | 
    try {
      CreatedResult result = apiInstance.createActivity(activity);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivitiesApi#createActivity");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

## Documentation for API Endpoints

All URIs are relative to *https://apis.e-conomic.com/api/v20.0.0*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ActivitiesApi* | [**createActivity**](docs/ActivitiesApi.md#createActivity) | **POST** /activities | Create a single Activity
*ActivitiesApi* | [**getActivityById**](docs/ActivitiesApi.md#getActivityById) | **GET** /activities/{number} | Retrieve single Activity
*ActivitiesApi* | [**getAllActivities**](docs/ActivitiesApi.md#getAllActivities) | **GET** /activities | Retrieve all Activities
*ActivitiesApi* | [**getAllowedActivities**](docs/ActivitiesApi.md#getAllowedActivities) | **GET** /activities/allowed | Retrieve allowed activities
*ActivitiesApi* | [**getNumberOfActivities**](docs/ActivitiesApi.md#getNumberOfActivities) | **GET** /activities/count | Retrieve the number of Activities
*ActivitiesApi* | [**getPageOfActivities**](docs/ActivitiesApi.md#getPageOfActivities) | **GET** /activities/paged | Retrieve a page of Activities
*ActivitiesApi* | [**updateActivity**](docs/ActivitiesApi.md#updateActivity) | **PUT** /activities | Update a single Activity
*ActivityGroupsApi* | [**createActivityGroup**](docs/ActivityGroupsApi.md#createActivityGroup) | **POST** /activitygroups | Create a single Activity Group
*ActivityGroupsApi* | [**getActivityGroupById**](docs/ActivityGroupsApi.md#getActivityGroupById) | **GET** /activitygroups/{number} | Retrieve single Activity Group
*ActivityGroupsApi* | [**getAllActivityGroups**](docs/ActivityGroupsApi.md#getAllActivityGroups) | **GET** /activitygroups | Retrieve all Activity Groups
*ActivityGroupsApi* | [**getNumberOfActivityGroups**](docs/ActivityGroupsApi.md#getNumberOfActivityGroups) | **GET** /activitygroups/count | Retrieve the number of Activity Groups
*ActivityGroupsApi* | [**getPageOfActivityGroups**](docs/ActivityGroupsApi.md#getPageOfActivityGroups) | **GET** /activitygroups/paged | Retrieve a page of Activity Groups
*CostTypeGroupsApi* | [**getAllCostTypeGroups**](docs/CostTypeGroupsApi.md#getAllCostTypeGroups) | **GET** /costtypegroups | Retrieve all Cost Type Groups
*CostTypeGroupsApi* | [**getCostTypeGroupById**](docs/CostTypeGroupsApi.md#getCostTypeGroupById) | **GET** /costtypegroups/{number} | Retrieve single Cost Type Group
*CostTypeGroupsApi* | [**getNumberOfCostTypeGroups**](docs/CostTypeGroupsApi.md#getNumberOfCostTypeGroups) | **GET** /costtypegroups/count | Retrieve the number of Cost Type Groups
*CostTypeGroupsApi* | [**getPageOfCostTypeGroups**](docs/CostTypeGroupsApi.md#getPageOfCostTypeGroups) | **GET** /costtypegroups/paged | Retrieve a page of Cost Type Groups
*CostTypesApi* | [**getAllCostTypes**](docs/CostTypesApi.md#getAllCostTypes) | **GET** /costtypes | Retrieve all Cost Types
*CostTypesApi* | [**getCostTypeById**](docs/CostTypesApi.md#getCostTypeById) | **GET** /costtypes/{number} | Retrieve single Cost Type
*CostTypesApi* | [**getNumberOfCostTypes**](docs/CostTypesApi.md#getNumberOfCostTypes) | **GET** /costtypes/count | Retrieve the number of Cost Types
*CostTypesApi* | [**getPageOfCostTypes**](docs/CostTypesApi.md#getPageOfCostTypes) | **GET** /costtypes/paged | Retrieve a page of Cost Types
*EmployeeGroupsApi* | [**createEmployeeGroup**](docs/EmployeeGroupsApi.md#createEmployeeGroup) | **POST** /employeegroups | Create a single Employee group
*EmployeeGroupsApi* | [**deleteEmployeeGroupById**](docs/EmployeeGroupsApi.md#deleteEmployeeGroupById) | **DELETE** /employeegroups/{number} | Delete single Employee group
*EmployeeGroupsApi* | [**getAllEmployeeGroups**](docs/EmployeeGroupsApi.md#getAllEmployeeGroups) | **GET** /employeegroups | Retrieve all Employee groups
*EmployeeGroupsApi* | [**getEmployeeGroupById**](docs/EmployeeGroupsApi.md#getEmployeeGroupById) | **GET** /employeegroups/{number} | Retrieve single Employee group
*EmployeeGroupsApi* | [**getNumberOfEmployeeGroups**](docs/EmployeeGroupsApi.md#getNumberOfEmployeeGroups) | **GET** /employeegroups/count | Retrieve the number of Employee groups
*EmployeeGroupsApi* | [**getPageOfEmployeeGroups**](docs/EmployeeGroupsApi.md#getPageOfEmployeeGroups) | **GET** /employeegroups/paged | Retrieve a page of Employee groups
*EmployeeGroupsApi* | [**updateEmployeeGroup**](docs/EmployeeGroupsApi.md#updateEmployeeGroup) | **PUT** /employeegroups | Update a single Employee group
*EmployeesApi* | [**createEmployee**](docs/EmployeesApi.md#createEmployee) | **POST** /employees | Create a single Employee
*EmployeesApi* | [**deleteEmployeeById**](docs/EmployeesApi.md#deleteEmployeeById) | **DELETE** /employees/{number} | Delete single Employee
*EmployeesApi* | [**getAllEmployees**](docs/EmployeesApi.md#getAllEmployees) | **GET** /employees | Retrieve all Employees
*EmployeesApi* | [**getEmployeeById**](docs/EmployeesApi.md#getEmployeeById) | **GET** /employees/{number} | Retrieve single Employee
*EmployeesApi* | [**getNumberOfEmployees**](docs/EmployeesApi.md#getNumberOfEmployees) | **GET** /employees/count | Retrieve the number of Employees
*EmployeesApi* | [**getPageOfEmployees**](docs/EmployeesApi.md#getPageOfEmployees) | **GET** /employees/paged | Retrieve a page of Employees
*EmployeesApi* | [**updateEmployee**](docs/EmployeesApi.md#updateEmployee) | **PUT** /employees | Update a single Employee
*MileageEntriesApi* | [**approveMileageEntries_0**](docs/MileageEntriesApi.md#approveMileageEntries_0) | **POST** /mileages/approve | Approve a list of Mileage entries
*MileageEntriesApi* | [**createMileage**](docs/MileageEntriesApi.md#createMileage) | **POST** /mileages | Create a single Mileage entry
*MileageEntriesApi* | [**deleteMileageById**](docs/MileageEntriesApi.md#deleteMileageById) | **DELETE** /mileages/{number} | Delete single Mileage entry
*MileageEntriesApi* | [**getAllMileageEntries**](docs/MileageEntriesApi.md#getAllMileageEntries) | **GET** /mileages | Retrieve all Mileage entries
*MileageEntriesApi* | [**getMileageById**](docs/MileageEntriesApi.md#getMileageById) | **GET** /mileages/{number} | Retrieve single Mileage entry
*MileageEntriesApi* | [**getNumberOfMileageEntries**](docs/MileageEntriesApi.md#getNumberOfMileageEntries) | **GET** /mileages/count | Retrieve the number of Mileage entries
*MileageEntriesApi* | [**getPageOfMileageEntries**](docs/MileageEntriesApi.md#getPageOfMileageEntries) | **GET** /mileages/paged | Retrieve a page of Mileage entries
*MileageEntriesApi* | [**updateMileage**](docs/MileageEntriesApi.md#updateMileage) | **PUT** /mileages | Update a single Mileage entry
*MileageEntryPricesApi* | [**getAllMileageEntryPrices**](docs/MileageEntryPricesApi.md#getAllMileageEntryPrices) | **GET** /mileageprices | Retrieve all Mileage entry prices
*MileageEntryPricesApi* | [**getMileagePricesById**](docs/MileageEntryPricesApi.md#getMileagePricesById) | **GET** /mileageprices/{number} | Retrieve single Mileage entry prices
*MileageEntryPricesApi* | [**getPageOfMileageEntryPrices**](docs/MileageEntryPricesApi.md#getPageOfMileageEntryPrices) | **GET** /mileageprices/paged | Retrieve a page of Mileage entry prices
*MileagesApi* | [**approveMileageEntries**](docs/MileagesApi.md#approveMileageEntries) | **POST** /mileages/approve | Approve a list of Mileage entries
*ProjectActivitiesApi* | [**createProjectActivity**](docs/ProjectActivitiesApi.md#createProjectActivity) | **POST** /project-activities | Create a single Project Activity
*ProjectActivitiesApi* | [**deleteProjectActivityById**](docs/ProjectActivitiesApi.md#deleteProjectActivityById) | **DELETE** /project-activities/{number} | Delete single Project Activity
*ProjectActivitiesApi* | [**getAllProjectActivities**](docs/ProjectActivitiesApi.md#getAllProjectActivities) | **GET** /project-activities | Retrieve all Project Activities
*ProjectActivitiesApi* | [**getNumberOfProjectActivities**](docs/ProjectActivitiesApi.md#getNumberOfProjectActivities) | **GET** /project-activities/count | Retrieve the number of Project Activities
*ProjectActivitiesApi* | [**getPageOfProjectActivities**](docs/ProjectActivitiesApi.md#getPageOfProjectActivities) | **GET** /project-activities/paged | Retrieve a page of Project Activities
*ProjectActivitiesApi* | [**getProjectActivityById**](docs/ProjectActivitiesApi.md#getProjectActivityById) | **GET** /project-activities/{number} | Retrieve single Project Activity
*ProjectActivitiesApi* | [**updateProjectActivity**](docs/ProjectActivitiesApi.md#updateProjectActivity) | **PUT** /project-activities | Update a single Project Activity
*ProjectCustomersApi* | [**getAllProjectCustomers**](docs/ProjectCustomersApi.md#getAllProjectCustomers) | **GET** /project-customers | Retrieve all Project Customers
*ProjectCustomersApi* | [**getNumberOfProjectCustomers**](docs/ProjectCustomersApi.md#getNumberOfProjectCustomers) | **GET** /project-customers/count | Retrieve the number of Project Customers
*ProjectCustomersApi* | [**getPageOfProjectCustomers**](docs/ProjectCustomersApi.md#getPageOfProjectCustomers) | **GET** /project-customers/paged | Retrieve a page of Project Customers
*ProjectCustomersApi* | [**getProjectCustomerById**](docs/ProjectCustomersApi.md#getProjectCustomerById) | **GET** /project-customers/{number} | Retrieve single Project Customer
*ProjectEmployeeGroupsApi* | [**createProjectEmployeeGroup**](docs/ProjectEmployeeGroupsApi.md#createProjectEmployeeGroup) | **POST** /project-employeegroups | Create a single Project employee group
*ProjectEmployeeGroupsApi* | [**deleteProjectEmployeeGroupById**](docs/ProjectEmployeeGroupsApi.md#deleteProjectEmployeeGroupById) | **DELETE** /project-employeegroups/{number} | Delete single Project employee group
*ProjectEmployeeGroupsApi* | [**getAllProjectEmployeeGroups**](docs/ProjectEmployeeGroupsApi.md#getAllProjectEmployeeGroups) | **GET** /project-employeegroups | Retrieve all Project employee groups
*ProjectEmployeeGroupsApi* | [**getNumberOfProjectEmployeeGroups**](docs/ProjectEmployeeGroupsApi.md#getNumberOfProjectEmployeeGroups) | **GET** /project-employeegroups/count | Retrieve the number of Project employee groups
*ProjectEmployeeGroupsApi* | [**getPageOfProjectEmployeeGroups**](docs/ProjectEmployeeGroupsApi.md#getPageOfProjectEmployeeGroups) | **GET** /project-employeegroups/paged | Retrieve a page of Project employee groups
*ProjectEmployeeGroupsApi* | [**getProjectEmployeeGroupById**](docs/ProjectEmployeeGroupsApi.md#getProjectEmployeeGroupById) | **GET** /project-employeegroups/{number} | Retrieve single Project employee group
*ProjectEmployeeGroupsApi* | [**updateProjectEmployeeGroup**](docs/ProjectEmployeeGroupsApi.md#updateProjectEmployeeGroup) | **PUT** /project-employeegroups | Update a single Project employee group
*ProjectEmployeesApi* | [**createProjectEmployee**](docs/ProjectEmployeesApi.md#createProjectEmployee) | **POST** /project-employees | Create a single Project employee
*ProjectEmployeesApi* | [**deleteProjectEmployeeById**](docs/ProjectEmployeesApi.md#deleteProjectEmployeeById) | **DELETE** /project-employees/{number} | Delete single Project employee
*ProjectEmployeesApi* | [**getAllProjectEmployees**](docs/ProjectEmployeesApi.md#getAllProjectEmployees) | **GET** /project-employees | Retrieve all Project employees
*ProjectEmployeesApi* | [**getNumberOfProjectEmployees**](docs/ProjectEmployeesApi.md#getNumberOfProjectEmployees) | **GET** /project-employees/count | Retrieve the number of Project employees
*ProjectEmployeesApi* | [**getPageOfProjectEmployees**](docs/ProjectEmployeesApi.md#getPageOfProjectEmployees) | **GET** /project-employees/paged | Retrieve a page of Project employees
*ProjectEmployeesApi* | [**getProjectEmployeeById**](docs/ProjectEmployeesApi.md#getProjectEmployeeById) | **GET** /project-employees/{number} | Retrieve single Project employee
*ProjectEmployeesApi* | [**updateProjectEmployee**](docs/ProjectEmployeesApi.md#updateProjectEmployee) | **PUT** /project-employees | Update a single Project employee
*ProjectGroupsApi* | [**createProjectGroup**](docs/ProjectGroupsApi.md#createProjectGroup) | **POST** /projectgroups | Create a single Project Group
*ProjectGroupsApi* | [**getAllProjectGroups**](docs/ProjectGroupsApi.md#getAllProjectGroups) | **GET** /projectgroups | Retrieve all Project Groups
*ProjectGroupsApi* | [**getNumberOfProjectGroups**](docs/ProjectGroupsApi.md#getNumberOfProjectGroups) | **GET** /projectgroups/count | Retrieve the number of Project Groups
*ProjectGroupsApi* | [**getPageOfProjectGroups**](docs/ProjectGroupsApi.md#getPageOfProjectGroups) | **GET** /projectgroups/paged | Retrieve a page of Project Groups
*ProjectGroupsApi* | [**getProjectGroupById**](docs/ProjectGroupsApi.md#getProjectGroupById) | **GET** /projectgroups/{number} | Retrieve single Project Group
*ProjectStatusesApi* | [**getAllProjectStatuses**](docs/ProjectStatusesApi.md#getAllProjectStatuses) | **GET** /projectstatuses | Retrieve all Project Statuses
*ProjectStatusesApi* | [**getNumberOfProjectStatuses**](docs/ProjectStatusesApi.md#getNumberOfProjectStatuses) | **GET** /projectstatuses/count | Retrieve the number of Project Statuses
*ProjectStatusesApi* | [**getPageOfProjectStatuses**](docs/ProjectStatusesApi.md#getPageOfProjectStatuses) | **GET** /projectstatuses/paged | Retrieve a page of Project Statuses
*ProjectStatusesApi* | [**getProjectStatusById**](docs/ProjectStatusesApi.md#getProjectStatusById) | **GET** /projectstatuses/{number} | Retrieve single Project Status
*ProjectsApi* | [**createProject**](docs/ProjectsApi.md#createProject) | **POST** /projects | Create a single Project
*ProjectsApi* | [**deleteProjectById**](docs/ProjectsApi.md#deleteProjectById) | **DELETE** /projects/{number} | Delete single Project
*ProjectsApi* | [**getAllProjects**](docs/ProjectsApi.md#getAllProjects) | **GET** /projects | Retrieve all Projects
*ProjectsApi* | [**getNumberOfProjects**](docs/ProjectsApi.md#getNumberOfProjects) | **GET** /projects/count | Retrieve the number of Projects
*ProjectsApi* | [**getPageOfProjects**](docs/ProjectsApi.md#getPageOfProjects) | **GET** /projects/paged | Retrieve a page of Projects
*ProjectsApi* | [**getPagedListOfProjectUnderEmployee**](docs/ProjectsApi.md#getPagedListOfProjectUnderEmployee) | **GET** /projects/allowed | Retrieve the allowed projects that employee can register an entry on.
*ProjectsApi* | [**getProjectById**](docs/ProjectsApi.md#getProjectById) | **GET** /projects/{number} | Retrieve single Project
*ProjectsApi* | [**updateProject**](docs/ProjectsApi.md#updateProject) | **PUT** /projects | Update a single Project
*TimeEntriesApi* | [**approveTimeEntries**](docs/TimeEntriesApi.md#approveTimeEntries) | **POST** /timeentries/approve | Approve a list of Time entries
*TimeEntriesApi* | [**approveTimeEntries_0**](docs/TimeEntriesApi.md#approveTimeEntries_0) | **POST** /timeentries/approve | Approve a list of Time entries
*TimeEntriesApi* | [**createTimeEntry**](docs/TimeEntriesApi.md#createTimeEntry) | **POST** /timeentries | Create a single Time entry
*TimeEntriesApi* | [**deleteTimeEntryById**](docs/TimeEntriesApi.md#deleteTimeEntryById) | **DELETE** /timeentries/{number} | Delete single Time entry
*TimeEntriesApi* | [**getAllTimeEntries**](docs/TimeEntriesApi.md#getAllTimeEntries) | **GET** /timeentries | Retrieve all Time entries
*TimeEntriesApi* | [**getNumberOfTimeEntries**](docs/TimeEntriesApi.md#getNumberOfTimeEntries) | **GET** /timeentries/count | Retrieve the number of Time entries
*TimeEntriesApi* | [**getPageOfTimeEntries**](docs/TimeEntriesApi.md#getPageOfTimeEntries) | **GET** /timeentries/paged | Retrieve a page of Time entries
*TimeEntriesApi* | [**getTimeEntryById**](docs/TimeEntriesApi.md#getTimeEntryById) | **GET** /timeentries/{number} | Retrieve single Time entry
*TimeEntriesApi* | [**updateTimeEntry**](docs/TimeEntriesApi.md#updateTimeEntry) | **PUT** /timeentries | Update a single Time entry
*TimeEntryPricesApi* | [**getAllTimeEntryPrices**](docs/TimeEntryPricesApi.md#getAllTimeEntryPrices) | **GET** /timeentryprices | Retrieve all Time entry prices
*TimeEntryPricesApi* | [**getPageOfTimeEntryPrices**](docs/TimeEntryPricesApi.md#getPageOfTimeEntryPrices) | **GET** /timeentryprices/paged | Retrieve a page of Time entry prices
*TimeEntryPricesApi* | [**getTimeEntryPricesById**](docs/TimeEntryPricesApi.md#getTimeEntryPricesById) | **GET** /timeentryprices/{number} | Retrieve single Time entry prices


## Documentation for Models

 - [Activity](docs/Activity.md)
 - [ActivityCursorResults](docs/ActivityCursorResults.md)
 - [ActivityGroup](docs/ActivityGroup.md)
 - [ActivityGroupCursorResults](docs/ActivityGroupCursorResults.md)
 - [ActivityGroupType](docs/ActivityGroupType.md)
 - [CostGroupType](docs/CostGroupType.md)
 - [CostType](docs/CostType.md)
 - [CostTypeCursorResults](docs/CostTypeCursorResults.md)
 - [CostTypeGroup](docs/CostTypeGroup.md)
 - [CostTypeGroupCursorResults](docs/CostTypeGroupCursorResults.md)
 - [CreatedResult](docs/CreatedResult.md)
 - [Employee](docs/Employee.md)
 - [EmployeeCursorResults](docs/EmployeeCursorResults.md)
 - [EmployeeGroup](docs/EmployeeGroup.md)
 - [EmployeeGroupCursorResults](docs/EmployeeGroupCursorResults.md)
 - [EmployeeType](docs/EmployeeType.md)
 - [Error](docs/Error.md)
 - [Mileage](docs/Mileage.md)
 - [MileageCursorResults](docs/MileageCursorResults.md)
 - [MileageNumbersCollection](docs/MileageNumbersCollection.md)
 - [MileagePrices](docs/MileagePrices.md)
 - [MileagePricesCursorResults](docs/MileagePricesCursorResults.md)
 - [OngoingAccountType](docs/OngoingAccountType.md)
 - [Project](docs/Project.md)
 - [ProjectActivity](docs/ProjectActivity.md)
 - [ProjectActivityCursorResults](docs/ProjectActivityCursorResults.md)
 - [ProjectCursorResults](docs/ProjectCursorResults.md)
 - [ProjectCustomer](docs/ProjectCustomer.md)
 - [ProjectCustomerCursorResults](docs/ProjectCustomerCursorResults.md)
 - [ProjectEmployee](docs/ProjectEmployee.md)
 - [ProjectEmployeeCursorResults](docs/ProjectEmployeeCursorResults.md)
 - [ProjectEmployeeGroup](docs/ProjectEmployeeGroup.md)
 - [ProjectEmployeeGroupCursorResults](docs/ProjectEmployeeGroupCursorResults.md)
 - [ProjectGroup](docs/ProjectGroup.md)
 - [ProjectGroupCursorResults](docs/ProjectGroupCursorResults.md)
 - [ProjectGroupType](docs/ProjectGroupType.md)
 - [ProjectStatus](docs/ProjectStatus.md)
 - [ProjectStatusCursorResults](docs/ProjectStatusCursorResults.md)
 - [ProjectStatusType](docs/ProjectStatusType.md)
 - [TimeEntry](docs/TimeEntry.md)
 - [TimeEntryCursorResults](docs/TimeEntryCursorResults.md)
 - [TimeEntryNumbersCollection](docs/TimeEntryNumbersCollection.md)
 - [TimeEntryPrices](docs/TimeEntryPrices.md)
 - [TimeEntryPricesCursorResults](docs/TimeEntryPricesCursorResults.md)


<a id="documentation-for-authorization"></a>
## Documentation for Authorization


Authentication schemes defined for the API:
<a id="X-AgreementGrantToken"></a>
### X-AgreementGrantToken

- **Type**: API key
- **API key parameter name**: X-AgreementGrantToken
- **Location**: HTTP header

<a id="X-AppSecretToken"></a>
### X-AppSecretToken

- **Type**: API key
- **API key parameter name**: X-AppSecretToken
- **Location**: HTTP header


## Recommendation

It's recommended to create an instance of `ApiClient` per thread in a multithreaded environment to avoid any potential issues.

## Author

api@e-conomic.com

