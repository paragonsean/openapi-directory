/**
 * OnSched Consumer API
 * Build secure and scalable custom apps for Online Booking. Our flexible API provides many options for availability and booking.  <br><br>  Take the API for a test drive. Just click on the Authorize button below and authenticate.   You can access our demo company profile if you are not a customer, or your own profile by using your assigned ClientId and Secret.  <br><br>  The API has two interfaces, consumer and setup.   <ul>  <li>  The consumer interface provides all the endpoints required for implementing consumer booking flows.  </li>  <li>  The setup interface provides endpoints for profile configuration and setup.  </li>  </ul>  Toggle freely between the two interfaces using the swagger tool bar option labelled 'Select a definition'.  
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

/**
 * The BusinessHolidayViewModel model module.
 * @module model/BusinessHolidayViewModel
 * @version v1
 */
class BusinessHolidayViewModel {
    /**
     * Constructs a new <code>BusinessHolidayViewModel</code>.
     * @alias module:model/BusinessHolidayViewModel
     */
    constructor() { 
        
        BusinessHolidayViewModel.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>BusinessHolidayViewModel</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/BusinessHolidayViewModel} obj Optional instance to populate.
     * @return {module:model/BusinessHolidayViewModel} The populated <code>BusinessHolidayViewModel</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new BusinessHolidayViewModel();

            if (data.hasOwnProperty('businessClosed')) {
                obj['businessClosed'] = ApiClient.convertToType(data['businessClosed'], 'Boolean');
            }
            if (data.hasOwnProperty('holidayName')) {
                obj['holidayName'] = ApiClient.convertToType(data['holidayName'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('publicHolidayId')) {
                obj['publicHolidayId'] = ApiClient.convertToType(data['publicHolidayId'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>BusinessHolidayViewModel</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>BusinessHolidayViewModel</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['holidayName'] && !(typeof data['holidayName'] === 'string' || data['holidayName'] instanceof String)) {
            throw new Error("Expected the field `holidayName` to be a primitive type in the JSON string but got " + data['holidayName']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }

        return true;
    }


}



/**
 * @member {Boolean} businessClosed
 */
BusinessHolidayViewModel.prototype['businessClosed'] = undefined;

/**
 * @member {String} holidayName
 */
BusinessHolidayViewModel.prototype['holidayName'] = undefined;

/**
 * @member {String} id
 */
BusinessHolidayViewModel.prototype['id'] = undefined;

/**
 * @member {Number} publicHolidayId
 */
BusinessHolidayViewModel.prototype['publicHolidayId'] = undefined;






export default BusinessHolidayViewModel;

