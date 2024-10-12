/**
 * MonitorManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2015-04-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The HttpRequestInfo model module.
 * @module model/HttpRequestInfo
 * @version 2015-04-01
 */
class HttpRequestInfo {
    /**
     * Constructs a new <code>HttpRequestInfo</code>.
     * The Http request info.
     * @alias module:model/HttpRequestInfo
     */
    constructor() { 
        
        HttpRequestInfo.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>HttpRequestInfo</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/HttpRequestInfo} obj Optional instance to populate.
     * @return {module:model/HttpRequestInfo} The populated <code>HttpRequestInfo</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new HttpRequestInfo();

            if (data.hasOwnProperty('clientIpAddress')) {
                obj['clientIpAddress'] = ApiClient.convertToType(data['clientIpAddress'], 'String');
            }
            if (data.hasOwnProperty('clientRequestId')) {
                obj['clientRequestId'] = ApiClient.convertToType(data['clientRequestId'], 'String');
            }
            if (data.hasOwnProperty('method')) {
                obj['method'] = ApiClient.convertToType(data['method'], 'String');
            }
            if (data.hasOwnProperty('uri')) {
                obj['uri'] = ApiClient.convertToType(data['uri'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>HttpRequestInfo</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>HttpRequestInfo</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['clientIpAddress'] && !(typeof data['clientIpAddress'] === 'string' || data['clientIpAddress'] instanceof String)) {
            throw new Error("Expected the field `clientIpAddress` to be a primitive type in the JSON string but got " + data['clientIpAddress']);
        }
        // ensure the json data is a string
        if (data['clientRequestId'] && !(typeof data['clientRequestId'] === 'string' || data['clientRequestId'] instanceof String)) {
            throw new Error("Expected the field `clientRequestId` to be a primitive type in the JSON string but got " + data['clientRequestId']);
        }
        // ensure the json data is a string
        if (data['method'] && !(typeof data['method'] === 'string' || data['method'] instanceof String)) {
            throw new Error("Expected the field `method` to be a primitive type in the JSON string but got " + data['method']);
        }
        // ensure the json data is a string
        if (data['uri'] && !(typeof data['uri'] === 'string' || data['uri'] instanceof String)) {
            throw new Error("Expected the field `uri` to be a primitive type in the JSON string but got " + data['uri']);
        }

        return true;
    }


}



/**
 * the client Ip Address
 * @member {String} clientIpAddress
 */
HttpRequestInfo.prototype['clientIpAddress'] = undefined;

/**
 * the client request id.
 * @member {String} clientRequestId
 */
HttpRequestInfo.prototype['clientRequestId'] = undefined;

/**
 * the Http request method.
 * @member {String} method
 */
HttpRequestInfo.prototype['method'] = undefined;

/**
 * the Uri.
 * @member {String} uri
 */
HttpRequestInfo.prototype['uri'] = undefined;






export default HttpRequestInfo;

