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
import UpdateNetworkCellularGatewayConnectivityMonitoringDestinationsRequestDestinationsInner from './UpdateNetworkCellularGatewayConnectivityMonitoringDestinationsRequestDestinationsInner';

/**
 * The UpdateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest model module.
 * @module model/UpdateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest
 * @version 1.32.0
 */
class UpdateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest {
    /**
     * Constructs a new <code>UpdateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest</code>.
     * @alias module:model/UpdateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest
     */
    constructor() { 
        
        UpdateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>UpdateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UpdateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest} obj Optional instance to populate.
     * @return {module:model/UpdateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest} The populated <code>UpdateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UpdateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest();

            if (data.hasOwnProperty('destinations')) {
                obj['destinations'] = ApiClient.convertToType(data['destinations'], [UpdateNetworkCellularGatewayConnectivityMonitoringDestinationsRequestDestinationsInner]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UpdateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UpdateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest</code>.
     */
    static validateJSON(data) {
        if (data['destinations']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['destinations'])) {
                throw new Error("Expected the field `destinations` to be an array in the JSON data but got " + data['destinations']);
            }
            // validate the optional field `destinations` (array)
            for (const item of data['destinations']) {
                UpdateNetworkCellularGatewayConnectivityMonitoringDestinationsRequestDestinationsInner.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * The list of connectivity monitoring destinations
 * @member {Array.<module:model/UpdateNetworkCellularGatewayConnectivityMonitoringDestinationsRequestDestinationsInner>} destinations
 */
UpdateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest.prototype['destinations'] = undefined;






export default UpdateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest;

