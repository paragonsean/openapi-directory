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
import DeviceSetDeviceConfigurationsInnerImage from './DeviceSetDeviceConfigurationsInnerImage';
import DeviceSetDeviceConfigurationsInnerModel from './DeviceSetDeviceConfigurationsInnerModel';

/**
 * The DeviceSetDeviceConfigurationsInner model module.
 * @module model/DeviceSetDeviceConfigurationsInner
 * @version v0.1
 */
class DeviceSetDeviceConfigurationsInner {
    /**
     * Constructs a new <code>DeviceSetDeviceConfigurationsInner</code>.
     * @alias module:model/DeviceSetDeviceConfigurationsInner
     */
    constructor() { 
        
        DeviceSetDeviceConfigurationsInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>DeviceSetDeviceConfigurationsInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/DeviceSetDeviceConfigurationsInner} obj Optional instance to populate.
     * @return {module:model/DeviceSetDeviceConfigurationsInner} The populated <code>DeviceSetDeviceConfigurationsInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new DeviceSetDeviceConfigurationsInner();

            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('image')) {
                obj['image'] = DeviceSetDeviceConfigurationsInnerImage.constructFromObject(data['image']);
            }
            if (data.hasOwnProperty('model')) {
                obj['model'] = DeviceSetDeviceConfigurationsInnerModel.constructFromObject(data['model']);
            }
            if (data.hasOwnProperty('os')) {
                obj['os'] = ApiClient.convertToType(data['os'], 'String');
            }
            if (data.hasOwnProperty('osName')) {
                obj['osName'] = ApiClient.convertToType(data['osName'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>DeviceSetDeviceConfigurationsInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>DeviceSetDeviceConfigurationsInner</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // validate the optional field `image`
        if (data['image']) { // data not null
          DeviceSetDeviceConfigurationsInnerImage.validateJSON(data['image']);
        }
        // validate the optional field `model`
        if (data['model']) { // data not null
          DeviceSetDeviceConfigurationsInnerModel.validateJSON(data['model']);
        }
        // ensure the json data is a string
        if (data['os'] && !(typeof data['os'] === 'string' || data['os'] instanceof String)) {
            throw new Error("Expected the field `os` to be a primitive type in the JSON string but got " + data['os']);
        }
        // ensure the json data is a string
        if (data['osName'] && !(typeof data['osName'] === 'string' || data['osName'] instanceof String)) {
            throw new Error("Expected the field `osName` to be a primitive type in the JSON string but got " + data['osName']);
        }

        return true;
    }


}



/**
 * The unique id of the device configuration
 * @member {String} id
 */
DeviceSetDeviceConfigurationsInner.prototype['id'] = undefined;

/**
 * @member {module:model/DeviceSetDeviceConfigurationsInnerImage} image
 */
DeviceSetDeviceConfigurationsInner.prototype['image'] = undefined;

/**
 * @member {module:model/DeviceSetDeviceConfigurationsInnerModel} model
 */
DeviceSetDeviceConfigurationsInner.prototype['model'] = undefined;

/**
 * @member {String} os
 */
DeviceSetDeviceConfigurationsInner.prototype['os'] = undefined;

/**
 * @member {String} osName
 */
DeviceSetDeviceConfigurationsInner.prototype['osName'] = undefined;






export default DeviceSetDeviceConfigurationsInner;

