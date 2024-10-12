/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 23 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 0.0.0-streaming
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The UpdateNetworkSsidRequestRadiusServersInner model module.
 * @module model/UpdateNetworkSsidRequestRadiusServersInner
 * @version 0.0.0-streaming
 */
class UpdateNetworkSsidRequestRadiusServersInner {
    /**
     * Constructs a new <code>UpdateNetworkSsidRequestRadiusServersInner</code>.
     * @alias module:model/UpdateNetworkSsidRequestRadiusServersInner
     * @param host {String} IP address of your RADIUS server
     */
    constructor(host) { 
        
        UpdateNetworkSsidRequestRadiusServersInner.initialize(this, host);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, host) { 
        obj['host'] = host;
    }

    /**
     * Constructs a <code>UpdateNetworkSsidRequestRadiusServersInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UpdateNetworkSsidRequestRadiusServersInner} obj Optional instance to populate.
     * @return {module:model/UpdateNetworkSsidRequestRadiusServersInner} The populated <code>UpdateNetworkSsidRequestRadiusServersInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UpdateNetworkSsidRequestRadiusServersInner();

            if (data.hasOwnProperty('host')) {
                obj['host'] = ApiClient.convertToType(data['host'], 'String');
            }
            if (data.hasOwnProperty('port')) {
                obj['port'] = ApiClient.convertToType(data['port'], 'Number');
            }
            if (data.hasOwnProperty('secret')) {
                obj['secret'] = ApiClient.convertToType(data['secret'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UpdateNetworkSsidRequestRadiusServersInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UpdateNetworkSsidRequestRadiusServersInner</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of UpdateNetworkSsidRequestRadiusServersInner.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['host'] && !(typeof data['host'] === 'string' || data['host'] instanceof String)) {
            throw new Error("Expected the field `host` to be a primitive type in the JSON string but got " + data['host']);
        }
        // ensure the json data is a string
        if (data['secret'] && !(typeof data['secret'] === 'string' || data['secret'] instanceof String)) {
            throw new Error("Expected the field `secret` to be a primitive type in the JSON string but got " + data['secret']);
        }

        return true;
    }


}

UpdateNetworkSsidRequestRadiusServersInner.RequiredProperties = ["host"];

/**
 * IP address of your RADIUS server
 * @member {String} host
 */
UpdateNetworkSsidRequestRadiusServersInner.prototype['host'] = undefined;

/**
 * UDP port the RADIUS server listens on for Access-requests
 * @member {Number} port
 */
UpdateNetworkSsidRequestRadiusServersInner.prototype['port'] = undefined;

/**
 * RADIUS client shared secret
 * @member {String} secret
 */
UpdateNetworkSsidRequestRadiusServersInner.prototype['secret'] = undefined;






export default UpdateNetworkSsidRequestRadiusServersInner;

