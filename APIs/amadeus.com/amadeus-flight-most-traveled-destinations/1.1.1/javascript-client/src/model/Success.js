/**
 * Flight Most Traveled Destinations
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.  Please also be aware that our test environment is based on a subset of the production, this API in test only returns a few selected cities. You can find the list in our **[data collection](https://github.com/amadeus4dev/data-collection)**.
 *
 * The version of the OpenAPI document: 1.1.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import AirTraffic from './AirTraffic';
import CollectionMeta from './CollectionMeta';
import Issue from './Issue';

/**
 * The Success model module.
 * @module model/Success
 * @version 1.1.1
 */
class Success {
    /**
     * Constructs a new <code>Success</code>.
     * @alias module:model/Success
     * @param data {Array.<module:model/AirTraffic>} 
     */
    constructor(data) { 
        
        Success.initialize(this, data);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, data) { 
        obj['data'] = data;
    }

    /**
     * Constructs a <code>Success</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Success} obj Optional instance to populate.
     * @return {module:model/Success} The populated <code>Success</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Success();

            if (data.hasOwnProperty('data')) {
                obj['data'] = ApiClient.convertToType(data['data'], [AirTraffic]);
            }
            if (data.hasOwnProperty('meta')) {
                obj['meta'] = CollectionMeta.constructFromObject(data['meta']);
            }
            if (data.hasOwnProperty('warnings')) {
                obj['warnings'] = ApiClient.convertToType(data['warnings'], [Issue]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Success</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Success</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of Success.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        if (data['data']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['data'])) {
                throw new Error("Expected the field `data` to be an array in the JSON data but got " + data['data']);
            }
            // validate the optional field `data` (array)
            for (const item of data['data']) {
                AirTraffic.validateJSON(item);
            };
        }
        // validate the optional field `meta`
        if (data['meta']) { // data not null
          CollectionMeta.validateJSON(data['meta']);
        }
        if (data['warnings']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['warnings'])) {
                throw new Error("Expected the field `warnings` to be an array in the JSON data but got " + data['warnings']);
            }
            // validate the optional field `warnings` (array)
            for (const item of data['warnings']) {
                Issue.validateJSON(item);
            };
        }

        return true;
    }


}

Success.RequiredProperties = ["data"];

/**
 * @member {Array.<module:model/AirTraffic>} data
 */
Success.prototype['data'] = undefined;

/**
 * @member {module:model/CollectionMeta} meta
 */
Success.prototype['meta'] = undefined;

/**
 * @member {Array.<module:model/Issue>} warnings
 */
Success.prototype['warnings'] = undefined;






export default Success;

