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
import GetNetworkWirelessSsidSplashSettings200ResponseBilling from './GetNetworkWirelessSsidSplashSettings200ResponseBilling';
import GetNetworkWirelessSsidSplashSettings200ResponseGuestSponsorship from './GetNetworkWirelessSsidSplashSettings200ResponseGuestSponsorship';
import GetNetworkWirelessSsidSplashSettings200ResponseSelfRegistration from './GetNetworkWirelessSsidSplashSettings200ResponseSelfRegistration';
import GetNetworkWirelessSsidSplashSettings200ResponseSentryEnrollment from './GetNetworkWirelessSsidSplashSettings200ResponseSentryEnrollment';
import GetNetworkWirelessSsidSplashSettings200ResponseSplashImage from './GetNetworkWirelessSsidSplashSettings200ResponseSplashImage';
import GetNetworkWirelessSsidSplashSettings200ResponseSplashLogo from './GetNetworkWirelessSsidSplashSettings200ResponseSplashLogo';
import GetNetworkWirelessSsidSplashSettings200ResponseSplashPrepaidFront from './GetNetworkWirelessSsidSplashSettings200ResponseSplashPrepaidFront';

/**
 * The GetNetworkWirelessSsidSplashSettings200Response model module.
 * @module model/GetNetworkWirelessSsidSplashSettings200Response
 * @version 1.32.0
 */
class GetNetworkWirelessSsidSplashSettings200Response {
    /**
     * Constructs a new <code>GetNetworkWirelessSsidSplashSettings200Response</code>.
     * @alias module:model/GetNetworkWirelessSsidSplashSettings200Response
     */
    constructor() { 
        
        GetNetworkWirelessSsidSplashSettings200Response.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>GetNetworkWirelessSsidSplashSettings200Response</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GetNetworkWirelessSsidSplashSettings200Response} obj Optional instance to populate.
     * @return {module:model/GetNetworkWirelessSsidSplashSettings200Response} The populated <code>GetNetworkWirelessSsidSplashSettings200Response</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GetNetworkWirelessSsidSplashSettings200Response();

            if (data.hasOwnProperty('allowSimultaneousLogins')) {
                obj['allowSimultaneousLogins'] = ApiClient.convertToType(data['allowSimultaneousLogins'], 'Boolean');
            }
            if (data.hasOwnProperty('billing')) {
                obj['billing'] = GetNetworkWirelessSsidSplashSettings200ResponseBilling.constructFromObject(data['billing']);
            }
            if (data.hasOwnProperty('blockAllTrafficBeforeSignOn')) {
                obj['blockAllTrafficBeforeSignOn'] = ApiClient.convertToType(data['blockAllTrafficBeforeSignOn'], 'Boolean');
            }
            if (data.hasOwnProperty('controllerDisconnectionBehavior')) {
                obj['controllerDisconnectionBehavior'] = ApiClient.convertToType(data['controllerDisconnectionBehavior'], 'String');
            }
            if (data.hasOwnProperty('guestSponsorship')) {
                obj['guestSponsorship'] = GetNetworkWirelessSsidSplashSettings200ResponseGuestSponsorship.constructFromObject(data['guestSponsorship']);
            }
            if (data.hasOwnProperty('redirectUrl')) {
                obj['redirectUrl'] = ApiClient.convertToType(data['redirectUrl'], 'String');
            }
            if (data.hasOwnProperty('selfRegistration')) {
                obj['selfRegistration'] = GetNetworkWirelessSsidSplashSettings200ResponseSelfRegistration.constructFromObject(data['selfRegistration']);
            }
            if (data.hasOwnProperty('sentryEnrollment')) {
                obj['sentryEnrollment'] = GetNetworkWirelessSsidSplashSettings200ResponseSentryEnrollment.constructFromObject(data['sentryEnrollment']);
            }
            if (data.hasOwnProperty('splashImage')) {
                obj['splashImage'] = GetNetworkWirelessSsidSplashSettings200ResponseSplashImage.constructFromObject(data['splashImage']);
            }
            if (data.hasOwnProperty('splashLogo')) {
                obj['splashLogo'] = GetNetworkWirelessSsidSplashSettings200ResponseSplashLogo.constructFromObject(data['splashLogo']);
            }
            if (data.hasOwnProperty('splashPage')) {
                obj['splashPage'] = ApiClient.convertToType(data['splashPage'], 'String');
            }
            if (data.hasOwnProperty('splashPrepaidFront')) {
                obj['splashPrepaidFront'] = GetNetworkWirelessSsidSplashSettings200ResponseSplashPrepaidFront.constructFromObject(data['splashPrepaidFront']);
            }
            if (data.hasOwnProperty('splashTimeout')) {
                obj['splashTimeout'] = ApiClient.convertToType(data['splashTimeout'], 'Number');
            }
            if (data.hasOwnProperty('splashUrl')) {
                obj['splashUrl'] = ApiClient.convertToType(data['splashUrl'], 'String');
            }
            if (data.hasOwnProperty('ssidNumber')) {
                obj['ssidNumber'] = ApiClient.convertToType(data['ssidNumber'], 'Number');
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
     * Validates the JSON data with respect to <code>GetNetworkWirelessSsidSplashSettings200Response</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GetNetworkWirelessSsidSplashSettings200Response</code>.
     */
    static validateJSON(data) {
        // validate the optional field `billing`
        if (data['billing']) { // data not null
          GetNetworkWirelessSsidSplashSettings200ResponseBilling.validateJSON(data['billing']);
        }
        // ensure the json data is a string
        if (data['controllerDisconnectionBehavior'] && !(typeof data['controllerDisconnectionBehavior'] === 'string' || data['controllerDisconnectionBehavior'] instanceof String)) {
            throw new Error("Expected the field `controllerDisconnectionBehavior` to be a primitive type in the JSON string but got " + data['controllerDisconnectionBehavior']);
        }
        // validate the optional field `guestSponsorship`
        if (data['guestSponsorship']) { // data not null
          GetNetworkWirelessSsidSplashSettings200ResponseGuestSponsorship.validateJSON(data['guestSponsorship']);
        }
        // ensure the json data is a string
        if (data['redirectUrl'] && !(typeof data['redirectUrl'] === 'string' || data['redirectUrl'] instanceof String)) {
            throw new Error("Expected the field `redirectUrl` to be a primitive type in the JSON string but got " + data['redirectUrl']);
        }
        // validate the optional field `selfRegistration`
        if (data['selfRegistration']) { // data not null
          GetNetworkWirelessSsidSplashSettings200ResponseSelfRegistration.validateJSON(data['selfRegistration']);
        }
        // validate the optional field `sentryEnrollment`
        if (data['sentryEnrollment']) { // data not null
          GetNetworkWirelessSsidSplashSettings200ResponseSentryEnrollment.validateJSON(data['sentryEnrollment']);
        }
        // validate the optional field `splashImage`
        if (data['splashImage']) { // data not null
          GetNetworkWirelessSsidSplashSettings200ResponseSplashImage.validateJSON(data['splashImage']);
        }
        // validate the optional field `splashLogo`
        if (data['splashLogo']) { // data not null
          GetNetworkWirelessSsidSplashSettings200ResponseSplashLogo.validateJSON(data['splashLogo']);
        }
        // ensure the json data is a string
        if (data['splashPage'] && !(typeof data['splashPage'] === 'string' || data['splashPage'] instanceof String)) {
            throw new Error("Expected the field `splashPage` to be a primitive type in the JSON string but got " + data['splashPage']);
        }
        // validate the optional field `splashPrepaidFront`
        if (data['splashPrepaidFront']) { // data not null
          GetNetworkWirelessSsidSplashSettings200ResponseSplashPrepaidFront.validateJSON(data['splashPrepaidFront']);
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
GetNetworkWirelessSsidSplashSettings200Response.prototype['allowSimultaneousLogins'] = undefined;

/**
 * @member {module:model/GetNetworkWirelessSsidSplashSettings200ResponseBilling} billing
 */
GetNetworkWirelessSsidSplashSettings200Response.prototype['billing'] = undefined;

/**
 * How restricted allowing traffic should be. If true, all traffic types are blocked until the splash page is acknowledged. If false, all non-HTTP traffic is allowed before the splash page is acknowledged.
 * @member {Boolean} blockAllTrafficBeforeSignOn
 */
GetNetworkWirelessSsidSplashSettings200Response.prototype['blockAllTrafficBeforeSignOn'] = undefined;

/**
 * How login attempts should be handled when the controller is unreachable.
 * @member {String} controllerDisconnectionBehavior
 */
GetNetworkWirelessSsidSplashSettings200Response.prototype['controllerDisconnectionBehavior'] = undefined;

/**
 * @member {module:model/GetNetworkWirelessSsidSplashSettings200ResponseGuestSponsorship} guestSponsorship
 */
GetNetworkWirelessSsidSplashSettings200Response.prototype['guestSponsorship'] = undefined;

/**
 * The custom redirect URL where the users will go after the splash page.
 * @member {String} redirectUrl
 */
GetNetworkWirelessSsidSplashSettings200Response.prototype['redirectUrl'] = undefined;

/**
 * @member {module:model/GetNetworkWirelessSsidSplashSettings200ResponseSelfRegistration} selfRegistration
 */
GetNetworkWirelessSsidSplashSettings200Response.prototype['selfRegistration'] = undefined;

/**
 * @member {module:model/GetNetworkWirelessSsidSplashSettings200ResponseSentryEnrollment} sentryEnrollment
 */
GetNetworkWirelessSsidSplashSettings200Response.prototype['sentryEnrollment'] = undefined;

/**
 * @member {module:model/GetNetworkWirelessSsidSplashSettings200ResponseSplashImage} splashImage
 */
GetNetworkWirelessSsidSplashSettings200Response.prototype['splashImage'] = undefined;

/**
 * @member {module:model/GetNetworkWirelessSsidSplashSettings200ResponseSplashLogo} splashLogo
 */
GetNetworkWirelessSsidSplashSettings200Response.prototype['splashLogo'] = undefined;

/**
 * The type of splash page for this SSID
 * @member {String} splashPage
 */
GetNetworkWirelessSsidSplashSettings200Response.prototype['splashPage'] = undefined;

/**
 * @member {module:model/GetNetworkWirelessSsidSplashSettings200ResponseSplashPrepaidFront} splashPrepaidFront
 */
GetNetworkWirelessSsidSplashSettings200Response.prototype['splashPrepaidFront'] = undefined;

/**
 * Splash timeout in minutes.
 * @member {Number} splashTimeout
 */
GetNetworkWirelessSsidSplashSettings200Response.prototype['splashTimeout'] = undefined;

/**
 * The custom splash URL of the click-through splash page.
 * @member {String} splashUrl
 */
GetNetworkWirelessSsidSplashSettings200Response.prototype['splashUrl'] = undefined;

/**
 * SSID number
 * @member {Number} ssidNumber
 */
GetNetworkWirelessSsidSplashSettings200Response.prototype['ssidNumber'] = undefined;

/**
 * The Boolean indicating whether the the user will be redirected to the custom redirect URL after the splash page.
 * @member {Boolean} useRedirectUrl
 */
GetNetworkWirelessSsidSplashSettings200Response.prototype['useRedirectUrl'] = undefined;

/**
 * Boolean indicating whether the users will be redirected to the custom splash url
 * @member {Boolean} useSplashUrl
 */
GetNetworkWirelessSsidSplashSettings200Response.prototype['useSplashUrl'] = undefined;

/**
 * The welcome message for the users on the splash page.
 * @member {String} welcomeMessage
 */
GetNetworkWirelessSsidSplashSettings200Response.prototype['welcomeMessage'] = undefined;






export default GetNetworkWirelessSsidSplashSettings200Response;

