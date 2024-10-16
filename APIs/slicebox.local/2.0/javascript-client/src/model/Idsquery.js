/**
 * Slicebox API
 * Slicebox - safe sharing of medical images
 *
 * The version of the OpenAPI document: 2.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The Idsquery model module.
 * @module model/Idsquery
 * @version 2.0
 */
class Idsquery {
    /**
     * Constructs a new <code>Idsquery</code>.
     * @alias module:model/Idsquery
     * @param ids {Array.<Number>} 
     */
    constructor(ids) { 
        
        Idsquery.initialize(this, ids);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, ids) { 
        obj['ids'] = ids;
    }

    /**
     * Constructs a <code>Idsquery</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Idsquery} obj Optional instance to populate.
     * @return {module:model/Idsquery} The populated <code>Idsquery</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Idsquery();

            if (data.hasOwnProperty('ids')) {
                obj['ids'] = ApiClient.convertToType(data['ids'], ['Number']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Idsquery</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Idsquery</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of Idsquery.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is an array
        if (!Array.isArray(data['ids'])) {
            throw new Error("Expected the field `ids` to be an array in the JSON data but got " + data['ids']);
        }

        return true;
    }


}

Idsquery.RequiredProperties = ["ids"];

/**
 * @member {Array.<Number>} ids
 */
Idsquery.prototype['ids'] = undefined;






export default Idsquery;

