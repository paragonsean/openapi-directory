/**
 * reverb
 * reverb
 *
 * The version of the OpenAPI document: 3.0
 * Contact: integrations@reverb.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The MyNegotiationsIdAcceptPostRequest model module.
 * @module model/MyNegotiationsIdAcceptPostRequest
 * @version 3.0
 */
class MyNegotiationsIdAcceptPostRequest {
    /**
     * Constructs a new <code>MyNegotiationsIdAcceptPostRequest</code>.
     * @alias module:model/MyNegotiationsIdAcceptPostRequest
     */
    constructor() { 
        
        MyNegotiationsIdAcceptPostRequest.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>MyNegotiationsIdAcceptPostRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/MyNegotiationsIdAcceptPostRequest} obj Optional instance to populate.
     * @return {module:model/MyNegotiationsIdAcceptPostRequest} The populated <code>MyNegotiationsIdAcceptPostRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new MyNegotiationsIdAcceptPostRequest();

            if (data.hasOwnProperty('message')) {
                obj['message'] = ApiClient.convertToType(data['message'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>MyNegotiationsIdAcceptPostRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>MyNegotiationsIdAcceptPostRequest</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['message'] && !(typeof data['message'] === 'string' || data['message'] instanceof String)) {
            throw new Error("Expected the field `message` to be a primitive type in the JSON string but got " + data['message']);
        }

        return true;
    }


}



/**
 * Message to include with accepted offer
 * @member {String} message
 */
MyNegotiationsIdAcceptPostRequest.prototype['message'] = undefined;






export default MyNegotiationsIdAcceptPostRequest;

