/**
 * Hotel Search API
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production for this API it may change dynamically. For your tests, use big cities like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 3.0.8
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The QualifiedFreeText model module.
 * @module model/QualifiedFreeText
 * @version 3.0.8
 */
class QualifiedFreeText {
    /**
     * Constructs a new <code>QualifiedFreeText</code>.
     * Specific type to convey a list of string for specific information type ( via qualifier) in specific character set, or language
     * @alias module:model/QualifiedFreeText
     */
    constructor() { 
        
        QualifiedFreeText.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>QualifiedFreeText</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/QualifiedFreeText} obj Optional instance to populate.
     * @return {module:model/QualifiedFreeText} The populated <code>QualifiedFreeText</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new QualifiedFreeText();

            if (data.hasOwnProperty('lang')) {
                obj['lang'] = ApiClient.convertToType(data['lang'], 'String');
            }
            if (data.hasOwnProperty('text')) {
                obj['text'] = ApiClient.convertToType(data['text'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>QualifiedFreeText</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>QualifiedFreeText</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['lang'] && !(typeof data['lang'] === 'string' || data['lang'] instanceof String)) {
            throw new Error("Expected the field `lang` to be a primitive type in the JSON string but got " + data['lang']);
        }
        // ensure the json data is a string
        if (data['text'] && !(typeof data['text'] === 'string' || data['text'] instanceof String)) {
            throw new Error("Expected the field `text` to be a primitive type in the JSON string but got " + data['text']);
        }

        return true;
    }


}



/**
 * see RFC 5646
 * @member {String} lang
 */
QualifiedFreeText.prototype['lang'] = undefined;

/**
 * Free Text
 * @member {String} text
 */
QualifiedFreeText.prototype['text'] = undefined;






export default QualifiedFreeText;

