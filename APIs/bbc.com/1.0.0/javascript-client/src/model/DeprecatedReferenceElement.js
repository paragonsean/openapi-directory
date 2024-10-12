/**
 * BBC Nitro API
 * BBC Nitro is the BBC's application programming interface (API) for BBC Programmes Metadata.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: nitro@bbc.co.uk
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import DeprecationAttributes from './DeprecationAttributes';
import ReferenceAttributes from './ReferenceAttributes';

/**
 * The DeprecatedReferenceElement model module.
 * @module model/DeprecatedReferenceElement
 * @version 1.0.0
 */
class DeprecatedReferenceElement {
    /**
     * Constructs a new <code>DeprecatedReferenceElement</code>.
     * @alias module:model/DeprecatedReferenceElement
     * @implements module:model/ReferenceAttributes
     * @implements module:model/DeprecationAttributes
     * @param href {String} 
     * @param resultType {String} 
     * @param deprecated {Boolean} 
     * @param deprecatedSince {String} 
     * @param replacedBy {String} 
     */
    constructor(href, resultType, deprecated, deprecatedSince, replacedBy) { 
        ReferenceAttributes.initialize(this, href, resultType);DeprecationAttributes.initialize(this, deprecated, deprecatedSince, replacedBy);
        DeprecatedReferenceElement.initialize(this, href, resultType, deprecated, deprecatedSince, replacedBy);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, href, resultType, deprecated, deprecatedSince, replacedBy) { 
        obj['href'] = href;
        obj['result_type'] = resultType;
        obj['deprecated'] = deprecated;
        obj['deprecated_since'] = deprecatedSince;
        obj['replaced_by'] = replacedBy;
    }

    /**
     * Constructs a <code>DeprecatedReferenceElement</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/DeprecatedReferenceElement} obj Optional instance to populate.
     * @return {module:model/DeprecatedReferenceElement} The populated <code>DeprecatedReferenceElement</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new DeprecatedReferenceElement();
            ReferenceAttributes.constructFromObject(data, obj);
            DeprecationAttributes.constructFromObject(data, obj);

            if (data.hasOwnProperty('href')) {
                obj['href'] = ApiClient.convertToType(data['href'], 'String');
            }
            if (data.hasOwnProperty('result_type')) {
                obj['result_type'] = ApiClient.convertToType(data['result_type'], 'String');
            }
            if (data.hasOwnProperty('deprecated')) {
                obj['deprecated'] = ApiClient.convertToType(data['deprecated'], 'Boolean');
            }
            if (data.hasOwnProperty('deprecated_since')) {
                obj['deprecated_since'] = ApiClient.convertToType(data['deprecated_since'], 'String');
            }
            if (data.hasOwnProperty('replaced_by')) {
                obj['replaced_by'] = ApiClient.convertToType(data['replaced_by'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>DeprecatedReferenceElement</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>DeprecatedReferenceElement</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of DeprecatedReferenceElement.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['href'] && !(typeof data['href'] === 'string' || data['href'] instanceof String)) {
            throw new Error("Expected the field `href` to be a primitive type in the JSON string but got " + data['href']);
        }
        // ensure the json data is a string
        if (data['result_type'] && !(typeof data['result_type'] === 'string' || data['result_type'] instanceof String)) {
            throw new Error("Expected the field `result_type` to be a primitive type in the JSON string but got " + data['result_type']);
        }
        // ensure the json data is a string
        if (data['deprecated_since'] && !(typeof data['deprecated_since'] === 'string' || data['deprecated_since'] instanceof String)) {
            throw new Error("Expected the field `deprecated_since` to be a primitive type in the JSON string but got " + data['deprecated_since']);
        }
        // ensure the json data is a string
        if (data['replaced_by'] && !(typeof data['replaced_by'] === 'string' || data['replaced_by'] instanceof String)) {
            throw new Error("Expected the field `replaced_by` to be a primitive type in the JSON string but got " + data['replaced_by']);
        }

        return true;
    }


}

DeprecatedReferenceElement.RequiredProperties = ["href", "result_type", "deprecated", "deprecated_since", "replaced_by"];

/**
 * @member {String} href
 */
DeprecatedReferenceElement.prototype['href'] = undefined;

/**
 * @member {String} result_type
 */
DeprecatedReferenceElement.prototype['result_type'] = undefined;

/**
 * @member {Boolean} deprecated
 */
DeprecatedReferenceElement.prototype['deprecated'] = undefined;

/**
 * @member {String} deprecated_since
 */
DeprecatedReferenceElement.prototype['deprecated_since'] = undefined;

/**
 * @member {String} replaced_by
 */
DeprecatedReferenceElement.prototype['replaced_by'] = undefined;


// Implement ReferenceAttributes interface:
/**
 * @member {String} href
 */
ReferenceAttributes.prototype['href'] = undefined;
/**
 * @member {String} result_type
 */
ReferenceAttributes.prototype['result_type'] = undefined;
// Implement DeprecationAttributes interface:
/**
 * @member {Boolean} deprecated
 */
DeprecationAttributes.prototype['deprecated'] = undefined;
/**
 * @member {String} deprecated_since
 */
DeprecationAttributes.prototype['deprecated_since'] = undefined;
/**
 * @member {String} replaced_by
 */
DeprecationAttributes.prototype['replaced_by'] = undefined;




export default DeprecatedReferenceElement;

