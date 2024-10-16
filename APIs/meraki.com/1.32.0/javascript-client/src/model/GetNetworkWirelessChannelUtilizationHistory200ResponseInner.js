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
 * The GetNetworkWirelessChannelUtilizationHistory200ResponseInner model module.
 * @module model/GetNetworkWirelessChannelUtilizationHistory200ResponseInner
 * @version 1.32.0
 */
class GetNetworkWirelessChannelUtilizationHistory200ResponseInner {
    /**
     * Constructs a new <code>GetNetworkWirelessChannelUtilizationHistory200ResponseInner</code>.
     * @alias module:model/GetNetworkWirelessChannelUtilizationHistory200ResponseInner
     */
    constructor() { 
        
        GetNetworkWirelessChannelUtilizationHistory200ResponseInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>GetNetworkWirelessChannelUtilizationHistory200ResponseInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GetNetworkWirelessChannelUtilizationHistory200ResponseInner} obj Optional instance to populate.
     * @return {module:model/GetNetworkWirelessChannelUtilizationHistory200ResponseInner} The populated <code>GetNetworkWirelessChannelUtilizationHistory200ResponseInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GetNetworkWirelessChannelUtilizationHistory200ResponseInner();

            if (data.hasOwnProperty('endTs')) {
                obj['endTs'] = ApiClient.convertToType(data['endTs'], 'Date');
            }
            if (data.hasOwnProperty('startTs')) {
                obj['startTs'] = ApiClient.convertToType(data['startTs'], 'Date');
            }
            if (data.hasOwnProperty('utilization80211')) {
                obj['utilization80211'] = ApiClient.convertToType(data['utilization80211'], 'Number');
            }
            if (data.hasOwnProperty('utilizationNon80211')) {
                obj['utilizationNon80211'] = ApiClient.convertToType(data['utilizationNon80211'], 'Number');
            }
            if (data.hasOwnProperty('utilizationTotal')) {
                obj['utilizationTotal'] = ApiClient.convertToType(data['utilizationTotal'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GetNetworkWirelessChannelUtilizationHistory200ResponseInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GetNetworkWirelessChannelUtilizationHistory200ResponseInner</code>.
     */
    static validateJSON(data) {

        return true;
    }


}



/**
 * The end time of the query range
 * @member {Date} endTs
 */
GetNetworkWirelessChannelUtilizationHistory200ResponseInner.prototype['endTs'] = undefined;

/**
 * The start time of the query range
 * @member {Date} startTs
 */
GetNetworkWirelessChannelUtilizationHistory200ResponseInner.prototype['startTs'] = undefined;

/**
 * Average wifi utilization
 * @member {Number} utilization80211
 */
GetNetworkWirelessChannelUtilizationHistory200ResponseInner.prototype['utilization80211'] = undefined;

/**
 * Average signal interference
 * @member {Number} utilizationNon80211
 */
GetNetworkWirelessChannelUtilizationHistory200ResponseInner.prototype['utilizationNon80211'] = undefined;

/**
 * Total channel utilization
 * @member {Number} utilizationTotal
 */
GetNetworkWirelessChannelUtilizationHistory200ResponseInner.prototype['utilizationTotal'] = undefined;






export default GetNetworkWirelessChannelUtilizationHistory200ResponseInner;

