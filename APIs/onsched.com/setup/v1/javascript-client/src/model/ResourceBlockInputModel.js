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
import RepeatInputModel from './RepeatInputModel';

/**
 * The ResourceBlockInputModel model module.
 * @module model/ResourceBlockInputModel
 * @version v1
 */
class ResourceBlockInputModel {
    /**
     * Constructs a new <code>ResourceBlockInputModel</code>.
     * @alias module:model/ResourceBlockInputModel
     */
    constructor() { 
        
        ResourceBlockInputModel.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ResourceBlockInputModel</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ResourceBlockInputModel} obj Optional instance to populate.
     * @return {module:model/ResourceBlockInputModel} The populated <code>ResourceBlockInputModel</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ResourceBlockInputModel();

            if (data.hasOwnProperty('allDay')) {
                obj['allDay'] = ApiClient.convertToType(data['allDay'], 'Boolean');
            }
            if (data.hasOwnProperty('endDate')) {
                obj['endDate'] = ApiClient.convertToType(data['endDate'], 'Date');
            }
            if (data.hasOwnProperty('endTime')) {
                obj['endTime'] = ApiClient.convertToType(data['endTime'], 'Number');
            }
            if (data.hasOwnProperty('reason')) {
                obj['reason'] = ApiClient.convertToType(data['reason'], 'String');
            }
            if (data.hasOwnProperty('repeat')) {
                obj['repeat'] = RepeatInputModel.constructFromObject(data['repeat']);
            }
            if (data.hasOwnProperty('repeats')) {
                obj['repeats'] = ApiClient.convertToType(data['repeats'], 'Boolean');
            }
            if (data.hasOwnProperty('startDate')) {
                obj['startDate'] = ApiClient.convertToType(data['startDate'], 'Date');
            }
            if (data.hasOwnProperty('startTime')) {
                obj['startTime'] = ApiClient.convertToType(data['startTime'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ResourceBlockInputModel</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ResourceBlockInputModel</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['reason'] && !(typeof data['reason'] === 'string' || data['reason'] instanceof String)) {
            throw new Error("Expected the field `reason` to be a primitive type in the JSON string but got " + data['reason']);
        }
        // validate the optional field `repeat`
        if (data['repeat']) { // data not null
          RepeatInputModel.validateJSON(data['repeat']);
        }

        return true;
    }


}



/**
 * @member {Boolean} allDay
 */
ResourceBlockInputModel.prototype['allDay'] = undefined;

/**
 * @member {Date} endDate
 */
ResourceBlockInputModel.prototype['endDate'] = undefined;

/**
 * @member {Number} endTime
 */
ResourceBlockInputModel.prototype['endTime'] = undefined;

/**
 * @member {String} reason
 */
ResourceBlockInputModel.prototype['reason'] = undefined;

/**
 * @member {module:model/RepeatInputModel} repeat
 */
ResourceBlockInputModel.prototype['repeat'] = undefined;

/**
 * @member {Boolean} repeats
 */
ResourceBlockInputModel.prototype['repeats'] = undefined;

/**
 * @member {Date} startDate
 */
ResourceBlockInputModel.prototype['startDate'] = undefined;

/**
 * @member {Number} startTime
 */
ResourceBlockInputModel.prototype['startTime'] = undefined;






export default ResourceBlockInputModel;

