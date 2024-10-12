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

#include "OAISubscriptionFeatureSectionDocument.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISubscriptionFeatureSectionDocument::OAISubscriptionFeatureSectionDocument(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISubscriptionFeatureSectionDocument::OAISubscriptionFeatureSectionDocument() {
    this->initializeModel();
}

OAISubscriptionFeatureSectionDocument::~OAISubscriptionFeatureSectionDocument() {}

void OAISubscriptionFeatureSectionDocument::initializeModel() {

    m_auto_categories_isSet = false;
    m_auto_categories_isValid = false;

    m_concept_topics_isSet = false;
    m_concept_topics_isValid = false;

    m_entity_themes_isSet = false;
    m_entity_themes_isValid = false;

    m_intentions_isSet = false;
    m_intentions_isValid = false;

    m_language_detection_isSet = false;
    m_language_detection_isValid = false;

    m_mentions_isSet = false;
    m_mentions_isValid = false;

    m_model_sentiment_isSet = false;
    m_model_sentiment_isValid = false;

    m_named_entities_isSet = false;
    m_named_entities_isValid = false;

    m_named_relations_isSet = false;
    m_named_relations_isValid = false;

    m_opinions_isSet = false;
    m_opinions_isValid = false;

    m_phrases_detection_isSet = false;
    m_phrases_detection_isValid = false;

    m_pos_tagging_isSet = false;
    m_pos_tagging_isValid = false;

    m_query_topics_isSet = false;
    m_query_topics_isValid = false;

    m_sentiment_phrases_isSet = false;
    m_sentiment_phrases_isValid = false;

    m_summary_isSet = false;
    m_summary_isValid = false;

    m_themes_isSet = false;
    m_themes_isValid = false;

    m_user_entities_isSet = false;
    m_user_entities_isValid = false;

    m_user_relations_isSet = false;
    m_user_relations_isValid = false;
}

void OAISubscriptionFeatureSectionDocument::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISubscriptionFeatureSectionDocument::fromJsonObject(QJsonObject json) {

    m_auto_categories_isValid = ::OpenAPI::fromJsonValue(m_auto_categories, json[QString("auto_categories")]);
    m_auto_categories_isSet = !json[QString("auto_categories")].isNull() && m_auto_categories_isValid;

    m_concept_topics_isValid = ::OpenAPI::fromJsonValue(m_concept_topics, json[QString("concept_topics")]);
    m_concept_topics_isSet = !json[QString("concept_topics")].isNull() && m_concept_topics_isValid;

    m_entity_themes_isValid = ::OpenAPI::fromJsonValue(m_entity_themes, json[QString("entity_themes")]);
    m_entity_themes_isSet = !json[QString("entity_themes")].isNull() && m_entity_themes_isValid;

    m_intentions_isValid = ::OpenAPI::fromJsonValue(m_intentions, json[QString("intentions")]);
    m_intentions_isSet = !json[QString("intentions")].isNull() && m_intentions_isValid;

    m_language_detection_isValid = ::OpenAPI::fromJsonValue(m_language_detection, json[QString("language_detection")]);
    m_language_detection_isSet = !json[QString("language_detection")].isNull() && m_language_detection_isValid;

    m_mentions_isValid = ::OpenAPI::fromJsonValue(m_mentions, json[QString("mentions")]);
    m_mentions_isSet = !json[QString("mentions")].isNull() && m_mentions_isValid;

    m_model_sentiment_isValid = ::OpenAPI::fromJsonValue(m_model_sentiment, json[QString("model_sentiment")]);
    m_model_sentiment_isSet = !json[QString("model_sentiment")].isNull() && m_model_sentiment_isValid;

    m_named_entities_isValid = ::OpenAPI::fromJsonValue(m_named_entities, json[QString("named_entities")]);
    m_named_entities_isSet = !json[QString("named_entities")].isNull() && m_named_entities_isValid;

    m_named_relations_isValid = ::OpenAPI::fromJsonValue(m_named_relations, json[QString("named_relations")]);
    m_named_relations_isSet = !json[QString("named_relations")].isNull() && m_named_relations_isValid;

    m_opinions_isValid = ::OpenAPI::fromJsonValue(m_opinions, json[QString("opinions")]);
    m_opinions_isSet = !json[QString("opinions")].isNull() && m_opinions_isValid;

    m_phrases_detection_isValid = ::OpenAPI::fromJsonValue(m_phrases_detection, json[QString("phrases_detection")]);
    m_phrases_detection_isSet = !json[QString("phrases_detection")].isNull() && m_phrases_detection_isValid;

    m_pos_tagging_isValid = ::OpenAPI::fromJsonValue(m_pos_tagging, json[QString("pos_tagging")]);
    m_pos_tagging_isSet = !json[QString("pos_tagging")].isNull() && m_pos_tagging_isValid;

    m_query_topics_isValid = ::OpenAPI::fromJsonValue(m_query_topics, json[QString("query_topics")]);
    m_query_topics_isSet = !json[QString("query_topics")].isNull() && m_query_topics_isValid;

    m_sentiment_phrases_isValid = ::OpenAPI::fromJsonValue(m_sentiment_phrases, json[QString("sentiment_phrases")]);
    m_sentiment_phrases_isSet = !json[QString("sentiment_phrases")].isNull() && m_sentiment_phrases_isValid;

    m_summary_isValid = ::OpenAPI::fromJsonValue(m_summary, json[QString("summary")]);
    m_summary_isSet = !json[QString("summary")].isNull() && m_summary_isValid;

    m_themes_isValid = ::OpenAPI::fromJsonValue(m_themes, json[QString("themes")]);
    m_themes_isSet = !json[QString("themes")].isNull() && m_themes_isValid;

    m_user_entities_isValid = ::OpenAPI::fromJsonValue(m_user_entities, json[QString("user_entities")]);
    m_user_entities_isSet = !json[QString("user_entities")].isNull() && m_user_entities_isValid;

    m_user_relations_isValid = ::OpenAPI::fromJsonValue(m_user_relations, json[QString("user_relations")]);
    m_user_relations_isSet = !json[QString("user_relations")].isNull() && m_user_relations_isValid;
}

QString OAISubscriptionFeatureSectionDocument::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISubscriptionFeatureSectionDocument::asJsonObject() const {
    QJsonObject obj;
    if (m_auto_categories_isSet) {
        obj.insert(QString("auto_categories"), ::OpenAPI::toJsonValue(m_auto_categories));
    }
    if (m_concept_topics_isSet) {
        obj.insert(QString("concept_topics"), ::OpenAPI::toJsonValue(m_concept_topics));
    }
    if (m_entity_themes_isSet) {
        obj.insert(QString("entity_themes"), ::OpenAPI::toJsonValue(m_entity_themes));
    }
    if (m_intentions_isSet) {
        obj.insert(QString("intentions"), ::OpenAPI::toJsonValue(m_intentions));
    }
    if (m_language_detection_isSet) {
        obj.insert(QString("language_detection"), ::OpenAPI::toJsonValue(m_language_detection));
    }
    if (m_mentions_isSet) {
        obj.insert(QString("mentions"), ::OpenAPI::toJsonValue(m_mentions));
    }
    if (m_model_sentiment_isSet) {
        obj.insert(QString("model_sentiment"), ::OpenAPI::toJsonValue(m_model_sentiment));
    }
    if (m_named_entities_isSet) {
        obj.insert(QString("named_entities"), ::OpenAPI::toJsonValue(m_named_entities));
    }
    if (m_named_relations_isSet) {
        obj.insert(QString("named_relations"), ::OpenAPI::toJsonValue(m_named_relations));
    }
    if (m_opinions_isSet) {
        obj.insert(QString("opinions"), ::OpenAPI::toJsonValue(m_opinions));
    }
    if (m_phrases_detection_isSet) {
        obj.insert(QString("phrases_detection"), ::OpenAPI::toJsonValue(m_phrases_detection));
    }
    if (m_pos_tagging_isSet) {
        obj.insert(QString("pos_tagging"), ::OpenAPI::toJsonValue(m_pos_tagging));
    }
    if (m_query_topics_isSet) {
        obj.insert(QString("query_topics"), ::OpenAPI::toJsonValue(m_query_topics));
    }
    if (m_sentiment_phrases_isSet) {
        obj.insert(QString("sentiment_phrases"), ::OpenAPI::toJsonValue(m_sentiment_phrases));
    }
    if (m_summary_isSet) {
        obj.insert(QString("summary"), ::OpenAPI::toJsonValue(m_summary));
    }
    if (m_themes_isSet) {
        obj.insert(QString("themes"), ::OpenAPI::toJsonValue(m_themes));
    }
    if (m_user_entities_isSet) {
        obj.insert(QString("user_entities"), ::OpenAPI::toJsonValue(m_user_entities));
    }
    if (m_user_relations_isSet) {
        obj.insert(QString("user_relations"), ::OpenAPI::toJsonValue(m_user_relations));
    }
    return obj;
}

bool OAISubscriptionFeatureSectionDocument::isAutoCategories() const {
    return m_auto_categories;
}
void OAISubscriptionFeatureSectionDocument::setAutoCategories(const bool &auto_categories) {
    m_auto_categories = auto_categories;
    m_auto_categories_isSet = true;
}

bool OAISubscriptionFeatureSectionDocument::is_auto_categories_Set() const{
    return m_auto_categories_isSet;
}

bool OAISubscriptionFeatureSectionDocument::is_auto_categories_Valid() const{
    return m_auto_categories_isValid;
}

bool OAISubscriptionFeatureSectionDocument::isConceptTopics() const {
    return m_concept_topics;
}
void OAISubscriptionFeatureSectionDocument::setConceptTopics(const bool &concept_topics) {
    m_concept_topics = concept_topics;
    m_concept_topics_isSet = true;
}

bool OAISubscriptionFeatureSectionDocument::is_concept_topics_Set() const{
    return m_concept_topics_isSet;
}

bool OAISubscriptionFeatureSectionDocument::is_concept_topics_Valid() const{
    return m_concept_topics_isValid;
}

bool OAISubscriptionFeatureSectionDocument::isEntityThemes() const {
    return m_entity_themes;
}
void OAISubscriptionFeatureSectionDocument::setEntityThemes(const bool &entity_themes) {
    m_entity_themes = entity_themes;
    m_entity_themes_isSet = true;
}

bool OAISubscriptionFeatureSectionDocument::is_entity_themes_Set() const{
    return m_entity_themes_isSet;
}

bool OAISubscriptionFeatureSectionDocument::is_entity_themes_Valid() const{
    return m_entity_themes_isValid;
}

bool OAISubscriptionFeatureSectionDocument::isIntentions() const {
    return m_intentions;
}
void OAISubscriptionFeatureSectionDocument::setIntentions(const bool &intentions) {
    m_intentions = intentions;
    m_intentions_isSet = true;
}

bool OAISubscriptionFeatureSectionDocument::is_intentions_Set() const{
    return m_intentions_isSet;
}

bool OAISubscriptionFeatureSectionDocument::is_intentions_Valid() const{
    return m_intentions_isValid;
}

bool OAISubscriptionFeatureSectionDocument::isLanguageDetection() const {
    return m_language_detection;
}
void OAISubscriptionFeatureSectionDocument::setLanguageDetection(const bool &language_detection) {
    m_language_detection = language_detection;
    m_language_detection_isSet = true;
}

bool OAISubscriptionFeatureSectionDocument::is_language_detection_Set() const{
    return m_language_detection_isSet;
}

bool OAISubscriptionFeatureSectionDocument::is_language_detection_Valid() const{
    return m_language_detection_isValid;
}

bool OAISubscriptionFeatureSectionDocument::isMentions() const {
    return m_mentions;
}
void OAISubscriptionFeatureSectionDocument::setMentions(const bool &mentions) {
    m_mentions = mentions;
    m_mentions_isSet = true;
}

bool OAISubscriptionFeatureSectionDocument::is_mentions_Set() const{
    return m_mentions_isSet;
}

bool OAISubscriptionFeatureSectionDocument::is_mentions_Valid() const{
    return m_mentions_isValid;
}

bool OAISubscriptionFeatureSectionDocument::isModelSentiment() const {
    return m_model_sentiment;
}
void OAISubscriptionFeatureSectionDocument::setModelSentiment(const bool &model_sentiment) {
    m_model_sentiment = model_sentiment;
    m_model_sentiment_isSet = true;
}

bool OAISubscriptionFeatureSectionDocument::is_model_sentiment_Set() const{
    return m_model_sentiment_isSet;
}

bool OAISubscriptionFeatureSectionDocument::is_model_sentiment_Valid() const{
    return m_model_sentiment_isValid;
}

bool OAISubscriptionFeatureSectionDocument::isNamedEntities() const {
    return m_named_entities;
}
void OAISubscriptionFeatureSectionDocument::setNamedEntities(const bool &named_entities) {
    m_named_entities = named_entities;
    m_named_entities_isSet = true;
}

bool OAISubscriptionFeatureSectionDocument::is_named_entities_Set() const{
    return m_named_entities_isSet;
}

bool OAISubscriptionFeatureSectionDocument::is_named_entities_Valid() const{
    return m_named_entities_isValid;
}

bool OAISubscriptionFeatureSectionDocument::isNamedRelations() const {
    return m_named_relations;
}
void OAISubscriptionFeatureSectionDocument::setNamedRelations(const bool &named_relations) {
    m_named_relations = named_relations;
    m_named_relations_isSet = true;
}

bool OAISubscriptionFeatureSectionDocument::is_named_relations_Set() const{
    return m_named_relations_isSet;
}

bool OAISubscriptionFeatureSectionDocument::is_named_relations_Valid() const{
    return m_named_relations_isValid;
}

bool OAISubscriptionFeatureSectionDocument::isOpinions() const {
    return m_opinions;
}
void OAISubscriptionFeatureSectionDocument::setOpinions(const bool &opinions) {
    m_opinions = opinions;
    m_opinions_isSet = true;
}

bool OAISubscriptionFeatureSectionDocument::is_opinions_Set() const{
    return m_opinions_isSet;
}

bool OAISubscriptionFeatureSectionDocument::is_opinions_Valid() const{
    return m_opinions_isValid;
}

bool OAISubscriptionFeatureSectionDocument::isPhrasesDetection() const {
    return m_phrases_detection;
}
void OAISubscriptionFeatureSectionDocument::setPhrasesDetection(const bool &phrases_detection) {
    m_phrases_detection = phrases_detection;
    m_phrases_detection_isSet = true;
}

bool OAISubscriptionFeatureSectionDocument::is_phrases_detection_Set() const{
    return m_phrases_detection_isSet;
}

bool OAISubscriptionFeatureSectionDocument::is_phrases_detection_Valid() const{
    return m_phrases_detection_isValid;
}

bool OAISubscriptionFeatureSectionDocument::isPosTagging() const {
    return m_pos_tagging;
}
void OAISubscriptionFeatureSectionDocument::setPosTagging(const bool &pos_tagging) {
    m_pos_tagging = pos_tagging;
    m_pos_tagging_isSet = true;
}

bool OAISubscriptionFeatureSectionDocument::is_pos_tagging_Set() const{
    return m_pos_tagging_isSet;
}

bool OAISubscriptionFeatureSectionDocument::is_pos_tagging_Valid() const{
    return m_pos_tagging_isValid;
}

bool OAISubscriptionFeatureSectionDocument::isQueryTopics() const {
    return m_query_topics;
}
void OAISubscriptionFeatureSectionDocument::setQueryTopics(const bool &query_topics) {
    m_query_topics = query_topics;
    m_query_topics_isSet = true;
}

bool OAISubscriptionFeatureSectionDocument::is_query_topics_Set() const{
    return m_query_topics_isSet;
}

bool OAISubscriptionFeatureSectionDocument::is_query_topics_Valid() const{
    return m_query_topics_isValid;
}

bool OAISubscriptionFeatureSectionDocument::isSentimentPhrases() const {
    return m_sentiment_phrases;
}
void OAISubscriptionFeatureSectionDocument::setSentimentPhrases(const bool &sentiment_phrases) {
    m_sentiment_phrases = sentiment_phrases;
    m_sentiment_phrases_isSet = true;
}

bool OAISubscriptionFeatureSectionDocument::is_sentiment_phrases_Set() const{
    return m_sentiment_phrases_isSet;
}

bool OAISubscriptionFeatureSectionDocument::is_sentiment_phrases_Valid() const{
    return m_sentiment_phrases_isValid;
}

bool OAISubscriptionFeatureSectionDocument::isSummary() const {
    return m_summary;
}
void OAISubscriptionFeatureSectionDocument::setSummary(const bool &summary) {
    m_summary = summary;
    m_summary_isSet = true;
}

bool OAISubscriptionFeatureSectionDocument::is_summary_Set() const{
    return m_summary_isSet;
}

bool OAISubscriptionFeatureSectionDocument::is_summary_Valid() const{
    return m_summary_isValid;
}

bool OAISubscriptionFeatureSectionDocument::isThemes() const {
    return m_themes;
}
void OAISubscriptionFeatureSectionDocument::setThemes(const bool &themes) {
    m_themes = themes;
    m_themes_isSet = true;
}

bool OAISubscriptionFeatureSectionDocument::is_themes_Set() const{
    return m_themes_isSet;
}

bool OAISubscriptionFeatureSectionDocument::is_themes_Valid() const{
    return m_themes_isValid;
}

bool OAISubscriptionFeatureSectionDocument::isUserEntities() const {
    return m_user_entities;
}
void OAISubscriptionFeatureSectionDocument::setUserEntities(const bool &user_entities) {
    m_user_entities = user_entities;
    m_user_entities_isSet = true;
}

bool OAISubscriptionFeatureSectionDocument::is_user_entities_Set() const{
    return m_user_entities_isSet;
}

bool OAISubscriptionFeatureSectionDocument::is_user_entities_Valid() const{
    return m_user_entities_isValid;
}

bool OAISubscriptionFeatureSectionDocument::isUserRelations() const {
    return m_user_relations;
}
void OAISubscriptionFeatureSectionDocument::setUserRelations(const bool &user_relations) {
    m_user_relations = user_relations;
    m_user_relations_isSet = true;
}

bool OAISubscriptionFeatureSectionDocument::is_user_relations_Set() const{
    return m_user_relations_isSet;
}

bool OAISubscriptionFeatureSectionDocument::is_user_relations_Valid() const{
    return m_user_relations_isValid;
}

bool OAISubscriptionFeatureSectionDocument::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_auto_categories_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_concept_topics_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_entity_themes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_intentions_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_language_detection_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_mentions_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_model_sentiment_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_named_entities_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_named_relations_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_opinions_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_phrases_detection_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_pos_tagging_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_query_topics_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sentiment_phrases_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_summary_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_themes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_user_entities_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_user_relations_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISubscriptionFeatureSectionDocument::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_auto_categories_isValid && m_concept_topics_isValid && m_entity_themes_isValid && m_intentions_isValid && m_language_detection_isValid && m_mentions_isValid && m_model_sentiment_isValid && m_named_entities_isValid && m_named_relations_isValid && m_opinions_isValid && m_phrases_detection_isValid && m_pos_tagging_isValid && m_query_topics_isValid && m_sentiment_phrases_isValid && m_summary_isValid && m_themes_isValid && m_user_entities_isValid && m_user_relations_isValid && true;
}

} // namespace OpenAPI
