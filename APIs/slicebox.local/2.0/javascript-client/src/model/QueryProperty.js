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
 * The QueryProperty model module.
 * @module model/QueryProperty
 * @version 2.0
 */
class QueryProperty {
    /**
     * Constructs a new <code>QueryProperty</code>.
     * @alias module:model/QueryProperty
     */
    constructor() { 
        
        QueryProperty.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>QueryProperty</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/QueryProperty} obj Optional instance to populate.
     * @return {module:model/QueryProperty} The populated <code>QueryProperty</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new QueryProperty();

            if (data.hasOwnProperty('operator')) {
                obj['operator'] = ApiClient.convertToType(data['operator'], 'String');
            }
            if (data.hasOwnProperty('propertyName')) {
                obj['propertyName'] = ApiClient.convertToType(data['propertyName'], 'String');
            }
            if (data.hasOwnProperty('propertyValue')) {
                obj['propertyValue'] = ApiClient.convertToType(data['propertyValue'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>QueryProperty</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>QueryProperty</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['operator'] && !(typeof data['operator'] === 'string' || data['operator'] instanceof String)) {
            throw new Error("Expected the field `operator` to be a primitive type in the JSON string but got " + data['operator']);
        }
        // ensure the json data is a string
        if (data['propertyName'] && !(typeof data['propertyName'] === 'string' || data['propertyName'] instanceof String)) {
            throw new Error("Expected the field `propertyName` to be a primitive type in the JSON string but got " + data['propertyName']);
        }
        // ensure the json data is a string
        if (data['propertyValue'] && !(typeof data['propertyValue'] === 'string' || data['propertyValue'] instanceof String)) {
            throw new Error("Expected the field `propertyValue` to be a primitive type in the JSON string but got " + data['propertyValue']);
        }

        return true;
    }


}



/**
 * @member {String} operator
 */
QueryProperty.prototype['operator'] = undefined;

/**
 * @member {String} propertyName
 */
QueryProperty.prototype['propertyName'] = undefined;

/**
 * @member {String} propertyValue
 */
QueryProperty.prototype['propertyValue'] = undefined;






export default QueryProperty;

