/**
 * Mastodon API Specification (https://github.com/mastodon/mastodon)
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 * Contact: sardo@hey.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import Account from './Account';
import Application from './Application';
import Attachment from './Attachment';
import Card from './Card';
import Emoji from './Emoji';
import Mention from './Mention';
import Poll from './Poll';
import ScheduledStatus from './ScheduledStatus';
import Status from './Status';
import StatusParams from './StatusParams';
import Tag from './Tag';

/**
 * The ApiV1StatusesPost200Response model module.
 * @module model/ApiV1StatusesPost200Response
 * @version 1.0
 */
class ApiV1StatusesPost200Response {
    /**
     * Constructs a new <code>ApiV1StatusesPost200Response</code>.
     * @alias module:model/ApiV1StatusesPost200Response
     * @param {(module:model/ScheduledStatus|module:model/Status)} instance The actual instance to initialize ApiV1StatusesPost200Response.
     */
    constructor(instance = null) {
        if (instance === null) {
            this.actualInstance = null;
            return;
        }
        var match = 0;
        var errorMessages = [];
        try {
            if (typeof instance === "Status") {
                this.actualInstance = instance;
            } else {
                // plain JS object
                // validate the object
                Status.validateJSON(instance); // throw an exception if no match
                // create Status from JS object
                this.actualInstance = Status.constructFromObject(instance);
            }
            match++;
        } catch(err) {
            // json data failed to deserialize into Status
            errorMessages.push("Failed to construct Status: " + err)
        }

        try {
            if (typeof instance === "ScheduledStatus") {
                this.actualInstance = instance;
            } else {
                // plain JS object
                // validate the object
                ScheduledStatus.validateJSON(instance); // throw an exception if no match
                // create ScheduledStatus from JS object
                this.actualInstance = ScheduledStatus.constructFromObject(instance);
            }
            match++;
        } catch(err) {
            // json data failed to deserialize into ScheduledStatus
            errorMessages.push("Failed to construct ScheduledStatus: " + err)
        }

        if (match > 1) {
            throw new Error("Multiple matches found constructing `ApiV1StatusesPost200Response` with oneOf schemas ScheduledStatus, Status. Input: " + JSON.stringify(instance));
        } else if (match === 0) {
            this.actualInstance = null; // clear the actual instance in case there are multiple matches
            throw new Error("No match found constructing `ApiV1StatusesPost200Response` with oneOf schemas ScheduledStatus, Status. Details: " +
                            errorMessages.join(", "));
        } else { // only 1 match
            // the input is valid
        }
    }

    /**
     * Constructs a <code>ApiV1StatusesPost200Response</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ApiV1StatusesPost200Response} obj Optional instance to populate.
     * @return {module:model/ApiV1StatusesPost200Response} The populated <code>ApiV1StatusesPost200Response</code> instance.
     */
    static constructFromObject(data, obj) {
        return new ApiV1StatusesPost200Response(data);
    }

    /**
     * Gets the actual instance, which can be <code>ScheduledStatus</code>, <code>Status</code>.
     * @return {(module:model/ScheduledStatus|module:model/Status)} The actual instance.
     */
    getActualInstance() {
        return this.actualInstance;
    }

    /**
     * Sets the actual instance, which can be <code>ScheduledStatus</code>, <code>Status</code>.
     * @param {(module:model/ScheduledStatus|module:model/Status)} obj The actual instance.
     */
    setActualInstance(obj) {
       this.actualInstance = ApiV1StatusesPost200Response.constructFromObject(obj).getActualInstance();
    }

    /**
     * Returns the JSON representation of the actual instance.
     * @return {string}
     */
    toJSON = function(){
        return this.getActualInstance();
    }

    /**
     * Create an instance of ApiV1StatusesPost200Response from a JSON string.
     * @param {string} json_string JSON string.
     * @return {module:model/ApiV1StatusesPost200Response} An instance of ApiV1StatusesPost200Response.
     */
    static fromJSON = function(json_string){
        return ApiV1StatusesPost200Response.constructFromObject(JSON.parse(json_string));
    }
}

/**
 * @member {module:model/Account} account
 */
ApiV1StatusesPost200Response.prototype['account'] = undefined;

/**
 * @member {module:model/Application} application
 */
ApiV1StatusesPost200Response.prototype['application'] = undefined;

/**
 * Have you bookmarked this status?
 * @member {Boolean} bookmarked
 */
ApiV1StatusesPost200Response.prototype['bookmarked'] = undefined;

/**
 * @member {module:model/Card} card
 */
ApiV1StatusesPost200Response.prototype['card'] = undefined;

/**
 * HTML-encoded status content.
 * @member {String} content
 */
ApiV1StatusesPost200Response.prototype['content'] = undefined;

/**
 * The date when this status was created.
 * @member {Date} created_at
 */
ApiV1StatusesPost200Response.prototype['created_at'] = undefined;

/**
 * Custom emoji to be used when rendering status content.
 * @member {Array.<module:model/Emoji>} emojis
 */
ApiV1StatusesPost200Response.prototype['emojis'] = undefined;

/**
 * Have you favourited this status?
 * @member {Boolean} favourited
 */
ApiV1StatusesPost200Response.prototype['favourited'] = undefined;

/**
 * How many favourites this status has received.
 * @member {Number} favourites_count
 */
ApiV1StatusesPost200Response.prototype['favourites_count'] = undefined;

/**
 * ID of the scheduled status in the database. Cast from an integer, but not guaranteed to be a number.
 * @member {String} id
 */
ApiV1StatusesPost200Response.prototype['id'] = undefined;

/**
 * ID of the account being replied to.
 * @member {String} in_reply_to_account_id
 */
ApiV1StatusesPost200Response.prototype['in_reply_to_account_id'] = undefined;

/**
 * ID of the status being replied. Cast from an integer but not guaranteed to be a number.
 * @member {String} in_reply_to_id
 */
ApiV1StatusesPost200Response.prototype['in_reply_to_id'] = undefined;

/**
 * Primary language of this status. ISO 639 Part 1 two-letter language code.
 * @member {String} language
 */
ApiV1StatusesPost200Response.prototype['language'] = undefined;

/**
 * Array of attachements
 * @member {Array.<module:model/Attachment>} media_attachments
 */
ApiV1StatusesPost200Response.prototype['media_attachments'] = undefined;

/**
 * Mentions of users within the status content.
 * @member {Array.<module:model/Mention>} mentions
 */
ApiV1StatusesPost200Response.prototype['mentions'] = undefined;

/**
 * Have you muted notifications for this status's conversation?
 * @member {Boolean} muted
 */
ApiV1StatusesPost200Response.prototype['muted'] = undefined;

/**
 * Have you pinned this status? Only appears if the status is pinnable.
 * @member {Boolean} pinned
 */
ApiV1StatusesPost200Response.prototype['pinned'] = undefined;

/**
 * @member {module:model/Poll} poll
 */
ApiV1StatusesPost200Response.prototype['poll'] = undefined;

/**
 * @member {module:model/Status} reblog
 */
ApiV1StatusesPost200Response.prototype['reblog'] = undefined;

/**
 * Have you boosted this status?
 * @member {Boolean} reblogged
 */
ApiV1StatusesPost200Response.prototype['reblogged'] = undefined;

/**
 * How many boosts this status has received.
 * @member {Number} reblogs_count
 */
ApiV1StatusesPost200Response.prototype['reblogs_count'] = undefined;

/**
 * How many replies this status has received.
 * @member {Number} replies_count
 */
ApiV1StatusesPost200Response.prototype['replies_count'] = undefined;

/**
 * Is this status marked as sensitive content?
 * @member {Boolean} sensitive
 */
ApiV1StatusesPost200Response.prototype['sensitive'] = undefined;

/**
 * Subject or summary line, below which status content is collapsed until expanded.
 * @member {String} spoiler_text
 */
ApiV1StatusesPost200Response.prototype['spoiler_text'] = undefined;

/**
 * Hashtags used within the status content.
 * @member {Array.<module:model/Tag>} tags
 */
ApiV1StatusesPost200Response.prototype['tags'] = undefined;

/**
 * Plain-text source of a status. Returned instead of `content` when status is deleted, so the user may redraft from the source text without the client having to reverse-engineer the original text from the HTML content.
 * @member {String} text
 */
ApiV1StatusesPost200Response.prototype['text'] = undefined;

/**
 * URI of the status used for federation.
 * @member {String} uri
 */
ApiV1StatusesPost200Response.prototype['uri'] = undefined;

/**
 * A link to the status's HTML representation.
 * @member {String} url
 */
ApiV1StatusesPost200Response.prototype['url'] = undefined;

/**
 * Visibility of this status.
 * @member {module:model/ApiV1StatusesPost200Response.VisibilityEnum} visibility
 */
ApiV1StatusesPost200Response.prototype['visibility'] = undefined;

/**
 * @member {module:model/StatusParams} params
 */
ApiV1StatusesPost200Response.prototype['params'] = undefined;

/**
 * ID of the status in the database. ISO 8601 Datetime.
 * @member {Date} scheduled_at
 */
ApiV1StatusesPost200Response.prototype['scheduled_at'] = undefined;


ApiV1StatusesPost200Response.OneOf = ["ScheduledStatus", "Status"];

export default ApiV1StatusesPost200Response;

