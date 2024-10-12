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

/**
 * The AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigVirtualApplicationsInnerVirtualDirectoriesInner model module.
 * @module model/AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigVirtualApplicationsInnerVirtualDirectoriesInner
 * @version 2019-08-01
 */
class AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigVirtualApplicationsInnerVirtualDirectoriesInner {
    /**
     * Constructs a new <code>AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigVirtualApplicationsInnerVirtualDirectoriesInner</code>.
     * Directory for virtual application.
     * @alias module:model/AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigVirtualApplicationsInnerVirtualDirectoriesInner
     */
    constructor() { 
        
        AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigVirtualApplicationsInnerVirtualDirectoriesInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigVirtualApplicationsInnerVirtualDirectoriesInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigVirtualApplicationsInnerVirtualDirectoriesInner} obj Optional instance to populate.
     * @return {module:model/AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigVirtualApplicationsInnerVirtualDirectoriesInner} The populated <code>AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigVirtualApplicationsInnerVirtualDirectoriesInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigVirtualApplicationsInnerVirtualDirectoriesInner();

            if (data.hasOwnProperty('physicalPath')) {
                obj['physicalPath'] = ApiClient.convertToType(data['physicalPath'], 'String');
            }
            if (data.hasOwnProperty('virtualPath')) {
                obj['virtualPath'] = ApiClient.convertToType(data['virtualPath'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigVirtualApplicationsInnerVirtualDirectoriesInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigVirtualApplicationsInnerVirtualDirectoriesInner</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['physicalPath'] && !(typeof data['physicalPath'] === 'string' || data['physicalPath'] instanceof String)) {
            throw new Error("Expected the field `physicalPath` to be a primitive type in the JSON string but got " + data['physicalPath']);
        }
        // ensure the json data is a string
        if (data['virtualPath'] && !(typeof data['virtualPath'] === 'string' || data['virtualPath'] instanceof String)) {
            throw new Error("Expected the field `virtualPath` to be a primitive type in the JSON string but got " + data['virtualPath']);
        }

        return true;
    }


}



/**
 * Physical path.
 * @member {String} physicalPath
 */
AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigVirtualApplicationsInnerVirtualDirectoriesInner.prototype['physicalPath'] = undefined;

/**
 * Path to virtual application.
 * @member {String} virtualPath
 */
AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigVirtualApplicationsInnerVirtualDirectoriesInner.prototype['virtualPath'] = undefined;






export default AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigVirtualApplicationsInnerVirtualDirectoriesInner;

