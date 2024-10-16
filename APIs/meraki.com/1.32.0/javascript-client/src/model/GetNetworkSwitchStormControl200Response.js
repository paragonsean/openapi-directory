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
 * The GetNetworkSwitchStormControl200Response model module.
 * @module model/GetNetworkSwitchStormControl200Response
 * @version 1.32.0
 */
class GetNetworkSwitchStormControl200Response {
    /**
     * Constructs a new <code>GetNetworkSwitchStormControl200Response</code>.
     * @alias module:model/GetNetworkSwitchStormControl200Response
     */
    constructor() { 
        
        GetNetworkSwitchStormControl200Response.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>GetNetworkSwitchStormControl200Response</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GetNetworkSwitchStormControl200Response} obj Optional instance to populate.
     * @return {module:model/GetNetworkSwitchStormControl200Response} The populated <code>GetNetworkSwitchStormControl200Response</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GetNetworkSwitchStormControl200Response();

            if (data.hasOwnProperty('broadcastThreshold')) {
                obj['broadcastThreshold'] = ApiClient.convertToType(data['broadcastThreshold'], 'Number');
            }
            if (data.hasOwnProperty('multicastThreshold')) {
                obj['multicastThreshold'] = ApiClient.convertToType(data['multicastThreshold'], 'Number');
            }
            if (data.hasOwnProperty('unknownUnicastThreshold')) {
                obj['unknownUnicastThreshold'] = ApiClient.convertToType(data['unknownUnicastThreshold'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GetNetworkSwitchStormControl200Response</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GetNetworkSwitchStormControl200Response</code>.
     */
    static validateJSON(data) {

        return true;
    }


}



/**
 * Broadcast threshold.
 * @member {Number} broadcastThreshold
 */
GetNetworkSwitchStormControl200Response.prototype['broadcastThreshold'] = undefined;

/**
 * Multicast threshold.
 * @member {Number} multicastThreshold
 */
GetNetworkSwitchStormControl200Response.prototype['multicastThreshold'] = undefined;

/**
 * Unknown Unicast threshold.
 * @member {Number} unknownUnicastThreshold
 */
GetNetworkSwitchStormControl200Response.prototype['unknownUnicastThreshold'] = undefined;






export default GetNetworkSwitchStormControl200Response;

