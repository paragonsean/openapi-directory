/**
 * Checks API
 * **NOTE:** This is a preview of the API and it is not considered stable since refinements are still being made.  # Introduction  Welcome to the  **Truora Check** [**RESTful API**](https://en.wikipedia.org/wiki/Representational_state_transfer) reference. You may also want to check out our [**Validations API docs**](https://docs.validations.truora.com/) or our [**Signals API docs**](https://docs.signals.truora.com/).  Truora Check API allows performing full background checks on people, vehicles and companies. There are three main types of background checks:  - **Personal background check**: Verifies national IDs in multiple databases of public and legal entities in the LATAM region. For every national ID, returns information on: personal identity, criminal records, international background check, and professional background.  - **Vehicle background check**: Verifies the vehicle documents and the owner identity in multiple databases of public and legal entities in the LATAM region. For every vehicle and owner type, returns information on: personal identity, driving records, criminal records, and vehicle information.    - **Company background check**: Verifies the tax ID or a company name in multiple databases of public and legal entities in the LATAM region. For every company, returns the associated: business status, legal and criminal records, and media reports.  # API Key V1 is live!  API key version 1 is now live. Users with version 0 API keys are not immediately required to upgrade to V1 but should plan to do so at their earliest convenience. The changes for integration with API keys v1 are as follows:  - The field ``user_authorized`` is now required to perform person checks. This field indicates the API user has authorization to perform the check in compliance with data protection law. - The field ``homonym_scores`` is no longer included in our person check response as its results are already included in the body of the check and keeping them duplicated is generating unnecessary confusion.   # API composition  ## Endpoints  - **Check endpoints**: Provide an easy way to create and search for a background check. They also allow inserting groups of checks into reports. Each check contains scores, datasets and databases.   ```plain https://api.truora.com/v1/checks ```  - **Report endpoints**: Support batch uploads and grouping multiple checks together. Excel and .csv files are supported for batch uploads.   ```plain https://api.truora.com/v1/reports ```  - **Configuration endpoints**: Allows personalizing data sets and scores for customized background checks.  ```plain https://api.truora.com/v1/config ```  - **Continuous check endpoints**: Allows creating recurring checks and get notified whenever a change in the check score occurs.  ```plain https://api.truora.com/v1/continuous_checks ```  - **Behavior endpoints**: Allows sharing anonymous feedback about a person behavior when interacting with the company.  ```plain https://api.truora.com/v1/behaviour ```  - **Hooks endpoints**: Allows sending notifications via requests to your service or another third-party service whenever certain events occur.  ```plain https://api.truora.com/v1/hooks ```  ## Datasets  Categories that group the resulting information for background checks from databases are called datasets. Datasets are divided in:  - **Personal identity**: Corroborates the existence and validates personal identity documents.   - **Criminal record**: Checks for crimes according to each country penal code or criminal code. Keep in mind that data aged less than 10 years is usually more consistent.  - **Legal background**: Checks for lawsuits filed. Keep in mind that data aged less than 10 years is usually more consistent.  - **International background**: Checks international lists for crimes related to identity theft, money laundering, terrorist financing, and high crimes.  - **Professional background**: Checks professional regulatory entities for relevant information.  - **Affiliations and insurances**: Checks the history and status of social security affiliations.  - **Alert in media**: Checks major media agencies for relevant news related to violent actions.      - **Vehicle information**: Checks for the physical characteristics of the vehicle, technical status, insurance history, and other relevant information.  - **Traffic fines**: Checks for outstanding traffic fines.  - **Driving licenses**: Shows information relevant to the driver. Such as license status and driver certificates.  - **Business background**: Checks for business status, legal and criminal history, and other relevant information.  - **Taxes and Finances**: Checks for the information related to personal finances, liabilities, and taxes.  ## Requests Format  The POST requests receive a body that must be encoded in `www-x-form-urlencoded`, for instance:  ```plain type=person&national_id=123456&country=CO ```  The responses are always encoded in `JSON` format.  ## Errors  Whenever there is an error, a JSON with the following format is returned:  ```json {     \"code\": <Truora error code>,     \"http_code\": <The HTTP status of the response>,     \"message\": <The error message> } ```  for instance:  ```json {     \"code\": 10404,     \"http_code\": 404,     \"message\": \"The Check was not found\" } ```  ## SDKs  If your favorite language was not on the next list, You can use our [OpenAPI 3 spec](https://docs.truora.com/openapi.json) to generate it using the [Open API Generator](https://openapi-generator.tech/docs/installation).  To download the SDK click on the desired programming language:  - [C# .Net Core](https://truora-sdk.s3.amazonaws.com/checks/checks_csharp-netcore_latest.zip)  - [Elixir](https://truora-sdk.s3.amazonaws.com/checks/checks_elixir_latest.zip)  - [Go](https://truora-sdk.s3.amazonaws.com/checks/checks_go_latest.zip)  - [Java](https://truora-sdk.s3.amazonaws.com/checks/checks_java_latest.zip)  - [JavaScript](https://truora-sdk.s3.amazonaws.com/checks/checks_javascript_latest.zip)  - [Objc](https://truora-sdk.s3.amazonaws.com/checks/checks_objc_latest.zip)  - [Php](https://truora-sdk.s3.amazonaws.com/checks/checks_php_latest.zip)  - [Python](https://truora-sdk.s3.amazonaws.com/checks/checks_python_latest.zip)  - [Ruby](https://truora-sdk.s3.amazonaws.com/checks/checks_ruby_latest.zip)  You can see the full list of supported platforms here:  https://openapi-generator.tech/docs/generators   
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: api@truora.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from './ApiClient';
import APIKey from './model/APIKey';
import APIKeyVersion from './model/APIKeyVersion';
import APIKeyVersionChangelog from './model/APIKeyVersionChangelog';
import Behavior from './model/Behavior';
import BehaviourOutput from './model/BehaviourOutput';
import Change from './model/Change';
import Check from './model/Check';
import CheckDetails from './model/CheckDetails';
import CheckDetailsOutput from './model/CheckDetailsOutput';
import CheckOutput from './model/CheckOutput';
import ChecksOutput from './model/ChecksOutput';
import Comment from './model/Comment';
import CommentOutput from './model/CommentOutput';
import CommentsOutput from './model/CommentsOutput';
import CompanySummary from './model/CompanySummary';
import Config from './model/Config';
import ContinuousCheck from './model/ContinuousCheck';
import ContinuousCheckEntry from './model/ContinuousCheckEntry';
import CreateAPIKeyInput from './model/CreateAPIKeyInput';
import CreateCommentInput from './model/CreateCommentInput';
import CreateRuleInput from './model/CreateRuleInput';
import CreateUserInput from './model/CreateUserInput';
import Database from './model/Database';
import DeleteAPIKeyInput from './model/DeleteAPIKeyInput';
import DeleteUserInput from './model/DeleteUserInput';
import Error from './model/Error';
import GetContiuousCheckHistoryOutput from './model/GetContiuousCheckHistoryOutput';
import GetHealthDashboardInput from './model/GetHealthDashboardInput';
import Hook from './model/Hook';
import HookOutput from './model/HookOutput';
import ListContinuousChecksOutput from './model/ListContinuousChecksOutput';
import NameFound from './model/NameFound';
import Report from './model/Report';
import ReportOutput from './model/ReportOutput';
import ReportsOutput from './model/ReportsOutput';
import Rule from './model/Rule';
import RuleOutput from './model/RuleOutput';
import Score from './model/Score';
import ScoreConfig from './model/ScoreConfig';
import ScoreConfigOutput from './model/ScoreConfigOutput';
import ScoreConfigsOutput from './model/ScoreConfigsOutput';
import ScoreDetail from './model/ScoreDetail';
import Status from './model/Status';
import Subscriber from './model/Subscriber';
import Summary from './model/Summary';
import Table from './model/Table';
import TableCell from './model/TableCell';
import TableRow from './model/TableRow';
import UpdateAPIKeyInput from './model/UpdateAPIKeyInput';
import User from './model/User';
import VehicleSummary from './model/VehicleSummary';
import WrongInput from './model/WrongInput';
import BehaviorApi from './api/BehaviorApi';
import ChecksApi from './api/ChecksApi';
import ContinuousApi from './api/ContinuousApi';
import CustomTypeApi from './api/CustomTypeApi';
import HooksApi from './api/HooksApi';
import PdfApi from './api/PdfApi';
import ReportsApi from './api/ReportsApi';


/**
* **NOTE:** This is a preview of the API and it is not considered stable since refinements are still being made.  # Introduction  Welcome to the  **Truora Check** [**RESTful API**](https://en.wikipedia.org/wiki/Representational_state_transfer) reference. You may also want to check out our [**Validations API docs**](https://docs.validations.truora.com/) or our [**Signals API docs**](https://docs.signals.truora.com/).  Truora Check API allows performing full background checks on people, vehicles and companies. There are three main types of background checks:  - **Personal background check**: Verifies national IDs in multiple databases of public and legal entities in the LATAM region. For every national ID, returns information on: personal identity, criminal records, international background check, and professional background.  - **Vehicle background check**: Verifies the vehicle documents and the owner identity in multiple databases of public and legal entities in the LATAM region. For every vehicle and owner type, returns information on: personal identity, driving records, criminal records, and vehicle information.    - **Company background check**: Verifies the tax ID or a company name in multiple databases of public and legal entities in the LATAM region. For every company, returns the associated: business status, legal and criminal records, and media reports.  # API Key V1 is live!  API key version 1 is now live. Users with version 0 API keys are not immediately required to upgrade to V1 but should plan to do so at their earliest convenience. The changes for integration with API keys v1 are as follows:  - The field &#x60;&#x60;user_authorized&#x60;&#x60; is now required to perform person checks. This field indicates the API user has authorization to perform the check in compliance with data protection law. - The field &#x60;&#x60;homonym_scores&#x60;&#x60; is no longer included in our person check response as its results are already included in the body of the check and keeping them duplicated is generating unnecessary confusion.   # API composition  ## Endpoints  - **Check endpoints**: Provide an easy way to create and search for a background check. They also allow inserting groups of checks into reports. Each check contains scores, datasets and databases.   &#x60;&#x60;&#x60;plain https://api.truora.com/v1/checks &#x60;&#x60;&#x60;  - **Report endpoints**: Support batch uploads and grouping multiple checks together. Excel and .csv files are supported for batch uploads.   &#x60;&#x60;&#x60;plain https://api.truora.com/v1/reports &#x60;&#x60;&#x60;  - **Configuration endpoints**: Allows personalizing data sets and scores for customized background checks.  &#x60;&#x60;&#x60;plain https://api.truora.com/v1/config &#x60;&#x60;&#x60;  - **Continuous check endpoints**: Allows creating recurring checks and get notified whenever a change in the check score occurs.  &#x60;&#x60;&#x60;plain https://api.truora.com/v1/continuous_checks &#x60;&#x60;&#x60;  - **Behavior endpoints**: Allows sharing anonymous feedback about a person behavior when interacting with the company.  &#x60;&#x60;&#x60;plain https://api.truora.com/v1/behaviour &#x60;&#x60;&#x60;  - **Hooks endpoints**: Allows sending notifications via requests to your service or another third-party service whenever certain events occur.  &#x60;&#x60;&#x60;plain https://api.truora.com/v1/hooks &#x60;&#x60;&#x60;  ## Datasets  Categories that group the resulting information for background checks from databases are called datasets. Datasets are divided in:  - **Personal identity**: Corroborates the existence and validates personal identity documents.   - **Criminal record**: Checks for crimes according to each country penal code or criminal code. Keep in mind that data aged less than 10 years is usually more consistent.  - **Legal background**: Checks for lawsuits filed. Keep in mind that data aged less than 10 years is usually more consistent.  - **International background**: Checks international lists for crimes related to identity theft, money laundering, terrorist financing, and high crimes.  - **Professional background**: Checks professional regulatory entities for relevant information.  - **Affiliations and insurances**: Checks the history and status of social security affiliations.  - **Alert in media**: Checks major media agencies for relevant news related to violent actions.      - **Vehicle information**: Checks for the physical characteristics of the vehicle, technical status, insurance history, and other relevant information.  - **Traffic fines**: Checks for outstanding traffic fines.  - **Driving licenses**: Shows information relevant to the driver. Such as license status and driver certificates.  - **Business background**: Checks for business status, legal and criminal history, and other relevant information.  - **Taxes and Finances**: Checks for the information related to personal finances, liabilities, and taxes.  ## Requests Format  The POST requests receive a body that must be encoded in &#x60;www-x-form-urlencoded&#x60;, for instance:  &#x60;&#x60;&#x60;plain type&#x3D;person&amp;national_id&#x3D;123456&amp;country&#x3D;CO &#x60;&#x60;&#x60;  The responses are always encoded in &#x60;JSON&#x60; format.  ## Errors  Whenever there is an error, a JSON with the following format is returned:  &#x60;&#x60;&#x60;json {     \&quot;code\&quot;: &lt;Truora error code&gt;,     \&quot;http_code\&quot;: &lt;The HTTP status of the response&gt;,     \&quot;message\&quot;: &lt;The error message&gt; } &#x60;&#x60;&#x60;  for instance:  &#x60;&#x60;&#x60;json {     \&quot;code\&quot;: 10404,     \&quot;http_code\&quot;: 404,     \&quot;message\&quot;: \&quot;The Check was not found\&quot; } &#x60;&#x60;&#x60;  ## SDKs  If your favorite language was not on the next list, You can use our [OpenAPI 3 spec](https://docs.truora.com/openapi.json) to generate it using the [Open API Generator](https://openapi-generator.tech/docs/installation).  To download the SDK click on the desired programming language:  - [C# .Net Core](https://truora-sdk.s3.amazonaws.com/checks/checks_csharp-netcore_latest.zip)  - [Elixir](https://truora-sdk.s3.amazonaws.com/checks/checks_elixir_latest.zip)  - [Go](https://truora-sdk.s3.amazonaws.com/checks/checks_go_latest.zip)  - [Java](https://truora-sdk.s3.amazonaws.com/checks/checks_java_latest.zip)  - [JavaScript](https://truora-sdk.s3.amazonaws.com/checks/checks_javascript_latest.zip)  - [Objc](https://truora-sdk.s3.amazonaws.com/checks/checks_objc_latest.zip)  - [Php](https://truora-sdk.s3.amazonaws.com/checks/checks_php_latest.zip)  - [Python](https://truora-sdk.s3.amazonaws.com/checks/checks_python_latest.zip)  - [Ruby](https://truora-sdk.s3.amazonaws.com/checks/checks_ruby_latest.zip)  You can see the full list of supported platforms here:  https://openapi-generator.tech/docs/generators   .<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var ChecksApi = require('index'); // See note below*.
* var xxxSvc = new ChecksApi.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new ChecksApi.Yyy(); // Construct a model instance.
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
* var xxxSvc = new ChecksApi.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new ChecksApi.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 1.0.0
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The APIKey model constructor.
     * @property {module:model/APIKey}
     */
    APIKey,

    /**
     * The APIKeyVersion model constructor.
     * @property {module:model/APIKeyVersion}
     */
    APIKeyVersion,

    /**
     * The APIKeyVersionChangelog model constructor.
     * @property {module:model/APIKeyVersionChangelog}
     */
    APIKeyVersionChangelog,

    /**
     * The Behavior model constructor.
     * @property {module:model/Behavior}
     */
    Behavior,

    /**
     * The BehaviourOutput model constructor.
     * @property {module:model/BehaviourOutput}
     */
    BehaviourOutput,

    /**
     * The Change model constructor.
     * @property {module:model/Change}
     */
    Change,

    /**
     * The Check model constructor.
     * @property {module:model/Check}
     */
    Check,

    /**
     * The CheckDetails model constructor.
     * @property {module:model/CheckDetails}
     */
    CheckDetails,

    /**
     * The CheckDetailsOutput model constructor.
     * @property {module:model/CheckDetailsOutput}
     */
    CheckDetailsOutput,

    /**
     * The CheckOutput model constructor.
     * @property {module:model/CheckOutput}
     */
    CheckOutput,

    /**
     * The ChecksOutput model constructor.
     * @property {module:model/ChecksOutput}
     */
    ChecksOutput,

    /**
     * The Comment model constructor.
     * @property {module:model/Comment}
     */
    Comment,

    /**
     * The CommentOutput model constructor.
     * @property {module:model/CommentOutput}
     */
    CommentOutput,

    /**
     * The CommentsOutput model constructor.
     * @property {module:model/CommentsOutput}
     */
    CommentsOutput,

    /**
     * The CompanySummary model constructor.
     * @property {module:model/CompanySummary}
     */
    CompanySummary,

    /**
     * The Config model constructor.
     * @property {module:model/Config}
     */
    Config,

    /**
     * The ContinuousCheck model constructor.
     * @property {module:model/ContinuousCheck}
     */
    ContinuousCheck,

    /**
     * The ContinuousCheckEntry model constructor.
     * @property {module:model/ContinuousCheckEntry}
     */
    ContinuousCheckEntry,

    /**
     * The CreateAPIKeyInput model constructor.
     * @property {module:model/CreateAPIKeyInput}
     */
    CreateAPIKeyInput,

    /**
     * The CreateCommentInput model constructor.
     * @property {module:model/CreateCommentInput}
     */
    CreateCommentInput,

    /**
     * The CreateRuleInput model constructor.
     * @property {module:model/CreateRuleInput}
     */
    CreateRuleInput,

    /**
     * The CreateUserInput model constructor.
     * @property {module:model/CreateUserInput}
     */
    CreateUserInput,

    /**
     * The Database model constructor.
     * @property {module:model/Database}
     */
    Database,

    /**
     * The DeleteAPIKeyInput model constructor.
     * @property {module:model/DeleteAPIKeyInput}
     */
    DeleteAPIKeyInput,

    /**
     * The DeleteUserInput model constructor.
     * @property {module:model/DeleteUserInput}
     */
    DeleteUserInput,

    /**
     * The Error model constructor.
     * @property {module:model/Error}
     */
    Error,

    /**
     * The GetContiuousCheckHistoryOutput model constructor.
     * @property {module:model/GetContiuousCheckHistoryOutput}
     */
    GetContiuousCheckHistoryOutput,

    /**
     * The GetHealthDashboardInput model constructor.
     * @property {module:model/GetHealthDashboardInput}
     */
    GetHealthDashboardInput,

    /**
     * The Hook model constructor.
     * @property {module:model/Hook}
     */
    Hook,

    /**
     * The HookOutput model constructor.
     * @property {module:model/HookOutput}
     */
    HookOutput,

    /**
     * The ListContinuousChecksOutput model constructor.
     * @property {module:model/ListContinuousChecksOutput}
     */
    ListContinuousChecksOutput,

    /**
     * The NameFound model constructor.
     * @property {module:model/NameFound}
     */
    NameFound,

    /**
     * The Report model constructor.
     * @property {module:model/Report}
     */
    Report,

    /**
     * The ReportOutput model constructor.
     * @property {module:model/ReportOutput}
     */
    ReportOutput,

    /**
     * The ReportsOutput model constructor.
     * @property {module:model/ReportsOutput}
     */
    ReportsOutput,

    /**
     * The Rule model constructor.
     * @property {module:model/Rule}
     */
    Rule,

    /**
     * The RuleOutput model constructor.
     * @property {module:model/RuleOutput}
     */
    RuleOutput,

    /**
     * The Score model constructor.
     * @property {module:model/Score}
     */
    Score,

    /**
     * The ScoreConfig model constructor.
     * @property {module:model/ScoreConfig}
     */
    ScoreConfig,

    /**
     * The ScoreConfigOutput model constructor.
     * @property {module:model/ScoreConfigOutput}
     */
    ScoreConfigOutput,

    /**
     * The ScoreConfigsOutput model constructor.
     * @property {module:model/ScoreConfigsOutput}
     */
    ScoreConfigsOutput,

    /**
     * The ScoreDetail model constructor.
     * @property {module:model/ScoreDetail}
     */
    ScoreDetail,

    /**
     * The Status model constructor.
     * @property {module:model/Status}
     */
    Status,

    /**
     * The Subscriber model constructor.
     * @property {module:model/Subscriber}
     */
    Subscriber,

    /**
     * The Summary model constructor.
     * @property {module:model/Summary}
     */
    Summary,

    /**
     * The Table model constructor.
     * @property {module:model/Table}
     */
    Table,

    /**
     * The TableCell model constructor.
     * @property {module:model/TableCell}
     */
    TableCell,

    /**
     * The TableRow model constructor.
     * @property {module:model/TableRow}
     */
    TableRow,

    /**
     * The UpdateAPIKeyInput model constructor.
     * @property {module:model/UpdateAPIKeyInput}
     */
    UpdateAPIKeyInput,

    /**
     * The User model constructor.
     * @property {module:model/User}
     */
    User,

    /**
     * The VehicleSummary model constructor.
     * @property {module:model/VehicleSummary}
     */
    VehicleSummary,

    /**
     * The WrongInput model constructor.
     * @property {module:model/WrongInput}
     */
    WrongInput,

    /**
    * The BehaviorApi service constructor.
    * @property {module:api/BehaviorApi}
    */
    BehaviorApi,

    /**
    * The ChecksApi service constructor.
    * @property {module:api/ChecksApi}
    */
    ChecksApi,

    /**
    * The ContinuousApi service constructor.
    * @property {module:api/ContinuousApi}
    */
    ContinuousApi,

    /**
    * The CustomTypeApi service constructor.
    * @property {module:api/CustomTypeApi}
    */
    CustomTypeApi,

    /**
    * The HooksApi service constructor.
    * @property {module:api/HooksApi}
    */
    HooksApi,

    /**
    * The PdfApi service constructor.
    * @property {module:api/PdfApi}
    */
    PdfApi,

    /**
    * The ReportsApi service constructor.
    * @property {module:api/ReportsApi}
    */
    ReportsApi
};
