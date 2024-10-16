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
import TestGetDeviceConfigurations200ResponseInnerModelDeviceFrameFull from './TestGetDeviceConfigurations200ResponseInnerModelDeviceFrameFull';

/**
 * The DeviceFrame model module.
 * @module model/DeviceFrame
 * @version v0.1
 */
class DeviceFrame {
    /**
     * Constructs a new <code>DeviceFrame</code>.
     * @alias module:model/DeviceFrame
     */
    constructor() { 
        
        DeviceFrame.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>DeviceFrame</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/DeviceFrame} obj Optional instance to populate.
     * @return {module:model/DeviceFrame} The populated <code>DeviceFrame</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new DeviceFrame();

            if (data.hasOwnProperty('full')) {
                obj['full'] = TestGetDeviceConfigurations200ResponseInnerModelDeviceFrameFull.constructFromObject(data['full']);
            }
            if (data.hasOwnProperty('grid')) {
                obj['grid'] = TestGetDeviceConfigurations200ResponseInnerModelDeviceFrameFull.constructFromObject(data['grid']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>DeviceFrame</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>DeviceFrame</code>.
     */
    static validateJSON(data) {
        // validate the optional field `full`
        if (data['full']) { // data not null
          TestGetDeviceConfigurations200ResponseInnerModelDeviceFrameFull.validateJSON(data['full']);
        }
        // validate the optional field `grid`
        if (data['grid']) { // data not null
          TestGetDeviceConfigurations200ResponseInnerModelDeviceFrameFull.validateJSON(data['grid']);
        }

        return true;
    }


}



/**
 * @member {module:model/TestGetDeviceConfigurations200ResponseInnerModelDeviceFrameFull} full
 */
DeviceFrame.prototype['full'] = undefined;

/**
 * @member {module:model/TestGetDeviceConfigurations200ResponseInnerModelDeviceFrameFull} grid
 */
DeviceFrame.prototype['grid'] = undefined;






export default DeviceFrame;

