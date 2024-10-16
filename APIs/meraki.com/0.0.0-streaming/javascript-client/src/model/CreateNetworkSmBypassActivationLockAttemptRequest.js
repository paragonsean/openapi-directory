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
 * The CreateNetworkSmBypassActivationLockAttemptRequest model module.
 * @module model/CreateNetworkSmBypassActivationLockAttemptRequest
 * @version 0.0.0-streaming
 */
class CreateNetworkSmBypassActivationLockAttemptRequest {
    /**
     * Constructs a new <code>CreateNetworkSmBypassActivationLockAttemptRequest</code>.
     * @alias module:model/CreateNetworkSmBypassActivationLockAttemptRequest
     * @param ids {Array.<String>} The ids of the devices to attempt activation lock bypass.
     */
    constructor(ids) { 
        
        CreateNetworkSmBypassActivationLockAttemptRequest.initialize(this, ids);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, ids) { 
        obj['ids'] = ids;
    }

    /**
     * Constructs a <code>CreateNetworkSmBypassActivationLockAttemptRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CreateNetworkSmBypassActivationLockAttemptRequest} obj Optional instance to populate.
     * @return {module:model/CreateNetworkSmBypassActivationLockAttemptRequest} The populated <code>CreateNetworkSmBypassActivationLockAttemptRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CreateNetworkSmBypassActivationLockAttemptRequest();

            if (data.hasOwnProperty('ids')) {
                obj['ids'] = ApiClient.convertToType(data['ids'], ['String']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CreateNetworkSmBypassActivationLockAttemptRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CreateNetworkSmBypassActivationLockAttemptRequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of CreateNetworkSmBypassActivationLockAttemptRequest.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is an array
        if (!Array.isArray(data['ids'])) {
            throw new Error("Expected the field `ids` to be an array in the JSON data but got " + data['ids']);
        }

        return true;
    }


}

CreateNetworkSmBypassActivationLockAttemptRequest.RequiredProperties = ["ids"];

/**
 * The ids of the devices to attempt activation lock bypass.
 * @member {Array.<String>} ids
 */
CreateNetworkSmBypassActivationLockAttemptRequest.prototype['ids'] = undefined;






export default CreateNetworkSmBypassActivationLockAttemptRequest;

