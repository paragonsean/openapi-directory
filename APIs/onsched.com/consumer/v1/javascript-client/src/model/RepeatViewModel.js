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
 * The RepeatViewModel model module.
 * @module model/RepeatViewModel
 * @version v1
 */
class RepeatViewModel {
    /**
     * Constructs a new <code>RepeatViewModel</code>.
     * @alias module:model/RepeatViewModel
     */
    constructor() { 
        
        RepeatViewModel.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>RepeatViewModel</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/RepeatViewModel} obj Optional instance to populate.
     * @return {module:model/RepeatViewModel} The populated <code>RepeatViewModel</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new RepeatViewModel();

            if (data.hasOwnProperty('frequency')) {
                obj['frequency'] = ApiClient.convertToType(data['frequency'], 'String');
            }
            if (data.hasOwnProperty('interval')) {
                obj['interval'] = ApiClient.convertToType(data['interval'], 'Number');
            }
            if (data.hasOwnProperty('monthDay')) {
                obj['monthDay'] = ApiClient.convertToType(data['monthDay'], 'String');
            }
            if (data.hasOwnProperty('monthType')) {
                obj['monthType'] = ApiClient.convertToType(data['monthType'], 'String');
            }
            if (data.hasOwnProperty('weekdays')) {
                obj['weekdays'] = ApiClient.convertToType(data['weekdays'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>RepeatViewModel</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>RepeatViewModel</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['frequency'] && !(typeof data['frequency'] === 'string' || data['frequency'] instanceof String)) {
            throw new Error("Expected the field `frequency` to be a primitive type in the JSON string but got " + data['frequency']);
        }
        // ensure the json data is a string
        if (data['monthDay'] && !(typeof data['monthDay'] === 'string' || data['monthDay'] instanceof String)) {
            throw new Error("Expected the field `monthDay` to be a primitive type in the JSON string but got " + data['monthDay']);
        }
        // ensure the json data is a string
        if (data['monthType'] && !(typeof data['monthType'] === 'string' || data['monthType'] instanceof String)) {
            throw new Error("Expected the field `monthType` to be a primitive type in the JSON string but got " + data['monthType']);
        }
        // ensure the json data is a string
        if (data['weekdays'] && !(typeof data['weekdays'] === 'string' || data['weekdays'] instanceof String)) {
            throw new Error("Expected the field `weekdays` to be a primitive type in the JSON string but got " + data['weekdays']);
        }

        return true;
    }


}



/**
 * @member {String} frequency
 */
RepeatViewModel.prototype['frequency'] = undefined;

/**
 * @member {Number} interval
 */
RepeatViewModel.prototype['interval'] = undefined;

/**
 * @member {String} monthDay
 */
RepeatViewModel.prototype['monthDay'] = undefined;

/**
 * @member {String} monthType
 */
RepeatViewModel.prototype['monthType'] = undefined;

/**
 * @member {String} weekdays
 */
RepeatViewModel.prototype['weekdays'] = undefined;






export default RepeatViewModel;

