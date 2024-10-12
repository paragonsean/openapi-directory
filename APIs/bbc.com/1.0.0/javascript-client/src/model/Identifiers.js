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
import Identifier from './Identifier';

/**
 * The Identifiers model module.
 * @module model/Identifiers
 * @version 1.0.0
 */
class Identifiers {
    /**
     * Constructs a new <code>Identifiers</code>.
     * @alias module:model/Identifiers
     * @param identifier {Array.<module:model/Identifier>} 
     */
    constructor(identifier) { 
        
        Identifiers.initialize(this, identifier);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, identifier) { 
        obj['identifier'] = identifier;
    }

    /**
     * Constructs a <code>Identifiers</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Identifiers} obj Optional instance to populate.
     * @return {module:model/Identifiers} The populated <code>Identifiers</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Identifiers();

            if (data.hasOwnProperty('identifier')) {
                obj['identifier'] = ApiClient.convertToType(data['identifier'], [Identifier]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Identifiers</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Identifiers</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of Identifiers.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        if (data['identifier']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['identifier'])) {
                throw new Error("Expected the field `identifier` to be an array in the JSON data but got " + data['identifier']);
            }
            // validate the optional field `identifier` (array)
            for (const item of data['identifier']) {
                Identifier.validateJSON(item);
            };
        }

        return true;
    }


}

Identifiers.RequiredProperties = ["identifier"];

/**
 * @member {Array.<module:model/Identifier>} identifier
 */
Identifiers.prototype['identifier'] = undefined;






export default Identifiers;

