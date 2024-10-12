/**
 * seven.io API
 * seven.io Swagger API. Get your API-Key now at seven.io.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: support@seven.io
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The HooksGet200ResponseHooksInner model module.
 * @module model/HooksGet200ResponseHooksInner
 * @version 1.0.0
 */
class HooksGet200ResponseHooksInner {
    /**
     * Constructs a new <code>HooksGet200ResponseHooksInner</code>.
     * @alias module:model/HooksGet200ResponseHooksInner
     */
    constructor() { 
        
        HooksGet200ResponseHooksInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>HooksGet200ResponseHooksInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/HooksGet200ResponseHooksInner} obj Optional instance to populate.
     * @return {module:model/HooksGet200ResponseHooksInner} The populated <code>HooksGet200ResponseHooksInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new HooksGet200ResponseHooksInner();

            if (data.hasOwnProperty('created')) {
                obj['created'] = ApiClient.convertToType(data['created'], 'String');
            }
            if (data.hasOwnProperty('event_type')) {
                obj['event_type'] = ApiClient.convertToType(data['event_type'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('request_method')) {
                obj['request_method'] = ApiClient.convertToType(data['request_method'], 'String');
            }
            if (data.hasOwnProperty('target_url')) {
                obj['target_url'] = ApiClient.convertToType(data['target_url'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>HooksGet200ResponseHooksInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>HooksGet200ResponseHooksInner</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['created'] && !(typeof data['created'] === 'string' || data['created'] instanceof String)) {
            throw new Error("Expected the field `created` to be a primitive type in the JSON string but got " + data['created']);
        }
        // ensure the json data is a string
        if (data['event_type'] && !(typeof data['event_type'] === 'string' || data['event_type'] instanceof String)) {
            throw new Error("Expected the field `event_type` to be a primitive type in the JSON string but got " + data['event_type']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['request_method'] && !(typeof data['request_method'] === 'string' || data['request_method'] instanceof String)) {
            throw new Error("Expected the field `request_method` to be a primitive type in the JSON string but got " + data['request_method']);
        }
        // ensure the json data is a string
        if (data['target_url'] && !(typeof data['target_url'] === 'string' || data['target_url'] instanceof String)) {
            throw new Error("Expected the field `target_url` to be a primitive type in the JSON string but got " + data['target_url']);
        }

        return true;
    }


}



/**
 * @member {String} created
 */
HooksGet200ResponseHooksInner.prototype['created'] = undefined;

/**
 * @member {String} event_type
 */
HooksGet200ResponseHooksInner.prototype['event_type'] = undefined;

/**
 * @member {String} id
 */
HooksGet200ResponseHooksInner.prototype['id'] = undefined;

/**
 * @member {String} request_method
 */
HooksGet200ResponseHooksInner.prototype['request_method'] = undefined;

/**
 * @member {String} target_url
 */
HooksGet200ResponseHooksInner.prototype['target_url'] = undefined;






export default HooksGet200ResponseHooksInner;

