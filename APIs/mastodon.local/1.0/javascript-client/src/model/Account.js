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
import Emoji from './Emoji';
import Field from './Field';
import Source from './Source';

/**
 * The Account model module.
 * @module model/Account
 * @version 1.0
 */
class Account {
    /**
     * Constructs a new <code>Account</code>.
     * Represents a user of Mastodon and their associated profile.
     * @alias module:model/Account
     */
    constructor() { 
        
        Account.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Account</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Account} obj Optional instance to populate.
     * @return {module:model/Account} The populated <code>Account</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Account();

            if (data.hasOwnProperty('acct')) {
                obj['acct'] = ApiClient.convertToType(data['acct'], 'String');
            }
            if (data.hasOwnProperty('avatar')) {
                obj['avatar'] = ApiClient.convertToType(data['avatar'], 'String');
            }
            if (data.hasOwnProperty('avatar_static')) {
                obj['avatar_static'] = ApiClient.convertToType(data['avatar_static'], 'String');
            }
            if (data.hasOwnProperty('bot')) {
                obj['bot'] = ApiClient.convertToType(data['bot'], 'Boolean');
            }
            if (data.hasOwnProperty('created_at')) {
                obj['created_at'] = ApiClient.convertToType(data['created_at'], 'Date');
            }
            if (data.hasOwnProperty('discoverable')) {
                obj['discoverable'] = ApiClient.convertToType(data['discoverable'], 'Boolean');
            }
            if (data.hasOwnProperty('display_name')) {
                obj['display_name'] = ApiClient.convertToType(data['display_name'], 'String');
            }
            if (data.hasOwnProperty('emojis')) {
                obj['emojis'] = ApiClient.convertToType(data['emojis'], [Emoji]);
            }
            if (data.hasOwnProperty('fields')) {
                obj['fields'] = ApiClient.convertToType(data['fields'], [Field]);
            }
            if (data.hasOwnProperty('followers_count')) {
                obj['followers_count'] = ApiClient.convertToType(data['followers_count'], 'Number');
            }
            if (data.hasOwnProperty('following_count')) {
                obj['following_count'] = ApiClient.convertToType(data['following_count'], 'Number');
            }
            if (data.hasOwnProperty('header')) {
                obj['header'] = ApiClient.convertToType(data['header'], 'String');
            }
            if (data.hasOwnProperty('header_static')) {
                obj['header_static'] = ApiClient.convertToType(data['header_static'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('last_status_at')) {
                obj['last_status_at'] = ApiClient.convertToType(data['last_status_at'], 'Date');
            }
            if (data.hasOwnProperty('locked')) {
                obj['locked'] = ApiClient.convertToType(data['locked'], 'Boolean');
            }
            if (data.hasOwnProperty('moved')) {
                obj['moved'] = Account.constructFromObject(data['moved']);
            }
            if (data.hasOwnProperty('mute_expires_at')) {
                obj['mute_expires_at'] = ApiClient.convertToType(data['mute_expires_at'], 'Date');
            }
            if (data.hasOwnProperty('note')) {
                obj['note'] = ApiClient.convertToType(data['note'], 'String');
            }
            if (data.hasOwnProperty('source')) {
                obj['source'] = Source.constructFromObject(data['source']);
            }
            if (data.hasOwnProperty('statuses_count')) {
                obj['statuses_count'] = ApiClient.convertToType(data['statuses_count'], 'Number');
            }
            if (data.hasOwnProperty('suspended')) {
                obj['suspended'] = ApiClient.convertToType(data['suspended'], 'Boolean');
            }
            if (data.hasOwnProperty('url')) {
                obj['url'] = ApiClient.convertToType(data['url'], 'String');
            }
            if (data.hasOwnProperty('username')) {
                obj['username'] = ApiClient.convertToType(data['username'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Account</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Account</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['acct'] && !(typeof data['acct'] === 'string' || data['acct'] instanceof String)) {
            throw new Error("Expected the field `acct` to be a primitive type in the JSON string but got " + data['acct']);
        }
        // ensure the json data is a string
        if (data['avatar'] && !(typeof data['avatar'] === 'string' || data['avatar'] instanceof String)) {
            throw new Error("Expected the field `avatar` to be a primitive type in the JSON string but got " + data['avatar']);
        }
        // ensure the json data is a string
        if (data['avatar_static'] && !(typeof data['avatar_static'] === 'string' || data['avatar_static'] instanceof String)) {
            throw new Error("Expected the field `avatar_static` to be a primitive type in the JSON string but got " + data['avatar_static']);
        }
        // ensure the json data is a string
        if (data['display_name'] && !(typeof data['display_name'] === 'string' || data['display_name'] instanceof String)) {
            throw new Error("Expected the field `display_name` to be a primitive type in the JSON string but got " + data['display_name']);
        }
        if (data['emojis']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['emojis'])) {
                throw new Error("Expected the field `emojis` to be an array in the JSON data but got " + data['emojis']);
            }
            // validate the optional field `emojis` (array)
            for (const item of data['emojis']) {
                Emoji.validateJSON(item);
            };
        }
        if (data['fields']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['fields'])) {
                throw new Error("Expected the field `fields` to be an array in the JSON data but got " + data['fields']);
            }
            // validate the optional field `fields` (array)
            for (const item of data['fields']) {
                Field.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['header'] && !(typeof data['header'] === 'string' || data['header'] instanceof String)) {
            throw new Error("Expected the field `header` to be a primitive type in the JSON string but got " + data['header']);
        }
        // ensure the json data is a string
        if (data['header_static'] && !(typeof data['header_static'] === 'string' || data['header_static'] instanceof String)) {
            throw new Error("Expected the field `header_static` to be a primitive type in the JSON string but got " + data['header_static']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // validate the optional field `moved`
        if (data['moved']) { // data not null
          Account.validateJSON(data['moved']);
        }
        // ensure the json data is a string
        if (data['note'] && !(typeof data['note'] === 'string' || data['note'] instanceof String)) {
            throw new Error("Expected the field `note` to be a primitive type in the JSON string but got " + data['note']);
        }
        // validate the optional field `source`
        if (data['source']) { // data not null
          Source.validateJSON(data['source']);
        }
        // ensure the json data is a string
        if (data['url'] && !(typeof data['url'] === 'string' || data['url'] instanceof String)) {
            throw new Error("Expected the field `url` to be a primitive type in the JSON string but got " + data['url']);
        }
        // ensure the json data is a string
        if (data['username'] && !(typeof data['username'] === 'string' || data['username'] instanceof String)) {
            throw new Error("Expected the field `username` to be a primitive type in the JSON string but got " + data['username']);
        }

        return true;
    }


}



/**
 * The Webfinger account URI. Equal to `username` for local users, or `username@domain` for
 * @member {String} acct
 */
Account.prototype['acct'] = undefined;

/**
 * An image icon that is shown next to statuses and in the profile. The format is URL.
 * @member {String} avatar
 */
Account.prototype['avatar'] = undefined;

/**
 * A static version of the avatar. Equal to `avatar` if its value is a static image; different if `avatar` is an animated GIF. The format is URL.
 * @member {String} avatar_static
 */
Account.prototype['avatar_static'] = undefined;

/**
 * A presentational flag. Indicates that the account may perform automated actions, may not be monitored, or identifies as a robot.
 * @member {Boolean} bot
 */
Account.prototype['bot'] = undefined;

/**
 * When the account was created.
 * @member {Date} created_at
 */
Account.prototype['created_at'] = undefined;

/**
 * Whether the account has opted into discovery features such as the profile directory.
 * @member {Boolean} discoverable
 */
Account.prototype['discoverable'] = undefined;

/**
 * The profile's display name.
 * @member {String} display_name
 */
Account.prototype['display_name'] = undefined;

/**
 * Custom emoji entities to be used when rendering the profile. If none, an empty array will be returned.
 * @member {Array.<module:model/Emoji>} emojis
 */
Account.prototype['emojis'] = undefined;

/**
 * Additional metadata attached to a profile as name-value pairs.
 * @member {Array.<module:model/Field>} fields
 */
Account.prototype['fields'] = undefined;

/**
 * The reported followers of this profile.
 * @member {Number} followers_count
 */
Account.prototype['followers_count'] = undefined;

/**
 * The reported follows of this profile.
 * @member {Number} following_count
 */
Account.prototype['following_count'] = undefined;

/**
 * An image banner that is shown above the profile and in profile cards. The format is URL.
 * @member {String} header
 */
Account.prototype['header'] = undefined;

/**
 * A static version of the header. Equal to `header` if its value is a static image; different if `header` is an animated GIF. The format is URL.
 * @member {String} header_static
 */
Account.prototype['header_static'] = undefined;

/**
 * The account id `header`.
 * @member {String} id
 */
Account.prototype['id'] = undefined;

/**
 * When the most recent status was posted.
 * @member {Date} last_status_at
 */
Account.prototype['last_status_at'] = undefined;

/**
 * Whether the account manually approves follow requests.
 * @member {Boolean} locked
 */
Account.prototype['locked'] = undefined;

/**
 * @member {module:model/Account} moved
 */
Account.prototype['moved'] = undefined;

/**
 * When a timed mute will expire, if applicable. ISO 8601 Datetime.
 * @member {Date} mute_expires_at
 */
Account.prototype['mute_expires_at'] = undefined;

/**
 * The profile's bio / description.
 * @member {String} note
 */
Account.prototype['note'] = undefined;

/**
 * @member {module:model/Source} source
 */
Account.prototype['source'] = undefined;

/**
 * How many statuses are attached to this account.
 * @member {Number} statuses_count
 */
Account.prototype['statuses_count'] = undefined;

/**
 * An extra entity returned when an account is suspended.
 * @member {Boolean} suspended
 */
Account.prototype['suspended'] = undefined;

/**
 * The location of the user's profile page. (HTTPS URL)
 * @member {String} url
 */
Account.prototype['url'] = undefined;

/**
 * The username of the account, not including domain.
 * @member {String} username
 */
Account.prototype['username'] = undefined;






export default Account;

