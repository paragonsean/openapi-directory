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
 * The GetDeviceApplianceUplinksSettings200ResponseInterfacesWan1PppoeAuthentication model module.
 * @module model/GetDeviceApplianceUplinksSettings200ResponseInterfacesWan1PppoeAuthentication
 * @version 1.32.0
 */
class GetDeviceApplianceUplinksSettings200ResponseInterfacesWan1PppoeAuthentication {
    /**
     * Constructs a new <code>GetDeviceApplianceUplinksSettings200ResponseInterfacesWan1PppoeAuthentication</code>.
     * Settings for PPPoE Authentication.
     * @alias module:model/GetDeviceApplianceUplinksSettings200ResponseInterfacesWan1PppoeAuthentication
     */
    constructor() { 
        
        GetDeviceApplianceUplinksSettings200ResponseInterfacesWan1PppoeAuthentication.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>GetDeviceApplianceUplinksSettings200ResponseInterfacesWan1PppoeAuthentication</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GetDeviceApplianceUplinksSettings200ResponseInterfacesWan1PppoeAuthentication} obj Optional instance to populate.
     * @return {module:model/GetDeviceApplianceUplinksSettings200ResponseInterfacesWan1PppoeAuthentication} The populated <code>GetDeviceApplianceUplinksSettings200ResponseInterfacesWan1PppoeAuthentication</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GetDeviceApplianceUplinksSettings200ResponseInterfacesWan1PppoeAuthentication();

            if (data.hasOwnProperty('enabled')) {
                obj['enabled'] = ApiClient.convertToType(data['enabled'], 'Boolean');
            }
            if (data.hasOwnProperty('username')) {
                obj['username'] = ApiClient.convertToType(data['username'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GetDeviceApplianceUplinksSettings200ResponseInterfacesWan1PppoeAuthentication</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GetDeviceApplianceUplinksSettings200ResponseInterfacesWan1PppoeAuthentication</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['username'] && !(typeof data['username'] === 'string' || data['username'] instanceof String)) {
            throw new Error("Expected the field `username` to be a primitive type in the JSON string but got " + data['username']);
        }

        return true;
    }


}



/**
 * Whether PPPoE authentication is enabled.
 * @member {Boolean} enabled
 */
GetDeviceApplianceUplinksSettings200ResponseInterfacesWan1PppoeAuthentication.prototype['enabled'] = undefined;

/**
 * Username for PPPoE authentication.
 * @member {String} username
 */
GetDeviceApplianceUplinksSettings200ResponseInterfacesWan1PppoeAuthentication.prototype['username'] = undefined;






export default GetDeviceApplianceUplinksSettings200ResponseInterfacesWan1PppoeAuthentication;

