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
 * The SalesDataCreditmemoCommentCreationInterface model module.
 * @module model/SalesDataCreditmemoCommentCreationInterface
 * @version 2.2.10
 */
class SalesDataCreditmemoCommentCreationInterface {
    /**
     * Constructs a new <code>SalesDataCreditmemoCommentCreationInterface</code>.
     * Interface CreditmemoCommentCreationInterface
     * @alias module:model/SalesDataCreditmemoCommentCreationInterface
     * @param comment {String} Comment.
     * @param isVisibleOnFront {Number} Is-visible-on-storefront flag value.
     */
    constructor(comment, isVisibleOnFront) { 
        
        SalesDataCreditmemoCommentCreationInterface.initialize(this, comment, isVisibleOnFront);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, comment, isVisibleOnFront) { 
        obj['comment'] = comment;
        obj['is_visible_on_front'] = isVisibleOnFront;
    }

    /**
     * Constructs a <code>SalesDataCreditmemoCommentCreationInterface</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/SalesDataCreditmemoCommentCreationInterface} obj Optional instance to populate.
     * @return {module:model/SalesDataCreditmemoCommentCreationInterface} The populated <code>SalesDataCreditmemoCommentCreationInterface</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new SalesDataCreditmemoCommentCreationInterface();

            if (data.hasOwnProperty('comment')) {
                obj['comment'] = ApiClient.convertToType(data['comment'], 'String');
            }
            if (data.hasOwnProperty('extension_attributes')) {
                obj['extension_attributes'] = ApiClient.convertToType(data['extension_attributes'], Object);
            }
            if (data.hasOwnProperty('is_visible_on_front')) {
                obj['is_visible_on_front'] = ApiClient.convertToType(data['is_visible_on_front'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>SalesDataCreditmemoCommentCreationInterface</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>SalesDataCreditmemoCommentCreationInterface</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of SalesDataCreditmemoCommentCreationInterface.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['comment'] && !(typeof data['comment'] === 'string' || data['comment'] instanceof String)) {
            throw new Error("Expected the field `comment` to be a primitive type in the JSON string but got " + data['comment']);
        }

        return true;
    }


}

SalesDataCreditmemoCommentCreationInterface.RequiredProperties = ["comment", "is_visible_on_front"];

/**
 * Comment.
 * @member {String} comment
 */
SalesDataCreditmemoCommentCreationInterface.prototype['comment'] = undefined;

/**
 * ExtensionInterface class for @see \\Magento\\Sales\\Api\\Data\\CreditmemoCommentCreationInterface
 * @member {Object} extension_attributes
 */
SalesDataCreditmemoCommentCreationInterface.prototype['extension_attributes'] = undefined;

/**
 * Is-visible-on-storefront flag value.
 * @member {Number} is_visible_on_front
 */
SalesDataCreditmemoCommentCreationInterface.prototype['is_visible_on_front'] = undefined;






export default SalesDataCreditmemoCommentCreationInterface;

