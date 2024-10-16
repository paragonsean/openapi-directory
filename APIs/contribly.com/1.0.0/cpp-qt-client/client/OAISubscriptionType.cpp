/**
 * Contribly
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAISubscriptionType.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISubscriptionType::OAISubscriptionType(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISubscriptionType::OAISubscriptionType() {
    this->initializeModel();
}

OAISubscriptionType::~OAISubscriptionType() {}

void OAISubscriptionType::initializeModel() {

    m_id_isSet = false;
    m_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;
}

void OAISubscriptionType::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISubscriptionType::fromJsonObject(QJsonObject json) {

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;
}

QString OAISubscriptionType::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISubscriptionType::asJsonObject() const {
    QJsonObject obj;
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    return obj;
}

QString OAISubscriptionType::getId() const {
    return m_id;
}
void OAISubscriptionType::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAISubscriptionType::is_id_Set() const{
    return m_id_isSet;
}

bool OAISubscriptionType::is_id_Valid() const{
    return m_id_isValid;
}

QString OAISubscriptionType::getName() const {
    return m_name;
}
void OAISubscriptionType::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAISubscriptionType::is_name_Set() const{
    return m_name_isSet;
}

bool OAISubscriptionType::is_name_Valid() const{
    return m_name_isValid;
}

bool OAISubscriptionType::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISubscriptionType::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_id_isValid && m_name_isValid && true;
}

} // namespace OpenAPI
