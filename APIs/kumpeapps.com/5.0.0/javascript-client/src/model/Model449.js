/**
 * KumpeApps API
 * KKid API. Due to security concerns all calls to this API requires authentication. If you have access then you may use your KumpeApps username/password to authenticate. To gain access please use the contact developer link below.
 *
 * The version of the OpenAPI document: 5.0.0
 * Contact: helpdesk@kumpeapps.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The Model449 model module.
 * @module model/Model449
 * @version 5.0.0
 */
class Model449 {
    /**
     * Constructs a new <code>Model449</code>.
     * OTP Required is configured for this User. Retry login with OTP
     * @alias module:model/Model449
     */
    constructor() { 
        
        Model449.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Model449</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Model449} obj Optional instance to populate.
     * @return {module:model/Model449} The populated <code>Model449</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Model449();

            if (data.hasOwnProperty('message')) {
                obj['message'] = ApiClient.convertToType(data['message'], 'String');
            }
            if (data.hasOwnProperty('success')) {
                obj['success'] = ApiClient.convertToType(data['success'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Model449</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Model449</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['message'] && !(typeof data['message'] === 'string' || data['message'] instanceof String)) {
            throw new Error("Expected the field `message` to be a primitive type in the JSON string but got " + data['message']);
        }

        return true;
    }


}



/**
 * @member {String} message
 */
Model449.prototype['message'] = undefined;

/**
 * @member {Boolean} success
 */
Model449.prototype['success'] = undefined;






export default Model449;

