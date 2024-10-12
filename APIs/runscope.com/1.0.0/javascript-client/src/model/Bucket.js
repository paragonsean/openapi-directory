/**
 * Runscope API
 * Manage Runscope programmatically.
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import Team from './Team';

/**
 * The Bucket model module.
 * @module model/Bucket
 * @version 1.0.0
 */
class Bucket {
    /**
     * Constructs a new <code>Bucket</code>.
     * @alias module:model/Bucket
     */
    constructor() { 
        
        Bucket.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Bucket</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Bucket} obj Optional instance to populate.
     * @return {module:model/Bucket} The populated <code>Bucket</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Bucket();

            if (data.hasOwnProperty('auth_token')) {
                obj['auth_token'] = ApiClient.convertToType(data['auth_token'], 'String');
            }
            if (data.hasOwnProperty('collections_url')) {
                obj['collections_url'] = ApiClient.convertToType(data['collections_url'], 'String');
            }
            if (data.hasOwnProperty('default')) {
                obj['default'] = ApiClient.convertToType(data['default'], 'Boolean');
            }
            if (data.hasOwnProperty('key')) {
                obj['key'] = ApiClient.convertToType(data['key'], 'String');
            }
            if (data.hasOwnProperty('messages_url')) {
                obj['messages_url'] = ApiClient.convertToType(data['messages_url'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('team')) {
                obj['team'] = Team.constructFromObject(data['team']);
            }
            if (data.hasOwnProperty('tests_url')) {
                obj['tests_url'] = ApiClient.convertToType(data['tests_url'], 'String');
            }
            if (data.hasOwnProperty('trigger_url')) {
                obj['trigger_url'] = ApiClient.convertToType(data['trigger_url'], 'String');
            }
            if (data.hasOwnProperty('verify_ssl')) {
                obj['verify_ssl'] = ApiClient.convertToType(data['verify_ssl'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Bucket</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Bucket</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['auth_token'] && !(typeof data['auth_token'] === 'string' || data['auth_token'] instanceof String)) {
            throw new Error("Expected the field `auth_token` to be a primitive type in the JSON string but got " + data['auth_token']);
        }
        // ensure the json data is a string
        if (data['collections_url'] && !(typeof data['collections_url'] === 'string' || data['collections_url'] instanceof String)) {
            throw new Error("Expected the field `collections_url` to be a primitive type in the JSON string but got " + data['collections_url']);
        }
        // ensure the json data is a string
        if (data['key'] && !(typeof data['key'] === 'string' || data['key'] instanceof String)) {
            throw new Error("Expected the field `key` to be a primitive type in the JSON string but got " + data['key']);
        }
        // ensure the json data is a string
        if (data['messages_url'] && !(typeof data['messages_url'] === 'string' || data['messages_url'] instanceof String)) {
            throw new Error("Expected the field `messages_url` to be a primitive type in the JSON string but got " + data['messages_url']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // validate the optional field `team`
        if (data['team']) { // data not null
          Team.validateJSON(data['team']);
        }
        // ensure the json data is a string
        if (data['tests_url'] && !(typeof data['tests_url'] === 'string' || data['tests_url'] instanceof String)) {
            throw new Error("Expected the field `tests_url` to be a primitive type in the JSON string but got " + data['tests_url']);
        }
        // ensure the json data is a string
        if (data['trigger_url'] && !(typeof data['trigger_url'] === 'string' || data['trigger_url'] instanceof String)) {
            throw new Error("Expected the field `trigger_url` to be a primitive type in the JSON string but got " + data['trigger_url']);
        }

        return true;
    }


}



/**
 * Bucket auth token if set, otherwise this value is null.
 * @member {String} auth_token
 */
Bucket.prototype['auth_token'] = undefined;

/**
 * @member {String} collections_url
 */
Bucket.prototype['collections_url'] = undefined;

/**
 * True if this bucket is the 'default' for a team. Default buckets cannot be deleted.
 * @member {Boolean} default
 */
Bucket.prototype['default'] = undefined;

/**
 * The unique identifier used to address a bucket.
 * @member {String} key
 */
Bucket.prototype['key'] = undefined;

/**
 * @member {String} messages_url
 */
Bucket.prototype['messages_url'] = undefined;

/**
 * The name of this bucket as displayed in your dashboard.
 * @member {String} name
 */
Bucket.prototype['name'] = undefined;

/**
 * @member {module:model/Team} team
 */
Bucket.prototype['team'] = undefined;

/**
 * @member {String} tests_url
 */
Bucket.prototype['tests_url'] = undefined;

/**
 * @member {String} trigger_url
 */
Bucket.prototype['trigger_url'] = undefined;

/**
 * True if this bucket is configured to verify ssl for requests made to it.
 * @member {Boolean} verify_ssl
 */
Bucket.prototype['verify_ssl'] = undefined;






export default Bucket;

