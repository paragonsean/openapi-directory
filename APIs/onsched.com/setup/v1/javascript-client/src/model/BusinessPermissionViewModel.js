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

/**
 * The BusinessPermissionViewModel model module.
 * @module model/BusinessPermissionViewModel
 * @version v1
 */
class BusinessPermissionViewModel {
    /**
     * Constructs a new <code>BusinessPermissionViewModel</code>.
     * @alias module:model/BusinessPermissionViewModel
     */
    constructor() { 
        
        BusinessPermissionViewModel.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>BusinessPermissionViewModel</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/BusinessPermissionViewModel} obj Optional instance to populate.
     * @return {module:model/BusinessPermissionViewModel} The populated <code>BusinessPermissionViewModel</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new BusinessPermissionViewModel();

            if (data.hasOwnProperty('access')) {
                obj['access'] = ApiClient.convertToType(data['access'], 'String');
            }
            if (data.hasOwnProperty('function')) {
                obj['function'] = ApiClient.convertToType(data['function'], 'String');
            }
            if (data.hasOwnProperty('object')) {
                obj['object'] = ApiClient.convertToType(data['object'], 'String');
            }
            if (data.hasOwnProperty('role')) {
                obj['role'] = ApiClient.convertToType(data['role'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>BusinessPermissionViewModel</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>BusinessPermissionViewModel</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['access'] && !(typeof data['access'] === 'string' || data['access'] instanceof String)) {
            throw new Error("Expected the field `access` to be a primitive type in the JSON string but got " + data['access']);
        }
        // ensure the json data is a string
        if (data['function'] && !(typeof data['function'] === 'string' || data['function'] instanceof String)) {
            throw new Error("Expected the field `function` to be a primitive type in the JSON string but got " + data['function']);
        }
        // ensure the json data is a string
        if (data['object'] && !(typeof data['object'] === 'string' || data['object'] instanceof String)) {
            throw new Error("Expected the field `object` to be a primitive type in the JSON string but got " + data['object']);
        }
        // ensure the json data is a string
        if (data['role'] && !(typeof data['role'] === 'string' || data['role'] instanceof String)) {
            throw new Error("Expected the field `role` to be a primitive type in the JSON string but got " + data['role']);
        }

        return true;
    }


}



/**
 * @member {String} access
 */
BusinessPermissionViewModel.prototype['access'] = undefined;

/**
 * @member {String} function
 */
BusinessPermissionViewModel.prototype['function'] = undefined;

/**
 * @member {String} object
 */
BusinessPermissionViewModel.prototype['object'] = undefined;

/**
 * @member {String} role
 */
BusinessPermissionViewModel.prototype['role'] = undefined;






export default BusinessPermissionViewModel;

