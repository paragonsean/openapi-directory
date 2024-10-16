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
import GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerPerformanceClass from './GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerPerformanceClass';
import GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerTrafficFiltersInner from './GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerTrafficFiltersInner';

/**
 * The GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner model module.
 * @module model/GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner
 * @version 1.32.0
 */
class GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner {
    /**
     * Constructs a new <code>GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner</code>.
     * @alias module:model/GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner
     * @param preferredUplink {module:model/GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner.PreferredUplinkEnum} Preferred uplink for uplink preference rule. Must be one of: 'wan1', 'wan2', 'bestForVoIP', 'loadBalancing' or 'defaultUplink'
     * @param trafficFilters {Array.<module:model/GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerTrafficFiltersInner>} Traffic filters
     */
    constructor(preferredUplink, trafficFilters) { 
        
        GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner.initialize(this, preferredUplink, trafficFilters);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, preferredUplink, trafficFilters) { 
        obj['preferredUplink'] = preferredUplink;
        obj['trafficFilters'] = trafficFilters;
    }

    /**
     * Constructs a <code>GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner} obj Optional instance to populate.
     * @return {module:model/GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner} The populated <code>GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner();

            if (data.hasOwnProperty('failOverCriterion')) {
                obj['failOverCriterion'] = ApiClient.convertToType(data['failOverCriterion'], 'String');
            }
            if (data.hasOwnProperty('performanceClass')) {
                obj['performanceClass'] = GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerPerformanceClass.constructFromObject(data['performanceClass']);
            }
            if (data.hasOwnProperty('preferredUplink')) {
                obj['preferredUplink'] = ApiClient.convertToType(data['preferredUplink'], 'String');
            }
            if (data.hasOwnProperty('trafficFilters')) {
                obj['trafficFilters'] = ApiClient.convertToType(data['trafficFilters'], [GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerTrafficFiltersInner]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['failOverCriterion'] && !(typeof data['failOverCriterion'] === 'string' || data['failOverCriterion'] instanceof String)) {
            throw new Error("Expected the field `failOverCriterion` to be a primitive type in the JSON string but got " + data['failOverCriterion']);
        }
        // validate the optional field `performanceClass`
        if (data['performanceClass']) { // data not null
          GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerPerformanceClass.validateJSON(data['performanceClass']);
        }
        // ensure the json data is a string
        if (data['preferredUplink'] && !(typeof data['preferredUplink'] === 'string' || data['preferredUplink'] instanceof String)) {
            throw new Error("Expected the field `preferredUplink` to be a primitive type in the JSON string but got " + data['preferredUplink']);
        }
        if (data['trafficFilters']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['trafficFilters'])) {
                throw new Error("Expected the field `trafficFilters` to be an array in the JSON data but got " + data['trafficFilters']);
            }
            // validate the optional field `trafficFilters` (array)
            for (const item of data['trafficFilters']) {
                GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerTrafficFiltersInner.validateJSON(item);
            };
        }

        return true;
    }


}

GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner.RequiredProperties = ["preferredUplink", "trafficFilters"];

/**
 * Fail over criterion for uplink preference rule. Must be one of: 'poorPerformance' or 'uplinkDown'
 * @member {module:model/GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner.FailOverCriterionEnum} failOverCriterion
 */
GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner.prototype['failOverCriterion'] = undefined;

/**
 * @member {module:model/GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerPerformanceClass} performanceClass
 */
GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner.prototype['performanceClass'] = undefined;

/**
 * Preferred uplink for uplink preference rule. Must be one of: 'wan1', 'wan2', 'bestForVoIP', 'loadBalancing' or 'defaultUplink'
 * @member {module:model/GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner.PreferredUplinkEnum} preferredUplink
 */
GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner.prototype['preferredUplink'] = undefined;

/**
 * Traffic filters
 * @member {Array.<module:model/GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerTrafficFiltersInner>} trafficFilters
 */
GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner.prototype['trafficFilters'] = undefined;





/**
 * Allowed values for the <code>failOverCriterion</code> property.
 * @enum {String}
 * @readonly
 */
GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner['FailOverCriterionEnum'] = {

    /**
     * value: "poorPerformance"
     * @const
     */
    "poorPerformance": "poorPerformance",

    /**
     * value: "uplinkDown"
     * @const
     */
    "uplinkDown": "uplinkDown"
};


/**
 * Allowed values for the <code>preferredUplink</code> property.
 * @enum {String}
 * @readonly
 */
GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner['PreferredUplinkEnum'] = {

    /**
     * value: "bestForVoIP"
     * @const
     */
    "bestForVoIP": "bestForVoIP",

    /**
     * value: "defaultUplink"
     * @const
     */
    "defaultUplink": "defaultUplink",

    /**
     * value: "loadBalancing"
     * @const
     */
    "loadBalancing": "loadBalancing",

    /**
     * value: "wan1"
     * @const
     */
    "wan1": "wan1",

    /**
     * value: "wan2"
     * @const
     */
    "wan2": "wan2"
};



export default GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner;

