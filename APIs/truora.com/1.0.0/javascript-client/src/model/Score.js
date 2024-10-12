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
import ScoreDetail from './ScoreDetail';

/**
 * The Score model module.
 * @module model/Score
 * @version 1.0.0
 */
class Score {
    /**
     * Constructs a new <code>Score</code>.
     * Represents dataset scores. A score is a number between 0 and 1 that indicates how trustworthy the person, vehicle, or company is accordig to the result of the background check. Severity represents the risk associated with each dataset according to the background check. Keep in mind that you should use either the score or the severity but not both
     * @alias module:model/Score
     * @param byId {module:model/ScoreDetail} 
     * @param byName {module:model/ScoreDetail} 
     * @param dataSet {module:model/Score.DataSetEnum} Dataset summed up to create the score
     * @param score {Number} Dataset score. Number between 0 and 1 where 1 is the best score.
     * @param severity {module:model/Score.SeverityEnum} Risk asociated with each category for the search according to the information found. None is returned when the person, vehicle or company is in the clear. Unknown is returned when the score is none due to a problem with one of the searches
     */
    constructor(byId, byName, dataSet, score, severity) { 
        
        Score.initialize(this, byId, byName, dataSet, score, severity);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, byId, byName, dataSet, score, severity) { 
        obj['by_id'] = byId;
        obj['by_name'] = byName;
        obj['data_set'] = dataSet;
        obj['score'] = score;
        obj['severity'] = severity;
    }

    /**
     * Constructs a <code>Score</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Score} obj Optional instance to populate.
     * @return {module:model/Score} The populated <code>Score</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Score();

            if (data.hasOwnProperty('by_id')) {
                obj['by_id'] = ScoreDetail.constructFromObject(data['by_id']);
            }
            if (data.hasOwnProperty('by_name')) {
                obj['by_name'] = ScoreDetail.constructFromObject(data['by_name']);
            }
            if (data.hasOwnProperty('data_set')) {
                obj['data_set'] = ApiClient.convertToType(data['data_set'], 'String');
            }
            if (data.hasOwnProperty('result')) {
                obj['result'] = ApiClient.convertToType(data['result'], 'String');
            }
            if (data.hasOwnProperty('score')) {
                obj['score'] = ApiClient.convertToType(data['score'], 'Number');
            }
            if (data.hasOwnProperty('severity')) {
                obj['severity'] = ApiClient.convertToType(data['severity'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Score</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Score</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of Score.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `by_id`
        if (data['by_id']) { // data not null
          ScoreDetail.validateJSON(data['by_id']);
        }
        // validate the optional field `by_name`
        if (data['by_name']) { // data not null
          ScoreDetail.validateJSON(data['by_name']);
        }
        // ensure the json data is a string
        if (data['data_set'] && !(typeof data['data_set'] === 'string' || data['data_set'] instanceof String)) {
            throw new Error("Expected the field `data_set` to be a primitive type in the JSON string but got " + data['data_set']);
        }
        // ensure the json data is a string
        if (data['result'] && !(typeof data['result'] === 'string' || data['result'] instanceof String)) {
            throw new Error("Expected the field `result` to be a primitive type in the JSON string but got " + data['result']);
        }
        // ensure the json data is a string
        if (data['severity'] && !(typeof data['severity'] === 'string' || data['severity'] instanceof String)) {
            throw new Error("Expected the field `severity` to be a primitive type in the JSON string but got " + data['severity']);
        }

        return true;
    }


}

Score.RequiredProperties = ["by_id", "by_name", "data_set", "score", "severity"];

/**
 * @member {module:model/ScoreDetail} by_id
 */
Score.prototype['by_id'] = undefined;

/**
 * @member {module:model/ScoreDetail} by_name
 */
Score.prototype['by_name'] = undefined;

/**
 * Dataset summed up to create the score
 * @member {module:model/Score.DataSetEnum} data_set
 */
Score.prototype['data_set'] = undefined;

/**
 * Overall result of the data collected. If at least one collected data status is found, the result will be found, otherwise, it will be the most frecuent status
 * @member {module:model/Score.ResultEnum} result
 */
Score.prototype['result'] = undefined;

/**
 * Dataset score. Number between 0 and 1 where 1 is the best score.
 * @member {Number} score
 */
Score.prototype['score'] = undefined;

/**
 * Risk asociated with each category for the search according to the information found. None is returned when the person, vehicle or company is in the clear. Unknown is returned when the score is none due to a problem with one of the searches
 * @member {module:model/Score.SeverityEnum} severity
 */
Score.prototype['severity'] = undefined;





/**
 * Allowed values for the <code>data_set</code> property.
 * @enum {String}
 * @readonly
 */
Score['DataSetEnum'] = {

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
 * Allowed values for the <code>result</code> property.
 * @enum {String}
 * @readonly
 */
Score['ResultEnum'] = {

    /**
     * value: "pending"
     * @const
     */
    "pending": "pending",

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
     * value: "ignored"
     * @const
     */
    "ignored": "ignored"
};


/**
 * Allowed values for the <code>severity</code> property.
 * @enum {String}
 * @readonly
 */
Score['SeverityEnum'] = {

    /**
     * value: "unknown"
     * @const
     */
    "unknown": "unknown",

    /**
     * value: "none"
     * @const
     */
    "none": "none",

    /**
     * value: "very_low"
     * @const
     */
    "very_low": "very_low",

    /**
     * value: "low"
     * @const
     */
    "low": "low",

    /**
     * value: "medium"
     * @const
     */
    "medium": "medium",

    /**
     * value: "high"
     * @const
     */
    "high": "high",

    /**
     * value: "very_high"
     * @const
     */
    "very_high": "very_high"
};



export default Score;

