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


import ApiClient from "../ApiClient";
import Error from '../model/Error';
import Hook from '../model/Hook';
import HookOutput from '../model/HookOutput';

/**
* Hooks service.
* @module api/HooksApi
* @version 1.0.0
*/
export default class HooksApi {

    /**
    * Constructs a new HooksApi. 
    * @alias module:api/HooksApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the createHook operation.
     * @callback module:api/HooksApi~createHookCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Hook} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Creates a hook subscription
     * Creates a hook subscription to notify events in Truora plataform. Subscriptions broadcast data as events occur and additional subscription instances are not required in order to refresh the information. Events are received in an array as a JWT and are decoded using the signing key returned by this endpoint. Their structure is as follows:  ``` {     \"events\": [         {             \"event_action\": \"created\",             \"event_type\": \"check\",             \"id\": \"HKEdd28c569cf5eb74e45f0f4c092096e62c1c95ba2\",             \"object\": {                 \"check_id\": \"CHK9c39003424c521aec8566ce59e1ddc86\",                 \"country\": \"CO\",                 \"creation_date\": \"2020-04-01T23:00:30.581232281Z\",                 \"homonym_score\": 0,                 \"id_score\": 0,                 \"national_id\": \"1151959906\",                 \"previous_check\": \"CHK4ec814fecd147eaae41027081d7d5caf\",                 \"score\": -1,                 \"status\": \"not_started\",                 \"type\": \"person\",                 \"update_date\": \"2020-04-01T23:00:30.680937413Z\"             },             \"timestamp\": \"2020-04-01T23:00:30Z\",             \"version\": \"1.0\"         }     ],     \"iat\": 1585782031,     \"iss\": \"Truora\" } ```  Keep in mind that the object attribute varies depending on the event_type.
     * @param {module:model/String} eventType The entity events the client wants to subscribe
     * @param {module:model/String} subscriberType A platform with an endpoint ready to process the information
     * @param {Object} opts Optional parameters
     * @param {Array.<String>} [actions] Actions you want to be notified. Possible inputs are created, started, and finished or any combination of those three
     * @param {module:model/String} [status] indicates whether the hook is active or not. enabled by default
     * @param {String} [subscriberAddress] Email address where the notification is to be sent. Required if subscriber_type was set to email
     * @param {module:model/String} [subscriberLanguage] Language for the notification to be sent
     * @param {String} [subscriberName] Name of the person to be notified
     * @param {String} [subscriberUrl] URL where the notification is to be sent. Required only if subscriber_type is set to web
     * @param {module:api/HooksApi~createHookCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Hook}
     */
    createHook(eventType, subscriberType, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'eventType' is set
      if (eventType === undefined || eventType === null) {
        throw new Error("Missing the required parameter 'eventType' when calling createHook");
      }
      // verify the required parameter 'subscriberType' is set
      if (subscriberType === undefined || subscriberType === null) {
        throw new Error("Missing the required parameter 'subscriberType' when calling createHook");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
        'actions': this.apiClient.buildCollectionParam(opts['actions'], 'csv'),
        'event_type': eventType,
        'status': opts['status'],
        'subscriber_address': opts['subscriberAddress'],
        'subscriber_language': opts['subscriberLanguage'],
        'subscriber_name': opts['subscriberName'],
        'subscriber_type': subscriberType,
        'subscriber_url': opts['subscriberUrl']
      };

      let authNames = ['api-key'];
      let contentTypes = ['application/x-www-form-urlencoded'];
      let accepts = ['application/json'];
      let returnType = Hook;
      return this.apiClient.callApi(
        '/v1/hooks', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deletHook operation.
     * @callback module:api/HooksApi~deletHookCallback
     * @param {String} error Error message, if any.
     * @param {String} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Deletes hook
     * Deletes hook configuration.
     * @param {String} hookId Hook ID
     * @param {module:api/HooksApi~deletHookCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link String}
     */
    deletHook(hookId, callback) {
      let postBody = null;
      // verify the required parameter 'hookId' is set
      if (hookId === undefined || hookId === null) {
        throw new Error("Missing the required parameter 'hookId' when calling deletHook");
      }

      let pathParams = {
        'hook_id': hookId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api-key'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = 'String';
      return this.apiClient.callApi(
        '/v1/hooks/{hook_id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listHook operation.
     * @callback module:api/HooksApi~listHookCallback
     * @param {String} error Error message, if any.
     * @param {module:model/HookOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Lists all hooks
     * Lists all the configured hooks in your account.
     * @param {module:api/HooksApi~listHookCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/HookOutput}
     */
    listHook(callback) {
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api-key'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = HookOutput;
      return this.apiClient.callApi(
        '/v1/hooks', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateHook operation.
     * @callback module:api/HooksApi~updateHookCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Hook} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Updates hook
     * Updates a hook configuration.
     * @param {String} hookId Hook ID
     * @param {module:model/String} eventType The entity events the client wants to subscribe
     * @param {module:model/String} subscriberType A platform with an endpoint ready to process the information
     * @param {Object} opts Optional parameters
     * @param {Array.<String>} [actions] Actions you want to be notified. Possible inputs are created, started, and finished or any combination of those three
     * @param {module:model/String} [status] indicates whether the hook is active or not. enabled by default
     * @param {String} [subscriberAddress] Email address where the notification is to be sent. Required if subscriber_type was set to email
     * @param {module:model/String} [subscriberLanguage] Language for the notification to be sent
     * @param {String} [subscriberName] Name of the person to be notified
     * @param {String} [subscriberUrl] URL where the notification is to be sent. Required only if subscriber_type is set to web
     * @param {module:api/HooksApi~updateHookCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Hook}
     */
    updateHook(hookId, eventType, subscriberType, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'hookId' is set
      if (hookId === undefined || hookId === null) {
        throw new Error("Missing the required parameter 'hookId' when calling updateHook");
      }
      // verify the required parameter 'eventType' is set
      if (eventType === undefined || eventType === null) {
        throw new Error("Missing the required parameter 'eventType' when calling updateHook");
      }
      // verify the required parameter 'subscriberType' is set
      if (subscriberType === undefined || subscriberType === null) {
        throw new Error("Missing the required parameter 'subscriberType' when calling updateHook");
      }

      let pathParams = {
        'hook_id': hookId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
        'actions': this.apiClient.buildCollectionParam(opts['actions'], 'csv'),
        'event_type': eventType,
        'status': opts['status'],
        'subscriber_address': opts['subscriberAddress'],
        'subscriber_language': opts['subscriberLanguage'],
        'subscriber_name': opts['subscriberName'],
        'subscriber_type': subscriberType,
        'subscriber_url': opts['subscriberUrl']
      };

      let authNames = ['api-key'];
      let contentTypes = ['application/x-www-form-urlencoded'];
      let accepts = ['application/x-www-form-urlencoded', 'application/json'];
      let returnType = Hook;
      return this.apiClient.callApi(
        '/v1/hooks/{hook_id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
