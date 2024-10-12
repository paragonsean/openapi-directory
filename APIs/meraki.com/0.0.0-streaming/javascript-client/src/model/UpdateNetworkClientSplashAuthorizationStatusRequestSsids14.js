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
 * The UpdateNetworkClientSplashAuthorizationStatusRequestSsids14 model module.
 * @module model/UpdateNetworkClientSplashAuthorizationStatusRequestSsids14
 * @version 0.0.0-streaming
 */
class UpdateNetworkClientSplashAuthorizationStatusRequestSsids14 {
    /**
     * Constructs a new <code>UpdateNetworkClientSplashAuthorizationStatusRequestSsids14</code>.
     * Splash authorization for SSID 14
     * @alias module:model/UpdateNetworkClientSplashAuthorizationStatusRequestSsids14
     */
    constructor() { 
        
        UpdateNetworkClientSplashAuthorizationStatusRequestSsids14.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>UpdateNetworkClientSplashAuthorizationStatusRequestSsids14</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UpdateNetworkClientSplashAuthorizationStatusRequestSsids14} obj Optional instance to populate.
     * @return {module:model/UpdateNetworkClientSplashAuthorizationStatusRequestSsids14} The populated <code>UpdateNetworkClientSplashAuthorizationStatusRequestSsids14</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UpdateNetworkClientSplashAuthorizationStatusRequestSsids14();

            if (data.hasOwnProperty('isAuthorized')) {
                obj['isAuthorized'] = ApiClient.convertToType(data['isAuthorized'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UpdateNetworkClientSplashAuthorizationStatusRequestSsids14</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UpdateNetworkClientSplashAuthorizationStatusRequestSsids14</code>.
     */
    static validateJSON(data) {

        return true;
    }


}



/**
 * New authorization status for the SSID (true, false).
 * @member {Boolean} isAuthorized
 */
UpdateNetworkClientSplashAuthorizationStatusRequestSsids14.prototype['isAuthorized'] = undefined;






export default UpdateNetworkClientSplashAuthorizationStatusRequestSsids14;

