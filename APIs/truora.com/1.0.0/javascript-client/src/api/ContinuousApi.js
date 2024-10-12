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
import ContinuousCheck from '../model/ContinuousCheck';
import Error from '../model/Error';
import GetContiuousCheckHistoryOutput from '../model/GetContiuousCheckHistoryOutput';
import ListContinuousChecksOutput from '../model/ListContinuousChecksOutput';

/**
* Continuous service.
* @module api/ContinuousApi
* @version 1.0.0
*/
export default class ContinuousApi {

    /**
    * Constructs a new ContinuousApi. 
    * @alias module:api/ContinuousApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the createContinuousCheck operation.
     * @callback module:api/ContinuousApi~createContinuousCheckCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ContinuousCheck} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Creates a continuous check that will run background checks recurrently according to the frequency provided.
     * @param {Object} opts Optional parameters
     * @param {String} [checkId] Background checks to be processed recurrently
     * @param {String} [frequency] Time between background checks. It can be daily, weekly, monthly, yearly or have a custom frequency written as a number accompanied by d: day, w: week, m: month, y: year for instance: 3d: every three days, 2w: every two weeks
     * @param {String} [status] Indicates whether the background checks must be processed recurrently (enabled | disabled)
     * @param {module:api/ContinuousApi~createContinuousCheckCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ContinuousCheck}
     */
    createContinuousCheck(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
        'check_id': opts['checkId'],
        'frequency': opts['frequency'],
        'status': opts['status']
      };

      let authNames = ['api-key'];
      let contentTypes = ['application/x-www-form-urlencoded'];
      let accepts = ['application/json'];
      let returnType = ContinuousCheck;
      return this.apiClient.callApi(
        '/v1/continuous-checks', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getContinuousCheck operation.
     * @callback module:api/ContinuousApi~getContinuousCheckCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ContinuousCheck} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Lists history associated with a Check. It can be paginated
     * @param {Number} continuousCheckId ID resulting from calling CreateContinuousCheck
     * @param {module:api/ContinuousApi~getContinuousCheckCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ContinuousCheck}
     */
    getContinuousCheck(continuousCheckId, callback) {
      let postBody = null;
      // verify the required parameter 'continuousCheckId' is set
      if (continuousCheckId === undefined || continuousCheckId === null) {
        throw new Error("Missing the required parameter 'continuousCheckId' when calling getContinuousCheck");
      }

      let pathParams = {
        'continuous_check_id': continuousCheckId
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
      let returnType = ContinuousCheck;
      return this.apiClient.callApi(
        '/v1/continuous-checks/{continuous_check_id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listContinuousChecks operation.
     * @callback module:api/ContinuousApi~listContinuousChecksCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListContinuousChecksOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Lists all continuous checks
     * @param {module:api/ContinuousApi~listContinuousChecksCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListContinuousChecksOutput}
     */
    listContinuousChecks(callback) {
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
      let returnType = ListContinuousChecksOutput;
      return this.apiClient.callApi(
        '/v1/continuous-checks', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateContinuousCheck operation.
     * @callback module:api/ContinuousApi~updateContinuousCheckCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ContinuousCheck} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Updates a continuous check
     * @param {Number} continuousCheckId ID resulting from calling CreateContinuousCheck
     * @param {String} frequency Time between background checks
     * @param {module:model/String} status Indicates whether the background checks must be processed recurrently
     * @param {module:api/ContinuousApi~updateContinuousCheckCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ContinuousCheck}
     */
    updateContinuousCheck(continuousCheckId, frequency, status, callback) {
      let postBody = null;
      // verify the required parameter 'continuousCheckId' is set
      if (continuousCheckId === undefined || continuousCheckId === null) {
        throw new Error("Missing the required parameter 'continuousCheckId' when calling updateContinuousCheck");
      }
      // verify the required parameter 'frequency' is set
      if (frequency === undefined || frequency === null) {
        throw new Error("Missing the required parameter 'frequency' when calling updateContinuousCheck");
      }
      // verify the required parameter 'status' is set
      if (status === undefined || status === null) {
        throw new Error("Missing the required parameter 'status' when calling updateContinuousCheck");
      }

      let pathParams = {
        'continuous_check_id': continuousCheckId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
        'frequency': frequency,
        'status': status
      };

      let authNames = ['api-key'];
      let contentTypes = ['application/x-www-form-urlencoded'];
      let accepts = ['application/json'];
      let returnType = ContinuousCheck;
      return this.apiClient.callApi(
        '/v1/continuous-checks/{continuous_check_id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the v1ContinuousChecksContinuousCheckIdHistoryGet operation.
     * @callback module:api/ContinuousApi~v1ContinuousChecksContinuousCheckIdHistoryGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetContiuousCheckHistoryOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Lists background check logs. It can be paginated  
     * @param {String} continuousCheckId 
     * @param {module:api/ContinuousApi~v1ContinuousChecksContinuousCheckIdHistoryGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetContiuousCheckHistoryOutput}
     */
    v1ContinuousChecksContinuousCheckIdHistoryGet(continuousCheckId, callback) {
      let postBody = null;
      // verify the required parameter 'continuousCheckId' is set
      if (continuousCheckId === undefined || continuousCheckId === null) {
        throw new Error("Missing the required parameter 'continuousCheckId' when calling v1ContinuousChecksContinuousCheckIdHistoryGet");
      }

      let pathParams = {
        'continuous_check_id': continuousCheckId
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
      let returnType = GetContiuousCheckHistoryOutput;
      return this.apiClient.callApi(
        '/v1/continuous-checks/{continuous_check_id}/history', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
