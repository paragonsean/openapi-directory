/**
 * KeyServ
 * KeyServ API
 *
 * The version of the OpenAPI document: 1.4.5
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The CurrentKey model module.
 * @module model/CurrentKey
 * @version 1.4.5
 */
class CurrentKey {
    /**
     * Constructs a new <code>CurrentKey</code>.
     * @alias module:model/CurrentKey
     */
    constructor() { 
        
        CurrentKey.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>CurrentKey</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CurrentKey} obj Optional instance to populate.
     * @return {module:model/CurrentKey} The populated <code>CurrentKey</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CurrentKey();

            if (data.hasOwnProperty('current')) {
                obj['current'] = ApiClient.convertToType(data['current'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CurrentKey</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CurrentKey</code>.
     */
    static validateJSON(data) {

        return true;
    }


}



/**
 * @member {Boolean} current
 */
CurrentKey.prototype['current'] = undefined;






export default CurrentKey;

