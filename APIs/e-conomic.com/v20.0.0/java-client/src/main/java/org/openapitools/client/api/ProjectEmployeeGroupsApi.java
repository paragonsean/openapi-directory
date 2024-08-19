/*
 * Visma e-conomic OpenAPI
 * # Changelog    <details>    <summary>Click to see changelog.</summary>    | Version | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |  |---------| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |  | 20.0.0  | Customer contacts and delivery locations endpoints deprecated. You can find the same enpoints in [`Customers API`](https://apis.e-conomic.com/#Customers)   | 19.0.0  | Page-based endpoints were moved under /paged url and cursor-based endpoints dropped the /all.  | 18.0.0  | Added isDeleted flag to [`customer-contacts`](#tag/Customer-contacts) and included deleted contacts in the response. <br> Deleted contacts can be used for history purposes, but cannot be set as reference persons on sales documents. <br> In previous versions only customer-contacts/id returns deleted contacts as well.  | 17.0.2  | `TimeEntryEmployeeNumberCannotBeUpdated` and `MileageEmployeeNumberCannotBeUpdated` error codes removed. The change affects all versions, but we bumped the version for transparency.  | 17.0.1  | New custom [`OpenAPI extension`](#section/Retrieving-data/Custom-extensions-in-OpenAPI-specification) added in the specification: `x-error-codes`. Existing `x-required-roles` extension converted to an array of strings.  | 17.0.0  | Improved the error model. Added `code` and `property` fields to the model. `code` represents the error code. `property` is the field name on which the input validation failed.  | 16.4.0  | [`customer-deliverylocations`](#tag/Customer-delivery-locations) endpoints added.  | 16.3.0  | [`customer-contacts`](#tag/Customer-contacts) endpoints added.    | 16.2.2  | Added input validations for required string properties, if a string property is required it can't be empty, it should contain at least 1 character.  | 16.2.1  | Error codes extended for [`mileages`](#tag/Mileage-entries) and [`timeentries`](#tag/Time-entries). Affects all the exisiting versions.  | 16.2.0  | - [`employeegroups`](#operation/DeleteEmployeeGroupById) DELETE endpoint added. <br>- [`employees`](#operation/DeleteEmployeeById) DELETE endpoint added. <br>- [`project-employeegroups`](#operation/DeleteProjectEmployeeGroupById) DELETE endpoint added. <br>- [`project-employees`](#operation/DeleteProjectEmployeeById) DELETE endpoint added.  | 16.1.0  | [`Time entry prices`](#tag/Time-entry-prices) and [`Mileage entry prices`](#tag/Mileage-entry-prices) endpoints added.  | 16.0.0  | Changed parameter schema for [`mileages`](#operation/ApproveMileageEntries) and [`timeentries`](#operation/ApproveTimeEntries) approve endpoints.  | 15.0.0  | Added cost and sales accounts properties in [`activitygroups`](#tag/Activity-Groups) endpoints.  | 14.1.3  | - Added new filter for `IsAccessible` in [`activities`](#tag/Activities) endpoints. <br>- Added new filter for `IsBarred` in [`costtypes`](#tag/Cost-Types) endpoints.  | 14.1.2  | - Added input validations for [`activitygroups`](#tag/Activity-Groups). <br>- Updated description for [`projectgroups`](#operation/CreateProjectGroup) properties.  | 14.1.1  | Added input validations for [`projectgroups`](#operation/CreateProjectGroup).  | 14.1.0  | [`project-employees-count`](#operation/GetNumberOfProjectEmployees) endpoint added.                                                                                                                                                                                                                                               | 14.0.0  | - [`project-activities`](#tag/Project-Activities) endpoints added. <br>- `projects/activities` have been deprecated.|  | 13.2.0  | [`costtypegroups`](#tag/Cost-Type-Groups) endpoints added.|  | 13.1.0  | [`costtypes`](#tag/Cost-Types) endpoints added.|  | 13.0.0  | - [`projectgroups`](#operation/CreateProjectGroup) POST endpoint added, `Number` made non-required,<br>- [`activitygroups`](#operation/CreateActivityGroup) POST endpoint added, `Number` made non-required.|  | 12.0.0  | [`projects`](#tag/Projects) `Number` made non-required.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |  | 11.0.0  | [`employees`](#tag/Employees) `Number` made required.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |  | 10.1.2  | API version number moved to the server URL.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |  | 10.1.1  | - [`activities`](#operation/GetAllowedActivities) `employeeNumber` maximum value changed to 999999. <br>- [`projects`](#operation/GetPagedListOfProjectUnderEmployee) `employeeNumber` maximum value changed to 999999.                                                                                                                                                                                                                                                                                                                                                                                             |  | 10.1.0  | [`project-employees`](#operation/CreateProjectEmployee) POST endpoint added.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |  | 10.0.0  | - [`activities`](#tag/Activities) POST and PUT endpoints added. <br>- [`activitygroups`](#tag/Activity-Groups) GET endpoints added. <br>- Object version field added to `activities`, `projectstatuses` and `projectgroups` endpoints.                                                                                                                                                                                                                                                                                                                                                                              |  | 9.0.0   | `Project related settings for employee` resource renamed as `Project employee`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |  | 8.1.0   | [`project-customers`](#tag/Project-Customers) endpoints added.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |  | 8.0.0   | - [`employeegroups`](#tag/Employee-groups) endpoints added: GET all paginated, GET count, POST and PUT. <br>- [`project-employeegroups`](#tag/Project-employee-groups) endpoints added: GET all paginated, GET all cursor-based, GET count, GET by number, POST and PUT. <br> - Object version field added to employee groups endpoints.                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |  | 7.0.0   | [Projects related settings for employee](#tag/Project-employees) extended with new fields for Name, GroupNumber and IsBarred.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |  | 6.0.0   | Readonly property `IsReconciled` added to `TimeEntries` endpoint.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |  | 5.1.0   | [Project delete](#operation/DeleteProjectById) endpoint added.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |  | 5.0.0   | - Project-related properties such as `isUser`, `userId`, `canApprove`, `canInvoice`, `employeeType` in `/employees` moved to `/project-employees`. <br>- Properties `lastUpdated`, `costPrice`, `salesPrice` and `invoicedtotal` in `/projects` changed to readonly.<br>- Property `date` in `/timeentries` changed to mandatory.<br>- Access permission to `/employees` changed to requiring access to `Sales`.<br>- PUT endpoints for `/timeentries/{number}`, `/employees/{number}`, `/employeeprojectrelatedsettings/{number}` have been deprecated and new ones without `{number}` in the URL have been added. |  | 4.0.0   | `project.CustomerNumber` made non-required, range check introduced.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |  | 3.1.0   | Error messages of time entry approval improved, `timeEntry.IsApproved`, `mileage.IsApproved` and `mileage.IncludeApproval` made read-only.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |  | 3.0.0   | `mileage.Date` made required. Verification for `mileage.EmployeeNumber` and `mileage.Distance` added.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |  | 2.2.2   | Range check introduced in `projects.Number`, `employee.Number` and `employeeGroup.Number`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |  | 2.2.1   | Employees PATCH endpoint deprecated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |  | 2.2.0   | [`employeegroups/all`](#operation/GetAllEmployeeGroups) and [`employeegroups/{number}`](#operation/GetEmployeeGroupById) endpoints added.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |  | 2.1.0   | [`/activities/allowed`](#operation/GetAllowedActivities) endpoint added to get allowed activities for an employee and project.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |  | 2.0.0   | Open API released! Endpoints related to Projects module added.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |    </details>   # TL;DR    **Add these three headers to your requests.**    | Header                | Value                      | What is this?                                                |  | :-------------------- | :------------------------- | :----------------------------------------------------------- |  | X-AppSecretToken      | YOUR_PRIVATE_TOKEN         | This identifies your app. This is your secret token. Try using the value `demo`. |  | X-AgreementGrantToken | YOUR_AGREEMENT_GRANT_TOKEN | This identifies the grant issued by an agreement, to allow your app to access the agreements data. Try using the value `demo`. |  | Content-Type          | application/json           | We’re a JSON based API. This tells us that you agree with us on using JSON. |    ### Examples    #### jQuery    ```javascript/jQuery  $.ajax({      url: \"https://apis.e-conomic.com/api/v20.0.0/projects\",      dataType: \"json\",      headers: {          'X-AppSecretToken': \"demo\",          'X-AgreementGrantToken': \"demo\",          'Content-Type': \"application/json\"      },      type: \"GET\"  })      .always(function (data) {      $(\"#output\").text(JSON.stringify(data, null, 4));  });  ```    #### cURL    ```curl  curl -H \"X-AppSecretToken: demo\" -H \"X-AgreementGrantToken: demo\" https://apis.e-conomic.com/api/v20.0.0/projects  ```        # Introduction    Welcome to the **Visma e-conomic OpenAPI** documentation!    The e-conomic API is a document-based JSON REST API.     For more in-depth information about e-conomic itself, please have a look at the e-copedia [http://wiki.e-conomic.dk](http://wiki.e-conomic.dk/).    ## Usage    - **Generating a client** can easily be done using tools like [swagger-codegen](https://github.com/swagger-api/swagger-codegen) or others that work with [OpenAPI Specification](https://github.com/OAI/OpenAPI-Specification) specs.      ## Versioning    API releases are versioned using a three-part versioning scheme: `{major version}.{minor version}.{patch version}`.    We broadly follow [Semantic Versioning](https://semver.org/) principles when versioning the API. The major version number is incremented when a breaking change occurs.     The format is:    `/api/v{major version}.{minor version}.{patch version}/{resource-name}`    Each value of the above are integers and you should configure the specific version in each API call.     An example could be: `/api/v2.2.1/projects`    To track the changes of versions, please see our [changelog](#section/Changelog).    We reserve the right to deprecate versions at intervals since this allows for moving into a friendly environment for you faster.    ## Demo authentication    If you wish to try out the API before registering a developer agreement, you can do this by using the demo agreement, which mimics the authentication flow you will have to use when you create your app. All you have to do is specify HTTP header tokens `X-AgreementGrantToken: demo` and `X-AppSecretToken: demo`. Note however that you can only do GET requests with the demo agreement. If you want full access to our API's, you will need to register.    # Retrieving data    Our data is exposed as collections of items. Each item has many properties, with one property as a unique identifier, usually called `number` or `id`. You can always get a single item if you already know the unique identifier. In case the unique identifier is not known, you can always search the collection and retrieve an array of items that satisfy the search criteria, or retrieve only the count of items that satisfy the search criteria. When you search for items in a collection, you can always use filtering, sorting and pagination. When it comes to pagination, we offer two distinct approaches available on separate endpoints. You can read more about filtering, sorting and pagination in the following sections.     ## Filtering    Filtering is enabled on all collection endpoints but not on all properties.    Filtering on collections can be done using the query string parameter `filter`. A filter is made up of a set of predicates and follows a syntax inspired by mongoDB. A predicate is made up of a property name, an operator, and a value.    Example: `?filter=name$eq:Joe`    This matches all resources with the value Joe in the property name.    Predicates can be chained using either of the logical operators AND and OR.    Example: `?filter=name$eq:Joe$and:city$like:*port`    Filtering on strings is case insensitive.    #### Filterable properties  Information about what properties allow filtering and on what operators can be found in the property in the schema for the collection. Each property that allows filtering has the property `\"x-filterable\"` in combination with `operators` set. If you try to filter on something that isn’t allowed the server will respond with a status code 400.    #### Specifying Operator affinity  If you want to control the operator affinity then you can use parentheses.    An example is: `?filter=name$eq:Joe$and:(city$like:*port$or:age$lt:40)`    #### URL Encoding  URL parameter values should always be URL compatible. Always URL encode filter strings.    #### Filter Operators  The possible filtering operators are:    | Operator   | Syntax |  | --------   | ------ |  |Equals | $eq:|  |Not equals | $ne:|  |Greater than | $gt:|  |Greater than or equal | $gte:|  |Less than | $lt:|  |Less than or equal | $lte:|  |Substring match | $like:|  |And also | $and:|  |Or else | $or:|  |In | $in:|  |Not In | $nin:|    #### Substring matching    The `$like:` operator supports both using wildcards (*) and not using wildcards. If no wildcards are used, the expression is considered a `contains` expression and effectively becomes a filter with a wildcard at the start of the string and one at the end of the string. This operator is only allowed on some properties.    #### Escaping special characters in your filter  To not interfere with the parsing of the filter expression, certain escape sequences are necessary.    - “$” is escaped with “$$”  - “(” is escaped with “$(”  - “)” is escaped with “$)”  - “*” is escaped with “$*”  - “,” is escaped with “$,”  - “[” is escaped with “$[”  - “]” is escaped with “$]”    #### Using null values in your filter  Should you want to filter for the nonexistence of a property (i.e. null value) you can use the null escape sequence.    `$null:`    #### Using in and not in operators  To determine whether a specified value matches any value in (or not in) a list you filter using the `$in:` or `$nin:` operator. The list to filter by has to be enclosed in brackets and values separated by commas.    `customerNumber$in:[2,5,7,22,45]`      It is possible to also use the `$null:` keyword if you wish to include that in the filter. The max supported length of an array using the `$in:` or `$nin:` operator is 200.      ## Sorting    Sorting on strings is case insensitive.    ### Sort ascending    Sorting on collections can be done using the query string parameter ‘sort’.    ```  ?sort=name  ```    ### Sort descending    The default sort direction is ascending, but this can be turned by prepending a minus (-).    ```  ?sort=-name  ```    ### Sort by multiple properties    If you need to sort by multiple properties these can just be separated by commas. Mixing of directions is allowed.    ```  ?sort=-name,age  ```    ### Sort alphabetically    In certain cases, you might want to enforce that even numeric values are sorted alphabetically, so 1000 is less than 30. In those cases, you can prepend the sort property with a tilde (~).    ```  ?sort=~name  ```    #### Sortable properties  Information about what properties are sortable can be found in the schema for the collection. Each property that allows sorting has the property `\"x-sortable\": true` set.      ## Pagination    When it comes to retrieving a collection of items, you can use two distinct approaches:    * **Cursor-based pagination** (continued loading of items using a `cursor` as a query parameter to get the next page of items)    * This is the recommended approach, and the one you should use by default.    * The endpoint naming scheme is **\"Retrieve all `Items`\"**. (Usage: `/{ITEM}?cursor={CURSOR_VALUE}`)      * **Classic pagination** (limited functionality*. Specify `skippages` and `pagesize ` as query parameters to get a specific page of items)    * You should only consider using classic pagination, if you rely on loading pages (i.e. for list views or table/grid-based UI's).    * The endpoint naming scheme is **\"Retrieve a page of `Items`\"**. (Usage: `/{ITEM}/paged?skippages=0&pagesize=20`)        \\* It's important to note that there is a limit of 10.000 items using this approach. Any items outside of the first 10.000 items will not be loaded.    Please bear in mind that the two approaches are supported by **separate endpoints**. To use classic pagination, add `/paged` to your request URL.    If you need to know the total count of items that you can expect to get from your search, you can use a separate endpoint called **\"Retrieve the number of `Items`\"**.    You can also use the result of this endpoint to calculate the pagination navigation buttons for a table/grid-based UI.      ### Which approach should you use?  We highly recommend that you use cursor-based pagination because:  - It is more performant and offers much faster retrieval of items;  - It can be used for very large collections of many thousands or millions of items, whereas classic pagination is limited to only returning 10.000 results, everything else is ignored;      Classic pagination is only appropriate when you have an app with a table/grid-based UI.    ### Cursor-based pagination    #### How it works    When you search for items in a large collection, the response will contain the first 1.000 items and a `cursor` that you can use in a subsequent request to get the next series of items. This way you can retrieve the next set of items only when needed (if 1.000 items suffice, you don't need to send a second request).    Please note that the cursor is currently the `id` of the first `item` on the next set and it should not be mistaken for the number of items which are yet to be displayed.  Also, if the cursor is not present in the response, it means that there are no more items in the results.    ##### Real world example    I want to retrieve all projects.    1) I send a request to `https://apis.e-conomic.com/api/v20.0.0/projects`     and get back an array of 1.000 projects, and a `cursor` with value `34781`      2) I send a request for the next items in the resulting collection:       `https://apis.e-conomic.com/api/v20.0.0/projects?cursor=34781`       and get back an array of 1.000 projects and a cursor with value `87695`      3) I send a request for the next items in the result:       `https://apis.e-conomic.com/api/v20.0.0/projects?cursor=87695`       and get back an array of 56 items and no cursor.       No cursor means I have retrieved all the projects, i.e. I have reached the end of the list.      ### Classic pagination    If no parameters are used, the collection endpoint returns 20 items at a time. URL parameters allow you to increase this to up to 100 items or to skip pages if necessary.    ##### Real world example    I want to show a grid with page size of 50 and pagination navigation buttons.    1) I send a request to see how many projects there are in the collection:       `https://apis.e-conomic.com/api/v20.0.0/projects/count`       I get the number of projects in the collection, `2056`, and I can calculate the number of pages to be 2056 divided by 50 = 40 with 6 as remainder, meaning I have 41 pages total. I can then use this to present the user the navigation buttons.      2) I send a request to retrieve the first page of projects that my user will see:       `https://apis.e-conomic.com/api/v20.0.0/projects/paged?pagesize=50&sort=name`       with this I get back an array of 50 projects, sorted alphabetically by the project name.      3) Now if the user wants to see page number 6, I'll send a new request, skipping the first 5 pages to get the projects from page number 6:       `https://apis.e-conomic.com/api/v20.0.0/projects/paged?pagesize=50&skippages=5&sort=name`       I get back an array of 50 projects, that belong to page number 6 when sorting alphabetically by the project name.        ### Number of items in a collection    As mentioned before we offer endpoint to get the count of items in the collection. You can also use this info for calculation of pagination navigation in case of classic pagination.    Example `https://apis.e-conomic.com/api/v20.0.0/projects/count`      ## HTTP Status Codes    The Open API returns these HTTP status codes.    | Code | Text                   | Description                                                  |  | :--- | :--------------------- | :----------------------------------------------------------- |  | 200  | OK                     | Everything is OK                                             |  | 201  | Created                | When you create resources, this is what you get. This will be accompanied by the created resource in the body and a location header with a link to the created resource. |  | 204  | No Content             | In certain cases there is nothing to return. So we will let you know by returning a 204. |  | 400  | Bad Request            | The request you made was somehow malformed. A malformed request could be failed validation on creation or updating. If you try to filter on something that isn’t filterable this is also what you’ll see. Whenever possible we will also try to include a developer hint to help you get around this issue. |  | 401  | Unauthorized           | The credentials you supplied us with weren’t correct, or perhaps you forgot them altogether. If an agreement has revoked the grant they gave your app, this is what you will see. |  | 403  | Forbidden              | You won’t necessarily have access to everything. So even though you were authorized we might still deny access to certain resources. This depends on the roles asked for when the grant was issued. |  | 404  | Not Found              | This is returned when you try to request something that doesn’t exist. This could be a resource that has been deleted or just a URL you tried to hack. If you see a lot of these, it could be an indication that you aren’t using the links provided by the API. You should never need to concatenate any URLs. The API should provide you with the links needed. |  | 405  | Method Not Allowed     | Not all endpoints support all HTTP methods. If you try issue a PUT request to a collection resource this is what you get. |  | 415  | Unsupported Media Type | Our API is a JSON api. If you ask us to give you anything else, we give you this, and tell you why in the JSON body of the response. |  | 500  | Internal Server Error  | We don’t like to see these, and they are flagged in our logs. When you see this, something went wrong on our end. Either try again, or contact our support. |      ## Required and Readonly Properties    Since OpenAPI allows client generation based on the specification, we decided to use the same model/schema in our for both read and write endpoints where possible.    This led us to chose not to have the Id/Number in the URL parameter for PUT requests, but to use the one from the body, so there is no confusion.    When a property is marked as `required` it means you need to provide a value on each POST and PUT requests.    When a property is marked as `readonly` it means you should provide the same value you get in the GET requests, or do not send the property in the JSON at all (skip it).    ## Custom resource encoding    For some resource ids (the direct URL path to a resource) the question of non-alphanumeric characters must be solved in REST APIs by either encoding or replacement to ensure URL compatibility.    In the e-conomic REST API a subset of non-alphanumeric characters are replaced using a custom scheme for resource URLs:    | Character        | Replacement |  | :--------------- | :---------- |  | “<”              | *0*         |  | “>”              | *1*         |  | “*”              | *2*         |  | “%”              | *3*         |  | “:”              | *4*         |  | “&”              | *5*         |  | “/”              | *6*         |  | “\\”              | *7*         |  | “_”              | *8*         |  | “ ” (whitespace) | *9*         |  | “?”              | *10*        |  | “.”              | *11*        |  | “#”              | *12*        |  | “+”              | *13*        |    Example: Product “My Awesome Product_Discount5%” Resource URL (self): https://apis.e-conomic.com/products/My_9_Awesome_9_Product_8_Discount5_3_    All other non-alphanumeric characters in resource URLs are standard URL encoded. Please refer to standard URL encoding for characters not mentioned above.    ## Implementation specifics    Helpful details to know when implementing e-conomic REST.    ### Booleans    Booleans should only be expected to be represented in responses when true. A false boolean is omitted from response body. The same logic applies to write operations such as POST and PUT.    ### Null values    Null values are omitted from the response body.    ### Nulling    We do not generally accept null as a value and a validation exception should be expected. To null a property you must exclude it from your JSON on the write operation.    ## Object version    ObjectVersion is the mechanism that enforces updates only on latest state of an object.  ObjectVersion property is mandatory in Put Requests.  ObjectVersion property is retrieved on Get Request and needs to be included in Put Request.  If object was modified between Get and Put requests, Put request will fail with error code `409 Conflict`    ```  {    \"message\": \"Update conflict. Version does not match.\",    \"developerHint\": \"The resource has been updated by another user. Retrieve the resource/object and try the update again. This is needed in order to prevent you from rolling back another user's update.\",    \"logId\": \"09580053-1141-4e7f-85e1-bed8600e0278\",    \"logTimeUtc\": \"2021-11-04T09:07:56\",    \"property\": \"version\"  }  ```    ## Custom extensions in OpenAPI specification    In the specification file, there are some custom extensions that developers can make use of when consuming endpoints.   Those extensions are always prefixed by `x-`.    1) `x-required-roles`: The list of roles that are required for each group of endpoints.  2) `x-error-codes`: The list of error codes that are potentially returned from each group of endpoints.  
 *
 * The version of the OpenAPI document: v20.0.0
 * Contact: api@e-conomic.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiCallback;
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.ApiResponse;
import org.openapitools.client.Configuration;
import org.openapitools.client.Pair;
import org.openapitools.client.ProgressRequestBody;
import org.openapitools.client.ProgressResponseBody;

import com.google.gson.reflect.TypeToken;

import java.io.IOException;


import org.openapitools.client.model.CreatedResult;
import org.openapitools.client.model.Error;
import org.openapitools.client.model.ProjectEmployeeGroup;
import org.openapitools.client.model.ProjectEmployeeGroupCursorResults;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ProjectEmployeeGroupsApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public ProjectEmployeeGroupsApi() {
        this(Configuration.getDefaultApiClient());
    }

    public ProjectEmployeeGroupsApi(ApiClient apiClient) {
        this.localVarApiClient = apiClient;
    }

    public ApiClient getApiClient() {
        return localVarApiClient;
    }

    public void setApiClient(ApiClient apiClient) {
        this.localVarApiClient = apiClient;
    }

    public int getHostIndex() {
        return localHostIndex;
    }

    public void setHostIndex(int hostIndex) {
        this.localHostIndex = hostIndex;
    }

    public String getCustomBaseUrl() {
        return localCustomBaseUrl;
    }

    public void setCustomBaseUrl(String customBaseUrl) {
        this.localCustomBaseUrl = customBaseUrl;
    }

    /**
     * Build call for createProjectEmployeeGroup
     * @param projectEmployeeGroup  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> **Bad request.** Your request does not pass our validation. See the message for more details. </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> **Unauthorized access.** Please take a look at https://apis.e-conomic.com and follow the links to help on authorization, or use the word demo for both tokens. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> **Access forbidden.** You won’t necessarily have access to everything. So even though you were authorized we might still deny access to certain resources. This depends on the roles asked for when the grant was issued. </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> **Too many requests.** You have made too many calls towards our API. You are over your quota. Need to wait a bit. Check info in the response headers. </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> **Internal server error.** Something went wrong but the error has been logged. If you continue to see errors here, please contact api@e-conomic.com. Remember to include log id and agreement number when contacting support. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createProjectEmployeeGroupCall(ProjectEmployeeGroup projectEmployeeGroup, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = projectEmployeeGroup;

        // create path and map variables
        String localVarPath = "/project-employeegroups";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/*+json",
            "application/json",
            "application/json-patch+json",
            "text/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "X-AgreementGrantToken", "X-AppSecretToken" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call createProjectEmployeeGroupValidateBeforeCall(ProjectEmployeeGroup projectEmployeeGroup, final ApiCallback _callback) throws ApiException {
        return createProjectEmployeeGroupCall(projectEmployeeGroup, _callback);

    }

    /**
     * Create a single Project employee group
     * Use this endpoint to create a single Project employee group.
     * @param projectEmployeeGroup  (optional)
     * @return CreatedResult
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> **Bad request.** Your request does not pass our validation. See the message for more details. </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> **Unauthorized access.** Please take a look at https://apis.e-conomic.com and follow the links to help on authorization, or use the word demo for both tokens. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> **Access forbidden.** You won’t necessarily have access to everything. So even though you were authorized we might still deny access to certain resources. This depends on the roles asked for when the grant was issued. </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> **Too many requests.** You have made too many calls towards our API. You are over your quota. Need to wait a bit. Check info in the response headers. </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> **Internal server error.** Something went wrong but the error has been logged. If you continue to see errors here, please contact api@e-conomic.com. Remember to include log id and agreement number when contacting support. </td><td>  -  </td></tr>
     </table>
     */
    public CreatedResult createProjectEmployeeGroup(ProjectEmployeeGroup projectEmployeeGroup) throws ApiException {
        ApiResponse<CreatedResult> localVarResp = createProjectEmployeeGroupWithHttpInfo(projectEmployeeGroup);
        return localVarResp.getData();
    }

    /**
     * Create a single Project employee group
     * Use this endpoint to create a single Project employee group.
     * @param projectEmployeeGroup  (optional)
     * @return ApiResponse&lt;CreatedResult&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> **Bad request.** Your request does not pass our validation. See the message for more details. </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> **Unauthorized access.** Please take a look at https://apis.e-conomic.com and follow the links to help on authorization, or use the word demo for both tokens. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> **Access forbidden.** You won’t necessarily have access to everything. So even though you were authorized we might still deny access to certain resources. This depends on the roles asked for when the grant was issued. </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> **Too many requests.** You have made too many calls towards our API. You are over your quota. Need to wait a bit. Check info in the response headers. </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> **Internal server error.** Something went wrong but the error has been logged. If you continue to see errors here, please contact api@e-conomic.com. Remember to include log id and agreement number when contacting support. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CreatedResult> createProjectEmployeeGroupWithHttpInfo(ProjectEmployeeGroup projectEmployeeGroup) throws ApiException {
        okhttp3.Call localVarCall = createProjectEmployeeGroupValidateBeforeCall(projectEmployeeGroup, null);
        Type localVarReturnType = new TypeToken<CreatedResult>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Create a single Project employee group (asynchronously)
     * Use this endpoint to create a single Project employee group.
     * @param projectEmployeeGroup  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> **Bad request.** Your request does not pass our validation. See the message for more details. </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> **Unauthorized access.** Please take a look at https://apis.e-conomic.com and follow the links to help on authorization, or use the word demo for both tokens. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> **Access forbidden.** You won’t necessarily have access to everything. So even though you were authorized we might still deny access to certain resources. This depends on the roles asked for when the grant was issued. </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> **Too many requests.** You have made too many calls towards our API. You are over your quota. Need to wait a bit. Check info in the response headers. </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> **Internal server error.** Something went wrong but the error has been logged. If you continue to see errors here, please contact api@e-conomic.com. Remember to include log id and agreement number when contacting support. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createProjectEmployeeGroupAsync(ProjectEmployeeGroup projectEmployeeGroup, final ApiCallback<CreatedResult> _callback) throws ApiException {

        okhttp3.Call localVarCall = createProjectEmployeeGroupValidateBeforeCall(projectEmployeeGroup, _callback);
        Type localVarReturnType = new TypeToken<CreatedResult>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteProjectEmployeeGroupById
     * @param number  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> **Bad request.** Your request does not pass our validation. See the message for more details. </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> **Unauthorized access.** Please take a look at https://apis.e-conomic.com and follow the links to help on authorization, or use the word demo for both tokens. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> **Access forbidden.** You won’t necessarily have access to everything. So even though you were authorized we might still deny access to certain resources. This depends on the roles asked for when the grant was issued. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> **Resource not found.** The resource you have been looking for does not exist. </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> **Too many requests.** You have made too many calls towards our API. You are over your quota. Need to wait a bit. Check info in the response headers. </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> **Internal server error.** Something went wrong but the error has been logged. If you continue to see errors here, please contact api@e-conomic.com. Remember to include log id and agreement number when contacting support. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteProjectEmployeeGroupByIdCall(Integer number, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/project-employeegroups/{number}"
            .replace("{" + "number" + "}", localVarApiClient.escapeString(number.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "X-AgreementGrantToken", "X-AppSecretToken" };
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call deleteProjectEmployeeGroupByIdValidateBeforeCall(Integer number, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'number' is set
        if (number == null) {
            throw new ApiException("Missing the required parameter 'number' when calling deleteProjectEmployeeGroupById(Async)");
        }

        return deleteProjectEmployeeGroupByIdCall(number, _callback);

    }

    /**
     * Delete single Project employee group
     * Use this endpoint to delete a single Project employee group by id/number.
     * @param number  (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> **Bad request.** Your request does not pass our validation. See the message for more details. </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> **Unauthorized access.** Please take a look at https://apis.e-conomic.com and follow the links to help on authorization, or use the word demo for both tokens. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> **Access forbidden.** You won’t necessarily have access to everything. So even though you were authorized we might still deny access to certain resources. This depends on the roles asked for when the grant was issued. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> **Resource not found.** The resource you have been looking for does not exist. </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> **Too many requests.** You have made too many calls towards our API. You are over your quota. Need to wait a bit. Check info in the response headers. </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> **Internal server error.** Something went wrong but the error has been logged. If you continue to see errors here, please contact api@e-conomic.com. Remember to include log id and agreement number when contacting support. </td><td>  -  </td></tr>
     </table>
     */
    public void deleteProjectEmployeeGroupById(Integer number) throws ApiException {
        deleteProjectEmployeeGroupByIdWithHttpInfo(number);
    }

    /**
     * Delete single Project employee group
     * Use this endpoint to delete a single Project employee group by id/number.
     * @param number  (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> **Bad request.** Your request does not pass our validation. See the message for more details. </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> **Unauthorized access.** Please take a look at https://apis.e-conomic.com and follow the links to help on authorization, or use the word demo for both tokens. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> **Access forbidden.** You won’t necessarily have access to everything. So even though you were authorized we might still deny access to certain resources. This depends on the roles asked for when the grant was issued. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> **Resource not found.** The resource you have been looking for does not exist. </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> **Too many requests.** You have made too many calls towards our API. You are over your quota. Need to wait a bit. Check info in the response headers. </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> **Internal server error.** Something went wrong but the error has been logged. If you continue to see errors here, please contact api@e-conomic.com. Remember to include log id and agreement number when contacting support. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> deleteProjectEmployeeGroupByIdWithHttpInfo(Integer number) throws ApiException {
        okhttp3.Call localVarCall = deleteProjectEmployeeGroupByIdValidateBeforeCall(number, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Delete single Project employee group (asynchronously)
     * Use this endpoint to delete a single Project employee group by id/number.
     * @param number  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> **Bad request.** Your request does not pass our validation. See the message for more details. </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> **Unauthorized access.** Please take a look at https://apis.e-conomic.com and follow the links to help on authorization, or use the word demo for both tokens. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> **Access forbidden.** You won’t necessarily have access to everything. So even though you were authorized we might still deny access to certain resources. This depends on the roles asked for when the grant was issued. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> **Resource not found.** The resource you have been looking for does not exist. </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> **Too many requests.** You have made too many calls towards our API. You are over your quota. Need to wait a bit. Check info in the response headers. </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> **Internal server error.** Something went wrong but the error has been logged. If you continue to see errors here, please contact api@e-conomic.com. Remember to include log id and agreement number when contacting support. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteProjectEmployeeGroupByIdAsync(Integer number, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteProjectEmployeeGroupByIdValidateBeforeCall(number, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for getAllProjectEmployeeGroups
     * @param cursor  (optional)
     * @param filter  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> **Bad request.** Your request does not pass our validation. See the message for more details. </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> **Unauthorized access.** Please take a look at https://apis.e-conomic.com and follow the links to help on authorization, or use the word demo for both tokens. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> **Access forbidden.** You won’t necessarily have access to everything. So even though you were authorized we might still deny access to certain resources. This depends on the roles asked for when the grant was issued. </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> **Too many requests.** You have made too many calls towards our API. You are over your quota. Need to wait a bit. Check info in the response headers. </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> **Internal server error.** Something went wrong but the error has been logged. If you continue to see errors here, please contact api@e-conomic.com. Remember to include log id and agreement number when contacting support. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getAllProjectEmployeeGroupsCall(String cursor, String filter, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/project-employeegroups";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (cursor != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("Cursor", cursor));
        }

        if (filter != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("Filter", filter));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "X-AgreementGrantToken", "X-AppSecretToken" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getAllProjectEmployeeGroupsValidateBeforeCall(String cursor, String filter, final ApiCallback _callback) throws ApiException {
        return getAllProjectEmployeeGroupsCall(cursor, filter, _callback);

    }

    /**
     * Retrieve all Project employee groups
     * Use this endpoint to retrieve all Project employee groups in bulk.  Max number of items returned in a single call is 1000. Use the continuation cursor parameter to set the continuation cursor for retrieval of next set of data. [pagination instructions](#section/Retrieving-data/Pagination)
     * @param cursor  (optional)
     * @param filter  (optional)
     * @return ProjectEmployeeGroupCursorResults
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> **Bad request.** Your request does not pass our validation. See the message for more details. </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> **Unauthorized access.** Please take a look at https://apis.e-conomic.com and follow the links to help on authorization, or use the word demo for both tokens. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> **Access forbidden.** You won’t necessarily have access to everything. So even though you were authorized we might still deny access to certain resources. This depends on the roles asked for when the grant was issued. </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> **Too many requests.** You have made too many calls towards our API. You are over your quota. Need to wait a bit. Check info in the response headers. </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> **Internal server error.** Something went wrong but the error has been logged. If you continue to see errors here, please contact api@e-conomic.com. Remember to include log id and agreement number when contacting support. </td><td>  -  </td></tr>
     </table>
     */
    public ProjectEmployeeGroupCursorResults getAllProjectEmployeeGroups(String cursor, String filter) throws ApiException {
        ApiResponse<ProjectEmployeeGroupCursorResults> localVarResp = getAllProjectEmployeeGroupsWithHttpInfo(cursor, filter);
        return localVarResp.getData();
    }

    /**
     * Retrieve all Project employee groups
     * Use this endpoint to retrieve all Project employee groups in bulk.  Max number of items returned in a single call is 1000. Use the continuation cursor parameter to set the continuation cursor for retrieval of next set of data. [pagination instructions](#section/Retrieving-data/Pagination)
     * @param cursor  (optional)
     * @param filter  (optional)
     * @return ApiResponse&lt;ProjectEmployeeGroupCursorResults&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> **Bad request.** Your request does not pass our validation. See the message for more details. </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> **Unauthorized access.** Please take a look at https://apis.e-conomic.com and follow the links to help on authorization, or use the word demo for both tokens. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> **Access forbidden.** You won’t necessarily have access to everything. So even though you were authorized we might still deny access to certain resources. This depends on the roles asked for when the grant was issued. </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> **Too many requests.** You have made too many calls towards our API. You are over your quota. Need to wait a bit. Check info in the response headers. </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> **Internal server error.** Something went wrong but the error has been logged. If you continue to see errors here, please contact api@e-conomic.com. Remember to include log id and agreement number when contacting support. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ProjectEmployeeGroupCursorResults> getAllProjectEmployeeGroupsWithHttpInfo(String cursor, String filter) throws ApiException {
        okhttp3.Call localVarCall = getAllProjectEmployeeGroupsValidateBeforeCall(cursor, filter, null);
        Type localVarReturnType = new TypeToken<ProjectEmployeeGroupCursorResults>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retrieve all Project employee groups (asynchronously)
     * Use this endpoint to retrieve all Project employee groups in bulk.  Max number of items returned in a single call is 1000. Use the continuation cursor parameter to set the continuation cursor for retrieval of next set of data. [pagination instructions](#section/Retrieving-data/Pagination)
     * @param cursor  (optional)
     * @param filter  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> **Bad request.** Your request does not pass our validation. See the message for more details. </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> **Unauthorized access.** Please take a look at https://apis.e-conomic.com and follow the links to help on authorization, or use the word demo for both tokens. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> **Access forbidden.** You won’t necessarily have access to everything. So even though you were authorized we might still deny access to certain resources. This depends on the roles asked for when the grant was issued. </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> **Too many requests.** You have made too many calls towards our API. You are over your quota. Need to wait a bit. Check info in the response headers. </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> **Internal server error.** Something went wrong but the error has been logged. If you continue to see errors here, please contact api@e-conomic.com. Remember to include log id and agreement number when contacting support. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getAllProjectEmployeeGroupsAsync(String cursor, String filter, final ApiCallback<ProjectEmployeeGroupCursorResults> _callback) throws ApiException {

        okhttp3.Call localVarCall = getAllProjectEmployeeGroupsValidateBeforeCall(cursor, filter, _callback);
        Type localVarReturnType = new TypeToken<ProjectEmployeeGroupCursorResults>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getNumberOfProjectEmployeeGroups
     * @param filter  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> **Bad request.** Your request does not pass our validation. See the message for more details. </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> **Unauthorized access.** Please take a look at https://apis.e-conomic.com and follow the links to help on authorization, or use the word demo for both tokens. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> **Access forbidden.** You won’t necessarily have access to everything. So even though you were authorized we might still deny access to certain resources. This depends on the roles asked for when the grant was issued. </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> **Too many requests.** You have made too many calls towards our API. You are over your quota. Need to wait a bit. Check info in the response headers. </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> **Internal server error.** Something went wrong but the error has been logged. If you continue to see errors here, please contact api@e-conomic.com. Remember to include log id and agreement number when contacting support. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getNumberOfProjectEmployeeGroupsCall(String filter, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/project-employeegroups/count";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (filter != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("Filter", filter));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "X-AgreementGrantToken", "X-AppSecretToken" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getNumberOfProjectEmployeeGroupsValidateBeforeCall(String filter, final ApiCallback _callback) throws ApiException {
        return getNumberOfProjectEmployeeGroupsCall(filter, _callback);

    }

    /**
     * Retrieve the number of Project employee groups
     * Call this endpoint to get the number of Project employee groups. You can use a filtering as well.
     * @param filter  (optional)
     * @return Integer
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> **Bad request.** Your request does not pass our validation. See the message for more details. </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> **Unauthorized access.** Please take a look at https://apis.e-conomic.com and follow the links to help on authorization, or use the word demo for both tokens. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> **Access forbidden.** You won’t necessarily have access to everything. So even though you were authorized we might still deny access to certain resources. This depends on the roles asked for when the grant was issued. </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> **Too many requests.** You have made too many calls towards our API. You are over your quota. Need to wait a bit. Check info in the response headers. </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> **Internal server error.** Something went wrong but the error has been logged. If you continue to see errors here, please contact api@e-conomic.com. Remember to include log id and agreement number when contacting support. </td><td>  -  </td></tr>
     </table>
     */
    public Integer getNumberOfProjectEmployeeGroups(String filter) throws ApiException {
        ApiResponse<Integer> localVarResp = getNumberOfProjectEmployeeGroupsWithHttpInfo(filter);
        return localVarResp.getData();
    }

    /**
     * Retrieve the number of Project employee groups
     * Call this endpoint to get the number of Project employee groups. You can use a filtering as well.
     * @param filter  (optional)
     * @return ApiResponse&lt;Integer&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> **Bad request.** Your request does not pass our validation. See the message for more details. </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> **Unauthorized access.** Please take a look at https://apis.e-conomic.com and follow the links to help on authorization, or use the word demo for both tokens. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> **Access forbidden.** You won’t necessarily have access to everything. So even though you were authorized we might still deny access to certain resources. This depends on the roles asked for when the grant was issued. </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> **Too many requests.** You have made too many calls towards our API. You are over your quota. Need to wait a bit. Check info in the response headers. </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> **Internal server error.** Something went wrong but the error has been logged. If you continue to see errors here, please contact api@e-conomic.com. Remember to include log id and agreement number when contacting support. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Integer> getNumberOfProjectEmployeeGroupsWithHttpInfo(String filter) throws ApiException {
        okhttp3.Call localVarCall = getNumberOfProjectEmployeeGroupsValidateBeforeCall(filter, null);
        Type localVarReturnType = new TypeToken<Integer>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retrieve the number of Project employee groups (asynchronously)
     * Call this endpoint to get the number of Project employee groups. You can use a filtering as well.
     * @param filter  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> **Bad request.** Your request does not pass our validation. See the message for more details. </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> **Unauthorized access.** Please take a look at https://apis.e-conomic.com and follow the links to help on authorization, or use the word demo for both tokens. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> **Access forbidden.** You won’t necessarily have access to everything. So even though you were authorized we might still deny access to certain resources. This depends on the roles asked for when the grant was issued. </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> **Too many requests.** You have made too many calls towards our API. You are over your quota. Need to wait a bit. Check info in the response headers. </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> **Internal server error.** Something went wrong but the error has been logged. If you continue to see errors here, please contact api@e-conomic.com. Remember to include log id and agreement number when contacting support. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getNumberOfProjectEmployeeGroupsAsync(String filter, final ApiCallback<Integer> _callback) throws ApiException {

        okhttp3.Call localVarCall = getNumberOfProjectEmployeeGroupsValidateBeforeCall(filter, _callback);
        Type localVarReturnType = new TypeToken<Integer>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getPageOfProjectEmployeeGroups
     * @param filter  (optional)
     * @param sort  (optional)
     * @param pageSize  (optional, default to 20)
     * @param skipPages  (optional, default to 0)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> **Bad request.** Your request does not pass our validation. See the message for more details. </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> **Unauthorized access.** Please take a look at https://apis.e-conomic.com and follow the links to help on authorization, or use the word demo for both tokens. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> **Access forbidden.** You won’t necessarily have access to everything. So even though you were authorized we might still deny access to certain resources. This depends on the roles asked for when the grant was issued. </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> **Too many requests.** You have made too many calls towards our API. You are over your quota. Need to wait a bit. Check info in the response headers. </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> **Internal server error.** Something went wrong but the error has been logged. If you continue to see errors here, please contact api@e-conomic.com. Remember to include log id and agreement number when contacting support. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getPageOfProjectEmployeeGroupsCall(String filter, String sort, Integer pageSize, Integer skipPages, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/project-employeegroups/paged";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (filter != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("Filter", filter));
        }

        if (sort != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("Sort", sort));
        }

        if (pageSize != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("PageSize", pageSize));
        }

        if (skipPages != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("SkipPages", skipPages));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "X-AgreementGrantToken", "X-AppSecretToken" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getPageOfProjectEmployeeGroupsValidateBeforeCall(String filter, String sort, Integer pageSize, Integer skipPages, final ApiCallback _callback) throws ApiException {
        return getPageOfProjectEmployeeGroupsCall(filter, sort, pageSize, skipPages, _callback);

    }

    /**
     * Retrieve a page of Project employee groups
     * Use this endpoint to load a page of Project employee groups.
     * @param filter  (optional)
     * @param sort  (optional)
     * @param pageSize  (optional, default to 20)
     * @param skipPages  (optional, default to 0)
     * @return List&lt;ProjectEmployeeGroup&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> **Bad request.** Your request does not pass our validation. See the message for more details. </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> **Unauthorized access.** Please take a look at https://apis.e-conomic.com and follow the links to help on authorization, or use the word demo for both tokens. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> **Access forbidden.** You won’t necessarily have access to everything. So even though you were authorized we might still deny access to certain resources. This depends on the roles asked for when the grant was issued. </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> **Too many requests.** You have made too many calls towards our API. You are over your quota. Need to wait a bit. Check info in the response headers. </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> **Internal server error.** Something went wrong but the error has been logged. If you continue to see errors here, please contact api@e-conomic.com. Remember to include log id and agreement number when contacting support. </td><td>  -  </td></tr>
     </table>
     */
    public List<ProjectEmployeeGroup> getPageOfProjectEmployeeGroups(String filter, String sort, Integer pageSize, Integer skipPages) throws ApiException {
        ApiResponse<List<ProjectEmployeeGroup>> localVarResp = getPageOfProjectEmployeeGroupsWithHttpInfo(filter, sort, pageSize, skipPages);
        return localVarResp.getData();
    }

    /**
     * Retrieve a page of Project employee groups
     * Use this endpoint to load a page of Project employee groups.
     * @param filter  (optional)
     * @param sort  (optional)
     * @param pageSize  (optional, default to 20)
     * @param skipPages  (optional, default to 0)
     * @return ApiResponse&lt;List&lt;ProjectEmployeeGroup&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> **Bad request.** Your request does not pass our validation. See the message for more details. </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> **Unauthorized access.** Please take a look at https://apis.e-conomic.com and follow the links to help on authorization, or use the word demo for both tokens. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> **Access forbidden.** You won’t necessarily have access to everything. So even though you were authorized we might still deny access to certain resources. This depends on the roles asked for when the grant was issued. </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> **Too many requests.** You have made too many calls towards our API. You are over your quota. Need to wait a bit. Check info in the response headers. </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> **Internal server error.** Something went wrong but the error has been logged. If you continue to see errors here, please contact api@e-conomic.com. Remember to include log id and agreement number when contacting support. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<ProjectEmployeeGroup>> getPageOfProjectEmployeeGroupsWithHttpInfo(String filter, String sort, Integer pageSize, Integer skipPages) throws ApiException {
        okhttp3.Call localVarCall = getPageOfProjectEmployeeGroupsValidateBeforeCall(filter, sort, pageSize, skipPages, null);
        Type localVarReturnType = new TypeToken<List<ProjectEmployeeGroup>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retrieve a page of Project employee groups (asynchronously)
     * Use this endpoint to load a page of Project employee groups.
     * @param filter  (optional)
     * @param sort  (optional)
     * @param pageSize  (optional, default to 20)
     * @param skipPages  (optional, default to 0)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> **Bad request.** Your request does not pass our validation. See the message for more details. </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> **Unauthorized access.** Please take a look at https://apis.e-conomic.com and follow the links to help on authorization, or use the word demo for both tokens. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> **Access forbidden.** You won’t necessarily have access to everything. So even though you were authorized we might still deny access to certain resources. This depends on the roles asked for when the grant was issued. </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> **Too many requests.** You have made too many calls towards our API. You are over your quota. Need to wait a bit. Check info in the response headers. </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> **Internal server error.** Something went wrong but the error has been logged. If you continue to see errors here, please contact api@e-conomic.com. Remember to include log id and agreement number when contacting support. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getPageOfProjectEmployeeGroupsAsync(String filter, String sort, Integer pageSize, Integer skipPages, final ApiCallback<List<ProjectEmployeeGroup>> _callback) throws ApiException {

        okhttp3.Call localVarCall = getPageOfProjectEmployeeGroupsValidateBeforeCall(filter, sort, pageSize, skipPages, _callback);
        Type localVarReturnType = new TypeToken<List<ProjectEmployeeGroup>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getProjectEmployeeGroupById
     * @param number  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> **Bad request.** Your request does not pass our validation. See the message for more details. </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> **Unauthorized access.** Please take a look at https://apis.e-conomic.com and follow the links to help on authorization, or use the word demo for both tokens. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> **Access forbidden.** You won’t necessarily have access to everything. So even though you were authorized we might still deny access to certain resources. This depends on the roles asked for when the grant was issued. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> **Resource not found.** The resource you have been looking for does not exist. </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> **Too many requests.** You have made too many calls towards our API. You are over your quota. Need to wait a bit. Check info in the response headers. </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> **Internal server error.** Something went wrong but the error has been logged. If you continue to see errors here, please contact api@e-conomic.com. Remember to include log id and agreement number when contacting support. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getProjectEmployeeGroupByIdCall(Integer number, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/project-employeegroups/{number}"
            .replace("{" + "number" + "}", localVarApiClient.escapeString(number.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "X-AgreementGrantToken", "X-AppSecretToken" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getProjectEmployeeGroupByIdValidateBeforeCall(Integer number, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'number' is set
        if (number == null) {
            throw new ApiException("Missing the required parameter 'number' when calling getProjectEmployeeGroupById(Async)");
        }

        return getProjectEmployeeGroupByIdCall(number, _callback);

    }

    /**
     * Retrieve single Project employee group
     * Use this endpoint to load a single Project employee group by id/number.
     * @param number  (required)
     * @return ProjectEmployeeGroup
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> **Bad request.** Your request does not pass our validation. See the message for more details. </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> **Unauthorized access.** Please take a look at https://apis.e-conomic.com and follow the links to help on authorization, or use the word demo for both tokens. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> **Access forbidden.** You won’t necessarily have access to everything. So even though you were authorized we might still deny access to certain resources. This depends on the roles asked for when the grant was issued. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> **Resource not found.** The resource you have been looking for does not exist. </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> **Too many requests.** You have made too many calls towards our API. You are over your quota. Need to wait a bit. Check info in the response headers. </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> **Internal server error.** Something went wrong but the error has been logged. If you continue to see errors here, please contact api@e-conomic.com. Remember to include log id and agreement number when contacting support. </td><td>  -  </td></tr>
     </table>
     */
    public ProjectEmployeeGroup getProjectEmployeeGroupById(Integer number) throws ApiException {
        ApiResponse<ProjectEmployeeGroup> localVarResp = getProjectEmployeeGroupByIdWithHttpInfo(number);
        return localVarResp.getData();
    }

    /**
     * Retrieve single Project employee group
     * Use this endpoint to load a single Project employee group by id/number.
     * @param number  (required)
     * @return ApiResponse&lt;ProjectEmployeeGroup&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> **Bad request.** Your request does not pass our validation. See the message for more details. </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> **Unauthorized access.** Please take a look at https://apis.e-conomic.com and follow the links to help on authorization, or use the word demo for both tokens. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> **Access forbidden.** You won’t necessarily have access to everything. So even though you were authorized we might still deny access to certain resources. This depends on the roles asked for when the grant was issued. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> **Resource not found.** The resource you have been looking for does not exist. </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> **Too many requests.** You have made too many calls towards our API. You are over your quota. Need to wait a bit. Check info in the response headers. </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> **Internal server error.** Something went wrong but the error has been logged. If you continue to see errors here, please contact api@e-conomic.com. Remember to include log id and agreement number when contacting support. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ProjectEmployeeGroup> getProjectEmployeeGroupByIdWithHttpInfo(Integer number) throws ApiException {
        okhttp3.Call localVarCall = getProjectEmployeeGroupByIdValidateBeforeCall(number, null);
        Type localVarReturnType = new TypeToken<ProjectEmployeeGroup>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retrieve single Project employee group (asynchronously)
     * Use this endpoint to load a single Project employee group by id/number.
     * @param number  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> **Bad request.** Your request does not pass our validation. See the message for more details. </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> **Unauthorized access.** Please take a look at https://apis.e-conomic.com and follow the links to help on authorization, or use the word demo for both tokens. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> **Access forbidden.** You won’t necessarily have access to everything. So even though you were authorized we might still deny access to certain resources. This depends on the roles asked for when the grant was issued. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> **Resource not found.** The resource you have been looking for does not exist. </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> **Too many requests.** You have made too many calls towards our API. You are over your quota. Need to wait a bit. Check info in the response headers. </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> **Internal server error.** Something went wrong but the error has been logged. If you continue to see errors here, please contact api@e-conomic.com. Remember to include log id and agreement number when contacting support. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getProjectEmployeeGroupByIdAsync(Integer number, final ApiCallback<ProjectEmployeeGroup> _callback) throws ApiException {

        okhttp3.Call localVarCall = getProjectEmployeeGroupByIdValidateBeforeCall(number, _callback);
        Type localVarReturnType = new TypeToken<ProjectEmployeeGroup>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for updateProjectEmployeeGroup
     * @param projectEmployeeGroup  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> **Bad request.** Your request does not pass our validation. See the message for more details. </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> **Unauthorized access.** Please take a look at https://apis.e-conomic.com and follow the links to help on authorization, or use the word demo for both tokens. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> **Access forbidden.** You won’t necessarily have access to everything. So even though you were authorized we might still deny access to certain resources. This depends on the roles asked for when the grant was issued. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> **Resource not found.** The resource you have been looking for does not exist. </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> **Update conflict. Object version does not match.** The resource has been updated by another user. Retrieve the resource again to get the latest object version and then try to update. </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> **Too many requests.** You have made too many calls towards our API. You are over your quota. Need to wait a bit. Check info in the response headers. </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> **Internal server error.** Something went wrong but the error has been logged. If you continue to see errors here, please contact api@e-conomic.com. Remember to include log id and agreement number when contacting support. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateProjectEmployeeGroupCall(ProjectEmployeeGroup projectEmployeeGroup, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = projectEmployeeGroup;

        // create path and map variables
        String localVarPath = "/project-employeegroups";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/*+json",
            "application/json",
            "application/json-patch+json",
            "text/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "X-AgreementGrantToken", "X-AppSecretToken" };
        return localVarApiClient.buildCall(basePath, localVarPath, "PUT", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call updateProjectEmployeeGroupValidateBeforeCall(ProjectEmployeeGroup projectEmployeeGroup, final ApiCallback _callback) throws ApiException {
        return updateProjectEmployeeGroupCall(projectEmployeeGroup, _callback);

    }

    /**
     * Update a single Project employee group
     * Use this endpoint to update a single Project employee group.
     * @param projectEmployeeGroup  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> **Bad request.** Your request does not pass our validation. See the message for more details. </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> **Unauthorized access.** Please take a look at https://apis.e-conomic.com and follow the links to help on authorization, or use the word demo for both tokens. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> **Access forbidden.** You won’t necessarily have access to everything. So even though you were authorized we might still deny access to certain resources. This depends on the roles asked for when the grant was issued. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> **Resource not found.** The resource you have been looking for does not exist. </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> **Update conflict. Object version does not match.** The resource has been updated by another user. Retrieve the resource again to get the latest object version and then try to update. </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> **Too many requests.** You have made too many calls towards our API. You are over your quota. Need to wait a bit. Check info in the response headers. </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> **Internal server error.** Something went wrong but the error has been logged. If you continue to see errors here, please contact api@e-conomic.com. Remember to include log id and agreement number when contacting support. </td><td>  -  </td></tr>
     </table>
     */
    public void updateProjectEmployeeGroup(ProjectEmployeeGroup projectEmployeeGroup) throws ApiException {
        updateProjectEmployeeGroupWithHttpInfo(projectEmployeeGroup);
    }

    /**
     * Update a single Project employee group
     * Use this endpoint to update a single Project employee group.
     * @param projectEmployeeGroup  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> **Bad request.** Your request does not pass our validation. See the message for more details. </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> **Unauthorized access.** Please take a look at https://apis.e-conomic.com and follow the links to help on authorization, or use the word demo for both tokens. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> **Access forbidden.** You won’t necessarily have access to everything. So even though you were authorized we might still deny access to certain resources. This depends on the roles asked for when the grant was issued. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> **Resource not found.** The resource you have been looking for does not exist. </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> **Update conflict. Object version does not match.** The resource has been updated by another user. Retrieve the resource again to get the latest object version and then try to update. </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> **Too many requests.** You have made too many calls towards our API. You are over your quota. Need to wait a bit. Check info in the response headers. </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> **Internal server error.** Something went wrong but the error has been logged. If you continue to see errors here, please contact api@e-conomic.com. Remember to include log id and agreement number when contacting support. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> updateProjectEmployeeGroupWithHttpInfo(ProjectEmployeeGroup projectEmployeeGroup) throws ApiException {
        okhttp3.Call localVarCall = updateProjectEmployeeGroupValidateBeforeCall(projectEmployeeGroup, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Update a single Project employee group (asynchronously)
     * Use this endpoint to update a single Project employee group.
     * @param projectEmployeeGroup  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> **Bad request.** Your request does not pass our validation. See the message for more details. </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> **Unauthorized access.** Please take a look at https://apis.e-conomic.com and follow the links to help on authorization, or use the word demo for both tokens. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> **Access forbidden.** You won’t necessarily have access to everything. So even though you were authorized we might still deny access to certain resources. This depends on the roles asked for when the grant was issued. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> **Resource not found.** The resource you have been looking for does not exist. </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> **Update conflict. Object version does not match.** The resource has been updated by another user. Retrieve the resource again to get the latest object version and then try to update. </td><td>  -  </td></tr>
        <tr><td> 429 </td><td> **Too many requests.** You have made too many calls towards our API. You are over your quota. Need to wait a bit. Check info in the response headers. </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> **Internal server error.** Something went wrong but the error has been logged. If you continue to see errors here, please contact api@e-conomic.com. Remember to include log id and agreement number when contacting support. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateProjectEmployeeGroupAsync(ProjectEmployeeGroup projectEmployeeGroup, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = updateProjectEmployeeGroupValidateBeforeCall(projectEmployeeGroup, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
}
