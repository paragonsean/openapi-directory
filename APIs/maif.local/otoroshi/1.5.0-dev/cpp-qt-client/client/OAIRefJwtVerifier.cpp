/**
 * Otoroshi Admin API
 * Admin API of the Otoroshi reverse proxy
 *
 * The version of the OpenAPI document: 1.5.0-dev
 * Contact: oss@maif.fr
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIRefJwtVerifier.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIRefJwtVerifier::OAIRefJwtVerifier(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIRefJwtVerifier::OAIRefJwtVerifier() {
    this->initializeModel();
}

OAIRefJwtVerifier::~OAIRefJwtVerifier() {}

void OAIRefJwtVerifier::initializeModel() {

    m_enabled_isSet = false;
    m_enabled_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIRefJwtVerifier::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIRefJwtVerifier::fromJsonObject(QJsonObject json) {

    m_enabled_isValid = ::OpenAPI::fromJsonValue(m_enabled, json[QString("enabled")]);
    m_enabled_isSet = !json[QString("enabled")].isNull() && m_enabled_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAIRefJwtVerifier::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIRefJwtVerifier::asJsonObject() const {
    QJsonObject obj;
    if (m_enabled_isSet) {
        obj.insert(QString("enabled"), ::OpenAPI::toJsonValue(m_enabled));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

bool OAIRefJwtVerifier::isEnabled() const {
    return m_enabled;
}
void OAIRefJwtVerifier::setEnabled(const bool &enabled) {
    m_enabled = enabled;
    m_enabled_isSet = true;
}

bool OAIRefJwtVerifier::is_enabled_Set() const{
    return m_enabled_isSet;
}

bool OAIRefJwtVerifier::is_enabled_Valid() const{
    return m_enabled_isValid;
}

QString OAIRefJwtVerifier::getId() const {
    return m_id;
}
void OAIRefJwtVerifier::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIRefJwtVerifier::is_id_Set() const{
    return m_id_isSet;
}

bool OAIRefJwtVerifier::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIRefJwtVerifier::getType() const {
    return m_type;
}
void OAIRefJwtVerifier::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIRefJwtVerifier::is_type_Set() const{
    return m_type_isSet;
}

bool OAIRefJwtVerifier::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIRefJwtVerifier::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_enabled_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIRefJwtVerifier::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_enabled_isValid && m_id_isValid && m_type_isValid && true;
}

} // namespace OpenAPI
