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
 * The NotificationGetDefaultResponseDetailsInner model module.
 * @module model/NotificationGetDefaultResponseDetailsInner
 * @version 2017-03-01
 */
class NotificationGetDefaultResponseDetailsInner {
    /**
     * Constructs a new <code>NotificationGetDefaultResponseDetailsInner</code>.
     * Error Field contract.
     * @alias module:model/NotificationGetDefaultResponseDetailsInner
     */
    constructor() { 
        
        NotificationGetDefaultResponseDetailsInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>NotificationGetDefaultResponseDetailsInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/NotificationGetDefaultResponseDetailsInner} obj Optional instance to populate.
     * @return {module:model/NotificationGetDefaultResponseDetailsInner} The populated <code>NotificationGetDefaultResponseDetailsInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new NotificationGetDefaultResponseDetailsInner();

            if (data.hasOwnProperty('code')) {
                obj['code'] = ApiClient.convertToType(data['code'], 'String');
            }
            if (data.hasOwnProperty('message')) {
                obj['message'] = ApiClient.convertToType(data['message'], 'String');
            }
            if (data.hasOwnProperty('target')) {
                obj['target'] = ApiClient.convertToType(data['target'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>NotificationGetDefaultResponseDetailsInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>NotificationGetDefaultResponseDetailsInner</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['code'] && !(typeof data['code'] === 'string' || data['code'] instanceof String)) {
            throw new Error("Expected the field `code` to be a primitive type in the JSON string but got " + data['code']);
        }
        // ensure the json data is a string
        if (data['message'] && !(typeof data['message'] === 'string' || data['message'] instanceof String)) {
            throw new Error("Expected the field `message` to be a primitive type in the JSON string but got " + data['message']);
        }
        // ensure the json data is a string
        if (data['target'] && !(typeof data['target'] === 'string' || data['target'] instanceof String)) {
            throw new Error("Expected the field `target` to be a primitive type in the JSON string but got " + data['target']);
        }

        return true;
    }


}



/**
 * Property level error code.
 * @member {String} code
 */
NotificationGetDefaultResponseDetailsInner.prototype['code'] = undefined;

/**
 * Human-readable representation of property-level error.
 * @member {String} message
 */
NotificationGetDefaultResponseDetailsInner.prototype['message'] = undefined;

/**
 * Property name.
 * @member {String} target
 */
NotificationGetDefaultResponseDetailsInner.prototype['target'] = undefined;






export default NotificationGetDefaultResponseDetailsInner;

