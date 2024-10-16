/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The UpdateDeviceCellularSimsRequestSimsInnerApnsInnerAuthentication model module.
 * @module model/UpdateDeviceCellularSimsRequestSimsInnerApnsInnerAuthentication
 * @version 1.32.0
 */
class UpdateDeviceCellularSimsRequestSimsInnerApnsInnerAuthentication {
    /**
     * Constructs a new <code>UpdateDeviceCellularSimsRequestSimsInnerApnsInnerAuthentication</code>.
     * APN authentication configurations.
     * @alias module:model/UpdateDeviceCellularSimsRequestSimsInnerApnsInnerAuthentication
     */
    constructor() { 
        
        UpdateDeviceCellularSimsRequestSimsInnerApnsInnerAuthentication.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
        obj['type'] = 'none';
    }

    /**
     * Constructs a <code>UpdateDeviceCellularSimsRequestSimsInnerApnsInnerAuthentication</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UpdateDeviceCellularSimsRequestSimsInnerApnsInnerAuthentication} obj Optional instance to populate.
     * @return {module:model/UpdateDeviceCellularSimsRequestSimsInnerApnsInnerAuthentication} The populated <code>UpdateDeviceCellularSimsRequestSimsInnerApnsInnerAuthentication</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UpdateDeviceCellularSimsRequestSimsInnerApnsInnerAuthentication();

            if (data.hasOwnProperty('password')) {
                obj['password'] = ApiClient.convertToType(data['password'], 'String');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
            if (data.hasOwnProperty('username')) {
                obj['username'] = ApiClient.convertToType(data['username'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UpdateDeviceCellularSimsRequestSimsInnerApnsInnerAuthentication</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UpdateDeviceCellularSimsRequestSimsInnerApnsInnerAuthentication</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['password'] && !(typeof data['password'] === 'string' || data['password'] instanceof String)) {
            throw new Error("Expected the field `password` to be a primitive type in the JSON string but got " + data['password']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }
        // ensure the json data is a string
        if (data['username'] && !(typeof data['username'] === 'string' || data['username'] instanceof String)) {
            throw new Error("Expected the field `username` to be a primitive type in the JSON string but got " + data['username']);
        }

        return true;
    }


}



/**
 * APN password, if type is set (if APN password is not supplied, the password is left unchanged).
 * @member {String} password
 */
UpdateDeviceCellularSimsRequestSimsInnerApnsInnerAuthentication.prototype['password'] = undefined;

/**
 * APN auth type.
 * @member {module:model/UpdateDeviceCellularSimsRequestSimsInnerApnsInnerAuthentication.TypeEnum} type
 * @default 'none'
 */
UpdateDeviceCellularSimsRequestSimsInnerApnsInnerAuthentication.prototype['type'] = 'none';

/**
 * APN username, if type is set.
 * @member {String} username
 */
UpdateDeviceCellularSimsRequestSimsInnerApnsInnerAuthentication.prototype['username'] = undefined;





/**
 * Allowed values for the <code>type</code> property.
 * @enum {String}
 * @readonly
 */
UpdateDeviceCellularSimsRequestSimsInnerApnsInnerAuthentication['TypeEnum'] = {

    /**
     * value: "chap"
     * @const
     */
    "chap": "chap",

    /**
     * value: "none"
     * @const
     */
    "none": "none",

    /**
     * value: "pap"
     * @const
     */
    "pap": "pap"
};



export default UpdateDeviceCellularSimsRequestSimsInnerApnsInnerAuthentication;

