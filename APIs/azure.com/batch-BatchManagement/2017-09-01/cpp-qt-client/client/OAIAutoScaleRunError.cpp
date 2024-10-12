/**
 * BatchManagement
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2017-09-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAutoScaleRunError.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAutoScaleRunError::OAIAutoScaleRunError(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAutoScaleRunError::OAIAutoScaleRunError() {
    this->initializeModel();
}

OAIAutoScaleRunError::~OAIAutoScaleRunError() {}

void OAIAutoScaleRunError::initializeModel() {

    m_code_isSet = false;
    m_code_isValid = false;

    m_details_isSet = false;
    m_details_isValid = false;

    m_message_isSet = false;
    m_message_isValid = false;
}

void OAIAutoScaleRunError::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAutoScaleRunError::fromJsonObject(QJsonObject json) {

    m_code_isValid = ::OpenAPI::fromJsonValue(m_code, json[QString("code")]);
    m_code_isSet = !json[QString("code")].isNull() && m_code_isValid;

    m_details_isValid = ::OpenAPI::fromJsonValue(m_details, json[QString("details")]);
    m_details_isSet = !json[QString("details")].isNull() && m_details_isValid;

    m_message_isValid = ::OpenAPI::fromJsonValue(m_message, json[QString("message")]);
    m_message_isSet = !json[QString("message")].isNull() && m_message_isValid;
}

QString OAIAutoScaleRunError::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAutoScaleRunError::asJsonObject() const {
    QJsonObject obj;
    if (m_code_isSet) {
        obj.insert(QString("code"), ::OpenAPI::toJsonValue(m_code));
    }
    if (m_details.size() > 0) {
        obj.insert(QString("details"), ::OpenAPI::toJsonValue(m_details));
    }
    if (m_message_isSet) {
        obj.insert(QString("message"), ::OpenAPI::toJsonValue(m_message));
    }
    return obj;
}

QString OAIAutoScaleRunError::getCode() const {
    return m_code;
}
void OAIAutoScaleRunError::setCode(const QString &code) {
    m_code = code;
    m_code_isSet = true;
}

bool OAIAutoScaleRunError::is_code_Set() const{
    return m_code_isSet;
}

bool OAIAutoScaleRunError::is_code_Valid() const{
    return m_code_isValid;
}

QList<OAIAutoScaleRunError> OAIAutoScaleRunError::getDetails() const {
    return m_details;
}
void OAIAutoScaleRunError::setDetails(const QList<OAIAutoScaleRunError> &details) {
    m_details = details;
    m_details_isSet = true;
}

bool OAIAutoScaleRunError::is_details_Set() const{
    return m_details_isSet;
}

bool OAIAutoScaleRunError::is_details_Valid() const{
    return m_details_isValid;
}

QString OAIAutoScaleRunError::getMessage() const {
    return m_message;
}
void OAIAutoScaleRunError::setMessage(const QString &message) {
    m_message = message;
    m_message_isSet = true;
}

bool OAIAutoScaleRunError::is_message_Set() const{
    return m_message_isSet;
}

bool OAIAutoScaleRunError::is_message_Valid() const{
    return m_message_isValid;
}

bool OAIAutoScaleRunError::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_details.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_message_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAutoScaleRunError::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_code_isValid && m_message_isValid && true;
}

} // namespace OpenAPI
