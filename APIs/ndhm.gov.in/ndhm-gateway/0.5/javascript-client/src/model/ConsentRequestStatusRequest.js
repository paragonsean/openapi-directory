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

/**
 * The ConsentRequestStatusRequest model module.
 * @module model/ConsentRequestStatusRequest
 * @version 0.5
 */
class ConsentRequestStatusRequest {
    /**
     * Constructs a new <code>ConsentRequestStatusRequest</code>.
     * @alias module:model/ConsentRequestStatusRequest
     * @param consentRequestId {String} 
     * @param requestId {String} a nonce, unique for each HTTP request
     * @param timestamp {Date} Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ
     */
    constructor(consentRequestId, requestId, timestamp) { 
        
        ConsentRequestStatusRequest.initialize(this, consentRequestId, requestId, timestamp);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, consentRequestId, requestId, timestamp) { 
        obj['consentRequestId'] = consentRequestId;
        obj['requestId'] = requestId;
        obj['timestamp'] = timestamp;
    }

    /**
     * Constructs a <code>ConsentRequestStatusRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ConsentRequestStatusRequest} obj Optional instance to populate.
     * @return {module:model/ConsentRequestStatusRequest} The populated <code>ConsentRequestStatusRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ConsentRequestStatusRequest();

            if (data.hasOwnProperty('consentRequestId')) {
                obj['consentRequestId'] = ApiClient.convertToType(data['consentRequestId'], 'String');
            }
            if (data.hasOwnProperty('requestId')) {
                obj['requestId'] = ApiClient.convertToType(data['requestId'], 'String');
            }
            if (data.hasOwnProperty('timestamp')) {
                obj['timestamp'] = ApiClient.convertToType(data['timestamp'], 'Date');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ConsentRequestStatusRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ConsentRequestStatusRequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of ConsentRequestStatusRequest.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['consentRequestId'] && !(typeof data['consentRequestId'] === 'string' || data['consentRequestId'] instanceof String)) {
            throw new Error("Expected the field `consentRequestId` to be a primitive type in the JSON string but got " + data['consentRequestId']);
        }
        // ensure the json data is a string
        if (data['requestId'] && !(typeof data['requestId'] === 'string' || data['requestId'] instanceof String)) {
            throw new Error("Expected the field `requestId` to be a primitive type in the JSON string but got " + data['requestId']);
        }

        return true;
    }


}

ConsentRequestStatusRequest.RequiredProperties = ["consentRequestId", "requestId", "timestamp"];

/**
 * @member {String} consentRequestId
 */
ConsentRequestStatusRequest.prototype['consentRequestId'] = undefined;

/**
 * a nonce, unique for each HTTP request
 * @member {String} requestId
 */
ConsentRequestStatusRequest.prototype['requestId'] = undefined;

/**
 * Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ
 * @member {Date} timestamp
 */
ConsentRequestStatusRequest.prototype['timestamp'] = undefined;






export default ConsentRequestStatusRequest;

