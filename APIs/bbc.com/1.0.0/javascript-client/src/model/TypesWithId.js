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
import TypesWithIdTypes from './TypesWithIdTypes';

/**
 * The TypesWithId model module.
 * @module model/TypesWithId
 * @version 1.0.0
 */
class TypesWithId {
    /**
     * Constructs a new <code>TypesWithId</code>.
     * @alias module:model/TypesWithId
     * @param types {module:model/TypesWithIdTypes} 
     */
    constructor(types) { 
        
        TypesWithId.initialize(this, types);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, types) { 
        obj['types'] = types;
    }

    /**
     * Constructs a <code>TypesWithId</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/TypesWithId} obj Optional instance to populate.
     * @return {module:model/TypesWithId} The populated <code>TypesWithId</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new TypesWithId();

            if (data.hasOwnProperty('types')) {
                obj['types'] = TypesWithIdTypes.constructFromObject(data['types']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>TypesWithId</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>TypesWithId</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of TypesWithId.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `types`
        if (data['types']) { // data not null
          TypesWithIdTypes.validateJSON(data['types']);
        }

        return true;
    }


}

TypesWithId.RequiredProperties = ["types"];

/**
 * @member {module:model/TypesWithIdTypes} types
 */
TypesWithId.prototype['types'] = undefined;






export default TypesWithId;

