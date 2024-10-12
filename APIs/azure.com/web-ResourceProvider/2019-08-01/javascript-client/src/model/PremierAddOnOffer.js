/**
 *  API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-08-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The PremierAddOnOffer model module.
 * @module model/PremierAddOnOffer
 * @version 2019-08-01
 */
class PremierAddOnOffer {
    /**
     * Constructs a new <code>PremierAddOnOffer</code>.
     * Premier add-on offer.
     * @alias module:model/PremierAddOnOffer
     */
    constructor() { 
        
        PremierAddOnOffer.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>PremierAddOnOffer</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PremierAddOnOffer} obj Optional instance to populate.
     * @return {module:model/PremierAddOnOffer} The populated <code>PremierAddOnOffer</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PremierAddOnOffer();

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
     * Validates the JSON data with respect to <code>PremierAddOnOffer</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PremierAddOnOffer</code>.
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
 * PremierAddOnOffer resource specific properties
 * @member {Object} properties
 */
PremierAddOnOffer.prototype['properties'] = undefined;

/**
 * Resource Id.
 * @member {String} id
 */
PremierAddOnOffer.prototype['id'] = undefined;

/**
 * Kind of resource.
 * @member {String} kind
 */
PremierAddOnOffer.prototype['kind'] = undefined;

/**
 * Resource Name.
 * @member {String} name
 */
PremierAddOnOffer.prototype['name'] = undefined;

/**
 * Resource type.
 * @member {String} type
 */
PremierAddOnOffer.prototype['type'] = undefined;






export default PremierAddOnOffer;

