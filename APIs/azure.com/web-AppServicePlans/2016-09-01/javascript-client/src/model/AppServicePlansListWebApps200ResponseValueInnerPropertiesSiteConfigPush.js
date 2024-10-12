/**
 * AppServicePlans API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2016-09-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigPushProperties from './AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigPushProperties';

/**
 * The AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigPush model module.
 * @module model/AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigPush
 * @version 2016-09-01
 */
class AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigPush {
    /**
     * Constructs a new <code>AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigPush</code>.
     * Push settings for the App.
     * @alias module:model/AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigPush
     */
    constructor() { 
        
        AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigPush.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigPush</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigPush} obj Optional instance to populate.
     * @return {module:model/AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigPush} The populated <code>AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigPush</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigPush();

            if (data.hasOwnProperty('properties')) {
                obj['properties'] = AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigPushProperties.constructFromObject(data['properties']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigPush</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigPush</code>.
     */
    static validateJSON(data) {
        // validate the optional field `properties`
        if (data['properties']) { // data not null
          AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigPushProperties.validateJSON(data['properties']);
        }

        return true;
    }


}



/**
 * @member {module:model/AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigPushProperties} properties
 */
AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigPush.prototype['properties'] = undefined;






export default AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigPush;

