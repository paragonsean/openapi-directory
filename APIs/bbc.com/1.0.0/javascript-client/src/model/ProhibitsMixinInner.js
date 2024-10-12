/**
 * BBC Nitro API
 * BBC Nitro is the BBC's application programming interface (API) for BBC Programmes Metadata.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: nitro@bbc.co.uk
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import ProhibitsFilterInner from './ProhibitsFilterInner';

/**
 * The ProhibitsMixinInner model module.
 * @module model/ProhibitsMixinInner
 * @version 1.0.0
 */
class ProhibitsMixinInner {
    /**
     * Constructs a new <code>ProhibitsMixinInner</code>.
     * @alias module:model/ProhibitsMixinInner
     * @param name {String} 
     */
    constructor(name) { 
        
        ProhibitsMixinInner.initialize(this, name);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, name) { 
        obj['name'] = name;
    }

    /**
     * Constructs a <code>ProhibitsMixinInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ProhibitsMixinInner} obj Optional instance to populate.
     * @return {module:model/ProhibitsMixinInner} The populated <code>ProhibitsMixinInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ProhibitsMixinInner();

            if (data.hasOwnProperty('filter')) {
                obj['filter'] = ApiClient.convertToType(data['filter'], [ProhibitsFilterInner]);
            }
            if (data.hasOwnProperty('mixin')) {
                obj['mixin'] = ApiClient.convertToType(data['mixin'], [ProhibitsFilterInner]);
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ProhibitsMixinInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ProhibitsMixinInner</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of ProhibitsMixinInner.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        if (data['filter']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['filter'])) {
                throw new Error("Expected the field `filter` to be an array in the JSON data but got " + data['filter']);
            }
            // validate the optional field `filter` (array)
            for (const item of data['filter']) {
                ProhibitsFilterInner.validateJSON(item);
            };
        }
        if (data['mixin']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['mixin'])) {
                throw new Error("Expected the field `mixin` to be an array in the JSON data but got " + data['mixin']);
            }
            // validate the optional field `mixin` (array)
            for (const item of data['mixin']) {
                ProhibitsFilterInner.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }

        return true;
    }


}

ProhibitsMixinInner.RequiredProperties = ["name"];

/**
 * @member {Array.<module:model/ProhibitsFilterInner>} filter
 */
ProhibitsMixinInner.prototype['filter'] = undefined;

/**
 * @member {Array.<module:model/ProhibitsFilterInner>} mixin
 */
ProhibitsMixinInner.prototype['mixin'] = undefined;

/**
 * @member {String} name
 */
ProhibitsMixinInner.prototype['name'] = undefined;






export default ProhibitsMixinInner;

