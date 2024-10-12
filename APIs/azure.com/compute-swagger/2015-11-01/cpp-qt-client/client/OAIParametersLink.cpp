/**
 * ComputeManagementConvenienceClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2015-11-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIParametersLink.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIParametersLink::OAIParametersLink(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIParametersLink::OAIParametersLink() {
    this->initializeModel();
}

OAIParametersLink::~OAIParametersLink() {}

void OAIParametersLink::initializeModel() {

    m_content_version_isSet = false;
    m_content_version_isValid = false;

    m_uri_isSet = false;
    m_uri_isValid = false;
}

void OAIParametersLink::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIParametersLink::fromJsonObject(QJsonObject json) {

    m_content_version_isValid = ::OpenAPI::fromJsonValue(m_content_version, json[QString("contentVersion")]);
    m_content_version_isSet = !json[QString("contentVersion")].isNull() && m_content_version_isValid;

    m_uri_isValid = ::OpenAPI::fromJsonValue(m_uri, json[QString("uri")]);
    m_uri_isSet = !json[QString("uri")].isNull() && m_uri_isValid;
}

QString OAIParametersLink::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIParametersLink::asJsonObject() const {
    QJsonObject obj;
    if (m_content_version_isSet) {
        obj.insert(QString("contentVersion"), ::OpenAPI::toJsonValue(m_content_version));
    }
    if (m_uri_isSet) {
        obj.insert(QString("uri"), ::OpenAPI::toJsonValue(m_uri));
    }
    return obj;
}

QString OAIParametersLink::getContentVersion() const {
    return m_content_version;
}
void OAIParametersLink::setContentVersion(const QString &content_version) {
    m_content_version = content_version;
    m_content_version_isSet = true;
}

bool OAIParametersLink::is_content_version_Set() const{
    return m_content_version_isSet;
}

bool OAIParametersLink::is_content_version_Valid() const{
    return m_content_version_isValid;
}

QString OAIParametersLink::getUri() const {
    return m_uri;
}
void OAIParametersLink::setUri(const QString &uri) {
    m_uri = uri;
    m_uri_isSet = true;
}

bool OAIParametersLink::is_uri_Set() const{
    return m_uri_isSet;
}

bool OAIParametersLink::is_uri_Valid() const{
    return m_uri_isValid;
}

bool OAIParametersLink::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_content_version_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_uri_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIParametersLink::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_uri_isValid && true;
}

} // namespace OpenAPI
