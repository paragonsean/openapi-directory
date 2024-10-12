/**
 * Open States API v3
 *  * [More documentation](https://docs.openstates.org/en/latest/api/v3/index.html) * [Register for an account](https://openstates.org/accounts/signup/)   **We are currently working to restore experimental support for committees & events.**  During this period please note that data is not yet available for all states and the exact format of the new endpoints may change slightly depending on user feedback.  If you have any issues or questions use our [GitHub Issues](https://github.com/openstates/issues/issues) to give feedback. 
 *
 * The version of the OpenAPI document: 2021.11.12
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import Organization from './Organization';

/**
 * The BillAction model module.
 * @module model/BillAction
 * @version 2021.11.12
 */
class BillAction {
    /**
     * Constructs a new <code>BillAction</code>.
     * @alias module:model/BillAction
     * @param classification {Array.<String>} 
     * @param date {String} 
     * @param description {String} 
     * @param order {Number} 
     * @param organization {module:model/Organization} 
     */
    constructor(classification, date, description, order, organization) { 
        
        BillAction.initialize(this, classification, date, description, order, organization);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, classification, date, description, order, organization) { 
        obj['classification'] = classification;
        obj['date'] = date;
        obj['description'] = description;
        obj['order'] = order;
        obj['organization'] = organization;
    }

    /**
     * Constructs a <code>BillAction</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/BillAction} obj Optional instance to populate.
     * @return {module:model/BillAction} The populated <code>BillAction</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new BillAction();

            if (data.hasOwnProperty('classification')) {
                obj['classification'] = ApiClient.convertToType(data['classification'], ['String']);
            }
            if (data.hasOwnProperty('date')) {
                obj['date'] = ApiClient.convertToType(data['date'], 'String');
            }
            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
            }
            if (data.hasOwnProperty('order')) {
                obj['order'] = ApiClient.convertToType(data['order'], 'Number');
            }
            if (data.hasOwnProperty('organization')) {
                obj['organization'] = Organization.constructFromObject(data['organization']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>BillAction</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>BillAction</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of BillAction.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is an array
        if (!Array.isArray(data['classification'])) {
            throw new Error("Expected the field `classification` to be an array in the JSON data but got " + data['classification']);
        }
        // ensure the json data is a string
        if (data['date'] && !(typeof data['date'] === 'string' || data['date'] instanceof String)) {
            throw new Error("Expected the field `date` to be a primitive type in the JSON string but got " + data['date']);
        }
        // ensure the json data is a string
        if (data['description'] && !(typeof data['description'] === 'string' || data['description'] instanceof String)) {
            throw new Error("Expected the field `description` to be a primitive type in the JSON string but got " + data['description']);
        }
        // validate the optional field `organization`
        if (data['organization']) { // data not null
          Organization.validateJSON(data['organization']);
        }

        return true;
    }


}

BillAction.RequiredProperties = ["classification", "date", "description", "order", "organization"];

/**
 * @member {Array.<String>} classification
 */
BillAction.prototype['classification'] = undefined;

/**
 * @member {String} date
 */
BillAction.prototype['date'] = undefined;

/**
 * @member {String} description
 */
BillAction.prototype['description'] = undefined;

/**
 * @member {Number} order
 */
BillAction.prototype['order'] = undefined;

/**
 * @member {module:model/Organization} organization
 */
BillAction.prototype['organization'] = undefined;






export default BillAction;

