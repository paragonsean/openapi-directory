/**
 * ManagedNetworkManagementClient
 * The Microsoft Azure Managed Network management API provides a RESTful set of web services that interact with Microsoft Azure Networks service to programmatically view, control, change, and monitor your entire Azure network centrally and with ease.
 *
 * The version of the OpenAPI document: 2019-06-01-preview
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import ManagedNetworkPeeringPolicyProperties from './ManagedNetworkPeeringPolicyProperties';
import ProxyResource from './ProxyResource';

/**
 * The ManagedNetworkPeeringPolicy model module.
 * @module model/ManagedNetworkPeeringPolicy
 * @version 2019-06-01-preview
 */
class ManagedNetworkPeeringPolicy {
    /**
     * Constructs a new <code>ManagedNetworkPeeringPolicy</code>.
     * The Managed Network Peering Policy resource
     * @alias module:model/ManagedNetworkPeeringPolicy
     * @implements module:model/ProxyResource
     */
    constructor() { 
        ProxyResource.initialize(this);
        ManagedNetworkPeeringPolicy.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ManagedNetworkPeeringPolicy</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ManagedNetworkPeeringPolicy} obj Optional instance to populate.
     * @return {module:model/ManagedNetworkPeeringPolicy} The populated <code>ManagedNetworkPeeringPolicy</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ManagedNetworkPeeringPolicy();
            ProxyResource.constructFromObject(data, obj);

            if (data.hasOwnProperty('properties')) {
                obj['properties'] = ManagedNetworkPeeringPolicyProperties.constructFromObject(data['properties']);
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('location')) {
                obj['location'] = ApiClient.convertToType(data['location'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ManagedNetworkPeeringPolicy</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ManagedNetworkPeeringPolicy</code>.
     */
    static validateJSON(data) {
        // validate the optional field `properties`
        if (data['properties']) { // data not null
          ManagedNetworkPeeringPolicyProperties.validateJSON(data['properties']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['location'] && !(typeof data['location'] === 'string' || data['location'] instanceof String)) {
            throw new Error("Expected the field `location` to be a primitive type in the JSON string but got " + data['location']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }

        return true;
    }


}



/**
 * @member {module:model/ManagedNetworkPeeringPolicyProperties} properties
 */
ManagedNetworkPeeringPolicy.prototype['properties'] = undefined;

/**
 * Fully qualified resource Id for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
 * @member {String} id
 */
ManagedNetworkPeeringPolicy.prototype['id'] = undefined;

/**
 * The geo-location where the resource lives
 * @member {String} location
 */
ManagedNetworkPeeringPolicy.prototype['location'] = undefined;

/**
 * The name of the resource
 * @member {String} name
 */
ManagedNetworkPeeringPolicy.prototype['name'] = undefined;

/**
 * The type of the resource. Ex- Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
 * @member {String} type
 */
ManagedNetworkPeeringPolicy.prototype['type'] = undefined;


// Implement ProxyResource interface:
/**
 * Fully qualified resource Id for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
 * @member {String} id
 */
ProxyResource.prototype['id'] = undefined;
/**
 * The geo-location where the resource lives
 * @member {String} location
 */
ProxyResource.prototype['location'] = undefined;
/**
 * The name of the resource
 * @member {String} name
 */
ProxyResource.prototype['name'] = undefined;
/**
 * The type of the resource. Ex- Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
 * @member {String} type
 */
ProxyResource.prototype['type'] = undefined;




export default ManagedNetworkPeeringPolicy;

