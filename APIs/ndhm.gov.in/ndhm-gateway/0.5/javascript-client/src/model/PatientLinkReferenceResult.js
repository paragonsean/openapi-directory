/**
 * Gateway
 * Gateway is the hub that routes/orchestrates the interaction between consent managers and API bridges. There are 5 categories of APIs; discovery, link, consent flow, data flow and  monitoring. To reflect the consumers of APIs, the above apis are also categorized under cm facing, hiu facing and hip facing  
 *
 * The version of the OpenAPI document: 0.5
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import Error from './Error';
import PatientLinkReferenceResultLink from './PatientLinkReferenceResultLink';
import RequestReference from './RequestReference';

/**
 * The PatientLinkReferenceResult model module.
 * @module model/PatientLinkReferenceResult
 * @version 0.5
 */
class PatientLinkReferenceResult {
    /**
     * Constructs a new <code>PatientLinkReferenceResult</code>.
     * @alias module:model/PatientLinkReferenceResult
     * @param requestId {String} a nonce, unique for each HTTP request
     * @param resp {module:model/RequestReference} 
     * @param timestamp {Date} Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ
     * @param transactionId {String} 
     */
    constructor(requestId, resp, timestamp, transactionId) { 
        
        PatientLinkReferenceResult.initialize(this, requestId, resp, timestamp, transactionId);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, requestId, resp, timestamp, transactionId) { 
        obj['requestId'] = requestId;
        obj['resp'] = resp;
        obj['timestamp'] = timestamp;
        obj['transactionId'] = transactionId;
    }

    /**
     * Constructs a <code>PatientLinkReferenceResult</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PatientLinkReferenceResult} obj Optional instance to populate.
     * @return {module:model/PatientLinkReferenceResult} The populated <code>PatientLinkReferenceResult</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PatientLinkReferenceResult();

            if (data.hasOwnProperty('error')) {
                obj['error'] = Error.constructFromObject(data['error']);
            }
            if (data.hasOwnProperty('link')) {
                obj['link'] = PatientLinkReferenceResultLink.constructFromObject(data['link']);
            }
            if (data.hasOwnProperty('requestId')) {
                obj['requestId'] = ApiClient.convertToType(data['requestId'], 'String');
            }
            if (data.hasOwnProperty('resp')) {
                obj['resp'] = RequestReference.constructFromObject(data['resp']);
            }
            if (data.hasOwnProperty('timestamp')) {
                obj['timestamp'] = ApiClient.convertToType(data['timestamp'], 'Date');
            }
            if (data.hasOwnProperty('transactionId')) {
                obj['transactionId'] = ApiClient.convertToType(data['transactionId'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PatientLinkReferenceResult</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PatientLinkReferenceResult</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of PatientLinkReferenceResult.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `error`
        if (data['error']) { // data not null
          Error.validateJSON(data['error']);
        }
        // validate the optional field `link`
        if (data['link']) { // data not null
          PatientLinkReferenceResultLink.validateJSON(data['link']);
        }
        // ensure the json data is a string
        if (data['requestId'] && !(typeof data['requestId'] === 'string' || data['requestId'] instanceof String)) {
            throw new Error("Expected the field `requestId` to be a primitive type in the JSON string but got " + data['requestId']);
        }
        // validate the optional field `resp`
        if (data['resp']) { // data not null
          RequestReference.validateJSON(data['resp']);
        }
        // ensure the json data is a string
        if (data['transactionId'] && !(typeof data['transactionId'] === 'string' || data['transactionId'] instanceof String)) {
            throw new Error("Expected the field `transactionId` to be a primitive type in the JSON string but got " + data['transactionId']);
        }

        return true;
    }


}

PatientLinkReferenceResult.RequiredProperties = ["requestId", "resp", "timestamp", "transactionId"];

/**
 * @member {module:model/Error} error
 */
PatientLinkReferenceResult.prototype['error'] = undefined;

/**
 * @member {module:model/PatientLinkReferenceResultLink} link
 */
PatientLinkReferenceResult.prototype['link'] = undefined;

/**
 * a nonce, unique for each HTTP request
 * @member {String} requestId
 */
PatientLinkReferenceResult.prototype['requestId'] = undefined;

/**
 * @member {module:model/RequestReference} resp
 */
PatientLinkReferenceResult.prototype['resp'] = undefined;

/**
 * Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ
 * @member {Date} timestamp
 */
PatientLinkReferenceResult.prototype['timestamp'] = undefined;

/**
 * @member {String} transactionId
 */
PatientLinkReferenceResult.prototype['transactionId'] = undefined;






export default PatientLinkReferenceResult;

