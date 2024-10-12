/**
 * TSAPI
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
/**
* Enum class ParentType.
* @enum {}
* @readonly
*/
export default class ParentType {
    
        /**
         * value: 1
         * @const
         */
        "1" = 1;

    
        /**
         * value: 2
         * @const
         */
        "2" = 2;

    
        /**
         * value: 3
         * @const
         */
        "3" = 3;

    

    /**
    * Returns a <code>ParentType</code> enum value from a Javascript object name.
    * @param {Object} data The plain JavaScript object containing the name of the enum value.
    * @return {module:model/ParentType} The enum <code>ParentType</code> value.
    */
    static constructFromObject(object) {
        return object;
    }
}

