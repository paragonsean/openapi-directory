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

#include "OAIErrorResponsev2.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIErrorResponsev2::OAIErrorResponsev2(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIErrorResponsev2::OAIErrorResponsev2() {
    this->initializeModel();
}

OAIErrorResponsev2::~OAIErrorResponsev2() {}

void OAIErrorResponsev2::initializeModel() {

    m_error_isSet = false;
    m_error_isValid = false;
}

void OAIErrorResponsev2::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIErrorResponsev2::fromJsonObject(QJsonObject json) {

    m_error_isValid = ::OpenAPI::fromJsonValue(m_error, json[QString("error")]);
    m_error_isSet = !json[QString("error")].isNull() && m_error_isValid;
}

QString OAIErrorResponsev2::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIErrorResponsev2::asJsonObject() const {
    QJsonObject obj;
    if (m_error.isSet()) {
        obj.insert(QString("error"), ::OpenAPI::toJsonValue(m_error));
    }
    return obj;
}

OAIUsers_getUserMetadata_default_response_error OAIErrorResponsev2::getError() const {
    return m_error;
}
void OAIErrorResponsev2::setError(const OAIUsers_getUserMetadata_default_response_error &error) {
    m_error = error;
    m_error_isSet = true;
}

bool OAIErrorResponsev2::is_error_Set() const{
    return m_error_isSet;
}

bool OAIErrorResponsev2::is_error_Valid() const{
    return m_error_isValid;
}

bool OAIErrorResponsev2::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_error.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIErrorResponsev2::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_error_isValid && true;
}

} // namespace OpenAPI
