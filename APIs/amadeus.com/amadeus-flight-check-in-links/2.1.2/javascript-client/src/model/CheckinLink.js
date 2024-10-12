/**
 * Flight Check-in Links
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.  Please also be aware that our test environment is based on a subset of the production, to see what is included in test please refer to our **[data collection](https://github.com/amadeus4dev/data-collection)**.
 *
 * The version of the OpenAPI document: 2.1.2
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The CheckinLink model module.
 * @module model/CheckinLink
 * @version 2.1.2
 */
class CheckinLink {
    /**
     * Constructs a new <code>CheckinLink</code>.
     * @alias module:model/CheckinLink
     * @param channel {module:model/CheckinLink.ChannelEnum} indicates the type of channel supported by the URL
     * @param href {String} direct URL to the relevant page
     * @param id {String} identifier of the resource
     * @param type {String} the resource name
     */
    constructor(channel, href, id, type) { 
        
        CheckinLink.initialize(this, channel, href, id, type);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, channel, href, id, type) { 
        obj['channel'] = channel;
        obj['href'] = href;
        obj['id'] = id;
        obj['type'] = type;
    }

    /**
     * Constructs a <code>CheckinLink</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CheckinLink} obj Optional instance to populate.
     * @return {module:model/CheckinLink} The populated <code>CheckinLink</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CheckinLink();

            if (data.hasOwnProperty('channel')) {
                obj['channel'] = ApiClient.convertToType(data['channel'], 'String');
            }
            if (data.hasOwnProperty('href')) {
                obj['href'] = ApiClient.convertToType(data['href'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('parameters')) {
                obj['parameters'] = ApiClient.convertToType(data['parameters'], Object);
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CheckinLink</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CheckinLink</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of CheckinLink.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['channel'] && !(typeof data['channel'] === 'string' || data['channel'] instanceof String)) {
            throw new Error("Expected the field `channel` to be a primitive type in the JSON string but got " + data['channel']);
        }
        // ensure the json data is a string
        if (data['href'] && !(typeof data['href'] === 'string' || data['href'] instanceof String)) {
            throw new Error("Expected the field `href` to be a primitive type in the JSON string but got " + data['href']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }

        return true;
    }


}

CheckinLink.RequiredProperties = ["channel", "href", "id", "type"];

/**
 * indicates the type of channel supported by the URL
 * @member {module:model/CheckinLink.ChannelEnum} channel
 */
CheckinLink.prototype['channel'] = undefined;

/**
 * direct URL to the relevant page
 * @member {String} href
 */
CheckinLink.prototype['href'] = undefined;

/**
 * identifier of the resource
 * @member {String} id
 */
CheckinLink.prototype['id'] = undefined;

/**
 * list of URL parameters with descriptive information such as description and/or type and/or format
 * @member {Object} parameters
 */
CheckinLink.prototype['parameters'] = undefined;

/**
 * the resource name
 * @member {String} type
 */
CheckinLink.prototype['type'] = undefined;





/**
 * Allowed values for the <code>channel</code> property.
 * @enum {String}
 * @readonly
 */
CheckinLink['ChannelEnum'] = {

    /**
     * value: "Mobile"
     * @const
     */
    "Mobile": "Mobile",

    /**
     * value: "Web"
     * @const
     */
    "Web": "Web",

    /**
     * value: "All"
     * @const
     */
    "All": "All"
};



export default CheckinLink;

