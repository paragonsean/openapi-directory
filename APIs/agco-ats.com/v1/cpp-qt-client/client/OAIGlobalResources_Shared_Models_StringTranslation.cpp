/**
 * AGCO API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIGlobalResources_Shared_Models_StringTranslation.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGlobalResources_Shared_Models_StringTranslation::OAIGlobalResources_Shared_Models_StringTranslation(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGlobalResources_Shared_Models_StringTranslation::OAIGlobalResources_Shared_Models_StringTranslation() {
    this->initializeModel();
}

OAIGlobalResources_Shared_Models_StringTranslation::~OAIGlobalResources_Shared_Models_StringTranslation() {}

void OAIGlobalResources_Shared_Models_StringTranslation::initializeModel() {

    m_author_id_isSet = false;
    m_author_id_isValid = false;

    m_language_id_isSet = false;
    m_language_id_isValid = false;

    m_state_isSet = false;
    m_state_isValid = false;

    m_string_id_isSet = false;
    m_string_id_isValid = false;

    m_string_value_isSet = false;
    m_string_value_isValid = false;

    m_timestamp_isSet = false;
    m_timestamp_isValid = false;
}

void OAIGlobalResources_Shared_Models_StringTranslation::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGlobalResources_Shared_Models_StringTranslation::fromJsonObject(QJsonObject json) {

    m_author_id_isValid = ::OpenAPI::fromJsonValue(m_author_id, json[QString("AuthorId")]);
    m_author_id_isSet = !json[QString("AuthorId")].isNull() && m_author_id_isValid;

    m_language_id_isValid = ::OpenAPI::fromJsonValue(m_language_id, json[QString("LanguageId")]);
    m_language_id_isSet = !json[QString("LanguageId")].isNull() && m_language_id_isValid;

    m_state_isValid = ::OpenAPI::fromJsonValue(m_state, json[QString("State")]);
    m_state_isSet = !json[QString("State")].isNull() && m_state_isValid;

    m_string_id_isValid = ::OpenAPI::fromJsonValue(m_string_id, json[QString("StringId")]);
    m_string_id_isSet = !json[QString("StringId")].isNull() && m_string_id_isValid;

    m_string_value_isValid = ::OpenAPI::fromJsonValue(m_string_value, json[QString("StringValue")]);
    m_string_value_isSet = !json[QString("StringValue")].isNull() && m_string_value_isValid;

    m_timestamp_isValid = ::OpenAPI::fromJsonValue(m_timestamp, json[QString("Timestamp")]);
    m_timestamp_isSet = !json[QString("Timestamp")].isNull() && m_timestamp_isValid;
}

QString OAIGlobalResources_Shared_Models_StringTranslation::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGlobalResources_Shared_Models_StringTranslation::asJsonObject() const {
    QJsonObject obj;
    if (m_author_id_isSet) {
        obj.insert(QString("AuthorId"), ::OpenAPI::toJsonValue(m_author_id));
    }
    if (m_language_id_isSet) {
        obj.insert(QString("LanguageId"), ::OpenAPI::toJsonValue(m_language_id));
    }
    if (m_state_isSet) {
        obj.insert(QString("State"), ::OpenAPI::toJsonValue(m_state));
    }
    if (m_string_id_isSet) {
        obj.insert(QString("StringId"), ::OpenAPI::toJsonValue(m_string_id));
    }
    if (m_string_value_isSet) {
        obj.insert(QString("StringValue"), ::OpenAPI::toJsonValue(m_string_value));
    }
    if (m_timestamp_isSet) {
        obj.insert(QString("Timestamp"), ::OpenAPI::toJsonValue(m_timestamp));
    }
    return obj;
}

qint32 OAIGlobalResources_Shared_Models_StringTranslation::getAuthorId() const {
    return m_author_id;
}
void OAIGlobalResources_Shared_Models_StringTranslation::setAuthorId(const qint32 &author_id) {
    m_author_id = author_id;
    m_author_id_isSet = true;
}

bool OAIGlobalResources_Shared_Models_StringTranslation::is_author_id_Set() const{
    return m_author_id_isSet;
}

bool OAIGlobalResources_Shared_Models_StringTranslation::is_author_id_Valid() const{
    return m_author_id_isValid;
}

qint32 OAIGlobalResources_Shared_Models_StringTranslation::getLanguageId() const {
    return m_language_id;
}
void OAIGlobalResources_Shared_Models_StringTranslation::setLanguageId(const qint32 &language_id) {
    m_language_id = language_id;
    m_language_id_isSet = true;
}

bool OAIGlobalResources_Shared_Models_StringTranslation::is_language_id_Set() const{
    return m_language_id_isSet;
}

bool OAIGlobalResources_Shared_Models_StringTranslation::is_language_id_Valid() const{
    return m_language_id_isValid;
}

QString OAIGlobalResources_Shared_Models_StringTranslation::getState() const {
    return m_state;
}
void OAIGlobalResources_Shared_Models_StringTranslation::setState(const QString &state) {
    m_state = state;
    m_state_isSet = true;
}

bool OAIGlobalResources_Shared_Models_StringTranslation::is_state_Set() const{
    return m_state_isSet;
}

bool OAIGlobalResources_Shared_Models_StringTranslation::is_state_Valid() const{
    return m_state_isValid;
}

QString OAIGlobalResources_Shared_Models_StringTranslation::getStringId() const {
    return m_string_id;
}
void OAIGlobalResources_Shared_Models_StringTranslation::setStringId(const QString &string_id) {
    m_string_id = string_id;
    m_string_id_isSet = true;
}

bool OAIGlobalResources_Shared_Models_StringTranslation::is_string_id_Set() const{
    return m_string_id_isSet;
}

bool OAIGlobalResources_Shared_Models_StringTranslation::is_string_id_Valid() const{
    return m_string_id_isValid;
}

QString OAIGlobalResources_Shared_Models_StringTranslation::getStringValue() const {
    return m_string_value;
}
void OAIGlobalResources_Shared_Models_StringTranslation::setStringValue(const QString &string_value) {
    m_string_value = string_value;
    m_string_value_isSet = true;
}

bool OAIGlobalResources_Shared_Models_StringTranslation::is_string_value_Set() const{
    return m_string_value_isSet;
}

bool OAIGlobalResources_Shared_Models_StringTranslation::is_string_value_Valid() const{
    return m_string_value_isValid;
}

QByteArray OAIGlobalResources_Shared_Models_StringTranslation::getTimestamp() const {
    return m_timestamp;
}
void OAIGlobalResources_Shared_Models_StringTranslation::setTimestamp(const QByteArray &timestamp) {
    m_timestamp = timestamp;
    m_timestamp_isSet = true;
}

bool OAIGlobalResources_Shared_Models_StringTranslation::is_timestamp_Set() const{
    return m_timestamp_isSet;
}

bool OAIGlobalResources_Shared_Models_StringTranslation::is_timestamp_Valid() const{
    return m_timestamp_isValid;
}

bool OAIGlobalResources_Shared_Models_StringTranslation::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_author_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_language_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_state_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_string_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_string_value_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_timestamp_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGlobalResources_Shared_Models_StringTranslation::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_string_value_isValid && true;
}

} // namespace OpenAPI
