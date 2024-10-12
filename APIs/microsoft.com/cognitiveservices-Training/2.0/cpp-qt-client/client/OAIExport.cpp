/**
 * TrainingApi
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIExport.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIExport::OAIExport(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIExport::OAIExport() {
    this->initializeModel();
}

OAIExport::~OAIExport() {}

void OAIExport::initializeModel() {

    m_download_uri_isSet = false;
    m_download_uri_isValid = false;

    m_flavor_isSet = false;
    m_flavor_isValid = false;

    m_platform_isSet = false;
    m_platform_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;
}

void OAIExport::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIExport::fromJsonObject(QJsonObject json) {

    m_download_uri_isValid = ::OpenAPI::fromJsonValue(m_download_uri, json[QString("downloadUri")]);
    m_download_uri_isSet = !json[QString("downloadUri")].isNull() && m_download_uri_isValid;

    m_flavor_isValid = ::OpenAPI::fromJsonValue(m_flavor, json[QString("flavor")]);
    m_flavor_isSet = !json[QString("flavor")].isNull() && m_flavor_isValid;

    m_platform_isValid = ::OpenAPI::fromJsonValue(m_platform, json[QString("platform")]);
    m_platform_isSet = !json[QString("platform")].isNull() && m_platform_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;
}

QString OAIExport::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIExport::asJsonObject() const {
    QJsonObject obj;
    if (m_download_uri_isSet) {
        obj.insert(QString("downloadUri"), ::OpenAPI::toJsonValue(m_download_uri));
    }
    if (m_flavor_isSet) {
        obj.insert(QString("flavor"), ::OpenAPI::toJsonValue(m_flavor));
    }
    if (m_platform_isSet) {
        obj.insert(QString("platform"), ::OpenAPI::toJsonValue(m_platform));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    return obj;
}

QString OAIExport::getDownloadUri() const {
    return m_download_uri;
}
void OAIExport::setDownloadUri(const QString &download_uri) {
    m_download_uri = download_uri;
    m_download_uri_isSet = true;
}

bool OAIExport::is_download_uri_Set() const{
    return m_download_uri_isSet;
}

bool OAIExport::is_download_uri_Valid() const{
    return m_download_uri_isValid;
}

QString OAIExport::getFlavor() const {
    return m_flavor;
}
void OAIExport::setFlavor(const QString &flavor) {
    m_flavor = flavor;
    m_flavor_isSet = true;
}

bool OAIExport::is_flavor_Set() const{
    return m_flavor_isSet;
}

bool OAIExport::is_flavor_Valid() const{
    return m_flavor_isValid;
}

QString OAIExport::getPlatform() const {
    return m_platform;
}
void OAIExport::setPlatform(const QString &platform) {
    m_platform = platform;
    m_platform_isSet = true;
}

bool OAIExport::is_platform_Set() const{
    return m_platform_isSet;
}

bool OAIExport::is_platform_Valid() const{
    return m_platform_isValid;
}

QString OAIExport::getStatus() const {
    return m_status;
}
void OAIExport::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIExport::is_status_Set() const{
    return m_status_isSet;
}

bool OAIExport::is_status_Valid() const{
    return m_status_isValid;
}

bool OAIExport::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_download_uri_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_flavor_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_platform_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIExport::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
