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
 * The DeviceResolution model module.
 * @module model/DeviceResolution
 * @version v0.1
 */
class DeviceResolution {
    /**
     * Constructs a new <code>DeviceResolution</code>.
     * Device screen resolution
     * @alias module:model/DeviceResolution
     */
    constructor() { 
        
        DeviceResolution.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>DeviceResolution</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/DeviceResolution} obj Optional instance to populate.
     * @return {module:model/DeviceResolution} The populated <code>DeviceResolution</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new DeviceResolution();

            if (data.hasOwnProperty('height')) {
                obj['height'] = ApiClient.convertToType(data['height'], 'String');
            }
            if (data.hasOwnProperty('ppi')) {
                obj['ppi'] = ApiClient.convertToType(data['ppi'], 'String');
            }
            if (data.hasOwnProperty('width')) {
                obj['width'] = ApiClient.convertToType(data['width'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>DeviceResolution</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>DeviceResolution</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['height'] && !(typeof data['height'] === 'string' || data['height'] instanceof String)) {
            throw new Error("Expected the field `height` to be a primitive type in the JSON string but got " + data['height']);
        }
        // ensure the json data is a string
        if (data['ppi'] && !(typeof data['ppi'] === 'string' || data['ppi'] instanceof String)) {
            throw new Error("Expected the field `ppi` to be a primitive type in the JSON string but got " + data['ppi']);
        }
        // ensure the json data is a string
        if (data['width'] && !(typeof data['width'] === 'string' || data['width'] instanceof String)) {
            throw new Error("Expected the field `width` to be a primitive type in the JSON string but got " + data['width']);
        }

        return true;
    }


}



/**
 * @member {String} height
 */
DeviceResolution.prototype['height'] = undefined;

/**
 * @member {String} ppi
 */
DeviceResolution.prototype['ppi'] = undefined;

/**
 * @member {String} width
 */
DeviceResolution.prototype['width'] = undefined;






export default DeviceResolution;

