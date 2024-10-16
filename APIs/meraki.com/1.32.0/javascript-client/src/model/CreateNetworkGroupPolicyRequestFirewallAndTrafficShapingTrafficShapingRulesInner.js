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
import UpdateNetworkApplianceTrafficShapingRulesRequestRulesInnerDefinitionsInner from './UpdateNetworkApplianceTrafficShapingRulesRequestRulesInnerDefinitionsInner';
import UpdateNetworkApplianceTrafficShapingRulesRequestRulesInnerPerClientBandwidthLimits from './UpdateNetworkApplianceTrafficShapingRulesRequestRulesInnerPerClientBandwidthLimits';

/**
 * The CreateNetworkGroupPolicyRequestFirewallAndTrafficShapingTrafficShapingRulesInner model module.
 * @module model/CreateNetworkGroupPolicyRequestFirewallAndTrafficShapingTrafficShapingRulesInner
 * @version 1.32.0
 */
class CreateNetworkGroupPolicyRequestFirewallAndTrafficShapingTrafficShapingRulesInner {
    /**
     * Constructs a new <code>CreateNetworkGroupPolicyRequestFirewallAndTrafficShapingTrafficShapingRulesInner</code>.
     * @alias module:model/CreateNetworkGroupPolicyRequestFirewallAndTrafficShapingTrafficShapingRulesInner
     * @param definitions {Array.<module:model/UpdateNetworkApplianceTrafficShapingRulesRequestRulesInnerDefinitionsInner>}     A list of objects describing the definitions of your traffic shaping rule. At least one definition is required. 
     */
    constructor(definitions) { 
        
        CreateNetworkGroupPolicyRequestFirewallAndTrafficShapingTrafficShapingRulesInner.initialize(this, definitions);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, definitions) { 
        obj['definitions'] = definitions;
    }

    /**
     * Constructs a <code>CreateNetworkGroupPolicyRequestFirewallAndTrafficShapingTrafficShapingRulesInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CreateNetworkGroupPolicyRequestFirewallAndTrafficShapingTrafficShapingRulesInner} obj Optional instance to populate.
     * @return {module:model/CreateNetworkGroupPolicyRequestFirewallAndTrafficShapingTrafficShapingRulesInner} The populated <code>CreateNetworkGroupPolicyRequestFirewallAndTrafficShapingTrafficShapingRulesInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CreateNetworkGroupPolicyRequestFirewallAndTrafficShapingTrafficShapingRulesInner();

            if (data.hasOwnProperty('definitions')) {
                obj['definitions'] = ApiClient.convertToType(data['definitions'], [UpdateNetworkApplianceTrafficShapingRulesRequestRulesInnerDefinitionsInner]);
            }
            if (data.hasOwnProperty('dscpTagValue')) {
                obj['dscpTagValue'] = ApiClient.convertToType(data['dscpTagValue'], 'Number');
            }
            if (data.hasOwnProperty('pcpTagValue')) {
                obj['pcpTagValue'] = ApiClient.convertToType(data['pcpTagValue'], 'Number');
            }
            if (data.hasOwnProperty('perClientBandwidthLimits')) {
                obj['perClientBandwidthLimits'] = UpdateNetworkApplianceTrafficShapingRulesRequestRulesInnerPerClientBandwidthLimits.constructFromObject(data['perClientBandwidthLimits']);
            }
            if (data.hasOwnProperty('priority')) {
                obj['priority'] = ApiClient.convertToType(data['priority'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CreateNetworkGroupPolicyRequestFirewallAndTrafficShapingTrafficShapingRulesInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CreateNetworkGroupPolicyRequestFirewallAndTrafficShapingTrafficShapingRulesInner</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of CreateNetworkGroupPolicyRequestFirewallAndTrafficShapingTrafficShapingRulesInner.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        if (data['definitions']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['definitions'])) {
                throw new Error("Expected the field `definitions` to be an array in the JSON data but got " + data['definitions']);
            }
            // validate the optional field `definitions` (array)
            for (const item of data['definitions']) {
                UpdateNetworkApplianceTrafficShapingRulesRequestRulesInnerDefinitionsInner.validateJSON(item);
            };
        }
        // validate the optional field `perClientBandwidthLimits`
        if (data['perClientBandwidthLimits']) { // data not null
          UpdateNetworkApplianceTrafficShapingRulesRequestRulesInnerPerClientBandwidthLimits.validateJSON(data['perClientBandwidthLimits']);
        }
        // ensure the json data is a string
        if (data['priority'] && !(typeof data['priority'] === 'string' || data['priority'] instanceof String)) {
            throw new Error("Expected the field `priority` to be a primitive type in the JSON string but got " + data['priority']);
        }

        return true;
    }


}

CreateNetworkGroupPolicyRequestFirewallAndTrafficShapingTrafficShapingRulesInner.RequiredProperties = ["definitions"];

/**
 *     A list of objects describing the definitions of your traffic shaping rule. At least one definition is required. 
 * @member {Array.<module:model/UpdateNetworkApplianceTrafficShapingRulesRequestRulesInnerDefinitionsInner>} definitions
 */
CreateNetworkGroupPolicyRequestFirewallAndTrafficShapingTrafficShapingRulesInner.prototype['definitions'] = undefined;

/**
 *     The DSCP tag applied by your rule. null means 'Do not change DSCP tag'.     For a list of possible tag values, use the trafficShaping/dscpTaggingOptions endpoint. 
 * @member {Number} dscpTagValue
 */
CreateNetworkGroupPolicyRequestFirewallAndTrafficShapingTrafficShapingRulesInner.prototype['dscpTagValue'] = undefined;

/**
 *     The PCP tag applied by your rule. Can be 0 (lowest priority) through 7 (highest priority).     null means 'Do not set PCP tag'. 
 * @member {Number} pcpTagValue
 */
CreateNetworkGroupPolicyRequestFirewallAndTrafficShapingTrafficShapingRulesInner.prototype['pcpTagValue'] = undefined;

/**
 * @member {module:model/UpdateNetworkApplianceTrafficShapingRulesRequestRulesInnerPerClientBandwidthLimits} perClientBandwidthLimits
 */
CreateNetworkGroupPolicyRequestFirewallAndTrafficShapingTrafficShapingRulesInner.prototype['perClientBandwidthLimits'] = undefined;

/**
 *     A string, indicating the priority level for packets bound to your rule.     Can be 'low', 'normal' or 'high'. 
 * @member {String} priority
 */
CreateNetworkGroupPolicyRequestFirewallAndTrafficShapingTrafficShapingRulesInner.prototype['priority'] = undefined;






export default CreateNetworkGroupPolicyRequestFirewallAndTrafficShapingTrafficShapingRulesInner;

