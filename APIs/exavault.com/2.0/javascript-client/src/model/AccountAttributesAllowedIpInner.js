/**
 * ExaVault
 * ExaVaults API allows you to incorporate ExaVaults suite of file transfer and user management tools into your own application.\\nExaVault supports both POST (recommended when requesting large data sets) and GET operations, and requires an API key in order to use.
 *
 * The version of the OpenAPI document: 2.0
 * Contact: support@exavault.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The AccountAttributesAllowedIpInner model module.
 * @module model/AccountAttributesAllowedIpInner
 * @version 2.0
 */
class AccountAttributesAllowedIpInner {
    /**
     * Constructs a new <code>AccountAttributesAllowedIpInner</code>.
     * @alias module:model/AccountAttributesAllowedIpInner
     */
    constructor() { 
        
        AccountAttributesAllowedIpInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>AccountAttributesAllowedIpInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AccountAttributesAllowedIpInner} obj Optional instance to populate.
     * @return {module:model/AccountAttributesAllowedIpInner} The populated <code>AccountAttributesAllowedIpInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AccountAttributesAllowedIpInner();

            if (data.hasOwnProperty('ipEnd')) {
                obj['ipEnd'] = ApiClient.convertToType(data['ipEnd'], 'String');
            }
            if (data.hasOwnProperty('ipStart')) {
                obj['ipStart'] = ApiClient.convertToType(data['ipStart'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AccountAttributesAllowedIpInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AccountAttributesAllowedIpInner</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['ipEnd'] && !(typeof data['ipEnd'] === 'string' || data['ipEnd'] instanceof String)) {
            throw new Error("Expected the field `ipEnd` to be a primitive type in the JSON string but got " + data['ipEnd']);
        }
        // ensure the json data is a string
        if (data['ipStart'] && !(typeof data['ipStart'] === 'string' || data['ipStart'] instanceof String)) {
            throw new Error("Expected the field `ipStart` to be a primitive type in the JSON string but got " + data['ipStart']);
        }

        return true;
    }


}



/**
 * @member {String} ipEnd
 */
AccountAttributesAllowedIpInner.prototype['ipEnd'] = undefined;

/**
 * @member {String} ipStart
 */
AccountAttributesAllowedIpInner.prototype['ipStart'] = undefined;






export default AccountAttributesAllowedIpInner;

