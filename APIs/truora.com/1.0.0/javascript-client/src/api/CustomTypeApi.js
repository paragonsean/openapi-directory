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
import ScoreConfigOutput from '../model/ScoreConfigOutput';
import ScoreConfigsOutput from '../model/ScoreConfigsOutput';

/**
* CustomType service.
* @module api/CustomTypeApi
* @version 1.0.0
*/
export default class CustomTypeApi {

    /**
    * Constructs a new CustomTypeApi. 
    * @alias module:api/CustomTypeApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the createScoreConfig operation.
     * @callback module:api/CustomTypeApi~createScoreConfigCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ScoreConfigOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create Score Configurations
     * Create a custom score configuration selecting the weight for each background check dataset and the country where it applies. Weights are numbers between 0 and 1 that represent how impactful the dataset is for the score. Keep in mind that the sum of all weights must equal 1.
     * @param {module:model/String} country Country where this set of rules applies. Use \\\"all\\\" if the check type searches by name by relying on international databases
     * @param {String} type Score configuration name. It cannot be person, vehicle, or company
     * @param {Object} opts Optional parameters
     * @param {Number} [datasetAffiliationsAndInsurances] Affiliation and insurance weight for score calculation. From 0 to 1
     * @param {Number} [datasetAlertInMedia] Alert in media weight for score calculation. From 0 to 1
     * @param {Number} [datasetBusinessBackground] Business background weight for score calculation. From 0 to 1
     * @param {Number} [datasetCriminalRecord] Criminal record weight for score calculation. From 0 to 1
     * @param {Number} [datasetDrivingLicenses] Driving license weight for score calculation. From 0 to 1
     * @param {Number} [datasetInternationalBackground] International background weight for score calculation. From 0 to 1
     * @param {Number} [datasetLegalBackground] Legal background weight for score calculation. From 0 to 1
     * @param {Number} [datasetPersonalIdentity] Personal identity weight for score calculation. From 0 to 1
     * @param {Number} [datasetProfessionalBackground] Professional background weight for score calculation. From 0 to 1
     * @param {Number} [datasetTaxesAndFinances] Taxes and financial background weight for score calculation. From 0 to 1
     * @param {Number} [datasetTrafficFines] Traffic fines weight for score calculation. From 0 to 1
     * @param {Number} [datasetVehicleInformation] Vehicle information weight for score calculation. From 0 to 1
     * @param {Number} [datasetVehiclePermits] Vehicle certificate background weight for score calculation. From 0 to 1
     * @param {module:api/CustomTypeApi~createScoreConfigCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ScoreConfigOutput}
     */
    createScoreConfig(country, type, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'country' is set
      if (country === undefined || country === null) {
        throw new Error("Missing the required parameter 'country' when calling createScoreConfig");
      }
      // verify the required parameter 'type' is set
      if (type === undefined || type === null) {
        throw new Error("Missing the required parameter 'type' when calling createScoreConfig");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
        'country': country,
        'dataset_affiliations_and_insurances': opts['datasetAffiliationsAndInsurances'],
        'dataset_alert_in_media': opts['datasetAlertInMedia'],
        'dataset_business_background': opts['datasetBusinessBackground'],
        'dataset_criminal_record': opts['datasetCriminalRecord'],
        'dataset_driving_licenses': opts['datasetDrivingLicenses'],
        'dataset_international_background': opts['datasetInternationalBackground'],
        'dataset_legal_background': opts['datasetLegalBackground'],
        'dataset_personal_identity': opts['datasetPersonalIdentity'],
        'dataset_professional_background': opts['datasetProfessionalBackground'],
        'dataset_taxes_and_finances': opts['datasetTaxesAndFinances'],
        'dataset_traffic_fines': opts['datasetTrafficFines'],
        'dataset_vehicle_information': opts['datasetVehicleInformation'],
        'dataset_vehicle_permits': opts['datasetVehiclePermits'],
        'type': type
      };

      let authNames = ['api-key'];
      let contentTypes = ['application/x-www-form-urlencoded'];
      let accepts = ['application/json'];
      let returnType = ScoreConfigOutput;
      return this.apiClient.callApi(
        '/v1/config', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteCustomType operation.
     * @callback module:api/CustomTypeApi~deleteCustomTypeCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete Custom Type
     * Allows deleting a custom type. Person, vehicle, and company types cannot be deleted
     * @param {String} type Name of the custom type to be deleted
     * @param {Object} opts Optional parameters
     * @param {module:model/String} [country] Country where the custom type is valid
     * @param {module:api/CustomTypeApi~deleteCustomTypeCallback} callback The callback function, accepting three arguments: error, data, response
     */
    deleteCustomType(type, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'type' is set
      if (type === undefined || type === null) {
        throw new Error("Missing the required parameter 'type' when calling deleteCustomType");
      }

      let pathParams = {
      };
      let queryParams = {
        'type': type,
        'country': opts['country']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api-key'];
      let contentTypes = [];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/v1/config', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listScoreConfigs operation.
     * @callback module:api/CustomTypeApi~listScoreConfigsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ScoreConfigsOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List Score Configurations
     * Lists the custom score configurations of the associated account.
     * @param {Object} opts Optional parameters
     * @param {String} [startKey] The key to start the pagination
     * @param {module:api/CustomTypeApi~listScoreConfigsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ScoreConfigsOutput}
     */
    listScoreConfigs(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'start_key': opts['startKey']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api-key'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ScoreConfigsOutput;
      return this.apiClient.callApi(
        '/v1/config', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateCustomType operation.
     * @callback module:api/CustomTypeApi~updateCustomTypeCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update Custom Type
     * Allows updating a custom type. Person, vehicle, and company types are not modifiable
     * @param {module:model/String} country Country where this set of rules applies. Use \\\"all\\\" if the check type searches by name by relying on international databases
     * @param {String} type Score configuration name. It cannot be person, vehicle, or company
     * @param {Object} opts Optional parameters
     * @param {Number} [datasetAffiliationsAndInsurances] Affiliation and insurance weight for score calculation. From 0 to 1
     * @param {Number} [datasetAlertInMedia] Alert in media weight for score calculation. From 0 to 1
     * @param {Number} [datasetBusinessBackground] Business background weight for score calculation. From 0 to 1
     * @param {Number} [datasetCriminalRecord] Criminal record weight for score calculation. From 0 to 1
     * @param {Number} [datasetDrivingLicenses] Driving license weight for score calculation. From 0 to 1
     * @param {Number} [datasetInternationalBackground] International background weight for score calculation. From 0 to 1
     * @param {Number} [datasetLegalBackground] Legal background weight for score calculation. From 0 to 1
     * @param {Number} [datasetPersonalIdentity] Personal identity weight for score calculation. From 0 to 1
     * @param {Number} [datasetProfessionalBackground] Professional background weight for score calculation. From 0 to 1
     * @param {Number} [datasetTaxesAndFinances] Taxes and financial background weight for score calculation. From 0 to 1
     * @param {Number} [datasetTrafficFines] Traffic fines weight for score calculation. From 0 to 1
     * @param {Number} [datasetVehicleInformation] Vehicle information weight for score calculation. From 0 to 1
     * @param {Number} [datasetVehiclePermits] Vehicle certificate background weight for score calculation. From 0 to 1
     * @param {module:api/CustomTypeApi~updateCustomTypeCallback} callback The callback function, accepting three arguments: error, data, response
     */
    updateCustomType(country, type, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'country' is set
      if (country === undefined || country === null) {
        throw new Error("Missing the required parameter 'country' when calling updateCustomType");
      }
      // verify the required parameter 'type' is set
      if (type === undefined || type === null) {
        throw new Error("Missing the required parameter 'type' when calling updateCustomType");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
        'country': country,
        'dataset_affiliations_and_insurances': opts['datasetAffiliationsAndInsurances'],
        'dataset_alert_in_media': opts['datasetAlertInMedia'],
        'dataset_business_background': opts['datasetBusinessBackground'],
        'dataset_criminal_record': opts['datasetCriminalRecord'],
        'dataset_driving_licenses': opts['datasetDrivingLicenses'],
        'dataset_international_background': opts['datasetInternationalBackground'],
        'dataset_legal_background': opts['datasetLegalBackground'],
        'dataset_personal_identity': opts['datasetPersonalIdentity'],
        'dataset_professional_background': opts['datasetProfessionalBackground'],
        'dataset_taxes_and_finances': opts['datasetTaxesAndFinances'],
        'dataset_traffic_fines': opts['datasetTrafficFines'],
        'dataset_vehicle_information': opts['datasetVehicleInformation'],
        'dataset_vehicle_permits': opts['datasetVehiclePermits'],
        'type': type
      };

      let authNames = ['api-key'];
      let contentTypes = ['application/x-www-form-urlencoded'];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/v1/config', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
