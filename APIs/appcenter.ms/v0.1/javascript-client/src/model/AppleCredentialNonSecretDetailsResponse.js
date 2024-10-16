/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The AppleCredentialNonSecretDetailsResponse model module.
 * @module model/AppleCredentialNonSecretDetailsResponse
 * @version v0.1
 */
class AppleCredentialNonSecretDetailsResponse {
    /**
     * Constructs a new <code>AppleCredentialNonSecretDetailsResponse</code>.
     * Apple credentials non-secret details
     * @alias module:model/AppleCredentialNonSecretDetailsResponse
     * @param displayName {String} display name of shared connection
     * @param serviceType {module:model/AppleCredentialNonSecretDetailsResponse.ServiceTypeEnum} service type of shared connection can be apple|gitlab|googleplay|jira
     */
    constructor(displayName, serviceType) { 
        
        AppleCredentialNonSecretDetailsResponse.initialize(this, displayName, serviceType);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, displayName, serviceType) { 
        obj['data'] = data;
        obj['displayName'] = displayName;
        obj['serviceType'] = serviceType;
    }

    /**
     * Constructs a <code>AppleCredentialNonSecretDetailsResponse</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AppleCredentialNonSecretDetailsResponse} obj Optional instance to populate.
     * @return {module:model/AppleCredentialNonSecretDetailsResponse} The populated <code>AppleCredentialNonSecretDetailsResponse</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AppleCredentialNonSecretDetailsResponse();

            if (data.hasOwnProperty('data')) {
                obj['data'] = ApiClient.convertToType(data['data'], Object);
            }
            if (data.hasOwnProperty('credentialType')) {
                obj['credentialType'] = ApiClient.convertToType(data['credentialType'], 'String');
            }
            if (data.hasOwnProperty('displayName')) {
                obj['displayName'] = ApiClient.convertToType(data['displayName'], 'String');
            }
            if (data.hasOwnProperty('serviceType')) {
                obj['serviceType'] = ApiClient.convertToType(data['serviceType'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AppleCredentialNonSecretDetailsResponse</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AppleCredentialNonSecretDetailsResponse</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of AppleCredentialNonSecretDetailsResponse.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `data`
        if (data['data']) { // data not null
          Object.validateJSON(data['data']);
        }
        // ensure the json data is a string
        if (data['credentialType'] && !(typeof data['credentialType'] === 'string' || data['credentialType'] instanceof String)) {
            throw new Error("Expected the field `credentialType` to be a primitive type in the JSON string but got " + data['credentialType']);
        }
        // ensure the json data is a string
        if (data['displayName'] && !(typeof data['displayName'] === 'string' || data['displayName'] instanceof String)) {
            throw new Error("Expected the field `displayName` to be a primitive type in the JSON string but got " + data['displayName']);
        }
        // ensure the json data is a string
        if (data['serviceType'] && !(typeof data['serviceType'] === 'string' || data['serviceType'] instanceof String)) {
            throw new Error("Expected the field `serviceType` to be a primitive type in the JSON string but got " + data['serviceType']);
        }

        return true;
    }


}

AppleCredentialNonSecretDetailsResponse.RequiredProperties = ["data", "displayName", "serviceType"];

/**
 * Apple credentials non-secret data
 * @member {Object} data
 */
AppleCredentialNonSecretDetailsResponse.prototype['data'] = undefined;

/**
 * the type of the credential
 * @member {module:model/AppleCredentialNonSecretDetailsResponse.CredentialTypeEnum} credentialType
 */
AppleCredentialNonSecretDetailsResponse.prototype['credentialType'] = undefined;

/**
 * display name of shared connection
 * @member {String} displayName
 */
AppleCredentialNonSecretDetailsResponse.prototype['displayName'] = undefined;

/**
 * service type of shared connection can be apple|gitlab|googleplay|jira
 * @member {module:model/AppleCredentialNonSecretDetailsResponse.ServiceTypeEnum} serviceType
 */
AppleCredentialNonSecretDetailsResponse.prototype['serviceType'] = undefined;





/**
 * Allowed values for the <code>credentialType</code> property.
 * @enum {String}
 * @readonly
 */
AppleCredentialNonSecretDetailsResponse['CredentialTypeEnum'] = {

    /**
     * value: "credentials"
     * @const
     */
    "credentials": "credentials",

    /**
     * value: "certificate"
     * @const
     */
    "certificate": "certificate",

    /**
     * value: "key"
     * @const
     */
    "key": "key"
};


/**
 * Allowed values for the <code>serviceType</code> property.
 * @enum {String}
 * @readonly
 */
AppleCredentialNonSecretDetailsResponse['ServiceTypeEnum'] = {

    /**
     * value: "apple"
     * @const
     */
    "apple": "apple",

    /**
     * value: "jira"
     * @const
     */
    "jira": "jira",

    /**
     * value: "googleplay"
     * @const
     */
    "googleplay": "googleplay",

    /**
     * value: "gitlab"
     * @const
     */
    "gitlab": "gitlab"
};



export default AppleCredentialNonSecretDetailsResponse;

