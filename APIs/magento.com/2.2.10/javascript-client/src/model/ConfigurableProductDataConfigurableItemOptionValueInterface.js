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
 * The ConfigurableProductDataConfigurableItemOptionValueInterface model module.
 * @module model/ConfigurableProductDataConfigurableItemOptionValueInterface
 * @version 2.2.10
 */
class ConfigurableProductDataConfigurableItemOptionValueInterface {
    /**
     * Constructs a new <code>ConfigurableProductDataConfigurableItemOptionValueInterface</code>.
     * Interface ConfigurableItemOptionValueInterface
     * @alias module:model/ConfigurableProductDataConfigurableItemOptionValueInterface
     * @param optionId {String} Option SKU
     */
    constructor(optionId) { 
        
        ConfigurableProductDataConfigurableItemOptionValueInterface.initialize(this, optionId);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, optionId) { 
        obj['option_id'] = optionId;
    }

    /**
     * Constructs a <code>ConfigurableProductDataConfigurableItemOptionValueInterface</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ConfigurableProductDataConfigurableItemOptionValueInterface} obj Optional instance to populate.
     * @return {module:model/ConfigurableProductDataConfigurableItemOptionValueInterface} The populated <code>ConfigurableProductDataConfigurableItemOptionValueInterface</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ConfigurableProductDataConfigurableItemOptionValueInterface();

            if (data.hasOwnProperty('extension_attributes')) {
                obj['extension_attributes'] = ApiClient.convertToType(data['extension_attributes'], Object);
            }
            if (data.hasOwnProperty('option_id')) {
                obj['option_id'] = ApiClient.convertToType(data['option_id'], 'String');
            }
            if (data.hasOwnProperty('option_value')) {
                obj['option_value'] = ApiClient.convertToType(data['option_value'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ConfigurableProductDataConfigurableItemOptionValueInterface</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ConfigurableProductDataConfigurableItemOptionValueInterface</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of ConfigurableProductDataConfigurableItemOptionValueInterface.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['option_id'] && !(typeof data['option_id'] === 'string' || data['option_id'] instanceof String)) {
            throw new Error("Expected the field `option_id` to be a primitive type in the JSON string but got " + data['option_id']);
        }

        return true;
    }


}

ConfigurableProductDataConfigurableItemOptionValueInterface.RequiredProperties = ["option_id"];

/**
 * ExtensionInterface class for @see \\Magento\\ConfigurableProduct\\Api\\Data\\ConfigurableItemOptionValueInterface
 * @member {Object} extension_attributes
 */
ConfigurableProductDataConfigurableItemOptionValueInterface.prototype['extension_attributes'] = undefined;

/**
 * Option SKU
 * @member {String} option_id
 */
ConfigurableProductDataConfigurableItemOptionValueInterface.prototype['option_id'] = undefined;

/**
 * Item id
 * @member {Number} option_value
 */
ConfigurableProductDataConfigurableItemOptionValueInterface.prototype['option_value'] = undefined;






export default ConfigurableProductDataConfigurableItemOptionValueInterface;

