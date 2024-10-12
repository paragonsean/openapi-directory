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
import AppServicePlansListWebApps200ResponseValueInnerIdentity from './AppServicePlansListWebApps200ResponseValueInnerIdentity';
import AppServicePlansListWebApps200ResponseValueInnerProperties from './AppServicePlansListWebApps200ResponseValueInnerProperties';

/**
 * The AppServicePlansListWebApps200ResponseValueInner model module.
 * @module model/AppServicePlansListWebApps200ResponseValueInner
 * @version 2018-02-01
 */
class AppServicePlansListWebApps200ResponseValueInner {
    /**
     * Constructs a new <code>AppServicePlansListWebApps200ResponseValueInner</code>.
     * A web app, a mobile app backend, or an API app.
     * @alias module:model/AppServicePlansListWebApps200ResponseValueInner
     */
    constructor() { 
        
        AppServicePlansListWebApps200ResponseValueInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>AppServicePlansListWebApps200ResponseValueInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AppServicePlansListWebApps200ResponseValueInner} obj Optional instance to populate.
     * @return {module:model/AppServicePlansListWebApps200ResponseValueInner} The populated <code>AppServicePlansListWebApps200ResponseValueInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AppServicePlansListWebApps200ResponseValueInner();

            if (data.hasOwnProperty('identity')) {
                obj['identity'] = AppServicePlansListWebApps200ResponseValueInnerIdentity.constructFromObject(data['identity']);
            }
            if (data.hasOwnProperty('properties')) {
                obj['properties'] = AppServicePlansListWebApps200ResponseValueInnerProperties.constructFromObject(data['properties']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AppServicePlansListWebApps200ResponseValueInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AppServicePlansListWebApps200ResponseValueInner</code>.
     */
    static validateJSON(data) {
        // validate the optional field `identity`
        if (data['identity']) { // data not null
          AppServicePlansListWebApps200ResponseValueInnerIdentity.validateJSON(data['identity']);
        }
        // validate the optional field `properties`
        if (data['properties']) { // data not null
          AppServicePlansListWebApps200ResponseValueInnerProperties.validateJSON(data['properties']);
        }

        return true;
    }


}



/**
 * @member {module:model/AppServicePlansListWebApps200ResponseValueInnerIdentity} identity
 */
AppServicePlansListWebApps200ResponseValueInner.prototype['identity'] = undefined;

/**
 * @member {module:model/AppServicePlansListWebApps200ResponseValueInnerProperties} properties
 */
AppServicePlansListWebApps200ResponseValueInner.prototype['properties'] = undefined;






export default AppServicePlansListWebApps200ResponseValueInner;

