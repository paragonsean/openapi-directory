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

#include "OAICollectionAnalyticData.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICollectionAnalyticData::OAICollectionAnalyticData(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICollectionAnalyticData::OAICollectionAnalyticData() {
    this->initializeModel();
}

OAICollectionAnalyticData::~OAICollectionAnalyticData() {}

void OAICollectionAnalyticData::initializeModel() {

    m_config_id_isSet = false;
    m_config_id_isValid = false;

    m_entities_isSet = false;
    m_entities_isValid = false;

    m_facets_isSet = false;
    m_facets_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_job_id_isSet = false;
    m_job_id_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_tag_isSet = false;
    m_tag_isValid = false;

    m_taxonomy_isSet = false;
    m_taxonomy_isValid = false;

    m_themes_isSet = false;
    m_themes_isValid = false;

    m_topics_isSet = false;
    m_topics_isValid = false;
}

void OAICollectionAnalyticData::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICollectionAnalyticData::fromJsonObject(QJsonObject json) {

    m_config_id_isValid = ::OpenAPI::fromJsonValue(m_config_id, json[QString("config_id")]);
    m_config_id_isSet = !json[QString("config_id")].isNull() && m_config_id_isValid;

    m_entities_isValid = ::OpenAPI::fromJsonValue(m_entities, json[QString("entities")]);
    m_entities_isSet = !json[QString("entities")].isNull() && m_entities_isValid;

    m_facets_isValid = ::OpenAPI::fromJsonValue(m_facets, json[QString("facets")]);
    m_facets_isSet = !json[QString("facets")].isNull() && m_facets_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_job_id_isValid = ::OpenAPI::fromJsonValue(m_job_id, json[QString("job_id")]);
    m_job_id_isSet = !json[QString("job_id")].isNull() && m_job_id_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_tag_isValid = ::OpenAPI::fromJsonValue(m_tag, json[QString("tag")]);
    m_tag_isSet = !json[QString("tag")].isNull() && m_tag_isValid;

    m_taxonomy_isValid = ::OpenAPI::fromJsonValue(m_taxonomy, json[QString("taxonomy")]);
    m_taxonomy_isSet = !json[QString("taxonomy")].isNull() && m_taxonomy_isValid;

    m_themes_isValid = ::OpenAPI::fromJsonValue(m_themes, json[QString("themes")]);
    m_themes_isSet = !json[QString("themes")].isNull() && m_themes_isValid;

    m_topics_isValid = ::OpenAPI::fromJsonValue(m_topics, json[QString("topics")]);
    m_topics_isSet = !json[QString("topics")].isNull() && m_topics_isValid;
}

QString OAICollectionAnalyticData::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICollectionAnalyticData::asJsonObject() const {
    QJsonObject obj;
    if (m_config_id_isSet) {
        obj.insert(QString("config_id"), ::OpenAPI::toJsonValue(m_config_id));
    }
    if (m_entities.size() > 0) {
        obj.insert(QString("entities"), ::OpenAPI::toJsonValue(m_entities));
    }
    if (m_facets.size() > 0) {
        obj.insert(QString("facets"), ::OpenAPI::toJsonValue(m_facets));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_job_id_isSet) {
        obj.insert(QString("job_id"), ::OpenAPI::toJsonValue(m_job_id));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_tag_isSet) {
        obj.insert(QString("tag"), ::OpenAPI::toJsonValue(m_tag));
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

QString OAICollectionAnalyticData::getConfigId() const {
    return m_config_id;
}
void OAICollectionAnalyticData::setConfigId(const QString &config_id) {
    m_config_id = config_id;
    m_config_id_isSet = true;
}

bool OAICollectionAnalyticData::is_config_id_Set() const{
    return m_config_id_isSet;
}

bool OAICollectionAnalyticData::is_config_id_Valid() const{
    return m_config_id_isValid;
}

QList<OAIEntity> OAICollectionAnalyticData::getEntities() const {
    return m_entities;
}
void OAICollectionAnalyticData::setEntities(const QList<OAIEntity> &entities) {
    m_entities = entities;
    m_entities_isSet = true;
}

bool OAICollectionAnalyticData::is_entities_Set() const{
    return m_entities_isSet;
}

bool OAICollectionAnalyticData::is_entities_Valid() const{
    return m_entities_isValid;
}

QList<OAIFacet> OAICollectionAnalyticData::getFacets() const {
    return m_facets;
}
void OAICollectionAnalyticData::setFacets(const QList<OAIFacet> &facets) {
    m_facets = facets;
    m_facets_isSet = true;
}

bool OAICollectionAnalyticData::is_facets_Set() const{
    return m_facets_isSet;
}

bool OAICollectionAnalyticData::is_facets_Valid() const{
    return m_facets_isValid;
}

QString OAICollectionAnalyticData::getId() const {
    return m_id;
}
void OAICollectionAnalyticData::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAICollectionAnalyticData::is_id_Set() const{
    return m_id_isSet;
}

bool OAICollectionAnalyticData::is_id_Valid() const{
    return m_id_isValid;
}

QString OAICollectionAnalyticData::getJobId() const {
    return m_job_id;
}
void OAICollectionAnalyticData::setJobId(const QString &job_id) {
    m_job_id = job_id;
    m_job_id_isSet = true;
}

bool OAICollectionAnalyticData::is_job_id_Set() const{
    return m_job_id_isSet;
}

bool OAICollectionAnalyticData::is_job_id_Valid() const{
    return m_job_id_isValid;
}

QString OAICollectionAnalyticData::getStatus() const {
    return m_status;
}
void OAICollectionAnalyticData::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAICollectionAnalyticData::is_status_Set() const{
    return m_status_isSet;
}

bool OAICollectionAnalyticData::is_status_Valid() const{
    return m_status_isValid;
}

QString OAICollectionAnalyticData::getTag() const {
    return m_tag;
}
void OAICollectionAnalyticData::setTag(const QString &tag) {
    m_tag = tag;
    m_tag_isSet = true;
}

bool OAICollectionAnalyticData::is_tag_Set() const{
    return m_tag_isSet;
}

bool OAICollectionAnalyticData::is_tag_Valid() const{
    return m_tag_isValid;
}

QList<OAITopic> OAICollectionAnalyticData::getTaxonomy() const {
    return m_taxonomy;
}
void OAICollectionAnalyticData::setTaxonomy(const QList<OAITopic> &taxonomy) {
    m_taxonomy = taxonomy;
    m_taxonomy_isSet = true;
}

bool OAICollectionAnalyticData::is_taxonomy_Set() const{
    return m_taxonomy_isSet;
}

bool OAICollectionAnalyticData::is_taxonomy_Valid() const{
    return m_taxonomy_isValid;
}

QList<OAITheme> OAICollectionAnalyticData::getThemes() const {
    return m_themes;
}
void OAICollectionAnalyticData::setThemes(const QList<OAITheme> &themes) {
    m_themes = themes;
    m_themes_isSet = true;
}

bool OAICollectionAnalyticData::is_themes_Set() const{
    return m_themes_isSet;
}

bool OAICollectionAnalyticData::is_themes_Valid() const{
    return m_themes_isValid;
}

QList<OAITopic> OAICollectionAnalyticData::getTopics() const {
    return m_topics;
}
void OAICollectionAnalyticData::setTopics(const QList<OAITopic> &topics) {
    m_topics = topics;
    m_topics_isSet = true;
}

bool OAICollectionAnalyticData::is_topics_Set() const{
    return m_topics_isSet;
}

bool OAICollectionAnalyticData::is_topics_Valid() const{
    return m_topics_isValid;
}

bool OAICollectionAnalyticData::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_config_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_entities.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_facets.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_job_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tag_isSet) {
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

bool OAICollectionAnalyticData::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_config_id_isValid && m_entities_isValid && m_facets_isValid && m_id_isValid && m_job_id_isValid && m_status_isValid && m_tag_isValid && m_taxonomy_isValid && m_themes_isValid && m_topics_isValid && true;
}

} // namespace OpenAPI
