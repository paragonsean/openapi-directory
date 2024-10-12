/**
 * Azure Machine Learning Model Management Service
 * These APIs allow end users to manage Azure Machine Learning Models, Images, Profiles, and Services.
 *
 * The version of the OpenAPI document: 2019-09-30
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAsset.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAsset::OAIAsset(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAsset::OAIAsset() {
    this->initializeModel();
}

OAIAsset::~OAIAsset() {}

void OAIAsset::initializeModel() {

    m_artifacts_isSet = false;
    m_artifacts_isValid = false;

    m_created_time_isSet = false;
    m_created_time_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_kv_tags_isSet = false;
    m_kv_tags_isValid = false;

    m_meta_isSet = false;
    m_meta_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_properties_isSet = false;
    m_properties_isValid = false;

    m_runid_isSet = false;
    m_runid_isValid = false;
}

void OAIAsset::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAsset::fromJsonObject(QJsonObject json) {

    m_artifacts_isValid = ::OpenAPI::fromJsonValue(m_artifacts, json[QString("artifacts")]);
    m_artifacts_isSet = !json[QString("artifacts")].isNull() && m_artifacts_isValid;

    m_created_time_isValid = ::OpenAPI::fromJsonValue(m_created_time, json[QString("createdTime")]);
    m_created_time_isSet = !json[QString("createdTime")].isNull() && m_created_time_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_kv_tags_isValid = ::OpenAPI::fromJsonValue(m_kv_tags, json[QString("kvTags")]);
    m_kv_tags_isSet = !json[QString("kvTags")].isNull() && m_kv_tags_isValid;

    m_meta_isValid = ::OpenAPI::fromJsonValue(m_meta, json[QString("meta")]);
    m_meta_isSet = !json[QString("meta")].isNull() && m_meta_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_properties_isValid = ::OpenAPI::fromJsonValue(m_properties, json[QString("properties")]);
    m_properties_isSet = !json[QString("properties")].isNull() && m_properties_isValid;

    m_runid_isValid = ::OpenAPI::fromJsonValue(m_runid, json[QString("runid")]);
    m_runid_isSet = !json[QString("runid")].isNull() && m_runid_isValid;
}

QString OAIAsset::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAsset::asJsonObject() const {
    QJsonObject obj;
    if (m_artifacts.size() > 0) {
        obj.insert(QString("artifacts"), ::OpenAPI::toJsonValue(m_artifacts));
    }
    if (m_created_time_isSet) {
        obj.insert(QString("createdTime"), ::OpenAPI::toJsonValue(m_created_time));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_kv_tags.size() > 0) {
        obj.insert(QString("kvTags"), ::OpenAPI::toJsonValue(m_kv_tags));
    }
    if (m_meta.size() > 0) {
        obj.insert(QString("meta"), ::OpenAPI::toJsonValue(m_meta));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_properties.size() > 0) {
        obj.insert(QString("properties"), ::OpenAPI::toJsonValue(m_properties));
    }
    if (m_runid_isSet) {
        obj.insert(QString("runid"), ::OpenAPI::toJsonValue(m_runid));
    }
    return obj;
}

QList<OAIArtifactDetails> OAIAsset::getArtifacts() const {
    return m_artifacts;
}
void OAIAsset::setArtifacts(const QList<OAIArtifactDetails> &artifacts) {
    m_artifacts = artifacts;
    m_artifacts_isSet = true;
}

bool OAIAsset::is_artifacts_Set() const{
    return m_artifacts_isSet;
}

bool OAIAsset::is_artifacts_Valid() const{
    return m_artifacts_isValid;
}

QDateTime OAIAsset::getCreatedTime() const {
    return m_created_time;
}
void OAIAsset::setCreatedTime(const QDateTime &created_time) {
    m_created_time = created_time;
    m_created_time_isSet = true;
}

bool OAIAsset::is_created_time_Set() const{
    return m_created_time_isSet;
}

bool OAIAsset::is_created_time_Valid() const{
    return m_created_time_isValid;
}

QString OAIAsset::getDescription() const {
    return m_description;
}
void OAIAsset::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIAsset::is_description_Set() const{
    return m_description_isSet;
}

bool OAIAsset::is_description_Valid() const{
    return m_description_isValid;
}

QString OAIAsset::getId() const {
    return m_id;
}
void OAIAsset::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIAsset::is_id_Set() const{
    return m_id_isSet;
}

bool OAIAsset::is_id_Valid() const{
    return m_id_isValid;
}

QMap<QString, QString> OAIAsset::getKvTags() const {
    return m_kv_tags;
}
void OAIAsset::setKvTags(const QMap<QString, QString> &kv_tags) {
    m_kv_tags = kv_tags;
    m_kv_tags_isSet = true;
}

bool OAIAsset::is_kv_tags_Set() const{
    return m_kv_tags_isSet;
}

bool OAIAsset::is_kv_tags_Valid() const{
    return m_kv_tags_isValid;
}

QMap<QString, QString> OAIAsset::getMeta() const {
    return m_meta;
}
void OAIAsset::setMeta(const QMap<QString, QString> &meta) {
    m_meta = meta;
    m_meta_isSet = true;
}

bool OAIAsset::is_meta_Set() const{
    return m_meta_isSet;
}

bool OAIAsset::is_meta_Valid() const{
    return m_meta_isValid;
}

QString OAIAsset::getName() const {
    return m_name;
}
void OAIAsset::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIAsset::is_name_Set() const{
    return m_name_isSet;
}

bool OAIAsset::is_name_Valid() const{
    return m_name_isValid;
}

QMap<QString, QString> OAIAsset::getProperties() const {
    return m_properties;
}
void OAIAsset::setProperties(const QMap<QString, QString> &properties) {
    m_properties = properties;
    m_properties_isSet = true;
}

bool OAIAsset::is_properties_Set() const{
    return m_properties_isSet;
}

bool OAIAsset::is_properties_Valid() const{
    return m_properties_isValid;
}

QString OAIAsset::getRunid() const {
    return m_runid;
}
void OAIAsset::setRunid(const QString &runid) {
    m_runid = runid;
    m_runid_isSet = true;
}

bool OAIAsset::is_runid_Set() const{
    return m_runid_isSet;
}

bool OAIAsset::is_runid_Valid() const{
    return m_runid_isValid;
}

bool OAIAsset::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_artifacts.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_kv_tags.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_meta.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_properties.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_runid_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAsset::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_name_isValid && true;
}

} // namespace OpenAPI
