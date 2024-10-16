/**
 * World Time API
 * A simple API to get the current time based on a request with a timezone.
 *
 * The version of the OpenAPI document: 20210108
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIErrorJsonResponse.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIErrorJsonResponse::OAIErrorJsonResponse(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIErrorJsonResponse::OAIErrorJsonResponse() {
    this->initializeModel();
}

OAIErrorJsonResponse::~OAIErrorJsonResponse() {}

void OAIErrorJsonResponse::initializeModel() {

    m_error_isSet = false;
    m_error_isValid = false;
}

void OAIErrorJsonResponse::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIErrorJsonResponse::fromJsonObject(QJsonObject json) {

    m_error_isValid = ::OpenAPI::fromJsonValue(m_error, json[QString("error")]);
    m_error_isSet = !json[QString("error")].isNull() && m_error_isValid;
}

QString OAIErrorJsonResponse::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIErrorJsonResponse::asJsonObject() const {
    QJsonObject obj;
    if (m_error_isSet) {
        obj.insert(QString("error"), ::OpenAPI::toJsonValue(m_error));
    }
    return obj;
}

QString OAIErrorJsonResponse::getError() const {
    return m_error;
}
void OAIErrorJsonResponse::setError(const QString &error) {
    m_error = error;
    m_error_isSet = true;
}

bool OAIErrorJsonResponse::is_error_Set() const{
    return m_error_isSet;
}

bool OAIErrorJsonResponse::is_error_Valid() const{
    return m_error_isValid;
}

bool OAIErrorJsonResponse::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_error_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIErrorJsonResponse::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_error_isValid && true;
}

} // namespace OpenAPI
