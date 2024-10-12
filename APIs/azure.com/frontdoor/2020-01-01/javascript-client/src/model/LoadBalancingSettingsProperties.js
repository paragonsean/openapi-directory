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
import LoadBalancingSettingsUpdateParameters from './LoadBalancingSettingsUpdateParameters';
import ResourceState from './ResourceState';

/**
 * The LoadBalancingSettingsProperties model module.
 * @module model/LoadBalancingSettingsProperties
 * @version 2020-01-01
 */
class LoadBalancingSettingsProperties {
    /**
     * Constructs a new <code>LoadBalancingSettingsProperties</code>.
     * The JSON object that contains the properties required to create load balancing settings
     * @alias module:model/LoadBalancingSettingsProperties
     * @implements module:model/LoadBalancingSettingsUpdateParameters
     */
    constructor() { 
        LoadBalancingSettingsUpdateParameters.initialize(this);
        LoadBalancingSettingsProperties.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>LoadBalancingSettingsProperties</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/LoadBalancingSettingsProperties} obj Optional instance to populate.
     * @return {module:model/LoadBalancingSettingsProperties} The populated <code>LoadBalancingSettingsProperties</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new LoadBalancingSettingsProperties();
            LoadBalancingSettingsUpdateParameters.constructFromObject(data, obj);

            if (data.hasOwnProperty('resourceState')) {
                obj['resourceState'] = ResourceState.constructFromObject(data['resourceState']);
            }
            if (data.hasOwnProperty('additionalLatencyMilliseconds')) {
                obj['additionalLatencyMilliseconds'] = ApiClient.convertToType(data['additionalLatencyMilliseconds'], 'Number');
            }
            if (data.hasOwnProperty('sampleSize')) {
                obj['sampleSize'] = ApiClient.convertToType(data['sampleSize'], 'Number');
            }
            if (data.hasOwnProperty('successfulSamplesRequired')) {
                obj['successfulSamplesRequired'] = ApiClient.convertToType(data['successfulSamplesRequired'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>LoadBalancingSettingsProperties</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>LoadBalancingSettingsProperties</code>.
     */
    static validateJSON(data) {

        return true;
    }


}



/**
 * @member {module:model/ResourceState} resourceState
 */
LoadBalancingSettingsProperties.prototype['resourceState'] = undefined;

/**
 * The additional latency in milliseconds for probes to fall into the lowest latency bucket
 * @member {Number} additionalLatencyMilliseconds
 */
LoadBalancingSettingsProperties.prototype['additionalLatencyMilliseconds'] = undefined;

/**
 * The number of samples to consider for load balancing decisions
 * @member {Number} sampleSize
 */
LoadBalancingSettingsProperties.prototype['sampleSize'] = undefined;

/**
 * The number of samples within the sample period that must succeed
 * @member {Number} successfulSamplesRequired
 */
LoadBalancingSettingsProperties.prototype['successfulSamplesRequired'] = undefined;


// Implement LoadBalancingSettingsUpdateParameters interface:
/**
 * The additional latency in milliseconds for probes to fall into the lowest latency bucket
 * @member {Number} additionalLatencyMilliseconds
 */
LoadBalancingSettingsUpdateParameters.prototype['additionalLatencyMilliseconds'] = undefined;
/**
 * The number of samples to consider for load balancing decisions
 * @member {Number} sampleSize
 */
LoadBalancingSettingsUpdateParameters.prototype['sampleSize'] = undefined;
/**
 * The number of samples within the sample period that must succeed
 * @member {Number} successfulSamplesRequired
 */
LoadBalancingSettingsUpdateParameters.prototype['successfulSamplesRequired'] = undefined;




export default LoadBalancingSettingsProperties;

