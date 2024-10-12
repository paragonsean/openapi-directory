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


package org.openapitools.client;

import okhttp3.*;
import okhttp3.internal.http.HttpMethod;
import okhttp3.internal.tls.OkHostnameVerifier;
import okhttp3.logging.HttpLoggingInterceptor;
import okhttp3.logging.HttpLoggingInterceptor.Level;
import okio.Buffer;
import okio.BufferedSink;
import okio.Okio;

import javax.net.ssl.*;
import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.io.UnsupportedEncodingException;
import java.lang.reflect.Type;
import java.net.URI;
import java.net.URLConnection;
import java.net.URLEncoder;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.security.GeneralSecurityException;
import java.security.KeyStore;
import java.security.SecureRandom;
import java.security.cert.Certificate;
import java.security.cert.CertificateException;
import java.security.cert.CertificateFactory;
import java.security.cert.X509Certificate;
import java.text.DateFormat;
import java.time.LocalDate;
import java.time.OffsetDateTime;
import java.time.format.DateTimeFormatter;
import java.util.*;
import java.util.Map.Entry;
import java.util.concurrent.TimeUnit;
import java.util.function.Supplier;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import org.openapitools.client.auth.Authentication;
import org.openapitools.client.auth.HttpBasicAuth;
import org.openapitools.client.auth.HttpBearerAuth;
import org.openapitools.client.auth.ApiKeyAuth;

/**
 * <p>ApiClient class.</p>
 */
public class ApiClient {

    private String basePath = "https://apis.e-conomic.com/api/v20.0.0";
    protected List<ServerConfiguration> servers = new ArrayList<ServerConfiguration>(Arrays.asList(
    new ServerConfiguration(
      "https://apis.e-conomic.com/api/v20.0.0",
      "No description provided",
      new HashMap<String, ServerVariable>()
    )
  ));
    protected Integer serverIndex = 0;
    protected Map<String, String> serverVariables = null;
    private boolean debugging = false;
    private Map<String, String> defaultHeaderMap = new HashMap<String, String>();
    private Map<String, String> defaultCookieMap = new HashMap<String, String>();
    private String tempFolderPath = null;

    private Map<String, Authentication> authentications;

    private DateFormat dateFormat;
    private DateFormat datetimeFormat;
    private boolean lenientDatetimeFormat;
    private int dateLength;

    private InputStream sslCaCert;
    private boolean verifyingSsl;
    private KeyManager[] keyManagers;

    private OkHttpClient httpClient;
    private JSON json;

    private HttpLoggingInterceptor loggingInterceptor;

    /**
     * Basic constructor for ApiClient
     */
    public ApiClient() {
        init();
        initHttpClient();

        // Setup authentications (key: authentication name, value: authentication).
        authentications.put("X-AgreementGrantToken", new ApiKeyAuth("header", "X-AgreementGrantToken"));
        authentications.put("X-AppSecretToken", new ApiKeyAuth("header", "X-AppSecretToken"));
        // Prevent the authentications from being modified.
        authentications = Collections.unmodifiableMap(authentications);
    }

    /**
     * Basic constructor with custom OkHttpClient
     *
     * @param client a {@link okhttp3.OkHttpClient} object
     */
    public ApiClient(OkHttpClient client) {
        init();

        httpClient = client;

        // Setup authentications (key: authentication name, value: authentication).
        authentications.put("X-AgreementGrantToken", new ApiKeyAuth("header", "X-AgreementGrantToken"));
        authentications.put("X-AppSecretToken", new ApiKeyAuth("header", "X-AppSecretToken"));
        // Prevent the authentications from being modified.
        authentications = Collections.unmodifiableMap(authentications);
    }

    private void initHttpClient() {
        initHttpClient(Collections.<Interceptor>emptyList());
    }

    private void initHttpClient(List<Interceptor> interceptors) {
        OkHttpClient.Builder builder = new OkHttpClient.Builder();
        builder.addNetworkInterceptor(getProgressInterceptor());
        for (Interceptor interceptor: interceptors) {
            builder.addInterceptor(interceptor);
        }

        httpClient = builder.build();
    }

    private void init() {
        verifyingSsl = true;

        json = new JSON();

        // Set default User-Agent.
        setUserAgent("OpenAPI-Generator/v20.0.0/java");

        authentications = new HashMap<String, Authentication>();
    }

    /**
     * Get base path
     *
     * @return Base path
     */
    public String getBasePath() {
        return basePath;
    }

    /**
     * Set base path
     *
     * @param basePath Base path of the URL (e.g https://apis.e-conomic.com/api/v20.0.0
     * @return An instance of OkHttpClient
     */
    public ApiClient setBasePath(String basePath) {
        this.basePath = basePath;
        this.serverIndex = null;
        return this;
    }

    public List<ServerConfiguration> getServers() {
        return servers;
    }

    public ApiClient setServers(List<ServerConfiguration> servers) {
        this.servers = servers;
        return this;
    }

    public Integer getServerIndex() {
        return serverIndex;
    }

    public ApiClient setServerIndex(Integer serverIndex) {
        this.serverIndex = serverIndex;
        return this;
    }

    public Map<String, String> getServerVariables() {
        return serverVariables;
    }

    public ApiClient setServerVariables(Map<String, String> serverVariables) {
        this.serverVariables = serverVariables;
        return this;
    }

    /**
     * Get HTTP client
     *
     * @return An instance of OkHttpClient
     */
    public OkHttpClient getHttpClient() {
        return httpClient;
    }

    /**
     * Set HTTP client, which must never be null.
     *
     * @param newHttpClient An instance of OkHttpClient
     * @return Api Client
     * @throws java.lang.NullPointerException when newHttpClient is null
     */
    public ApiClient setHttpClient(OkHttpClient newHttpClient) {
        this.httpClient = Objects.requireNonNull(newHttpClient, "HttpClient must not be null!");
        return this;
    }

    /**
     * Get JSON
     *
     * @return JSON object
     */
    public JSON getJSON() {
        return json;
    }

    /**
     * Set JSON
     *
     * @param json JSON object
     * @return Api client
     */
    public ApiClient setJSON(JSON json) {
        this.json = json;
        return this;
    }

    /**
     * True if isVerifyingSsl flag is on
     *
     * @return True if isVerifySsl flag is on
     */
    public boolean isVerifyingSsl() {
        return verifyingSsl;
    }

    /**
     * Configure whether to verify certificate and hostname when making https requests.
     * Default to true.
     * NOTE: Do NOT set to false in production code, otherwise you would face multiple types of cryptographic attacks.
     *
     * @param verifyingSsl True to verify TLS/SSL connection
     * @return ApiClient
     */
    public ApiClient setVerifyingSsl(boolean verifyingSsl) {
        this.verifyingSsl = verifyingSsl;
        applySslSettings();
        return this;
    }

    /**
     * Get SSL CA cert.
     *
     * @return Input stream to the SSL CA cert
     */
    public InputStream getSslCaCert() {
        return sslCaCert;
    }

    /**
     * Configure the CA certificate to be trusted when making https requests.
     * Use null to reset to default.
     *
     * @param sslCaCert input stream for SSL CA cert
     * @return ApiClient
     */
    public ApiClient setSslCaCert(InputStream sslCaCert) {
        this.sslCaCert = sslCaCert;
        applySslSettings();
        return this;
    }

    /**
     * <p>Getter for the field <code>keyManagers</code>.</p>
     *
     * @return an array of {@link javax.net.ssl.KeyManager} objects
     */
    public KeyManager[] getKeyManagers() {
        return keyManagers;
    }

    /**
     * Configure client keys to use for authorization in an SSL session.
     * Use null to reset to default.
     *
     * @param managers The KeyManagers to use
     * @return ApiClient
     */
    public ApiClient setKeyManagers(KeyManager[] managers) {
        this.keyManagers = managers;
        applySslSettings();
        return this;
    }

    /**
     * <p>Getter for the field <code>dateFormat</code>.</p>
     *
     * @return a {@link java.text.DateFormat} object
     */
    public DateFormat getDateFormat() {
        return dateFormat;
    }

    /**
     * <p>Setter for the field <code>dateFormat</code>.</p>
     *
     * @param dateFormat a {@link java.text.DateFormat} object
     * @return a {@link org.openapitools.client.ApiClient} object
     */
    public ApiClient setDateFormat(DateFormat dateFormat) {
        JSON.setDateFormat(dateFormat);
        return this;
    }

    /**
     * <p>Set SqlDateFormat.</p>
     *
     * @param dateFormat a {@link java.text.DateFormat} object
     * @return a {@link org.openapitools.client.ApiClient} object
     */
    public ApiClient setSqlDateFormat(DateFormat dateFormat) {
        JSON.setSqlDateFormat(dateFormat);
        return this;
    }

    /**
     * <p>Set OffsetDateTimeFormat.</p>
     *
     * @param dateFormat a {@link java.time.format.DateTimeFormatter} object
     * @return a {@link org.openapitools.client.ApiClient} object
     */
    public ApiClient setOffsetDateTimeFormat(DateTimeFormatter dateFormat) {
        JSON.setOffsetDateTimeFormat(dateFormat);
        return this;
    }

    /**
     * <p>Set LocalDateFormat.</p>
     *
     * @param dateFormat a {@link java.time.format.DateTimeFormatter} object
     * @return a {@link org.openapitools.client.ApiClient} object
     */
    public ApiClient setLocalDateFormat(DateTimeFormatter dateFormat) {
        JSON.setLocalDateFormat(dateFormat);
        return this;
    }

    /**
     * <p>Set LenientOnJson.</p>
     *
     * @param lenientOnJson a boolean
     * @return a {@link org.openapitools.client.ApiClient} object
     */
    public ApiClient setLenientOnJson(boolean lenientOnJson) {
        JSON.setLenientOnJson(lenientOnJson);
        return this;
    }

    /**
     * Get authentications (key: authentication name, value: authentication).
     *
     * @return Map of authentication objects
     */
    public Map<String, Authentication> getAuthentications() {
        return authentications;
    }

    /**
     * Get authentication for the given name.
     *
     * @param authName The authentication name
     * @return The authentication, null if not found
     */
    public Authentication getAuthentication(String authName) {
        return authentications.get(authName);
    }


    /**
     * Helper method to set username for the first HTTP basic authentication.
     *
     * @param username Username
     */
    public void setUsername(String username) {
        for (Authentication auth : authentications.values()) {
            if (auth instanceof HttpBasicAuth) {
                ((HttpBasicAuth) auth).setUsername(username);
                return;
            }
        }
        throw new RuntimeException("No HTTP basic authentication configured!");
    }

    /**
     * Helper method to set password for the first HTTP basic authentication.
     *
     * @param password Password
     */
    public void setPassword(String password) {
        for (Authentication auth : authentications.values()) {
            if (auth instanceof HttpBasicAuth) {
                ((HttpBasicAuth) auth).setPassword(password);
                return;
            }
        }
        throw new RuntimeException("No HTTP basic authentication configured!");
    }

    /**
     * Helper method to set API key value for the first API key authentication.
     *
     * @param apiKey API key
     */
    public void setApiKey(String apiKey) {
        for (Authentication auth : authentications.values()) {
            if (auth instanceof ApiKeyAuth) {
                ((ApiKeyAuth) auth).setApiKey(apiKey);
                return;
            }
        }
        throw new RuntimeException("No API key authentication configured!");
    }

    /**
     * Helper method to set API key prefix for the first API key authentication.
     *
     * @param apiKeyPrefix API key prefix
     */
    public void setApiKeyPrefix(String apiKeyPrefix) {
        for (Authentication auth : authentications.values()) {
            if (auth instanceof ApiKeyAuth) {
                ((ApiKeyAuth) auth).setApiKeyPrefix(apiKeyPrefix);
                return;
            }
        }
        throw new RuntimeException("No API key authentication configured!");
    }

    /**
     * Helper method to set access token for the first OAuth2 authentication.
     *
     * @param accessToken Access token
     */
    public void setAccessToken(String accessToken) {
        throw new RuntimeException("No OAuth2 authentication configured!");
    }

    /**
     * Helper method to set credentials for AWSV4 Signature
     *
     * @param accessKey Access Key
     * @param secretKey Secret Key
     * @param region Region
     * @param service Service to access to
     */
    public void setAWS4Configuration(String accessKey, String secretKey, String region, String service) {
        throw new RuntimeException("No AWS4 authentication configured!");
    }

    /**
     * Helper method to set credentials for AWSV4 Signature
     *
     * @param accessKey Access Key
     * @param secretKey Secret Key
     * @param sessionToken Session Token
     * @param region Region
     * @param service Service to access to
     */
    public void setAWS4Configuration(String accessKey, String secretKey, String sessionToken, String region, String service) {
        throw new RuntimeException("No AWS4 authentication configured!");
    }

    /**
     * Set the User-Agent header's value (by adding to the default header map).
     *
     * @param userAgent HTTP request's user agent
     * @return ApiClient
     */
    public ApiClient setUserAgent(String userAgent) {
        addDefaultHeader("User-Agent", userAgent);
        return this;
    }

    /**
     * Add a default header.
     *
     * @param key The header's key
     * @param value The header's value
     * @return ApiClient
     */
    public ApiClient addDefaultHeader(String key, String value) {
        defaultHeaderMap.put(key, value);
        return this;
    }

    /**
     * Add a default cookie.
     *
     * @param key The cookie's key
     * @param value The cookie's value
     * @return ApiClient
     */
    public ApiClient addDefaultCookie(String key, String value) {
        defaultCookieMap.put(key, value);
        return this;
    }

    /**
     * Check that whether debugging is enabled for this API client.
     *
     * @return True if debugging is enabled, false otherwise.
     */
    public boolean isDebugging() {
        return debugging;
    }

    /**
     * Enable/disable debugging for this API client.
     *
     * @param debugging To enable (true) or disable (false) debugging
     * @return ApiClient
     */
    public ApiClient setDebugging(boolean debugging) {
        if (debugging != this.debugging) {
            if (debugging) {
                loggingInterceptor = new HttpLoggingInterceptor();
                loggingInterceptor.setLevel(Level.BODY);
                httpClient = httpClient.newBuilder().addInterceptor(loggingInterceptor).build();
            } else {
                final OkHttpClient.Builder builder = httpClient.newBuilder();
                builder.interceptors().remove(loggingInterceptor);
                httpClient = builder.build();
                loggingInterceptor = null;
            }
        }
        this.debugging = debugging;
        return this;
    }

    /**
     * The path of temporary folder used to store downloaded files from endpoints
     * with file response. The default value is <code>null</code>, i.e. using
     * the system's default temporary folder.
     *
     * @see <a href="https://docs.oracle.com/javase/7/docs/api/java/nio/file/Files.html#createTempFile(java.lang.String,%20java.lang.String,%20java.nio.file.attribute.FileAttribute...)">createTempFile</a>
     * @return Temporary folder path
     */
    public String getTempFolderPath() {
        return tempFolderPath;
    }

    /**
     * Set the temporary folder path (for downloading files)
     *
     * @param tempFolderPath Temporary folder path
     * @return ApiClient
     */
    public ApiClient setTempFolderPath(String tempFolderPath) {
        this.tempFolderPath = tempFolderPath;
        return this;
    }

    /**
     * Get connection timeout (in milliseconds).
     *
     * @return Timeout in milliseconds
     */
    public int getConnectTimeout() {
        return httpClient.connectTimeoutMillis();
    }

    /**
     * Sets the connect timeout (in milliseconds).
     * A value of 0 means no timeout, otherwise values must be between 1 and
     * {@link java.lang.Integer#MAX_VALUE}.
     *
     * @param connectionTimeout connection timeout in milliseconds
     * @return Api client
     */
    public ApiClient setConnectTimeout(int connectionTimeout) {
        httpClient = httpClient.newBuilder().connectTimeout(connectionTimeout, TimeUnit.MILLISECONDS).build();
        return this;
    }

    /**
     * Get read timeout (in milliseconds).
     *
     * @return Timeout in milliseconds
     */
    public int getReadTimeout() {
        return httpClient.readTimeoutMillis();
    }

    /**
     * Sets the read timeout (in milliseconds).
     * A value of 0 means no timeout, otherwise values must be between 1 and
     * {@link java.lang.Integer#MAX_VALUE}.
     *
     * @param readTimeout read timeout in milliseconds
     * @return Api client
     */
    public ApiClient setReadTimeout(int readTimeout) {
        httpClient = httpClient.newBuilder().readTimeout(readTimeout, TimeUnit.MILLISECONDS).build();
        return this;
    }

    /**
     * Get write timeout (in milliseconds).
     *
     * @return Timeout in milliseconds
     */
    public int getWriteTimeout() {
        return httpClient.writeTimeoutMillis();
    }

    /**
     * Sets the write timeout (in milliseconds).
     * A value of 0 means no timeout, otherwise values must be between 1 and
     * {@link java.lang.Integer#MAX_VALUE}.
     *
     * @param writeTimeout connection timeout in milliseconds
     * @return Api client
     */
    public ApiClient setWriteTimeout(int writeTimeout) {
        httpClient = httpClient.newBuilder().writeTimeout(writeTimeout, TimeUnit.MILLISECONDS).build();
        return this;
    }


    /**
     * Format the given parameter object into string.
     *
     * @param param Parameter
     * @return String representation of the parameter
     */
    public String parameterToString(Object param) {
        if (param == null) {
            return "";
        } else if (param instanceof Date || param instanceof OffsetDateTime || param instanceof LocalDate) {
            //Serialize to json string and remove the " enclosing characters
            String jsonStr = JSON.serialize(param);
            return jsonStr.substring(1, jsonStr.length() - 1);
        } else if (param instanceof Collection) {
            StringBuilder b = new StringBuilder();
            for (Object o : (Collection) param) {
                if (b.length() > 0) {
                    b.append(",");
                }
                b.append(o);
            }
            return b.toString();
        } else {
            return String.valueOf(param);
        }
    }

    /**
     * Formats the specified query parameter to a list containing a single {@code Pair} object.
     *
     * Note that {@code value} must not be a collection.
     *
     * @param name The name of the parameter.
     * @param value The value of the parameter.
     * @return A list containing a single {@code Pair} object.
     */
    public List<Pair> parameterToPair(String name, Object value) {
        List<Pair> params = new ArrayList<Pair>();

        // preconditions
        if (name == null || name.isEmpty() || value == null || value instanceof Collection) {
            return params;
        }

        params.add(new Pair(name, parameterToString(value)));
        return params;
    }

    /**
     * Formats the specified collection query parameters to a list of {@code Pair} objects.
     *
     * Note that the values of each of the returned Pair objects are percent-encoded.
     *
     * @param collectionFormat The collection format of the parameter.
     * @param name The name of the parameter.
     * @param value The value of the parameter.
     * @return A list of {@code Pair} objects.
     */
    public List<Pair> parameterToPairs(String collectionFormat, String name, Collection value) {
        List<Pair> params = new ArrayList<Pair>();

        // preconditions
        if (name == null || name.isEmpty() || value == null || value.isEmpty()) {
            return params;
        }

        // create the params based on the collection format
        if ("multi".equals(collectionFormat)) {
            for (Object item : value) {
                params.add(new Pair(name, escapeString(parameterToString(item))));
            }
            return params;
        }

        // collectionFormat is assumed to be "csv" by default
        String delimiter = ",";

        // escape all delimiters except commas, which are URI reserved
        // characters
        if ("ssv".equals(collectionFormat)) {
            delimiter = escapeString(" ");
        } else if ("tsv".equals(collectionFormat)) {
            delimiter = escapeString("\t");
        } else if ("pipes".equals(collectionFormat)) {
            delimiter = escapeString("|");
        }

        StringBuilder sb = new StringBuilder();
        for (Object item : value) {
            sb.append(delimiter);
            sb.append(escapeString(parameterToString(item)));
        }

        params.add(new Pair(name, sb.substring(delimiter.length())));

        return params;
    }

    /**
    * Formats the specified free-form query parameters to a list of {@code Pair} objects.
    *
    * @param value The free-form query parameters.
    * @return A list of {@code Pair} objects.
    */
    public List<Pair> freeFormParameterToPairs(Object value) {
        List<Pair> params = new ArrayList<>();

        // preconditions
        if (value == null || !(value instanceof Map )) {
            return params;
        }

        final Map<String, Object> valuesMap = (Map<String, Object>) value;

        for (Map.Entry<String, Object> entry : valuesMap.entrySet()) {
            params.add(new Pair(entry.getKey(), parameterToString(entry.getValue())));
        }

        return params;
    }


    /**
     * Formats the specified collection path parameter to a string value.
     *
     * @param collectionFormat The collection format of the parameter.
     * @param value The value of the parameter.
     * @return String representation of the parameter
     */
    public String collectionPathParameterToString(String collectionFormat, Collection value) {
        // create the value based on the collection format
        if ("multi".equals(collectionFormat)) {
            // not valid for path params
            return parameterToString(value);
        }

        // collectionFormat is assumed to be "csv" by default
        String delimiter = ",";

        if ("ssv".equals(collectionFormat)) {
            delimiter = " ";
        } else if ("tsv".equals(collectionFormat)) {
            delimiter = "\t";
        } else if ("pipes".equals(collectionFormat)) {
            delimiter = "|";
        }

        StringBuilder sb = new StringBuilder() ;
        for (Object item : value) {
            sb.append(delimiter);
            sb.append(parameterToString(item));
        }

        return sb.substring(delimiter.length());
    }

    /**
     * Sanitize filename by removing path.
     * e.g. ../../sun.gif becomes sun.gif
     *
     * @param filename The filename to be sanitized
     * @return The sanitized filename
     */
    public String sanitizeFilename(String filename) {
        return filename.replaceAll(".*[/\\\\]", "");
    }

    /**
     * Check if the given MIME is a JSON MIME.
     * JSON MIME examples:
     *   application/json
     *   application/json; charset=UTF8
     *   APPLICATION/JSON
     *   application/vnd.company+json
     * "* / *" is also default to JSON
     * @param mime MIME (Multipurpose Internet Mail Extensions)
     * @return True if the given MIME is JSON, false otherwise.
     */
    public boolean isJsonMime(String mime) {
        String jsonMime = "(?i)^(application/json|[^;/ \t]+/[^;/ \t]+[+]json)[ \t]*(;.*)?$";
        return mime != null && (mime.matches(jsonMime) || mime.equals("*/*"));
    }

    /**
     * Select the Accept header's value from the given accepts array:
     *   if JSON exists in the given array, use it;
     *   otherwise use all of them (joining into a string)
     *
     * @param accepts The accepts array to select from
     * @return The Accept header to use. If the given array is empty,
     *   null will be returned (not to set the Accept header explicitly).
     */
    public String selectHeaderAccept(String[] accepts) {
        if (accepts.length == 0) {
            return null;
        }
        for (String accept : accepts) {
            if (isJsonMime(accept)) {
                return accept;
            }
        }
        return StringUtil.join(accepts, ",");
    }

    /**
     * Select the Content-Type header's value from the given array:
     *   if JSON exists in the given array, use it;
     *   otherwise use the first one of the array.
     *
     * @param contentTypes The Content-Type array to select from
     * @return The Content-Type header to use. If the given array is empty,
     *   returns null. If it matches "any", JSON will be used.
     */
    public String selectHeaderContentType(String[] contentTypes) {
        if (contentTypes.length == 0) {
            return null;
        }

        if (contentTypes[0].equals("*/*")) {
            return "application/json";
        }

        for (String contentType : contentTypes) {
            if (isJsonMime(contentType)) {
                return contentType;
            }
        }

        return contentTypes[0];
    }

    /**
     * Escape the given string to be used as URL query value.
     *
     * @param str String to be escaped
     * @return Escaped string
     */
    public String escapeString(String str) {
        try {
            return URLEncoder.encode(str, "utf8").replaceAll("\\+", "%20");
        } catch (UnsupportedEncodingException e) {
            return str;
        }
    }

    /**
     * Deserialize response body to Java object, according to the return type and
     * the Content-Type response header.
     *
     * @param <T> Type
     * @param response HTTP response
     * @param returnType The type of the Java object
     * @return The deserialized Java object
     * @throws org.openapitools.client.ApiException If fail to deserialize response body, i.e. cannot read response body
     *   or the Content-Type of the response is not supported.
     */
    @SuppressWarnings("unchecked")
    public <T> T deserialize(Response response, Type returnType) throws ApiException {
        if (response == null || returnType == null) {
            return null;
        }

        if ("byte[]".equals(returnType.toString())) {
            // Handle binary response (byte array).
            try {
                return (T) response.body().bytes();
            } catch (IOException e) {
                throw new ApiException(e);
            }
        } else if (returnType.equals(File.class)) {
            // Handle file downloading.
            return (T) downloadFileFromResponse(response);
        }

        String respBody;
        try {
            if (response.body() != null)
                respBody = response.body().string();
            else
                respBody = null;
        } catch (IOException e) {
            throw new ApiException(e);
        }

        if (respBody == null || "".equals(respBody)) {
            return null;
        }

        String contentType = response.headers().get("Content-Type");
        if (contentType == null) {
            // ensuring a default content type
            contentType = "application/json";
        }
        if (isJsonMime(contentType)) {
            return JSON.deserialize(respBody, returnType);
        } else if (returnType.equals(String.class)) {
            // Expecting string, return the raw response body.
            return (T) respBody;
        } else {
            throw new ApiException(
                    "Content type \"" + contentType + "\" is not supported for type: " + returnType,
                    response.code(),
                    response.headers().toMultimap(),
                    respBody);
        }
    }

    /**
     * Serialize the given Java object into request body according to the object's
     * class and the request Content-Type.
     *
     * @param obj The Java object
     * @param contentType The request Content-Type
     * @return The serialized request body
     * @throws org.openapitools.client.ApiException If fail to serialize the given object
     */
    public RequestBody serialize(Object obj, String contentType) throws ApiException {
        if (obj instanceof byte[]) {
            // Binary (byte array) body parameter support.
            return RequestBody.create((byte[]) obj, MediaType.parse(contentType));
        } else if (obj instanceof File) {
            // File body parameter support.
            return RequestBody.create((File) obj, MediaType.parse(contentType));
        } else if ("text/plain".equals(contentType) && obj instanceof String) {
            return RequestBody.create((String) obj, MediaType.parse(contentType));
        } else if (isJsonMime(contentType)) {
            String content;
            if (obj != null) {
                content = JSON.serialize(obj);
            } else {
                content = null;
            }
            return RequestBody.create(content, MediaType.parse(contentType));
        } else if (obj instanceof String) {
            return RequestBody.create((String) obj, MediaType.parse(contentType));
        } else {
            throw new ApiException("Content type \"" + contentType + "\" is not supported");
        }
    }

    /**
     * Download file from the given response.
     *
     * @param response An instance of the Response object
     * @throws org.openapitools.client.ApiException If fail to read file content from response and write to disk
     * @return Downloaded file
     */
    public File downloadFileFromResponse(Response response) throws ApiException {
        try {
            File file = prepareDownloadFile(response);
            BufferedSink sink = Okio.buffer(Okio.sink(file));
            sink.writeAll(response.body().source());
            sink.close();
            return file;
        } catch (IOException e) {
            throw new ApiException(e);
        }
    }

    /**
     * Prepare file for download
     *
     * @param response An instance of the Response object
     * @return Prepared file for the download
     * @throws java.io.IOException If fail to prepare file for download
     */
    public File prepareDownloadFile(Response response) throws IOException {
        String filename = null;
        String contentDisposition = response.header("Content-Disposition");
        if (contentDisposition != null && !"".equals(contentDisposition)) {
            // Get filename from the Content-Disposition header.
            Pattern pattern = Pattern.compile("filename=['\"]?([^'\"\\s]+)['\"]?");
            Matcher matcher = pattern.matcher(contentDisposition);
            if (matcher.find()) {
                filename = sanitizeFilename(matcher.group(1));
            }
        }

        String prefix = null;
        String suffix = null;
        if (filename == null) {
            prefix = "download-";
            suffix = "";
        } else {
            int pos = filename.lastIndexOf(".");
            if (pos == -1) {
                prefix = filename + "-";
            } else {
                prefix = filename.substring(0, pos) + "-";
                suffix = filename.substring(pos);
            }
            // Files.createTempFile requires the prefix to be at least three characters long
            if (prefix.length() < 3)
                prefix = "download-";
        }

        if (tempFolderPath == null)
            return Files.createTempFile(prefix, suffix).toFile();
        else
            return Files.createTempFile(Paths.get(tempFolderPath), prefix, suffix).toFile();
    }

    /**
     * {@link #execute(Call, Type)}
     *
     * @param <T> Type
     * @param call An instance of the Call object
     * @return ApiResponse&lt;T&gt;
     * @throws org.openapitools.client.ApiException If fail to execute the call
     */
    public <T> ApiResponse<T> execute(Call call) throws ApiException {
        return execute(call, null);
    }

    /**
     * Execute HTTP call and deserialize the HTTP response body into the given return type.
     *
     * @param returnType The return type used to deserialize HTTP response body
     * @param <T> The return type corresponding to (same with) returnType
     * @param call Call
     * @return ApiResponse object containing response status, headers and
     *   data, which is a Java object deserialized from response body and would be null
     *   when returnType is null.
     * @throws org.openapitools.client.ApiException If fail to execute the call
     */
    public <T> ApiResponse<T> execute(Call call, Type returnType) throws ApiException {
        try {
            Response response = call.execute();
            T data = handleResponse(response, returnType);
            return new ApiResponse<T>(response.code(), response.headers().toMultimap(), data);
        } catch (IOException e) {
            throw new ApiException(e);
        }
    }

    /**
     * {@link #executeAsync(Call, Type, ApiCallback)}
     *
     * @param <T> Type
     * @param call An instance of the Call object
     * @param callback ApiCallback&lt;T&gt;
     */
    public <T> void executeAsync(Call call, ApiCallback<T> callback) {
        executeAsync(call, null, callback);
    }

    /**
     * Execute HTTP call asynchronously.
     *
     * @param <T> Type
     * @param call The callback to be executed when the API call finishes
     * @param returnType Return type
     * @param callback ApiCallback
     * @see #execute(Call, Type)
     */
    @SuppressWarnings("unchecked")
    public <T> void executeAsync(Call call, final Type returnType, final ApiCallback<T> callback) {
        call.enqueue(new Callback() {
            @Override
            public void onFailure(Call call, IOException e) {
                callback.onFailure(new ApiException(e), 0, null);
            }

            @Override
            public void onResponse(Call call, Response response) throws IOException {
                T result;
                try {
                    result = (T) handleResponse(response, returnType);
                } catch (ApiException e) {
                    callback.onFailure(e, response.code(), response.headers().toMultimap());
                    return;
                } catch (Exception e) {
                    callback.onFailure(new ApiException(e), response.code(), response.headers().toMultimap());
                    return;
                }
                callback.onSuccess(result, response.code(), response.headers().toMultimap());
            }
        });
    }

    /**
     * Handle the given response, return the deserialized object when the response is successful.
     *
     * @param <T> Type
     * @param response Response
     * @param returnType Return type
     * @return Type
     * @throws org.openapitools.client.ApiException If the response has an unsuccessful status code or
     *                      fail to deserialize the response body
     */
    public <T> T handleResponse(Response response, Type returnType) throws ApiException {
        if (response.isSuccessful()) {
            if (returnType == null || response.code() == 204) {
                // returning null if the returnType is not defined,
                // or the status code is 204 (No Content)
                if (response.body() != null) {
                    try {
                        response.body().close();
                    } catch (Exception e) {
                        throw new ApiException(response.message(), e, response.code(), response.headers().toMultimap());
                    }
                }
                return null;
            } else {
                return deserialize(response, returnType);
            }
        } else {
            String respBody = null;
            if (response.body() != null) {
                try {
                    respBody = response.body().string();
                } catch (IOException e) {
                    throw new ApiException(response.message(), e, response.code(), response.headers().toMultimap());
                }
            }
            throw new ApiException(response.message(), response.code(), response.headers().toMultimap(), respBody);
        }
    }

    /**
     * Build HTTP call with the given options.
     *
     * @param baseUrl The base URL
     * @param path The sub-path of the HTTP URL
     * @param method The request method, one of "GET", "HEAD", "OPTIONS", "POST", "PUT", "PATCH" and "DELETE"
     * @param queryParams The query parameters
     * @param collectionQueryParams The collection query parameters
     * @param body The request body object
     * @param headerParams The header parameters
     * @param cookieParams The cookie parameters
     * @param formParams The form parameters
     * @param authNames The authentications to apply
     * @param callback Callback for upload/download progress
     * @return The HTTP call
     * @throws org.openapitools.client.ApiException If fail to serialize the request body object
     */
    public Call buildCall(String baseUrl, String path, String method, List<Pair> queryParams, List<Pair> collectionQueryParams, Object body, Map<String, String> headerParams, Map<String, String> cookieParams, Map<String, Object> formParams, String[] authNames, ApiCallback callback) throws ApiException {
        Request request = buildRequest(baseUrl, path, method, queryParams, collectionQueryParams, body, headerParams, cookieParams, formParams, authNames, callback);

        return httpClient.newCall(request);
    }

    /**
     * Build an HTTP request with the given options.
     *
     * @param baseUrl The base URL
     * @param path The sub-path of the HTTP URL
     * @param method The request method, one of "GET", "HEAD", "OPTIONS", "POST", "PUT", "PATCH" and "DELETE"
     * @param queryParams The query parameters
     * @param collectionQueryParams The collection query parameters
     * @param body The request body object
     * @param headerParams The header parameters
     * @param cookieParams The cookie parameters
     * @param formParams The form parameters
     * @param authNames The authentications to apply
     * @param callback Callback for upload/download progress
     * @return The HTTP request
     * @throws org.openapitools.client.ApiException If fail to serialize the request body object
     */
    public Request buildRequest(String baseUrl, String path, String method, List<Pair> queryParams, List<Pair> collectionQueryParams, Object body, Map<String, String> headerParams, Map<String, String> cookieParams, Map<String, Object> formParams, String[] authNames, ApiCallback callback) throws ApiException {
        final String url = buildUrl(baseUrl, path, queryParams, collectionQueryParams);

        // prepare HTTP request body
        RequestBody reqBody;
        String contentType = headerParams.get("Content-Type");
        String contentTypePure = contentType;
        if (contentTypePure != null && contentTypePure.contains(";")) {
            contentTypePure = contentType.substring(0, contentType.indexOf(";"));
        }
        if (!HttpMethod.permitsRequestBody(method)) {
            reqBody = null;
        } else if ("application/x-www-form-urlencoded".equals(contentTypePure)) {
            reqBody = buildRequestBodyFormEncoding(formParams);
        } else if ("multipart/form-data".equals(contentTypePure)) {
            reqBody = buildRequestBodyMultipart(formParams);
        } else if (body == null) {
            if ("DELETE".equals(method)) {
                // allow calling DELETE without sending a request body
                reqBody = null;
            } else {
                // use an empty request body (for POST, PUT and PATCH)
                reqBody = RequestBody.create("", contentType == null ? null : MediaType.parse(contentType));
            }
        } else {
            reqBody = serialize(body, contentType);
        }

        List<Pair> updatedQueryParams = new ArrayList<>(queryParams);

        // update parameters with authentication settings
        updateParamsForAuth(authNames, updatedQueryParams, headerParams, cookieParams, requestBodyToString(reqBody), method, URI.create(url));

        final Request.Builder reqBuilder = new Request.Builder().url(buildUrl(baseUrl, path, updatedQueryParams, collectionQueryParams));
        processHeaderParams(headerParams, reqBuilder);
        processCookieParams(cookieParams, reqBuilder);

        // Associate callback with request (if not null) so interceptor can
        // access it when creating ProgressResponseBody
        reqBuilder.tag(callback);

        Request request = null;

        if (callback != null && reqBody != null) {
            ProgressRequestBody progressRequestBody = new ProgressRequestBody(reqBody, callback);
            request = reqBuilder.method(method, progressRequestBody).build();
        } else {
            request = reqBuilder.method(method, reqBody).build();
        }

        return request;
    }

    /**
     * Build full URL by concatenating base path, the given sub path and query parameters.
     *
     * @param baseUrl The base URL
     * @param path The sub path
     * @param queryParams The query parameters
     * @param collectionQueryParams The collection query parameters
     * @return The full URL
     */
    public String buildUrl(String baseUrl, String path, List<Pair> queryParams, List<Pair> collectionQueryParams) {
        final StringBuilder url = new StringBuilder();
        if (baseUrl != null) {
            url.append(baseUrl).append(path);
        } else {
            String baseURL;
            if (serverIndex != null) {
                if (serverIndex < 0 || serverIndex >= servers.size()) {
                    throw new ArrayIndexOutOfBoundsException(String.format(
                    "Invalid index %d when selecting the host settings. Must be less than %d", serverIndex, servers.size()
                    ));
                }
                baseURL = servers.get(serverIndex).URL(serverVariables);
            } else {
                baseURL = basePath;
            }
            url.append(baseURL).append(path);
        }

        if (queryParams != null && !queryParams.isEmpty()) {
            // support (constant) query string in `path`, e.g. "/posts?draft=1"
            String prefix = path.contains("?") ? "&" : "?";
            for (Pair param : queryParams) {
                if (param.getValue() != null) {
                    if (prefix != null) {
                        url.append(prefix);
                        prefix = null;
                    } else {
                        url.append("&");
                    }
                    String value = parameterToString(param.getValue());
                    url.append(escapeString(param.getName())).append("=").append(escapeString(value));
                }
            }
        }

        if (collectionQueryParams != null && !collectionQueryParams.isEmpty()) {
            String prefix = url.toString().contains("?") ? "&" : "?";
            for (Pair param : collectionQueryParams) {
                if (param.getValue() != null) {
                    if (prefix != null) {
                        url.append(prefix);
                        prefix = null;
                    } else {
                        url.append("&");
                    }
                    String value = parameterToString(param.getValue());
                    // collection query parameter value already escaped as part of parameterToPairs
                    url.append(escapeString(param.getName())).append("=").append(value);
                }
            }
        }

        return url.toString();
    }

    /**
     * Set header parameters to the request builder, including default headers.
     *
     * @param headerParams Header parameters in the form of Map
     * @param reqBuilder Request.Builder
     */
    public void processHeaderParams(Map<String, String> headerParams, Request.Builder reqBuilder) {
        for (Entry<String, String> param : headerParams.entrySet()) {
            reqBuilder.header(param.getKey(), parameterToString(param.getValue()));
        }
        for (Entry<String, String> header : defaultHeaderMap.entrySet()) {
            if (!headerParams.containsKey(header.getKey())) {
                reqBuilder.header(header.getKey(), parameterToString(header.getValue()));
            }
        }
    }

    /**
     * Set cookie parameters to the request builder, including default cookies.
     *
     * @param cookieParams Cookie parameters in the form of Map
     * @param reqBuilder Request.Builder
     */
    public void processCookieParams(Map<String, String> cookieParams, Request.Builder reqBuilder) {
        for (Entry<String, String> param : cookieParams.entrySet()) {
            reqBuilder.addHeader("Cookie", String.format("%s=%s", param.getKey(), param.getValue()));
        }
        for (Entry<String, String> param : defaultCookieMap.entrySet()) {
            if (!cookieParams.containsKey(param.getKey())) {
                reqBuilder.addHeader("Cookie", String.format("%s=%s", param.getKey(), param.getValue()));
            }
        }
    }

    /**
     * Update query and header parameters based on authentication settings.
     *
     * @param authNames The authentications to apply
     * @param queryParams List of query parameters
     * @param headerParams Map of header parameters
     * @param cookieParams Map of cookie parameters
     * @param payload HTTP request body
     * @param method HTTP method
     * @param uri URI
     * @throws org.openapitools.client.ApiException If fails to update the parameters
     */
    public void updateParamsForAuth(String[] authNames, List<Pair> queryParams, Map<String, String> headerParams,
                                    Map<String, String> cookieParams, String payload, String method, URI uri) throws ApiException {
        for (String authName : authNames) {
            Authentication auth = authentications.get(authName);
            if (auth == null) {
                throw new RuntimeException("Authentication undefined: " + authName);
            }
            auth.applyToParams(queryParams, headerParams, cookieParams, payload, method, uri);
        }
    }

    /**
     * Build a form-encoding request body with the given form parameters.
     *
     * @param formParams Form parameters in the form of Map
     * @return RequestBody
     */
    public RequestBody buildRequestBodyFormEncoding(Map<String, Object> formParams) {
        okhttp3.FormBody.Builder formBuilder = new okhttp3.FormBody.Builder();
        for (Entry<String, Object> param : formParams.entrySet()) {
            formBuilder.add(param.getKey(), parameterToString(param.getValue()));
        }
        return formBuilder.build();
    }

    /**
     * Build a multipart (file uploading) request body with the given form parameters,
     * which could contain text fields and file fields.
     *
     * @param formParams Form parameters in the form of Map
     * @return RequestBody
     */
    public RequestBody buildRequestBodyMultipart(Map<String, Object> formParams) {
        MultipartBody.Builder mpBuilder = new MultipartBody.Builder().setType(MultipartBody.FORM);
        for (Entry<String, Object> param : formParams.entrySet()) {
            if (param.getValue() instanceof File) {
                File file = (File) param.getValue();
                addPartToMultiPartBuilder(mpBuilder, param.getKey(), file);
            } else if (param.getValue() instanceof List) {
                List list = (List) param.getValue();
                for (Object item: list) {
                    if (item instanceof File) {
                        addPartToMultiPartBuilder(mpBuilder, param.getKey(), (File) item);
                    } else {
                        addPartToMultiPartBuilder(mpBuilder, param.getKey(), param.getValue());
                    }
                }
            } else {
                addPartToMultiPartBuilder(mpBuilder, param.getKey(), param.getValue());
            }
        }
        return mpBuilder.build();
    }

    /**
     * Guess Content-Type header from the given file (defaults to "application/octet-stream").
     *
     * @param file The given file
     * @return The guessed Content-Type
     */
    public String guessContentTypeFromFile(File file) {
        String contentType = URLConnection.guessContentTypeFromName(file.getName());
        if (contentType == null) {
            return "application/octet-stream";
        } else {
            return contentType;
        }
    }

    /**
     * Add a Content-Disposition Header for the given key and file to the MultipartBody Builder.
     *
     * @param mpBuilder MultipartBody.Builder 
     * @param key The key of the Header element
     * @param file The file to add to the Header
     */ 
    private void addPartToMultiPartBuilder(MultipartBody.Builder mpBuilder, String key, File file) {
        Headers partHeaders = Headers.of("Content-Disposition", "form-data; name=\"" + key + "\"; filename=\"" + file.getName() + "\"");
        MediaType mediaType = MediaType.parse(guessContentTypeFromFile(file));
        mpBuilder.addPart(partHeaders, RequestBody.create(file, mediaType));
    }

    /**
     * Add a Content-Disposition Header for the given key and complex object to the MultipartBody Builder.
     *
     * @param mpBuilder MultipartBody.Builder
     * @param key The key of the Header element
     * @param obj The complex object to add to the Header
     */
    private void addPartToMultiPartBuilder(MultipartBody.Builder mpBuilder, String key, Object obj) {
        RequestBody requestBody;
        if (obj instanceof String) {
            requestBody = RequestBody.create((String) obj, MediaType.parse("text/plain"));
        } else {
            String content;
            if (obj != null) {
                content = JSON.serialize(obj);
            } else {
                content = null;
            }
            requestBody = RequestBody.create(content, MediaType.parse("application/json"));
        }

        Headers partHeaders = Headers.of("Content-Disposition", "form-data; name=\"" + key + "\"");
        mpBuilder.addPart(partHeaders, requestBody);
    }

    /**
     * Get network interceptor to add it to the httpClient to track download progress for
     * async requests.
     */
    private Interceptor getProgressInterceptor() {
        return new Interceptor() {
            @Override
            public Response intercept(Interceptor.Chain chain) throws IOException {
                final Request request = chain.request();
                final Response originalResponse = chain.proceed(request);
                if (request.tag() instanceof ApiCallback) {
                    final ApiCallback callback = (ApiCallback) request.tag();
                    return originalResponse.newBuilder()
                        .body(new ProgressResponseBody(originalResponse.body(), callback))
                        .build();
                }
                return originalResponse;
            }
        };
    }

    /**
     * Apply SSL related settings to httpClient according to the current values of
     * verifyingSsl and sslCaCert.
     */
    private void applySslSettings() {
        try {
            TrustManager[] trustManagers;
            HostnameVerifier hostnameVerifier;
            if (!verifyingSsl) {
                trustManagers = new TrustManager[]{
                        new X509TrustManager() {
                            @Override
                            public void checkClientTrusted(java.security.cert.X509Certificate[] chain, String authType) throws CertificateException {
                            }

                            @Override
                            public void checkServerTrusted(java.security.cert.X509Certificate[] chain, String authType) throws CertificateException {
                            }

                            @Override
                            public java.security.cert.X509Certificate[] getAcceptedIssuers() {
                                return new java.security.cert.X509Certificate[]{};
                            }
                        }
                };
                hostnameVerifier = new HostnameVerifier() {
                    @Override
                    public boolean verify(String hostname, SSLSession session) {
                        return true;
                    }
                };
            } else {
                TrustManagerFactory trustManagerFactory = TrustManagerFactory.getInstance(TrustManagerFactory.getDefaultAlgorithm());

                if (sslCaCert == null) {
                    trustManagerFactory.init((KeyStore) null);
                } else {
                    char[] password = null; // Any password will work.
                    CertificateFactory certificateFactory = CertificateFactory.getInstance("X.509");
                    Collection<? extends Certificate> certificates = certificateFactory.generateCertificates(sslCaCert);
                    if (certificates.isEmpty()) {
                        throw new IllegalArgumentException("expected non-empty set of trusted certificates");
                    }
                    KeyStore caKeyStore = newEmptyKeyStore(password);
                    int index = 0;
                    for (Certificate certificate : certificates) {
                        String certificateAlias = "ca" + (index++);
                        caKeyStore.setCertificateEntry(certificateAlias, certificate);
                    }
                    trustManagerFactory.init(caKeyStore);
                }
                trustManagers = trustManagerFactory.getTrustManagers();
                hostnameVerifier = OkHostnameVerifier.INSTANCE;
            }

            SSLContext sslContext = SSLContext.getInstance("TLS");
            sslContext.init(keyManagers, trustManagers, new SecureRandom());
            httpClient = httpClient.newBuilder()
                            .sslSocketFactory(sslContext.getSocketFactory(), (X509TrustManager) trustManagers[0])
                            .hostnameVerifier(hostnameVerifier)
                            .build();
        } catch (GeneralSecurityException e) {
            throw new RuntimeException(e);
        }
    }

    private KeyStore newEmptyKeyStore(char[] password) throws GeneralSecurityException {
        try {
            KeyStore keyStore = KeyStore.getInstance(KeyStore.getDefaultType());
            keyStore.load(null, password);
            return keyStore;
        } catch (IOException e) {
            throw new AssertionError(e);
        }
    }

    /**
     * Convert the HTTP request body to a string.
     *
     * @param requestBody The HTTP request object
     * @return The string representation of the HTTP request body
     * @throws org.openapitools.client.ApiException If fail to serialize the request body object into a string
     */
    private String requestBodyToString(RequestBody requestBody) throws ApiException {
        if (requestBody != null) {
            try {
                final Buffer buffer = new Buffer();
                requestBody.writeTo(buffer);
                return buffer.readUtf8();
            } catch (final IOException e) {
                throw new ApiException(e);
            }
        }

        // empty http request body
        return "";
    }
}
