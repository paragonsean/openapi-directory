/**
 * FrontDoorManagementClient
 * Use these APIs to manage Azure Front Door resources through the Azure Resource Manager. You must make sure that requests made to these resources are secure.
 *
 * The version of the OpenAPI document: 2019-05-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import BackendPool from './BackendPool';
import BackendPoolsSettings from './BackendPoolsSettings';
import FrontendEndpoint from './FrontendEndpoint';
import HealthProbeSettingsModel from './HealthProbeSettingsModel';
import LoadBalancingSettingsModel from './LoadBalancingSettingsModel';
import RoutingRule from './RoutingRule';

/**
 * The FrontDoorUpdateParameters model module.
 * @module model/FrontDoorUpdateParameters
 * @version 2019-05-01
 */
class FrontDoorUpdateParameters {
    /**
     * Constructs a new <code>FrontDoorUpdateParameters</code>.
     * The properties needed to update a Front Door
     * @alias module:model/FrontDoorUpdateParameters
     */
    constructor() { 
        
        FrontDoorUpdateParameters.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>FrontDoorUpdateParameters</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/FrontDoorUpdateParameters} obj Optional instance to populate.
     * @return {module:model/FrontDoorUpdateParameters} The populated <code>FrontDoorUpdateParameters</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new FrontDoorUpdateParameters();

            if (data.hasOwnProperty('backendPools')) {
                obj['backendPools'] = ApiClient.convertToType(data['backendPools'], [BackendPool]);
            }
            if (data.hasOwnProperty('backendPoolsSettings')) {
                obj['backendPoolsSettings'] = BackendPoolsSettings.constructFromObject(data['backendPoolsSettings']);
            }
            if (data.hasOwnProperty('enabledState')) {
                obj['enabledState'] = ApiClient.convertToType(data['enabledState'], 'String');
            }
            if (data.hasOwnProperty('friendlyName')) {
                obj['friendlyName'] = ApiClient.convertToType(data['friendlyName'], 'String');
            }
            if (data.hasOwnProperty('frontendEndpoints')) {
                obj['frontendEndpoints'] = ApiClient.convertToType(data['frontendEndpoints'], [FrontendEndpoint]);
            }
            if (data.hasOwnProperty('healthProbeSettings')) {
                obj['healthProbeSettings'] = ApiClient.convertToType(data['healthProbeSettings'], [HealthProbeSettingsModel]);
            }
            if (data.hasOwnProperty('loadBalancingSettings')) {
                obj['loadBalancingSettings'] = ApiClient.convertToType(data['loadBalancingSettings'], [LoadBalancingSettingsModel]);
            }
            if (data.hasOwnProperty('routingRules')) {
                obj['routingRules'] = ApiClient.convertToType(data['routingRules'], [RoutingRule]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>FrontDoorUpdateParameters</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>FrontDoorUpdateParameters</code>.
     */
    static validateJSON(data) {
        if (data['backendPools']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['backendPools'])) {
                throw new Error("Expected the field `backendPools` to be an array in the JSON data but got " + data['backendPools']);
            }
            // validate the optional field `backendPools` (array)
            for (const item of data['backendPools']) {
                BackendPool.validateJSON(item);
            };
        }
        // validate the optional field `backendPoolsSettings`
        if (data['backendPoolsSettings']) { // data not null
          BackendPoolsSettings.validateJSON(data['backendPoolsSettings']);
        }
        // ensure the json data is a string
        if (data['enabledState'] && !(typeof data['enabledState'] === 'string' || data['enabledState'] instanceof String)) {
            throw new Error("Expected the field `enabledState` to be a primitive type in the JSON string but got " + data['enabledState']);
        }
        // ensure the json data is a string
        if (data['friendlyName'] && !(typeof data['friendlyName'] === 'string' || data['friendlyName'] instanceof String)) {
            throw new Error("Expected the field `friendlyName` to be a primitive type in the JSON string but got " + data['friendlyName']);
        }
        if (data['frontendEndpoints']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['frontendEndpoints'])) {
                throw new Error("Expected the field `frontendEndpoints` to be an array in the JSON data but got " + data['frontendEndpoints']);
            }
            // validate the optional field `frontendEndpoints` (array)
            for (const item of data['frontendEndpoints']) {
                FrontendEndpoint.validateJSON(item);
            };
        }
        if (data['healthProbeSettings']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['healthProbeSettings'])) {
                throw new Error("Expected the field `healthProbeSettings` to be an array in the JSON data but got " + data['healthProbeSettings']);
            }
            // validate the optional field `healthProbeSettings` (array)
            for (const item of data['healthProbeSettings']) {
                HealthProbeSettingsModel.validateJSON(item);
            };
        }
        if (data['loadBalancingSettings']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['loadBalancingSettings'])) {
                throw new Error("Expected the field `loadBalancingSettings` to be an array in the JSON data but got " + data['loadBalancingSettings']);
            }
            // validate the optional field `loadBalancingSettings` (array)
            for (const item of data['loadBalancingSettings']) {
                LoadBalancingSettingsModel.validateJSON(item);
            };
        }
        if (data['routingRules']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['routingRules'])) {
                throw new Error("Expected the field `routingRules` to be an array in the JSON data but got " + data['routingRules']);
            }
            // validate the optional field `routingRules` (array)
            for (const item of data['routingRules']) {
                RoutingRule.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * Backend pools available to routing rules.
 * @member {Array.<module:model/BackendPool>} backendPools
 */
FrontDoorUpdateParameters.prototype['backendPools'] = undefined;

/**
 * @member {module:model/BackendPoolsSettings} backendPoolsSettings
 */
FrontDoorUpdateParameters.prototype['backendPoolsSettings'] = undefined;

/**
 * Operational status of the Front Door load balancer. Permitted values are 'Enabled' or 'Disabled'
 * @member {module:model/FrontDoorUpdateParameters.EnabledStateEnum} enabledState
 */
FrontDoorUpdateParameters.prototype['enabledState'] = undefined;

/**
 * A friendly name for the frontDoor
 * @member {String} friendlyName
 */
FrontDoorUpdateParameters.prototype['friendlyName'] = undefined;

/**
 * Frontend endpoints available to routing rules.
 * @member {Array.<module:model/FrontendEndpoint>} frontendEndpoints
 */
FrontDoorUpdateParameters.prototype['frontendEndpoints'] = undefined;

/**
 * Health probe settings associated with this Front Door instance.
 * @member {Array.<module:model/HealthProbeSettingsModel>} healthProbeSettings
 */
FrontDoorUpdateParameters.prototype['healthProbeSettings'] = undefined;

/**
 * Load balancing settings associated with this Front Door instance.
 * @member {Array.<module:model/LoadBalancingSettingsModel>} loadBalancingSettings
 */
FrontDoorUpdateParameters.prototype['loadBalancingSettings'] = undefined;

/**
 * Routing rules associated with this Front Door.
 * @member {Array.<module:model/RoutingRule>} routingRules
 */
FrontDoorUpdateParameters.prototype['routingRules'] = undefined;





/**
 * Allowed values for the <code>enabledState</code> property.
 * @enum {String}
 * @readonly
 */
FrontDoorUpdateParameters['EnabledStateEnum'] = {

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



export default FrontDoorUpdateParameters;

