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
import BehaviourOutput from '../model/BehaviourOutput';
import Error from '../model/Error';

/**
* Behavior service.
* @module api/BehaviorApi
* @version 1.0.0
*/
export default class BehaviorApi {

    /**
    * Constructs a new BehaviorApi. 
    * @alias module:api/BehaviorApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the reportBehavior operation.
     * @callback module:api/BehaviorApi~reportBehaviorCallback
     * @param {String} error Error message, if any.
     * @param {module:model/BehaviourOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Report Behavior
     * Creates a behavior item to report employee conducts that do not or might not be included in their background check. This report includes both possitive and negative behaviors and sorts them by severity.  ### Reasons to report a person  <table>   <tr>     <td style=\"width: 100px\"><center><b>Very High</b><br>(Score: 1)</td>     <td>Rape, Drug Dealing, Sexual Harassment</td>   </tr>   <tr>     <td><center><b>High</b><br>(Score: 0.8)</td>     <td>Theft, Fights, Aggressive Behaviour, Identity Fraud, Drunk, Drug Possession</td>   </tr>   <tr>     <td><center><b>Medium</b><br>(Score: 0.6)</td>     <td>Absences</td>   </tr>   <tr>     <td><center><b>Low</b><br>(Score: 0.4)</td>     <td>Tardiness, Confidentiality Breach</td>   </tr>   <tr>     <td><center><b>None</b><br>(Score: 0)</td>     <td>Good Reputation</td>   </tr>   <tr>     <td><center><b>Unknown</b></td>     <td>No information</td>   </tr> </table>  **NOTE:** If the reason of your report is not here, please contact Truora support team. 
     * @param {Date} birthDate Birth date of reported person
     * @param {module:model/String} country Document country
     * @param {String} documentId Person document ID
     * @param {module:model/String} documentType Document type associated with the background check
     * @param {String} email Reported person e-mail
     * @param {Date} feedbackDate Behavior report date
     * @param {String} firstName Person first name
     * @param {String} lastName Person last name
     * @param {module:model/String} reason Report reason
     * @param {Object} opts Optional parameters
     * @param {String} [phoneNumber] Phone number of the reported person
     * @param {module:api/BehaviorApi~reportBehaviorCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/BehaviourOutput}
     */
    reportBehavior(birthDate, country, documentId, documentType, email, feedbackDate, firstName, lastName, reason, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'birthDate' is set
      if (birthDate === undefined || birthDate === null) {
        throw new Error("Missing the required parameter 'birthDate' when calling reportBehavior");
      }
      // verify the required parameter 'country' is set
      if (country === undefined || country === null) {
        throw new Error("Missing the required parameter 'country' when calling reportBehavior");
      }
      // verify the required parameter 'documentId' is set
      if (documentId === undefined || documentId === null) {
        throw new Error("Missing the required parameter 'documentId' when calling reportBehavior");
      }
      // verify the required parameter 'documentType' is set
      if (documentType === undefined || documentType === null) {
        throw new Error("Missing the required parameter 'documentType' when calling reportBehavior");
      }
      // verify the required parameter 'email' is set
      if (email === undefined || email === null) {
        throw new Error("Missing the required parameter 'email' when calling reportBehavior");
      }
      // verify the required parameter 'feedbackDate' is set
      if (feedbackDate === undefined || feedbackDate === null) {
        throw new Error("Missing the required parameter 'feedbackDate' when calling reportBehavior");
      }
      // verify the required parameter 'firstName' is set
      if (firstName === undefined || firstName === null) {
        throw new Error("Missing the required parameter 'firstName' when calling reportBehavior");
      }
      // verify the required parameter 'lastName' is set
      if (lastName === undefined || lastName === null) {
        throw new Error("Missing the required parameter 'lastName' when calling reportBehavior");
      }
      // verify the required parameter 'reason' is set
      if (reason === undefined || reason === null) {
        throw new Error("Missing the required parameter 'reason' when calling reportBehavior");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
        'birth_date': birthDate,
        'country': country,
        'document_id': documentId,
        'document_type': documentType,
        'email': email,
        'feedback_date': feedbackDate,
        'first_name': firstName,
        'last_name': lastName,
        'phone_number': opts['phoneNumber'],
        'reason': reason
      };

      let authNames = ['api-key'];
      let contentTypes = ['application/x-www-form-urlencoded'];
      let accepts = ['application/json'];
      let returnType = BehaviourOutput;
      return this.apiClient.callApi(
        '/v1/behavior', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
