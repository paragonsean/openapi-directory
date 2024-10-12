/**
 * FrontDoorManagementClient
 * Use these APIs to manage Azure Front Door resources through the Azure Resource Manager. You must make sure that requests made to these resources are secure.
 *
 * The version of the OpenAPI document: 2020-01-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The HealthProbeSettingsUpdateParameters model module.
 * @module model/HealthProbeSettingsUpdateParameters
 * @version 2020-01-01
 */
class HealthProbeSettingsUpdateParameters {
    /**
     * Constructs a new <code>HealthProbeSettingsUpdateParameters</code>.
     * L7 health probe settings for a backend pool
     * @alias module:model/HealthProbeSettingsUpdateParameters
     */
    constructor() { 
        
        HealthProbeSettingsUpdateParameters.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
        obj['healthProbeMethod'] = 'HEAD';
    }

    /**
     * Constructs a <code>HealthProbeSettingsUpdateParameters</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/HealthProbeSettingsUpdateParameters} obj Optional instance to populate.
     * @return {module:model/HealthProbeSettingsUpdateParameters} The populated <code>HealthProbeSettingsUpdateParameters</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new HealthProbeSettingsUpdateParameters();

            if (data.hasOwnProperty('enabledState')) {
                obj['enabledState'] = ApiClient.convertToType(data['enabledState'], 'String');
            }
            if (data.hasOwnProperty('healthProbeMethod')) {
                obj['healthProbeMethod'] = ApiClient.convertToType(data['healthProbeMethod'], 'String');
            }
            if (data.hasOwnProperty('intervalInSeconds')) {
                obj['intervalInSeconds'] = ApiClient.convertToType(data['intervalInSeconds'], 'Number');
            }
            if (data.hasOwnProperty('path')) {
                obj['path'] = ApiClient.convertToType(data['path'], 'String');
            }
            if (data.hasOwnProperty('protocol')) {
                obj['protocol'] = ApiClient.convertToType(data['protocol'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>HealthProbeSettingsUpdateParameters</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>HealthProbeSettingsUpdateParameters</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['enabledState'] && !(typeof data['enabledState'] === 'string' || data['enabledState'] instanceof String)) {
            throw new Error("Expected the field `enabledState` to be a primitive type in the JSON string but got " + data['enabledState']);
        }
        // ensure the json data is a string
        if (data['healthProbeMethod'] && !(typeof data['healthProbeMethod'] === 'string' || data['healthProbeMethod'] instanceof String)) {
            throw new Error("Expected the field `healthProbeMethod` to be a primitive type in the JSON string but got " + data['healthProbeMethod']);
        }
        // ensure the json data is a string
        if (data['path'] && !(typeof data['path'] === 'string' || data['path'] instanceof String)) {
            throw new Error("Expected the field `path` to be a primitive type in the JSON string but got " + data['path']);
        }
        // ensure the json data is a string
        if (data['protocol'] && !(typeof data['protocol'] === 'string' || data['protocol'] instanceof String)) {
            throw new Error("Expected the field `protocol` to be a primitive type in the JSON string but got " + data['protocol']);
        }

        return true;
    }


}



/**
 * Whether to enable health probes to be made against backends defined under backendPools. Health probes can only be disabled if there is a single enabled backend in single enabled backend pool.
 * @member {module:model/HealthProbeSettingsUpdateParameters.EnabledStateEnum} enabledState
 */
HealthProbeSettingsUpdateParameters.prototype['enabledState'] = undefined;

/**
 * Configures which HTTP method to use to probe the backends defined under backendPools.
 * @member {module:model/HealthProbeSettingsUpdateParameters.HealthProbeMethodEnum} healthProbeMethod
 * @default 'HEAD'
 */
HealthProbeSettingsUpdateParameters.prototype['healthProbeMethod'] = 'HEAD';

/**
 * The number of seconds between health probes.
 * @member {Number} intervalInSeconds
 */
HealthProbeSettingsUpdateParameters.prototype['intervalInSeconds'] = undefined;

/**
 * The path to use for the health probe. Default is /
 * @member {String} path
 */
HealthProbeSettingsUpdateParameters.prototype['path'] = undefined;

/**
 * Protocol scheme to use for this probe
 * @member {module:model/HealthProbeSettingsUpdateParameters.ProtocolEnum} protocol
 */
HealthProbeSettingsUpdateParameters.prototype['protocol'] = undefined;





/**
 * Allowed values for the <code>enabledState</code> property.
 * @enum {String}
 * @readonly
 */
HealthProbeSettingsUpdateParameters['EnabledStateEnum'] = {

    /**
     * value: "Enabled"
     * @const
     */
    "Enabled": "Enabled",

    /**
     * value: "Disabled"
     * @const
     */
    "Disabled": "Disabled"
};


/**
 * Allowed values for the <code>healthProbeMethod</code> property.
 * @enum {String}
 * @readonly
 */
HealthProbeSettingsUpdateParameters['HealthProbeMethodEnum'] = {

    /**
     * value: "GET"
     * @const
     */
    "GET": "GET",

    /**
     * value: "HEAD"
     * @const
     */
    "HEAD": "HEAD"
};


/**
 * Allowed values for the <code>protocol</code> property.
 * @enum {String}
 * @readonly
 */
HealthProbeSettingsUpdateParameters['ProtocolEnum'] = {

    /**
     * value: "Http"
     * @const
     */
    "Http": "Http",

    /**
     * value: "Https"
     * @const
     */
    "Https": "Https"
};



export default HealthProbeSettingsUpdateParameters;

