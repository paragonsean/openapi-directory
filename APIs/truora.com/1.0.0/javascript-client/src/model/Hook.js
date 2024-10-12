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
 * The Hook model module.
 * @module model/Hook
 * @version 1.0.0
 */
class Hook {
    /**
     * Constructs a new <code>Hook</code>.
     * Represents a hook configuration
     * @alias module:model/Hook
     */
    constructor() { 
        
        Hook.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Hook</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Hook} obj Optional instance to populate.
     * @return {module:model/Hook} The populated <code>Hook</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Hook();

            if (data.hasOwnProperty('actions')) {
                obj['actions'] = ApiClient.convertToType(data['actions'], ['String']);
            }
            if (data.hasOwnProperty('event_type')) {
                obj['event_type'] = ApiClient.convertToType(data['event_type'], 'String');
            }
            if (data.hasOwnProperty('signing_key')) {
                obj['signing_key'] = ApiClient.convertToType(data['signing_key'], 'String');
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], 'String');
            }
            if (data.hasOwnProperty('subscriber_type')) {
                obj['subscriber_type'] = ApiClient.convertToType(data['subscriber_type'], 'String');
            }
            if (data.hasOwnProperty('subscriber_url')) {
                obj['subscriber_url'] = ApiClient.convertToType(data['subscriber_url'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Hook</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Hook</code>.
     */
    static validateJSON(data) {
        // ensure the json data is an array
        if (!Array.isArray(data['actions'])) {
            throw new Error("Expected the field `actions` to be an array in the JSON data but got " + data['actions']);
        }
        // ensure the json data is a string
        if (data['event_type'] && !(typeof data['event_type'] === 'string' || data['event_type'] instanceof String)) {
            throw new Error("Expected the field `event_type` to be a primitive type in the JSON string but got " + data['event_type']);
        }
        // ensure the json data is a string
        if (data['signing_key'] && !(typeof data['signing_key'] === 'string' || data['signing_key'] instanceof String)) {
            throw new Error("Expected the field `signing_key` to be a primitive type in the JSON string but got " + data['signing_key']);
        }
        // ensure the json data is a string
        if (data['status'] && !(typeof data['status'] === 'string' || data['status'] instanceof String)) {
            throw new Error("Expected the field `status` to be a primitive type in the JSON string but got " + data['status']);
        }
        // ensure the json data is a string
        if (data['subscriber_type'] && !(typeof data['subscriber_type'] === 'string' || data['subscriber_type'] instanceof String)) {
            throw new Error("Expected the field `subscriber_type` to be a primitive type in the JSON string but got " + data['subscriber_type']);
        }
        // ensure the json data is a string
        if (data['subscriber_url'] && !(typeof data['subscriber_url'] === 'string' || data['subscriber_url'] instanceof String)) {
            throw new Error("Expected the field `subscriber_url` to be a primitive type in the JSON string but got " + data['subscriber_url']);
        }

        return true;
    }


}



/**
 * Actions you want to be notified. Possible inputs are created, started, and finished or any combination of those three
 * @member {Array.<String>} actions
 */
Hook.prototype['actions'] = undefined;

/**
 * Entity events you want to be notified. If all is selected, there is no need to enter actions
 * @member {module:model/Hook.EventTypeEnum} event_type
 */
Hook.prototype['event_type'] = undefined;

/**
 * Secret random hexadecimal key used to sign the event and confirm its legitimacy. Signing keys are used to decode the JWT you get as payload from events
 * @member {String} signing_key
 */
Hook.prototype['signing_key'] = undefined;

/**
 * indicates whether the hook is active or not. enabled by default
 * @member {module:model/Hook.StatusEnum} status
 */
Hook.prototype['status'] = undefined;

/**
 * Platform with an endpoint ready to process the information. Only web is supported currently
 * @member {String} subscriber_type
 */
Hook.prototype['subscriber_type'] = undefined;

/**
 * Link where notification requests will be sent, required when subscriber_type is web
 * @member {String} subscriber_url
 */
Hook.prototype['subscriber_url'] = undefined;





/**
 * Allowed values for the <code>event_type</code> property.
 * @enum {String}
 * @readonly
 */
Hook['EventTypeEnum'] = {

    /**
     * value: "all"
     * @const
     */
    "all": "all",

    /**
     * value: "check"
     * @const
     */
    "check": "check"
};


/**
 * Allowed values for the <code>status</code> property.
 * @enum {String}
 * @readonly
 */
Hook['StatusEnum'] = {

    /**
     * value: "enabled"
     * @const
     */
    "enabled": "enabled",

    /**
     * value: "disabled"
     * @const
     */
    "disabled": "disabled"
};



export default Hook;

