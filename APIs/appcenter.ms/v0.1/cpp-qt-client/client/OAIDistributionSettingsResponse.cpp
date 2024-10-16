/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIDistributionSettingsResponse.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIDistributionSettingsResponse::OAIDistributionSettingsResponse(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIDistributionSettingsResponse::OAIDistributionSettingsResponse() {
    this->initializeModel();
}

OAIDistributionSettingsResponse::~OAIDistributionSettingsResponse() {}

void OAIDistributionSettingsResponse::initializeModel() {

    m_default_public_isSet = false;
    m_default_public_isValid = false;
}

void OAIDistributionSettingsResponse::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIDistributionSettingsResponse::fromJsonObject(QJsonObject json) {

    m_default_public_isValid = ::OpenAPI::fromJsonValue(m_default_public, json[QString("default_public")]);
    m_default_public_isSet = !json[QString("default_public")].isNull() && m_default_public_isValid;
}

QString OAIDistributionSettingsResponse::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIDistributionSettingsResponse::asJsonObject() const {
    QJsonObject obj;
    if (m_default_public_isSet) {
        obj.insert(QString("default_public"), ::OpenAPI::toJsonValue(m_default_public));
    }
    return obj;
}

bool OAIDistributionSettingsResponse::isDefaultPublic() const {
    return m_default_public;
}
void OAIDistributionSettingsResponse::setDefaultPublic(const bool &default_public) {
    m_default_public = default_public;
    m_default_public_isSet = true;
}

bool OAIDistributionSettingsResponse::is_default_public_Set() const{
    return m_default_public_isSet;
}

bool OAIDistributionSettingsResponse::is_default_public_Valid() const{
    return m_default_public_isValid;
}

bool OAIDistributionSettingsResponse::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_default_public_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIDistributionSettingsResponse::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_default_public_isValid && true;
}

} // namespace OpenAPI
