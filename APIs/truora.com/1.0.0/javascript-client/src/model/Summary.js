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
import NameFound from './NameFound';

/**
 * The Summary model module.
 * @module model/Summary
 * @version 1.0.0
 */
class Summary {
    /**
     * Constructs a new <code>Summary</code>.
     * Represents a background check summary
     * @alias module:model/Summary
     * @param namesFound {Array.<module:model/NameFound>} Names found during the background check process
     */
    constructor(namesFound) { 
        
        Summary.initialize(this, namesFound);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, namesFound) { 
        obj['names_found'] = namesFound;
    }

    /**
     * Constructs a <code>Summary</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Summary} obj Optional instance to populate.
     * @return {module:model/Summary} The populated <code>Summary</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Summary();

            if (data.hasOwnProperty('date_of_birth')) {
                obj['date_of_birth'] = ApiClient.convertToType(data['date_of_birth'], 'Date');
            }
            if (data.hasOwnProperty('death_date')) {
                obj['death_date'] = ApiClient.convertToType(data['death_date'], 'Date');
            }
            if (data.hasOwnProperty('drivers_license')) {
                obj['drivers_license'] = ApiClient.convertToType(data['drivers_license'], 'String');
            }
            if (data.hasOwnProperty('gender')) {
                obj['gender'] = ApiClient.convertToType(data['gender'], 'String');
            }
            if (data.hasOwnProperty('identity_status')) {
                obj['identity_status'] = ApiClient.convertToType(data['identity_status'], 'String');
            }
            if (data.hasOwnProperty('names_found')) {
                obj['names_found'] = ApiClient.convertToType(data['names_found'], [NameFound]);
            }
            if (data.hasOwnProperty('nss')) {
                obj['nss'] = ApiClient.convertToType(data['nss'], 'String');
            }
            if (data.hasOwnProperty('rfc')) {
                obj['rfc'] = ApiClient.convertToType(data['rfc'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Summary</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Summary</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of Summary.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['drivers_license'] && !(typeof data['drivers_license'] === 'string' || data['drivers_license'] instanceof String)) {
            throw new Error("Expected the field `drivers_license` to be a primitive type in the JSON string but got " + data['drivers_license']);
        }
        // ensure the json data is a string
        if (data['gender'] && !(typeof data['gender'] === 'string' || data['gender'] instanceof String)) {
            throw new Error("Expected the field `gender` to be a primitive type in the JSON string but got " + data['gender']);
        }
        // ensure the json data is a string
        if (data['identity_status'] && !(typeof data['identity_status'] === 'string' || data['identity_status'] instanceof String)) {
            throw new Error("Expected the field `identity_status` to be a primitive type in the JSON string but got " + data['identity_status']);
        }
        if (data['names_found']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['names_found'])) {
                throw new Error("Expected the field `names_found` to be an array in the JSON data but got " + data['names_found']);
            }
            // validate the optional field `names_found` (array)
            for (const item of data['names_found']) {
                NameFound.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['nss'] && !(typeof data['nss'] === 'string' || data['nss'] instanceof String)) {
            throw new Error("Expected the field `nss` to be a primitive type in the JSON string but got " + data['nss']);
        }
        // ensure the json data is a string
        if (data['rfc'] && !(typeof data['rfc'] === 'string' || data['rfc'] instanceof String)) {
            throw new Error("Expected the field `rfc` to be a primitive type in the JSON string but got " + data['rfc']);
        }

        return true;
    }


}

Summary.RequiredProperties = ["names_found"];

/**
 * Person date of birth in RFC3339 format
 * @member {Date} date_of_birth
 */
Summary.prototype['date_of_birth'] = undefined;

/**
 * Person date of death
 * @member {Date} death_date
 */
Summary.prototype['death_date'] = undefined;

/**
 * Person driver's license
 * @member {String} drivers_license
 */
Summary.prototype['drivers_license'] = undefined;

/**
 * Person gender
 * @member {module:model/Summary.GenderEnum} gender
 */
Summary.prototype['gender'] = undefined;

/**
 * Indicates whether a person was found, found as dead or not found at all
 * @member {module:model/Summary.IdentityStatusEnum} identity_status
 */
Summary.prototype['identity_status'] = undefined;

/**
 * Names found during the background check process
 * @member {Array.<module:model/NameFound>} names_found
 */
Summary.prototype['names_found'] = undefined;

/**
 * Social security number of the person (Mexico)
 * @member {String} nss
 */
Summary.prototype['nss'] = undefined;

/**
 * Federal taxpayer registration number of the person
 * @member {String} rfc
 */
Summary.prototype['rfc'] = undefined;





/**
 * Allowed values for the <code>gender</code> property.
 * @enum {String}
 * @readonly
 */
Summary['GenderEnum'] = {

    /**
     * value: "male"
     * @const
     */
    "male": "male",

    /**
     * value: "female"
     * @const
     */
    "female": "female"
};


/**
 * Allowed values for the <code>identity_status</code> property.
 * @enum {String}
 * @readonly
 */
Summary['IdentityStatusEnum'] = {

    /**
     * value: "found"
     * @const
     */
    "found": "found",

    /**
     * value: "not_found"
     * @const
     */
    "not_found": "not_found",

    /**
     * value: "dead"
     * @const
     */
    "dead": "dead"
};



export default Summary;

