/**
 * ComputeManagementConvenienceClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2015-11-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The ParametersLink model module.
 * @module model/ParametersLink
 * @version 2015-11-01
 */
class ParametersLink {
    /**
     * Constructs a new <code>ParametersLink</code>.
     * Entity representing the reference to the deployment parameters.
     * @alias module:model/ParametersLink
     * @param uri {String} URI referencing the template.
     */
    constructor(uri) { 
        
        ParametersLink.initialize(this, uri);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, uri) { 
        obj['uri'] = uri;
    }

    /**
     * Constructs a <code>ParametersLink</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ParametersLink} obj Optional instance to populate.
     * @return {module:model/ParametersLink} The populated <code>ParametersLink</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ParametersLink();

            if (data.hasOwnProperty('contentVersion')) {
                obj['contentVersion'] = ApiClient.convertToType(data['contentVersion'], 'String');
            }
            if (data.hasOwnProperty('uri')) {
                obj['uri'] = ApiClient.convertToType(data['uri'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ParametersLink</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ParametersLink</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of ParametersLink.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['contentVersion'] && !(typeof data['contentVersion'] === 'string' || data['contentVersion'] instanceof String)) {
            throw new Error("Expected the field `contentVersion` to be a primitive type in the JSON string but got " + data['contentVersion']);
        }
        // ensure the json data is a string
        if (data['uri'] && !(typeof data['uri'] === 'string' || data['uri'] instanceof String)) {
            throw new Error("Expected the field `uri` to be a primitive type in the JSON string but got " + data['uri']);
        }

        return true;
    }


}

ParametersLink.RequiredProperties = ["uri"];

/**
 * If included it must match the ContentVersion in the template.
 * @member {String} contentVersion
 */
ParametersLink.prototype['contentVersion'] = undefined;

/**
 * URI referencing the template.
 * @member {String} uri
 */
ParametersLink.prototype['uri'] = undefined;






export default ParametersLink;

