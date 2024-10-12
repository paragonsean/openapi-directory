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
* Enum class EntryOptionalFields.
* @enum {}
* @readonly
*/
export default class EntryOptionalFields {
    
        /**
         * value: "None"
         * @const
         */
        "None" = "None";

    
        /**
         * value: "AdditionalNames"
         * @const
         */
        "AdditionalNames" = "AdditionalNames";

    
        /**
         * value: "Description"
         * @const
         */
        "Description" = "Description";

    
        /**
         * value: "MainPicture"
         * @const
         */
        "MainPicture" = "MainPicture";

    
        /**
         * value: "Names"
         * @const
         */
        "Names" = "Names";

    
        /**
         * value: "PVs"
         * @const
         */
        "PVs" = "PVs";

    
        /**
         * value: "Tags"
         * @const
         */
        "Tags" = "Tags";

    
        /**
         * value: "WebLinks"
         * @const
         */
        "WebLinks" = "WebLinks";

    

    /**
    * Returns a <code>EntryOptionalFields</code> enum value from a Javascript object name.
    * @param {Object} data The plain JavaScript object containing the name of the enum value.
    * @return {module:model/EntryOptionalFields} The enum <code>EntryOptionalFields</code> value.
    */
    static constructFromObject(object) {
        return object;
    }
}

