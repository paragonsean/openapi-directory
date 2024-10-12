/**
 * StorSimple8000SeriesManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2017-06-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The AcsConfiguration model module.
 * @module model/AcsConfiguration
 * @version 2017-06-01
 */
class AcsConfiguration {
    /**
     * Constructs a new <code>AcsConfiguration</code>.
     * The ACS configuration.
     * @alias module:model/AcsConfiguration
     * @param namespace {String} The namespace.
     * @param realm {String} The realm.
     * @param serviceUrl {String} The service URL.
     */
    constructor(namespace, realm, serviceUrl) { 
        
        AcsConfiguration.initialize(this, namespace, realm, serviceUrl);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, namespace, realm, serviceUrl) { 
        obj['namespace'] = namespace;
        obj['realm'] = realm;
        obj['serviceUrl'] = serviceUrl;
    }

    /**
     * Constructs a <code>AcsConfiguration</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AcsConfiguration} obj Optional instance to populate.
     * @return {module:model/AcsConfiguration} The populated <code>AcsConfiguration</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AcsConfiguration();

            if (data.hasOwnProperty('namespace')) {
                obj['namespace'] = ApiClient.convertToType(data['namespace'], 'String');
            }
            if (data.hasOwnProperty('realm')) {
                obj['realm'] = ApiClient.convertToType(data['realm'], 'String');
            }
            if (data.hasOwnProperty('serviceUrl')) {
                obj['serviceUrl'] = ApiClient.convertToType(data['serviceUrl'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AcsConfiguration</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AcsConfiguration</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of AcsConfiguration.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['namespace'] && !(typeof data['namespace'] === 'string' || data['namespace'] instanceof String)) {
            throw new Error("Expected the field `namespace` to be a primitive type in the JSON string but got " + data['namespace']);
        }
        // ensure the json data is a string
        if (data['realm'] && !(typeof data['realm'] === 'string' || data['realm'] instanceof String)) {
            throw new Error("Expected the field `realm` to be a primitive type in the JSON string but got " + data['realm']);
        }
        // ensure the json data is a string
        if (data['serviceUrl'] && !(typeof data['serviceUrl'] === 'string' || data['serviceUrl'] instanceof String)) {
            throw new Error("Expected the field `serviceUrl` to be a primitive type in the JSON string but got " + data['serviceUrl']);
        }

        return true;
    }


}

AcsConfiguration.RequiredProperties = ["namespace", "realm", "serviceUrl"];

/**
 * The namespace.
 * @member {String} namespace
 */
AcsConfiguration.prototype['namespace'] = undefined;

/**
 * The realm.
 * @member {String} realm
 */
AcsConfiguration.prototype['realm'] = undefined;

/**
 * The service URL.
 * @member {String} serviceUrl
 */
AcsConfiguration.prototype['serviceUrl'] = undefined;






export default AcsConfiguration;

