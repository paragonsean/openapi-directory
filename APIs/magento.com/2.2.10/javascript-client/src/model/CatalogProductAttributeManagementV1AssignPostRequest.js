/**
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The CatalogProductAttributeManagementV1AssignPostRequest model module.
 * @module model/CatalogProductAttributeManagementV1AssignPostRequest
 * @version 2.2.10
 */
class CatalogProductAttributeManagementV1AssignPostRequest {
    /**
     * Constructs a new <code>CatalogProductAttributeManagementV1AssignPostRequest</code>.
     * @alias module:model/CatalogProductAttributeManagementV1AssignPostRequest
     * @param attributeCode {String} 
     * @param attributeGroupId {Number} 
     * @param attributeSetId {Number} 
     * @param sortOrder {Number} 
     */
    constructor(attributeCode, attributeGroupId, attributeSetId, sortOrder) { 
        
        CatalogProductAttributeManagementV1AssignPostRequest.initialize(this, attributeCode, attributeGroupId, attributeSetId, sortOrder);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, attributeCode, attributeGroupId, attributeSetId, sortOrder) { 
        obj['attributeCode'] = attributeCode;
        obj['attributeGroupId'] = attributeGroupId;
        obj['attributeSetId'] = attributeSetId;
        obj['sortOrder'] = sortOrder;
    }

    /**
     * Constructs a <code>CatalogProductAttributeManagementV1AssignPostRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CatalogProductAttributeManagementV1AssignPostRequest} obj Optional instance to populate.
     * @return {module:model/CatalogProductAttributeManagementV1AssignPostRequest} The populated <code>CatalogProductAttributeManagementV1AssignPostRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CatalogProductAttributeManagementV1AssignPostRequest();

            if (data.hasOwnProperty('attributeCode')) {
                obj['attributeCode'] = ApiClient.convertToType(data['attributeCode'], 'String');
            }
            if (data.hasOwnProperty('attributeGroupId')) {
                obj['attributeGroupId'] = ApiClient.convertToType(data['attributeGroupId'], 'Number');
            }
            if (data.hasOwnProperty('attributeSetId')) {
                obj['attributeSetId'] = ApiClient.convertToType(data['attributeSetId'], 'Number');
            }
            if (data.hasOwnProperty('sortOrder')) {
                obj['sortOrder'] = ApiClient.convertToType(data['sortOrder'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CatalogProductAttributeManagementV1AssignPostRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CatalogProductAttributeManagementV1AssignPostRequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of CatalogProductAttributeManagementV1AssignPostRequest.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['attributeCode'] && !(typeof data['attributeCode'] === 'string' || data['attributeCode'] instanceof String)) {
            throw new Error("Expected the field `attributeCode` to be a primitive type in the JSON string but got " + data['attributeCode']);
        }

        return true;
    }


}

CatalogProductAttributeManagementV1AssignPostRequest.RequiredProperties = ["attributeCode", "attributeGroupId", "attributeSetId", "sortOrder"];

/**
 * @member {String} attributeCode
 */
CatalogProductAttributeManagementV1AssignPostRequest.prototype['attributeCode'] = undefined;

/**
 * @member {Number} attributeGroupId
 */
CatalogProductAttributeManagementV1AssignPostRequest.prototype['attributeGroupId'] = undefined;

/**
 * @member {Number} attributeSetId
 */
CatalogProductAttributeManagementV1AssignPostRequest.prototype['attributeSetId'] = undefined;

/**
 * @member {Number} sortOrder
 */
CatalogProductAttributeManagementV1AssignPostRequest.prototype['sortOrder'] = undefined;






export default CatalogProductAttributeManagementV1AssignPostRequest;

