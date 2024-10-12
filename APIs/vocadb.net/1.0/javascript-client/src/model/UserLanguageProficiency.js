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
* Enum class UserLanguageProficiency.
* @enum {}
* @readonly
*/
export default class UserLanguageProficiency {
    
        /**
         * value: "Nothing"
         * @const
         */
        "Nothing" = "Nothing";

    
        /**
         * value: "Basics"
         * @const
         */
        "Basics" = "Basics";

    
        /**
         * value: "Intermediate"
         * @const
         */
        "Intermediate" = "Intermediate";

    
        /**
         * value: "Advanced"
         * @const
         */
        "Advanced" = "Advanced";

    
        /**
         * value: "Native"
         * @const
         */
        "Native" = "Native";

    

    /**
    * Returns a <code>UserLanguageProficiency</code> enum value from a Javascript object name.
    * @param {Object} data The plain JavaScript object containing the name of the enum value.
    * @return {module:model/UserLanguageProficiency} The enum <code>UserLanguageProficiency</code> value.
    */
    static constructFromObject(object) {
        return object;
    }
}

