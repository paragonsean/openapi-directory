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
 * The UpdateOrganizationPolicyObjectsGroupRequest model module.
 * @module model/UpdateOrganizationPolicyObjectsGroupRequest
 * @version 1.32.0
 */
class UpdateOrganizationPolicyObjectsGroupRequest {
    /**
     * Constructs a new <code>UpdateOrganizationPolicyObjectsGroupRequest</code>.
     * @alias module:model/UpdateOrganizationPolicyObjectsGroupRequest
     */
    constructor() { 
        
        UpdateOrganizationPolicyObjectsGroupRequest.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>UpdateOrganizationPolicyObjectsGroupRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UpdateOrganizationPolicyObjectsGroupRequest} obj Optional instance to populate.
     * @return {module:model/UpdateOrganizationPolicyObjectsGroupRequest} The populated <code>UpdateOrganizationPolicyObjectsGroupRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UpdateOrganizationPolicyObjectsGroupRequest();

            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('objectIds')) {
                obj['objectIds'] = ApiClient.convertToType(data['objectIds'], ['Number']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UpdateOrganizationPolicyObjectsGroupRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UpdateOrganizationPolicyObjectsGroupRequest</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['objectIds'])) {
            throw new Error("Expected the field `objectIds` to be an array in the JSON data but got " + data['objectIds']);
        }

        return true;
    }


}



/**
 * A name for the group of network addresses, unique within the organization (alphanumeric, space, dash, or underscore characters only)
 * @member {String} name
 */
UpdateOrganizationPolicyObjectsGroupRequest.prototype['name'] = undefined;

/**
 * A list of Policy Object ID's that this NetworkObjectGroup should be associated to (note: these ID's will replace the existing associated Policy Objects)
 * @member {Array.<Number>} objectIds
 */
UpdateOrganizationPolicyObjectsGroupRequest.prototype['objectIds'] = undefined;






export default UpdateOrganizationPolicyObjectsGroupRequest;

