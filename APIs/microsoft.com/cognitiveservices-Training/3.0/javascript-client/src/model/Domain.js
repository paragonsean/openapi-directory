/**
 * Custom Vision Training Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 3.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The Domain model module.
 * @module model/Domain
 * @version 3.0
 */
class Domain {
    /**
     * Constructs a new <code>Domain</code>.
     * @alias module:model/Domain
     */
    constructor() { 
        
        Domain.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Domain</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Domain} obj Optional instance to populate.
     * @return {module:model/Domain} The populated <code>Domain</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Domain();

            if (data.hasOwnProperty('enabled')) {
                obj['enabled'] = ApiClient.convertToType(data['enabled'], 'Boolean');
            }
            if (data.hasOwnProperty('exportable')) {
                obj['exportable'] = ApiClient.convertToType(data['exportable'], 'Boolean');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
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
     * Validates the JSON data with respect to <code>Domain</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Domain</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
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
 * @member {Boolean} enabled
 */
Domain.prototype['enabled'] = undefined;

/**
 * @member {Boolean} exportable
 */
Domain.prototype['exportable'] = undefined;

/**
 * @member {String} id
 */
Domain.prototype['id'] = undefined;

/**
 * @member {String} name
 */
Domain.prototype['name'] = undefined;

/**
 * @member {module:model/Domain.TypeEnum} type
 */
Domain.prototype['type'] = undefined;





/**
 * Allowed values for the <code>type</code> property.
 * @enum {String}
 * @readonly
 */
Domain['TypeEnum'] = {

    /**
     * value: "Classification"
     * @const
     */
    "Classification": "Classification",

    /**
     * value: "ObjectDetection"
     * @const
     */
    "ObjectDetection": "ObjectDetection"
};



export default Domain;

