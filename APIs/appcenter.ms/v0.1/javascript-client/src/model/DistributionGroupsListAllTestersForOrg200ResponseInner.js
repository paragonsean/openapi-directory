/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The DistributionGroupsListAllTestersForOrg200ResponseInner model module.
 * @module model/DistributionGroupsListAllTestersForOrg200ResponseInner
 * @version v0.1
 */
class DistributionGroupsListAllTestersForOrg200ResponseInner {
    /**
     * Constructs a new <code>DistributionGroupsListAllTestersForOrg200ResponseInner</code>.
     * @alias module:model/DistributionGroupsListAllTestersForOrg200ResponseInner
     * @param email {String} The email address of the tester
     * @param name {String} The unique name that is used to identify the tester.
     */
    constructor(email, name) { 
        
        DistributionGroupsListAllTestersForOrg200ResponseInner.initialize(this, email, name);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, email, name) { 
        obj['email'] = email;
        obj['name'] = name;
    }

    /**
     * Constructs a <code>DistributionGroupsListAllTestersForOrg200ResponseInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/DistributionGroupsListAllTestersForOrg200ResponseInner} obj Optional instance to populate.
     * @return {module:model/DistributionGroupsListAllTestersForOrg200ResponseInner} The populated <code>DistributionGroupsListAllTestersForOrg200ResponseInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new DistributionGroupsListAllTestersForOrg200ResponseInner();

            if (data.hasOwnProperty('display_name')) {
                obj['display_name'] = ApiClient.convertToType(data['display_name'], 'String');
            }
            if (data.hasOwnProperty('email')) {
                obj['email'] = ApiClient.convertToType(data['email'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>DistributionGroupsListAllTestersForOrg200ResponseInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>DistributionGroupsListAllTestersForOrg200ResponseInner</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of DistributionGroupsListAllTestersForOrg200ResponseInner.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['display_name'] && !(typeof data['display_name'] === 'string' || data['display_name'] instanceof String)) {
            throw new Error("Expected the field `display_name` to be a primitive type in the JSON string but got " + data['display_name']);
        }
        // ensure the json data is a string
        if (data['email'] && !(typeof data['email'] === 'string' || data['email'] instanceof String)) {
            throw new Error("Expected the field `email` to be a primitive type in the JSON string but got " + data['email']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }

        return true;
    }


}

DistributionGroupsListAllTestersForOrg200ResponseInner.RequiredProperties = ["email", "name"];

/**
 * The full name of the tester. Might for example be first and last name
 * @member {String} display_name
 */
DistributionGroupsListAllTestersForOrg200ResponseInner.prototype['display_name'] = undefined;

/**
 * The email address of the tester
 * @member {String} email
 */
DistributionGroupsListAllTestersForOrg200ResponseInner.prototype['email'] = undefined;

/**
 * The unique name that is used to identify the tester.
 * @member {String} name
 */
DistributionGroupsListAllTestersForOrg200ResponseInner.prototype['name'] = undefined;






export default DistributionGroupsListAllTestersForOrg200ResponseInner;

