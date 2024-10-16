/**
 * Radio & Music Services
 * We encapsulate Radio & Music business logic for iPlayer Radio and BBC Music products on all platforms. We add value by reliably providing the right blend of metadata needed by clients.
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
import PersonalisedRadioActivity from './PersonalisedRadioActivity';

/**
 * The PersonalisedRadioResponse model module.
 * @module model/PersonalisedRadioResponse
 * @version 1.0.0
 */
class PersonalisedRadioResponse {
    /**
     * Constructs a new <code>PersonalisedRadioResponse</code>.
     * @alias module:model/PersonalisedRadioResponse
     * @param schema {String} 
     * @param limit {Number} 
     * @param method {String} 
     * @param offset {Number} 
     * @param repliedAt {String} 
     * @param results {Array.<module:model/PersonalisedRadioActivity>} 
     * @param total {Number} 
     */
    constructor(schema, limit, method, offset, repliedAt, results, total) { 
        
        PersonalisedRadioResponse.initialize(this, schema, limit, method, offset, repliedAt, results, total);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, schema, limit, method, offset, repliedAt, results, total) { 
        obj['$schema'] = schema;
        obj['limit'] = limit;
        obj['method'] = method;
        obj['offset'] = offset;
        obj['replied_at'] = repliedAt;
        obj['results'] = results;
        obj['total'] = total;
    }

    /**
     * Constructs a <code>PersonalisedRadioResponse</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PersonalisedRadioResponse} obj Optional instance to populate.
     * @return {module:model/PersonalisedRadioResponse} The populated <code>PersonalisedRadioResponse</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PersonalisedRadioResponse();

            if (data.hasOwnProperty('$schema')) {
                obj['$schema'] = ApiClient.convertToType(data['$schema'], 'String');
            }
            if (data.hasOwnProperty('limit')) {
                obj['limit'] = ApiClient.convertToType(data['limit'], 'Number');
            }
            if (data.hasOwnProperty('method')) {
                obj['method'] = ApiClient.convertToType(data['method'], 'String');
            }
            if (data.hasOwnProperty('offset')) {
                obj['offset'] = ApiClient.convertToType(data['offset'], 'Number');
            }
            if (data.hasOwnProperty('replied_at')) {
                obj['replied_at'] = ApiClient.convertToType(data['replied_at'], 'String');
            }
            if (data.hasOwnProperty('results')) {
                obj['results'] = ApiClient.convertToType(data['results'], [PersonalisedRadioActivity]);
            }
            if (data.hasOwnProperty('total')) {
                obj['total'] = ApiClient.convertToType(data['total'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PersonalisedRadioResponse</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PersonalisedRadioResponse</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of PersonalisedRadioResponse.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['$schema'] && !(typeof data['$schema'] === 'string' || data['$schema'] instanceof String)) {
            throw new Error("Expected the field `$schema` to be a primitive type in the JSON string but got " + data['$schema']);
        }
        // ensure the json data is a string
        if (data['method'] && !(typeof data['method'] === 'string' || data['method'] instanceof String)) {
            throw new Error("Expected the field `method` to be a primitive type in the JSON string but got " + data['method']);
        }
        // ensure the json data is a string
        if (data['replied_at'] && !(typeof data['replied_at'] === 'string' || data['replied_at'] instanceof String)) {
            throw new Error("Expected the field `replied_at` to be a primitive type in the JSON string but got " + data['replied_at']);
        }
        if (data['results']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['results'])) {
                throw new Error("Expected the field `results` to be an array in the JSON data but got " + data['results']);
            }
            // validate the optional field `results` (array)
            for (const item of data['results']) {
                PersonalisedRadioActivity.validateJSON(item);
            };
        }

        return true;
    }


}

PersonalisedRadioResponse.RequiredProperties = ["$schema", "limit", "method", "offset", "replied_at", "results", "total"];

/**
 * @member {String} $schema
 */
PersonalisedRadioResponse.prototype['$schema'] = undefined;

/**
 * @member {Number} limit
 */
PersonalisedRadioResponse.prototype['limit'] = undefined;

/**
 * @member {String} method
 */
PersonalisedRadioResponse.prototype['method'] = undefined;

/**
 * @member {Number} offset
 */
PersonalisedRadioResponse.prototype['offset'] = undefined;

/**
 * @member {String} replied_at
 */
PersonalisedRadioResponse.prototype['replied_at'] = undefined;

/**
 * @member {Array.<module:model/PersonalisedRadioActivity>} results
 */
PersonalisedRadioResponse.prototype['results'] = undefined;

/**
 * @member {Number} total
 */
PersonalisedRadioResponse.prototype['total'] = undefined;






export default PersonalisedRadioResponse;

