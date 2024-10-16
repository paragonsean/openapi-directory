/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 23 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 0.0.0-streaming
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import UpdateDeviceCellularGatewaySettingsRequestFixedIpAssignmentsInner from './UpdateDeviceCellularGatewaySettingsRequestFixedIpAssignmentsInner';
import UpdateDeviceCellularGatewaySettingsRequestReservedIpRangesInner from './UpdateDeviceCellularGatewaySettingsRequestReservedIpRangesInner';

/**
 * The UpdateDeviceCellularGatewaySettingsRequest model module.
 * @module model/UpdateDeviceCellularGatewaySettingsRequest
 * @version 0.0.0-streaming
 */
class UpdateDeviceCellularGatewaySettingsRequest {
    /**
     * Constructs a new <code>UpdateDeviceCellularGatewaySettingsRequest</code>.
     * @alias module:model/UpdateDeviceCellularGatewaySettingsRequest
     */
    constructor() { 
        
        UpdateDeviceCellularGatewaySettingsRequest.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>UpdateDeviceCellularGatewaySettingsRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UpdateDeviceCellularGatewaySettingsRequest} obj Optional instance to populate.
     * @return {module:model/UpdateDeviceCellularGatewaySettingsRequest} The populated <code>UpdateDeviceCellularGatewaySettingsRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UpdateDeviceCellularGatewaySettingsRequest();

            if (data.hasOwnProperty('fixedIpAssignments')) {
                obj['fixedIpAssignments'] = ApiClient.convertToType(data['fixedIpAssignments'], [UpdateDeviceCellularGatewaySettingsRequestFixedIpAssignmentsInner]);
            }
            if (data.hasOwnProperty('reservedIpRanges')) {
                obj['reservedIpRanges'] = ApiClient.convertToType(data['reservedIpRanges'], [UpdateDeviceCellularGatewaySettingsRequestReservedIpRangesInner]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UpdateDeviceCellularGatewaySettingsRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UpdateDeviceCellularGatewaySettingsRequest</code>.
     */
    static validateJSON(data) {
        if (data['fixedIpAssignments']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['fixedIpAssignments'])) {
                throw new Error("Expected the field `fixedIpAssignments` to be an array in the JSON data but got " + data['fixedIpAssignments']);
            }
            // validate the optional field `fixedIpAssignments` (array)
            for (const item of data['fixedIpAssignments']) {
                UpdateDeviceCellularGatewaySettingsRequestFixedIpAssignmentsInner.validateJSON(item);
            };
        }
        if (data['reservedIpRanges']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['reservedIpRanges'])) {
                throw new Error("Expected the field `reservedIpRanges` to be an array in the JSON data but got " + data['reservedIpRanges']);
            }
            // validate the optional field `reservedIpRanges` (array)
            for (const item of data['reservedIpRanges']) {
                UpdateDeviceCellularGatewaySettingsRequestReservedIpRangesInner.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * list of all fixed IP assignments for a single MG
 * @member {Array.<module:model/UpdateDeviceCellularGatewaySettingsRequestFixedIpAssignmentsInner>} fixedIpAssignments
 */
UpdateDeviceCellularGatewaySettingsRequest.prototype['fixedIpAssignments'] = undefined;

/**
 * list of all reserved IP ranges for a single MG
 * @member {Array.<module:model/UpdateDeviceCellularGatewaySettingsRequestReservedIpRangesInner>} reservedIpRanges
 */
UpdateDeviceCellularGatewaySettingsRequest.prototype['reservedIpRanges'] = undefined;






export default UpdateDeviceCellularGatewaySettingsRequest;

