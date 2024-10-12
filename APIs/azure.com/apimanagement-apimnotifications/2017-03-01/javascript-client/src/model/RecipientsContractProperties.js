/**
 * ApiManagementClient
 * Use these REST APIs for performing operations on who is going to receive notifications associated with your Azure API Management deployment.
 *
 * The version of the OpenAPI document: 2017-03-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The RecipientsContractProperties model module.
 * @module model/RecipientsContractProperties
 * @version 2017-03-01
 */
class RecipientsContractProperties {
    /**
     * Constructs a new <code>RecipientsContractProperties</code>.
     * Notification Parameter contract.
     * @alias module:model/RecipientsContractProperties
     */
    constructor() { 
        
        RecipientsContractProperties.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>RecipientsContractProperties</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/RecipientsContractProperties} obj Optional instance to populate.
     * @return {module:model/RecipientsContractProperties} The populated <code>RecipientsContractProperties</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new RecipientsContractProperties();

            if (data.hasOwnProperty('emails')) {
                obj['emails'] = ApiClient.convertToType(data['emails'], ['String']);
            }
            if (data.hasOwnProperty('users')) {
                obj['users'] = ApiClient.convertToType(data['users'], ['String']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>RecipientsContractProperties</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>RecipientsContractProperties</code>.
     */
    static validateJSON(data) {
        // ensure the json data is an array
        if (!Array.isArray(data['emails'])) {
            throw new Error("Expected the field `emails` to be an array in the JSON data but got " + data['emails']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['users'])) {
            throw new Error("Expected the field `users` to be an array in the JSON data but got " + data['users']);
        }

        return true;
    }


}



/**
 * List of Emails subscribed for the notification.
 * @member {Array.<String>} emails
 */
RecipientsContractProperties.prototype['emails'] = undefined;

/**
 * List of Users subscribed for the notification.
 * @member {Array.<String>} users
 */
RecipientsContractProperties.prototype['users'] = undefined;






export default RecipientsContractProperties;

