/**
 * Personnel Data
 * API for reading and writing personnel data incl. data about attendances and absences
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import CreateTimeOffPeriodResponseAllOfData from './CreateTimeOffPeriodResponseAllOfData';
import Response from './Response';

/**
 * The CreateTimeOffPeriodResponse model module.
 * @module model/CreateTimeOffPeriodResponse
 * @version 1.0
 */
class CreateTimeOffPeriodResponse {
    /**
     * Constructs a new <code>CreateTimeOffPeriodResponse</code>.
     * @alias module:model/CreateTimeOffPeriodResponse
     * @implements module:model/Response
     * @param data {module:model/CreateTimeOffPeriodResponseAllOfData} 
     * @param success {Boolean} 
     */
    constructor(data, success) { 
        Response.initialize(this, data, success);
        CreateTimeOffPeriodResponse.initialize(this, data, success);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, data, success) { 
        obj['data'] = data;
        obj['success'] = success;
    }

    /**
     * Constructs a <code>CreateTimeOffPeriodResponse</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CreateTimeOffPeriodResponse} obj Optional instance to populate.
     * @return {module:model/CreateTimeOffPeriodResponse} The populated <code>CreateTimeOffPeriodResponse</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CreateTimeOffPeriodResponse();
            Response.constructFromObject(data, obj);

            if (data.hasOwnProperty('data')) {
                obj['data'] = CreateTimeOffPeriodResponseAllOfData.constructFromObject(data['data']);
            }
            if (data.hasOwnProperty('success')) {
                obj['success'] = ApiClient.convertToType(data['success'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CreateTimeOffPeriodResponse</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CreateTimeOffPeriodResponse</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of CreateTimeOffPeriodResponse.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `data`
        if (data['data']) { // data not null
          CreateTimeOffPeriodResponseAllOfData.validateJSON(data['data']);
        }

        return true;
    }


}

CreateTimeOffPeriodResponse.RequiredProperties = ["data", "success"];

/**
 * @member {module:model/CreateTimeOffPeriodResponseAllOfData} data
 */
CreateTimeOffPeriodResponse.prototype['data'] = undefined;

/**
 * @member {Boolean} success
 */
CreateTimeOffPeriodResponse.prototype['success'] = undefined;


// Implement Response interface:
/**
 * @member {Object} data
 */
Response.prototype['data'] = undefined;
/**
 * @member {Boolean} success
 */
Response.prototype['success'] = undefined;




export default CreateTimeOffPeriodResponse;

