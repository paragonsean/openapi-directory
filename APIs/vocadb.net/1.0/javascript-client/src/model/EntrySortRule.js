/**
 * VocaDbWeb
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
/**
* Enum class EntrySortRule.
* @enum {}
* @readonly
*/
export default class EntrySortRule {
    
        /**
         * value: "None"
         * @const
         */
        "None" = "None";

    
        /**
         * value: "Name"
         * @const
         */
        "Name" = "Name";

    
        /**
         * value: "AdditionDate"
         * @const
         */
        "AdditionDate" = "AdditionDate";

    
        /**
         * value: "ActivityDate"
         * @const
         */
        "ActivityDate" = "ActivityDate";

    

    /**
    * Returns a <code>EntrySortRule</code> enum value from a Javascript object name.
    * @param {Object} data The plain JavaScript object containing the name of the enum value.
    * @return {module:model/EntrySortRule} The enum <code>EntrySortRule</code> value.
    */
    static constructFromObject(object) {
        return object;
    }
}

