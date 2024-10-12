/**
 * Visma e-conomic OpenAPI
 * # Changelog    <details>    <summary>Click to see changelog.</summary>    | Version | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |  |---------| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |  | 20.0.0  | Customer contacts and delivery locations endpoints deprecated. You can find the same enpoints in [`Customers API`](https://apis.e-conomic.com/#Customers)   | 19.0.0  | Page-based endpoints were moved under /paged url and cursor-based endpoints dropped the /all.  | 18.0.0  | Added isDeleted flag to [`customer-contacts`](#tag/Customer-contacts) and included deleted contacts in the response. <br> Deleted contacts can be used for history purposes, but cannot be set as reference persons on sales documents. <br> In previous versions only customer-contacts/id returns deleted contacts as well.  | 17.0.2  | `TimeEntryEmployeeNumberCannotBeUpdated` and `MileageEmployeeNumberCannotBeUpdated` error codes removed. The change affects all versions, but we bumped the version for transparency.  | 17.0.1  | New custom [`OpenAPI extension`](#section/Retrieving-data/Custom-extensions-in-OpenAPI-specification) added in the specification: `x-error-codes`. Existing `x-required-roles` extension converted to an array of strings.  | 17.0.0  | Improved the error model. Added `code` and `property` fields to the model. `code` represents the error code. `property` is the field name on which the input validation failed.  | 16.4.0  | [`customer-deliverylocations`](#tag/Customer-delivery-locations) endpoints added.  | 16.3.0  | [`customer-contacts`](#tag/Customer-contacts) endpoints added.    | 16.2.2  | Added input validations for required string properties, if a string property is required it can't be empty, it should contain at least 1 character.  | 16.2.1  | Error codes extended for [`mileages`](#tag/Mileage-entries) and [`timeentries`](#tag/Time-entries). Affects all the exisiting versions.  | 16.2.0  | - [`employeegroups`](#operation/DeleteEmployeeGroupById) DELETE endpoint added. <br>- [`employees`](#operation/DeleteEmployeeById) DELETE endpoint added. <br>- [`project-employeegroups`](#operation/DeleteProjectEmployeeGroupById) DELETE endpoint added. <br>- [`project-employees`](#operation/DeleteProjectEmployeeById) DELETE endpoint added.  | 16.1.0  | [`Time entry prices`](#tag/Time-entry-prices) and [`Mileage entry prices`](#tag/Mileage-entry-prices) endpoints added.  | 16.0.0  | Changed parameter schema for [`mileages`](#operation/ApproveMileageEntries) and [`timeentries`](#operation/ApproveTimeEntries) approve endpoints.  | 15.0.0  | Added cost and sales accounts properties in [`activitygroups`](#tag/Activity-Groups) endpoints.  | 14.1.3  | - Added new filter for `IsAccessible` in [`activities`](#tag/Activities) endpoints. <br>- Added new filter for `IsBarred` in [`costtypes`](#tag/Cost-Types) endpoints.  | 14.1.2  | - Added input validations for [`activitygroups`](#tag/Activity-Groups). <br>- Updated description for [`projectgroups`](#operation/CreateProjectGroup) properties.  | 14.1.1  | Added input validations for [`projectgroups`](#operation/CreateProjectGroup).  | 14.1.0  | [`project-employees-count`](#operation/GetNumberOfProjectEmployees) endpoint added.                                                                                                                                                                                                                                               | 14.0.0  | - [`project-activities`](#tag/Project-Activities) endpoints added. <br>- `projects/activities` have been deprecated.|  | 13.2.0  | [`costtypegroups`](#tag/Cost-Type-Groups) endpoints added.|  | 13.1.0  | [`costtypes`](#tag/Cost-Types) endpoints added.|  | 13.0.0  | - [`projectgroups`](#operation/CreateProjectGroup) POST endpoint added, `Number` made non-required,<br>- [`activitygroups`](#operation/CreateActivityGroup) POST endpoint added, `Number` made non-required.|  | 12.0.0  | [`projects`](#tag/Projects) `Number` made non-required.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |  | 11.0.0  | [`employees`](#tag/Employees) `Number` made required.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |  | 10.1.2  | API version number moved to the server URL.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |  | 10.1.1  | - [`activities`](#operation/GetAllowedActivities) `employeeNumber` maximum value changed to 999999. <br>- [`projects`](#operation/GetPagedListOfProjectUnderEmployee) `employeeNumber` maximum value changed to 999999.                                                                                                                                                                                                                                                                                                                                                                                             |  | 10.1.0  | [`project-employees`](#operation/CreateProjectEmployee) POST endpoint added.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |  | 10.0.0  | - [`activities`](#tag/Activities) POST and PUT endpoints added. <br>- [`activitygroups`](#tag/Activity-Groups) GET endpoints added. <br>- Object version field added to `activities`, `projectstatuses` and `projectgroups` endpoints.                                                                                                                                                                                                                                                                                                                                                                              |  | 9.0.0   | `Project related settings for employee` resource renamed as `Project employee`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |  | 8.1.0   | [`project-customers`](#tag/Project-Customers) endpoints added.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |  | 8.0.0   | - [`employeegroups`](#tag/Employee-groups) endpoints added: GET all paginated, GET count, POST and PUT. <br>- [`project-employeegroups`](#tag/Project-employee-groups) endpoints added: GET all paginated, GET all cursor-based, GET count, GET by number, POST and PUT. <br> - Object version field added to employee groups endpoints.                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |  | 7.0.0   | [Projects related settings for employee](#tag/Project-employees) extended with new fields for Name, GroupNumber and IsBarred.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |  | 6.0.0   | Readonly property `IsReconciled` added to `TimeEntries` endpoint.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |  | 5.1.0   | [Project delete](#operation/DeleteProjectById) endpoint added.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |  | 5.0.0   | - Project-related properties such as `isUser`, `userId`, `canApprove`, `canInvoice`, `employeeType` in `/employees` moved to `/project-employees`. <br>- Properties `lastUpdated`, `costPrice`, `salesPrice` and `invoicedtotal` in `/projects` changed to readonly.<br>- Property `date` in `/timeentries` changed to mandatory.<br>- Access permission to `/employees` changed to requiring access to `Sales`.<br>- PUT endpoints for `/timeentries/{number}`, `/employees/{number}`, `/employeeprojectrelatedsettings/{number}` have been deprecated and new ones without `{number}` in the URL have been added. |  | 4.0.0   | `project.CustomerNumber` made non-required, range check introduced.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |  | 3.1.0   | Error messages of time entry approval improved, `timeEntry.IsApproved`, `mileage.IsApproved` and `mileage.IncludeApproval` made read-only.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |  | 3.0.0   | `mileage.Date` made required. Verification for `mileage.EmployeeNumber` and `mileage.Distance` added.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |  | 2.2.2   | Range check introduced in `projects.Number`, `employee.Number` and `employeeGroup.Number`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |  | 2.2.1   | Employees PATCH endpoint deprecated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |  | 2.2.0   | [`employeegroups/all`](#operation/GetAllEmployeeGroups) and [`employeegroups/{number}`](#operation/GetEmployeeGroupById) endpoints added.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |  | 2.1.0   | [`/activities/allowed`](#operation/GetAllowedActivities) endpoint added to get allowed activities for an employee and project.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |  | 2.0.0   | Open API released! Endpoints related to Projects module added.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |    </details>   # TL;DR    **Add these three headers to your requests.**    | Header                | Value                      | What is this?                                                |  | :-------------------- | :------------------------- | :----------------------------------------------------------- |  | X-AppSecretToken      | YOUR_PRIVATE_TOKEN         | This identifies your app. This is your secret token. Try using the value `demo`. |  | X-AgreementGrantToken | YOUR_AGREEMENT_GRANT_TOKEN | This identifies the grant issued by an agreement, to allow your app to access the agreements data. Try using the value `demo`. |  | Content-Type          | application/json           | We’re a JSON based API. This tells us that you agree with us on using JSON. |    ### Examples    #### jQuery    ```javascript/jQuery  $.ajax({      url: \"https://apis.e-conomic.com/api/v20.0.0/projects\",      dataType: \"json\",      headers: {          'X-AppSecretToken': \"demo\",          'X-AgreementGrantToken': \"demo\",          'Content-Type': \"application/json\"      },      type: \"GET\"  })      .always(function (data) {      $(\"#output\").text(JSON.stringify(data, null, 4));  });  ```    #### cURL    ```curl  curl -H \"X-AppSecretToken: demo\" -H \"X-AgreementGrantToken: demo\" https://apis.e-conomic.com/api/v20.0.0/projects  ```        # Introduction    Welcome to the **Visma e-conomic OpenAPI** documentation!    The e-conomic API is a document-based JSON REST API.     For more in-depth information about e-conomic itself, please have a look at the e-copedia [http://wiki.e-conomic.dk](http://wiki.e-conomic.dk/).    ## Usage    - **Generating a client** can easily be done using tools like [swagger-codegen](https://github.com/swagger-api/swagger-codegen) or others that work with [OpenAPI Specification](https://github.com/OAI/OpenAPI-Specification) specs.      ## Versioning    API releases are versioned using a three-part versioning scheme: `{major version}.{minor version}.{patch version}`.    We broadly follow [Semantic Versioning](https://semver.org/) principles when versioning the API. The major version number is incremented when a breaking change occurs.     The format is:    `/api/v{major version}.{minor version}.{patch version}/{resource-name}`    Each value of the above are integers and you should configure the specific version in each API call.     An example could be: `/api/v2.2.1/projects`    To track the changes of versions, please see our [changelog](#section/Changelog).    We reserve the right to deprecate versions at intervals since this allows for moving into a friendly environment for you faster.    ## Demo authentication    If you wish to try out the API before registering a developer agreement, you can do this by using the demo agreement, which mimics the authentication flow you will have to use when you create your app. All you have to do is specify HTTP header tokens `X-AgreementGrantToken: demo` and `X-AppSecretToken: demo`. Note however that you can only do GET requests with the demo agreement. If you want full access to our API's, you will need to register.    # Retrieving data    Our data is exposed as collections of items. Each item has many properties, with one property as a unique identifier, usually called `number` or `id`. You can always get a single item if you already know the unique identifier. In case the unique identifier is not known, you can always search the collection and retrieve an array of items that satisfy the search criteria, or retrieve only the count of items that satisfy the search criteria. When you search for items in a collection, you can always use filtering, sorting and pagination. When it comes to pagination, we offer two distinct approaches available on separate endpoints. You can read more about filtering, sorting and pagination in the following sections.     ## Filtering    Filtering is enabled on all collection endpoints but not on all properties.    Filtering on collections can be done using the query string parameter `filter`. A filter is made up of a set of predicates and follows a syntax inspired by mongoDB. A predicate is made up of a property name, an operator, and a value.    Example: `?filter=name$eq:Joe`    This matches all resources with the value Joe in the property name.    Predicates can be chained using either of the logical operators AND and OR.    Example: `?filter=name$eq:Joe$and:city$like:*port`    Filtering on strings is case insensitive.    #### Filterable properties  Information about what properties allow filtering and on what operators can be found in the property in the schema for the collection. Each property that allows filtering has the property `\"x-filterable\"` in combination with `operators` set. If you try to filter on something that isn’t allowed the server will respond with a status code 400.    #### Specifying Operator affinity  If you want to control the operator affinity then you can use parentheses.    An example is: `?filter=name$eq:Joe$and:(city$like:*port$or:age$lt:40)`    #### URL Encoding  URL parameter values should always be URL compatible. Always URL encode filter strings.    #### Filter Operators  The possible filtering operators are:    | Operator   | Syntax |  | --------   | ------ |  |Equals | $eq:|  |Not equals | $ne:|  |Greater than | $gt:|  |Greater than or equal | $gte:|  |Less than | $lt:|  |Less than or equal | $lte:|  |Substring match | $like:|  |And also | $and:|  |Or else | $or:|  |In | $in:|  |Not In | $nin:|    #### Substring matching    The `$like:` operator supports both using wildcards (*) and not using wildcards. If no wildcards are used, the expression is considered a `contains` expression and effectively becomes a filter with a wildcard at the start of the string and one at the end of the string. This operator is only allowed on some properties.    #### Escaping special characters in your filter  To not interfere with the parsing of the filter expression, certain escape sequences are necessary.    - “$” is escaped with “$$”  - “(” is escaped with “$(”  - “)” is escaped with “$)”  - “*” is escaped with “$*”  - “,” is escaped with “$,”  - “[” is escaped with “$[”  - “]” is escaped with “$]”    #### Using null values in your filter  Should you want to filter for the nonexistence of a property (i.e. null value) you can use the null escape sequence.    `$null:`    #### Using in and not in operators  To determine whether a specified value matches any value in (or not in) a list you filter using the `$in:` or `$nin:` operator. The list to filter by has to be enclosed in brackets and values separated by commas.    `customerNumber$in:[2,5,7,22,45]`      It is possible to also use the `$null:` keyword if you wish to include that in the filter. The max supported length of an array using the `$in:` or `$nin:` operator is 200.      ## Sorting    Sorting on strings is case insensitive.    ### Sort ascending    Sorting on collections can be done using the query string parameter ‘sort’.    ```  ?sort=name  ```    ### Sort descending    The default sort direction is ascending, but this can be turned by prepending a minus (-).    ```  ?sort=-name  ```    ### Sort by multiple properties    If you need to sort by multiple properties these can just be separated by commas. Mixing of directions is allowed.    ```  ?sort=-name,age  ```    ### Sort alphabetically    In certain cases, you might want to enforce that even numeric values are sorted alphabetically, so 1000 is less than 30. In those cases, you can prepend the sort property with a tilde (~).    ```  ?sort=~name  ```    #### Sortable properties  Information about what properties are sortable can be found in the schema for the collection. Each property that allows sorting has the property `\"x-sortable\": true` set.      ## Pagination    When it comes to retrieving a collection of items, you can use two distinct approaches:    * **Cursor-based pagination** (continued loading of items using a `cursor` as a query parameter to get the next page of items)    * This is the recommended approach, and the one you should use by default.    * The endpoint naming scheme is **\"Retrieve all `Items`\"**. (Usage: `/{ITEM}?cursor={CURSOR_VALUE}`)      * **Classic pagination** (limited functionality*. Specify `skippages` and `pagesize ` as query parameters to get a specific page of items)    * You should only consider using classic pagination, if you rely on loading pages (i.e. for list views or table/grid-based UI's).    * The endpoint naming scheme is **\"Retrieve a page of `Items`\"**. (Usage: `/{ITEM}/paged?skippages=0&pagesize=20`)        \\* It's important to note that there is a limit of 10.000 items using this approach. Any items outside of the first 10.000 items will not be loaded.    Please bear in mind that the two approaches are supported by **separate endpoints**. To use classic pagination, add `/paged` to your request URL.    If you need to know the total count of items that you can expect to get from your search, you can use a separate endpoint called **\"Retrieve the number of `Items`\"**.    You can also use the result of this endpoint to calculate the pagination navigation buttons for a table/grid-based UI.      ### Which approach should you use?  We highly recommend that you use cursor-based pagination because:  - It is more performant and offers much faster retrieval of items;  - It can be used for very large collections of many thousands or millions of items, whereas classic pagination is limited to only returning 10.000 results, everything else is ignored;      Classic pagination is only appropriate when you have an app with a table/grid-based UI.    ### Cursor-based pagination    #### How it works    When you search for items in a large collection, the response will contain the first 1.000 items and a `cursor` that you can use in a subsequent request to get the next series of items. This way you can retrieve the next set of items only when needed (if 1.000 items suffice, you don't need to send a second request).    Please note that the cursor is currently the `id` of the first `item` on the next set and it should not be mistaken for the number of items which are yet to be displayed.  Also, if the cursor is not present in the response, it means that there are no more items in the results.    ##### Real world example    I want to retrieve all projects.    1) I send a request to `https://apis.e-conomic.com/api/v20.0.0/projects`     and get back an array of 1.000 projects, and a `cursor` with value `34781`      2) I send a request for the next items in the resulting collection:       `https://apis.e-conomic.com/api/v20.0.0/projects?cursor=34781`       and get back an array of 1.000 projects and a cursor with value `87695`      3) I send a request for the next items in the result:       `https://apis.e-conomic.com/api/v20.0.0/projects?cursor=87695`       and get back an array of 56 items and no cursor.       No cursor means I have retrieved all the projects, i.e. I have reached the end of the list.      ### Classic pagination    If no parameters are used, the collection endpoint returns 20 items at a time. URL parameters allow you to increase this to up to 100 items or to skip pages if necessary.    ##### Real world example    I want to show a grid with page size of 50 and pagination navigation buttons.    1) I send a request to see how many projects there are in the collection:       `https://apis.e-conomic.com/api/v20.0.0/projects/count`       I get the number of projects in the collection, `2056`, and I can calculate the number of pages to be 2056 divided by 50 = 40 with 6 as remainder, meaning I have 41 pages total. I can then use this to present the user the navigation buttons.      2) I send a request to retrieve the first page of projects that my user will see:       `https://apis.e-conomic.com/api/v20.0.0/projects/paged?pagesize=50&sort=name`       with this I get back an array of 50 projects, sorted alphabetically by the project name.      3) Now if the user wants to see page number 6, I'll send a new request, skipping the first 5 pages to get the projects from page number 6:       `https://apis.e-conomic.com/api/v20.0.0/projects/paged?pagesize=50&skippages=5&sort=name`       I get back an array of 50 projects, that belong to page number 6 when sorting alphabetically by the project name.        ### Number of items in a collection    As mentioned before we offer endpoint to get the count of items in the collection. You can also use this info for calculation of pagination navigation in case of classic pagination.    Example `https://apis.e-conomic.com/api/v20.0.0/projects/count`      ## HTTP Status Codes    The Open API returns these HTTP status codes.    | Code | Text                   | Description                                                  |  | :--- | :--------------------- | :----------------------------------------------------------- |  | 200  | OK                     | Everything is OK                                             |  | 201  | Created                | When you create resources, this is what you get. This will be accompanied by the created resource in the body and a location header with a link to the created resource. |  | 204  | No Content             | In certain cases there is nothing to return. So we will let you know by returning a 204. |  | 400  | Bad Request            | The request you made was somehow malformed. A malformed request could be failed validation on creation or updating. If you try to filter on something that isn’t filterable this is also what you’ll see. Whenever possible we will also try to include a developer hint to help you get around this issue. |  | 401  | Unauthorized           | The credentials you supplied us with weren’t correct, or perhaps you forgot them altogether. If an agreement has revoked the grant they gave your app, this is what you will see. |  | 403  | Forbidden              | You won’t necessarily have access to everything. So even though you were authorized we might still deny access to certain resources. This depends on the roles asked for when the grant was issued. |  | 404  | Not Found              | This is returned when you try to request something that doesn’t exist. This could be a resource that has been deleted or just a URL you tried to hack. If you see a lot of these, it could be an indication that you aren’t using the links provided by the API. You should never need to concatenate any URLs. The API should provide you with the links needed. |  | 405  | Method Not Allowed     | Not all endpoints support all HTTP methods. If you try issue a PUT request to a collection resource this is what you get. |  | 415  | Unsupported Media Type | Our API is a JSON api. If you ask us to give you anything else, we give you this, and tell you why in the JSON body of the response. |  | 500  | Internal Server Error  | We don’t like to see these, and they are flagged in our logs. When you see this, something went wrong on our end. Either try again, or contact our support. |      ## Required and Readonly Properties    Since OpenAPI allows client generation based on the specification, we decided to use the same model/schema in our for both read and write endpoints where possible.    This led us to chose not to have the Id/Number in the URL parameter for PUT requests, but to use the one from the body, so there is no confusion.    When a property is marked as `required` it means you need to provide a value on each POST and PUT requests.    When a property is marked as `readonly` it means you should provide the same value you get in the GET requests, or do not send the property in the JSON at all (skip it).    ## Custom resource encoding    For some resource ids (the direct URL path to a resource) the question of non-alphanumeric characters must be solved in REST APIs by either encoding or replacement to ensure URL compatibility.    In the e-conomic REST API a subset of non-alphanumeric characters are replaced using a custom scheme for resource URLs:    | Character        | Replacement |  | :--------------- | :---------- |  | “<”              | *0*         |  | “>”              | *1*         |  | “*”              | *2*         |  | “%”              | *3*         |  | “:”              | *4*         |  | “&”              | *5*         |  | “/”              | *6*         |  | “\\”              | *7*         |  | “_”              | *8*         |  | “ ” (whitespace) | *9*         |  | “?”              | *10*        |  | “.”              | *11*        |  | “#”              | *12*        |  | “+”              | *13*        |    Example: Product “My Awesome Product_Discount5%” Resource URL (self): https://apis.e-conomic.com/products/My_9_Awesome_9_Product_8_Discount5_3_    All other non-alphanumeric characters in resource URLs are standard URL encoded. Please refer to standard URL encoding for characters not mentioned above.    ## Implementation specifics    Helpful details to know when implementing e-conomic REST.    ### Booleans    Booleans should only be expected to be represented in responses when true. A false boolean is omitted from response body. The same logic applies to write operations such as POST and PUT.    ### Null values    Null values are omitted from the response body.    ### Nulling    We do not generally accept null as a value and a validation exception should be expected. To null a property you must exclude it from your JSON on the write operation.    ## Object version    ObjectVersion is the mechanism that enforces updates only on latest state of an object.  ObjectVersion property is mandatory in Put Requests.  ObjectVersion property is retrieved on Get Request and needs to be included in Put Request.  If object was modified between Get and Put requests, Put request will fail with error code `409 Conflict`    ```  {    \"message\": \"Update conflict. Version does not match.\",    \"developerHint\": \"The resource has been updated by another user. Retrieve the resource/object and try the update again. This is needed in order to prevent you from rolling back another user's update.\",    \"logId\": \"09580053-1141-4e7f-85e1-bed8600e0278\",    \"logTimeUtc\": \"2021-11-04T09:07:56\",    \"property\": \"version\"  }  ```    ## Custom extensions in OpenAPI specification    In the specification file, there are some custom extensions that developers can make use of when consuming endpoints.   Those extensions are always prefixed by `x-`.    1) `x-required-roles`: The list of roles that are required for each group of endpoints.  2) `x-error-codes`: The list of error codes that are potentially returned from each group of endpoints.  
 *
 * The version of the OpenAPI document: v20.0.0
 * Contact: api@e-conomic.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from './ApiClient';
import Activity from './model/Activity';
import ActivityCursorResults from './model/ActivityCursorResults';
import ActivityGroup from './model/ActivityGroup';
import ActivityGroupCursorResults from './model/ActivityGroupCursorResults';
import ActivityGroupType from './model/ActivityGroupType';
import CostGroupType from './model/CostGroupType';
import CostType from './model/CostType';
import CostTypeCursorResults from './model/CostTypeCursorResults';
import CostTypeGroup from './model/CostTypeGroup';
import CostTypeGroupCursorResults from './model/CostTypeGroupCursorResults';
import CreatedResult from './model/CreatedResult';
import Employee from './model/Employee';
import EmployeeCursorResults from './model/EmployeeCursorResults';
import EmployeeGroup from './model/EmployeeGroup';
import EmployeeGroupCursorResults from './model/EmployeeGroupCursorResults';
import EmployeeType from './model/EmployeeType';
import Error from './model/Error';
import Mileage from './model/Mileage';
import MileageCursorResults from './model/MileageCursorResults';
import MileageNumbersCollection from './model/MileageNumbersCollection';
import MileagePrices from './model/MileagePrices';
import MileagePricesCursorResults from './model/MileagePricesCursorResults';
import OngoingAccountType from './model/OngoingAccountType';
import Project from './model/Project';
import ProjectActivity from './model/ProjectActivity';
import ProjectActivityCursorResults from './model/ProjectActivityCursorResults';
import ProjectCursorResults from './model/ProjectCursorResults';
import ProjectCustomer from './model/ProjectCustomer';
import ProjectCustomerCursorResults from './model/ProjectCustomerCursorResults';
import ProjectEmployee from './model/ProjectEmployee';
import ProjectEmployeeCursorResults from './model/ProjectEmployeeCursorResults';
import ProjectEmployeeGroup from './model/ProjectEmployeeGroup';
import ProjectEmployeeGroupCursorResults from './model/ProjectEmployeeGroupCursorResults';
import ProjectGroup from './model/ProjectGroup';
import ProjectGroupCursorResults from './model/ProjectGroupCursorResults';
import ProjectGroupType from './model/ProjectGroupType';
import ProjectStatus from './model/ProjectStatus';
import ProjectStatusCursorResults from './model/ProjectStatusCursorResults';
import ProjectStatusType from './model/ProjectStatusType';
import TimeEntry from './model/TimeEntry';
import TimeEntryCursorResults from './model/TimeEntryCursorResults';
import TimeEntryNumbersCollection from './model/TimeEntryNumbersCollection';
import TimeEntryPrices from './model/TimeEntryPrices';
import TimeEntryPricesCursorResults from './model/TimeEntryPricesCursorResults';
import ActivitiesApi from './api/ActivitiesApi';
import ActivityGroupsApi from './api/ActivityGroupsApi';
import CostTypeGroupsApi from './api/CostTypeGroupsApi';
import CostTypesApi from './api/CostTypesApi';
import EmployeeGroupsApi from './api/EmployeeGroupsApi';
import EmployeesApi from './api/EmployeesApi';
import MileageEntriesApi from './api/MileageEntriesApi';
import MileageEntryPricesApi from './api/MileageEntryPricesApi';
import MileagesApi from './api/MileagesApi';
import ProjectActivitiesApi from './api/ProjectActivitiesApi';
import ProjectCustomersApi from './api/ProjectCustomersApi';
import ProjectEmployeeGroupsApi from './api/ProjectEmployeeGroupsApi';
import ProjectEmployeesApi from './api/ProjectEmployeesApi';
import ProjectGroupsApi from './api/ProjectGroupsApi';
import ProjectStatusesApi from './api/ProjectStatusesApi';
import ProjectsApi from './api/ProjectsApi';
import TimeEntriesApi from './api/TimeEntriesApi';
import TimeEntryPricesApi from './api/TimeEntryPricesApi';


/**
* # Changelog    &lt;details&gt;    &lt;summary&gt;Click to see changelog.&lt;/summary&gt;    | Version | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |  |---------| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |  | 20.0.0  | Customer contacts and delivery locations endpoints deprecated. You can find the same enpoints in [&#x60;Customers API&#x60;](https://apis.e-conomic.com/#Customers)   | 19.0.0  | Page-based endpoints were moved under /paged url and cursor-based endpoints dropped the /all.  | 18.0.0  | Added isDeleted flag to [&#x60;customer-contacts&#x60;](#tag/Customer-contacts) and included deleted contacts in the response. &lt;br&gt; Deleted contacts can be used for history purposes, but cannot be set as reference persons on sales documents. &lt;br&gt; In previous versions only customer-contacts/id returns deleted contacts as well.  | 17.0.2  | &#x60;TimeEntryEmployeeNumberCannotBeUpdated&#x60; and &#x60;MileageEmployeeNumberCannotBeUpdated&#x60; error codes removed. The change affects all versions, but we bumped the version for transparency.  | 17.0.1  | New custom [&#x60;OpenAPI extension&#x60;](#section/Retrieving-data/Custom-extensions-in-OpenAPI-specification) added in the specification: &#x60;x-error-codes&#x60;. Existing &#x60;x-required-roles&#x60; extension converted to an array of strings.  | 17.0.0  | Improved the error model. Added &#x60;code&#x60; and &#x60;property&#x60; fields to the model. &#x60;code&#x60; represents the error code. &#x60;property&#x60; is the field name on which the input validation failed.  | 16.4.0  | [&#x60;customer-deliverylocations&#x60;](#tag/Customer-delivery-locations) endpoints added.  | 16.3.0  | [&#x60;customer-contacts&#x60;](#tag/Customer-contacts) endpoints added.    | 16.2.2  | Added input validations for required string properties, if a string property is required it can&#39;t be empty, it should contain at least 1 character.  | 16.2.1  | Error codes extended for [&#x60;mileages&#x60;](#tag/Mileage-entries) and [&#x60;timeentries&#x60;](#tag/Time-entries). Affects all the exisiting versions.  | 16.2.0  | - [&#x60;employeegroups&#x60;](#operation/DeleteEmployeeGroupById) DELETE endpoint added. &lt;br&gt;- [&#x60;employees&#x60;](#operation/DeleteEmployeeById) DELETE endpoint added. &lt;br&gt;- [&#x60;project-employeegroups&#x60;](#operation/DeleteProjectEmployeeGroupById) DELETE endpoint added. &lt;br&gt;- [&#x60;project-employees&#x60;](#operation/DeleteProjectEmployeeById) DELETE endpoint added.  | 16.1.0  | [&#x60;Time entry prices&#x60;](#tag/Time-entry-prices) and [&#x60;Mileage entry prices&#x60;](#tag/Mileage-entry-prices) endpoints added.  | 16.0.0  | Changed parameter schema for [&#x60;mileages&#x60;](#operation/ApproveMileageEntries) and [&#x60;timeentries&#x60;](#operation/ApproveTimeEntries) approve endpoints.  | 15.0.0  | Added cost and sales accounts properties in [&#x60;activitygroups&#x60;](#tag/Activity-Groups) endpoints.  | 14.1.3  | - Added new filter for &#x60;IsAccessible&#x60; in [&#x60;activities&#x60;](#tag/Activities) endpoints. &lt;br&gt;- Added new filter for &#x60;IsBarred&#x60; in [&#x60;costtypes&#x60;](#tag/Cost-Types) endpoints.  | 14.1.2  | - Added input validations for [&#x60;activitygroups&#x60;](#tag/Activity-Groups). &lt;br&gt;- Updated description for [&#x60;projectgroups&#x60;](#operation/CreateProjectGroup) properties.  | 14.1.1  | Added input validations for [&#x60;projectgroups&#x60;](#operation/CreateProjectGroup).  | 14.1.0  | [&#x60;project-employees-count&#x60;](#operation/GetNumberOfProjectEmployees) endpoint added.                                                                                                                                                                                                                                               | 14.0.0  | - [&#x60;project-activities&#x60;](#tag/Project-Activities) endpoints added. &lt;br&gt;- &#x60;projects/activities&#x60; have been deprecated.|  | 13.2.0  | [&#x60;costtypegroups&#x60;](#tag/Cost-Type-Groups) endpoints added.|  | 13.1.0  | [&#x60;costtypes&#x60;](#tag/Cost-Types) endpoints added.|  | 13.0.0  | - [&#x60;projectgroups&#x60;](#operation/CreateProjectGroup) POST endpoint added, &#x60;Number&#x60; made non-required,&lt;br&gt;- [&#x60;activitygroups&#x60;](#operation/CreateActivityGroup) POST endpoint added, &#x60;Number&#x60; made non-required.|  | 12.0.0  | [&#x60;projects&#x60;](#tag/Projects) &#x60;Number&#x60; made non-required.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |  | 11.0.0  | [&#x60;employees&#x60;](#tag/Employees) &#x60;Number&#x60; made required.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |  | 10.1.2  | API version number moved to the server URL.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |  | 10.1.1  | - [&#x60;activities&#x60;](#operation/GetAllowedActivities) &#x60;employeeNumber&#x60; maximum value changed to 999999. &lt;br&gt;- [&#x60;projects&#x60;](#operation/GetPagedListOfProjectUnderEmployee) &#x60;employeeNumber&#x60; maximum value changed to 999999.                                                                                                                                                                                                                                                                                                                                                                                             |  | 10.1.0  | [&#x60;project-employees&#x60;](#operation/CreateProjectEmployee) POST endpoint added.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |  | 10.0.0  | - [&#x60;activities&#x60;](#tag/Activities) POST and PUT endpoints added. &lt;br&gt;- [&#x60;activitygroups&#x60;](#tag/Activity-Groups) GET endpoints added. &lt;br&gt;- Object version field added to &#x60;activities&#x60;, &#x60;projectstatuses&#x60; and &#x60;projectgroups&#x60; endpoints.                                                                                                                                                                                                                                                                                                                                                                              |  | 9.0.0   | &#x60;Project related settings for employee&#x60; resource renamed as &#x60;Project employee&#x60;.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |  | 8.1.0   | [&#x60;project-customers&#x60;](#tag/Project-Customers) endpoints added.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |  | 8.0.0   | - [&#x60;employeegroups&#x60;](#tag/Employee-groups) endpoints added: GET all paginated, GET count, POST and PUT. &lt;br&gt;- [&#x60;project-employeegroups&#x60;](#tag/Project-employee-groups) endpoints added: GET all paginated, GET all cursor-based, GET count, GET by number, POST and PUT. &lt;br&gt; - Object version field added to employee groups endpoints.                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |  | 7.0.0   | [Projects related settings for employee](#tag/Project-employees) extended with new fields for Name, GroupNumber and IsBarred.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |  | 6.0.0   | Readonly property &#x60;IsReconciled&#x60; added to &#x60;TimeEntries&#x60; endpoint.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |  | 5.1.0   | [Project delete](#operation/DeleteProjectById) endpoint added.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |  | 5.0.0   | - Project-related properties such as &#x60;isUser&#x60;, &#x60;userId&#x60;, &#x60;canApprove&#x60;, &#x60;canInvoice&#x60;, &#x60;employeeType&#x60; in &#x60;/employees&#x60; moved to &#x60;/project-employees&#x60;. &lt;br&gt;- Properties &#x60;lastUpdated&#x60;, &#x60;costPrice&#x60;, &#x60;salesPrice&#x60; and &#x60;invoicedtotal&#x60; in &#x60;/projects&#x60; changed to readonly.&lt;br&gt;- Property &#x60;date&#x60; in &#x60;/timeentries&#x60; changed to mandatory.&lt;br&gt;- Access permission to &#x60;/employees&#x60; changed to requiring access to &#x60;Sales&#x60;.&lt;br&gt;- PUT endpoints for &#x60;/timeentries/{number}&#x60;, &#x60;/employees/{number}&#x60;, &#x60;/employeeprojectrelatedsettings/{number}&#x60; have been deprecated and new ones without &#x60;{number}&#x60; in the URL have been added. |  | 4.0.0   | &#x60;project.CustomerNumber&#x60; made non-required, range check introduced.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |  | 3.1.0   | Error messages of time entry approval improved, &#x60;timeEntry.IsApproved&#x60;, &#x60;mileage.IsApproved&#x60; and &#x60;mileage.IncludeApproval&#x60; made read-only.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |  | 3.0.0   | &#x60;mileage.Date&#x60; made required. Verification for &#x60;mileage.EmployeeNumber&#x60; and &#x60;mileage.Distance&#x60; added.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |  | 2.2.2   | Range check introduced in &#x60;projects.Number&#x60;, &#x60;employee.Number&#x60; and &#x60;employeeGroup.Number&#x60;.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |  | 2.2.1   | Employees PATCH endpoint deprecated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |  | 2.2.0   | [&#x60;employeegroups/all&#x60;](#operation/GetAllEmployeeGroups) and [&#x60;employeegroups/{number}&#x60;](#operation/GetEmployeeGroupById) endpoints added.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |  | 2.1.0   | [&#x60;/activities/allowed&#x60;](#operation/GetAllowedActivities) endpoint added to get allowed activities for an employee and project.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |  | 2.0.0   | Open API released! Endpoints related to Projects module added.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |    &lt;/details&gt;   # TL;DR    **Add these three headers to your requests.**    | Header                | Value                      | What is this?                                                |  | :-------------------- | :------------------------- | :----------------------------------------------------------- |  | X-AppSecretToken      | YOUR_PRIVATE_TOKEN         | This identifies your app. This is your secret token. Try using the value &#x60;demo&#x60;. |  | X-AgreementGrantToken | YOUR_AGREEMENT_GRANT_TOKEN | This identifies the grant issued by an agreement, to allow your app to access the agreements data. Try using the value &#x60;demo&#x60;. |  | Content-Type          | application/json           | We’re a JSON based API. This tells us that you agree with us on using JSON. |    ### Examples    #### jQuery    &#x60;&#x60;&#x60;javascript/jQuery  $.ajax({      url: \&quot;https://apis.e-conomic.com/api/v20.0.0/projects\&quot;,      dataType: \&quot;json\&quot;,      headers: {          &#39;X-AppSecretToken&#39;: \&quot;demo\&quot;,          &#39;X-AgreementGrantToken&#39;: \&quot;demo\&quot;,          &#39;Content-Type&#39;: \&quot;application/json\&quot;      },      type: \&quot;GET\&quot;  })      .always(function (data) {      $(\&quot;#output\&quot;).text(JSON.stringify(data, null, 4));  });  &#x60;&#x60;&#x60;    #### cURL    &#x60;&#x60;&#x60;curl  curl -H \&quot;X-AppSecretToken: demo\&quot; -H \&quot;X-AgreementGrantToken: demo\&quot; https://apis.e-conomic.com/api/v20.0.0/projects  &#x60;&#x60;&#x60;        # Introduction    Welcome to the **Visma e-conomic OpenAPI** documentation!    The e-conomic API is a document-based JSON REST API.     For more in-depth information about e-conomic itself, please have a look at the e-copedia [http://wiki.e-conomic.dk](http://wiki.e-conomic.dk/).    ## Usage    - **Generating a client** can easily be done using tools like [swagger-codegen](https://github.com/swagger-api/swagger-codegen) or others that work with [OpenAPI Specification](https://github.com/OAI/OpenAPI-Specification) specs.      ## Versioning    API releases are versioned using a three-part versioning scheme: &#x60;{major version}.{minor version}.{patch version}&#x60;.    We broadly follow [Semantic Versioning](https://semver.org/) principles when versioning the API. The major version number is incremented when a breaking change occurs.     The format is:    &#x60;/api/v{major version}.{minor version}.{patch version}/{resource-name}&#x60;    Each value of the above are integers and you should configure the specific version in each API call.     An example could be: &#x60;/api/v2.2.1/projects&#x60;    To track the changes of versions, please see our [changelog](#section/Changelog).    We reserve the right to deprecate versions at intervals since this allows for moving into a friendly environment for you faster.    ## Demo authentication    If you wish to try out the API before registering a developer agreement, you can do this by using the demo agreement, which mimics the authentication flow you will have to use when you create your app. All you have to do is specify HTTP header tokens &#x60;X-AgreementGrantToken: demo&#x60; and &#x60;X-AppSecretToken: demo&#x60;. Note however that you can only do GET requests with the demo agreement. If you want full access to our API&#39;s, you will need to register.    # Retrieving data    Our data is exposed as collections of items. Each item has many properties, with one property as a unique identifier, usually called &#x60;number&#x60; or &#x60;id&#x60;. You can always get a single item if you already know the unique identifier. In case the unique identifier is not known, you can always search the collection and retrieve an array of items that satisfy the search criteria, or retrieve only the count of items that satisfy the search criteria. When you search for items in a collection, you can always use filtering, sorting and pagination. When it comes to pagination, we offer two distinct approaches available on separate endpoints. You can read more about filtering, sorting and pagination in the following sections.     ## Filtering    Filtering is enabled on all collection endpoints but not on all properties.    Filtering on collections can be done using the query string parameter &#x60;filter&#x60;. A filter is made up of a set of predicates and follows a syntax inspired by mongoDB. A predicate is made up of a property name, an operator, and a value.    Example: &#x60;?filter&#x3D;name$eq:Joe&#x60;    This matches all resources with the value Joe in the property name.    Predicates can be chained using either of the logical operators AND and OR.    Example: &#x60;?filter&#x3D;name$eq:Joe$and:city$like:*port&#x60;    Filtering on strings is case insensitive.    #### Filterable properties  Information about what properties allow filtering and on what operators can be found in the property in the schema for the collection. Each property that allows filtering has the property &#x60;\&quot;x-filterable\&quot;&#x60; in combination with &#x60;operators&#x60; set. If you try to filter on something that isn’t allowed the server will respond with a status code 400.    #### Specifying Operator affinity  If you want to control the operator affinity then you can use parentheses.    An example is: &#x60;?filter&#x3D;name$eq:Joe$and:(city$like:*port$or:age$lt:40)&#x60;    #### URL Encoding  URL parameter values should always be URL compatible. Always URL encode filter strings.    #### Filter Operators  The possible filtering operators are:    | Operator   | Syntax |  | --------   | ------ |  |Equals | $eq:|  |Not equals | $ne:|  |Greater than | $gt:|  |Greater than or equal | $gte:|  |Less than | $lt:|  |Less than or equal | $lte:|  |Substring match | $like:|  |And also | $and:|  |Or else | $or:|  |In | $in:|  |Not In | $nin:|    #### Substring matching    The &#x60;$like:&#x60; operator supports both using wildcards (*) and not using wildcards. If no wildcards are used, the expression is considered a &#x60;contains&#x60; expression and effectively becomes a filter with a wildcard at the start of the string and one at the end of the string. This operator is only allowed on some properties.    #### Escaping special characters in your filter  To not interfere with the parsing of the filter expression, certain escape sequences are necessary.    - “$” is escaped with “$$”  - “(” is escaped with “$(”  - “)” is escaped with “$)”  - “*” is escaped with “$*”  - “,” is escaped with “$,”  - “[” is escaped with “$[”  - “]” is escaped with “$]”    #### Using null values in your filter  Should you want to filter for the nonexistence of a property (i.e. null value) you can use the null escape sequence.    &#x60;$null:&#x60;    #### Using in and not in operators  To determine whether a specified value matches any value in (or not in) a list you filter using the &#x60;$in:&#x60; or &#x60;$nin:&#x60; operator. The list to filter by has to be enclosed in brackets and values separated by commas.    &#x60;customerNumber$in:[2,5,7,22,45]&#x60;      It is possible to also use the &#x60;$null:&#x60; keyword if you wish to include that in the filter. The max supported length of an array using the &#x60;$in:&#x60; or &#x60;$nin:&#x60; operator is 200.      ## Sorting    Sorting on strings is case insensitive.    ### Sort ascending    Sorting on collections can be done using the query string parameter ‘sort’.    &#x60;&#x60;&#x60;  ?sort&#x3D;name  &#x60;&#x60;&#x60;    ### Sort descending    The default sort direction is ascending, but this can be turned by prepending a minus (-).    &#x60;&#x60;&#x60;  ?sort&#x3D;-name  &#x60;&#x60;&#x60;    ### Sort by multiple properties    If you need to sort by multiple properties these can just be separated by commas. Mixing of directions is allowed.    &#x60;&#x60;&#x60;  ?sort&#x3D;-name,age  &#x60;&#x60;&#x60;    ### Sort alphabetically    In certain cases, you might want to enforce that even numeric values are sorted alphabetically, so 1000 is less than 30. In those cases, you can prepend the sort property with a tilde (~).    &#x60;&#x60;&#x60;  ?sort&#x3D;~name  &#x60;&#x60;&#x60;    #### Sortable properties  Information about what properties are sortable can be found in the schema for the collection. Each property that allows sorting has the property &#x60;\&quot;x-sortable\&quot;: true&#x60; set.      ## Pagination    When it comes to retrieving a collection of items, you can use two distinct approaches:    * **Cursor-based pagination** (continued loading of items using a &#x60;cursor&#x60; as a query parameter to get the next page of items)    * This is the recommended approach, and the one you should use by default.    * The endpoint naming scheme is **\&quot;Retrieve all &#x60;Items&#x60;\&quot;**. (Usage: &#x60;/{ITEM}?cursor&#x3D;{CURSOR_VALUE}&#x60;)      * **Classic pagination** (limited functionality*. Specify &#x60;skippages&#x60; and &#x60;pagesize &#x60; as query parameters to get a specific page of items)    * You should only consider using classic pagination, if you rely on loading pages (i.e. for list views or table/grid-based UI&#39;s).    * The endpoint naming scheme is **\&quot;Retrieve a page of &#x60;Items&#x60;\&quot;**. (Usage: &#x60;/{ITEM}/paged?skippages&#x3D;0&amp;pagesize&#x3D;20&#x60;)        \\* It&#39;s important to note that there is a limit of 10.000 items using this approach. Any items outside of the first 10.000 items will not be loaded.    Please bear in mind that the two approaches are supported by **separate endpoints**. To use classic pagination, add &#x60;/paged&#x60; to your request URL.    If you need to know the total count of items that you can expect to get from your search, you can use a separate endpoint called **\&quot;Retrieve the number of &#x60;Items&#x60;\&quot;**.    You can also use the result of this endpoint to calculate the pagination navigation buttons for a table/grid-based UI.      ### Which approach should you use?  We highly recommend that you use cursor-based pagination because:  - It is more performant and offers much faster retrieval of items;  - It can be used for very large collections of many thousands or millions of items, whereas classic pagination is limited to only returning 10.000 results, everything else is ignored;      Classic pagination is only appropriate when you have an app with a table/grid-based UI.    ### Cursor-based pagination    #### How it works    When you search for items in a large collection, the response will contain the first 1.000 items and a &#x60;cursor&#x60; that you can use in a subsequent request to get the next series of items. This way you can retrieve the next set of items only when needed (if 1.000 items suffice, you don&#39;t need to send a second request).    Please note that the cursor is currently the &#x60;id&#x60; of the first &#x60;item&#x60; on the next set and it should not be mistaken for the number of items which are yet to be displayed.  Also, if the cursor is not present in the response, it means that there are no more items in the results.    ##### Real world example    I want to retrieve all projects.    1) I send a request to &#x60;https://apis.e-conomic.com/api/v20.0.0/projects&#x60;     and get back an array of 1.000 projects, and a &#x60;cursor&#x60; with value &#x60;34781&#x60;      2) I send a request for the next items in the resulting collection:       &#x60;https://apis.e-conomic.com/api/v20.0.0/projects?cursor&#x3D;34781&#x60;       and get back an array of 1.000 projects and a cursor with value &#x60;87695&#x60;      3) I send a request for the next items in the result:       &#x60;https://apis.e-conomic.com/api/v20.0.0/projects?cursor&#x3D;87695&#x60;       and get back an array of 56 items and no cursor.       No cursor means I have retrieved all the projects, i.e. I have reached the end of the list.      ### Classic pagination    If no parameters are used, the collection endpoint returns 20 items at a time. URL parameters allow you to increase this to up to 100 items or to skip pages if necessary.    ##### Real world example    I want to show a grid with page size of 50 and pagination navigation buttons.    1) I send a request to see how many projects there are in the collection:       &#x60;https://apis.e-conomic.com/api/v20.0.0/projects/count&#x60;       I get the number of projects in the collection, &#x60;2056&#x60;, and I can calculate the number of pages to be 2056 divided by 50 &#x3D; 40 with 6 as remainder, meaning I have 41 pages total. I can then use this to present the user the navigation buttons.      2) I send a request to retrieve the first page of projects that my user will see:       &#x60;https://apis.e-conomic.com/api/v20.0.0/projects/paged?pagesize&#x3D;50&amp;sort&#x3D;name&#x60;       with this I get back an array of 50 projects, sorted alphabetically by the project name.      3) Now if the user wants to see page number 6, I&#39;ll send a new request, skipping the first 5 pages to get the projects from page number 6:       &#x60;https://apis.e-conomic.com/api/v20.0.0/projects/paged?pagesize&#x3D;50&amp;skippages&#x3D;5&amp;sort&#x3D;name&#x60;       I get back an array of 50 projects, that belong to page number 6 when sorting alphabetically by the project name.        ### Number of items in a collection    As mentioned before we offer endpoint to get the count of items in the collection. You can also use this info for calculation of pagination navigation in case of classic pagination.    Example &#x60;https://apis.e-conomic.com/api/v20.0.0/projects/count&#x60;      ## HTTP Status Codes    The Open API returns these HTTP status codes.    | Code | Text                   | Description                                                  |  | :--- | :--------------------- | :----------------------------------------------------------- |  | 200  | OK                     | Everything is OK                                             |  | 201  | Created                | When you create resources, this is what you get. This will be accompanied by the created resource in the body and a location header with a link to the created resource. |  | 204  | No Content             | In certain cases there is nothing to return. So we will let you know by returning a 204. |  | 400  | Bad Request            | The request you made was somehow malformed. A malformed request could be failed validation on creation or updating. If you try to filter on something that isn’t filterable this is also what you’ll see. Whenever possible we will also try to include a developer hint to help you get around this issue. |  | 401  | Unauthorized           | The credentials you supplied us with weren’t correct, or perhaps you forgot them altogether. If an agreement has revoked the grant they gave your app, this is what you will see. |  | 403  | Forbidden              | You won’t necessarily have access to everything. So even though you were authorized we might still deny access to certain resources. This depends on the roles asked for when the grant was issued. |  | 404  | Not Found              | This is returned when you try to request something that doesn’t exist. This could be a resource that has been deleted or just a URL you tried to hack. If you see a lot of these, it could be an indication that you aren’t using the links provided by the API. You should never need to concatenate any URLs. The API should provide you with the links needed. |  | 405  | Method Not Allowed     | Not all endpoints support all HTTP methods. If you try issue a PUT request to a collection resource this is what you get. |  | 415  | Unsupported Media Type | Our API is a JSON api. If you ask us to give you anything else, we give you this, and tell you why in the JSON body of the response. |  | 500  | Internal Server Error  | We don’t like to see these, and they are flagged in our logs. When you see this, something went wrong on our end. Either try again, or contact our support. |      ## Required and Readonly Properties    Since OpenAPI allows client generation based on the specification, we decided to use the same model/schema in our for both read and write endpoints where possible.    This led us to chose not to have the Id/Number in the URL parameter for PUT requests, but to use the one from the body, so there is no confusion.    When a property is marked as &#x60;required&#x60; it means you need to provide a value on each POST and PUT requests.    When a property is marked as &#x60;readonly&#x60; it means you should provide the same value you get in the GET requests, or do not send the property in the JSON at all (skip it).    ## Custom resource encoding    For some resource ids (the direct URL path to a resource) the question of non-alphanumeric characters must be solved in REST APIs by either encoding or replacement to ensure URL compatibility.    In the e-conomic REST API a subset of non-alphanumeric characters are replaced using a custom scheme for resource URLs:    | Character        | Replacement |  | :--------------- | :---------- |  | “&lt;”              | *0*         |  | “&gt;”              | *1*         |  | “*”              | *2*         |  | “%”              | *3*         |  | “:”              | *4*         |  | “&amp;”              | *5*         |  | “/”              | *6*         |  | “\\”              | *7*         |  | “_”              | *8*         |  | “ ” (whitespace) | *9*         |  | “?”              | *10*        |  | “.”              | *11*        |  | “#”              | *12*        |  | “+”              | *13*        |    Example: Product “My Awesome Product_Discount5%” Resource URL (self): https://apis.e-conomic.com/products/My_9_Awesome_9_Product_8_Discount5_3_    All other non-alphanumeric characters in resource URLs are standard URL encoded. Please refer to standard URL encoding for characters not mentioned above.    ## Implementation specifics    Helpful details to know when implementing e-conomic REST.    ### Booleans    Booleans should only be expected to be represented in responses when true. A false boolean is omitted from response body. The same logic applies to write operations such as POST and PUT.    ### Null values    Null values are omitted from the response body.    ### Nulling    We do not generally accept null as a value and a validation exception should be expected. To null a property you must exclude it from your JSON on the write operation.    ## Object version    ObjectVersion is the mechanism that enforces updates only on latest state of an object.  ObjectVersion property is mandatory in Put Requests.  ObjectVersion property is retrieved on Get Request and needs to be included in Put Request.  If object was modified between Get and Put requests, Put request will fail with error code &#x60;409 Conflict&#x60;    &#x60;&#x60;&#x60;  {    \&quot;message\&quot;: \&quot;Update conflict. Version does not match.\&quot;,    \&quot;developerHint\&quot;: \&quot;The resource has been updated by another user. Retrieve the resource/object and try the update again. This is needed in order to prevent you from rolling back another user&#39;s update.\&quot;,    \&quot;logId\&quot;: \&quot;09580053-1141-4e7f-85e1-bed8600e0278\&quot;,    \&quot;logTimeUtc\&quot;: \&quot;2021-11-04T09:07:56\&quot;,    \&quot;property\&quot;: \&quot;version\&quot;  }  &#x60;&#x60;&#x60;    ## Custom extensions in OpenAPI specification    In the specification file, there are some custom extensions that developers can make use of when consuming endpoints.   Those extensions are always prefixed by &#x60;x-&#x60;.    1) &#x60;x-required-roles&#x60;: The list of roles that are required for each group of endpoints.  2) &#x60;x-error-codes&#x60;: The list of error codes that are potentially returned from each group of endpoints.  .<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var VismaEConomicOpenApi = require('index'); // See note below*.
* var xxxSvc = new VismaEConomicOpenApi.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new VismaEConomicOpenApi.Yyy(); // Construct a model instance.
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
* var xxxSvc = new VismaEConomicOpenApi.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new VismaEConomicOpenApi.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version v20.0.0
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The Activity model constructor.
     * @property {module:model/Activity}
     */
    Activity,

    /**
     * The ActivityCursorResults model constructor.
     * @property {module:model/ActivityCursorResults}
     */
    ActivityCursorResults,

    /**
     * The ActivityGroup model constructor.
     * @property {module:model/ActivityGroup}
     */
    ActivityGroup,

    /**
     * The ActivityGroupCursorResults model constructor.
     * @property {module:model/ActivityGroupCursorResults}
     */
    ActivityGroupCursorResults,

    /**
     * The ActivityGroupType model constructor.
     * @property {module:model/ActivityGroupType}
     */
    ActivityGroupType,

    /**
     * The CostGroupType model constructor.
     * @property {module:model/CostGroupType}
     */
    CostGroupType,

    /**
     * The CostType model constructor.
     * @property {module:model/CostType}
     */
    CostType,

    /**
     * The CostTypeCursorResults model constructor.
     * @property {module:model/CostTypeCursorResults}
     */
    CostTypeCursorResults,

    /**
     * The CostTypeGroup model constructor.
     * @property {module:model/CostTypeGroup}
     */
    CostTypeGroup,

    /**
     * The CostTypeGroupCursorResults model constructor.
     * @property {module:model/CostTypeGroupCursorResults}
     */
    CostTypeGroupCursorResults,

    /**
     * The CreatedResult model constructor.
     * @property {module:model/CreatedResult}
     */
    CreatedResult,

    /**
     * The Employee model constructor.
     * @property {module:model/Employee}
     */
    Employee,

    /**
     * The EmployeeCursorResults model constructor.
     * @property {module:model/EmployeeCursorResults}
     */
    EmployeeCursorResults,

    /**
     * The EmployeeGroup model constructor.
     * @property {module:model/EmployeeGroup}
     */
    EmployeeGroup,

    /**
     * The EmployeeGroupCursorResults model constructor.
     * @property {module:model/EmployeeGroupCursorResults}
     */
    EmployeeGroupCursorResults,

    /**
     * The EmployeeType model constructor.
     * @property {module:model/EmployeeType}
     */
    EmployeeType,

    /**
     * The Error model constructor.
     * @property {module:model/Error}
     */
    Error,

    /**
     * The Mileage model constructor.
     * @property {module:model/Mileage}
     */
    Mileage,

    /**
     * The MileageCursorResults model constructor.
     * @property {module:model/MileageCursorResults}
     */
    MileageCursorResults,

    /**
     * The MileageNumbersCollection model constructor.
     * @property {module:model/MileageNumbersCollection}
     */
    MileageNumbersCollection,

    /**
     * The MileagePrices model constructor.
     * @property {module:model/MileagePrices}
     */
    MileagePrices,

    /**
     * The MileagePricesCursorResults model constructor.
     * @property {module:model/MileagePricesCursorResults}
     */
    MileagePricesCursorResults,

    /**
     * The OngoingAccountType model constructor.
     * @property {module:model/OngoingAccountType}
     */
    OngoingAccountType,

    /**
     * The Project model constructor.
     * @property {module:model/Project}
     */
    Project,

    /**
     * The ProjectActivity model constructor.
     * @property {module:model/ProjectActivity}
     */
    ProjectActivity,

    /**
     * The ProjectActivityCursorResults model constructor.
     * @property {module:model/ProjectActivityCursorResults}
     */
    ProjectActivityCursorResults,

    /**
     * The ProjectCursorResults model constructor.
     * @property {module:model/ProjectCursorResults}
     */
    ProjectCursorResults,

    /**
     * The ProjectCustomer model constructor.
     * @property {module:model/ProjectCustomer}
     */
    ProjectCustomer,

    /**
     * The ProjectCustomerCursorResults model constructor.
     * @property {module:model/ProjectCustomerCursorResults}
     */
    ProjectCustomerCursorResults,

    /**
     * The ProjectEmployee model constructor.
     * @property {module:model/ProjectEmployee}
     */
    ProjectEmployee,

    /**
     * The ProjectEmployeeCursorResults model constructor.
     * @property {module:model/ProjectEmployeeCursorResults}
     */
    ProjectEmployeeCursorResults,

    /**
     * The ProjectEmployeeGroup model constructor.
     * @property {module:model/ProjectEmployeeGroup}
     */
    ProjectEmployeeGroup,

    /**
     * The ProjectEmployeeGroupCursorResults model constructor.
     * @property {module:model/ProjectEmployeeGroupCursorResults}
     */
    ProjectEmployeeGroupCursorResults,

    /**
     * The ProjectGroup model constructor.
     * @property {module:model/ProjectGroup}
     */
    ProjectGroup,

    /**
     * The ProjectGroupCursorResults model constructor.
     * @property {module:model/ProjectGroupCursorResults}
     */
    ProjectGroupCursorResults,

    /**
     * The ProjectGroupType model constructor.
     * @property {module:model/ProjectGroupType}
     */
    ProjectGroupType,

    /**
     * The ProjectStatus model constructor.
     * @property {module:model/ProjectStatus}
     */
    ProjectStatus,

    /**
     * The ProjectStatusCursorResults model constructor.
     * @property {module:model/ProjectStatusCursorResults}
     */
    ProjectStatusCursorResults,

    /**
     * The ProjectStatusType model constructor.
     * @property {module:model/ProjectStatusType}
     */
    ProjectStatusType,

    /**
     * The TimeEntry model constructor.
     * @property {module:model/TimeEntry}
     */
    TimeEntry,

    /**
     * The TimeEntryCursorResults model constructor.
     * @property {module:model/TimeEntryCursorResults}
     */
    TimeEntryCursorResults,

    /**
     * The TimeEntryNumbersCollection model constructor.
     * @property {module:model/TimeEntryNumbersCollection}
     */
    TimeEntryNumbersCollection,

    /**
     * The TimeEntryPrices model constructor.
     * @property {module:model/TimeEntryPrices}
     */
    TimeEntryPrices,

    /**
     * The TimeEntryPricesCursorResults model constructor.
     * @property {module:model/TimeEntryPricesCursorResults}
     */
    TimeEntryPricesCursorResults,

    /**
    * The ActivitiesApi service constructor.
    * @property {module:api/ActivitiesApi}
    */
    ActivitiesApi,

    /**
    * The ActivityGroupsApi service constructor.
    * @property {module:api/ActivityGroupsApi}
    */
    ActivityGroupsApi,

    /**
    * The CostTypeGroupsApi service constructor.
    * @property {module:api/CostTypeGroupsApi}
    */
    CostTypeGroupsApi,

    /**
    * The CostTypesApi service constructor.
    * @property {module:api/CostTypesApi}
    */
    CostTypesApi,

    /**
    * The EmployeeGroupsApi service constructor.
    * @property {module:api/EmployeeGroupsApi}
    */
    EmployeeGroupsApi,

    /**
    * The EmployeesApi service constructor.
    * @property {module:api/EmployeesApi}
    */
    EmployeesApi,

    /**
    * The MileageEntriesApi service constructor.
    * @property {module:api/MileageEntriesApi}
    */
    MileageEntriesApi,

    /**
    * The MileageEntryPricesApi service constructor.
    * @property {module:api/MileageEntryPricesApi}
    */
    MileageEntryPricesApi,

    /**
    * The MileagesApi service constructor.
    * @property {module:api/MileagesApi}
    */
    MileagesApi,

    /**
    * The ProjectActivitiesApi service constructor.
    * @property {module:api/ProjectActivitiesApi}
    */
    ProjectActivitiesApi,

    /**
    * The ProjectCustomersApi service constructor.
    * @property {module:api/ProjectCustomersApi}
    */
    ProjectCustomersApi,

    /**
    * The ProjectEmployeeGroupsApi service constructor.
    * @property {module:api/ProjectEmployeeGroupsApi}
    */
    ProjectEmployeeGroupsApi,

    /**
    * The ProjectEmployeesApi service constructor.
    * @property {module:api/ProjectEmployeesApi}
    */
    ProjectEmployeesApi,

    /**
    * The ProjectGroupsApi service constructor.
    * @property {module:api/ProjectGroupsApi}
    */
    ProjectGroupsApi,

    /**
    * The ProjectStatusesApi service constructor.
    * @property {module:api/ProjectStatusesApi}
    */
    ProjectStatusesApi,

    /**
    * The ProjectsApi service constructor.
    * @property {module:api/ProjectsApi}
    */
    ProjectsApi,

    /**
    * The TimeEntriesApi service constructor.
    * @property {module:api/TimeEntriesApi}
    */
    TimeEntriesApi,

    /**
    * The TimeEntryPricesApi service constructor.
    * @property {module:api/TimeEntryPricesApi}
    */
    TimeEntryPricesApi
};
