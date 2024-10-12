/**
 * BatchManagement
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-08-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAICertificateBaseProperties.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICertificateBaseProperties::OAICertificateBaseProperties(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICertificateBaseProperties::OAICertificateBaseProperties() {
    this->initializeModel();
}

OAICertificateBaseProperties::~OAICertificateBaseProperties() {}

void OAICertificateBaseProperties::initializeModel() {

    m_format_isSet = false;
    m_format_isValid = false;

    m_thumbprint_isSet = false;
    m_thumbprint_isValid = false;

    m_thumbprint_algorithm_isSet = false;
    m_thumbprint_algorithm_isValid = false;
}

void OAICertificateBaseProperties::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICertificateBaseProperties::fromJsonObject(QJsonObject json) {

    m_format_isValid = ::OpenAPI::fromJsonValue(m_format, json[QString("format")]);
    m_format_isSet = !json[QString("format")].isNull() && m_format_isValid;

    m_thumbprint_isValid = ::OpenAPI::fromJsonValue(m_thumbprint, json[QString("thumbprint")]);
    m_thumbprint_isSet = !json[QString("thumbprint")].isNull() && m_thumbprint_isValid;

    m_thumbprint_algorithm_isValid = ::OpenAPI::fromJsonValue(m_thumbprint_algorithm, json[QString("thumbprintAlgorithm")]);
    m_thumbprint_algorithm_isSet = !json[QString("thumbprintAlgorithm")].isNull() && m_thumbprint_algorithm_isValid;
}

QString OAICertificateBaseProperties::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICertificateBaseProperties::asJsonObject() const {
    QJsonObject obj;
    if (m_format_isSet) {
        obj.insert(QString("format"), ::OpenAPI::toJsonValue(m_format));
    }
    if (m_thumbprint_isSet) {
        obj.insert(QString("thumbprint"), ::OpenAPI::toJsonValue(m_thumbprint));
    }
    if (m_thumbprint_algorithm_isSet) {
        obj.insert(QString("thumbprintAlgorithm"), ::OpenAPI::toJsonValue(m_thumbprint_algorithm));
    }
    return obj;
}

QString OAICertificateBaseProperties::getFormat() const {
    return m_format;
}
void OAICertificateBaseProperties::setFormat(const QString &format) {
    m_format = format;
    m_format_isSet = true;
}

bool OAICertificateBaseProperties::is_format_Set() const{
    return m_format_isSet;
}

bool OAICertificateBaseProperties::is_format_Valid() const{
    return m_format_isValid;
}

QString OAICertificateBaseProperties::getThumbprint() const {
    return m_thumbprint;
}
void OAICertificateBaseProperties::setThumbprint(const QString &thumbprint) {
    m_thumbprint = thumbprint;
    m_thumbprint_isSet = true;
}

bool OAICertificateBaseProperties::is_thumbprint_Set() const{
    return m_thumbprint_isSet;
}

bool OAICertificateBaseProperties::is_thumbprint_Valid() const{
    return m_thumbprint_isValid;
}

QString OAICertificateBaseProperties::getThumbprintAlgorithm() const {
    return m_thumbprint_algorithm;
}
void OAICertificateBaseProperties::setThumbprintAlgorithm(const QString &thumbprint_algorithm) {
    m_thumbprint_algorithm = thumbprint_algorithm;
    m_thumbprint_algorithm_isSet = true;
}

bool OAICertificateBaseProperties::is_thumbprint_algorithm_Set() const{
    return m_thumbprint_algorithm_isSet;
}

bool OAICertificateBaseProperties::is_thumbprint_algorithm_Valid() const{
    return m_thumbprint_algorithm_isValid;
}

bool OAICertificateBaseProperties::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_format_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_thumbprint_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_thumbprint_algorithm_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICertificateBaseProperties::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
