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
import TestGetDeviceConfigurations200ResponseInnerModelCpu from './TestGetDeviceConfigurations200ResponseInnerModelCpu';
import TestGetDeviceConfigurations200ResponseInnerModelDeviceFrame from './TestGetDeviceConfigurations200ResponseInnerModelDeviceFrame';
import TestGetDeviceConfigurations200ResponseInnerModelDimensions from './TestGetDeviceConfigurations200ResponseInnerModelDimensions';
import TestGetDeviceConfigurations200ResponseInnerModelMemory from './TestGetDeviceConfigurations200ResponseInnerModelMemory';
import TestGetDeviceConfigurations200ResponseInnerModelResolution from './TestGetDeviceConfigurations200ResponseInnerModelResolution';
import TestGetDeviceConfigurations200ResponseInnerModelScreenSize from './TestGetDeviceConfigurations200ResponseInnerModelScreenSize';

/**
 * The DeviceModel model module.
 * @module model/DeviceModel
 * @version v0.1
 */
class DeviceModel {
    /**
     * Constructs a new <code>DeviceModel</code>.
     * @alias module:model/DeviceModel
     */
    constructor() { 
        
        DeviceModel.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>DeviceModel</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/DeviceModel} obj Optional instance to populate.
     * @return {module:model/DeviceModel} The populated <code>DeviceModel</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new DeviceModel();

            if (data.hasOwnProperty('availabilityCount')) {
                obj['availabilityCount'] = ApiClient.convertToType(data['availabilityCount'], 'Number');
            }
            if (data.hasOwnProperty('cpu')) {
                obj['cpu'] = TestGetDeviceConfigurations200ResponseInnerModelCpu.constructFromObject(data['cpu']);
            }
            if (data.hasOwnProperty('deviceFrame')) {
                obj['deviceFrame'] = TestGetDeviceConfigurations200ResponseInnerModelDeviceFrame.constructFromObject(data['deviceFrame']);
            }
            if (data.hasOwnProperty('dimensions')) {
                obj['dimensions'] = TestGetDeviceConfigurations200ResponseInnerModelDimensions.constructFromObject(data['dimensions']);
            }
            if (data.hasOwnProperty('formFactor')) {
                obj['formFactor'] = ApiClient.convertToType(data['formFactor'], 'String');
            }
            if (data.hasOwnProperty('manufacturer')) {
                obj['manufacturer'] = ApiClient.convertToType(data['manufacturer'], 'String');
            }
            if (data.hasOwnProperty('memory')) {
                obj['memory'] = TestGetDeviceConfigurations200ResponseInnerModelMemory.constructFromObject(data['memory']);
            }
            if (data.hasOwnProperty('model')) {
                obj['model'] = ApiClient.convertToType(data['model'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('platform')) {
                obj['platform'] = ApiClient.convertToType(data['platform'], 'String');
            }
            if (data.hasOwnProperty('releaseDate')) {
                obj['releaseDate'] = ApiClient.convertToType(data['releaseDate'], 'String');
            }
            if (data.hasOwnProperty('resolution')) {
                obj['resolution'] = TestGetDeviceConfigurations200ResponseInnerModelResolution.constructFromObject(data['resolution']);
            }
            if (data.hasOwnProperty('screenRotation')) {
                obj['screenRotation'] = ApiClient.convertToType(data['screenRotation'], 'Number');
            }
            if (data.hasOwnProperty('screenSize')) {
                obj['screenSize'] = TestGetDeviceConfigurations200ResponseInnerModelScreenSize.constructFromObject(data['screenSize']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>DeviceModel</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>DeviceModel</code>.
     */
    static validateJSON(data) {
        // validate the optional field `cpu`
        if (data['cpu']) { // data not null
          TestGetDeviceConfigurations200ResponseInnerModelCpu.validateJSON(data['cpu']);
        }
        // validate the optional field `deviceFrame`
        if (data['deviceFrame']) { // data not null
          TestGetDeviceConfigurations200ResponseInnerModelDeviceFrame.validateJSON(data['deviceFrame']);
        }
        // validate the optional field `dimensions`
        if (data['dimensions']) { // data not null
          TestGetDeviceConfigurations200ResponseInnerModelDimensions.validateJSON(data['dimensions']);
        }
        // ensure the json data is a string
        if (data['formFactor'] && !(typeof data['formFactor'] === 'string' || data['formFactor'] instanceof String)) {
            throw new Error("Expected the field `formFactor` to be a primitive type in the JSON string but got " + data['formFactor']);
        }
        // ensure the json data is a string
        if (data['manufacturer'] && !(typeof data['manufacturer'] === 'string' || data['manufacturer'] instanceof String)) {
            throw new Error("Expected the field `manufacturer` to be a primitive type in the JSON string but got " + data['manufacturer']);
        }
        // validate the optional field `memory`
        if (data['memory']) { // data not null
          TestGetDeviceConfigurations200ResponseInnerModelMemory.validateJSON(data['memory']);
        }
        // ensure the json data is a string
        if (data['model'] && !(typeof data['model'] === 'string' || data['model'] instanceof String)) {
            throw new Error("Expected the field `model` to be a primitive type in the JSON string but got " + data['model']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['platform'] && !(typeof data['platform'] === 'string' || data['platform'] instanceof String)) {
            throw new Error("Expected the field `platform` to be a primitive type in the JSON string but got " + data['platform']);
        }
        // ensure the json data is a string
        if (data['releaseDate'] && !(typeof data['releaseDate'] === 'string' || data['releaseDate'] instanceof String)) {
            throw new Error("Expected the field `releaseDate` to be a primitive type in the JSON string but got " + data['releaseDate']);
        }
        // validate the optional field `resolution`
        if (data['resolution']) { // data not null
          TestGetDeviceConfigurations200ResponseInnerModelResolution.validateJSON(data['resolution']);
        }
        // validate the optional field `screenSize`
        if (data['screenSize']) { // data not null
          TestGetDeviceConfigurations200ResponseInnerModelScreenSize.validateJSON(data['screenSize']);
        }

        return true;
    }


}



/**
 * @member {Number} availabilityCount
 */
DeviceModel.prototype['availabilityCount'] = undefined;

/**
 * @member {module:model/TestGetDeviceConfigurations200ResponseInnerModelCpu} cpu
 */
DeviceModel.prototype['cpu'] = undefined;

/**
 * @member {module:model/TestGetDeviceConfigurations200ResponseInnerModelDeviceFrame} deviceFrame
 */
DeviceModel.prototype['deviceFrame'] = undefined;

/**
 * @member {module:model/TestGetDeviceConfigurations200ResponseInnerModelDimensions} dimensions
 */
DeviceModel.prototype['dimensions'] = undefined;

/**
 * @member {String} formFactor
 */
DeviceModel.prototype['formFactor'] = undefined;

/**
 * @member {String} manufacturer
 */
DeviceModel.prototype['manufacturer'] = undefined;

/**
 * @member {module:model/TestGetDeviceConfigurations200ResponseInnerModelMemory} memory
 */
DeviceModel.prototype['memory'] = undefined;

/**
 * @member {String} model
 */
DeviceModel.prototype['model'] = undefined;

/**
 * @member {String} name
 */
DeviceModel.prototype['name'] = undefined;

/**
 * @member {String} platform
 */
DeviceModel.prototype['platform'] = undefined;

/**
 * @member {String} releaseDate
 */
DeviceModel.prototype['releaseDate'] = undefined;

/**
 * @member {module:model/TestGetDeviceConfigurations200ResponseInnerModelResolution} resolution
 */
DeviceModel.prototype['resolution'] = undefined;

/**
 * @member {Number} screenRotation
 */
DeviceModel.prototype['screenRotation'] = undefined;

/**
 * @member {module:model/TestGetDeviceConfigurations200ResponseInnerModelScreenSize} screenSize
 */
DeviceModel.prototype['screenSize'] = undefined;






export default DeviceModel;

