/**
 * Health Repository Provider Specifications for HIP
 * The following are the specifications for the APIs to be implemented at the Health Repository end if an entity is only serving the role of a HIP. The specs are essentially duplicates from the Gateway and Health Repository, but put together so as to make it clear to *HIPs* which set of APIs they should implement to participate in the network.  
 *
 * The version of the OpenAPI document: 0.5
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIOpenIdConfiguration.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIOpenIdConfiguration::OAIOpenIdConfiguration(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIOpenIdConfiguration::OAIOpenIdConfiguration() {
    this->initializeModel();
}

OAIOpenIdConfiguration::~OAIOpenIdConfiguration() {}

void OAIOpenIdConfiguration::initializeModel() {

    m_jwks_uri_isSet = false;
    m_jwks_uri_isValid = false;
}

void OAIOpenIdConfiguration::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIOpenIdConfiguration::fromJsonObject(QJsonObject json) {

    m_jwks_uri_isValid = ::OpenAPI::fromJsonValue(m_jwks_uri, json[QString("jwks_uri")]);
    m_jwks_uri_isSet = !json[QString("jwks_uri")].isNull() && m_jwks_uri_isValid;
}

QString OAIOpenIdConfiguration::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIOpenIdConfiguration::asJsonObject() const {
    QJsonObject obj;
    if (m_jwks_uri_isSet) {
        obj.insert(QString("jwks_uri"), ::OpenAPI::toJsonValue(m_jwks_uri));
    }
    return obj;
}

QString OAIOpenIdConfiguration::getJwksUri() const {
    return m_jwks_uri;
}
void OAIOpenIdConfiguration::setJwksUri(const QString &jwks_uri) {
    m_jwks_uri = jwks_uri;
    m_jwks_uri_isSet = true;
}

bool OAIOpenIdConfiguration::is_jwks_uri_Set() const{
    return m_jwks_uri_isSet;
}

bool OAIOpenIdConfiguration::is_jwks_uri_Valid() const{
    return m_jwks_uri_isValid;
}

bool OAIOpenIdConfiguration::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_jwks_uri_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIOpenIdConfiguration::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
