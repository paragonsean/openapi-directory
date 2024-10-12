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
import GlobalCsmSkuDescriptionCapabilitiesInner from './GlobalCsmSkuDescriptionCapabilitiesInner';
import GlobalCsmSkuDescriptionCapacity from './GlobalCsmSkuDescriptionCapacity';

/**
 * The GlobalCsmSkuDescription model module.
 * @module model/GlobalCsmSkuDescription
 * @version 2019-08-01
 */
class GlobalCsmSkuDescription {
    /**
     * Constructs a new <code>GlobalCsmSkuDescription</code>.
     * A Global SKU Description.
     * @alias module:model/GlobalCsmSkuDescription
     */
    constructor() { 
        
        GlobalCsmSkuDescription.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>GlobalCsmSkuDescription</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GlobalCsmSkuDescription} obj Optional instance to populate.
     * @return {module:model/GlobalCsmSkuDescription} The populated <code>GlobalCsmSkuDescription</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GlobalCsmSkuDescription();

            if (data.hasOwnProperty('capabilities')) {
                obj['capabilities'] = ApiClient.convertToType(data['capabilities'], [GlobalCsmSkuDescriptionCapabilitiesInner]);
            }
            if (data.hasOwnProperty('capacity')) {
                obj['capacity'] = GlobalCsmSkuDescriptionCapacity.constructFromObject(data['capacity']);
            }
            if (data.hasOwnProperty('family')) {
                obj['family'] = ApiClient.convertToType(data['family'], 'String');
            }
            if (data.hasOwnProperty('locations')) {
                obj['locations'] = ApiClient.convertToType(data['locations'], ['String']);
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('size')) {
                obj['size'] = ApiClient.convertToType(data['size'], 'String');
            }
            if (data.hasOwnProperty('tier')) {
                obj['tier'] = ApiClient.convertToType(data['tier'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GlobalCsmSkuDescription</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GlobalCsmSkuDescription</code>.
     */
    static validateJSON(data) {
        if (data['capabilities']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['capabilities'])) {
                throw new Error("Expected the field `capabilities` to be an array in the JSON data but got " + data['capabilities']);
            }
            // validate the optional field `capabilities` (array)
            for (const item of data['capabilities']) {
                GlobalCsmSkuDescriptionCapabilitiesInner.validateJSON(item);
            };
        }
        // validate the optional field `capacity`
        if (data['capacity']) { // data not null
          GlobalCsmSkuDescriptionCapacity.validateJSON(data['capacity']);
        }
        // ensure the json data is a string
        if (data['family'] && !(typeof data['family'] === 'string' || data['family'] instanceof String)) {
            throw new Error("Expected the field `family` to be a primitive type in the JSON string but got " + data['family']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['locations'])) {
            throw new Error("Expected the field `locations` to be an array in the JSON data but got " + data['locations']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['size'] && !(typeof data['size'] === 'string' || data['size'] instanceof String)) {
            throw new Error("Expected the field `size` to be a primitive type in the JSON string but got " + data['size']);
        }
        // ensure the json data is a string
        if (data['tier'] && !(typeof data['tier'] === 'string' || data['tier'] instanceof String)) {
            throw new Error("Expected the field `tier` to be a primitive type in the JSON string but got " + data['tier']);
        }

        return true;
    }


}



/**
 * Capabilities of the SKU, e.g., is traffic manager enabled?
 * @member {Array.<module:model/GlobalCsmSkuDescriptionCapabilitiesInner>} capabilities
 */
GlobalCsmSkuDescription.prototype['capabilities'] = undefined;

/**
 * @member {module:model/GlobalCsmSkuDescriptionCapacity} capacity
 */
GlobalCsmSkuDescription.prototype['capacity'] = undefined;

/**
 * Family code of the resource SKU.
 * @member {String} family
 */
GlobalCsmSkuDescription.prototype['family'] = undefined;

/**
 * Locations of the SKU.
 * @member {Array.<String>} locations
 */
GlobalCsmSkuDescription.prototype['locations'] = undefined;

/**
 * Name of the resource SKU.
 * @member {String} name
 */
GlobalCsmSkuDescription.prototype['name'] = undefined;

/**
 * Size specifier of the resource SKU.
 * @member {String} size
 */
GlobalCsmSkuDescription.prototype['size'] = undefined;

/**
 * Service Tier of the resource SKU.
 * @member {String} tier
 */
GlobalCsmSkuDescription.prototype['tier'] = undefined;






export default GlobalCsmSkuDescription;

