/**
 * Contribly
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIErrorResponse.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIErrorResponse::OAIErrorResponse(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIErrorResponse::OAIErrorResponse() {
    this->initializeModel();
}

OAIErrorResponse::~OAIErrorResponse() {}

void OAIErrorResponse::initializeModel() {

    m_fields_isSet = false;
    m_fields_isValid = false;

    m_message_isSet = false;
    m_message_isValid = false;
}

void OAIErrorResponse::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIErrorResponse::fromJsonObject(QJsonObject json) {

    m_fields_isValid = ::OpenAPI::fromJsonValue(m_fields, json[QString("fields")]);
    m_fields_isSet = !json[QString("fields")].isNull() && m_fields_isValid;

    m_message_isValid = ::OpenAPI::fromJsonValue(m_message, json[QString("message")]);
    m_message_isSet = !json[QString("message")].isNull() && m_message_isValid;
}

QString OAIErrorResponse::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIErrorResponse::asJsonObject() const {
    QJsonObject obj;
    if (m_fields.size() > 0) {
        obj.insert(QString("fields"), ::OpenAPI::toJsonValue(m_fields));
    }
    if (m_message_isSet) {
        obj.insert(QString("message"), ::OpenAPI::toJsonValue(m_message));
    }
    return obj;
}

QList<OAIErrorField> OAIErrorResponse::getFields() const {
    return m_fields;
}
void OAIErrorResponse::setFields(const QList<OAIErrorField> &fields) {
    m_fields = fields;
    m_fields_isSet = true;
}

bool OAIErrorResponse::is_fields_Set() const{
    return m_fields_isSet;
}

bool OAIErrorResponse::is_fields_Valid() const{
    return m_fields_isValid;
}

QString OAIErrorResponse::getMessage() const {
    return m_message;
}
void OAIErrorResponse::setMessage(const QString &message) {
    m_message = message;
    m_message_isSet = true;
}

bool OAIErrorResponse::is_message_Set() const{
    return m_message_isSet;
}

bool OAIErrorResponse::is_message_Valid() const{
    return m_message_isValid;
}

bool OAIErrorResponse::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_fields.size() > 0) {
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

bool OAIErrorResponse::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
