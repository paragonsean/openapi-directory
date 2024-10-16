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
 * The CreateNetworkGroupPolicyRequestBandwidthBandwidthLimits model module.
 * @module model/CreateNetworkGroupPolicyRequestBandwidthBandwidthLimits
 * @version 1.32.0
 */
class CreateNetworkGroupPolicyRequestBandwidthBandwidthLimits {
    /**
     * Constructs a new <code>CreateNetworkGroupPolicyRequestBandwidthBandwidthLimits</code>.
     * The bandwidth limits object, specifying upload and download speed for clients bound to the group policy. These are only enforced if &#39;settings&#39; is set to &#39;custom&#39;.
     * @alias module:model/CreateNetworkGroupPolicyRequestBandwidthBandwidthLimits
     */
    constructor() { 
        
        CreateNetworkGroupPolicyRequestBandwidthBandwidthLimits.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>CreateNetworkGroupPolicyRequestBandwidthBandwidthLimits</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CreateNetworkGroupPolicyRequestBandwidthBandwidthLimits} obj Optional instance to populate.
     * @return {module:model/CreateNetworkGroupPolicyRequestBandwidthBandwidthLimits} The populated <code>CreateNetworkGroupPolicyRequestBandwidthBandwidthLimits</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CreateNetworkGroupPolicyRequestBandwidthBandwidthLimits();

            if (data.hasOwnProperty('limitDown')) {
                obj['limitDown'] = ApiClient.convertToType(data['limitDown'], 'Number');
            }
            if (data.hasOwnProperty('limitUp')) {
                obj['limitUp'] = ApiClient.convertToType(data['limitUp'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CreateNetworkGroupPolicyRequestBandwidthBandwidthLimits</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CreateNetworkGroupPolicyRequestBandwidthBandwidthLimits</code>.
     */
    static validateJSON(data) {

        return true;
    }


}



/**
 * The maximum download limit (integer, in Kbps). null indicates no limit
 * @member {Number} limitDown
 */
CreateNetworkGroupPolicyRequestBandwidthBandwidthLimits.prototype['limitDown'] = undefined;

/**
 * The maximum upload limit (integer, in Kbps). null indicates no limit
 * @member {Number} limitUp
 */
CreateNetworkGroupPolicyRequestBandwidthBandwidthLimits.prototype['limitUp'] = undefined;






export default CreateNetworkGroupPolicyRequestBandwidthBandwidthLimits;

