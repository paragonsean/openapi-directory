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
 * The SubscriptionFeatureSectionCollection model module.
 * @module model/SubscriptionFeatureSectionCollection
 * @version 4.0
 */
class SubscriptionFeatureSectionCollection {
    /**
     * Constructs a new <code>SubscriptionFeatureSectionCollection</code>.
     * @alias module:model/SubscriptionFeatureSectionCollection
     * @param conceptTopics {Boolean} Indicates whether concept topics are allowed or not
     * @param facets {Boolean} Indicates whether facets extraction feature is allowed or not
     * @param mentions {Boolean} Indicates whether mentions are allowed for facets and attributes or not
     * @param namedEntities {Boolean} Indicates whether named entities feature is allowed or not
     * @param queryTopics {Boolean} Indicates whether query defined topics are allowed or not
     * @param themes {Boolean} Indicates whether themes extraction feature is allowed or not
     * @param userEntities {Boolean} Indicates whether user entities feature is allowed or not
     */
    constructor(conceptTopics, facets, mentions, namedEntities, queryTopics, themes, userEntities) { 
        
        SubscriptionFeatureSectionCollection.initialize(this, conceptTopics, facets, mentions, namedEntities, queryTopics, themes, userEntities);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, conceptTopics, facets, mentions, namedEntities, queryTopics, themes, userEntities) { 
        obj['concept_topics'] = conceptTopics;
        obj['facets'] = facets;
        obj['mentions'] = mentions;
        obj['named_entities'] = namedEntities;
        obj['query_topics'] = queryTopics;
        obj['themes'] = themes;
        obj['user_entities'] = userEntities;
    }

    /**
     * Constructs a <code>SubscriptionFeatureSectionCollection</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/SubscriptionFeatureSectionCollection} obj Optional instance to populate.
     * @return {module:model/SubscriptionFeatureSectionCollection} The populated <code>SubscriptionFeatureSectionCollection</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new SubscriptionFeatureSectionCollection();

            if (data.hasOwnProperty('concept_topics')) {
                obj['concept_topics'] = ApiClient.convertToType(data['concept_topics'], 'Boolean');
            }
            if (data.hasOwnProperty('facets')) {
                obj['facets'] = ApiClient.convertToType(data['facets'], 'Boolean');
            }
            if (data.hasOwnProperty('mentions')) {
                obj['mentions'] = ApiClient.convertToType(data['mentions'], 'Boolean');
            }
            if (data.hasOwnProperty('named_entities')) {
                obj['named_entities'] = ApiClient.convertToType(data['named_entities'], 'Boolean');
            }
            if (data.hasOwnProperty('query_topics')) {
                obj['query_topics'] = ApiClient.convertToType(data['query_topics'], 'Boolean');
            }
            if (data.hasOwnProperty('themes')) {
                obj['themes'] = ApiClient.convertToType(data['themes'], 'Boolean');
            }
            if (data.hasOwnProperty('user_entities')) {
                obj['user_entities'] = ApiClient.convertToType(data['user_entities'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>SubscriptionFeatureSectionCollection</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>SubscriptionFeatureSectionCollection</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of SubscriptionFeatureSectionCollection.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }

        return true;
    }


}

SubscriptionFeatureSectionCollection.RequiredProperties = ["concept_topics", "facets", "mentions", "named_entities", "query_topics", "themes", "user_entities"];

/**
 * Indicates whether concept topics are allowed or not
 * @member {Boolean} concept_topics
 */
SubscriptionFeatureSectionCollection.prototype['concept_topics'] = undefined;

/**
 * Indicates whether facets extraction feature is allowed or not
 * @member {Boolean} facets
 */
SubscriptionFeatureSectionCollection.prototype['facets'] = undefined;

/**
 * Indicates whether mentions are allowed for facets and attributes or not
 * @member {Boolean} mentions
 */
SubscriptionFeatureSectionCollection.prototype['mentions'] = undefined;

/**
 * Indicates whether named entities feature is allowed or not
 * @member {Boolean} named_entities
 */
SubscriptionFeatureSectionCollection.prototype['named_entities'] = undefined;

/**
 * Indicates whether query defined topics are allowed or not
 * @member {Boolean} query_topics
 */
SubscriptionFeatureSectionCollection.prototype['query_topics'] = undefined;

/**
 * Indicates whether themes extraction feature is allowed or not
 * @member {Boolean} themes
 */
SubscriptionFeatureSectionCollection.prototype['themes'] = undefined;

/**
 * Indicates whether user entities feature is allowed or not
 * @member {Boolean} user_entities
 */
SubscriptionFeatureSectionCollection.prototype['user_entities'] = undefined;






export default SubscriptionFeatureSectionCollection;

