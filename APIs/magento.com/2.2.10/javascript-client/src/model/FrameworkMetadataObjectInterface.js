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
 * The FrameworkMetadataObjectInterface model module.
 * @module model/FrameworkMetadataObjectInterface
 * @version 2.2.10
 */
class FrameworkMetadataObjectInterface {
    /**
     * Constructs a new <code>FrameworkMetadataObjectInterface</code>.
     * Provides metadata about an attribute.
     * @alias module:model/FrameworkMetadataObjectInterface
     * @param attributeCode {String} Code of the attribute.
     */
    constructor(attributeCode) { 
        
        FrameworkMetadataObjectInterface.initialize(this, attributeCode);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, attributeCode) { 
        obj['attribute_code'] = attributeCode;
    }

    /**
     * Constructs a <code>FrameworkMetadataObjectInterface</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/FrameworkMetadataObjectInterface} obj Optional instance to populate.
     * @return {module:model/FrameworkMetadataObjectInterface} The populated <code>FrameworkMetadataObjectInterface</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new FrameworkMetadataObjectInterface();

            if (data.hasOwnProperty('attribute_code')) {
                obj['attribute_code'] = ApiClient.convertToType(data['attribute_code'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>FrameworkMetadataObjectInterface</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>FrameworkMetadataObjectInterface</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of FrameworkMetadataObjectInterface.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['attribute_code'] && !(typeof data['attribute_code'] === 'string' || data['attribute_code'] instanceof String)) {
            throw new Error("Expected the field `attribute_code` to be a primitive type in the JSON string but got " + data['attribute_code']);
        }

        return true;
    }


}

FrameworkMetadataObjectInterface.RequiredProperties = ["attribute_code"];

/**
 * Code of the attribute.
 * @member {String} attribute_code
 */
FrameworkMetadataObjectInterface.prototype['attribute_code'] = undefined;






export default FrameworkMetadataObjectInterface;

