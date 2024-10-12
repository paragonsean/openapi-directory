/**
 * Semantria
 * Semantria applies Text and Sentiment Analysis to tweets, facebook posts, surveys, reviews or enterprise content.
 *
 * The version of the OpenAPI document: 4.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import ConfigurationCollectionSection from './ConfigurationCollectionSection';
import ConfigurationDocumentSection from './ConfigurationDocumentSection';

/**
 * The ConfigurationUpdateVersion model module.
 * @module model/ConfigurationUpdateVersion
 * @version 4.0
 */
class ConfigurationUpdateVersion {
    /**
     * Constructs a new <code>ConfigurationUpdateVersion</code>.
     * @alias module:model/ConfigurationUpdateVersion
     * @param autoResponse {Boolean} Defines whether or not the service should respond with processed results automatically. Default: false
     * @param callback {String} Defines a callback URL for automatic data responding
     * @param categoriesThreshold {Number} Defines low threshold for strength score of user categories to be reported in the output. Default: 0.45
     * @param charsThreshold {Number} Defines the threshold for alphanumeric characters in the text in percent. Default: 80
     * @param collection {module:model/ConfigurationCollectionSection} 
     * @param configId {String} Unique configuration identifier
     * @param document {module:model/ConfigurationDocumentSection} 
     * @param entitiesThreshold {Number} Defines low threshold for evidence score of named and user entities to be reported in the output. Default: 55
     * @param isPrimary {Boolean} Identifies whether the current configuration is primary or not. Default: false
     * @param language {String} Defines target language that will be used for task processing. Default: English
     * @param name {String} Configuration name
     * @param oneSentence {Boolean} Leads the service to consider the entire document as single sentence. Default: false
     * @param processHtml {Boolean} Leads the service to clean HTML tags before processing. Default: false
     */
    constructor(autoResponse, callback, categoriesThreshold, charsThreshold, collection, configId, document, entitiesThreshold, isPrimary, language, name, oneSentence, processHtml) { 
        
        ConfigurationUpdateVersion.initialize(this, autoResponse, callback, categoriesThreshold, charsThreshold, collection, configId, document, entitiesThreshold, isPrimary, language, name, oneSentence, processHtml);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, autoResponse, callback, categoriesThreshold, charsThreshold, collection, configId, document, entitiesThreshold, isPrimary, language, name, oneSentence, processHtml) { 
        obj['auto_response'] = autoResponse;
        obj['callback'] = callback;
        obj['categories_threshold'] = categoriesThreshold;
        obj['chars_threshold'] = charsThreshold;
        obj['collection'] = collection;
        obj['config_id'] = configId;
        obj['document'] = document;
        obj['entities_threshold'] = entitiesThreshold;
        obj['is_primary'] = isPrimary;
        obj['language'] = language;
        obj['name'] = name;
        obj['one_sentence'] = oneSentence;
        obj['process_html'] = processHtml;
    }

    /**
     * Constructs a <code>ConfigurationUpdateVersion</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ConfigurationUpdateVersion} obj Optional instance to populate.
     * @return {module:model/ConfigurationUpdateVersion} The populated <code>ConfigurationUpdateVersion</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ConfigurationUpdateVersion();

            if (data.hasOwnProperty('auto_response')) {
                obj['auto_response'] = ApiClient.convertToType(data['auto_response'], 'Boolean');
            }
            if (data.hasOwnProperty('callback')) {
                obj['callback'] = ApiClient.convertToType(data['callback'], 'String');
            }
            if (data.hasOwnProperty('categories_threshold')) {
                obj['categories_threshold'] = ApiClient.convertToType(data['categories_threshold'], 'Number');
            }
            if (data.hasOwnProperty('chars_threshold')) {
                obj['chars_threshold'] = ApiClient.convertToType(data['chars_threshold'], 'Number');
            }
            if (data.hasOwnProperty('collection')) {
                obj['collection'] = ConfigurationCollectionSection.constructFromObject(data['collection']);
            }
            if (data.hasOwnProperty('config_id')) {
                obj['config_id'] = ApiClient.convertToType(data['config_id'], 'String');
            }
            if (data.hasOwnProperty('document')) {
                obj['document'] = ConfigurationDocumentSection.constructFromObject(data['document']);
            }
            if (data.hasOwnProperty('entities_threshold')) {
                obj['entities_threshold'] = ApiClient.convertToType(data['entities_threshold'], 'Number');
            }
            if (data.hasOwnProperty('is_primary')) {
                obj['is_primary'] = ApiClient.convertToType(data['is_primary'], 'Boolean');
            }
            if (data.hasOwnProperty('language')) {
                obj['language'] = ApiClient.convertToType(data['language'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('one_sentence')) {
                obj['one_sentence'] = ApiClient.convertToType(data['one_sentence'], 'Boolean');
            }
            if (data.hasOwnProperty('process_html')) {
                obj['process_html'] = ApiClient.convertToType(data['process_html'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ConfigurationUpdateVersion</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ConfigurationUpdateVersion</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of ConfigurationUpdateVersion.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['callback'] && !(typeof data['callback'] === 'string' || data['callback'] instanceof String)) {
            throw new Error("Expected the field `callback` to be a primitive type in the JSON string but got " + data['callback']);
        }
        // validate the optional field `collection`
        if (data['collection']) { // data not null
          ConfigurationCollectionSection.validateJSON(data['collection']);
        }
        // ensure the json data is a string
        if (data['config_id'] && !(typeof data['config_id'] === 'string' || data['config_id'] instanceof String)) {
            throw new Error("Expected the field `config_id` to be a primitive type in the JSON string but got " + data['config_id']);
        }
        // validate the optional field `document`
        if (data['document']) { // data not null
          ConfigurationDocumentSection.validateJSON(data['document']);
        }
        // ensure the json data is a string
        if (data['language'] && !(typeof data['language'] === 'string' || data['language'] instanceof String)) {
            throw new Error("Expected the field `language` to be a primitive type in the JSON string but got " + data['language']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }

        return true;
    }


}

ConfigurationUpdateVersion.RequiredProperties = ["auto_response", "callback", "categories_threshold", "chars_threshold", "collection", "config_id", "document", "entities_threshold", "is_primary", "language", "name", "one_sentence", "process_html"];

/**
 * Defines whether or not the service should respond with processed results automatically. Default: false
 * @member {Boolean} auto_response
 */
ConfigurationUpdateVersion.prototype['auto_response'] = undefined;

/**
 * Defines a callback URL for automatic data responding
 * @member {String} callback
 */
ConfigurationUpdateVersion.prototype['callback'] = undefined;

/**
 * Defines low threshold for strength score of user categories to be reported in the output. Default: 0.45
 * @member {Number} categories_threshold
 */
ConfigurationUpdateVersion.prototype['categories_threshold'] = undefined;

/**
 * Defines the threshold for alphanumeric characters in the text in percent. Default: 80
 * @member {Number} chars_threshold
 */
ConfigurationUpdateVersion.prototype['chars_threshold'] = undefined;

/**
 * @member {module:model/ConfigurationCollectionSection} collection
 */
ConfigurationUpdateVersion.prototype['collection'] = undefined;

/**
 * Unique configuration identifier
 * @member {String} config_id
 */
ConfigurationUpdateVersion.prototype['config_id'] = undefined;

/**
 * @member {module:model/ConfigurationDocumentSection} document
 */
ConfigurationUpdateVersion.prototype['document'] = undefined;

/**
 * Defines low threshold for evidence score of named and user entities to be reported in the output. Default: 55
 * @member {Number} entities_threshold
 */
ConfigurationUpdateVersion.prototype['entities_threshold'] = undefined;

/**
 * Identifies whether the current configuration is primary or not. Default: false
 * @member {Boolean} is_primary
 */
ConfigurationUpdateVersion.prototype['is_primary'] = undefined;

/**
 * Defines target language that will be used for task processing. Default: English
 * @member {String} language
 */
ConfigurationUpdateVersion.prototype['language'] = undefined;

/**
 * Configuration name
 * @member {String} name
 */
ConfigurationUpdateVersion.prototype['name'] = undefined;

/**
 * Leads the service to consider the entire document as single sentence. Default: false
 * @member {Boolean} one_sentence
 */
ConfigurationUpdateVersion.prototype['one_sentence'] = undefined;

/**
 * Leads the service to clean HTML tags before processing. Default: false
 * @member {Boolean} process_html
 */
ConfigurationUpdateVersion.prototype['process_html'] = undefined;






export default ConfigurationUpdateVersion;

