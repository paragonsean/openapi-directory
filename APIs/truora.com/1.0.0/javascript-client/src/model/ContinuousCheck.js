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
import Check from './Check';
import ContinuousCheckEntry from './ContinuousCheckEntry';

/**
 * The ContinuousCheck model module.
 * @module model/ContinuousCheck
 * @version 1.0.0
 */
class ContinuousCheck {
    /**
     * Constructs a new <code>ContinuousCheck</code>.
     * Continuous check allows for background checks to be performed on the same people or vehicles periodically and notifies if new information is found. Allowing companies to keep an eye on their workforce or vehicle fleet for any recent wrongdoing they might be involved in.
     * @alias module:model/ContinuousCheck
     * @param continuousCheckStatus {module:model/ContinuousCheck.ContinuousCheckStatusEnum} Shows whether the background check score rose, fell, stood the same or was just created
     * @param frequency {String} Time between background checks. It can be daily, weekly, monthly, yearly or have a custom frequency written as a number accompanied by d: day, w: week, m: month, y: year for instance: 3d: every three days, 2w: every two weeks
     * @param lastCheckID {String} Last check ID
     */
    constructor(continuousCheckStatus, frequency, lastCheckID) { 
        
        ContinuousCheck.initialize(this, continuousCheckStatus, frequency, lastCheckID);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, continuousCheckStatus, frequency, lastCheckID) { 
        obj['ContinuousCheckStatus'] = continuousCheckStatus;
        obj['Frequency'] = frequency;
        obj['LastCheckID'] = lastCheckID;
    }

    /**
     * Constructs a <code>ContinuousCheck</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ContinuousCheck} obj Optional instance to populate.
     * @return {module:model/ContinuousCheck} The populated <code>ContinuousCheck</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ContinuousCheck();

            if (data.hasOwnProperty('ContinuousCheckID')) {
                obj['ContinuousCheckID'] = ApiClient.convertToType(data['ContinuousCheckID'], 'String');
            }
            if (data.hasOwnProperty('ContinuousCheckStatus')) {
                obj['ContinuousCheckStatus'] = ApiClient.convertToType(data['ContinuousCheckStatus'], 'String');
            }
            if (data.hasOwnProperty('CreationDate')) {
                obj['CreationDate'] = ApiClient.convertToType(data['CreationDate'], 'Date');
            }
            if (data.hasOwnProperty('Enabled')) {
                obj['Enabled'] = ApiClient.convertToType(data['Enabled'], 'Boolean');
            }
            if (data.hasOwnProperty('Frequency')) {
                obj['Frequency'] = ApiClient.convertToType(data['Frequency'], 'String');
            }
            if (data.hasOwnProperty('History')) {
                obj['History'] = ContinuousCheckEntry.constructFromObject(data['History']);
            }
            if (data.hasOwnProperty('LastCheckID')) {
                obj['LastCheckID'] = ApiClient.convertToType(data['LastCheckID'], 'String');
            }
            if (data.hasOwnProperty('NextRunDate')) {
                obj['NextRunDate'] = ApiClient.convertToType(data['NextRunDate'], 'Date');
            }
            if (data.hasOwnProperty('OriginalCheck')) {
                obj['OriginalCheck'] = Check.constructFromObject(data['OriginalCheck']);
            }
            if (data.hasOwnProperty('UpdateDate')) {
                obj['UpdateDate'] = ApiClient.convertToType(data['UpdateDate'], 'Date');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ContinuousCheck</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ContinuousCheck</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of ContinuousCheck.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['ContinuousCheckID'] && !(typeof data['ContinuousCheckID'] === 'string' || data['ContinuousCheckID'] instanceof String)) {
            throw new Error("Expected the field `ContinuousCheckID` to be a primitive type in the JSON string but got " + data['ContinuousCheckID']);
        }
        // ensure the json data is a string
        if (data['ContinuousCheckStatus'] && !(typeof data['ContinuousCheckStatus'] === 'string' || data['ContinuousCheckStatus'] instanceof String)) {
            throw new Error("Expected the field `ContinuousCheckStatus` to be a primitive type in the JSON string but got " + data['ContinuousCheckStatus']);
        }
        // ensure the json data is a string
        if (data['Frequency'] && !(typeof data['Frequency'] === 'string' || data['Frequency'] instanceof String)) {
            throw new Error("Expected the field `Frequency` to be a primitive type in the JSON string but got " + data['Frequency']);
        }
        // validate the optional field `History`
        if (data['History']) { // data not null
          ContinuousCheckEntry.validateJSON(data['History']);
        }
        // ensure the json data is a string
        if (data['LastCheckID'] && !(typeof data['LastCheckID'] === 'string' || data['LastCheckID'] instanceof String)) {
            throw new Error("Expected the field `LastCheckID` to be a primitive type in the JSON string but got " + data['LastCheckID']);
        }
        // validate the optional field `OriginalCheck`
        if (data['OriginalCheck']) { // data not null
          Check.validateJSON(data['OriginalCheck']);
        }

        return true;
    }


}

ContinuousCheck.RequiredProperties = ["ContinuousCheckStatus", "Frequency", "LastCheckID"];

/**
 * Continuous check ID [partition key and sort key]
 * @member {String} ContinuousCheckID
 */
ContinuousCheck.prototype['ContinuousCheckID'] = undefined;

/**
 * Shows whether the background check score rose, fell, stood the same or was just created
 * @member {module:model/ContinuousCheck.ContinuousCheckStatusEnum} ContinuousCheckStatus
 */
ContinuousCheck.prototype['ContinuousCheckStatus'] = undefined;

/**
 * Continuous check creation date in RFC3339 format
 * @member {Date} CreationDate
 */
ContinuousCheck.prototype['CreationDate'] = undefined;

/**
 * Indicates whether continuous check is enabled
 * @member {Boolean} Enabled
 */
ContinuousCheck.prototype['Enabled'] = undefined;

/**
 * Time between background checks. It can be daily, weekly, monthly, yearly or have a custom frequency written as a number accompanied by d: day, w: week, m: month, y: year for instance: 3d: every three days, 2w: every two weeks
 * @member {String} Frequency
 */
ContinuousCheck.prototype['Frequency'] = undefined;

/**
 * @member {module:model/ContinuousCheckEntry} History
 */
ContinuousCheck.prototype['History'] = undefined;

/**
 * Last check ID
 * @member {String} LastCheckID
 */
ContinuousCheck.prototype['LastCheckID'] = undefined;

/**
 * Next background check date, in RFC3339 format (without time)
 * @member {Date} NextRunDate
 */
ContinuousCheck.prototype['NextRunDate'] = undefined;

/**
 * @member {module:model/Check} OriginalCheck
 */
ContinuousCheck.prototype['OriginalCheck'] = undefined;

/**
 * Continuous check update date in RFC3339 format
 * @member {Date} UpdateDate
 */
ContinuousCheck.prototype['UpdateDate'] = undefined;





/**
 * Allowed values for the <code>ContinuousCheckStatus</code> property.
 * @enum {String}
 * @readonly
 */
ContinuousCheck['ContinuousCheckStatusEnum'] = {

    /**
     * value: "new"
     * @const
     */
    "new": "new",

    /**
     * value: "up"
     * @const
     */
    "up": "up",

    /**
     * value: "down"
     * @const
     */
    "down": "down",

    /**
     * value: "same"
     * @const
     */
    "same": "same"
};



export default ContinuousCheck;

