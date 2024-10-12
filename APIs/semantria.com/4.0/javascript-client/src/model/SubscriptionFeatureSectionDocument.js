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
 * The SubscriptionFeatureSectionDocument model module.
 * @module model/SubscriptionFeatureSectionDocument
 * @version 4.0
 */
class SubscriptionFeatureSectionDocument {
    /**
     * Constructs a new <code>SubscriptionFeatureSectionDocument</code>.
     * @alias module:model/SubscriptionFeatureSectionDocument
     * @param autoCategories {Boolean} Indicates whether auto categories feature is allowed or not
     * @param conceptTopics {Boolean} Indicates whether concept topics are allowed or not
     * @param entityThemes {Boolean} Indicates whether entity themes feature is allowed or not
     * @param intentions {Boolean} Indicates whether intentions feature is allowed or not.
     * @param languageDetection {Boolean} Indicates whether language detection feature is allowed or not
     * @param mentions {Boolean} Indicates whether mentions for entities and themes are allowed or not
     * @param modelSentiment {Boolean} Indicates whether model-based sentiment feature is allowed or not
     * @param namedEntities {Boolean} Indicates whether named entities feature is allowed or not
     * @param namedRelations {Boolean} Indicates whether relations for named entities are allowed or not
     * @param opinions {Boolean} Indicates whether opinions feature is allowed or not
     * @param phrasesDetection {Boolean} Indicates whether possible phrases detection feature is allowed or not
     * @param posTagging {Boolean} Indicates whether part of speech tagging feature is allowed or not
     * @param queryTopics {Boolean} Indicates whether query defined topics are allowed or not
     * @param sentimentPhrases {Boolean} Indicates whether sentiment-bearing phrases output is allowed or not
     * @param summary {Boolean} Indicates whether summarization feature is allowed or not
     * @param themes {Boolean} Indicates whether document themes feature is allowed or not
     * @param userEntities {Boolean} Indicates whether user entities feature is allowed or not
     * @param userRelations {Boolean} Indicates whether relations for user entities are allowed or not
     */
    constructor(autoCategories, conceptTopics, entityThemes, intentions, languageDetection, mentions, modelSentiment, namedEntities, namedRelations, opinions, phrasesDetection, posTagging, queryTopics, sentimentPhrases, summary, themes, userEntities, userRelations) { 
        
        SubscriptionFeatureSectionDocument.initialize(this, autoCategories, conceptTopics, entityThemes, intentions, languageDetection, mentions, modelSentiment, namedEntities, namedRelations, opinions, phrasesDetection, posTagging, queryTopics, sentimentPhrases, summary, themes, userEntities, userRelations);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, autoCategories, conceptTopics, entityThemes, intentions, languageDetection, mentions, modelSentiment, namedEntities, namedRelations, opinions, phrasesDetection, posTagging, queryTopics, sentimentPhrases, summary, themes, userEntities, userRelations) { 
        obj['auto_categories'] = autoCategories;
        obj['concept_topics'] = conceptTopics;
        obj['entity_themes'] = entityThemes;
        obj['intentions'] = intentions;
        obj['language_detection'] = languageDetection;
        obj['mentions'] = mentions;
        obj['model_sentiment'] = modelSentiment;
        obj['named_entities'] = namedEntities;
        obj['named_relations'] = namedRelations;
        obj['opinions'] = opinions;
        obj['phrases_detection'] = phrasesDetection;
        obj['pos_tagging'] = posTagging;
        obj['query_topics'] = queryTopics;
        obj['sentiment_phrases'] = sentimentPhrases;
        obj['summary'] = summary;
        obj['themes'] = themes;
        obj['user_entities'] = userEntities;
        obj['user_relations'] = userRelations;
    }

    /**
     * Constructs a <code>SubscriptionFeatureSectionDocument</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/SubscriptionFeatureSectionDocument} obj Optional instance to populate.
     * @return {module:model/SubscriptionFeatureSectionDocument} The populated <code>SubscriptionFeatureSectionDocument</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new SubscriptionFeatureSectionDocument();

            if (data.hasOwnProperty('auto_categories')) {
                obj['auto_categories'] = ApiClient.convertToType(data['auto_categories'], 'Boolean');
            }
            if (data.hasOwnProperty('concept_topics')) {
                obj['concept_topics'] = ApiClient.convertToType(data['concept_topics'], 'Boolean');
            }
            if (data.hasOwnProperty('entity_themes')) {
                obj['entity_themes'] = ApiClient.convertToType(data['entity_themes'], 'Boolean');
            }
            if (data.hasOwnProperty('intentions')) {
                obj['intentions'] = ApiClient.convertToType(data['intentions'], 'Boolean');
            }
            if (data.hasOwnProperty('language_detection')) {
                obj['language_detection'] = ApiClient.convertToType(data['language_detection'], 'Boolean');
            }
            if (data.hasOwnProperty('mentions')) {
                obj['mentions'] = ApiClient.convertToType(data['mentions'], 'Boolean');
            }
            if (data.hasOwnProperty('model_sentiment')) {
                obj['model_sentiment'] = ApiClient.convertToType(data['model_sentiment'], 'Boolean');
            }
            if (data.hasOwnProperty('named_entities')) {
                obj['named_entities'] = ApiClient.convertToType(data['named_entities'], 'Boolean');
            }
            if (data.hasOwnProperty('named_relations')) {
                obj['named_relations'] = ApiClient.convertToType(data['named_relations'], 'Boolean');
            }
            if (data.hasOwnProperty('opinions')) {
                obj['opinions'] = ApiClient.convertToType(data['opinions'], 'Boolean');
            }
            if (data.hasOwnProperty('phrases_detection')) {
                obj['phrases_detection'] = ApiClient.convertToType(data['phrases_detection'], 'Boolean');
            }
            if (data.hasOwnProperty('pos_tagging')) {
                obj['pos_tagging'] = ApiClient.convertToType(data['pos_tagging'], 'Boolean');
            }
            if (data.hasOwnProperty('query_topics')) {
                obj['query_topics'] = ApiClient.convertToType(data['query_topics'], 'Boolean');
            }
            if (data.hasOwnProperty('sentiment_phrases')) {
                obj['sentiment_phrases'] = ApiClient.convertToType(data['sentiment_phrases'], 'Boolean');
            }
            if (data.hasOwnProperty('summary')) {
                obj['summary'] = ApiClient.convertToType(data['summary'], 'Boolean');
            }
            if (data.hasOwnProperty('themes')) {
                obj['themes'] = ApiClient.convertToType(data['themes'], 'Boolean');
            }
            if (data.hasOwnProperty('user_entities')) {
                obj['user_entities'] = ApiClient.convertToType(data['user_entities'], 'Boolean');
            }
            if (data.hasOwnProperty('user_relations')) {
                obj['user_relations'] = ApiClient.convertToType(data['user_relations'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>SubscriptionFeatureSectionDocument</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>SubscriptionFeatureSectionDocument</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of SubscriptionFeatureSectionDocument.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }

        return true;
    }


}

SubscriptionFeatureSectionDocument.RequiredProperties = ["auto_categories", "concept_topics", "entity_themes", "intentions", "language_detection", "mentions", "model_sentiment", "named_entities", "named_relations", "opinions", "phrases_detection", "pos_tagging", "query_topics", "sentiment_phrases", "summary", "themes", "user_entities", "user_relations"];

/**
 * Indicates whether auto categories feature is allowed or not
 * @member {Boolean} auto_categories
 */
SubscriptionFeatureSectionDocument.prototype['auto_categories'] = undefined;

/**
 * Indicates whether concept topics are allowed or not
 * @member {Boolean} concept_topics
 */
SubscriptionFeatureSectionDocument.prototype['concept_topics'] = undefined;

/**
 * Indicates whether entity themes feature is allowed or not
 * @member {Boolean} entity_themes
 */
SubscriptionFeatureSectionDocument.prototype['entity_themes'] = undefined;

/**
 * Indicates whether intentions feature is allowed or not.
 * @member {Boolean} intentions
 */
SubscriptionFeatureSectionDocument.prototype['intentions'] = undefined;

/**
 * Indicates whether language detection feature is allowed or not
 * @member {Boolean} language_detection
 */
SubscriptionFeatureSectionDocument.prototype['language_detection'] = undefined;

/**
 * Indicates whether mentions for entities and themes are allowed or not
 * @member {Boolean} mentions
 */
SubscriptionFeatureSectionDocument.prototype['mentions'] = undefined;

/**
 * Indicates whether model-based sentiment feature is allowed or not
 * @member {Boolean} model_sentiment
 */
SubscriptionFeatureSectionDocument.prototype['model_sentiment'] = undefined;

/**
 * Indicates whether named entities feature is allowed or not
 * @member {Boolean} named_entities
 */
SubscriptionFeatureSectionDocument.prototype['named_entities'] = undefined;

/**
 * Indicates whether relations for named entities are allowed or not
 * @member {Boolean} named_relations
 */
SubscriptionFeatureSectionDocument.prototype['named_relations'] = undefined;

/**
 * Indicates whether opinions feature is allowed or not
 * @member {Boolean} opinions
 */
SubscriptionFeatureSectionDocument.prototype['opinions'] = undefined;

/**
 * Indicates whether possible phrases detection feature is allowed or not
 * @member {Boolean} phrases_detection
 */
SubscriptionFeatureSectionDocument.prototype['phrases_detection'] = undefined;

/**
 * Indicates whether part of speech tagging feature is allowed or not
 * @member {Boolean} pos_tagging
 */
SubscriptionFeatureSectionDocument.prototype['pos_tagging'] = undefined;

/**
 * Indicates whether query defined topics are allowed or not
 * @member {Boolean} query_topics
 */
SubscriptionFeatureSectionDocument.prototype['query_topics'] = undefined;

/**
 * Indicates whether sentiment-bearing phrases output is allowed or not
 * @member {Boolean} sentiment_phrases
 */
SubscriptionFeatureSectionDocument.prototype['sentiment_phrases'] = undefined;

/**
 * Indicates whether summarization feature is allowed or not
 * @member {Boolean} summary
 */
SubscriptionFeatureSectionDocument.prototype['summary'] = undefined;

/**
 * Indicates whether document themes feature is allowed or not
 * @member {Boolean} themes
 */
SubscriptionFeatureSectionDocument.prototype['themes'] = undefined;

/**
 * Indicates whether user entities feature is allowed or not
 * @member {Boolean} user_entities
 */
SubscriptionFeatureSectionDocument.prototype['user_entities'] = undefined;

/**
 * Indicates whether relations for user entities are allowed or not
 * @member {Boolean} user_relations
 */
SubscriptionFeatureSectionDocument.prototype['user_relations'] = undefined;






export default SubscriptionFeatureSectionDocument;

