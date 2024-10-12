/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The CreateOrganizationActionBatchRequestActionsInner model module.
 * @module model/CreateOrganizationActionBatchRequestActionsInner
 * @version 1.32.0
 */
class CreateOrganizationActionBatchRequestActionsInner {
    /**
     * Constructs a new <code>CreateOrganizationActionBatchRequestActionsInner</code>.
     * @alias module:model/CreateOrganizationActionBatchRequestActionsInner
     * @param operation {String} The operation to be used
     * @param resource {String} Unique identifier for the resource to be acted on
     */
    constructor(operation, resource) { 
        
        CreateOrganizationActionBatchRequestActionsInner.initialize(this, operation, resource);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, operation, resource) { 
        obj['operation'] = operation;
        obj['resource'] = resource;
    }

    /**
     * Constructs a <code>CreateOrganizationActionBatchRequestActionsInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CreateOrganizationActionBatchRequestActionsInner} obj Optional instance to populate.
     * @return {module:model/CreateOrganizationActionBatchRequestActionsInner} The populated <code>CreateOrganizationActionBatchRequestActionsInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CreateOrganizationActionBatchRequestActionsInner();

            if (data.hasOwnProperty('body')) {
                obj['body'] = ApiClient.convertToType(data['body'], Object);
            }
            if (data.hasOwnProperty('operation')) {
                obj['operation'] = ApiClient.convertToType(data['operation'], 'String');
            }
            if (data.hasOwnProperty('resource')) {
                obj['resource'] = ApiClient.convertToType(data['resource'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CreateOrganizationActionBatchRequestActionsInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CreateOrganizationActionBatchRequestActionsInner</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of CreateOrganizationActionBatchRequestActionsInner.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['operation'] && !(typeof data['operation'] === 'string' || data['operation'] instanceof String)) {
            throw new Error("Expected the field `operation` to be a primitive type in the JSON string but got " + data['operation']);
        }
        // ensure the json data is a string
        if (data['resource'] && !(typeof data['resource'] === 'string' || data['resource'] instanceof String)) {
            throw new Error("Expected the field `resource` to be a primitive type in the JSON string but got " + data['resource']);
        }

        return true;
    }


}

CreateOrganizationActionBatchRequestActionsInner.RequiredProperties = ["operation", "resource"];

/**
 * The body of the action
 * @member {Object} body
 */
CreateOrganizationActionBatchRequestActionsInner.prototype['body'] = undefined;

/**
 * The operation to be used
 * @member {String} operation
 */
CreateOrganizationActionBatchRequestActionsInner.prototype['operation'] = undefined;

/**
 * Unique identifier for the resource to be acted on
 * @member {String} resource
 */
CreateOrganizationActionBatchRequestActionsInner.prototype['resource'] = undefined;






export default CreateOrganizationActionBatchRequestActionsInner;

