/**
 * OnSched Setup API
 * Build secure and scalable custom apps for onboarding and setup. Our flexible API provides many options for configuration.  <br><br>  Take the API for a test drive. Just click on the Authorize button below and authenticate.   You can access our demo company profile if you are not a customer, or your own profile by using your assigned ClientId and Secret.  <br><br>  The API has two interfaces, consumer and setup.   <ul>  <li>  The consumer interface provides all the endpoints required for implementing consumer booking flows.  </li>  <li>  The setup interface provides endpoints for profile configuration and setup.  </li>  </ul>  Toggle freely between the two interfaces using the swagger tool bar option labelled 'Select a definition'.  
 *
 * The version of the OpenAPI document: v1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import TimezonesViewModel from './TimezonesViewModel';

/**
 * The TimezoneViewModel model module.
 * @module model/TimezoneViewModel
 * @version v1
 */
class TimezoneViewModel {
    /**
     * Constructs a new <code>TimezoneViewModel</code>.
     * @alias module:model/TimezoneViewModel
     */
    constructor() { 
        
        TimezoneViewModel.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>TimezoneViewModel</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/TimezoneViewModel} obj Optional instance to populate.
     * @return {module:model/TimezoneViewModel} The populated <code>TimezoneViewModel</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new TimezoneViewModel();

            if (data.hasOwnProperty('object')) {
                obj['object'] = ApiClient.convertToType(data['object'], 'String');
            }
            if (data.hasOwnProperty('regions')) {
                obj['regions'] = ApiClient.convertToType(data['regions'], ['String']);
            }
            if (data.hasOwnProperty('timezones')) {
                obj['timezones'] = ApiClient.convertToType(data['timezones'], [TimezonesViewModel]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>TimezoneViewModel</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>TimezoneViewModel</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['object'] && !(typeof data['object'] === 'string' || data['object'] instanceof String)) {
            throw new Error("Expected the field `object` to be a primitive type in the JSON string but got " + data['object']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['regions'])) {
            throw new Error("Expected the field `regions` to be an array in the JSON data but got " + data['regions']);
        }
        if (data['timezones']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['timezones'])) {
                throw new Error("Expected the field `timezones` to be an array in the JSON data but got " + data['timezones']);
            }
            // validate the optional field `timezones` (array)
            for (const item of data['timezones']) {
                TimezonesViewModel.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {String} object
 */
TimezoneViewModel.prototype['object'] = undefined;

/**
 * @member {Array.<String>} regions
 */
TimezoneViewModel.prototype['regions'] = undefined;

/**
 * @member {Array.<module:model/TimezonesViewModel>} timezones
 */
TimezoneViewModel.prototype['timezones'] = undefined;






export default TimezoneViewModel;

