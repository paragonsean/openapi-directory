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

/**
 * The WebServiceSendSmsRequest model module.
 * @module model/WebServiceSendSmsRequest
 * @version 1
 */
class WebServiceSendSmsRequest {
    /**
     * Constructs a new <code>WebServiceSendSmsRequest</code>.
     * WebServiceSendSmsRequest
     * @alias module:model/WebServiceSendSmsRequest
     */
    constructor() { 
        
        WebServiceSendSmsRequest.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>WebServiceSendSmsRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/WebServiceSendSmsRequest} obj Optional instance to populate.
     * @return {module:model/WebServiceSendSmsRequest} The populated <code>WebServiceSendSmsRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new WebServiceSendSmsRequest();

            if (data.hasOwnProperty('campaign')) {
                obj['campaign'] = ApiClient.convertToType(data['campaign'], 'String');
            }
            if (data.hasOwnProperty('dataField')) {
                obj['dataField'] = ApiClient.convertToType(data['dataField'], 'String');
            }
            if (data.hasOwnProperty('dateToSend')) {
                obj['dateToSend'] = ApiClient.convertToType(data['dateToSend'], 'Date');
            }
            if (data.hasOwnProperty('message')) {
                obj['message'] = ApiClient.convertToType(data['message'], 'String');
            }
            if (data.hasOwnProperty('recipientNumber')) {
                obj['recipientNumber'] = ApiClient.convertToType(data['recipientNumber'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>WebServiceSendSmsRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>WebServiceSendSmsRequest</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['campaign'] && !(typeof data['campaign'] === 'string' || data['campaign'] instanceof String)) {
            throw new Error("Expected the field `campaign` to be a primitive type in the JSON string but got " + data['campaign']);
        }
        // ensure the json data is a string
        if (data['dataField'] && !(typeof data['dataField'] === 'string' || data['dataField'] instanceof String)) {
            throw new Error("Expected the field `dataField` to be a primitive type in the JSON string but got " + data['dataField']);
        }
        // ensure the json data is a string
        if (data['message'] && !(typeof data['message'] === 'string' || data['message'] instanceof String)) {
            throw new Error("Expected the field `message` to be a primitive type in the JSON string but got " + data['message']);
        }
        // ensure the json data is a string
        if (data['recipientNumber'] && !(typeof data['recipientNumber'] === 'string' || data['recipientNumber'] instanceof String)) {
            throw new Error("Expected the field `recipientNumber` to be a primitive type in the JSON string but got " + data['recipientNumber']);
        }

        return true;
    }


}



/**
 * @member {String} campaign
 */
WebServiceSendSmsRequest.prototype['campaign'] = undefined;

/**
 * @member {String} dataField
 */
WebServiceSendSmsRequest.prototype['dataField'] = undefined;

/**
 * @member {Date} dateToSend
 */
WebServiceSendSmsRequest.prototype['dateToSend'] = undefined;

/**
 * @member {String} message
 */
WebServiceSendSmsRequest.prototype['message'] = undefined;

/**
 * @member {String} recipientNumber
 */
WebServiceSendSmsRequest.prototype['recipientNumber'] = undefined;






export default WebServiceSendSmsRequest;

