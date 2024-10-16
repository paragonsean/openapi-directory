/**
 * Microcks API v1.7
 * API offered by Microcks, the Kubernetes native tools for API and microservices mocking and testing (microcks.io)
 *
 * The version of the OpenAPI document: 1.7.0
 * Contact: laurent@microcks.io
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import Header from './Header';

/**
 * The Request model module.
 * @module model/Request
 * @version 1.7.0
 */
class Request {
    /**
     * Constructs a new <code>Request</code>.
     * A mock invocation or test request
     * @alias module:model/Request
     * @param name {String} Unique distinct name of this Request
     * @param operationId {String} Identifier of Operation this Request is associated to
     */
    constructor(name, operationId) { 
        
        Request.initialize(this, name, operationId);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, name, operationId) { 
        obj['name'] = name;
        obj['operationId'] = operationId;
    }

    /**
     * Constructs a <code>Request</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Request} obj Optional instance to populate.
     * @return {module:model/Request} The populated <code>Request</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Request();

            if (data.hasOwnProperty('content')) {
                obj['content'] = ApiClient.convertToType(data['content'], 'String');
            }
            if (data.hasOwnProperty('headers')) {
                obj['headers'] = ApiClient.convertToType(data['headers'], [Header]);
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('operationId')) {
                obj['operationId'] = ApiClient.convertToType(data['operationId'], 'String');
            }
            if (data.hasOwnProperty('testCaseId')) {
                obj['testCaseId'] = ApiClient.convertToType(data['testCaseId'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Request</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Request</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of Request.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['content'] && !(typeof data['content'] === 'string' || data['content'] instanceof String)) {
            throw new Error("Expected the field `content` to be a primitive type in the JSON string but got " + data['content']);
        }
        if (data['headers']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['headers'])) {
                throw new Error("Expected the field `headers` to be an array in the JSON data but got " + data['headers']);
            }
            // validate the optional field `headers` (array)
            for (const item of data['headers']) {
                Header.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['operationId'] && !(typeof data['operationId'] === 'string' || data['operationId'] instanceof String)) {
            throw new Error("Expected the field `operationId` to be a primitive type in the JSON string but got " + data['operationId']);
        }
        // ensure the json data is a string
        if (data['testCaseId'] && !(typeof data['testCaseId'] === 'string' || data['testCaseId'] instanceof String)) {
            throw new Error("Expected the field `testCaseId` to be a primitive type in the JSON string but got " + data['testCaseId']);
        }

        return true;
    }


}

Request.RequiredProperties = ["name", "operationId"];

/**
 * Body content for this request
 * @member {String} content
 */
Request.prototype['content'] = undefined;

/**
 * Headers for this Request
 * @member {Array.<module:model/Header>} headers
 */
Request.prototype['headers'] = undefined;

/**
 * Unique identifier of Request
 * @member {String} id
 */
Request.prototype['id'] = undefined;

/**
 * Unique distinct name of this Request
 * @member {String} name
 */
Request.prototype['name'] = undefined;

/**
 * Identifier of Operation this Request is associated to
 * @member {String} operationId
 */
Request.prototype['operationId'] = undefined;

/**
 * Unique identifier of TestCase this Request is attached (in case of a test)
 * @member {String} testCaseId
 */
Request.prototype['testCaseId'] = undefined;






export default Request;

