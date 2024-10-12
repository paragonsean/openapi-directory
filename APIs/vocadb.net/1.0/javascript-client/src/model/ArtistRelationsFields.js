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
* Enum class ArtistRelationsFields.
* @enum {}
* @readonly
*/
export default class ArtistRelationsFields {
    
        /**
         * value: "None"
         * @const
         */
        "None" = "None";

    
        /**
         * value: "LatestAlbums"
         * @const
         */
        "LatestAlbums" = "LatestAlbums";

    
        /**
         * value: "LatestEvents"
         * @const
         */
        "LatestEvents" = "LatestEvents";

    
        /**
         * value: "LatestSongs"
         * @const
         */
        "LatestSongs" = "LatestSongs";

    
        /**
         * value: "PopularAlbums"
         * @const
         */
        "PopularAlbums" = "PopularAlbums";

    
        /**
         * value: "PopularSongs"
         * @const
         */
        "PopularSongs" = "PopularSongs";

    
        /**
         * value: "All"
         * @const
         */
        "All" = "All";

    

    /**
    * Returns a <code>ArtistRelationsFields</code> enum value from a Javascript object name.
    * @param {Object} data The plain JavaScript object containing the name of the enum value.
    * @return {module:model/ArtistRelationsFields} The enum <code>ArtistRelationsFields</code> value.
    */
    static constructFromObject(object) {
        return object;
    }
}

