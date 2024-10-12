/**
 * Flight Cheapest Date Search
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.  Please also be aware that our test environment is based on a subset of the production, to see what is included in test please refer to our **[data collection](https://github.com/amadeus4dev/data-collection)**. 
 *
 * The version of the OpenAPI document: 1.0.6
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The Links model module.
 * @module model/Links
 * @version 1.0.6
 */
class Links {
    /**
     * Constructs a new <code>Links</code>.
     * @alias module:model/Links
     */
    constructor() { 
        
        Links.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Links</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Links} obj Optional instance to populate.
     * @return {module:model/Links} The populated <code>Links</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Links();

            if (data.hasOwnProperty('self')) {
                obj['self'] = ApiClient.convertToType(data['self'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Links</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Links</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['self'] && !(typeof data['self'] === 'string' || data['self'] instanceof String)) {
            throw new Error("Expected the field `self` to be a primitive type in the JSON string but got " + data['self']);
        }

        return true;
    }


}



/**
 * @member {String} self
 */
Links.prototype['self'] = undefined;






export default Links;

