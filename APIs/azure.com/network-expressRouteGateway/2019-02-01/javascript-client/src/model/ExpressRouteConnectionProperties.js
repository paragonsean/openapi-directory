/**
 * NetworkManagementClient
 * The Microsoft Azure Network management API provides a RESTful set of web services that interact with Microsoft Azure Networks service to manage your network resources. The API has entities that capture the relationship between an end user and the Microsoft Azure Networks service.
 *
 * The version of the OpenAPI document: 2019-02-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import ExpressRouteCircuitPeeringId from './ExpressRouteCircuitPeeringId';

/**
 * The ExpressRouteConnectionProperties model module.
 * @module model/ExpressRouteConnectionProperties
 * @version 2019-02-01
 */
class ExpressRouteConnectionProperties {
    /**
     * Constructs a new <code>ExpressRouteConnectionProperties</code>.
     * Properties of the ExpressRouteConnection subresource.
     * @alias module:model/ExpressRouteConnectionProperties
     * @param expressRouteCircuitPeering {module:model/ExpressRouteCircuitPeeringId} 
     */
    constructor(expressRouteCircuitPeering) { 
        
        ExpressRouteConnectionProperties.initialize(this, expressRouteCircuitPeering);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, expressRouteCircuitPeering) { 
        obj['expressRouteCircuitPeering'] = expressRouteCircuitPeering;
    }

    /**
     * Constructs a <code>ExpressRouteConnectionProperties</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ExpressRouteConnectionProperties} obj Optional instance to populate.
     * @return {module:model/ExpressRouteConnectionProperties} The populated <code>ExpressRouteConnectionProperties</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ExpressRouteConnectionProperties();

            if (data.hasOwnProperty('authorizationKey')) {
                obj['authorizationKey'] = ApiClient.convertToType(data['authorizationKey'], 'String');
            }
            if (data.hasOwnProperty('expressRouteCircuitPeering')) {
                obj['expressRouteCircuitPeering'] = ExpressRouteCircuitPeeringId.constructFromObject(data['expressRouteCircuitPeering']);
            }
            if (data.hasOwnProperty('provisioningState')) {
                obj['provisioningState'] = ApiClient.convertToType(data['provisioningState'], 'String');
            }
            if (data.hasOwnProperty('routingWeight')) {
                obj['routingWeight'] = ApiClient.convertToType(data['routingWeight'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ExpressRouteConnectionProperties</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ExpressRouteConnectionProperties</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of ExpressRouteConnectionProperties.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['authorizationKey'] && !(typeof data['authorizationKey'] === 'string' || data['authorizationKey'] instanceof String)) {
            throw new Error("Expected the field `authorizationKey` to be a primitive type in the JSON string but got " + data['authorizationKey']);
        }
        // validate the optional field `expressRouteCircuitPeering`
        if (data['expressRouteCircuitPeering']) { // data not null
          ExpressRouteCircuitPeeringId.validateJSON(data['expressRouteCircuitPeering']);
        }
        // ensure the json data is a string
        if (data['provisioningState'] && !(typeof data['provisioningState'] === 'string' || data['provisioningState'] instanceof String)) {
            throw new Error("Expected the field `provisioningState` to be a primitive type in the JSON string but got " + data['provisioningState']);
        }

        return true;
    }


}

ExpressRouteConnectionProperties.RequiredProperties = ["expressRouteCircuitPeering"];

/**
 * Authorization key to establish the connection.
 * @member {String} authorizationKey
 */
ExpressRouteConnectionProperties.prototype['authorizationKey'] = undefined;

/**
 * @member {module:model/ExpressRouteCircuitPeeringId} expressRouteCircuitPeering
 */
ExpressRouteConnectionProperties.prototype['expressRouteCircuitPeering'] = undefined;

/**
 * The current provisioning state.
 * @member {module:model/ExpressRouteConnectionProperties.ProvisioningStateEnum} provisioningState
 */
ExpressRouteConnectionProperties.prototype['provisioningState'] = undefined;

/**
 * The routing weight associated to the connection.
 * @member {Number} routingWeight
 */
ExpressRouteConnectionProperties.prototype['routingWeight'] = undefined;





/**
 * Allowed values for the <code>provisioningState</code> property.
 * @enum {String}
 * @readonly
 */
ExpressRouteConnectionProperties['ProvisioningStateEnum'] = {

    /**
     * value: "Succeeded"
     * @const
     */
    "Succeeded": "Succeeded",

    /**
     * value: "Updating"
     * @const
     */
    "Updating": "Updating",

    /**
     * value: "Deleting"
     * @const
     */
    "Deleting": "Deleting",

    /**
     * value: "Failed"
     * @const
     */
    "Failed": "Failed"
};



export default ExpressRouteConnectionProperties;

