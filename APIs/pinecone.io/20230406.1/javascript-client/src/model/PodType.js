/**
 * Pinecone API
 * Pinecone is a vector database. This is an unofficial, community-managed OpenAPI spec that (should) accurately model the Pinecone API. This project was developed independent of and is unaffiliated with Pinecone Systems. Users should switch to the official API spec, if and when Pinecone releases it.
 *
 * The version of the OpenAPI document: 20230406.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
/**
* Enum class PodType.
* @enum {}
* @readonly
*/
export default class PodType {
    
        /**
         * value: "s1.x1"
         * @const
         */
        "s1.x1" = "s1.x1";

    
        /**
         * value: "s1.x2"
         * @const
         */
        "s1.x2" = "s1.x2";

    
        /**
         * value: "s1.x4"
         * @const
         */
        "s1.x4" = "s1.x4";

    
        /**
         * value: "s1.x8"
         * @const
         */
        "s1.x8" = "s1.x8";

    
        /**
         * value: "p1.x1"
         * @const
         */
        "p1.x1" = "p1.x1";

    
        /**
         * value: "p1.x2"
         * @const
         */
        "p1.x2" = "p1.x2";

    
        /**
         * value: "p1.x4"
         * @const
         */
        "p1.x4" = "p1.x4";

    
        /**
         * value: "p1.x8"
         * @const
         */
        "p1.x8" = "p1.x8";

    
        /**
         * value: "p2.x1"
         * @const
         */
        "p2.x1" = "p2.x1";

    
        /**
         * value: "p2.x2"
         * @const
         */
        "p2.x2" = "p2.x2";

    
        /**
         * value: "p2.x4"
         * @const
         */
        "p2.x4" = "p2.x4";

    
        /**
         * value: "p2.x8"
         * @const
         */
        "p2.x8" = "p2.x8";

    

    /**
    * Returns a <code>PodType</code> enum value from a Javascript object name.
    * @param {Object} data The plain JavaScript object containing the name of the enum value.
    * @return {module:model/PodType} The enum <code>PodType</code> value.
    */
    static constructFromObject(object) {
        return object;
    }
}

