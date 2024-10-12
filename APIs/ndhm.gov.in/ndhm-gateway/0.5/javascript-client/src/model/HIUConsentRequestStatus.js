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
import HIUConsentRequestStatusConsentRequest from './HIUConsentRequestStatusConsentRequest';
import RequestReference from './RequestReference';

/**
 * The HIUConsentRequestStatus model module.
 * @module model/HIUConsentRequestStatus
 * @version 0.5
 */
class HIUConsentRequestStatus {
    /**
     * Constructs a new <code>HIUConsentRequestStatus</code>.
     * @alias module:model/HIUConsentRequestStatus
     * @param requestId {String} a nonce, unique for each HTTP request
     * @param resp {module:model/RequestReference} 
     * @param timestamp {Date} Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ
     */
    constructor(requestId, resp, timestamp) { 
        
        HIUConsentRequestStatus.initialize(this, requestId, resp, timestamp);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, requestId, resp, timestamp) { 
        obj['requestId'] = requestId;
        obj['resp'] = resp;
        obj['timestamp'] = timestamp;
    }

    /**
     * Constructs a <code>HIUConsentRequestStatus</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/HIUConsentRequestStatus} obj Optional instance to populate.
     * @return {module:model/HIUConsentRequestStatus} The populated <code>HIUConsentRequestStatus</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new HIUConsentRequestStatus();

            if (data.hasOwnProperty('consentRequest')) {
                obj['consentRequest'] = HIUConsentRequestStatusConsentRequest.constructFromObject(data['consentRequest']);
            }
            if (data.hasOwnProperty('error')) {
                obj['error'] = Error.constructFromObject(data['error']);
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
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>HIUConsentRequestStatus</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>HIUConsentRequestStatus</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of HIUConsentRequestStatus.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `consentRequest`
        if (data['consentRequest']) { // data not null
          HIUConsentRequestStatusConsentRequest.validateJSON(data['consentRequest']);
        }
        // validate the optional field `error`
        if (data['error']) { // data not null
          Error.validateJSON(data['error']);
        }
        // ensure the json data is a string
        if (data['requestId'] && !(typeof data['requestId'] === 'string' || data['requestId'] instanceof String)) {
            throw new Error("Expected the field `requestId` to be a primitive type in the JSON string but got " + data['requestId']);
        }
        // validate the optional field `resp`
        if (data['resp']) { // data not null
          RequestReference.validateJSON(data['resp']);
        }

        return true;
    }


}

HIUConsentRequestStatus.RequiredProperties = ["requestId", "resp", "timestamp"];

/**
 * @member {module:model/HIUConsentRequestStatusConsentRequest} consentRequest
 */
HIUConsentRequestStatus.prototype['consentRequest'] = undefined;

/**
 * @member {module:model/Error} error
 */
HIUConsentRequestStatus.prototype['error'] = undefined;

/**
 * a nonce, unique for each HTTP request
 * @member {String} requestId
 */
HIUConsentRequestStatus.prototype['requestId'] = undefined;

/**
 * @member {module:model/RequestReference} resp
 */
HIUConsentRequestStatus.prototype['resp'] = undefined;

/**
 * Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ
 * @member {Date} timestamp
 */
HIUConsentRequestStatus.prototype['timestamp'] = undefined;






export default HIUConsentRequestStatus;

