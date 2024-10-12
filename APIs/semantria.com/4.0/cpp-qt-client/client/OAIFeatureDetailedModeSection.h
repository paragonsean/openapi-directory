/**
 * Semantria
 * Semantria applies Text and Sentiment Analysis to tweets, facebook posts, surveys, reviews or enterprise content.
 *
 * The version of the OpenAPI document: 4.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIFeatureDetailedModeSection.h
 *
 * 
 */

#ifndef OAIFeatureDetailedModeSection_H
#define OAIFeatureDetailedModeSection_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIFeatureDetailedModeSection : public OAIObject {
public:
    OAIFeatureDetailedModeSection();
    OAIFeatureDetailedModeSection(QString json);
    ~OAIFeatureDetailedModeSection() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isAutoCategories() const;
    void setAutoCategories(const bool &auto_categories);
    bool is_auto_categories_Set() const;
    bool is_auto_categories_Valid() const;

    bool isEntityMentions() const;
    void setEntityMentions(const bool &entity_mentions);
    bool is_entity_mentions_Set() const;
    bool is_entity_mentions_Valid() const;

    bool isEntityOpinions() const;
    void setEntityOpinions(const bool &entity_opinions);
    bool is_entity_opinions_Set() const;
    bool is_entity_opinions_Valid() const;

    bool isEntityRelations() const;
    void setEntityRelations(const bool &entity_relations);
    bool is_entity_relations_Set() const;
    bool is_entity_relations_Valid() const;

    bool isEntityThemes() const;
    void setEntityThemes(const bool &entity_themes);
    bool is_entity_themes_Set() const;
    bool is_entity_themes_Valid() const;

    bool isIntentions() const;
    void setIntentions(const bool &intentions);
    bool is_intentions_Set() const;
    bool is_intentions_Valid() const;

    bool isLanguageDetection() const;
    void setLanguageDetection(const bool &language_detection);
    bool is_language_detection_Set() const;
    bool is_language_detection_Valid() const;

    bool isModelSentiment() const;
    void setModelSentiment(const bool &model_sentiment);
    bool is_model_sentiment_Set() const;
    bool is_model_sentiment_Valid() const;

    bool isNamedEntities() const;
    void setNamedEntities(const bool &named_entities);
    bool is_named_entities_Set() const;
    bool is_named_entities_Valid() const;

    bool isPosTagging() const;
    void setPosTagging(const bool &pos_tagging);
    bool is_pos_tagging_Set() const;
    bool is_pos_tagging_Valid() const;

    bool isQueries() const;
    void setQueries(const bool &queries);
    bool is_queries_Set() const;
    bool is_queries_Valid() const;

    bool isSentiment() const;
    void setSentiment(const bool &sentiment);
    bool is_sentiment_Set() const;
    bool is_sentiment_Valid() const;

    bool isSentimentPhrases() const;
    void setSentimentPhrases(const bool &sentiment_phrases);
    bool is_sentiment_phrases_Set() const;
    bool is_sentiment_phrases_Valid() const;

    bool isSummarization() const;
    void setSummarization(const bool &summarization);
    bool is_summarization_Set() const;
    bool is_summarization_Valid() const;

    bool isTaxonomy() const;
    void setTaxonomy(const bool &taxonomy);
    bool is_taxonomy_Set() const;
    bool is_taxonomy_Valid() const;

    bool isThemeMentions() const;
    void setThemeMentions(const bool &theme_mentions);
    bool is_theme_mentions_Set() const;
    bool is_theme_mentions_Valid() const;

    bool isThemes() const;
    void setThemes(const bool &themes);
    bool is_themes_Set() const;
    bool is_themes_Valid() const;

    bool isUserCategories() const;
    void setUserCategories(const bool &user_categories);
    bool is_user_categories_Set() const;
    bool is_user_categories_Valid() const;

    bool isUserEntities() const;
    void setUserEntities(const bool &user_entities);
    bool is_user_entities_Set() const;
    bool is_user_entities_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_auto_categories;
    bool m_auto_categories_isSet;
    bool m_auto_categories_isValid;

    bool m_entity_mentions;
    bool m_entity_mentions_isSet;
    bool m_entity_mentions_isValid;

    bool m_entity_opinions;
    bool m_entity_opinions_isSet;
    bool m_entity_opinions_isValid;

    bool m_entity_relations;
    bool m_entity_relations_isSet;
    bool m_entity_relations_isValid;

    bool m_entity_themes;
    bool m_entity_themes_isSet;
    bool m_entity_themes_isValid;

    bool m_intentions;
    bool m_intentions_isSet;
    bool m_intentions_isValid;

    bool m_language_detection;
    bool m_language_detection_isSet;
    bool m_language_detection_isValid;

    bool m_model_sentiment;
    bool m_model_sentiment_isSet;
    bool m_model_sentiment_isValid;

    bool m_named_entities;
    bool m_named_entities_isSet;
    bool m_named_entities_isValid;

    bool m_pos_tagging;
    bool m_pos_tagging_isSet;
    bool m_pos_tagging_isValid;

    bool m_queries;
    bool m_queries_isSet;
    bool m_queries_isValid;

    bool m_sentiment;
    bool m_sentiment_isSet;
    bool m_sentiment_isValid;

    bool m_sentiment_phrases;
    bool m_sentiment_phrases_isSet;
    bool m_sentiment_phrases_isValid;

    bool m_summarization;
    bool m_summarization_isSet;
    bool m_summarization_isValid;

    bool m_taxonomy;
    bool m_taxonomy_isSet;
    bool m_taxonomy_isValid;

    bool m_theme_mentions;
    bool m_theme_mentions_isSet;
    bool m_theme_mentions_isValid;

    bool m_themes;
    bool m_themes_isSet;
    bool m_themes_isValid;

    bool m_user_categories;
    bool m_user_categories_isSet;
    bool m_user_categories_isValid;

    bool m_user_entities;
    bool m_user_entities_isSet;
    bool m_user_entities_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIFeatureDetailedModeSection)

#endif // OAIFeatureDetailedModeSection_H
