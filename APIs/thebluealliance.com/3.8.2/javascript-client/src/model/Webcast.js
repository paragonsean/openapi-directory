/**
 * The Blue Alliance API v3
 * # Overview    Information and statistics about FIRST Robotics Competition teams and events.   # Authentication   All endpoints require an Auth Key to be passed in the header `X-TBA-Auth-Key`. If you do not have an auth key yet, you can obtain one from your [Account Page](/account).
 *
 * The version of the OpenAPI document: 3.8.2
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The Webcast model module.
 * @module model/Webcast
 * @version 3.8.2
 */
class Webcast {
    /**
     * Constructs a new <code>Webcast</code>.
     * @alias module:model/Webcast
     * @param channel {String} Type specific channel information. May be the YouTube stream, or Twitch channel name. In the case of iframe types, contains HTML to embed the stream in an HTML iframe.
     * @param type {module:model/Webcast.TypeEnum} Type of webcast, typically descriptive of the streaming provider.
     */
    constructor(channel, type) { 
        
        Webcast.initialize(this, channel, type);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, channel, type) { 
        obj['channel'] = channel;
        obj['type'] = type;
    }

    /**
     * Constructs a <code>Webcast</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Webcast} obj Optional instance to populate.
     * @return {module:model/Webcast} The populated <code>Webcast</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Webcast();

            if (data.hasOwnProperty('channel')) {
                obj['channel'] = ApiClient.convertToType(data['channel'], 'String');
            }
            if (data.hasOwnProperty('date')) {
                obj['date'] = ApiClient.convertToType(data['date'], 'String');
            }
            if (data.hasOwnProperty('file')) {
                obj['file'] = ApiClient.convertToType(data['file'], 'String');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Webcast</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Webcast</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of Webcast.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['channel'] && !(typeof data['channel'] === 'string' || data['channel'] instanceof String)) {
            throw new Error("Expected the field `channel` to be a primitive type in the JSON string but got " + data['channel']);
        }
        // ensure the json data is a string
        if (data['date'] && !(typeof data['date'] === 'string' || data['date'] instanceof String)) {
            throw new Error("Expected the field `date` to be a primitive type in the JSON string but got " + data['date']);
        }
        // ensure the json data is a string
        if (data['file'] && !(typeof data['file'] === 'string' || data['file'] instanceof String)) {
            throw new Error("Expected the field `file` to be a primitive type in the JSON string but got " + data['file']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }

        return true;
    }


}

Webcast.RequiredProperties = ["channel", "type"];

/**
 * Type specific channel information. May be the YouTube stream, or Twitch channel name. In the case of iframe types, contains HTML to embed the stream in an HTML iframe.
 * @member {String} channel
 */
Webcast.prototype['channel'] = undefined;

/**
 * The date for the webcast in `yyyy-mm-dd` format. May be null.
 * @member {String} date
 */
Webcast.prototype['date'] = undefined;

/**
 * File identification as may be required for some types. May be null.
 * @member {String} file
 */
Webcast.prototype['file'] = undefined;

/**
 * Type of webcast, typically descriptive of the streaming provider.
 * @member {module:model/Webcast.TypeEnum} type
 */
Webcast.prototype['type'] = undefined;





/**
 * Allowed values for the <code>type</code> property.
 * @enum {String}
 * @readonly
 */
Webcast['TypeEnum'] = {

    /**
     * value: "youtube"
     * @const
     */
    "youtube": "youtube",

    /**
     * value: "twitch"
     * @const
     */
    "twitch": "twitch",

    /**
     * value: "ustream"
     * @const
     */
    "ustream": "ustream",

    /**
     * value: "iframe"
     * @const
     */
    "iframe": "iframe",

    /**
     * value: "html5"
     * @const
     */
    "html5": "html5",

    /**
     * value: "rtmp"
     * @const
     */
    "rtmp": "rtmp",

    /**
     * value: "livestream"
     * @const
     */
    "livestream": "livestream",

    /**
     * value: "direct_link"
     * @const
     */
    "direct_link": "direct_link",

    /**
     * value: "mms"
     * @const
     */
    "mms": "mms",

    /**
     * value: "justin"
     * @const
     */
    "justin": "justin",

    /**
     * value: "stemtv"
     * @const
     */
    "stemtv": "stemtv",

    /**
     * value: "dacast"
     * @const
     */
    "dacast": "dacast"
};



export default Webcast;

