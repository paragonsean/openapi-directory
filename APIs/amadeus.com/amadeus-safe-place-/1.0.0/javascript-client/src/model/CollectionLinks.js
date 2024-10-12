/**
 * Safe Place
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.     Please also be aware that our test environment is based on a subset of the production, this API in test only returns a few selected cities. You can find the list in our **[data collection](https://github.com/amadeus4dev/data-collection)**.
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The CollectionLinks model module.
 * @module model/CollectionLinks
 * @version 1.0.0
 */
class CollectionLinks {
    /**
     * Constructs a new <code>CollectionLinks</code>.
     * @alias module:model/CollectionLinks
     */
    constructor() { 
        
        CollectionLinks.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>CollectionLinks</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CollectionLinks} obj Optional instance to populate.
     * @return {module:model/CollectionLinks} The populated <code>CollectionLinks</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CollectionLinks();

            if (data.hasOwnProperty('first')) {
                obj['first'] = ApiClient.convertToType(data['first'], 'String');
            }
            if (data.hasOwnProperty('last')) {
                obj['last'] = ApiClient.convertToType(data['last'], 'String');
            }
            if (data.hasOwnProperty('next')) {
                obj['next'] = ApiClient.convertToType(data['next'], 'String');
            }
            if (data.hasOwnProperty('previous')) {
                obj['previous'] = ApiClient.convertToType(data['previous'], 'String');
            }
            if (data.hasOwnProperty('self')) {
                obj['self'] = ApiClient.convertToType(data['self'], 'String');
            }
            if (data.hasOwnProperty('up')) {
                obj['up'] = ApiClient.convertToType(data['up'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CollectionLinks</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CollectionLinks</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['first'] && !(typeof data['first'] === 'string' || data['first'] instanceof String)) {
            throw new Error("Expected the field `first` to be a primitive type in the JSON string but got " + data['first']);
        }
        // ensure the json data is a string
        if (data['last'] && !(typeof data['last'] === 'string' || data['last'] instanceof String)) {
            throw new Error("Expected the field `last` to be a primitive type in the JSON string but got " + data['last']);
        }
        // ensure the json data is a string
        if (data['next'] && !(typeof data['next'] === 'string' || data['next'] instanceof String)) {
            throw new Error("Expected the field `next` to be a primitive type in the JSON string but got " + data['next']);
        }
        // ensure the json data is a string
        if (data['previous'] && !(typeof data['previous'] === 'string' || data['previous'] instanceof String)) {
            throw new Error("Expected the field `previous` to be a primitive type in the JSON string but got " + data['previous']);
        }
        // ensure the json data is a string
        if (data['self'] && !(typeof data['self'] === 'string' || data['self'] instanceof String)) {
            throw new Error("Expected the field `self` to be a primitive type in the JSON string but got " + data['self']);
        }
        // ensure the json data is a string
        if (data['up'] && !(typeof data['up'] === 'string' || data['up'] instanceof String)) {
            throw new Error("Expected the field `up` to be a primitive type in the JSON string but got " + data['up']);
        }

        return true;
    }


}



/**
 * @member {String} first
 */
CollectionLinks.prototype['first'] = undefined;

/**
 * @member {String} last
 */
CollectionLinks.prototype['last'] = undefined;

/**
 * @member {String} next
 */
CollectionLinks.prototype['next'] = undefined;

/**
 * @member {String} previous
 */
CollectionLinks.prototype['previous'] = undefined;

/**
 * @member {String} self
 */
CollectionLinks.prototype['self'] = undefined;

/**
 * @member {String} up
 */
CollectionLinks.prototype['up'] = undefined;






export default CollectionLinks;

