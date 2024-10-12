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

/**
 * The ApiV1FiltersPostRequest model module.
 * @module model/ApiV1FiltersPostRequest
 * @version 1.0
 */
class ApiV1FiltersPostRequest {
    /**
     * Constructs a new <code>ApiV1FiltersPostRequest</code>.
     * @alias module:model/ApiV1FiltersPostRequest
     * @param context {Array.<module:model/ApiV1FiltersPostRequest.ContextEnum>} Array of enumerable strings `home`, `notifications`, `public`, `thread`. At least one context must be specified.
     * @param phrase {String} Text to be filtered.
     */
    constructor(context, phrase) { 
        
        ApiV1FiltersPostRequest.initialize(this, context, phrase);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, context, phrase) { 
        obj['context'] = context;
        obj['phrase'] = phrase;
    }

    /**
     * Constructs a <code>ApiV1FiltersPostRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ApiV1FiltersPostRequest} obj Optional instance to populate.
     * @return {module:model/ApiV1FiltersPostRequest} The populated <code>ApiV1FiltersPostRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ApiV1FiltersPostRequest();

            if (data.hasOwnProperty('context')) {
                obj['context'] = ApiClient.convertToType(data['context'], ['String']);
            }
            if (data.hasOwnProperty('expires_in')) {
                obj['expires_in'] = ApiClient.convertToType(data['expires_in'], 'Number');
            }
            if (data.hasOwnProperty('irreversible')) {
                obj['irreversible'] = ApiClient.convertToType(data['irreversible'], 'Boolean');
            }
            if (data.hasOwnProperty('phrase')) {
                obj['phrase'] = ApiClient.convertToType(data['phrase'], 'String');
            }
            if (data.hasOwnProperty('whole_word')) {
                obj['whole_word'] = ApiClient.convertToType(data['whole_word'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ApiV1FiltersPostRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ApiV1FiltersPostRequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of ApiV1FiltersPostRequest.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is an array
        if (!Array.isArray(data['context'])) {
            throw new Error("Expected the field `context` to be an array in the JSON data but got " + data['context']);
        }
        // ensure the json data is a string
        if (data['phrase'] && !(typeof data['phrase'] === 'string' || data['phrase'] instanceof String)) {
            throw new Error("Expected the field `phrase` to be a primitive type in the JSON string but got " + data['phrase']);
        }

        return true;
    }


}

ApiV1FiltersPostRequest.RequiredProperties = ["context", "phrase"];

/**
 * Array of enumerable strings `home`, `notifications`, `public`, `thread`. At least one context must be specified.
 * @member {Array.<module:model/ApiV1FiltersPostRequest.ContextEnum>} context
 */
ApiV1FiltersPostRequest.prototype['context'] = undefined;

/**
 * Number of seconds from now the filter should expire. Otherwise, null for a filter that doesn't expire.
 * @member {Number} expires_in
 */
ApiV1FiltersPostRequest.prototype['expires_in'] = undefined;

/**
 * Should the server irreversibly drop matching entities from home and notifications?
 * @member {Boolean} irreversible
 */
ApiV1FiltersPostRequest.prototype['irreversible'] = undefined;

/**
 * Text to be filtered.
 * @member {String} phrase
 */
ApiV1FiltersPostRequest.prototype['phrase'] = undefined;

/**
 * Consider word boundaries?
 * @member {Boolean} whole_word
 */
ApiV1FiltersPostRequest.prototype['whole_word'] = undefined;





/**
 * Allowed values for the <code>context</code> property.
 * @enum {String}
 * @readonly
 */
ApiV1FiltersPostRequest['ContextEnum'] = {

    /**
     * value: "home"
     * @const
     */
    "home": "home",

    /**
     * value: "notifications"
     * @const
     */
    "notifications": "notifications",

    /**
     * value: "public"
     * @const
     */
    "public": "public",

    /**
     * value: "thread"
     * @const
     */
    "thread": "thread"
};



export default ApiV1FiltersPostRequest;

