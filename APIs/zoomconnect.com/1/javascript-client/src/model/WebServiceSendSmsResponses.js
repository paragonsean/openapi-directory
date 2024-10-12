/**
 * www.zoomconnect.com
 * The world's greatest SMS API
 *
 * The version of the OpenAPI document: 1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import WebServiceSendSmsResponse from './WebServiceSendSmsResponse';

/**
 * The WebServiceSendSmsResponses model module.
 * @module model/WebServiceSendSmsResponses
 * @version 1
 */
class WebServiceSendSmsResponses {
    /**
     * Constructs a new <code>WebServiceSendSmsResponses</code>.
     * WebServiceSendSmsResponses
     * @alias module:model/WebServiceSendSmsResponses
     */
    constructor() { 
        
        WebServiceSendSmsResponses.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>WebServiceSendSmsResponses</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/WebServiceSendSmsResponses} obj Optional instance to populate.
     * @return {module:model/WebServiceSendSmsResponses} The populated <code>WebServiceSendSmsResponses</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new WebServiceSendSmsResponses();

            if (data.hasOwnProperty('sendSmsResponses')) {
                obj['sendSmsResponses'] = ApiClient.convertToType(data['sendSmsResponses'], [WebServiceSendSmsResponse]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>WebServiceSendSmsResponses</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>WebServiceSendSmsResponses</code>.
     */
    static validateJSON(data) {
        if (data['sendSmsResponses']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['sendSmsResponses'])) {
                throw new Error("Expected the field `sendSmsResponses` to be an array in the JSON data but got " + data['sendSmsResponses']);
            }
            // validate the optional field `sendSmsResponses` (array)
            for (const item of data['sendSmsResponses']) {
                WebServiceSendSmsResponse.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {Array.<module:model/WebServiceSendSmsResponse>} sendSmsResponses
 */
WebServiceSendSmsResponses.prototype['sendSmsResponses'] = undefined;






export default WebServiceSendSmsResponses;

