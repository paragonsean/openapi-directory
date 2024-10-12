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
import RequestReference from './RequestReference';
import ShareProfileAcknowledgement from './ShareProfileAcknowledgement';

/**
 * The ShareProfileResult model module.
 * @module model/ShareProfileResult
 * @version 0.5
 */
class ShareProfileResult {
    /**
     * Constructs a new <code>ShareProfileResult</code>.
     * @alias module:model/ShareProfileResult
     * @param acknowledgement {module:model/ShareProfileAcknowledgement} 
     * @param requestId {String} a nonce, unique for each HTTP request
     * @param resp {module:model/RequestReference} 
     * @param timestamp {Date} Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ
     */
    constructor(acknowledgement, requestId, resp, timestamp) { 
        
        ShareProfileResult.initialize(this, acknowledgement, requestId, resp, timestamp);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, acknowledgement, requestId, resp, timestamp) { 
        obj['acknowledgement'] = acknowledgement;
        obj['requestId'] = requestId;
        obj['resp'] = resp;
        obj['timestamp'] = timestamp;
    }

    /**
     * Constructs a <code>ShareProfileResult</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ShareProfileResult} obj Optional instance to populate.
     * @return {module:model/ShareProfileResult} The populated <code>ShareProfileResult</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ShareProfileResult();

            if (data.hasOwnProperty('acknowledgement')) {
                obj['acknowledgement'] = ShareProfileAcknowledgement.constructFromObject(data['acknowledgement']);
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
     * Validates the JSON data with respect to <code>ShareProfileResult</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ShareProfileResult</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of ShareProfileResult.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `acknowledgement`
        if (data['acknowledgement']) { // data not null
          ShareProfileAcknowledgement.validateJSON(data['acknowledgement']);
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

ShareProfileResult.RequiredProperties = ["acknowledgement", "requestId", "resp", "timestamp"];

/**
 * @member {module:model/ShareProfileAcknowledgement} acknowledgement
 */
ShareProfileResult.prototype['acknowledgement'] = undefined;

/**
 * @member {module:model/Error} error
 */
ShareProfileResult.prototype['error'] = undefined;

/**
 * a nonce, unique for each HTTP request
 * @member {String} requestId
 */
ShareProfileResult.prototype['requestId'] = undefined;

/**
 * @member {module:model/RequestReference} resp
 */
ShareProfileResult.prototype['resp'] = undefined;

/**
 * Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ
 * @member {Date} timestamp
 */
ShareProfileResult.prototype['timestamp'] = undefined;






export default ShareProfileResult;

