/**
 * NetworkManagementClient
 * The Microsoft Azure Network management API provides a RESTful set of web services that interact with Microsoft Azure Networks service to manage your network resources. The API has entities that capture the relationship between an end user and the Microsoft Azure Networks service.
 *
 * The version of the OpenAPI document: 2018-12-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import ExpressRouteGatewayProperties from './ExpressRouteGatewayProperties';

/**
 * The ExpressRouteGateway model module.
 * @module model/ExpressRouteGateway
 * @version 2018-12-01
 */
class ExpressRouteGateway {
    /**
     * Constructs a new <code>ExpressRouteGateway</code>.
     * ExpressRoute gateway resource.
     * @alias module:model/ExpressRouteGateway
     */
    constructor() { 
        
        ExpressRouteGateway.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ExpressRouteGateway</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ExpressRouteGateway} obj Optional instance to populate.
     * @return {module:model/ExpressRouteGateway} The populated <code>ExpressRouteGateway</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ExpressRouteGateway();

            if (data.hasOwnProperty('etag')) {
                obj['etag'] = ApiClient.convertToType(data['etag'], 'String');
            }
            if (data.hasOwnProperty('properties')) {
                obj['properties'] = ExpressRouteGatewayProperties.constructFromObject(data['properties']);
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
            if (data.hasOwnProperty('tags')) {
                obj['tags'] = ApiClient.convertToType(data['tags'], {'String': 'String'});
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ExpressRouteGateway</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ExpressRouteGateway</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['etag'] && !(typeof data['etag'] === 'string' || data['etag'] instanceof String)) {
            throw new Error("Expected the field `etag` to be a primitive type in the JSON string but got " + data['etag']);
        }
        // validate the optional field `properties`
        if (data['properties']) { // data not null
          ExpressRouteGatewayProperties.validateJSON(data['properties']);
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
 * A unique read-only string that changes whenever the resource is updated.
 * @member {String} etag
 */
ExpressRouteGateway.prototype['etag'] = undefined;

/**
 * @member {module:model/ExpressRouteGatewayProperties} properties
 */
ExpressRouteGateway.prototype['properties'] = undefined;

/**
 * Resource ID.
 * @member {String} id
 */
ExpressRouteGateway.prototype['id'] = undefined;

/**
 * Resource location.
 * @member {String} location
 */
ExpressRouteGateway.prototype['location'] = undefined;

/**
 * Resource name.
 * @member {String} name
 */
ExpressRouteGateway.prototype['name'] = undefined;

/**
 * Resource tags.
 * @member {Object.<String, String>} tags
 */
ExpressRouteGateway.prototype['tags'] = undefined;

/**
 * Resource type.
 * @member {String} type
 */
ExpressRouteGateway.prototype['type'] = undefined;






export default ExpressRouteGateway;

