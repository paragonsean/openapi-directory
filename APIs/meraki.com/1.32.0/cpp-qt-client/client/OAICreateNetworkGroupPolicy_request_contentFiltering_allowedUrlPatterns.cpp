/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAICreateNetworkGroupPolicy_request_contentFiltering_allowedUrlPatterns.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICreateNetworkGroupPolicy_request_contentFiltering_allowedUrlPatterns::OAICreateNetworkGroupPolicy_request_contentFiltering_allowedUrlPatterns(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICreateNetworkGroupPolicy_request_contentFiltering_allowedUrlPatterns::OAICreateNetworkGroupPolicy_request_contentFiltering_allowedUrlPatterns() {
    this->initializeModel();
}

OAICreateNetworkGroupPolicy_request_contentFiltering_allowedUrlPatterns::~OAICreateNetworkGroupPolicy_request_contentFiltering_allowedUrlPatterns() {}

void OAICreateNetworkGroupPolicy_request_contentFiltering_allowedUrlPatterns::initializeModel() {

    m_patterns_isSet = false;
    m_patterns_isValid = false;

    m_settings_isSet = false;
    m_settings_isValid = false;
}

void OAICreateNetworkGroupPolicy_request_contentFiltering_allowedUrlPatterns::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICreateNetworkGroupPolicy_request_contentFiltering_allowedUrlPatterns::fromJsonObject(QJsonObject json) {

    m_patterns_isValid = ::OpenAPI::fromJsonValue(m_patterns, json[QString("patterns")]);
    m_patterns_isSet = !json[QString("patterns")].isNull() && m_patterns_isValid;

    m_settings_isValid = ::OpenAPI::fromJsonValue(m_settings, json[QString("settings")]);
    m_settings_isSet = !json[QString("settings")].isNull() && m_settings_isValid;
}

QString OAICreateNetworkGroupPolicy_request_contentFiltering_allowedUrlPatterns::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICreateNetworkGroupPolicy_request_contentFiltering_allowedUrlPatterns::asJsonObject() const {
    QJsonObject obj;
    if (m_patterns.size() > 0) {
        obj.insert(QString("patterns"), ::OpenAPI::toJsonValue(m_patterns));
    }
    if (m_settings_isSet) {
        obj.insert(QString("settings"), ::OpenAPI::toJsonValue(m_settings));
    }
    return obj;
}

QList<QString> OAICreateNetworkGroupPolicy_request_contentFiltering_allowedUrlPatterns::getPatterns() const {
    return m_patterns;
}
void OAICreateNetworkGroupPolicy_request_contentFiltering_allowedUrlPatterns::setPatterns(const QList<QString> &patterns) {
    m_patterns = patterns;
    m_patterns_isSet = true;
}

bool OAICreateNetworkGroupPolicy_request_contentFiltering_allowedUrlPatterns::is_patterns_Set() const{
    return m_patterns_isSet;
}

bool OAICreateNetworkGroupPolicy_request_contentFiltering_allowedUrlPatterns::is_patterns_Valid() const{
    return m_patterns_isValid;
}

QString OAICreateNetworkGroupPolicy_request_contentFiltering_allowedUrlPatterns::getSettings() const {
    return m_settings;
}
void OAICreateNetworkGroupPolicy_request_contentFiltering_allowedUrlPatterns::setSettings(const QString &settings) {
    m_settings = settings;
    m_settings_isSet = true;
}

bool OAICreateNetworkGroupPolicy_request_contentFiltering_allowedUrlPatterns::is_settings_Set() const{
    return m_settings_isSet;
}

bool OAICreateNetworkGroupPolicy_request_contentFiltering_allowedUrlPatterns::is_settings_Valid() const{
    return m_settings_isValid;
}

bool OAICreateNetworkGroupPolicy_request_contentFiltering_allowedUrlPatterns::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_patterns.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_settings_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICreateNetworkGroupPolicy_request_contentFiltering_allowedUrlPatterns::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
