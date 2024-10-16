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
 * The AppleLoginResponse model module.
 * @module model/AppleLoginResponse
 * @version v0.1
 */
class AppleLoginResponse {
    /**
     * Constructs a new <code>AppleLoginResponse</code>.
     * Indicates if login was successful.
     * @alias module:model/AppleLoginResponse
     */
    constructor() { 
        
        AppleLoginResponse.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>AppleLoginResponse</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AppleLoginResponse} obj Optional instance to populate.
     * @return {module:model/AppleLoginResponse} The populated <code>AppleLoginResponse</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AppleLoginResponse();

            if (data.hasOwnProperty('successful')) {
                obj['successful'] = ApiClient.convertToType(data['successful'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AppleLoginResponse</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AppleLoginResponse</code>.
     */
    static validateJSON(data) {

        return true;
    }


}



/**
 * True when login was successful.
 * @member {Boolean} successful
 */
AppleLoginResponse.prototype['successful'] = undefined;






export default AppleLoginResponse;

