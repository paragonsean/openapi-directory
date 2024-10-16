/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The GetNetworkSmDevicePerformanceHistory200ResponseInnerDiskUsageC model module.
 * @module model/GetNetworkSmDevicePerformanceHistory200ResponseInnerDiskUsageC
 * @version 1.32.0
 */
class GetNetworkSmDevicePerformanceHistory200ResponseInnerDiskUsageC {
    /**
     * Constructs a new <code>GetNetworkSmDevicePerformanceHistory200ResponseInnerDiskUsageC</code>.
     * An object containing current disk usage details.
     * @alias module:model/GetNetworkSmDevicePerformanceHistory200ResponseInnerDiskUsageC
     */
    constructor() { 
        
        GetNetworkSmDevicePerformanceHistory200ResponseInnerDiskUsageC.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>GetNetworkSmDevicePerformanceHistory200ResponseInnerDiskUsageC</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GetNetworkSmDevicePerformanceHistory200ResponseInnerDiskUsageC} obj Optional instance to populate.
     * @return {module:model/GetNetworkSmDevicePerformanceHistory200ResponseInnerDiskUsageC} The populated <code>GetNetworkSmDevicePerformanceHistory200ResponseInnerDiskUsageC</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GetNetworkSmDevicePerformanceHistory200ResponseInnerDiskUsageC();

            if (data.hasOwnProperty('space')) {
                obj['space'] = ApiClient.convertToType(data['space'], 'Number');
            }
            if (data.hasOwnProperty('used')) {
                obj['used'] = ApiClient.convertToType(data['used'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GetNetworkSmDevicePerformanceHistory200ResponseInnerDiskUsageC</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GetNetworkSmDevicePerformanceHistory200ResponseInnerDiskUsageC</code>.
     */
    static validateJSON(data) {

        return true;
    }


}



/**
 * The available disk space.
 * @member {Number} space
 */
GetNetworkSmDevicePerformanceHistory200ResponseInnerDiskUsageC.prototype['space'] = undefined;

/**
 * The used disk space.
 * @member {Number} used
 */
GetNetworkSmDevicePerformanceHistory200ResponseInnerDiskUsageC.prototype['used'] = undefined;






export default GetNetworkSmDevicePerformanceHistory200ResponseInnerDiskUsageC;

