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
 * The JiraSecretDetails model module.
 * @module model/JiraSecretDetails
 * @version v0.1
 */
class JiraSecretDetails {
    /**
     * Constructs a new <code>JiraSecretDetails</code>.
     * Jira secret details
     * @alias module:model/JiraSecretDetails
     * @param baseUrl {String} baseUrl to connect to jira instance
     * @param password {String} password to connect to jira instance
     * @param username {String} username to connect to jira instance
     */
    constructor(baseUrl, password, username) { 
        
        JiraSecretDetails.initialize(this, baseUrl, password, username);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, baseUrl, password, username) { 
        obj['baseUrl'] = baseUrl;
        obj['password'] = password;
        obj['username'] = username;
    }

    /**
     * Constructs a <code>JiraSecretDetails</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/JiraSecretDetails} obj Optional instance to populate.
     * @return {module:model/JiraSecretDetails} The populated <code>JiraSecretDetails</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new JiraSecretDetails();

            if (data.hasOwnProperty('baseUrl')) {
                obj['baseUrl'] = ApiClient.convertToType(data['baseUrl'], 'String');
            }
            if (data.hasOwnProperty('password')) {
                obj['password'] = ApiClient.convertToType(data['password'], 'String');
            }
            if (data.hasOwnProperty('username')) {
                obj['username'] = ApiClient.convertToType(data['username'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>JiraSecretDetails</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>JiraSecretDetails</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of JiraSecretDetails.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['baseUrl'] && !(typeof data['baseUrl'] === 'string' || data['baseUrl'] instanceof String)) {
            throw new Error("Expected the field `baseUrl` to be a primitive type in the JSON string but got " + data['baseUrl']);
        }
        // ensure the json data is a string
        if (data['password'] && !(typeof data['password'] === 'string' || data['password'] instanceof String)) {
            throw new Error("Expected the field `password` to be a primitive type in the JSON string but got " + data['password']);
        }
        // ensure the json data is a string
        if (data['username'] && !(typeof data['username'] === 'string' || data['username'] instanceof String)) {
            throw new Error("Expected the field `username` to be a primitive type in the JSON string but got " + data['username']);
        }

        return true;
    }


}

JiraSecretDetails.RequiredProperties = ["baseUrl", "password", "username"];

/**
 * baseUrl to connect to jira instance
 * @member {String} baseUrl
 */
JiraSecretDetails.prototype['baseUrl'] = undefined;

/**
 * password to connect to jira instance
 * @member {String} password
 */
JiraSecretDetails.prototype['password'] = undefined;

/**
 * username to connect to jira instance
 * @member {String} username
 */
JiraSecretDetails.prototype['username'] = undefined;






export default JiraSecretDetails;

