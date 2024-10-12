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

import ApiClient from '../ApiClient';

/**
 * The Status model module.
 * @module model/Status
 * @version 1.0.0
 */
class Status {
    /**
     * Constructs a new <code>Status</code>.
     * Represents the status of databases used to generate background checks
     * @alias module:model/Status
     */
    constructor() { 
        
        Status.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Status</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Status} obj Optional instance to populate.
     * @return {module:model/Status} The populated <code>Status</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Status();

            if (data.hasOwnProperty('data_set')) {
                obj['data_set'] = ApiClient.convertToType(data['data_set'], 'String');
            }
            if (data.hasOwnProperty('database_id')) {
                obj['database_id'] = ApiClient.convertToType(data['database_id'], 'String');
            }
            if (data.hasOwnProperty('database_name')) {
                obj['database_name'] = ApiClient.convertToType(data['database_name'], 'String');
            }
            if (data.hasOwnProperty('invalid_inputs')) {
                obj['invalid_inputs'] = ApiClient.convertToType(data['invalid_inputs'], ['String']);
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Status</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Status</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['data_set'] && !(typeof data['data_set'] === 'string' || data['data_set'] instanceof String)) {
            throw new Error("Expected the field `data_set` to be a primitive type in the JSON string but got " + data['data_set']);
        }
        // ensure the json data is a string
        if (data['database_id'] && !(typeof data['database_id'] === 'string' || data['database_id'] instanceof String)) {
            throw new Error("Expected the field `database_id` to be a primitive type in the JSON string but got " + data['database_id']);
        }
        // ensure the json data is a string
        if (data['database_name'] && !(typeof data['database_name'] === 'string' || data['database_name'] instanceof String)) {
            throw new Error("Expected the field `database_name` to be a primitive type in the JSON string but got " + data['database_name']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['invalid_inputs'])) {
            throw new Error("Expected the field `invalid_inputs` to be an array in the JSON data but got " + data['invalid_inputs']);
        }
        // ensure the json data is a string
        if (data['status'] && !(typeof data['status'] === 'string' || data['status'] instanceof String)) {
            throw new Error("Expected the field `status` to be a primitive type in the JSON string but got " + data['status']);
        }

        return true;
    }


}



/**
 * Background check dataset
 * @member {module:model/Status.DataSetEnum} data_set
 */
Status.prototype['data_set'] = undefined;

/**
 * Database ID. Can be used to verify the database status
 * @member {String} database_id
 */
Status.prototype['database_id'] = undefined;

/**
 * Background check database name. Do not use this field to identify the database as it may change during the check execution. Use database_id instead
 * @member {String} database_name
 */
Status.prototype['database_name'] = undefined;

/**
 * List of missing or invalid inputs
 * @member {Array.<String>} invalid_inputs
 */
Status.prototype['invalid_inputs'] = undefined;

/**
 * Result status of the background check. **Not_started** means the background check is still in queue, since there is a limit of background checks that can be processed simultaneously, **completed** means the search finished successfully, **error** means the search failed, **expired** means the search took too long to finish and therefore failed, **skipped** means the search failed because a wrong number or type of parameters was provided, **delayed** means the search is waiting for an additional requirement to be met and can last up to 3 days
 * @member {module:model/Status.StatusEnum} status
 */
Status.prototype['status'] = undefined;





/**
 * Allowed values for the <code>data_set</code> property.
 * @enum {String}
 * @readonly
 */
Status['DataSetEnum'] = {

    /**
     * value: "affiliations_and_insurances"
     * @const
     */
    "affiliations_and_insurances": "affiliations_and_insurances",

    /**
     * value: "alert_in_media"
     * @const
     */
    "alert_in_media": "alert_in_media",

    /**
     * value: "behavior"
     * @const
     */
    "behavior": "behavior",

    /**
     * value: "business_background"
     * @const
     */
    "business_background": "business_background",

    /**
     * value: "criminal_record"
     * @const
     */
    "criminal_record": "criminal_record",

    /**
     * value: "driving_licenses"
     * @const
     */
    "driving_licenses": "driving_licenses",

    /**
     * value: "international_background"
     * @const
     */
    "international_background": "international_background",

    /**
     * value: "legal_background"
     * @const
     */
    "legal_background": "legal_background",

    /**
     * value: "personal_identity"
     * @const
     */
    "personal_identity": "personal_identity",

    /**
     * value: "professional_background"
     * @const
     */
    "professional_background": "professional_background",

    /**
     * value: "traffic_fines"
     * @const
     */
    "traffic_fines": "traffic_fines",

    /**
     * value: "vehicle_information"
     * @const
     */
    "vehicle_information": "vehicle_information",

    /**
     * value: "vehicle_permits"
     * @const
     */
    "vehicle_permits": "vehicle_permits",

    /**
     * value: "taxes_and_finances"
     * @const
     */
    "taxes_and_finances": "taxes_and_finances"
};


/**
 * Allowed values for the <code>status</code> property.
 * @enum {String}
 * @readonly
 */
Status['StatusEnum'] = {

    /**
     * value: "not_started"
     * @const
     */
    "not_started": "not_started",

    /**
     * value: "completed"
     * @const
     */
    "completed": "completed",

    /**
     * value: "expired"
     * @const
     */
    "expired": "expired",

    /**
     * value: "error"
     * @const
     */
    "error": "error",

    /**
     * value: "delayed"
     * @const
     */
    "delayed": "delayed",

    /**
     * value: "skipped"
     * @const
     */
    "skipped": "skipped"
};



export default Status;

