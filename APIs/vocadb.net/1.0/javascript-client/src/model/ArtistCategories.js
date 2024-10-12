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
* Enum class ArtistCategories.
* @enum {}
* @readonly
*/
export default class ArtistCategories {
    
        /**
         * value: "Nothing"
         * @const
         */
        "Nothing" = "Nothing";

    
        /**
         * value: "Vocalist"
         * @const
         */
        "Vocalist" = "Vocalist";

    
        /**
         * value: "Producer"
         * @const
         */
        "Producer" = "Producer";

    
        /**
         * value: "Animator"
         * @const
         */
        "Animator" = "Animator";

    
        /**
         * value: "Label"
         * @const
         */
        "Label" = "Label";

    
        /**
         * value: "Circle"
         * @const
         */
        "Circle" = "Circle";

    
        /**
         * value: "Other"
         * @const
         */
        "Other" = "Other";

    
        /**
         * value: "Band"
         * @const
         */
        "Band" = "Band";

    
        /**
         * value: "Illustrator"
         * @const
         */
        "Illustrator" = "Illustrator";

    
        /**
         * value: "Subject"
         * @const
         */
        "Subject" = "Subject";

    

    /**
    * Returns a <code>ArtistCategories</code> enum value from a Javascript object name.
    * @param {Object} data The plain JavaScript object containing the name of the enum value.
    * @return {module:model/ArtistCategories} The enum <code>ArtistCategories</code> value.
    */
    static constructFromObject(object) {
        return object;
    }
}

