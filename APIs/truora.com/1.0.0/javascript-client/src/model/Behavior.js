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
 * The Behavior model module.
 * @module model/Behavior
 * @version 1.0.0
 */
class Behavior {
    /**
     * Constructs a new <code>Behavior</code>.
     * Represents behaviour reports
     * @alias module:model/Behavior
     * @param birthDate {Date} Birth date of reported person
     * @param country {module:model/Behavior.CountryEnum} Document country
     * @param documentId {String} Person document ID
     * @param documentType {module:model/Behavior.DocumentTypeEnum} Document type associated with the background check
     * @param email {String} Reported person e-mail
     * @param feedbackDate {Date} Behavior report date
     * @param firstName {String} Person first name
     * @param lastName {String} Person last name
     * @param reason {String} Report reason
     */
    constructor(birthDate, country, documentId, documentType, email, feedbackDate, firstName, lastName, reason) { 
        
        Behavior.initialize(this, birthDate, country, documentId, documentType, email, feedbackDate, firstName, lastName, reason);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, birthDate, country, documentId, documentType, email, feedbackDate, firstName, lastName, reason) { 
        obj['birth_date'] = birthDate;
        obj['country'] = country;
        obj['document_id'] = documentId;
        obj['document_type'] = documentType;
        obj['email'] = email;
        obj['feedback_date'] = feedbackDate;
        obj['first_name'] = firstName;
        obj['last_name'] = lastName;
        obj['reason'] = reason;
    }

    /**
     * Constructs a <code>Behavior</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Behavior} obj Optional instance to populate.
     * @return {module:model/Behavior} The populated <code>Behavior</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Behavior();

            if (data.hasOwnProperty('birth_date')) {
                obj['birth_date'] = ApiClient.convertToType(data['birth_date'], 'Date');
            }
            if (data.hasOwnProperty('country')) {
                obj['country'] = ApiClient.convertToType(data['country'], 'String');
            }
            if (data.hasOwnProperty('creation_date')) {
                obj['creation_date'] = ApiClient.convertToType(data['creation_date'], 'Date');
            }
            if (data.hasOwnProperty('document_id')) {
                obj['document_id'] = ApiClient.convertToType(data['document_id'], 'String');
            }
            if (data.hasOwnProperty('document_type')) {
                obj['document_type'] = ApiClient.convertToType(data['document_type'], 'String');
            }
            if (data.hasOwnProperty('email')) {
                obj['email'] = ApiClient.convertToType(data['email'], 'String');
            }
            if (data.hasOwnProperty('feedback_date')) {
                obj['feedback_date'] = ApiClient.convertToType(data['feedback_date'], 'Date');
            }
            if (data.hasOwnProperty('first_name')) {
                obj['first_name'] = ApiClient.convertToType(data['first_name'], 'String');
            }
            if (data.hasOwnProperty('last_name')) {
                obj['last_name'] = ApiClient.convertToType(data['last_name'], 'String');
            }
            if (data.hasOwnProperty('phone_number')) {
                obj['phone_number'] = ApiClient.convertToType(data['phone_number'], 'String');
            }
            if (data.hasOwnProperty('reason')) {
                obj['reason'] = ApiClient.convertToType(data['reason'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Behavior</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Behavior</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of Behavior.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['country'] && !(typeof data['country'] === 'string' || data['country'] instanceof String)) {
            throw new Error("Expected the field `country` to be a primitive type in the JSON string but got " + data['country']);
        }
        // ensure the json data is a string
        if (data['document_id'] && !(typeof data['document_id'] === 'string' || data['document_id'] instanceof String)) {
            throw new Error("Expected the field `document_id` to be a primitive type in the JSON string but got " + data['document_id']);
        }
        // ensure the json data is a string
        if (data['document_type'] && !(typeof data['document_type'] === 'string' || data['document_type'] instanceof String)) {
            throw new Error("Expected the field `document_type` to be a primitive type in the JSON string but got " + data['document_type']);
        }
        // ensure the json data is a string
        if (data['email'] && !(typeof data['email'] === 'string' || data['email'] instanceof String)) {
            throw new Error("Expected the field `email` to be a primitive type in the JSON string but got " + data['email']);
        }
        // ensure the json data is a string
        if (data['first_name'] && !(typeof data['first_name'] === 'string' || data['first_name'] instanceof String)) {
            throw new Error("Expected the field `first_name` to be a primitive type in the JSON string but got " + data['first_name']);
        }
        // ensure the json data is a string
        if (data['last_name'] && !(typeof data['last_name'] === 'string' || data['last_name'] instanceof String)) {
            throw new Error("Expected the field `last_name` to be a primitive type in the JSON string but got " + data['last_name']);
        }
        // ensure the json data is a string
        if (data['phone_number'] && !(typeof data['phone_number'] === 'string' || data['phone_number'] instanceof String)) {
            throw new Error("Expected the field `phone_number` to be a primitive type in the JSON string but got " + data['phone_number']);
        }
        // ensure the json data is a string
        if (data['reason'] && !(typeof data['reason'] === 'string' || data['reason'] instanceof String)) {
            throw new Error("Expected the field `reason` to be a primitive type in the JSON string but got " + data['reason']);
        }

        return true;
    }


}

Behavior.RequiredProperties = ["birth_date", "country", "document_id", "document_type", "email", "feedback_date", "first_name", "last_name", "reason"];

/**
 * Birth date of reported person
 * @member {Date} birth_date
 */
Behavior.prototype['birth_date'] = undefined;

/**
 * Document country
 * @member {module:model/Behavior.CountryEnum} country
 */
Behavior.prototype['country'] = undefined;

/**
 * Feedback creation date
 * @member {Date} creation_date
 */
Behavior.prototype['creation_date'] = undefined;

/**
 * Person document ID
 * @member {String} document_id
 */
Behavior.prototype['document_id'] = undefined;

/**
 * Document type associated with the background check
 * @member {module:model/Behavior.DocumentTypeEnum} document_type
 */
Behavior.prototype['document_type'] = undefined;

/**
 * Reported person e-mail
 * @member {String} email
 */
Behavior.prototype['email'] = undefined;

/**
 * Behavior report date
 * @member {Date} feedback_date
 */
Behavior.prototype['feedback_date'] = undefined;

/**
 * Person first name
 * @member {String} first_name
 */
Behavior.prototype['first_name'] = undefined;

/**
 * Person last name
 * @member {String} last_name
 */
Behavior.prototype['last_name'] = undefined;

/**
 * Phone number of the reported person
 * @member {String} phone_number
 */
Behavior.prototype['phone_number'] = undefined;

/**
 * Report reason
 * @member {String} reason
 */
Behavior.prototype['reason'] = undefined;





/**
 * Allowed values for the <code>country</code> property.
 * @enum {String}
 * @readonly
 */
Behavior['CountryEnum'] = {

    /**
     * value: "co"
     * @const
     */
    "co": "co",

    /**
     * value: "ve"
     * @const
     */
    "ve": "ve",

    /**
     * value: "cl"
     * @const
     */
    "cl": "cl",

    /**
     * value: "mx"
     * @const
     */
    "mx": "mx",

    /**
     * value: "pe"
     * @const
     */
    "pe": "pe",

    /**
     * value: "do"
     * @const
     */
    "do": "do",

    /**
     * value: "sv"
     * @const
     */
    "sv": "sv",

    /**
     * value: "gt"
     * @const
     */
    "gt": "gt",

    /**
     * value: "bo"
     * @const
     */
    "bo": "bo",

    /**
     * value: "cr"
     * @const
     */
    "cr": "cr",

    /**
     * value: "ec"
     * @const
     */
    "ec": "ec",

    /**
     * value: "pa"
     * @const
     */
    "pa": "pa",

    /**
     * value: "br"
     * @const
     */
    "br": "br"
};


/**
 * Allowed values for the <code>document_type</code> property.
 * @enum {String}
 * @readonly
 */
Behavior['DocumentTypeEnum'] = {

    /**
     * value: "national-id"
     * @const
     */
    "national-id": "national-id",

    /**
     * value: "passport"
     * @const
     */
    "passport": "passport",

    /**
     * value: "foreign-id"
     * @const
     */
    "foreign-id": "foreign-id",

    /**
     * value: "nit"
     * @const
     */
    "nit": "nit",

    /**
     * value: "diplomatic-id"
     * @const
     */
    "diplomatic-id": "diplomatic-id",

    /**
     * value: "civil-registration"
     * @const
     */
    "civil-registration": "civil-registration",

    /**
     * value: "identity-card"
     * @const
     */
    "identity-card": "identity-card",

    /**
     * value: "foreigner-card"
     * @const
     */
    "foreigner-card": "foreigner-card",

    /**
     * value: "professional-card"
     * @const
     */
    "professional-card": "professional-card",

    /**
     * value: "military-card"
     * @const
     */
    "military-card": "military-card",

    /**
     * value: "pep"
     * @const
     */
    "pep": "pep",

    /**
     * value: "nis"
     * @const
     */
    "nis": "nis",

    /**
     * value: "dni"
     * @const
     */
    "dni": "dni",

    /**
     * value: "rui"
     * @const
     */
    "rui": "rui",

    /**
     * value: "license-plate"
     * @const
     */
    "license-plate": "license-plate",

    /**
     * value: "query"
     * @const
     */
    "query": "query",

    /**
     * value: "name"
     * @const
     */
    "name": "name",

    /**
     * value: "rut"
     * @const
     */
    "rut": "rut",

    /**
     * value: "nuip"
     * @const
     */
    "nuip": "nuip",

    /**
     * value: "foreign-societies"
     * @const
     */
    "foreign-societies": "foreign-societies",

    /**
     * value: "escrow"
     * @const
     */
    "escrow": "escrow",

    /**
     * value: "individual-registration"
     * @const
     */
    "individual-registration": "individual-registration",

    /**
     * value: "general-registration"
     * @const
     */
    "general-registration": "general-registration",

    /**
     * value: "curp"
     * @const
     */
    "curp": "curp",

    /**
     * value: "dui"
     * @const
     */
    "dui": "dui",

    /**
     * value: "driver-license"
     * @const
     */
    "driver-license": "driver-license",

    /**
     * value: "ruc"
     * @const
     */
    "ruc": "ruc"
};



export default Behavior;

