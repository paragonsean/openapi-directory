/**
 * Flight Offers Price
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.2.2
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The IssueSource model module.
 * @module model/IssueSource
 * @version 1.2.2
 */
class IssueSource {
    /**
     * Constructs a new <code>IssueSource</code>.
     * an object containing references to the source of the error
     * @alias module:model/IssueSource
     */
    constructor() { 
        
        IssueSource.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>IssueSource</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/IssueSource} obj Optional instance to populate.
     * @return {module:model/IssueSource} The populated <code>IssueSource</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new IssueSource();

            if (data.hasOwnProperty('example')) {
                obj['example'] = ApiClient.convertToType(data['example'], 'String');
            }
            if (data.hasOwnProperty('parameter')) {
                obj['parameter'] = ApiClient.convertToType(data['parameter'], 'String');
            }
            if (data.hasOwnProperty('pointer')) {
                obj['pointer'] = ApiClient.convertToType(data['pointer'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>IssueSource</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>IssueSource</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['example'] && !(typeof data['example'] === 'string' || data['example'] instanceof String)) {
            throw new Error("Expected the field `example` to be a primitive type in the JSON string but got " + data['example']);
        }
        // ensure the json data is a string
        if (data['parameter'] && !(typeof data['parameter'] === 'string' || data['parameter'] instanceof String)) {
            throw new Error("Expected the field `parameter` to be a primitive type in the JSON string but got " + data['parameter']);
        }
        // ensure the json data is a string
        if (data['pointer'] && !(typeof data['pointer'] === 'string' || data['pointer'] instanceof String)) {
            throw new Error("Expected the field `pointer` to be a primitive type in the JSON string but got " + data['pointer']);
        }

        return true;
    }


}



/**
 * a string indicating an example of the right value
 * @member {String} example
 */
IssueSource.prototype['example'] = undefined;

/**
 * a string indicating which URI query parameter caused the issue
 * @member {String} parameter
 */
IssueSource.prototype['parameter'] = undefined;

/**
 * a JSON Pointer [RFC6901] to the associated entity in the request document
 * @member {String} pointer
 */
IssueSource.prototype['pointer'] = undefined;






export default IssueSource;

