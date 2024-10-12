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

/**
 * The IssueListByService200ResponseValueInnerProperties model module.
 * @module model/IssueListByService200ResponseValueInnerProperties
 * @version 2019-01-01
 */
class IssueListByService200ResponseValueInnerProperties {
    /**
     * Constructs a new <code>IssueListByService200ResponseValueInnerProperties</code>.
     * Issue contract Properties.
     * @alias module:model/IssueListByService200ResponseValueInnerProperties
     * @param description {String} Text describing the issue.
     * @param title {String} The issue title.
     * @param userId {String} A resource identifier for the user created the issue.
     */
    constructor(description, title, userId) { 
        
        IssueListByService200ResponseValueInnerProperties.initialize(this, description, title, userId);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, description, title, userId) { 
        obj['description'] = description;
        obj['title'] = title;
        obj['userId'] = userId;
    }

    /**
     * Constructs a <code>IssueListByService200ResponseValueInnerProperties</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/IssueListByService200ResponseValueInnerProperties} obj Optional instance to populate.
     * @return {module:model/IssueListByService200ResponseValueInnerProperties} The populated <code>IssueListByService200ResponseValueInnerProperties</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new IssueListByService200ResponseValueInnerProperties();

            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
            }
            if (data.hasOwnProperty('title')) {
                obj['title'] = ApiClient.convertToType(data['title'], 'String');
            }
            if (data.hasOwnProperty('userId')) {
                obj['userId'] = ApiClient.convertToType(data['userId'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>IssueListByService200ResponseValueInnerProperties</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>IssueListByService200ResponseValueInnerProperties</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of IssueListByService200ResponseValueInnerProperties.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['description'] && !(typeof data['description'] === 'string' || data['description'] instanceof String)) {
            throw new Error("Expected the field `description` to be a primitive type in the JSON string but got " + data['description']);
        }
        // ensure the json data is a string
        if (data['title'] && !(typeof data['title'] === 'string' || data['title'] instanceof String)) {
            throw new Error("Expected the field `title` to be a primitive type in the JSON string but got " + data['title']);
        }
        // ensure the json data is a string
        if (data['userId'] && !(typeof data['userId'] === 'string' || data['userId'] instanceof String)) {
            throw new Error("Expected the field `userId` to be a primitive type in the JSON string but got " + data['userId']);
        }

        return true;
    }


}

IssueListByService200ResponseValueInnerProperties.RequiredProperties = ["description", "title", "userId"];

/**
 * Text describing the issue.
 * @member {String} description
 */
IssueListByService200ResponseValueInnerProperties.prototype['description'] = undefined;

/**
 * The issue title.
 * @member {String} title
 */
IssueListByService200ResponseValueInnerProperties.prototype['title'] = undefined;

/**
 * A resource identifier for the user created the issue.
 * @member {String} userId
 */
IssueListByService200ResponseValueInnerProperties.prototype['userId'] = undefined;






export default IssueListByService200ResponseValueInnerProperties;

