/**
 * Mailscript
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.4.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import AddTriggerRequestCriteria from './AddTriggerRequestCriteria';

/**
 * The AddTriggerRequest model module.
 * @module model/AddTriggerRequest
 * @version 0.4.0
 */
class AddTriggerRequest {
    /**
     * Constructs a new <code>AddTriggerRequest</code>.
     * @alias module:model/AddTriggerRequest
     * @param criteria {module:model/AddTriggerRequestCriteria} 
     * @param name {String} 
     */
    constructor(criteria, name) { 
        
        AddTriggerRequest.initialize(this, criteria, name);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, criteria, name) { 
        obj['criteria'] = criteria;
        obj['name'] = name;
    }

    /**
     * Constructs a <code>AddTriggerRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AddTriggerRequest} obj Optional instance to populate.
     * @return {module:model/AddTriggerRequest} The populated <code>AddTriggerRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AddTriggerRequest();

            if (data.hasOwnProperty('criteria')) {
                obj['criteria'] = AddTriggerRequestCriteria.constructFromObject(data['criteria']);
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AddTriggerRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AddTriggerRequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of AddTriggerRequest.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `criteria`
        if (data['criteria']) { // data not null
          AddTriggerRequestCriteria.validateJSON(data['criteria']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }

        return true;
    }


}

AddTriggerRequest.RequiredProperties = ["criteria", "name"];

/**
 * @member {module:model/AddTriggerRequestCriteria} criteria
 */
AddTriggerRequest.prototype['criteria'] = undefined;

/**
 * @member {String} name
 */
AddTriggerRequest.prototype['name'] = undefined;






export default AddTriggerRequest;

