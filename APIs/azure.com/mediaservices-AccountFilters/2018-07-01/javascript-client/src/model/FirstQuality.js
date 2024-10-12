/**
 * Azure Media Services
 * This Swagger was generated by the API Framework.
 *
 * The version of the OpenAPI document: 2018-07-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The FirstQuality model module.
 * @module model/FirstQuality
 * @version 2018-07-01
 */
class FirstQuality {
    /**
     * Constructs a new <code>FirstQuality</code>.
     * Filter First Quality
     * @alias module:model/FirstQuality
     * @param bitrate {Number} The first quality bitrate.
     */
    constructor(bitrate) { 
        
        FirstQuality.initialize(this, bitrate);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, bitrate) { 
        obj['bitrate'] = bitrate;
    }

    /**
     * Constructs a <code>FirstQuality</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/FirstQuality} obj Optional instance to populate.
     * @return {module:model/FirstQuality} The populated <code>FirstQuality</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new FirstQuality();

            if (data.hasOwnProperty('bitrate')) {
                obj['bitrate'] = ApiClient.convertToType(data['bitrate'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>FirstQuality</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>FirstQuality</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of FirstQuality.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }

        return true;
    }


}

FirstQuality.RequiredProperties = ["bitrate"];

/**
 * The first quality bitrate.
 * @member {Number} bitrate
 */
FirstQuality.prototype['bitrate'] = undefined;






export default FirstQuality;

