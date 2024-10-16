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
import ResourceBulkUpdateModel from './ResourceBulkUpdateModel';

/**
 * The ResourcesUpdateModel model module.
 * @module model/ResourcesUpdateModel
 * @version v1
 */
class ResourcesUpdateModel {
    /**
     * Constructs a new <code>ResourcesUpdateModel</code>.
     * @alias module:model/ResourcesUpdateModel
     */
    constructor() { 
        
        ResourcesUpdateModel.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ResourcesUpdateModel</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ResourcesUpdateModel} obj Optional instance to populate.
     * @return {module:model/ResourcesUpdateModel} The populated <code>ResourcesUpdateModel</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ResourcesUpdateModel();

            if (data.hasOwnProperty('resources')) {
                obj['resources'] = ApiClient.convertToType(data['resources'], [ResourceBulkUpdateModel]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ResourcesUpdateModel</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ResourcesUpdateModel</code>.
     */
    static validateJSON(data) {
        if (data['resources']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['resources'])) {
                throw new Error("Expected the field `resources` to be an array in the JSON data but got " + data['resources']);
            }
            // validate the optional field `resources` (array)
            for (const item of data['resources']) {
                ResourceBulkUpdateModel.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {Array.<module:model/ResourceBulkUpdateModel>} resources
 */
ResourcesUpdateModel.prototype['resources'] = undefined;






export default ResourcesUpdateModel;

