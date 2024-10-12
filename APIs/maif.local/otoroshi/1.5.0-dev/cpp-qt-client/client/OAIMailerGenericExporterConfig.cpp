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

#include "OAIMailerGenericExporterConfig.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIMailerGenericExporterConfig::OAIMailerGenericExporterConfig(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIMailerGenericExporterConfig::OAIMailerGenericExporterConfig() {
    this->initializeModel();
}

OAIMailerGenericExporterConfig::~OAIMailerGenericExporterConfig() {}

void OAIMailerGenericExporterConfig::initializeModel() {

    m_headers_isSet = false;
    m_headers_isValid = false;

    m_to_isSet = false;
    m_to_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;

    m_url_isSet = false;
    m_url_isValid = false;
}

void OAIMailerGenericExporterConfig::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIMailerGenericExporterConfig::fromJsonObject(QJsonObject json) {

    m_headers_isValid = ::OpenAPI::fromJsonValue(m_headers, json[QString("headers")]);
    m_headers_isSet = !json[QString("headers")].isNull() && m_headers_isValid;

    m_to_isValid = ::OpenAPI::fromJsonValue(m_to, json[QString("to")]);
    m_to_isSet = !json[QString("to")].isNull() && m_to_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;

    m_url_isValid = ::OpenAPI::fromJsonValue(m_url, json[QString("url")]);
    m_url_isSet = !json[QString("url")].isNull() && m_url_isValid;
}

QString OAIMailerGenericExporterConfig::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIMailerGenericExporterConfig::asJsonObject() const {
    QJsonObject obj;
    if (m_headers.size() > 0) {
        obj.insert(QString("headers"), ::OpenAPI::toJsonValue(m_headers));
    }
    if (m_to.size() > 0) {
        obj.insert(QString("to"), ::OpenAPI::toJsonValue(m_to));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    if (m_url_isSet) {
        obj.insert(QString("url"), ::OpenAPI::toJsonValue(m_url));
    }
    return obj;
}

QMap<QString, QString> OAIMailerGenericExporterConfig::getHeaders() const {
    return m_headers;
}
void OAIMailerGenericExporterConfig::setHeaders(const QMap<QString, QString> &headers) {
    m_headers = headers;
    m_headers_isSet = true;
}

bool OAIMailerGenericExporterConfig::is_headers_Set() const{
    return m_headers_isSet;
}

bool OAIMailerGenericExporterConfig::is_headers_Valid() const{
    return m_headers_isValid;
}

QList<QString> OAIMailerGenericExporterConfig::getTo() const {
    return m_to;
}
void OAIMailerGenericExporterConfig::setTo(const QList<QString> &to) {
    m_to = to;
    m_to_isSet = true;
}

bool OAIMailerGenericExporterConfig::is_to_Set() const{
    return m_to_isSet;
}

bool OAIMailerGenericExporterConfig::is_to_Valid() const{
    return m_to_isValid;
}

QString OAIMailerGenericExporterConfig::getType() const {
    return m_type;
}
void OAIMailerGenericExporterConfig::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIMailerGenericExporterConfig::is_type_Set() const{
    return m_type_isSet;
}

bool OAIMailerGenericExporterConfig::is_type_Valid() const{
    return m_type_isValid;
}

QString OAIMailerGenericExporterConfig::getUrl() const {
    return m_url;
}
void OAIMailerGenericExporterConfig::setUrl(const QString &url) {
    m_url = url;
    m_url_isSet = true;
}

bool OAIMailerGenericExporterConfig::is_url_Set() const{
    return m_url_isSet;
}

bool OAIMailerGenericExporterConfig::is_url_Valid() const{
    return m_url_isValid;
}

bool OAIMailerGenericExporterConfig::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_headers.size() > 0) {
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

        if (m_url_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIMailerGenericExporterConfig::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_type_isValid && true;
}

} // namespace OpenAPI
