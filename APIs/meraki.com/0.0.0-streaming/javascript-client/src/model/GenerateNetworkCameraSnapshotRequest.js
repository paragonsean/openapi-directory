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

/**
 * The GenerateNetworkCameraSnapshotRequest model module.
 * @module model/GenerateNetworkCameraSnapshotRequest
 * @version 0.0.0-streaming
 */
class GenerateNetworkCameraSnapshotRequest {
    /**
     * Constructs a new <code>GenerateNetworkCameraSnapshotRequest</code>.
     * @alias module:model/GenerateNetworkCameraSnapshotRequest
     */
    constructor() { 
        
        GenerateNetworkCameraSnapshotRequest.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>GenerateNetworkCameraSnapshotRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GenerateNetworkCameraSnapshotRequest} obj Optional instance to populate.
     * @return {module:model/GenerateNetworkCameraSnapshotRequest} The populated <code>GenerateNetworkCameraSnapshotRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GenerateNetworkCameraSnapshotRequest();

            if (data.hasOwnProperty('fullframe')) {
                obj['fullframe'] = ApiClient.convertToType(data['fullframe'], 'Boolean');
            }
            if (data.hasOwnProperty('timestamp')) {
                obj['timestamp'] = ApiClient.convertToType(data['timestamp'], 'Date');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GenerateNetworkCameraSnapshotRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GenerateNetworkCameraSnapshotRequest</code>.
     */
    static validateJSON(data) {

        return true;
    }


}



/**
 * [optional] If set to \"true\" the snapshot will be taken at full sensor resolution. This will error if used with timestamp.
 * @member {Boolean} fullframe
 */
GenerateNetworkCameraSnapshotRequest.prototype['fullframe'] = undefined;

/**
 * [optional] The snapshot will be taken from this time on the camera. The timestamp is expected to be in ISO 8601 format. If no timestamp is specified, we will assume current time.
 * @member {Date} timestamp
 */
GenerateNetworkCameraSnapshotRequest.prototype['timestamp'] = undefined;






export default GenerateNetworkCameraSnapshotRequest;

