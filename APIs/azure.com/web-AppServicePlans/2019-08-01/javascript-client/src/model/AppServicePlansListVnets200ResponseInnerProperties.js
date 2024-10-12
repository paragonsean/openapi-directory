/**
 * AppServicePlans API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-08-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import AppServicePlansListVnets200ResponseInnerPropertiesRoutesInner from './AppServicePlansListVnets200ResponseInnerPropertiesRoutesInner';

/**
 * The AppServicePlansListVnets200ResponseInnerProperties model module.
 * @module model/AppServicePlansListVnets200ResponseInnerProperties
 * @version 2019-08-01
 */
class AppServicePlansListVnets200ResponseInnerProperties {
    /**
     * Constructs a new <code>AppServicePlansListVnets200ResponseInnerProperties</code>.
     * VnetInfo resource specific properties
     * @alias module:model/AppServicePlansListVnets200ResponseInnerProperties
     */
    constructor() { 
        
        AppServicePlansListVnets200ResponseInnerProperties.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>AppServicePlansListVnets200ResponseInnerProperties</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AppServicePlansListVnets200ResponseInnerProperties} obj Optional instance to populate.
     * @return {module:model/AppServicePlansListVnets200ResponseInnerProperties} The populated <code>AppServicePlansListVnets200ResponseInnerProperties</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AppServicePlansListVnets200ResponseInnerProperties();

            if (data.hasOwnProperty('certBlob')) {
                obj['certBlob'] = ApiClient.convertToType(data['certBlob'], 'String');
            }
            if (data.hasOwnProperty('certThumbprint')) {
                obj['certThumbprint'] = ApiClient.convertToType(data['certThumbprint'], 'String');
            }
            if (data.hasOwnProperty('dnsServers')) {
                obj['dnsServers'] = ApiClient.convertToType(data['dnsServers'], 'String');
            }
            if (data.hasOwnProperty('isSwift')) {
                obj['isSwift'] = ApiClient.convertToType(data['isSwift'], 'Boolean');
            }
            if (data.hasOwnProperty('resyncRequired')) {
                obj['resyncRequired'] = ApiClient.convertToType(data['resyncRequired'], 'Boolean');
            }
            if (data.hasOwnProperty('routes')) {
                obj['routes'] = ApiClient.convertToType(data['routes'], [AppServicePlansListVnets200ResponseInnerPropertiesRoutesInner]);
            }
            if (data.hasOwnProperty('vnetResourceId')) {
                obj['vnetResourceId'] = ApiClient.convertToType(data['vnetResourceId'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AppServicePlansListVnets200ResponseInnerProperties</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AppServicePlansListVnets200ResponseInnerProperties</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['certBlob'] && !(typeof data['certBlob'] === 'string' || data['certBlob'] instanceof String)) {
            throw new Error("Expected the field `certBlob` to be a primitive type in the JSON string but got " + data['certBlob']);
        }
        // ensure the json data is a string
        if (data['certThumbprint'] && !(typeof data['certThumbprint'] === 'string' || data['certThumbprint'] instanceof String)) {
            throw new Error("Expected the field `certThumbprint` to be a primitive type in the JSON string but got " + data['certThumbprint']);
        }
        // ensure the json data is a string
        if (data['dnsServers'] && !(typeof data['dnsServers'] === 'string' || data['dnsServers'] instanceof String)) {
            throw new Error("Expected the field `dnsServers` to be a primitive type in the JSON string but got " + data['dnsServers']);
        }
        if (data['routes']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['routes'])) {
                throw new Error("Expected the field `routes` to be an array in the JSON data but got " + data['routes']);
            }
            // validate the optional field `routes` (array)
            for (const item of data['routes']) {
                AppServicePlansListVnets200ResponseInnerPropertiesRoutesInner.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['vnetResourceId'] && !(typeof data['vnetResourceId'] === 'string' || data['vnetResourceId'] instanceof String)) {
            throw new Error("Expected the field `vnetResourceId` to be a primitive type in the JSON string but got " + data['vnetResourceId']);
        }

        return true;
    }


}



/**
 * A certificate file (.cer) blob containing the public key of the private key used to authenticate a  Point-To-Site VPN connection.
 * @member {String} certBlob
 */
AppServicePlansListVnets200ResponseInnerProperties.prototype['certBlob'] = undefined;

/**
 * The client certificate thumbprint.
 * @member {String} certThumbprint
 */
AppServicePlansListVnets200ResponseInnerProperties.prototype['certThumbprint'] = undefined;

/**
 * DNS servers to be used by this Virtual Network. This should be a comma-separated list of IP addresses.
 * @member {String} dnsServers
 */
AppServicePlansListVnets200ResponseInnerProperties.prototype['dnsServers'] = undefined;

/**
 * Flag that is used to denote if this is VNET injection
 * @member {Boolean} isSwift
 */
AppServicePlansListVnets200ResponseInnerProperties.prototype['isSwift'] = undefined;

/**
 * <code>true</code> if a resync is required; otherwise, <code>false</code>.
 * @member {Boolean} resyncRequired
 */
AppServicePlansListVnets200ResponseInnerProperties.prototype['resyncRequired'] = undefined;

/**
 * The routes that this Virtual Network connection uses.
 * @member {Array.<module:model/AppServicePlansListVnets200ResponseInnerPropertiesRoutesInner>} routes
 */
AppServicePlansListVnets200ResponseInnerProperties.prototype['routes'] = undefined;

/**
 * The Virtual Network's resource ID.
 * @member {String} vnetResourceId
 */
AppServicePlansListVnets200ResponseInnerProperties.prototype['vnetResourceId'] = undefined;






export default AppServicePlansListVnets200ResponseInnerProperties;

