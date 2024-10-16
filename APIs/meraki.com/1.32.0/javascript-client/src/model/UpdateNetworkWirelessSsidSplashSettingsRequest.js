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
import UpdateNetworkWirelessSsidSplashSettingsRequestBilling from './UpdateNetworkWirelessSsidSplashSettingsRequestBilling';
import UpdateNetworkWirelessSsidSplashSettingsRequestGuestSponsorship from './UpdateNetworkWirelessSsidSplashSettingsRequestGuestSponsorship';
import UpdateNetworkWirelessSsidSplashSettingsRequestSentryEnrollment from './UpdateNetworkWirelessSsidSplashSettingsRequestSentryEnrollment';
import UpdateNetworkWirelessSsidSplashSettingsRequestSplashImage from './UpdateNetworkWirelessSsidSplashSettingsRequestSplashImage';
import UpdateNetworkWirelessSsidSplashSettingsRequestSplashLogo from './UpdateNetworkWirelessSsidSplashSettingsRequestSplashLogo';
import UpdateNetworkWirelessSsidSplashSettingsRequestSplashPrepaidFront from './UpdateNetworkWirelessSsidSplashSettingsRequestSplashPrepaidFront';

/**
 * The UpdateNetworkWirelessSsidSplashSettingsRequest model module.
 * @module model/UpdateNetworkWirelessSsidSplashSettingsRequest
 * @version 1.32.0
 */
class UpdateNetworkWirelessSsidSplashSettingsRequest {
    /**
     * Constructs a new <code>UpdateNetworkWirelessSsidSplashSettingsRequest</code>.
     * @alias module:model/UpdateNetworkWirelessSsidSplashSettingsRequest
     */
    constructor() { 
        
        UpdateNetworkWirelessSsidSplashSettingsRequest.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>UpdateNetworkWirelessSsidSplashSettingsRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UpdateNetworkWirelessSsidSplashSettingsRequest} obj Optional instance to populate.
     * @return {module:model/UpdateNetworkWirelessSsidSplashSettingsRequest} The populated <code>UpdateNetworkWirelessSsidSplashSettingsRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UpdateNetworkWirelessSsidSplashSettingsRequest();

            if (data.hasOwnProperty('allowSimultaneousLogins')) {
                obj['allowSimultaneousLogins'] = ApiClient.convertToType(data['allowSimultaneousLogins'], 'Boolean');
            }
            if (data.hasOwnProperty('billing')) {
                obj['billing'] = UpdateNetworkWirelessSsidSplashSettingsRequestBilling.constructFromObject(data['billing']);
            }
            if (data.hasOwnProperty('blockAllTrafficBeforeSignOn')) {
                obj['blockAllTrafficBeforeSignOn'] = ApiClient.convertToType(data['blockAllTrafficBeforeSignOn'], 'Boolean');
            }
            if (data.hasOwnProperty('controllerDisconnectionBehavior')) {
                obj['controllerDisconnectionBehavior'] = ApiClient.convertToType(data['controllerDisconnectionBehavior'], 'String');
            }
            if (data.hasOwnProperty('guestSponsorship')) {
                obj['guestSponsorship'] = UpdateNetworkWirelessSsidSplashSettingsRequestGuestSponsorship.constructFromObject(data['guestSponsorship']);
            }
            if (data.hasOwnProperty('redirectUrl')) {
                obj['redirectUrl'] = ApiClient.convertToType(data['redirectUrl'], 'String');
            }
            if (data.hasOwnProperty('sentryEnrollment')) {
                obj['sentryEnrollment'] = UpdateNetworkWirelessSsidSplashSettingsRequestSentryEnrollment.constructFromObject(data['sentryEnrollment']);
            }
            if (data.hasOwnProperty('splashImage')) {
                obj['splashImage'] = UpdateNetworkWirelessSsidSplashSettingsRequestSplashImage.constructFromObject(data['splashImage']);
            }
            if (data.hasOwnProperty('splashLogo')) {
                obj['splashLogo'] = UpdateNetworkWirelessSsidSplashSettingsRequestSplashLogo.constructFromObject(data['splashLogo']);
            }
            if (data.hasOwnProperty('splashPrepaidFront')) {
                obj['splashPrepaidFront'] = UpdateNetworkWirelessSsidSplashSettingsRequestSplashPrepaidFront.constructFromObject(data['splashPrepaidFront']);
            }
            if (data.hasOwnProperty('splashTimeout')) {
                obj['splashTimeout'] = ApiClient.convertToType(data['splashTimeout'], 'Number');
            }
            if (data.hasOwnProperty('splashUrl')) {
                obj['splashUrl'] = ApiClient.convertToType(data['splashUrl'], 'String');
            }
            if (data.hasOwnProperty('useRedirectUrl')) {
                obj['useRedirectUrl'] = ApiClient.convertToType(data['useRedirectUrl'], 'Boolean');
            }
            if (data.hasOwnProperty('useSplashUrl')) {
                obj['useSplashUrl'] = ApiClient.convertToType(data['useSplashUrl'], 'Boolean');
            }
            if (data.hasOwnProperty('welcomeMessage')) {
                obj['welcomeMessage'] = ApiClient.convertToType(data['welcomeMessage'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UpdateNetworkWirelessSsidSplashSettingsRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UpdateNetworkWirelessSsidSplashSettingsRequest</code>.
     */
    static validateJSON(data) {
        // validate the optional field `billing`
        if (data['billing']) { // data not null
          UpdateNetworkWirelessSsidSplashSettingsRequestBilling.validateJSON(data['billing']);
        }
        // ensure the json data is a string
        if (data['controllerDisconnectionBehavior'] && !(typeof data['controllerDisconnectionBehavior'] === 'string' || data['controllerDisconnectionBehavior'] instanceof String)) {
            throw new Error("Expected the field `controllerDisconnectionBehavior` to be a primitive type in the JSON string but got " + data['controllerDisconnectionBehavior']);
        }
        // validate the optional field `guestSponsorship`
        if (data['guestSponsorship']) { // data not null
          UpdateNetworkWirelessSsidSplashSettingsRequestGuestSponsorship.validateJSON(data['guestSponsorship']);
        }
        // ensure the json data is a string
        if (data['redirectUrl'] && !(typeof data['redirectUrl'] === 'string' || data['redirectUrl'] instanceof String)) {
            throw new Error("Expected the field `redirectUrl` to be a primitive type in the JSON string but got " + data['redirectUrl']);
        }
        // validate the optional field `sentryEnrollment`
        if (data['sentryEnrollment']) { // data not null
          UpdateNetworkWirelessSsidSplashSettingsRequestSentryEnrollment.validateJSON(data['sentryEnrollment']);
        }
        // validate the optional field `splashImage`
        if (data['splashImage']) { // data not null
          UpdateNetworkWirelessSsidSplashSettingsRequestSplashImage.validateJSON(data['splashImage']);
        }
        // validate the optional field `splashLogo`
        if (data['splashLogo']) { // data not null
          UpdateNetworkWirelessSsidSplashSettingsRequestSplashLogo.validateJSON(data['splashLogo']);
        }
        // validate the optional field `splashPrepaidFront`
        if (data['splashPrepaidFront']) { // data not null
          UpdateNetworkWirelessSsidSplashSettingsRequestSplashPrepaidFront.validateJSON(data['splashPrepaidFront']);
        }
        // ensure the json data is a string
        if (data['splashUrl'] && !(typeof data['splashUrl'] === 'string' || data['splashUrl'] instanceof String)) {
            throw new Error("Expected the field `splashUrl` to be a primitive type in the JSON string but got " + data['splashUrl']);
        }
        // ensure the json data is a string
        if (data['welcomeMessage'] && !(typeof data['welcomeMessage'] === 'string' || data['welcomeMessage'] instanceof String)) {
            throw new Error("Expected the field `welcomeMessage` to be a primitive type in the JSON string but got " + data['welcomeMessage']);
        }

        return true;
    }


}



/**
 * Whether or not to allow simultaneous logins from different devices.
 * @member {Boolean} allowSimultaneousLogins
 */
UpdateNetworkWirelessSsidSplashSettingsRequest.prototype['allowSimultaneousLogins'] = undefined;

/**
 * @member {module:model/UpdateNetworkWirelessSsidSplashSettingsRequestBilling} billing
 */
UpdateNetworkWirelessSsidSplashSettingsRequest.prototype['billing'] = undefined;

/**
 * How restricted allowing traffic should be. If true, all traffic types are blocked until the splash page is acknowledged. If false, all non-HTTP traffic is allowed before the splash page is acknowledged.
 * @member {Boolean} blockAllTrafficBeforeSignOn
 */
UpdateNetworkWirelessSsidSplashSettingsRequest.prototype['blockAllTrafficBeforeSignOn'] = undefined;

/**
 * How login attempts should be handled when the controller is unreachable. Can be either 'open', 'restricted', or 'default'.
 * @member {module:model/UpdateNetworkWirelessSsidSplashSettingsRequest.ControllerDisconnectionBehaviorEnum} controllerDisconnectionBehavior
 */
UpdateNetworkWirelessSsidSplashSettingsRequest.prototype['controllerDisconnectionBehavior'] = undefined;

/**
 * @member {module:model/UpdateNetworkWirelessSsidSplashSettingsRequestGuestSponsorship} guestSponsorship
 */
UpdateNetworkWirelessSsidSplashSettingsRequest.prototype['guestSponsorship'] = undefined;

/**
 * The custom redirect URL where the users will go after the splash page.
 * @member {String} redirectUrl
 */
UpdateNetworkWirelessSsidSplashSettingsRequest.prototype['redirectUrl'] = undefined;

/**
 * @member {module:model/UpdateNetworkWirelessSsidSplashSettingsRequestSentryEnrollment} sentryEnrollment
 */
UpdateNetworkWirelessSsidSplashSettingsRequest.prototype['sentryEnrollment'] = undefined;

/**
 * @member {module:model/UpdateNetworkWirelessSsidSplashSettingsRequestSplashImage} splashImage
 */
UpdateNetworkWirelessSsidSplashSettingsRequest.prototype['splashImage'] = undefined;

/**
 * @member {module:model/UpdateNetworkWirelessSsidSplashSettingsRequestSplashLogo} splashLogo
 */
UpdateNetworkWirelessSsidSplashSettingsRequest.prototype['splashLogo'] = undefined;

/**
 * @member {module:model/UpdateNetworkWirelessSsidSplashSettingsRequestSplashPrepaidFront} splashPrepaidFront
 */
UpdateNetworkWirelessSsidSplashSettingsRequest.prototype['splashPrepaidFront'] = undefined;

/**
 * Splash timeout in minutes. This will determine how often users will see the splash page.
 * @member {Number} splashTimeout
 */
UpdateNetworkWirelessSsidSplashSettingsRequest.prototype['splashTimeout'] = undefined;

/**
 * [optional] The custom splash URL of the click-through splash page. Note that the URL can be configured without necessarily being used. In order to enable the custom URL, see 'useSplashUrl'
 * @member {String} splashUrl
 */
UpdateNetworkWirelessSsidSplashSettingsRequest.prototype['splashUrl'] = undefined;

/**
 * The Boolean indicating whether the the user will be redirected to the custom redirect URL after the splash page. A custom redirect URL must be set if this is true.
 * @member {Boolean} useRedirectUrl
 */
UpdateNetworkWirelessSsidSplashSettingsRequest.prototype['useRedirectUrl'] = undefined;

/**
 * [optional] Boolean indicating whether the users will be redirected to the custom splash url. A custom splash URL must be set if this is true. Note that depending on your SSID's access control settings, it may not be possible to use the custom splash URL.
 * @member {Boolean} useSplashUrl
 */
UpdateNetworkWirelessSsidSplashSettingsRequest.prototype['useSplashUrl'] = undefined;

/**
 * The welcome message for the users on the splash page.
 * @member {String} welcomeMessage
 */
UpdateNetworkWirelessSsidSplashSettingsRequest.prototype['welcomeMessage'] = undefined;





/**
 * Allowed values for the <code>controllerDisconnectionBehavior</code> property.
 * @enum {String}
 * @readonly
 */
UpdateNetworkWirelessSsidSplashSettingsRequest['ControllerDisconnectionBehaviorEnum'] = {

    /**
     * value: "default"
     * @const
     */
    "default": "default",

    /**
     * value: "open"
     * @const
     */
    "open": "open",

    /**
     * value: "restricted"
     * @const
     */
    "restricted": "restricted"
};



export default UpdateNetworkWirelessSsidSplashSettingsRequest;

