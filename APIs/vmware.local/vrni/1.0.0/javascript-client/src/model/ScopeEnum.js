/**
 * vRealize Network Insight API Reference
 * vRealize Network Insight API Reference
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
/**
* Enum class ScopeEnum.
* @enum {}
* @readonly
*/
export default class ScopeEnum {
    
        /**
         * value: "UNIVERSAL"
         * @const
         */
        "UNIVERSAL" = "UNIVERSAL";

    
        /**
         * value: "GLOBAL"
         * @const
         */
        "GLOBAL" = "GLOBAL";

    

    /**
    * Returns a <code>ScopeEnum</code> enum value from a Javascript object name.
    * @param {Object} data The plain JavaScript object containing the name of the enum value.
    * @return {module:model/ScopeEnum} The enum <code>ScopeEnum</code> value.
    */
    static constructFromObject(object) {
        return object;
    }
}

