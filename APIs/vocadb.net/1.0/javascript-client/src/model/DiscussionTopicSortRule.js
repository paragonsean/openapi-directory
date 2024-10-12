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
* Enum class DiscussionTopicSortRule.
* @enum {}
* @readonly
*/
export default class DiscussionTopicSortRule {
    
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
         * value: "DateCreated"
         * @const
         */
        "DateCreated" = "DateCreated";

    
        /**
         * value: "LastCommentDate"
         * @const
         */
        "LastCommentDate" = "LastCommentDate";

    

    /**
    * Returns a <code>DiscussionTopicSortRule</code> enum value from a Javascript object name.
    * @param {Object} data The plain JavaScript object containing the name of the enum value.
    * @return {module:model/DiscussionTopicSortRule} The enum <code>DiscussionTopicSortRule</code> value.
    */
    static constructFromObject(object) {
        return object;
    }
}

