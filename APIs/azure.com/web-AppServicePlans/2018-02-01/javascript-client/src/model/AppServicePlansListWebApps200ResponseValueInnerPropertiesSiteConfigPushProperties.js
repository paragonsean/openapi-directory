/**
 * AppServicePlans API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2018-02-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigPushProperties model module.
 * @module model/AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigPushProperties
 * @version 2018-02-01
 */
class AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigPushProperties {
    /**
     * Constructs a new <code>AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigPushProperties</code>.
     * PushSettings resource specific properties
     * @alias module:model/AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigPushProperties
     * @param isPushEnabled {Boolean} Gets or sets a flag indicating whether the Push endpoint is enabled.
     */
    constructor(isPushEnabled) { 
        
        AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigPushProperties.initialize(this, isPushEnabled);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, isPushEnabled) { 
        obj['isPushEnabled'] = isPushEnabled;
    }

    /**
     * Constructs a <code>AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigPushProperties</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigPushProperties} obj Optional instance to populate.
     * @return {module:model/AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigPushProperties} The populated <code>AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigPushProperties</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigPushProperties();

            if (data.hasOwnProperty('dynamicTagsJson')) {
                obj['dynamicTagsJson'] = ApiClient.convertToType(data['dynamicTagsJson'], 'String');
            }
            if (data.hasOwnProperty('isPushEnabled')) {
                obj['isPushEnabled'] = ApiClient.convertToType(data['isPushEnabled'], 'Boolean');
            }
            if (data.hasOwnProperty('tagWhitelistJson')) {
                obj['tagWhitelistJson'] = ApiClient.convertToType(data['tagWhitelistJson'], 'String');
            }
            if (data.hasOwnProperty('tagsRequiringAuth')) {
                obj['tagsRequiringAuth'] = ApiClient.convertToType(data['tagsRequiringAuth'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigPushProperties</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigPushProperties</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigPushProperties.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['dynamicTagsJson'] && !(typeof data['dynamicTagsJson'] === 'string' || data['dynamicTagsJson'] instanceof String)) {
            throw new Error("Expected the field `dynamicTagsJson` to be a primitive type in the JSON string but got " + data['dynamicTagsJson']);
        }
        // ensure the json data is a string
        if (data['tagWhitelistJson'] && !(typeof data['tagWhitelistJson'] === 'string' || data['tagWhitelistJson'] instanceof String)) {
            throw new Error("Expected the field `tagWhitelistJson` to be a primitive type in the JSON string but got " + data['tagWhitelistJson']);
        }
        // ensure the json data is a string
        if (data['tagsRequiringAuth'] && !(typeof data['tagsRequiringAuth'] === 'string' || data['tagsRequiringAuth'] instanceof String)) {
            throw new Error("Expected the field `tagsRequiringAuth` to be a primitive type in the JSON string but got " + data['tagsRequiringAuth']);
        }

        return true;
    }


}

AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigPushProperties.RequiredProperties = ["isPushEnabled"];

/**
 * Gets or sets a JSON string containing a list of dynamic tags that will be evaluated from user claims in the push registration endpoint.
 * @member {String} dynamicTagsJson
 */
AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigPushProperties.prototype['dynamicTagsJson'] = undefined;

/**
 * Gets or sets a flag indicating whether the Push endpoint is enabled.
 * @member {Boolean} isPushEnabled
 */
AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigPushProperties.prototype['isPushEnabled'] = undefined;

/**
 * Gets or sets a JSON string containing a list of tags that are whitelisted for use by the push registration endpoint.
 * @member {String} tagWhitelistJson
 */
AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigPushProperties.prototype['tagWhitelistJson'] = undefined;

/**
 * Gets or sets a JSON string containing a list of tags that require user authentication to be used in the push registration endpoint. Tags can consist of alphanumeric characters and the following: '_', '@', '#', '.', ':', '-'.  Validation should be performed at the PushRequestHandler.
 * @member {String} tagsRequiringAuth
 */
AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigPushProperties.prototype['tagsRequiringAuth'] = undefined;






export default AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigPushProperties;

