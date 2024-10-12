/**
 * AppServicePlans API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2016-09-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The HybridConnectionLimits model module.
 * @module model/HybridConnectionLimits
 * @version 2016-09-01
 */
class HybridConnectionLimits {
    /**
     * Constructs a new <code>HybridConnectionLimits</code>.
     * Hybrid Connection limits contract. This is used to return the plan limits of Hybrid Connections.
     * @alias module:model/HybridConnectionLimits
     */
    constructor() { 
        
        HybridConnectionLimits.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>HybridConnectionLimits</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/HybridConnectionLimits} obj Optional instance to populate.
     * @return {module:model/HybridConnectionLimits} The populated <code>HybridConnectionLimits</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new HybridConnectionLimits();

            if (data.hasOwnProperty('properties')) {
                obj['properties'] = ApiClient.convertToType(data['properties'], Object);
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('kind')) {
                obj['kind'] = ApiClient.convertToType(data['kind'], 'String');
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
     * Validates the JSON data with respect to <code>HybridConnectionLimits</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>HybridConnectionLimits</code>.
     */
    static validateJSON(data) {
        // validate the optional field `properties`
        if (data['properties']) { // data not null
          Object.validateJSON(data['properties']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['kind'] && !(typeof data['kind'] === 'string' || data['kind'] instanceof String)) {
            throw new Error("Expected the field `kind` to be a primitive type in the JSON string but got " + data['kind']);
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
 * HybridConnectionLimits resource specific properties
 * @member {Object} properties
 */
HybridConnectionLimits.prototype['properties'] = undefined;

/**
 * Resource Id.
 * @member {String} id
 */
HybridConnectionLimits.prototype['id'] = undefined;

/**
 * Kind of resource.
 * @member {String} kind
 */
HybridConnectionLimits.prototype['kind'] = undefined;

/**
 * Resource Name.
 * @member {String} name
 */
HybridConnectionLimits.prototype['name'] = undefined;

/**
 * Resource type.
 * @member {String} type
 */
HybridConnectionLimits.prototype['type'] = undefined;






export default HybridConnectionLimits;

