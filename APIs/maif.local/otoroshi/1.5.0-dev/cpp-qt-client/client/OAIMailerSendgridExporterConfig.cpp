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

#include "OAIMailerSendgridExporterConfig.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIMailerSendgridExporterConfig::OAIMailerSendgridExporterConfig(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIMailerSendgridExporterConfig::OAIMailerSendgridExporterConfig() {
    this->initializeModel();
}

OAIMailerSendgridExporterConfig::~OAIMailerSendgridExporterConfig() {}

void OAIMailerSendgridExporterConfig::initializeModel() {

    m_api_key_public_isSet = false;
    m_api_key_public_isValid = false;

    m_to_isSet = false;
    m_to_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIMailerSendgridExporterConfig::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIMailerSendgridExporterConfig::fromJsonObject(QJsonObject json) {

    m_api_key_public_isValid = ::OpenAPI::fromJsonValue(m_api_key_public, json[QString("apiKeyPublic")]);
    m_api_key_public_isSet = !json[QString("apiKeyPublic")].isNull() && m_api_key_public_isValid;

    m_to_isValid = ::OpenAPI::fromJsonValue(m_to, json[QString("to")]);
    m_to_isSet = !json[QString("to")].isNull() && m_to_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAIMailerSendgridExporterConfig::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIMailerSendgridExporterConfig::asJsonObject() const {
    QJsonObject obj;
    if (m_api_key_public_isSet) {
        obj.insert(QString("apiKeyPublic"), ::OpenAPI::toJsonValue(m_api_key_public));
    }
    if (m_to.size() > 0) {
        obj.insert(QString("to"), ::OpenAPI::toJsonValue(m_to));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

QString OAIMailerSendgridExporterConfig::getApiKeyPublic() const {
    return m_api_key_public;
}
void OAIMailerSendgridExporterConfig::setApiKeyPublic(const QString &api_key_public) {
    m_api_key_public = api_key_public;
    m_api_key_public_isSet = true;
}

bool OAIMailerSendgridExporterConfig::is_api_key_public_Set() const{
    return m_api_key_public_isSet;
}

bool OAIMailerSendgridExporterConfig::is_api_key_public_Valid() const{
    return m_api_key_public_isValid;
}

QList<QString> OAIMailerSendgridExporterConfig::getTo() const {
    return m_to;
}
void OAIMailerSendgridExporterConfig::setTo(const QList<QString> &to) {
    m_to = to;
    m_to_isSet = true;
}

bool OAIMailerSendgridExporterConfig::is_to_Set() const{
    return m_to_isSet;
}

bool OAIMailerSendgridExporterConfig::is_to_Valid() const{
    return m_to_isValid;
}

QString OAIMailerSendgridExporterConfig::getType() const {
    return m_type;
}
void OAIMailerSendgridExporterConfig::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIMailerSendgridExporterConfig::is_type_Set() const{
    return m_type_isSet;
}

bool OAIMailerSendgridExporterConfig::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIMailerSendgridExporterConfig::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_api_key_public_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_to.size() > 0) {
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

bool OAIMailerSendgridExporterConfig::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_type_isValid && true;
}

} // namespace OpenAPI
