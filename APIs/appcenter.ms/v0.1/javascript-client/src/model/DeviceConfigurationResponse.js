/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The DeviceConfigurationResponse model module.
 * @module model/DeviceConfigurationResponse
 * @version v0.1
 */
class DeviceConfigurationResponse {
    /**
     * Constructs a new <code>DeviceConfigurationResponse</code>.
     * A response containing the fully encoded binary blob for a mobileconfig
     * @alias module:model/DeviceConfigurationResponse
     * @param dataUrl {String} A data URL containing a signed mobileconfig profile
     */
    constructor(dataUrl) { 
        
        DeviceConfigurationResponse.initialize(this, dataUrl);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, dataUrl) { 
        obj['data_url'] = dataUrl;
    }

    /**
     * Constructs a <code>DeviceConfigurationResponse</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/DeviceConfigurationResponse} obj Optional instance to populate.
     * @return {module:model/DeviceConfigurationResponse} The populated <code>DeviceConfigurationResponse</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new DeviceConfigurationResponse();

            if (data.hasOwnProperty('data_url')) {
                obj['data_url'] = ApiClient.convertToType(data['data_url'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>DeviceConfigurationResponse</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>DeviceConfigurationResponse</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of DeviceConfigurationResponse.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['data_url'] && !(typeof data['data_url'] === 'string' || data['data_url'] instanceof String)) {
            throw new Error("Expected the field `data_url` to be a primitive type in the JSON string but got " + data['data_url']);
        }

        return true;
    }


}

DeviceConfigurationResponse.RequiredProperties = ["data_url"];

/**
 * A data URL containing a signed mobileconfig profile
 * @member {String} data_url
 */
DeviceConfigurationResponse.prototype['data_url'] = undefined;






export default DeviceConfigurationResponse;

