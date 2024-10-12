/**
 * ApiManagementClient
 * Use this REST API to get all the issues across an Azure Api Management service.
 *
 * The version of the OpenAPI document: 2019-01-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import IssueListByService200ResponseValueInnerProperties from './IssueListByService200ResponseValueInnerProperties';

/**
 * The IssueGet200Response model module.
 * @module model/IssueGet200Response
 * @version 2019-01-01
 */
class IssueGet200Response {
    /**
     * Constructs a new <code>IssueGet200Response</code>.
     * Issue Contract details.
     * @alias module:model/IssueGet200Response
     */
    constructor() { 
        
        IssueGet200Response.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>IssueGet200Response</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/IssueGet200Response} obj Optional instance to populate.
     * @return {module:model/IssueGet200Response} The populated <code>IssueGet200Response</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new IssueGet200Response();

            if (data.hasOwnProperty('properties')) {
                obj['properties'] = IssueListByService200ResponseValueInnerProperties.constructFromObject(data['properties']);
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>IssueGet200Response</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>IssueGet200Response</code>.
     */
    static validateJSON(data) {
        // validate the optional field `properties`
        if (data['properties']) { // data not null
          IssueListByService200ResponseValueInnerProperties.validateJSON(data['properties']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }

        return true;
    }


}



/**
 * @member {module:model/IssueListByService200ResponseValueInnerProperties} properties
 */
IssueGet200Response.prototype['properties'] = undefined;

/**
 * Resource ID.
 * @member {String} id
 */
IssueGet200Response.prototype['id'] = undefined;

/**
 * Resource name.
 * @member {String} name
 */
IssueGet200Response.prototype['name'] = undefined;

/**
 * Resource type for API Management resource.
 * @member {String} type
 */
IssueGet200Response.prototype['type'] = undefined;






export default IssueGet200Response;

