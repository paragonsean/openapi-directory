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
import EventMessage from './EventMessage';
import Request from './Request';
import Response from './Response';

/**
 * The TestReturn model module.
 * @module model/TestReturn
 * @version 1.7.0
 */
class TestReturn {
    /**
     * Constructs a new <code>TestReturn</code>.
     * TestReturn is used for wrapping the return code of a test step execution
     * @alias module:model/TestReturn
     * @param code {Number} Return code for test (0 means Success, 1 means Failure)
     * @param elapsedTime {Number} Elapsed time in milliseconds
     */
    constructor(code, elapsedTime) { 
        
        TestReturn.initialize(this, code, elapsedTime);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, code, elapsedTime) { 
        obj['code'] = code;
        obj['elapsedTime'] = elapsedTime;
    }

    /**
     * Constructs a <code>TestReturn</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/TestReturn} obj Optional instance to populate.
     * @return {module:model/TestReturn} The populated <code>TestReturn</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new TestReturn();

            if (data.hasOwnProperty('code')) {
                obj['code'] = ApiClient.convertToType(data['code'], 'Number');
            }
            if (data.hasOwnProperty('elapsedTime')) {
                obj['elapsedTime'] = ApiClient.convertToType(data['elapsedTime'], 'Number');
            }
            if (data.hasOwnProperty('eventMessage')) {
                obj['eventMessage'] = EventMessage.constructFromObject(data['eventMessage']);
            }
            if (data.hasOwnProperty('message')) {
                obj['message'] = ApiClient.convertToType(data['message'], 'String');
            }
            if (data.hasOwnProperty('request')) {
                obj['request'] = Request.constructFromObject(data['request']);
            }
            if (data.hasOwnProperty('response')) {
                obj['response'] = Response.constructFromObject(data['response']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>TestReturn</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>TestReturn</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of TestReturn.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `eventMessage`
        if (data['eventMessage']) { // data not null
          EventMessage.validateJSON(data['eventMessage']);
        }
        // ensure the json data is a string
        if (data['message'] && !(typeof data['message'] === 'string' || data['message'] instanceof String)) {
            throw new Error("Expected the field `message` to be a primitive type in the JSON string but got " + data['message']);
        }
        // validate the optional field `request`
        if (data['request']) { // data not null
          Request.validateJSON(data['request']);
        }
        // validate the optional field `response`
        if (data['response']) { // data not null
          Response.validateJSON(data['response']);
        }

        return true;
    }


}

TestReturn.RequiredProperties = ["code", "elapsedTime"];

/**
 * Return code for test (0 means Success, 1 means Failure)
 * @member {Number} code
 */
TestReturn.prototype['code'] = undefined;

/**
 * Elapsed time in milliseconds
 * @member {Number} elapsedTime
 */
TestReturn.prototype['elapsedTime'] = undefined;

/**
 * @member {module:model/EventMessage} eventMessage
 */
TestReturn.prototype['eventMessage'] = undefined;

/**
 * Error message if any
 * @member {String} message
 */
TestReturn.prototype['message'] = undefined;

/**
 * @member {module:model/Request} request
 */
TestReturn.prototype['request'] = undefined;

/**
 * @member {module:model/Response} response
 */
TestReturn.prototype['response'] = undefined;






export default TestReturn;

