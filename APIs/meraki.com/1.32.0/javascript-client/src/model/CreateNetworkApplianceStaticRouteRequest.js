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
 * The CreateNetworkApplianceStaticRouteRequest model module.
 * @module model/CreateNetworkApplianceStaticRouteRequest
 * @version 1.32.0
 */
class CreateNetworkApplianceStaticRouteRequest {
    /**
     * Constructs a new <code>CreateNetworkApplianceStaticRouteRequest</code>.
     * @alias module:model/CreateNetworkApplianceStaticRouteRequest
     * @param gatewayIp {String} The gateway IP (next hop) of the static route
     * @param name {String} The name of the new static route
     * @param subnet {String} The subnet of the static route
     */
    constructor(gatewayIp, name, subnet) { 
        
        CreateNetworkApplianceStaticRouteRequest.initialize(this, gatewayIp, name, subnet);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, gatewayIp, name, subnet) { 
        obj['gatewayIp'] = gatewayIp;
        obj['name'] = name;
        obj['subnet'] = subnet;
    }

    /**
     * Constructs a <code>CreateNetworkApplianceStaticRouteRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CreateNetworkApplianceStaticRouteRequest} obj Optional instance to populate.
     * @return {module:model/CreateNetworkApplianceStaticRouteRequest} The populated <code>CreateNetworkApplianceStaticRouteRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CreateNetworkApplianceStaticRouteRequest();

            if (data.hasOwnProperty('gatewayIp')) {
                obj['gatewayIp'] = ApiClient.convertToType(data['gatewayIp'], 'String');
            }
            if (data.hasOwnProperty('gatewayVlanId')) {
                obj['gatewayVlanId'] = ApiClient.convertToType(data['gatewayVlanId'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('subnet')) {
                obj['subnet'] = ApiClient.convertToType(data['subnet'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CreateNetworkApplianceStaticRouteRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CreateNetworkApplianceStaticRouteRequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of CreateNetworkApplianceStaticRouteRequest.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['gatewayIp'] && !(typeof data['gatewayIp'] === 'string' || data['gatewayIp'] instanceof String)) {
            throw new Error("Expected the field `gatewayIp` to be a primitive type in the JSON string but got " + data['gatewayIp']);
        }
        // ensure the json data is a string
        if (data['gatewayVlanId'] && !(typeof data['gatewayVlanId'] === 'string' || data['gatewayVlanId'] instanceof String)) {
            throw new Error("Expected the field `gatewayVlanId` to be a primitive type in the JSON string but got " + data['gatewayVlanId']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['subnet'] && !(typeof data['subnet'] === 'string' || data['subnet'] instanceof String)) {
            throw new Error("Expected the field `subnet` to be a primitive type in the JSON string but got " + data['subnet']);
        }

        return true;
    }


}

CreateNetworkApplianceStaticRouteRequest.RequiredProperties = ["gatewayIp", "name", "subnet"];

/**
 * The gateway IP (next hop) of the static route
 * @member {String} gatewayIp
 */
CreateNetworkApplianceStaticRouteRequest.prototype['gatewayIp'] = undefined;

/**
 * The gateway IP (next hop) VLAN ID of the static route
 * @member {String} gatewayVlanId
 */
CreateNetworkApplianceStaticRouteRequest.prototype['gatewayVlanId'] = undefined;

/**
 * The name of the new static route
 * @member {String} name
 */
CreateNetworkApplianceStaticRouteRequest.prototype['name'] = undefined;

/**
 * The subnet of the static route
 * @member {String} subnet
 */
CreateNetworkApplianceStaticRouteRequest.prototype['subnet'] = undefined;






export default CreateNetworkApplianceStaticRouteRequest;

