/**
 * TrainingApi
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIImageTagCreateSummary.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIImageTagCreateSummary::OAIImageTagCreateSummary(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIImageTagCreateSummary::OAIImageTagCreateSummary() {
    this->initializeModel();
}

OAIImageTagCreateSummary::~OAIImageTagCreateSummary() {}

void OAIImageTagCreateSummary::initializeModel() {

    m_created_isSet = false;
    m_created_isValid = false;

    m_duplicated_isSet = false;
    m_duplicated_isValid = false;

    m_exceeded_isSet = false;
    m_exceeded_isValid = false;
}

void OAIImageTagCreateSummary::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIImageTagCreateSummary::fromJsonObject(QJsonObject json) {

    m_created_isValid = ::OpenAPI::fromJsonValue(m_created, json[QString("created")]);
    m_created_isSet = !json[QString("created")].isNull() && m_created_isValid;

    m_duplicated_isValid = ::OpenAPI::fromJsonValue(m_duplicated, json[QString("duplicated")]);
    m_duplicated_isSet = !json[QString("duplicated")].isNull() && m_duplicated_isValid;

    m_exceeded_isValid = ::OpenAPI::fromJsonValue(m_exceeded, json[QString("exceeded")]);
    m_exceeded_isSet = !json[QString("exceeded")].isNull() && m_exceeded_isValid;
}

QString OAIImageTagCreateSummary::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIImageTagCreateSummary::asJsonObject() const {
    QJsonObject obj;
    if (m_created.size() > 0) {
        obj.insert(QString("created"), ::OpenAPI::toJsonValue(m_created));
    }
    if (m_duplicated.size() > 0) {
        obj.insert(QString("duplicated"), ::OpenAPI::toJsonValue(m_duplicated));
    }
    if (m_exceeded.size() > 0) {
        obj.insert(QString("exceeded"), ::OpenAPI::toJsonValue(m_exceeded));
    }
    return obj;
}

QList<OAIImageTagCreateEntry> OAIImageTagCreateSummary::getCreated() const {
    return m_created;
}
void OAIImageTagCreateSummary::setCreated(const QList<OAIImageTagCreateEntry> &created) {
    m_created = created;
    m_created_isSet = true;
}

bool OAIImageTagCreateSummary::is_created_Set() const{
    return m_created_isSet;
}

bool OAIImageTagCreateSummary::is_created_Valid() const{
    return m_created_isValid;
}

QList<OAIImageTagCreateEntry> OAIImageTagCreateSummary::getDuplicated() const {
    return m_duplicated;
}
void OAIImageTagCreateSummary::setDuplicated(const QList<OAIImageTagCreateEntry> &duplicated) {
    m_duplicated = duplicated;
    m_duplicated_isSet = true;
}

bool OAIImageTagCreateSummary::is_duplicated_Set() const{
    return m_duplicated_isSet;
}

bool OAIImageTagCreateSummary::is_duplicated_Valid() const{
    return m_duplicated_isValid;
}

QList<OAIImageTagCreateEntry> OAIImageTagCreateSummary::getExceeded() const {
    return m_exceeded;
}
void OAIImageTagCreateSummary::setExceeded(const QList<OAIImageTagCreateEntry> &exceeded) {
    m_exceeded = exceeded;
    m_exceeded_isSet = true;
}

bool OAIImageTagCreateSummary::is_exceeded_Set() const{
    return m_exceeded_isSet;
}

bool OAIImageTagCreateSummary::is_exceeded_Valid() const{
    return m_exceeded_isValid;
}

bool OAIImageTagCreateSummary::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_created.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_duplicated.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_exceeded.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIImageTagCreateSummary::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
