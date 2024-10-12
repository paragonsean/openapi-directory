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

#include "OAIDocumentAnalyticData.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIDocumentAnalyticData::OAIDocumentAnalyticData(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIDocumentAnalyticData::OAIDocumentAnalyticData() {
    this->initializeModel();
}

OAIDocumentAnalyticData::~OAIDocumentAnalyticData() {}

void OAIDocumentAnalyticData::initializeModel() {

    m_auto_categories_isSet = false;
    m_auto_categories_isValid = false;

    m_config_id_isSet = false;
    m_config_id_isValid = false;

    m_details_isSet = false;
    m_details_isValid = false;

    m_entities_isSet = false;
    m_entities_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_intentions_isSet = false;
    m_intentions_isValid = false;

    m_job_id_isSet = false;
    m_job_id_isValid = false;

    m_language_isSet = false;
    m_language_isValid = false;

    m_language_score_isSet = false;
    m_language_score_isValid = false;

    m_model_sentiment_isSet = false;
    m_model_sentiment_isValid = false;

    m_opinions_isSet = false;
    m_opinions_isValid = false;

    m_phrases_isSet = false;
    m_phrases_isValid = false;

    m_relations_isSet = false;
    m_relations_isValid = false;

    m_sentiment_polarity_isSet = false;
    m_sentiment_polarity_isValid = false;

    m_sentiment_score_isSet = false;
    m_sentiment_score_isValid = false;

    m_source_text_isSet = false;
    m_source_text_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_summary_isSet = false;
    m_summary_isValid = false;

    m_taxonomy_isSet = false;
    m_taxonomy_isValid = false;

    m_themes_isSet = false;
    m_themes_isValid = false;

    m_topics_isSet = false;
    m_topics_isValid = false;
}

void OAIDocumentAnalyticData::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIDocumentAnalyticData::fromJsonObject(QJsonObject json) {

    m_auto_categories_isValid = ::OpenAPI::fromJsonValue(m_auto_categories, json[QString("auto_categories")]);
    m_auto_categories_isSet = !json[QString("auto_categories")].isNull() && m_auto_categories_isValid;

    m_config_id_isValid = ::OpenAPI::fromJsonValue(m_config_id, json[QString("config_id")]);
    m_config_id_isSet = !json[QString("config_id")].isNull() && m_config_id_isValid;

    m_details_isValid = ::OpenAPI::fromJsonValue(m_details, json[QString("details")]);
    m_details_isSet = !json[QString("details")].isNull() && m_details_isValid;

    m_entities_isValid = ::OpenAPI::fromJsonValue(m_entities, json[QString("entities")]);
    m_entities_isSet = !json[QString("entities")].isNull() && m_entities_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_intentions_isValid = ::OpenAPI::fromJsonValue(m_intentions, json[QString("intentions")]);
    m_intentions_isSet = !json[QString("intentions")].isNull() && m_intentions_isValid;

    m_job_id_isValid = ::OpenAPI::fromJsonValue(m_job_id, json[QString("job_id")]);
    m_job_id_isSet = !json[QString("job_id")].isNull() && m_job_id_isValid;

    m_language_isValid = ::OpenAPI::fromJsonValue(m_language, json[QString("language")]);
    m_language_isSet = !json[QString("language")].isNull() && m_language_isValid;

    m_language_score_isValid = ::OpenAPI::fromJsonValue(m_language_score, json[QString("language_score")]);
    m_language_score_isSet = !json[QString("language_score")].isNull() && m_language_score_isValid;

    m_model_sentiment_isValid = ::OpenAPI::fromJsonValue(m_model_sentiment, json[QString("model_sentiment")]);
    m_model_sentiment_isSet = !json[QString("model_sentiment")].isNull() && m_model_sentiment_isValid;

    m_opinions_isValid = ::OpenAPI::fromJsonValue(m_opinions, json[QString("opinions")]);
    m_opinions_isSet = !json[QString("opinions")].isNull() && m_opinions_isValid;

    m_phrases_isValid = ::OpenAPI::fromJsonValue(m_phrases, json[QString("phrases")]);
    m_phrases_isSet = !json[QString("phrases")].isNull() && m_phrases_isValid;

    m_relations_isValid = ::OpenAPI::fromJsonValue(m_relations, json[QString("relations")]);
    m_relations_isSet = !json[QString("relations")].isNull() && m_relations_isValid;

    m_sentiment_polarity_isValid = ::OpenAPI::fromJsonValue(m_sentiment_polarity, json[QString("sentiment_polarity")]);
    m_sentiment_polarity_isSet = !json[QString("sentiment_polarity")].isNull() && m_sentiment_polarity_isValid;

    m_sentiment_score_isValid = ::OpenAPI::fromJsonValue(m_sentiment_score, json[QString("sentiment_score")]);
    m_sentiment_score_isSet = !json[QString("sentiment_score")].isNull() && m_sentiment_score_isValid;

    m_source_text_isValid = ::OpenAPI::fromJsonValue(m_source_text, json[QString("source_text")]);
    m_source_text_isSet = !json[QString("source_text")].isNull() && m_source_text_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_summary_isValid = ::OpenAPI::fromJsonValue(m_summary, json[QString("summary")]);
    m_summary_isSet = !json[QString("summary")].isNull() && m_summary_isValid;

    m_taxonomy_isValid = ::OpenAPI::fromJsonValue(m_taxonomy, json[QString("taxonomy")]);
    m_taxonomy_isSet = !json[QString("taxonomy")].isNull() && m_taxonomy_isValid;

    m_themes_isValid = ::OpenAPI::fromJsonValue(m_themes, json[QString("themes")]);
    m_themes_isSet = !json[QString("themes")].isNull() && m_themes_isValid;

    m_topics_isValid = ::OpenAPI::fromJsonValue(m_topics, json[QString("topics")]);
    m_topics_isSet = !json[QString("topics")].isNull() && m_topics_isValid;
}

QString OAIDocumentAnalyticData::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIDocumentAnalyticData::asJsonObject() const {
    QJsonObject obj;
    if (m_auto_categories.size() > 0) {
        obj.insert(QString("auto_categories"), ::OpenAPI::toJsonValue(m_auto_categories));
    }
    if (m_config_id_isSet) {
        obj.insert(QString("config_id"), ::OpenAPI::toJsonValue(m_config_id));
    }
    if (m_details.size() > 0) {
        obj.insert(QString("details"), ::OpenAPI::toJsonValue(m_details));
    }
    if (m_entities.size() > 0) {
        obj.insert(QString("entities"), ::OpenAPI::toJsonValue(m_entities));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_intentions.size() > 0) {
        obj.insert(QString("intentions"), ::OpenAPI::toJsonValue(m_intentions));
    }
    if (m_job_id_isSet) {
        obj.insert(QString("job_id"), ::OpenAPI::toJsonValue(m_job_id));
    }
    if (m_language_isSet) {
        obj.insert(QString("language"), ::OpenAPI::toJsonValue(m_language));
    }
    if (m_language_score_isSet) {
        obj.insert(QString("language_score"), ::OpenAPI::toJsonValue(m_language_score));
    }
    if (m_model_sentiment.isSet()) {
        obj.insert(QString("model_sentiment"), ::OpenAPI::toJsonValue(m_model_sentiment));
    }
    if (m_opinions.size() > 0) {
        obj.insert(QString("opinions"), ::OpenAPI::toJsonValue(m_opinions));
    }
    if (m_phrases.size() > 0) {
        obj.insert(QString("phrases"), ::OpenAPI::toJsonValue(m_phrases));
    }
    if (m_relations.size() > 0) {
        obj.insert(QString("relations"), ::OpenAPI::toJsonValue(m_relations));
    }
    if (m_sentiment_polarity_isSet) {
        obj.insert(QString("sentiment_polarity"), ::OpenAPI::toJsonValue(m_sentiment_polarity));
    }
    if (m_sentiment_score_isSet) {
        obj.insert(QString("sentiment_score"), ::OpenAPI::toJsonValue(m_sentiment_score));
    }
    if (m_source_text_isSet) {
        obj.insert(QString("source_text"), ::OpenAPI::toJsonValue(m_source_text));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_summary_isSet) {
        obj.insert(QString("summary"), ::OpenAPI::toJsonValue(m_summary));
    }
    if (m_taxonomy.size() > 0) {
        obj.insert(QString("taxonomy"), ::OpenAPI::toJsonValue(m_taxonomy));
    }
    if (m_themes.size() > 0) {
        obj.insert(QString("themes"), ::OpenAPI::toJsonValue(m_themes));
    }
    if (m_topics.size() > 0) {
        obj.insert(QString("topics"), ::OpenAPI::toJsonValue(m_topics));
    }
    return obj;
}

QList<OAIAutoCategory> OAIDocumentAnalyticData::getAutoCategories() const {
    return m_auto_categories;
}
void OAIDocumentAnalyticData::setAutoCategories(const QList<OAIAutoCategory> &auto_categories) {
    m_auto_categories = auto_categories;
    m_auto_categories_isSet = true;
}

bool OAIDocumentAnalyticData::is_auto_categories_Set() const{
    return m_auto_categories_isSet;
}

bool OAIDocumentAnalyticData::is_auto_categories_Valid() const{
    return m_auto_categories_isValid;
}

QString OAIDocumentAnalyticData::getConfigId() const {
    return m_config_id;
}
void OAIDocumentAnalyticData::setConfigId(const QString &config_id) {
    m_config_id = config_id;
    m_config_id_isSet = true;
}

bool OAIDocumentAnalyticData::is_config_id_Set() const{
    return m_config_id_isSet;
}

bool OAIDocumentAnalyticData::is_config_id_Valid() const{
    return m_config_id_isValid;
}

QList<OAIDetails> OAIDocumentAnalyticData::getDetails() const {
    return m_details;
}
void OAIDocumentAnalyticData::setDetails(const QList<OAIDetails> &details) {
    m_details = details;
    m_details_isSet = true;
}

bool OAIDocumentAnalyticData::is_details_Set() const{
    return m_details_isSet;
}

bool OAIDocumentAnalyticData::is_details_Valid() const{
    return m_details_isValid;
}

QList<OAIEntity> OAIDocumentAnalyticData::getEntities() const {
    return m_entities;
}
void OAIDocumentAnalyticData::setEntities(const QList<OAIEntity> &entities) {
    m_entities = entities;
    m_entities_isSet = true;
}

bool OAIDocumentAnalyticData::is_entities_Set() const{
    return m_entities_isSet;
}

bool OAIDocumentAnalyticData::is_entities_Valid() const{
    return m_entities_isValid;
}

QString OAIDocumentAnalyticData::getId() const {
    return m_id;
}
void OAIDocumentAnalyticData::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIDocumentAnalyticData::is_id_Set() const{
    return m_id_isSet;
}

bool OAIDocumentAnalyticData::is_id_Valid() const{
    return m_id_isValid;
}

QList<OAIIntention> OAIDocumentAnalyticData::getIntentions() const {
    return m_intentions;
}
void OAIDocumentAnalyticData::setIntentions(const QList<OAIIntention> &intentions) {
    m_intentions = intentions;
    m_intentions_isSet = true;
}

bool OAIDocumentAnalyticData::is_intentions_Set() const{
    return m_intentions_isSet;
}

bool OAIDocumentAnalyticData::is_intentions_Valid() const{
    return m_intentions_isValid;
}

QString OAIDocumentAnalyticData::getJobId() const {
    return m_job_id;
}
void OAIDocumentAnalyticData::setJobId(const QString &job_id) {
    m_job_id = job_id;
    m_job_id_isSet = true;
}

bool OAIDocumentAnalyticData::is_job_id_Set() const{
    return m_job_id_isSet;
}

bool OAIDocumentAnalyticData::is_job_id_Valid() const{
    return m_job_id_isValid;
}

QString OAIDocumentAnalyticData::getLanguage() const {
    return m_language;
}
void OAIDocumentAnalyticData::setLanguage(const QString &language) {
    m_language = language;
    m_language_isSet = true;
}

bool OAIDocumentAnalyticData::is_language_Set() const{
    return m_language_isSet;
}

bool OAIDocumentAnalyticData::is_language_Valid() const{
    return m_language_isValid;
}

double OAIDocumentAnalyticData::getLanguageScore() const {
    return m_language_score;
}
void OAIDocumentAnalyticData::setLanguageScore(const double &language_score) {
    m_language_score = language_score;
    m_language_score_isSet = true;
}

bool OAIDocumentAnalyticData::is_language_score_Set() const{
    return m_language_score_isSet;
}

bool OAIDocumentAnalyticData::is_language_score_Valid() const{
    return m_language_score_isValid;
}

OAIModelSentiment OAIDocumentAnalyticData::getModelSentiment() const {
    return m_model_sentiment;
}
void OAIDocumentAnalyticData::setModelSentiment(const OAIModelSentiment &model_sentiment) {
    m_model_sentiment = model_sentiment;
    m_model_sentiment_isSet = true;
}

bool OAIDocumentAnalyticData::is_model_sentiment_Set() const{
    return m_model_sentiment_isSet;
}

bool OAIDocumentAnalyticData::is_model_sentiment_Valid() const{
    return m_model_sentiment_isValid;
}

QList<OAIOpinion> OAIDocumentAnalyticData::getOpinions() const {
    return m_opinions;
}
void OAIDocumentAnalyticData::setOpinions(const QList<OAIOpinion> &opinions) {
    m_opinions = opinions;
    m_opinions_isSet = true;
}

bool OAIDocumentAnalyticData::is_opinions_Set() const{
    return m_opinions_isSet;
}

bool OAIDocumentAnalyticData::is_opinions_Valid() const{
    return m_opinions_isValid;
}

QList<OAIPhrase> OAIDocumentAnalyticData::getPhrases() const {
    return m_phrases;
}
void OAIDocumentAnalyticData::setPhrases(const QList<OAIPhrase> &phrases) {
    m_phrases = phrases;
    m_phrases_isSet = true;
}

bool OAIDocumentAnalyticData::is_phrases_Set() const{
    return m_phrases_isSet;
}

bool OAIDocumentAnalyticData::is_phrases_Valid() const{
    return m_phrases_isValid;
}

QList<OAIRelation> OAIDocumentAnalyticData::getRelations() const {
    return m_relations;
}
void OAIDocumentAnalyticData::setRelations(const QList<OAIRelation> &relations) {
    m_relations = relations;
    m_relations_isSet = true;
}

bool OAIDocumentAnalyticData::is_relations_Set() const{
    return m_relations_isSet;
}

bool OAIDocumentAnalyticData::is_relations_Valid() const{
    return m_relations_isValid;
}

QString OAIDocumentAnalyticData::getSentimentPolarity() const {
    return m_sentiment_polarity;
}
void OAIDocumentAnalyticData::setSentimentPolarity(const QString &sentiment_polarity) {
    m_sentiment_polarity = sentiment_polarity;
    m_sentiment_polarity_isSet = true;
}

bool OAIDocumentAnalyticData::is_sentiment_polarity_Set() const{
    return m_sentiment_polarity_isSet;
}

bool OAIDocumentAnalyticData::is_sentiment_polarity_Valid() const{
    return m_sentiment_polarity_isValid;
}

double OAIDocumentAnalyticData::getSentimentScore() const {
    return m_sentiment_score;
}
void OAIDocumentAnalyticData::setSentimentScore(const double &sentiment_score) {
    m_sentiment_score = sentiment_score;
    m_sentiment_score_isSet = true;
}

bool OAIDocumentAnalyticData::is_sentiment_score_Set() const{
    return m_sentiment_score_isSet;
}

bool OAIDocumentAnalyticData::is_sentiment_score_Valid() const{
    return m_sentiment_score_isValid;
}

QString OAIDocumentAnalyticData::getSourceText() const {
    return m_source_text;
}
void OAIDocumentAnalyticData::setSourceText(const QString &source_text) {
    m_source_text = source_text;
    m_source_text_isSet = true;
}

bool OAIDocumentAnalyticData::is_source_text_Set() const{
    return m_source_text_isSet;
}

bool OAIDocumentAnalyticData::is_source_text_Valid() const{
    return m_source_text_isValid;
}

QString OAIDocumentAnalyticData::getStatus() const {
    return m_status;
}
void OAIDocumentAnalyticData::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIDocumentAnalyticData::is_status_Set() const{
    return m_status_isSet;
}

bool OAIDocumentAnalyticData::is_status_Valid() const{
    return m_status_isValid;
}

QString OAIDocumentAnalyticData::getSummary() const {
    return m_summary;
}
void OAIDocumentAnalyticData::setSummary(const QString &summary) {
    m_summary = summary;
    m_summary_isSet = true;
}

bool OAIDocumentAnalyticData::is_summary_Set() const{
    return m_summary_isSet;
}

bool OAIDocumentAnalyticData::is_summary_Valid() const{
    return m_summary_isValid;
}

QList<OAITopic> OAIDocumentAnalyticData::getTaxonomy() const {
    return m_taxonomy;
}
void OAIDocumentAnalyticData::setTaxonomy(const QList<OAITopic> &taxonomy) {
    m_taxonomy = taxonomy;
    m_taxonomy_isSet = true;
}

bool OAIDocumentAnalyticData::is_taxonomy_Set() const{
    return m_taxonomy_isSet;
}

bool OAIDocumentAnalyticData::is_taxonomy_Valid() const{
    return m_taxonomy_isValid;
}

QList<OAITheme> OAIDocumentAnalyticData::getThemes() const {
    return m_themes;
}
void OAIDocumentAnalyticData::setThemes(const QList<OAITheme> &themes) {
    m_themes = themes;
    m_themes_isSet = true;
}

bool OAIDocumentAnalyticData::is_themes_Set() const{
    return m_themes_isSet;
}

bool OAIDocumentAnalyticData::is_themes_Valid() const{
    return m_themes_isValid;
}

QList<OAITopic> OAIDocumentAnalyticData::getTopics() const {
    return m_topics;
}
void OAIDocumentAnalyticData::setTopics(const QList<OAITopic> &topics) {
    m_topics = topics;
    m_topics_isSet = true;
}

bool OAIDocumentAnalyticData::is_topics_Set() const{
    return m_topics_isSet;
}

bool OAIDocumentAnalyticData::is_topics_Valid() const{
    return m_topics_isValid;
}

bool OAIDocumentAnalyticData::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_auto_categories.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_config_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_details.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_entities.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_intentions.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_job_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_language_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_language_score_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_model_sentiment.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_opinions.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_phrases.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_relations.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_sentiment_polarity_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sentiment_score_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_source_text_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_summary_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_taxonomy.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_themes.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_topics.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIDocumentAnalyticData::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_auto_categories_isValid && m_config_id_isValid && m_details_isValid && m_entities_isValid && m_id_isValid && m_intentions_isValid && m_job_id_isValid && m_language_isValid && m_language_score_isValid && m_model_sentiment_isValid && m_opinions_isValid && m_phrases_isValid && m_relations_isValid && m_sentiment_polarity_isValid && m_sentiment_score_isValid && m_source_text_isValid && m_status_isValid && m_summary_isValid && m_taxonomy_isValid && m_themes_isValid && m_topics_isValid && true;
}

} // namespace OpenAPI
