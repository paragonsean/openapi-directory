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

/**
 * The ConfigurationDocumentSection model module.
 * @module model/ConfigurationDocumentSection
 * @version 4.0
 */
class ConfigurationDocumentSection {
    /**
     * Constructs a new <code>ConfigurationDocumentSection</code>.
     * @alias module:model/ConfigurationDocumentSection
     * @param autoCategoriesLimit {Number} Limits the number of auto categories the service responds. Default: 5
     * @param conceptTopicsLimit {Number} Limits the number of concept topics the service responds. Default: 5
     * @param detectLanguage {Boolean} Switches on language detection feature. Default: true
     * @param entityThemesLimit {Number} Limits the number of entity themes the service responds. Default: 0
     * @param intentions {Boolean} Switches on intentions detection feature. Default: false
     * @param modelSentiment {Boolean} Switches on/off model-based sentiment feature. Default: false
     * @param namedEntitiesLimit {Number} Limits the number of named entities the service responds. Default: 5
     * @param namedMentionsLimit {Number} Limits the number of named entity related mentions. Default: 0
     * @param namedOpinionsLimit {Number} Limits the number of named entity opinions the service responds. Default: 0
     * @param namedRelationsLimit {Number} Limits the number of named entity relations the service responds. Default: 0
     * @param phrasesLimit {Number} Limits the number of responded sentiment-bearing phrases for document. Default: 0
     * @param posTypes {module:model/ConfigurationDocumentSection.PosTypesEnum} Defines parts-of-speech which will be responded by the server
     * @param possiblePhrasesLimit {Number} Limits the number of responded possible phrases which may affect on sentiment score extraction. Default: 0
     * @param queryTopicsLimit {Number} Limits the number of query topics the service responds. Default: 5
     * @param summaryLimit {Number} Limits the number of sentences for the document summary feature. Default: 3
     * @param themeMentionsLimit {Number} Limits the number of document and entity related theme mentions. Default: 0
     * @param themesLimit {Number} Limits the number of document themes the service responds. Default: 0
     * @param userEntitiesLimit {Number} Limits the number of user entities the service responds. Default: 5
     * @param userMentionsLimit {Number} Limits the number of user entity related mentions. Default: 0
     * @param userOpinionsLimit {Number} Limits the number of concept topics the service responds. Default: 0
     * @param userRelationsLimit {Number} Limits the number of user entity relations the service responds. Default: 0
     */
    constructor(autoCategoriesLimit, conceptTopicsLimit, detectLanguage, entityThemesLimit, intentions, modelSentiment, namedEntitiesLimit, namedMentionsLimit, namedOpinionsLimit, namedRelationsLimit, phrasesLimit, posTypes, possiblePhrasesLimit, queryTopicsLimit, summaryLimit, themeMentionsLimit, themesLimit, userEntitiesLimit, userMentionsLimit, userOpinionsLimit, userRelationsLimit) { 
        
        ConfigurationDocumentSection.initialize(this, autoCategoriesLimit, conceptTopicsLimit, detectLanguage, entityThemesLimit, intentions, modelSentiment, namedEntitiesLimit, namedMentionsLimit, namedOpinionsLimit, namedRelationsLimit, phrasesLimit, posTypes, possiblePhrasesLimit, queryTopicsLimit, summaryLimit, themeMentionsLimit, themesLimit, userEntitiesLimit, userMentionsLimit, userOpinionsLimit, userRelationsLimit);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, autoCategoriesLimit, conceptTopicsLimit, detectLanguage, entityThemesLimit, intentions, modelSentiment, namedEntitiesLimit, namedMentionsLimit, namedOpinionsLimit, namedRelationsLimit, phrasesLimit, posTypes, possiblePhrasesLimit, queryTopicsLimit, summaryLimit, themeMentionsLimit, themesLimit, userEntitiesLimit, userMentionsLimit, userOpinionsLimit, userRelationsLimit) { 
        obj['auto_categories_limit'] = autoCategoriesLimit;
        obj['concept_topics_limit'] = conceptTopicsLimit;
        obj['detect_language'] = detectLanguage;
        obj['entity_themes_limit'] = entityThemesLimit;
        obj['intentions'] = intentions;
        obj['model_sentiment'] = modelSentiment;
        obj['named_entities_limit'] = namedEntitiesLimit;
        obj['named_mentions_limit'] = namedMentionsLimit;
        obj['named_opinions_limit'] = namedOpinionsLimit;
        obj['named_relations_limit'] = namedRelationsLimit;
        obj['phrases_limit'] = phrasesLimit;
        obj['pos_types'] = posTypes;
        obj['possible_phrases_limit'] = possiblePhrasesLimit;
        obj['query_topics_limit'] = queryTopicsLimit;
        obj['summary_limit'] = summaryLimit;
        obj['theme_mentions_limit'] = themeMentionsLimit;
        obj['themes_limit'] = themesLimit;
        obj['user_entities_limit'] = userEntitiesLimit;
        obj['user_mentions_limit'] = userMentionsLimit;
        obj['user_opinions_limit'] = userOpinionsLimit;
        obj['user_relations_limit'] = userRelationsLimit;
    }

    /**
     * Constructs a <code>ConfigurationDocumentSection</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ConfigurationDocumentSection} obj Optional instance to populate.
     * @return {module:model/ConfigurationDocumentSection} The populated <code>ConfigurationDocumentSection</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ConfigurationDocumentSection();

            if (data.hasOwnProperty('auto_categories_limit')) {
                obj['auto_categories_limit'] = ApiClient.convertToType(data['auto_categories_limit'], 'Number');
            }
            if (data.hasOwnProperty('concept_topics_limit')) {
                obj['concept_topics_limit'] = ApiClient.convertToType(data['concept_topics_limit'], 'Number');
            }
            if (data.hasOwnProperty('detect_language')) {
                obj['detect_language'] = ApiClient.convertToType(data['detect_language'], 'Boolean');
            }
            if (data.hasOwnProperty('entity_themes_limit')) {
                obj['entity_themes_limit'] = ApiClient.convertToType(data['entity_themes_limit'], 'Number');
            }
            if (data.hasOwnProperty('intentions')) {
                obj['intentions'] = ApiClient.convertToType(data['intentions'], 'Boolean');
            }
            if (data.hasOwnProperty('model_sentiment')) {
                obj['model_sentiment'] = ApiClient.convertToType(data['model_sentiment'], 'Boolean');
            }
            if (data.hasOwnProperty('named_entities_limit')) {
                obj['named_entities_limit'] = ApiClient.convertToType(data['named_entities_limit'], 'Number');
            }
            if (data.hasOwnProperty('named_mentions_limit')) {
                obj['named_mentions_limit'] = ApiClient.convertToType(data['named_mentions_limit'], 'Number');
            }
            if (data.hasOwnProperty('named_opinions_limit')) {
                obj['named_opinions_limit'] = ApiClient.convertToType(data['named_opinions_limit'], 'Number');
            }
            if (data.hasOwnProperty('named_relations_limit')) {
                obj['named_relations_limit'] = ApiClient.convertToType(data['named_relations_limit'], 'Number');
            }
            if (data.hasOwnProperty('phrases_limit')) {
                obj['phrases_limit'] = ApiClient.convertToType(data['phrases_limit'], 'Number');
            }
            if (data.hasOwnProperty('pos_types')) {
                obj['pos_types'] = ApiClient.convertToType(data['pos_types'], 'String');
            }
            if (data.hasOwnProperty('possible_phrases_limit')) {
                obj['possible_phrases_limit'] = ApiClient.convertToType(data['possible_phrases_limit'], 'Number');
            }
            if (data.hasOwnProperty('query_topics_limit')) {
                obj['query_topics_limit'] = ApiClient.convertToType(data['query_topics_limit'], 'Number');
            }
            if (data.hasOwnProperty('summary_limit')) {
                obj['summary_limit'] = ApiClient.convertToType(data['summary_limit'], 'Number');
            }
            if (data.hasOwnProperty('theme_mentions_limit')) {
                obj['theme_mentions_limit'] = ApiClient.convertToType(data['theme_mentions_limit'], 'Number');
            }
            if (data.hasOwnProperty('themes_limit')) {
                obj['themes_limit'] = ApiClient.convertToType(data['themes_limit'], 'Number');
            }
            if (data.hasOwnProperty('user_entities_limit')) {
                obj['user_entities_limit'] = ApiClient.convertToType(data['user_entities_limit'], 'Number');
            }
            if (data.hasOwnProperty('user_mentions_limit')) {
                obj['user_mentions_limit'] = ApiClient.convertToType(data['user_mentions_limit'], 'Number');
            }
            if (data.hasOwnProperty('user_opinions_limit')) {
                obj['user_opinions_limit'] = ApiClient.convertToType(data['user_opinions_limit'], 'Number');
            }
            if (data.hasOwnProperty('user_relations_limit')) {
                obj['user_relations_limit'] = ApiClient.convertToType(data['user_relations_limit'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ConfigurationDocumentSection</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ConfigurationDocumentSection</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of ConfigurationDocumentSection.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['pos_types'] && !(typeof data['pos_types'] === 'string' || data['pos_types'] instanceof String)) {
            throw new Error("Expected the field `pos_types` to be a primitive type in the JSON string but got " + data['pos_types']);
        }

        return true;
    }


}

ConfigurationDocumentSection.RequiredProperties = ["auto_categories_limit", "concept_topics_limit", "detect_language", "entity_themes_limit", "intentions", "model_sentiment", "named_entities_limit", "named_mentions_limit", "named_opinions_limit", "named_relations_limit", "phrases_limit", "pos_types", "possible_phrases_limit", "query_topics_limit", "summary_limit", "theme_mentions_limit", "themes_limit", "user_entities_limit", "user_mentions_limit", "user_opinions_limit", "user_relations_limit"];

/**
 * Limits the number of auto categories the service responds. Default: 5
 * @member {Number} auto_categories_limit
 */
ConfigurationDocumentSection.prototype['auto_categories_limit'] = undefined;

/**
 * Limits the number of concept topics the service responds. Default: 5
 * @member {Number} concept_topics_limit
 */
ConfigurationDocumentSection.prototype['concept_topics_limit'] = undefined;

/**
 * Switches on language detection feature. Default: true
 * @member {Boolean} detect_language
 */
ConfigurationDocumentSection.prototype['detect_language'] = undefined;

/**
 * Limits the number of entity themes the service responds. Default: 0
 * @member {Number} entity_themes_limit
 */
ConfigurationDocumentSection.prototype['entity_themes_limit'] = undefined;

/**
 * Switches on intentions detection feature. Default: false
 * @member {Boolean} intentions
 */
ConfigurationDocumentSection.prototype['intentions'] = undefined;

/**
 * Switches on/off model-based sentiment feature. Default: false
 * @member {Boolean} model_sentiment
 */
ConfigurationDocumentSection.prototype['model_sentiment'] = undefined;

/**
 * Limits the number of named entities the service responds. Default: 5
 * @member {Number} named_entities_limit
 */
ConfigurationDocumentSection.prototype['named_entities_limit'] = undefined;

/**
 * Limits the number of named entity related mentions. Default: 0
 * @member {Number} named_mentions_limit
 */
ConfigurationDocumentSection.prototype['named_mentions_limit'] = undefined;

/**
 * Limits the number of named entity opinions the service responds. Default: 0
 * @member {Number} named_opinions_limit
 */
ConfigurationDocumentSection.prototype['named_opinions_limit'] = undefined;

/**
 * Limits the number of named entity relations the service responds. Default: 0
 * @member {Number} named_relations_limit
 */
ConfigurationDocumentSection.prototype['named_relations_limit'] = undefined;

/**
 * Limits the number of responded sentiment-bearing phrases for document. Default: 0
 * @member {Number} phrases_limit
 */
ConfigurationDocumentSection.prototype['phrases_limit'] = undefined;

/**
 * Defines parts-of-speech which will be responded by the server
 * @member {module:model/ConfigurationDocumentSection.PosTypesEnum} pos_types
 */
ConfigurationDocumentSection.prototype['pos_types'] = undefined;

/**
 * Limits the number of responded possible phrases which may affect on sentiment score extraction. Default: 0
 * @member {Number} possible_phrases_limit
 */
ConfigurationDocumentSection.prototype['possible_phrases_limit'] = undefined;

/**
 * Limits the number of query topics the service responds. Default: 5
 * @member {Number} query_topics_limit
 */
ConfigurationDocumentSection.prototype['query_topics_limit'] = undefined;

/**
 * Limits the number of sentences for the document summary feature. Default: 3
 * @member {Number} summary_limit
 */
ConfigurationDocumentSection.prototype['summary_limit'] = undefined;

/**
 * Limits the number of document and entity related theme mentions. Default: 0
 * @member {Number} theme_mentions_limit
 */
ConfigurationDocumentSection.prototype['theme_mentions_limit'] = undefined;

/**
 * Limits the number of document themes the service responds. Default: 0
 * @member {Number} themes_limit
 */
ConfigurationDocumentSection.prototype['themes_limit'] = undefined;

/**
 * Limits the number of user entities the service responds. Default: 5
 * @member {Number} user_entities_limit
 */
ConfigurationDocumentSection.prototype['user_entities_limit'] = undefined;

/**
 * Limits the number of user entity related mentions. Default: 0
 * @member {Number} user_mentions_limit
 */
ConfigurationDocumentSection.prototype['user_mentions_limit'] = undefined;

/**
 * Limits the number of concept topics the service responds. Default: 0
 * @member {Number} user_opinions_limit
 */
ConfigurationDocumentSection.prototype['user_opinions_limit'] = undefined;

/**
 * Limits the number of user entity relations the service responds. Default: 0
 * @member {Number} user_relations_limit
 */
ConfigurationDocumentSection.prototype['user_relations_limit'] = undefined;





/**
 * Allowed values for the <code>pos_types</code> property.
 * @enum {String}
 * @readonly
 */
ConfigurationDocumentSection['PosTypesEnum'] = {

    /**
     * value: "All"
     * @const
     */
    "All": "All",

    /**
     * value: "Noun"
     * @const
     */
    "Noun": "Noun",

    /**
     * value: "Verb"
     * @const
     */
    "Verb": "Verb",

    /**
     * value: "Adjective"
     * @const
     */
    "Adjective": "Adjective",

    /**
     * value: "Determiner"
     * @const
     */
    "Determiner": "Determiner",

    /**
     * value: "Misc"
     * @const
     */
    "Misc": "Misc",

    /**
     * value: "Twitter"
     * @const
     */
    "Twitter": "Twitter",

    /**
     * value: "Chinese"
     * @const
     */
    "Chinese": "Chinese"
};



export default ConfigurationDocumentSection;

