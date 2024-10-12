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
 * The VehicleSummary model module.
 * @module model/VehicleSummary
 * @version 1.0.0
 */
class VehicleSummary {
    /**
     * Constructs a new <code>VehicleSummary</code>.
     * Represents the summary of a vehicle background check
     * @alias module:model/VehicleSummary
     */
    constructor() { 
        
        VehicleSummary.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>VehicleSummary</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/VehicleSummary} obj Optional instance to populate.
     * @return {module:model/VehicleSummary} The populated <code>VehicleSummary</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new VehicleSummary();

            if (data.hasOwnProperty('capacity')) {
                obj['capacity'] = ApiClient.convertToType(data['capacity'], 'Number');
            }
            if (data.hasOwnProperty('color')) {
                obj['color'] = ApiClient.convertToType(data['color'], 'String');
            }
            if (data.hasOwnProperty('license_plate')) {
                obj['license_plate'] = ApiClient.convertToType(data['license_plate'], 'String');
            }
            if (data.hasOwnProperty('manufacturer')) {
                obj['manufacturer'] = ApiClient.convertToType(data['manufacturer'], 'String');
            }
            if (data.hasOwnProperty('model')) {
                obj['model'] = ApiClient.convertToType(data['model'], 'String');
            }
            if (data.hasOwnProperty('number_of_doors')) {
                obj['number_of_doors'] = ApiClient.convertToType(data['number_of_doors'], 'Number');
            }
            if (data.hasOwnProperty('obligatory_insurance_expiration_date')) {
                obj['obligatory_insurance_expiration_date'] = ApiClient.convertToType(data['obligatory_insurance_expiration_date'], 'Date');
            }
            if (data.hasOwnProperty('obligatory_insurance_status')) {
                obj['obligatory_insurance_status'] = ApiClient.convertToType(data['obligatory_insurance_status'], 'String');
            }
            if (data.hasOwnProperty('service_type')) {
                obj['service_type'] = ApiClient.convertToType(data['service_type'], 'String');
            }
            if (data.hasOwnProperty('vehicle_category')) {
                obj['vehicle_category'] = ApiClient.convertToType(data['vehicle_category'], 'String');
            }
            if (data.hasOwnProperty('vehicle_id')) {
                obj['vehicle_id'] = ApiClient.convertToType(data['vehicle_id'], 'String');
            }
            if (data.hasOwnProperty('vehicle_type')) {
                obj['vehicle_type'] = ApiClient.convertToType(data['vehicle_type'], 'String');
            }
            if (data.hasOwnProperty('year')) {
                obj['year'] = ApiClient.convertToType(data['year'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>VehicleSummary</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>VehicleSummary</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['color'] && !(typeof data['color'] === 'string' || data['color'] instanceof String)) {
            throw new Error("Expected the field `color` to be a primitive type in the JSON string but got " + data['color']);
        }
        // ensure the json data is a string
        if (data['license_plate'] && !(typeof data['license_plate'] === 'string' || data['license_plate'] instanceof String)) {
            throw new Error("Expected the field `license_plate` to be a primitive type in the JSON string but got " + data['license_plate']);
        }
        // ensure the json data is a string
        if (data['manufacturer'] && !(typeof data['manufacturer'] === 'string' || data['manufacturer'] instanceof String)) {
            throw new Error("Expected the field `manufacturer` to be a primitive type in the JSON string but got " + data['manufacturer']);
        }
        // ensure the json data is a string
        if (data['model'] && !(typeof data['model'] === 'string' || data['model'] instanceof String)) {
            throw new Error("Expected the field `model` to be a primitive type in the JSON string but got " + data['model']);
        }
        // ensure the json data is a string
        if (data['obligatory_insurance_status'] && !(typeof data['obligatory_insurance_status'] === 'string' || data['obligatory_insurance_status'] instanceof String)) {
            throw new Error("Expected the field `obligatory_insurance_status` to be a primitive type in the JSON string but got " + data['obligatory_insurance_status']);
        }
        // ensure the json data is a string
        if (data['service_type'] && !(typeof data['service_type'] === 'string' || data['service_type'] instanceof String)) {
            throw new Error("Expected the field `service_type` to be a primitive type in the JSON string but got " + data['service_type']);
        }
        // ensure the json data is a string
        if (data['vehicle_category'] && !(typeof data['vehicle_category'] === 'string' || data['vehicle_category'] instanceof String)) {
            throw new Error("Expected the field `vehicle_category` to be a primitive type in the JSON string but got " + data['vehicle_category']);
        }
        // ensure the json data is a string
        if (data['vehicle_id'] && !(typeof data['vehicle_id'] === 'string' || data['vehicle_id'] instanceof String)) {
            throw new Error("Expected the field `vehicle_id` to be a primitive type in the JSON string but got " + data['vehicle_id']);
        }
        // ensure the json data is a string
        if (data['vehicle_type'] && !(typeof data['vehicle_type'] === 'string' || data['vehicle_type'] instanceof String)) {
            throw new Error("Expected the field `vehicle_type` to be a primitive type in the JSON string but got " + data['vehicle_type']);
        }

        return true;
    }


}



/**
 * Number of passengers allowed to travel in the vehicle
 * @member {Number} capacity
 */
VehicleSummary.prototype['capacity'] = undefined;

/**
 * Vehicle color
 * @member {String} color
 */
VehicleSummary.prototype['color'] = undefined;

/**
 * Vehicle license plate
 * @member {String} license_plate
 */
VehicleSummary.prototype['license_plate'] = undefined;

/**
 * Vehicle manufacturer
 * @member {String} manufacturer
 */
VehicleSummary.prototype['manufacturer'] = undefined;

/**
 * Vehicle model
 * @member {String} model
 */
VehicleSummary.prototype['model'] = undefined;

/**
 * Vehicle door count
 * @member {Number} number_of_doors
 */
VehicleSummary.prototype['number_of_doors'] = undefined;

/**
 * Expiration date of the vehicle compulsory insurance 
 * @member {Date} obligatory_insurance_expiration_date
 */
VehicleSummary.prototype['obligatory_insurance_expiration_date'] = undefined;

/**
 * Status of the vehicle compulsory insurances
 * @member {String} obligatory_insurance_status
 */
VehicleSummary.prototype['obligatory_insurance_status'] = undefined;

/**
 * Vehicle service type
 * @member {String} service_type
 */
VehicleSummary.prototype['service_type'] = undefined;

/**
 * Vehicle category
 * @member {String} vehicle_category
 */
VehicleSummary.prototype['vehicle_category'] = undefined;

/**
 * Vehicle ID
 * @member {String} vehicle_id
 */
VehicleSummary.prototype['vehicle_id'] = undefined;

/**
 * Vehicle type
 * @member {String} vehicle_type
 */
VehicleSummary.prototype['vehicle_type'] = undefined;

/**
 * Vehicle model year
 * @member {Number} year
 */
VehicleSummary.prototype['year'] = undefined;






export default VehicleSummary;

