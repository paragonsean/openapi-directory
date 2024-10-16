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
 * The UpdateNetworkClientSplashAuthorizationStatusRequestSsids0 model module.
 * @module model/UpdateNetworkClientSplashAuthorizationStatusRequestSsids0
 * @version 1.32.0
 */
class UpdateNetworkClientSplashAuthorizationStatusRequestSsids0 {
    /**
     * Constructs a new <code>UpdateNetworkClientSplashAuthorizationStatusRequestSsids0</code>.
     * Splash authorization for SSID 0
     * @alias module:model/UpdateNetworkClientSplashAuthorizationStatusRequestSsids0
     */
    constructor() { 
        
        UpdateNetworkClientSplashAuthorizationStatusRequestSsids0.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>UpdateNetworkClientSplashAuthorizationStatusRequestSsids0</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UpdateNetworkClientSplashAuthorizationStatusRequestSsids0} obj Optional instance to populate.
     * @return {module:model/UpdateNetworkClientSplashAuthorizationStatusRequestSsids0} The populated <code>UpdateNetworkClientSplashAuthorizationStatusRequestSsids0</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UpdateNetworkClientSplashAuthorizationStatusRequestSsids0();

            if (data.hasOwnProperty('isAuthorized')) {
                obj['isAuthorized'] = ApiClient.convertToType(data['isAuthorized'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UpdateNetworkClientSplashAuthorizationStatusRequestSsids0</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UpdateNetworkClientSplashAuthorizationStatusRequestSsids0</code>.
     */
    static validateJSON(data) {

        return true;
    }


}



/**
 * New authorization status for the SSID (true, false).
 * @member {Boolean} isAuthorized
 */
UpdateNetworkClientSplashAuthorizationStatusRequestSsids0.prototype['isAuthorized'] = undefined;






export default UpdateNetworkClientSplashAuthorizationStatusRequestSsids0;

