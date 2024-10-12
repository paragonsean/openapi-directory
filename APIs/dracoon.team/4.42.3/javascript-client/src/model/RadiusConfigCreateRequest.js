/**
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import FailoverServer from './FailoverServer';

/**
 * The RadiusConfigCreateRequest model module.
 * @module model/RadiusConfigCreateRequest
 * @version 4.42.3
 */
class RadiusConfigCreateRequest {
    /**
     * Constructs a new <code>RadiusConfigCreateRequest</code>.
     * Request model for creating a RADIUS configuration
     * @alias module:model/RadiusConfigCreateRequest
     * @param ipAddress {String} RADIUS Server IP Address
     * @param port {Number} RADIUS Server Port
     * @param sharedSecret {String} Shared Secret to access the RADIUS server
     */
    constructor(ipAddress, port, sharedSecret) { 
        
        RadiusConfigCreateRequest.initialize(this, ipAddress, port, sharedSecret);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, ipAddress, port, sharedSecret) { 
        obj['ipAddress'] = ipAddress;
        obj['otpPinFirst'] = true;
        obj['port'] = port;
        obj['sharedSecret'] = sharedSecret;
    }

    /**
     * Constructs a <code>RadiusConfigCreateRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/RadiusConfigCreateRequest} obj Optional instance to populate.
     * @return {module:model/RadiusConfigCreateRequest} The populated <code>RadiusConfigCreateRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new RadiusConfigCreateRequest();

            if (data.hasOwnProperty('failoverServer')) {
                obj['failoverServer'] = FailoverServer.constructFromObject(data['failoverServer']);
            }
            if (data.hasOwnProperty('ipAddress')) {
                obj['ipAddress'] = ApiClient.convertToType(data['ipAddress'], 'String');
            }
            if (data.hasOwnProperty('otpPinFirst')) {
                obj['otpPinFirst'] = ApiClient.convertToType(data['otpPinFirst'], 'Boolean');
            }
            if (data.hasOwnProperty('port')) {
                obj['port'] = ApiClient.convertToType(data['port'], 'Number');
            }
            if (data.hasOwnProperty('sharedSecret')) {
                obj['sharedSecret'] = ApiClient.convertToType(data['sharedSecret'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>RadiusConfigCreateRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>RadiusConfigCreateRequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of RadiusConfigCreateRequest.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `failoverServer`
        if (data['failoverServer']) { // data not null
          FailoverServer.validateJSON(data['failoverServer']);
        }
        // ensure the json data is a string
        if (data['ipAddress'] && !(typeof data['ipAddress'] === 'string' || data['ipAddress'] instanceof String)) {
            throw new Error("Expected the field `ipAddress` to be a primitive type in the JSON string but got " + data['ipAddress']);
        }
        // ensure the json data is a string
        if (data['sharedSecret'] && !(typeof data['sharedSecret'] === 'string' || data['sharedSecret'] instanceof String)) {
            throw new Error("Expected the field `sharedSecret` to be a primitive type in the JSON string but got " + data['sharedSecret']);
        }

        return true;
    }


}

RadiusConfigCreateRequest.RequiredProperties = ["ipAddress", "port", "sharedSecret"];

/**
 * @member {module:model/FailoverServer} failoverServer
 */
RadiusConfigCreateRequest.prototype['failoverServer'] = undefined;

/**
 * RADIUS Server IP Address
 * @member {String} ipAddress
 */
RadiusConfigCreateRequest.prototype['ipAddress'] = undefined;

/**
 * Sequence order of concatenated PIN and one-time token
 * @member {Boolean} otpPinFirst
 * @default true
 */
RadiusConfigCreateRequest.prototype['otpPinFirst'] = true;

/**
 * RADIUS Server Port
 * @member {Number} port
 */
RadiusConfigCreateRequest.prototype['port'] = undefined;

/**
 * Shared Secret to access the RADIUS server
 * @member {String} sharedSecret
 */
RadiusConfigCreateRequest.prototype['sharedSecret'] = undefined;






export default RadiusConfigCreateRequest;

