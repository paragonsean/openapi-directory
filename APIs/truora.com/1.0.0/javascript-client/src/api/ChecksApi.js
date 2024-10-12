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
import CheckDetailsOutput from '../model/CheckDetailsOutput';
import CheckOutput from '../model/CheckOutput';
import ChecksOutput from '../model/ChecksOutput';
import Database from '../model/Database';
import Error from '../model/Error';

/**
* Checks service.
* @module api/ChecksApi
* @version 1.0.0
*/
export default class ChecksApi {

    /**
    * Constructs a new ChecksApi. 
    * @alias module:api/ChecksApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the createCheck operation.
     * @callback module:api/ChecksApi~createCheckCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CheckOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a background check
     * Creates a background check and queues it to start collecting information. The full details of background checks can be retrieved with their respective Check IDs using getCheck endpoint. Keep in mind that, depending on the check type, input document, and country of a search, certain inputs are required. You should always provide as many inputs as possible in order to get the highest accuracy.  If your check type is not referenced in the following table, please reach out to find out the fields that apply for you.  | Country | Person-National | PersonForeigner | Company | Vehicle-National | Vehicle-Foreigner | |:-------:|:---------------:|:---------------:|:-------:|:----------------:|:-----------------:| | Chile<br>CL | national_id*<br>date_of_birth<br>phone_number | foreign_id*<br>date_of_birth*<br>phone_number<br>first_name*<br>last_name*<br>native_country* | N/A | national_id*<br>license_plate*<br>payment_date (Santiago only)<br>driver_license (Santiago only) | foreign_id*<br>first_name*<br>last_name*<br>date_of_birth*<br>native_country*<br>license_plate*<br>payment_date (Santiago only)<br>driver_license (Santiago only) | | Colombia<br>CO | national_id*<br>date_of_birth<br>issue_date<br>phone_number | foreign_id* or PEP*<br>date_of_birth<br>phone_number<br>issue_date* | tax_id*<br>national_id | national_id*<br>date_of_birth<br>phone_number<br>license_plate*<br>owner_document_type<br>owner_document_id | foreign_id*<br>date_of_birth<br>phone_number<br>license_plate*<br>issue_date* | | Mexico<br>MX | national_id*<br>phone_number | foreign_id* | tax_id* | license_plate*<br>national_id<br>vehicle_id<br>driver_license(Estado de Mexico only) | N/A | | Brazil<br>BR | national_id*<br>date_of_birth*<br>region*<br>phone_number | N/A | tax_id* | license_plate* | N/A | | Costa Rica<br>CR | national_id*<br>phone_number | foreign_id* | N/A | license_plate* | N/A | | Ecuador<br>EC | national_id*<br>phone_number | foreign_id* | tax_id* | license_plate* | N/A | | Peru<br>PE | national_id*<br>date_of_birth<br>phone_number | foreign_id*<br>ptp<br>date_of_birth*<br>phone_number | N/A | national_id*<br>date_of_birth<br>license_plate* | foreign_id*<br>ptp<br>date_of_birth*<br>license_plate* | | Argentina<br>AR | national_id* | N/A | N/A | national_id* | N/A | | International<br>ALL | name* | name* | company_name* | N/A | N/A |  (*) Required field
     * @param {module:model/String} country Document country
     * @param {module:model/String} type Background check type
     * @param {Object} opts Optional parameters
     * @param {module:model/String} [truoraPriority] Describes the background check priority. The amount of high priority checks is limited by country. Medium priority is used by default
     * @param {String} [birthCertificate] Person birth certificate
     * @param {String} [companyName] Company name \\\"Don't forget this required field to complete background checks in Brazil\\\"
     * @param {Date} [dateOfBirth] Person birthdate. This date is used to get some additional information about a person and to filter homonyms in some cases. YYYY-MM-DD format, Required for complete background checks in Brazil
     * @param {String} [diplomaticId] Diplomatic ID
     * @param {String} [driverLicense] Driver's license number
     * @param {String} [escrow] Colombian escrow
     * @param {String} [firstName] Person or entity first name. If the document type and number are not provided, the report might include homonyms. Required when searching by first name, Required in order to get complete background checks in Brazil
     * @param {Boolean} [forceCreation] Forces a new background check creation when true. Reuses recently created background checks otherwise
     * @param {String} [foreignId] Person foreign ID
     * @param {Date} [issueDate] Person document issue date in \\\"YYYY-mm-dd\\\" format (e.g. 2008-12-31) . This date is used to get some additional information about a person in some cases
     * @param {String} [lastName] Person or entity last name. If the document type and number are not provided, the report might include homonyms. Required when searching by last name. Required in order to get complete background checks in Brazil
     * @param {String} [licensePlate] Vehicle license plate
     * @param {String} [nationalId] National ID
     * @param {String} [nativeCountry] Country of birth
     * @param {String} [ownerDocumentId] National ID of the vehicle owner
     * @param {String} [ownerDocumentType] National ID, foreign ID, or tax ID
     * @param {String} [passport] Person passport
     * @param {Date} [paymentDate] Payment day of a vehicle circulation permit (Chile only)
     * @param {String} [pep] ID for Venezuelans working in Colombia
     * @param {String} [phoneNumber] Person phone number. Required by law to notify the person their background is being checked
     * @param {String} [professionalCard] Professional ID card
     * @param {String} [ptp] ID for Venezuelans working in Peru
     * @param {module:model/String} [region] Region where the background is to be checked in addition to the region where the person is from. By default, background checks in Brazil are performed in the region where the person is from. Required for Brazil only. Allowed values are: DF: Distrito Federal, AC: Acre, AL: Alagoas, AP: Amapá, AM: Amazonas, BA: Bahía, CE: Ceará, ES: Espírito Santo, GO: Goiás, MA: Maranhão, MT: Mato Grosso, MS: Mato Grosso do Sul, MG: Minas Gerais, PA: Pará, PB: Paraíba, PR: Paraná, PE: Pernambuco, PI: Piauí, RJ: Río de Janeiro, RN: Río Grande do Norte, RS: Río Grande do Sul, RO: Rondônia, RR: Roraima, SC: Santa Catarina, SP: São Paulo, SE: Sergipe, TO : Tocantins.
     * @param {String} [reportId] Report ID the background check will be inserted into
     * @param {String} [stateId]  Used for the RG (Registro Geral) identification in Brazil. This identification has different formats according to the state that issues the document. It can have numbers and letters but other characters (- * , . ) are omitted, Required in order to get complete background checks in Brazil
     * @param {String} [taxId] Company ID used for tax payments
     * @param {Boolean} [userAuthorized] Indicates whether the person subject to the validation authorized the validation. Must be true in order to proceed [Required for API key V1 or later]
     * @param {String} [vehicleId] Vehicle license plate
     * @param {String} [verificationCode] Verification code registered for criminal records in Peru only
     * @param {String} [watch] Indicates whether the check score is to be periodically revised and its frequency. It can be daily, weekly, monthly, yearly or have a custom frequency written as a number accompanied by d: day, w: week, m: month, y: year for instance: 3d: every three days, 2w: every two weeks. Ignore this field if the check is only to be performed once
     * @param {module:api/ChecksApi~createCheckCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CheckOutput}
     */
    createCheck(country, type, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'country' is set
      if (country === undefined || country === null) {
        throw new Error("Missing the required parameter 'country' when calling createCheck");
      }
      // verify the required parameter 'type' is set
      if (type === undefined || type === null) {
        throw new Error("Missing the required parameter 'type' when calling createCheck");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'Truora-Priority': opts['truoraPriority']
      };
      let formParams = {
        'birth_certificate': opts['birthCertificate'],
        'company_name': opts['companyName'],
        'country': country,
        'date_of_birth': opts['dateOfBirth'],
        'diplomatic_id': opts['diplomaticId'],
        'driver_license': opts['driverLicense'],
        'escrow': opts['escrow'],
        'first_name': opts['firstName'],
        'force_creation': opts['forceCreation'],
        'foreign_id': opts['foreignId'],
        'issue_date': opts['issueDate'],
        'last_name': opts['lastName'],
        'license_plate': opts['licensePlate'],
        'national_id': opts['nationalId'],
        'native_country': opts['nativeCountry'],
        'owner_document_id': opts['ownerDocumentId'],
        'owner_document_type': opts['ownerDocumentType'],
        'passport': opts['passport'],
        'payment_date': opts['paymentDate'],
        'pep': opts['pep'],
        'phone_number': opts['phoneNumber'],
        'professional_card': opts['professionalCard'],
        'ptp': opts['ptp'],
        'region': opts['region'],
        'report_id': opts['reportId'],
        'state_id': opts['stateId'],
        'tax_id': opts['taxId'],
        'type': type,
        'user_authorized': opts['userAuthorized'],
        'vehicle_id': opts['vehicleId'],
        'verification_code': opts['verificationCode'],
        'watch': opts['watch']
      };

      let authNames = ['api-key'];
      let contentTypes = ['application/x-www-form-urlencoded'];
      let accepts = ['application/json'];
      let returnType = CheckOutput;
      return this.apiClient.callApi(
        '/v1/checks', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getCheck operation.
     * @callback module:api/ChecksApi~getCheckCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CheckOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get Background Check
     * Returns the results of the check that matches the ID provided, complete with a set of scores explained below.  ### Scores:   - **Global Score**: Average risk associated with a person, company or vehicle, according to  the background check results. The global score considers results that are validated with the  ID number provided. The score ranges from 0 to 1, where 0 represents high risk and 1 low risk.   - **ID Score**: Average risk associated with a person according to the background check  results. The ID score considers the results that are validated with a person identity  document. The score ranges from 0 to 1, where 0 represents high risk and 1 low risk.    - **Homonym Score**: Average risk associated with a person according to the background check  results. The homonym score considers results that are validated against the name of a person and could not be validated with their ID number. These results might have homonyms associated with them. The score ranges from 0 to 1, where 0 represents high risk and 1 low risk.   In order to calculate these scores, a weighted average is considered with different weights allocated to each dataset. Scores can be customized using the config endpoints by assigning a weight to each dataset according to its relevance.  Keep in mind that results from the API vary depending on the country, check type and the inputs entered on check creation.
     * @param {String} checkId Check ID
     * @param {module:api/ChecksApi~getCheckCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CheckOutput}
     */
    getCheck(checkId, callback) {
      let postBody = null;
      // verify the required parameter 'checkId' is set
      if (checkId === undefined || checkId === null) {
        throw new Error("Missing the required parameter 'checkId' when calling getCheck");
      }

      let pathParams = {
        'check_id': checkId
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
      let returnType = CheckOutput;
      return this.apiClient.callApi(
        '/v1/checks/{check_id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getHealthDashboard operation.
     * @callback module:api/ChecksApi~getHealthDashboardCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/Database>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get Health Dashboard
     * Get the status of a database
     * @param {Object} opts Optional parameters
     * @param {String} [country] Country in ISO 3166, uppercase
     * @param {String} [unixTimestampSeconds] Unix timestamp in seconds. Send a day timestamp to view the database hourly status for that day or send the current time to know the current database status
     * @param {String} [unixtimezoneOffsetSeconds] Offset between the local time and the UTC time in seconds. (e.g., Colombia is at UTC -18000 seconds)  
     * @param {module:api/ChecksApi~getHealthDashboardCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/Database>}
     */
    getHealthDashboard(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'country': opts['country'],
        'unixTimestampSeconds': opts['unixTimestampSeconds'],
        'unixtimezoneOffsetSeconds': opts['unixtimezoneOffsetSeconds']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api-key'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [Database];
      return this.apiClient.callApi(
        '/v1/checks/health', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listCheckDetails operation.
     * @callback module:api/ChecksApi~listCheckDetailsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CheckDetailsOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List Check Details
     * Lists all details associated with a Check. It can be paginated.
     * @param {String} checkId ID of the Check
     * @param {Object} opts Optional parameters
     * @param {String} [startKey] Start key value for the pagination
     * @param {String} [lang] This parameter is used to specify the language wanted for details, if not specified details will come in their original language.
     * @param {module:api/ChecksApi~listCheckDetailsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CheckDetailsOutput}
     */
    listCheckDetails(checkId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'checkId' is set
      if (checkId === undefined || checkId === null) {
        throw new Error("Missing the required parameter 'checkId' when calling listCheckDetails");
      }

      let pathParams = {
        'check_id': checkId
      };
      let queryParams = {
        'start_key': opts['startKey'],
        'lang': opts['lang']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api-key'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = CheckDetailsOutput;
      return this.apiClient.callApi(
        '/v1/checks/{check_id}/details', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listChecks operation.
     * @callback module:api/ChecksApi~listChecksCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ChecksOutput} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List Checks
     * Lists the existing checks in the account or in a specified report.
     * @param {Object} opts Optional parameters
     * @param {String} [startKey] Start key value for the pagination
     * @param {String} [reportId] Report id checks to be returned
     * @param {module:api/ChecksApi~listChecksCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ChecksOutput}
     */
    listChecks(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'start_key': opts['startKey'],
        'report_id': opts['reportId']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api-key'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ChecksOutput;
      return this.apiClient.callApi(
        '/v1/checks', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
