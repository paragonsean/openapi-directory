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
 * The CustomFieldInputModel model module.
 * @module model/CustomFieldInputModel
 * @version v1
 */
class CustomFieldInputModel {
    /**
     * Constructs a new <code>CustomFieldInputModel</code>.
     * @alias module:model/CustomFieldInputModel
     */
    constructor() { 
        
        CustomFieldInputModel.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>CustomFieldInputModel</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CustomFieldInputModel} obj Optional instance to populate.
     * @return {module:model/CustomFieldInputModel} The populated <code>CustomFieldInputModel</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CustomFieldInputModel();

            if (data.hasOwnProperty('field1')) {
                obj['field1'] = ApiClient.convertToType(data['field1'], 'String');
            }
            if (data.hasOwnProperty('field10')) {
                obj['field10'] = ApiClient.convertToType(data['field10'], 'String');
            }
            if (data.hasOwnProperty('field2')) {
                obj['field2'] = ApiClient.convertToType(data['field2'], 'String');
            }
            if (data.hasOwnProperty('field3')) {
                obj['field3'] = ApiClient.convertToType(data['field3'], 'String');
            }
            if (data.hasOwnProperty('field4')) {
                obj['field4'] = ApiClient.convertToType(data['field4'], 'String');
            }
            if (data.hasOwnProperty('field5')) {
                obj['field5'] = ApiClient.convertToType(data['field5'], 'String');
            }
            if (data.hasOwnProperty('field6')) {
                obj['field6'] = ApiClient.convertToType(data['field6'], 'String');
            }
            if (data.hasOwnProperty('field7')) {
                obj['field7'] = ApiClient.convertToType(data['field7'], 'String');
            }
            if (data.hasOwnProperty('field8')) {
                obj['field8'] = ApiClient.convertToType(data['field8'], 'String');
            }
            if (data.hasOwnProperty('field9')) {
                obj['field9'] = ApiClient.convertToType(data['field9'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CustomFieldInputModel</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CustomFieldInputModel</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['field1'] && !(typeof data['field1'] === 'string' || data['field1'] instanceof String)) {
            throw new Error("Expected the field `field1` to be a primitive type in the JSON string but got " + data['field1']);
        }
        // ensure the json data is a string
        if (data['field10'] && !(typeof data['field10'] === 'string' || data['field10'] instanceof String)) {
            throw new Error("Expected the field `field10` to be a primitive type in the JSON string but got " + data['field10']);
        }
        // ensure the json data is a string
        if (data['field2'] && !(typeof data['field2'] === 'string' || data['field2'] instanceof String)) {
            throw new Error("Expected the field `field2` to be a primitive type in the JSON string but got " + data['field2']);
        }
        // ensure the json data is a string
        if (data['field3'] && !(typeof data['field3'] === 'string' || data['field3'] instanceof String)) {
            throw new Error("Expected the field `field3` to be a primitive type in the JSON string but got " + data['field3']);
        }
        // ensure the json data is a string
        if (data['field4'] && !(typeof data['field4'] === 'string' || data['field4'] instanceof String)) {
            throw new Error("Expected the field `field4` to be a primitive type in the JSON string but got " + data['field4']);
        }
        // ensure the json data is a string
        if (data['field5'] && !(typeof data['field5'] === 'string' || data['field5'] instanceof String)) {
            throw new Error("Expected the field `field5` to be a primitive type in the JSON string but got " + data['field5']);
        }
        // ensure the json data is a string
        if (data['field6'] && !(typeof data['field6'] === 'string' || data['field6'] instanceof String)) {
            throw new Error("Expected the field `field6` to be a primitive type in the JSON string but got " + data['field6']);
        }
        // ensure the json data is a string
        if (data['field7'] && !(typeof data['field7'] === 'string' || data['field7'] instanceof String)) {
            throw new Error("Expected the field `field7` to be a primitive type in the JSON string but got " + data['field7']);
        }
        // ensure the json data is a string
        if (data['field8'] && !(typeof data['field8'] === 'string' || data['field8'] instanceof String)) {
            throw new Error("Expected the field `field8` to be a primitive type in the JSON string but got " + data['field8']);
        }
        // ensure the json data is a string
        if (data['field9'] && !(typeof data['field9'] === 'string' || data['field9'] instanceof String)) {
            throw new Error("Expected the field `field9` to be a primitive type in the JSON string but got " + data['field9']);
        }

        return true;
    }


}



/**
 * @member {String} field1
 */
CustomFieldInputModel.prototype['field1'] = undefined;

/**
 * @member {String} field10
 */
CustomFieldInputModel.prototype['field10'] = undefined;

/**
 * @member {String} field2
 */
CustomFieldInputModel.prototype['field2'] = undefined;

/**
 * @member {String} field3
 */
CustomFieldInputModel.prototype['field3'] = undefined;

/**
 * @member {String} field4
 */
CustomFieldInputModel.prototype['field4'] = undefined;

/**
 * @member {String} field5
 */
CustomFieldInputModel.prototype['field5'] = undefined;

/**
 * @member {String} field6
 */
CustomFieldInputModel.prototype['field6'] = undefined;

/**
 * @member {String} field7
 */
CustomFieldInputModel.prototype['field7'] = undefined;

/**
 * @member {String} field8
 */
CustomFieldInputModel.prototype['field8'] = undefined;

/**
 * @member {String} field9
 */
CustomFieldInputModel.prototype['field9'] = undefined;






export default CustomFieldInputModel;

