/**
 * NetworkManagementClient
 * The Microsoft Azure Network management API provides a RESTful set of web services that interact with Microsoft Azure Networks service to manage your network resources. The API has entities that capture the relationship between an end user and the Microsoft Azure Networks service.
 *
 * The version of the OpenAPI document: 2018-08-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import ExpressRouteConnectionProperties from './ExpressRouteConnectionProperties';

/**
 * The ExpressRouteConnection model module.
 * @module model/ExpressRouteConnection
 * @version 2018-08-01
 */
class ExpressRouteConnection {
    /**
     * Constructs a new <code>ExpressRouteConnection</code>.
     * ExpressRouteConnection resource.
     * @alias module:model/ExpressRouteConnection
     */
    constructor() { 
        
        ExpressRouteConnection.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
        obj['name'] = name;
    }

    /**
     * Constructs a <code>ExpressRouteConnection</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ExpressRouteConnection} obj Optional instance to populate.
     * @return {module:model/ExpressRouteConnection} The populated <code>ExpressRouteConnection</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ExpressRouteConnection();

            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('properties')) {
                obj['properties'] = ExpressRouteConnectionProperties.constructFromObject(data['properties']);
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ExpressRouteConnection</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ExpressRouteConnection</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of ExpressRouteConnection.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // validate the optional field `properties`
        if (data['properties']) { // data not null
          ExpressRouteConnectionProperties.validateJSON(data['properties']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }

        return true;
    }


}

ExpressRouteConnection.RequiredProperties = ["name"];

/**
 * The name of the resource.
 * @member {String} name
 */
ExpressRouteConnection.prototype['name'] = undefined;

/**
 * @member {module:model/ExpressRouteConnectionProperties} properties
 */
ExpressRouteConnection.prototype['properties'] = undefined;

/**
 * Resource ID.
 * @member {String} id
 */
ExpressRouteConnection.prototype['id'] = undefined;






export default ExpressRouteConnection;

