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
* Enum class EntryType.
* @enum {}
* @readonly
*/
export default class EntryType {
    
        /**
         * value: "Undefined"
         * @const
         */
        "Undefined" = "Undefined";

    
        /**
         * value: "Album"
         * @const
         */
        "Album" = "Album";

    
        /**
         * value: "Artist"
         * @const
         */
        "Artist" = "Artist";

    
        /**
         * value: "DiscussionTopic"
         * @const
         */
        "DiscussionTopic" = "DiscussionTopic";

    
        /**
         * value: "PV"
         * @const
         */
        "PV" = "PV";

    
        /**
         * value: "ReleaseEvent"
         * @const
         */
        "ReleaseEvent" = "ReleaseEvent";

    
        /**
         * value: "ReleaseEventSeries"
         * @const
         */
        "ReleaseEventSeries" = "ReleaseEventSeries";

    
        /**
         * value: "Song"
         * @const
         */
        "Song" = "Song";

    
        /**
         * value: "SongList"
         * @const
         */
        "SongList" = "SongList";

    
        /**
         * value: "Tag"
         * @const
         */
        "Tag" = "Tag";

    
        /**
         * value: "User"
         * @const
         */
        "User" = "User";

    
        /**
         * value: "Venue"
         * @const
         */
        "Venue" = "Venue";

    

    /**
    * Returns a <code>EntryType</code> enum value from a Javascript object name.
    * @param {Object} data The plain JavaScript object containing the name of the enum value.
    * @return {module:model/EntryType} The enum <code>EntryType</code> value.
    */
    static constructFromObject(object) {
        return object;
    }
}

