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
import CompanySummary from './CompanySummary';
import Score from './Score';
import Status from './Status';
import Summary from './Summary';
import VehicleSummary from './VehicleSummary';
import WrongInput from './WrongInput';

/**
 * The Check model module.
 * @module model/Check
 * @version 1.0.0
 */
class Check {
    /**
     * Constructs a new <code>Check</code>.
     * Represents a background check
     * @alias module:model/Check
     * @param checkId {String} Background check ID
     * @param country {module:model/Check.CountryEnum} ID Document country
     * @param creationDate {Date} Background check creation date
     * @param idScore {Number} Background check score regarding results by ID number only. It is a number between 0 and 1 where 1 is the best score. This result is a weighted average of the id_scores listed under scores.
     * @param score {Number} Background check score. Number between 0 and 1 where 1 is the best score
     * @param status {module:model/Check.StatusEnum} Result status of the background check. **Not_started** means the background check is still in queue, since there is a limit of background checks that can be processed simultaneously, **completed** means the check finished successfully, **error** means the check failed, **in_progress** means the check is currently being processed, **delayed** means the check is waiting for an additional requirement to be met, this can last up to 3 days. **Completed** and **error** are the two only final statuses
     * @param statuses {Array.<module:model/Status>} Database status list
     * @param summary {module:model/Summary} 
     * @param type {module:model/Check.TypeEnum} Background check type
     */
    constructor(checkId, country, creationDate, idScore, score, status, statuses, summary, type) { 
        
        Check.initialize(this, checkId, country, creationDate, idScore, score, status, statuses, summary, type);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, checkId, country, creationDate, idScore, score, status, statuses, summary, type) { 
        obj['check_id'] = checkId;
        obj['country'] = country;
        obj['creation_date'] = creationDate;
        obj['id_score'] = idScore;
        obj['score'] = score;
        obj['status'] = status;
        obj['statuses'] = statuses;
        obj['summary'] = summary;
        obj['type'] = type;
    }

    /**
     * Constructs a <code>Check</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Check} obj Optional instance to populate.
     * @return {module:model/Check} The populated <code>Check</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Check();

            if (data.hasOwnProperty('birth_certificate')) {
                obj['birth_certificate'] = ApiClient.convertToType(data['birth_certificate'], 'String');
            }
            if (data.hasOwnProperty('check_id')) {
                obj['check_id'] = ApiClient.convertToType(data['check_id'], 'String');
            }
            if (data.hasOwnProperty('company_summary')) {
                obj['company_summary'] = CompanySummary.constructFromObject(data['company_summary']);
            }
            if (data.hasOwnProperty('country')) {
                obj['country'] = ApiClient.convertToType(data['country'], 'String');
            }
            if (data.hasOwnProperty('creation_date')) {
                obj['creation_date'] = ApiClient.convertToType(data['creation_date'], 'Date');
            }
            if (data.hasOwnProperty('date_of_birth')) {
                obj['date_of_birth'] = ApiClient.convertToType(data['date_of_birth'], 'Date');
            }
            if (data.hasOwnProperty('diplomatic_id')) {
                obj['diplomatic_id'] = ApiClient.convertToType(data['diplomatic_id'], 'String');
            }
            if (data.hasOwnProperty('driver_license')) {
                obj['driver_license'] = ApiClient.convertToType(data['driver_license'], 'String');
            }
            if (data.hasOwnProperty('first_name')) {
                obj['first_name'] = ApiClient.convertToType(data['first_name'], 'String');
            }
            if (data.hasOwnProperty('foreign_id')) {
                obj['foreign_id'] = ApiClient.convertToType(data['foreign_id'], 'String');
            }
            if (data.hasOwnProperty('homonym_probability')) {
                obj['homonym_probability'] = ApiClient.convertToType(data['homonym_probability'], 'Number');
            }
            if (data.hasOwnProperty('homonym_score')) {
                obj['homonym_score'] = ApiClient.convertToType(data['homonym_score'], 'Number');
            }
            if (data.hasOwnProperty('homonym_scores')) {
                obj['homonym_scores'] = ApiClient.convertToType(data['homonym_scores'], [Score]);
            }
            if (data.hasOwnProperty('id_score')) {
                obj['id_score'] = ApiClient.convertToType(data['id_score'], 'Number');
            }
            if (data.hasOwnProperty('issue_date')) {
                obj['issue_date'] = ApiClient.convertToType(data['issue_date'], 'Date');
            }
            if (data.hasOwnProperty('last_name')) {
                obj['last_name'] = ApiClient.convertToType(data['last_name'], 'String');
            }
            if (data.hasOwnProperty('license_plate')) {
                obj['license_plate'] = ApiClient.convertToType(data['license_plate'], 'String');
            }
            if (data.hasOwnProperty('national_id')) {
                obj['national_id'] = ApiClient.convertToType(data['national_id'], 'String');
            }
            if (data.hasOwnProperty('native_country')) {
                obj['native_country'] = ApiClient.convertToType(data['native_country'], 'String');
            }
            if (data.hasOwnProperty('owner_document_id')) {
                obj['owner_document_id'] = ApiClient.convertToType(data['owner_document_id'], 'String');
            }
            if (data.hasOwnProperty('owner_document_type')) {
                obj['owner_document_type'] = ApiClient.convertToType(data['owner_document_type'], 'String');
            }
            if (data.hasOwnProperty('passport')) {
                obj['passport'] = ApiClient.convertToType(data['passport'], 'String');
            }
            if (data.hasOwnProperty('payment_date')) {
                obj['payment_date'] = ApiClient.convertToType(data['payment_date'], 'String');
            }
            if (data.hasOwnProperty('pep')) {
                obj['pep'] = ApiClient.convertToType(data['pep'], 'String');
            }
            if (data.hasOwnProperty('phone_number')) {
                obj['phone_number'] = ApiClient.convertToType(data['phone_number'], 'String');
            }
            if (data.hasOwnProperty('professional_card')) {
                obj['professional_card'] = ApiClient.convertToType(data['professional_card'], 'String');
            }
            if (data.hasOwnProperty('ptp')) {
                obj['ptp'] = ApiClient.convertToType(data['ptp'], 'String');
            }
            if (data.hasOwnProperty('region')) {
                obj['region'] = ApiClient.convertToType(data['region'], 'String');
            }
            if (data.hasOwnProperty('report_id')) {
                obj['report_id'] = ApiClient.convertToType(data['report_id'], 'String');
            }
            if (data.hasOwnProperty('score')) {
                obj['score'] = ApiClient.convertToType(data['score'], 'Number');
            }
            if (data.hasOwnProperty('scores')) {
                obj['scores'] = ApiClient.convertToType(data['scores'], [Score]);
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], 'String');
            }
            if (data.hasOwnProperty('statuses')) {
                obj['statuses'] = ApiClient.convertToType(data['statuses'], [Status]);
            }
            if (data.hasOwnProperty('summary')) {
                obj['summary'] = Summary.constructFromObject(data['summary']);
            }
            if (data.hasOwnProperty('tax_id')) {
                obj['tax_id'] = ApiClient.convertToType(data['tax_id'], 'String');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
            if (data.hasOwnProperty('update_date')) {
                obj['update_date'] = ApiClient.convertToType(data['update_date'], 'Date');
            }
            if (data.hasOwnProperty('vehicle_id')) {
                obj['vehicle_id'] = ApiClient.convertToType(data['vehicle_id'], 'String');
            }
            if (data.hasOwnProperty('vehicle_summary')) {
                obj['vehicle_summary'] = VehicleSummary.constructFromObject(data['vehicle_summary']);
            }
            if (data.hasOwnProperty('wrong_inputs')) {
                obj['wrong_inputs'] = ApiClient.convertToType(data['wrong_inputs'], [WrongInput]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Check</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Check</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of Check.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['birth_certificate'] && !(typeof data['birth_certificate'] === 'string' || data['birth_certificate'] instanceof String)) {
            throw new Error("Expected the field `birth_certificate` to be a primitive type in the JSON string but got " + data['birth_certificate']);
        }
        // ensure the json data is a string
        if (data['check_id'] && !(typeof data['check_id'] === 'string' || data['check_id'] instanceof String)) {
            throw new Error("Expected the field `check_id` to be a primitive type in the JSON string but got " + data['check_id']);
        }
        // validate the optional field `company_summary`
        if (data['company_summary']) { // data not null
          CompanySummary.validateJSON(data['company_summary']);
        }
        // ensure the json data is a string
        if (data['country'] && !(typeof data['country'] === 'string' || data['country'] instanceof String)) {
            throw new Error("Expected the field `country` to be a primitive type in the JSON string but got " + data['country']);
        }
        // ensure the json data is a string
        if (data['diplomatic_id'] && !(typeof data['diplomatic_id'] === 'string' || data['diplomatic_id'] instanceof String)) {
            throw new Error("Expected the field `diplomatic_id` to be a primitive type in the JSON string but got " + data['diplomatic_id']);
        }
        // ensure the json data is a string
        if (data['driver_license'] && !(typeof data['driver_license'] === 'string' || data['driver_license'] instanceof String)) {
            throw new Error("Expected the field `driver_license` to be a primitive type in the JSON string but got " + data['driver_license']);
        }
        // ensure the json data is a string
        if (data['first_name'] && !(typeof data['first_name'] === 'string' || data['first_name'] instanceof String)) {
            throw new Error("Expected the field `first_name` to be a primitive type in the JSON string but got " + data['first_name']);
        }
        // ensure the json data is a string
        if (data['foreign_id'] && !(typeof data['foreign_id'] === 'string' || data['foreign_id'] instanceof String)) {
            throw new Error("Expected the field `foreign_id` to be a primitive type in the JSON string but got " + data['foreign_id']);
        }
        if (data['homonym_scores']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['homonym_scores'])) {
                throw new Error("Expected the field `homonym_scores` to be an array in the JSON data but got " + data['homonym_scores']);
            }
            // validate the optional field `homonym_scores` (array)
            for (const item of data['homonym_scores']) {
                Score.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['last_name'] && !(typeof data['last_name'] === 'string' || data['last_name'] instanceof String)) {
            throw new Error("Expected the field `last_name` to be a primitive type in the JSON string but got " + data['last_name']);
        }
        // ensure the json data is a string
        if (data['license_plate'] && !(typeof data['license_plate'] === 'string' || data['license_plate'] instanceof String)) {
            throw new Error("Expected the field `license_plate` to be a primitive type in the JSON string but got " + data['license_plate']);
        }
        // ensure the json data is a string
        if (data['national_id'] && !(typeof data['national_id'] === 'string' || data['national_id'] instanceof String)) {
            throw new Error("Expected the field `national_id` to be a primitive type in the JSON string but got " + data['national_id']);
        }
        // ensure the json data is a string
        if (data['native_country'] && !(typeof data['native_country'] === 'string' || data['native_country'] instanceof String)) {
            throw new Error("Expected the field `native_country` to be a primitive type in the JSON string but got " + data['native_country']);
        }
        // ensure the json data is a string
        if (data['owner_document_id'] && !(typeof data['owner_document_id'] === 'string' || data['owner_document_id'] instanceof String)) {
            throw new Error("Expected the field `owner_document_id` to be a primitive type in the JSON string but got " + data['owner_document_id']);
        }
        // ensure the json data is a string
        if (data['owner_document_type'] && !(typeof data['owner_document_type'] === 'string' || data['owner_document_type'] instanceof String)) {
            throw new Error("Expected the field `owner_document_type` to be a primitive type in the JSON string but got " + data['owner_document_type']);
        }
        // ensure the json data is a string
        if (data['passport'] && !(typeof data['passport'] === 'string' || data['passport'] instanceof String)) {
            throw new Error("Expected the field `passport` to be a primitive type in the JSON string but got " + data['passport']);
        }
        // ensure the json data is a string
        if (data['payment_date'] && !(typeof data['payment_date'] === 'string' || data['payment_date'] instanceof String)) {
            throw new Error("Expected the field `payment_date` to be a primitive type in the JSON string but got " + data['payment_date']);
        }
        // ensure the json data is a string
        if (data['pep'] && !(typeof data['pep'] === 'string' || data['pep'] instanceof String)) {
            throw new Error("Expected the field `pep` to be a primitive type in the JSON string but got " + data['pep']);
        }
        // ensure the json data is a string
        if (data['phone_number'] && !(typeof data['phone_number'] === 'string' || data['phone_number'] instanceof String)) {
            throw new Error("Expected the field `phone_number` to be a primitive type in the JSON string but got " + data['phone_number']);
        }
        // ensure the json data is a string
        if (data['professional_card'] && !(typeof data['professional_card'] === 'string' || data['professional_card'] instanceof String)) {
            throw new Error("Expected the field `professional_card` to be a primitive type in the JSON string but got " + data['professional_card']);
        }
        // ensure the json data is a string
        if (data['ptp'] && !(typeof data['ptp'] === 'string' || data['ptp'] instanceof String)) {
            throw new Error("Expected the field `ptp` to be a primitive type in the JSON string but got " + data['ptp']);
        }
        // ensure the json data is a string
        if (data['region'] && !(typeof data['region'] === 'string' || data['region'] instanceof String)) {
            throw new Error("Expected the field `region` to be a primitive type in the JSON string but got " + data['region']);
        }
        // ensure the json data is a string
        if (data['report_id'] && !(typeof data['report_id'] === 'string' || data['report_id'] instanceof String)) {
            throw new Error("Expected the field `report_id` to be a primitive type in the JSON string but got " + data['report_id']);
        }
        if (data['scores']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['scores'])) {
                throw new Error("Expected the field `scores` to be an array in the JSON data but got " + data['scores']);
            }
            // validate the optional field `scores` (array)
            for (const item of data['scores']) {
                Score.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['status'] && !(typeof data['status'] === 'string' || data['status'] instanceof String)) {
            throw new Error("Expected the field `status` to be a primitive type in the JSON string but got " + data['status']);
        }
        if (data['statuses']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['statuses'])) {
                throw new Error("Expected the field `statuses` to be an array in the JSON data but got " + data['statuses']);
            }
            // validate the optional field `statuses` (array)
            for (const item of data['statuses']) {
                Status.validateJSON(item);
            };
        }
        // validate the optional field `summary`
        if (data['summary']) { // data not null
          Summary.validateJSON(data['summary']);
        }
        // ensure the json data is a string
        if (data['tax_id'] && !(typeof data['tax_id'] === 'string' || data['tax_id'] instanceof String)) {
            throw new Error("Expected the field `tax_id` to be a primitive type in the JSON string but got " + data['tax_id']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }
        // ensure the json data is a string
        if (data['vehicle_id'] && !(typeof data['vehicle_id'] === 'string' || data['vehicle_id'] instanceof String)) {
            throw new Error("Expected the field `vehicle_id` to be a primitive type in the JSON string but got " + data['vehicle_id']);
        }
        // validate the optional field `vehicle_summary`
        if (data['vehicle_summary']) { // data not null
          VehicleSummary.validateJSON(data['vehicle_summary']);
        }
        if (data['wrong_inputs']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['wrong_inputs'])) {
                throw new Error("Expected the field `wrong_inputs` to be an array in the JSON data but got " + data['wrong_inputs']);
            }
            // validate the optional field `wrong_inputs` (array)
            for (const item of data['wrong_inputs']) {
                WrongInput.validateJSON(item);
            };
        }

        return true;
    }


}

Check.RequiredProperties = ["check_id", "country", "creation_date", "id_score", "score", "status", "statuses", "summary", "type"];

/**
 * Person birth certificate
 * @member {String} birth_certificate
 */
Check.prototype['birth_certificate'] = undefined;

/**
 * Background check ID
 * @member {String} check_id
 */
Check.prototype['check_id'] = undefined;

/**
 * @member {module:model/CompanySummary} company_summary
 */
Check.prototype['company_summary'] = undefined;

/**
 * ID Document country
 * @member {module:model/Check.CountryEnum} country
 */
Check.prototype['country'] = undefined;

/**
 * Background check creation date
 * @member {Date} creation_date
 */
Check.prototype['creation_date'] = undefined;

/**
 * Person birthdate. Shown only if provided during check creation. YYYY-MM-DD format
 * @member {Date} date_of_birth
 */
Check.prototype['date_of_birth'] = undefined;

/**
 * Person diplomatic id
 * @member {String} diplomatic_id
 */
Check.prototype['diplomatic_id'] = undefined;

/**
 * Person driver's license
 * @member {String} driver_license
 */
Check.prototype['driver_license'] = undefined;

/**
 * Person or entity first name. Shown only if provided during check creation
 * @member {String} first_name
 */
Check.prototype['first_name'] = undefined;

/**
 * Person foreign identification
 * @member {String} foreign_id
 */
Check.prototype['foreign_id'] = undefined;

/**
 * [Experimental] Analyzes the probability that the results by name are attributed to a homonym. Number between 0 and 1 where 1 is the the greatest probability
 * @member {Number} homonym_probability
 */
Check.prototype['homonym_probability'] = undefined;

/**
 * Background check score including results by name only. This might contain homonym information
 * @member {Number} homonym_score
 */
Check.prototype['homonym_score'] = undefined;

/**
 * Background check scores by name for each profile group. [Deprecated for API key V1]
 * @member {Array.<module:model/Score>} homonym_scores
 */
Check.prototype['homonym_scores'] = undefined;

/**
 * Background check score regarding results by ID number only. It is a number between 0 and 1 where 1 is the best score. This result is a weighted average of the id_scores listed under scores.
 * @member {Number} id_score
 */
Check.prototype['id_score'] = undefined;

/**
 * Issue date of the person ID
 * @member {Date} issue_date
 */
Check.prototype['issue_date'] = undefined;

/**
 * Person or entity last name. Shown only if provided during check creation
 * @member {String} last_name
 */
Check.prototype['last_name'] = undefined;

/**
 * Vehicle license plate
 * @member {String} license_plate
 */
Check.prototype['license_plate'] = undefined;

/**
 * Person national identification
 * @member {String} national_id
 */
Check.prototype['national_id'] = undefined;

/**
 * Person origin country
 * @member {module:model/Check.NativeCountryEnum} native_country
 */
Check.prototype['native_country'] = undefined;

/**
 * Vehicle owner identification
 * @member {String} owner_document_id
 */
Check.prototype['owner_document_id'] = undefined;

/**
 * Vehicle owner document type
 * @member {String} owner_document_type
 */
Check.prototype['owner_document_type'] = undefined;

/**
 * Person passport
 * @member {String} passport
 */
Check.prototype['passport'] = undefined;

/**
 * Vehicle license payment date
 * @member {String} payment_date
 */
Check.prototype['payment_date'] = undefined;

/**
 * Colombian PEP idenfitication for Venezuelans
 * @member {String} pep
 */
Check.prototype['pep'] = undefined;

/**
 * Person phone number. Required by law in order to notify the person their background is being checked
 * @member {String} phone_number
 */
Check.prototype['phone_number'] = undefined;

/**
 * Person professional card number
 * @member {String} professional_card
 */
Check.prototype['professional_card'] = undefined;

/**
 * Temporary residence permit of the person
 * @member {String} ptp
 */
Check.prototype['ptp'] = undefined;

/**
 * Region where the background is to be checked. By default, background checks in Brazil are performed in region where the person is from. Applies for some Brazil collectors only. Allowed values are: DF: Distrito Federal, AC: Acre, AL: Alagoas, AP: Amapá, AM: Amazonas, BA: Bahía, CE: Ceará, ES: Espírito Santo, GO: Goiás, MA: Maranhão, MT: Mato Grosso, MS: Mato Grosso do Sul, MG: Minas Gerais, PA: Pará, PB: Paraíba, PR: Paraná, PE: Pernambuco, PI: Piauí, RJ: Río de Janeiro, RN: Río Grande do Norte, RS: Río Grande do Sul, RO: Rondônia, RR: Roraima, SC: Santa Catarina, SP: São Paulo, SE: Sergipe, TO : Tocantins.  
 * @member {module:model/Check.RegionEnum} region
 */
Check.prototype['region'] = undefined;

/**
 * Report ID the background check is associated with
 * @member {String} report_id
 */
Check.prototype['report_id'] = undefined;

/**
 * Background check score. Number between 0 and 1 where 1 is the best score
 * @member {Number} score
 */
Check.prototype['score'] = undefined;

/**
 * Background check score of each profile group and dataset
 * @member {Array.<module:model/Score>} scores
 */
Check.prototype['scores'] = undefined;

/**
 * Result status of the background check. **Not_started** means the background check is still in queue, since there is a limit of background checks that can be processed simultaneously, **completed** means the check finished successfully, **error** means the check failed, **in_progress** means the check is currently being processed, **delayed** means the check is waiting for an additional requirement to be met, this can last up to 3 days. **Completed** and **error** are the two only final statuses
 * @member {module:model/Check.StatusEnum} status
 */
Check.prototype['status'] = undefined;

/**
 * Database status list
 * @member {Array.<module:model/Status>} statuses
 */
Check.prototype['statuses'] = undefined;

/**
 * @member {module:model/Summary} summary
 */
Check.prototype['summary'] = undefined;

/**
 * Person or company tax id
 * @member {String} tax_id
 */
Check.prototype['tax_id'] = undefined;

/**
 * Background check type
 * @member {module:model/Check.TypeEnum} type
 */
Check.prototype['type'] = undefined;

/**
 * Background check update date
 * @member {Date} update_date
 */
Check.prototype['update_date'] = undefined;

/**
 * Vehicle identification
 * @member {String} vehicle_id
 */
Check.prototype['vehicle_id'] = undefined;

/**
 * @member {module:model/VehicleSummary} vehicle_summary
 */
Check.prototype['vehicle_summary'] = undefined;

/**
 * List of parameters entered during background check creation that do not match the information obtained
 * @member {Array.<module:model/WrongInput>} wrong_inputs
 */
Check.prototype['wrong_inputs'] = undefined;





/**
 * Allowed values for the <code>country</code> property.
 * @enum {String}
 * @readonly
 */
Check['CountryEnum'] = {

    /**
     * value: "ALL"
     * @const
     */
    "ALL": "ALL",

    /**
     * value: "BR"
     * @const
     */
    "BR": "BR",

    /**
     * value: "CL"
     * @const
     */
    "CL": "CL",

    /**
     * value: "CO"
     * @const
     */
    "CO": "CO",

    /**
     * value: "CR"
     * @const
     */
    "CR": "CR",

    /**
     * value: "EC"
     * @const
     */
    "EC": "EC",

    /**
     * value: "MX"
     * @const
     */
    "MX": "MX",

    /**
     * value: "PE"
     * @const
     */
    "PE": "PE",

    /**
     * value: "AR"
     * @const
     */
    "AR": "AR"
};


/**
 * Allowed values for the <code>native_country</code> property.
 * @enum {String}
 * @readonly
 */
Check['NativeCountryEnum'] = {

    /**
     * value: "ad"
     * @const
     */
    "ad": "ad",

    /**
     * value: "ae"
     * @const
     */
    "ae": "ae",

    /**
     * value: "af"
     * @const
     */
    "af": "af",

    /**
     * value: "ag"
     * @const
     */
    "ag": "ag",

    /**
     * value: "ai"
     * @const
     */
    "ai": "ai",

    /**
     * value: "al"
     * @const
     */
    "al": "al",

    /**
     * value: "am"
     * @const
     */
    "am": "am",

    /**
     * value: "an"
     * @const
     */
    "an": "an",

    /**
     * value: "ao"
     * @const
     */
    "ao": "ao",

    /**
     * value: "aq"
     * @const
     */
    "aq": "aq",

    /**
     * value: "ar"
     * @const
     */
    "ar": "ar",

    /**
     * value: "as"
     * @const
     */
    "as": "as",

    /**
     * value: "at"
     * @const
     */
    "at": "at",

    /**
     * value: "au"
     * @const
     */
    "au": "au",

    /**
     * value: "aw"
     * @const
     */
    "aw": "aw",

    /**
     * value: "ax"
     * @const
     */
    "ax": "ax",

    /**
     * value: "az"
     * @const
     */
    "az": "az",

    /**
     * value: "ba"
     * @const
     */
    "ba": "ba",

    /**
     * value: "bb"
     * @const
     */
    "bb": "bb",

    /**
     * value: "bd"
     * @const
     */
    "bd": "bd",

    /**
     * value: "be"
     * @const
     */
    "be": "be",

    /**
     * value: "bf"
     * @const
     */
    "bf": "bf",

    /**
     * value: "bg"
     * @const
     */
    "bg": "bg",

    /**
     * value: "bh"
     * @const
     */
    "bh": "bh",

    /**
     * value: "bi"
     * @const
     */
    "bi": "bi",

    /**
     * value: "bj"
     * @const
     */
    "bj": "bj",

    /**
     * value: "bm"
     * @const
     */
    "bm": "bm",

    /**
     * value: "bn"
     * @const
     */
    "bn": "bn",

    /**
     * value: "bo"
     * @const
     */
    "bo": "bo",

    /**
     * value: "br"
     * @const
     */
    "br": "br",

    /**
     * value: "bs"
     * @const
     */
    "bs": "bs",

    /**
     * value: "bt"
     * @const
     */
    "bt": "bt",

    /**
     * value: "bv"
     * @const
     */
    "bv": "bv",

    /**
     * value: "bw"
     * @const
     */
    "bw": "bw",

    /**
     * value: "by"
     * @const
     */
    "by": "by",

    /**
     * value: "bz"
     * @const
     */
    "bz": "bz",

    /**
     * value: "ca"
     * @const
     */
    "ca": "ca",

    /**
     * value: "cc"
     * @const
     */
    "cc": "cc",

    /**
     * value: "cd"
     * @const
     */
    "cd": "cd",

    /**
     * value: "cf"
     * @const
     */
    "cf": "cf",

    /**
     * value: "cg"
     * @const
     */
    "cg": "cg",

    /**
     * value: "ch"
     * @const
     */
    "ch": "ch",

    /**
     * value: "ci"
     * @const
     */
    "ci": "ci",

    /**
     * value: "ck"
     * @const
     */
    "ck": "ck",

    /**
     * value: "cl"
     * @const
     */
    "cl": "cl",

    /**
     * value: "cm"
     * @const
     */
    "cm": "cm",

    /**
     * value: "cn"
     * @const
     */
    "cn": "cn",

    /**
     * value: "co"
     * @const
     */
    "co": "co",

    /**
     * value: "cr"
     * @const
     */
    "cr": "cr",

    /**
     * value: "cu"
     * @const
     */
    "cu": "cu",

    /**
     * value: "cv"
     * @const
     */
    "cv": "cv",

    /**
     * value: "cx"
     * @const
     */
    "cx": "cx",

    /**
     * value: "cy"
     * @const
     */
    "cy": "cy",

    /**
     * value: "cz"
     * @const
     */
    "cz": "cz",

    /**
     * value: "de"
     * @const
     */
    "de": "de",

    /**
     * value: "dj"
     * @const
     */
    "dj": "dj",

    /**
     * value: "dk"
     * @const
     */
    "dk": "dk",

    /**
     * value: "dm"
     * @const
     */
    "dm": "dm",

    /**
     * value: "do"
     * @const
     */
    "do": "do",

    /**
     * value: "dz"
     * @const
     */
    "dz": "dz",

    /**
     * value: "ea"
     * @const
     */
    "ea": "ea",

    /**
     * value: "ec"
     * @const
     */
    "ec": "ec",

    /**
     * value: "ee"
     * @const
     */
    "ee": "ee",

    /**
     * value: "eg"
     * @const
     */
    "eg": "eg",

    /**
     * value: "eh"
     * @const
     */
    "eh": "eh",

    /**
     * value: "er"
     * @const
     */
    "er": "er",

    /**
     * value: "es"
     * @const
     */
    "es": "es",

    /**
     * value: "et"
     * @const
     */
    "et": "et",

    /**
     * value: "fi"
     * @const
     */
    "fi": "fi",

    /**
     * value: "fj"
     * @const
     */
    "fj": "fj",

    /**
     * value: "fk"
     * @const
     */
    "fk": "fk",

    /**
     * value: "fm"
     * @const
     */
    "fm": "fm",

    /**
     * value: "fo"
     * @const
     */
    "fo": "fo",

    /**
     * value: "fr"
     * @const
     */
    "fr": "fr",

    /**
     * value: "ga"
     * @const
     */
    "ga": "ga",

    /**
     * value: "gb"
     * @const
     */
    "gb": "gb",

    /**
     * value: "gd"
     * @const
     */
    "gd": "gd",

    /**
     * value: "ge"
     * @const
     */
    "ge": "ge",

    /**
     * value: "gf"
     * @const
     */
    "gf": "gf",

    /**
     * value: "gg"
     * @const
     */
    "gg": "gg",

    /**
     * value: "gh"
     * @const
     */
    "gh": "gh",

    /**
     * value: "gi"
     * @const
     */
    "gi": "gi",

    /**
     * value: "gl"
     * @const
     */
    "gl": "gl",

    /**
     * value: "gm"
     * @const
     */
    "gm": "gm",

    /**
     * value: "gn"
     * @const
     */
    "gn": "gn",

    /**
     * value: "gp"
     * @const
     */
    "gp": "gp",

    /**
     * value: "gq"
     * @const
     */
    "gq": "gq",

    /**
     * value: "gr"
     * @const
     */
    "gr": "gr",

    /**
     * value: "gs"
     * @const
     */
    "gs": "gs",

    /**
     * value: "gt"
     * @const
     */
    "gt": "gt",

    /**
     * value: "gu"
     * @const
     */
    "gu": "gu",

    /**
     * value: "gw"
     * @const
     */
    "gw": "gw",

    /**
     * value: "gy"
     * @const
     */
    "gy": "gy",

    /**
     * value: "hk"
     * @const
     */
    "hk": "hk",

    /**
     * value: "hm"
     * @const
     */
    "hm": "hm",

    /**
     * value: "hn"
     * @const
     */
    "hn": "hn",

    /**
     * value: "hr"
     * @const
     */
    "hr": "hr",

    /**
     * value: "ht"
     * @const
     */
    "ht": "ht",

    /**
     * value: "hu"
     * @const
     */
    "hu": "hu",

    /**
     * value: "id"
     * @const
     */
    "id": "id",

    /**
     * value: "ie"
     * @const
     */
    "ie": "ie",

    /**
     * value: "il"
     * @const
     */
    "il": "il",

    /**
     * value: "im"
     * @const
     */
    "im": "im",

    /**
     * value: "in"
     * @const
     */
    "in": "in",

    /**
     * value: "io"
     * @const
     */
    "io": "io",

    /**
     * value: "iq"
     * @const
     */
    "iq": "iq",

    /**
     * value: "ir"
     * @const
     */
    "ir": "ir",

    /**
     * value: "is"
     * @const
     */
    "is": "is",

    /**
     * value: "it"
     * @const
     */
    "it": "it",

    /**
     * value: "je"
     * @const
     */
    "je": "je",

    /**
     * value: "jm"
     * @const
     */
    "jm": "jm",

    /**
     * value: "jo"
     * @const
     */
    "jo": "jo",

    /**
     * value: "jp"
     * @const
     */
    "jp": "jp",

    /**
     * value: "ke"
     * @const
     */
    "ke": "ke",

    /**
     * value: "kg"
     * @const
     */
    "kg": "kg",

    /**
     * value: "kh"
     * @const
     */
    "kh": "kh",

    /**
     * value: "ki"
     * @const
     */
    "ki": "ki",

    /**
     * value: "km"
     * @const
     */
    "km": "km",

    /**
     * value: "kn"
     * @const
     */
    "kn": "kn",

    /**
     * value: "kp"
     * @const
     */
    "kp": "kp",

    /**
     * value: "kr"
     * @const
     */
    "kr": "kr",

    /**
     * value: "kw"
     * @const
     */
    "kw": "kw",

    /**
     * value: "ky"
     * @const
     */
    "ky": "ky",

    /**
     * value: "kz"
     * @const
     */
    "kz": "kz",

    /**
     * value: "la"
     * @const
     */
    "la": "la",

    /**
     * value: "lb"
     * @const
     */
    "lb": "lb",

    /**
     * value: "lc"
     * @const
     */
    "lc": "lc",

    /**
     * value: "li"
     * @const
     */
    "li": "li",

    /**
     * value: "lk"
     * @const
     */
    "lk": "lk",

    /**
     * value: "lr"
     * @const
     */
    "lr": "lr",

    /**
     * value: "ls"
     * @const
     */
    "ls": "ls",

    /**
     * value: "lt"
     * @const
     */
    "lt": "lt",

    /**
     * value: "lu"
     * @const
     */
    "lu": "lu",

    /**
     * value: "lv"
     * @const
     */
    "lv": "lv",

    /**
     * value: "ly"
     * @const
     */
    "ly": "ly",

    /**
     * value: "ma"
     * @const
     */
    "ma": "ma",

    /**
     * value: "mc"
     * @const
     */
    "mc": "mc",

    /**
     * value: "md"
     * @const
     */
    "md": "md",

    /**
     * value: "me"
     * @const
     */
    "me": "me",

    /**
     * value: "mg"
     * @const
     */
    "mg": "mg",

    /**
     * value: "mh"
     * @const
     */
    "mh": "mh",

    /**
     * value: "mk"
     * @const
     */
    "mk": "mk",

    /**
     * value: "ml"
     * @const
     */
    "ml": "ml",

    /**
     * value: "mm"
     * @const
     */
    "mm": "mm",

    /**
     * value: "mn"
     * @const
     */
    "mn": "mn",

    /**
     * value: "mo"
     * @const
     */
    "mo": "mo",

    /**
     * value: "mp"
     * @const
     */
    "mp": "mp",

    /**
     * value: "mq"
     * @const
     */
    "mq": "mq",

    /**
     * value: "mr"
     * @const
     */
    "mr": "mr",

    /**
     * value: "ms"
     * @const
     */
    "ms": "ms",

    /**
     * value: "mt"
     * @const
     */
    "mt": "mt",

    /**
     * value: "mu"
     * @const
     */
    "mu": "mu",

    /**
     * value: "mv"
     * @const
     */
    "mv": "mv",

    /**
     * value: "mw"
     * @const
     */
    "mw": "mw",

    /**
     * value: "mx"
     * @const
     */
    "mx": "mx",

    /**
     * value: "my"
     * @const
     */
    "my": "my",

    /**
     * value: "mz"
     * @const
     */
    "mz": "mz",

    /**
     * value: "na"
     * @const
     */
    "na": "na",

    /**
     * value: "nc"
     * @const
     */
    "nc": "nc",

    /**
     * value: "ne"
     * @const
     */
    "ne": "ne",

    /**
     * value: "nf"
     * @const
     */
    "nf": "nf",

    /**
     * value: "ng"
     * @const
     */
    "ng": "ng",

    /**
     * value: "ni"
     * @const
     */
    "ni": "ni",

    /**
     * value: "nl"
     * @const
     */
    "nl": "nl",

    /**
     * value: "false"
     * @const
     */
    "false": "false",

    /**
     * value: "np"
     * @const
     */
    "np": "np",

    /**
     * value: "nr"
     * @const
     */
    "nr": "nr",

    /**
     * value: "nu"
     * @const
     */
    "nu": "nu",

    /**
     * value: "nz"
     * @const
     */
    "nz": "nz",

    /**
     * value: "om"
     * @const
     */
    "om": "om",

    /**
     * value: "pa"
     * @const
     */
    "pa": "pa",

    /**
     * value: "pe"
     * @const
     */
    "pe": "pe",

    /**
     * value: "pf"
     * @const
     */
    "pf": "pf",

    /**
     * value: "pg"
     * @const
     */
    "pg": "pg",

    /**
     * value: "ph"
     * @const
     */
    "ph": "ph",

    /**
     * value: "pk"
     * @const
     */
    "pk": "pk",

    /**
     * value: "pl"
     * @const
     */
    "pl": "pl",

    /**
     * value: "pm"
     * @const
     */
    "pm": "pm",

    /**
     * value: "pn"
     * @const
     */
    "pn": "pn",

    /**
     * value: "pr"
     * @const
     */
    "pr": "pr",

    /**
     * value: "ps"
     * @const
     */
    "ps": "ps",

    /**
     * value: "pt"
     * @const
     */
    "pt": "pt",

    /**
     * value: "pw"
     * @const
     */
    "pw": "pw",

    /**
     * value: "py"
     * @const
     */
    "py": "py",

    /**
     * value: "qa"
     * @const
     */
    "qa": "qa",

    /**
     * value: "re"
     * @const
     */
    "re": "re",

    /**
     * value: "ro"
     * @const
     */
    "ro": "ro",

    /**
     * value: "rs"
     * @const
     */
    "rs": "rs",

    /**
     * value: "ru"
     * @const
     */
    "ru": "ru",

    /**
     * value: "rw"
     * @const
     */
    "rw": "rw",

    /**
     * value: "sa"
     * @const
     */
    "sa": "sa",

    /**
     * value: "sb"
     * @const
     */
    "sb": "sb",

    /**
     * value: "sc"
     * @const
     */
    "sc": "sc",

    /**
     * value: "sd"
     * @const
     */
    "sd": "sd",

    /**
     * value: "se"
     * @const
     */
    "se": "se",

    /**
     * value: "sg"
     * @const
     */
    "sg": "sg",

    /**
     * value: "sh"
     * @const
     */
    "sh": "sh",

    /**
     * value: "si"
     * @const
     */
    "si": "si",

    /**
     * value: "sj"
     * @const
     */
    "sj": "sj",

    /**
     * value: "sk"
     * @const
     */
    "sk": "sk",

    /**
     * value: "sl"
     * @const
     */
    "sl": "sl",

    /**
     * value: "sm"
     * @const
     */
    "sm": "sm",

    /**
     * value: "sn"
     * @const
     */
    "sn": "sn",

    /**
     * value: "so"
     * @const
     */
    "so": "so",

    /**
     * value: "sr"
     * @const
     */
    "sr": "sr",

    /**
     * value: "st"
     * @const
     */
    "st": "st",

    /**
     * value: "sv"
     * @const
     */
    "sv": "sv",

    /**
     * value: "sy"
     * @const
     */
    "sy": "sy",

    /**
     * value: "sz"
     * @const
     */
    "sz": "sz",

    /**
     * value: "tc"
     * @const
     */
    "tc": "tc",

    /**
     * value: "td"
     * @const
     */
    "td": "td",

    /**
     * value: "tf"
     * @const
     */
    "tf": "tf",

    /**
     * value: "tg"
     * @const
     */
    "tg": "tg",

    /**
     * value: "th"
     * @const
     */
    "th": "th",

    /**
     * value: "tj"
     * @const
     */
    "tj": "tj",

    /**
     * value: "tk"
     * @const
     */
    "tk": "tk",

    /**
     * value: "tl"
     * @const
     */
    "tl": "tl",

    /**
     * value: "tm"
     * @const
     */
    "tm": "tm",

    /**
     * value: "tn"
     * @const
     */
    "tn": "tn",

    /**
     * value: "to"
     * @const
     */
    "to": "to",

    /**
     * value: "tr"
     * @const
     */
    "tr": "tr",

    /**
     * value: "tt"
     * @const
     */
    "tt": "tt",

    /**
     * value: "tv"
     * @const
     */
    "tv": "tv",

    /**
     * value: "tw"
     * @const
     */
    "tw": "tw",

    /**
     * value: "tz"
     * @const
     */
    "tz": "tz",

    /**
     * value: "ua"
     * @const
     */
    "ua": "ua",

    /**
     * value: "ug"
     * @const
     */
    "ug": "ug",

    /**
     * value: "um"
     * @const
     */
    "um": "um",

    /**
     * value: "us"
     * @const
     */
    "us": "us",

    /**
     * value: "uy"
     * @const
     */
    "uy": "uy",

    /**
     * value: "uz"
     * @const
     */
    "uz": "uz",

    /**
     * value: "va"
     * @const
     */
    "va": "va",

    /**
     * value: "vc"
     * @const
     */
    "vc": "vc",

    /**
     * value: "ve"
     * @const
     */
    "ve": "ve",

    /**
     * value: "vg"
     * @const
     */
    "vg": "vg",

    /**
     * value: "vi"
     * @const
     */
    "vi": "vi",

    /**
     * value: "vn"
     * @const
     */
    "vn": "vn",

    /**
     * value: "vu"
     * @const
     */
    "vu": "vu",

    /**
     * value: "wf"
     * @const
     */
    "wf": "wf",

    /**
     * value: "ws"
     * @const
     */
    "ws": "ws",

    /**
     * value: "ye"
     * @const
     */
    "ye": "ye",

    /**
     * value: "yt"
     * @const
     */
    "yt": "yt",

    /**
     * value: "za"
     * @const
     */
    "za": "za",

    /**
     * value: "zm"
     * @const
     */
    "zm": "zm",

    /**
     * value: "zw"
     * @const
     */
    "zw": "zw"
};


/**
 * Allowed values for the <code>region</code> property.
 * @enum {String}
 * @readonly
 */
Check['RegionEnum'] = {

    /**
     * value: "DF"
     * @const
     */
    "DF": "DF",

    /**
     * value: "AC"
     * @const
     */
    "AC": "AC",

    /**
     * value: "AL"
     * @const
     */
    "AL": "AL",

    /**
     * value: "AP"
     * @const
     */
    "AP": "AP",

    /**
     * value: "AM"
     * @const
     */
    "AM": "AM",

    /**
     * value: "BA"
     * @const
     */
    "BA": "BA",

    /**
     * value: "CE"
     * @const
     */
    "CE": "CE",

    /**
     * value: "ES"
     * @const
     */
    "ES": "ES",

    /**
     * value: "GO"
     * @const
     */
    "GO": "GO",

    /**
     * value: "MA"
     * @const
     */
    "MA": "MA",

    /**
     * value: "MT"
     * @const
     */
    "MT": "MT",

    /**
     * value: "MS"
     * @const
     */
    "MS": "MS",

    /**
     * value: "MG"
     * @const
     */
    "MG": "MG",

    /**
     * value: "PA"
     * @const
     */
    "PA": "PA",

    /**
     * value: "PB"
     * @const
     */
    "PB": "PB",

    /**
     * value: "PR"
     * @const
     */
    "PR": "PR",

    /**
     * value: "PE"
     * @const
     */
    "PE": "PE",

    /**
     * value: "PI"
     * @const
     */
    "PI": "PI",

    /**
     * value: "RJ"
     * @const
     */
    "RJ": "RJ",

    /**
     * value: "RN"
     * @const
     */
    "RN": "RN",

    /**
     * value: "RS"
     * @const
     */
    "RS": "RS",

    /**
     * value: "RO"
     * @const
     */
    "RO": "RO",

    /**
     * value: "RR"
     * @const
     */
    "RR": "RR",

    /**
     * value: "SC"
     * @const
     */
    "SC": "SC",

    /**
     * value: "SP"
     * @const
     */
    "SP": "SP",

    /**
     * value: "SE"
     * @const
     */
    "SE": "SE",

    /**
     * value: "TO"
     * @const
     */
    "TO": "TO"
};


/**
 * Allowed values for the <code>status</code> property.
 * @enum {String}
 * @readonly
 */
Check['StatusEnum'] = {

    /**
     * value: "not_started"
     * @const
     */
    "not_started": "not_started",

    /**
     * value: "in_progress"
     * @const
     */
    "in_progress": "in_progress",

    /**
     * value: "completed"
     * @const
     */
    "completed": "completed",

    /**
     * value: "error"
     * @const
     */
    "error": "error",

    /**
     * value: "delayed"
     * @const
     */
    "delayed": "delayed"
};


/**
 * Allowed values for the <code>type</code> property.
 * @enum {String}
 * @readonly
 */
Check['TypeEnum'] = {

    /**
     * value: "company"
     * @const
     */
    "company": "company",

    /**
     * value: "person"
     * @const
     */
    "person": "person",

    /**
     * value: "vehicle"
     * @const
     */
    "vehicle": "vehicle"
};



export default Check;

