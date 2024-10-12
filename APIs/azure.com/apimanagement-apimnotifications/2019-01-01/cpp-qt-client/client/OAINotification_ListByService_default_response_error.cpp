/**
 * ApiManagementClient
 * Use these REST APIs for performing operations on who is going to receive notifications associated with your Azure API Management deployment.
 *
 * The version of the OpenAPI document: 2019-01-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAINotification_ListByService_default_response_error.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAINotification_ListByService_default_response_error::OAINotification_ListByService_default_response_error(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAINotification_ListByService_default_response_error::OAINotification_ListByService_default_response_error() {
    this->initializeModel();
}

OAINotification_ListByService_default_response_error::~OAINotification_ListByService_default_response_error() {}

void OAINotification_ListByService_default_response_error::initializeModel() {

    m_code_isSet = false;
    m_code_isValid = false;

    m_details_isSet = false;
    m_details_isValid = false;

    m_message_isSet = false;
    m_message_isValid = false;
}

void OAINotification_ListByService_default_response_error::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAINotification_ListByService_default_response_error::fromJsonObject(QJsonObject json) {

    m_code_isValid = ::OpenAPI::fromJsonValue(m_code, json[QString("code")]);
    m_code_isSet = !json[QString("code")].isNull() && m_code_isValid;

    m_details_isValid = ::OpenAPI::fromJsonValue(m_details, json[QString("details")]);
    m_details_isSet = !json[QString("details")].isNull() && m_details_isValid;

    m_message_isValid = ::OpenAPI::fromJsonValue(m_message, json[QString("message")]);
    m_message_isSet = !json[QString("message")].isNull() && m_message_isValid;
}

QString OAINotification_ListByService_default_response_error::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAINotification_ListByService_default_response_error::asJsonObject() const {
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

QString OAINotification_ListByService_default_response_error::getCode() const {
    return m_code;
}
void OAINotification_ListByService_default_response_error::setCode(const QString &code) {
    m_code = code;
    m_code_isSet = true;
}

bool OAINotification_ListByService_default_response_error::is_code_Set() const{
    return m_code_isSet;
}

bool OAINotification_ListByService_default_response_error::is_code_Valid() const{
    return m_code_isValid;
}

QList<OAINotification_ListByService_default_response_error_details_inner> OAINotification_ListByService_default_response_error::getDetails() const {
    return m_details;
}
void OAINotification_ListByService_default_response_error::setDetails(const QList<OAINotification_ListByService_default_response_error_details_inner> &details) {
    m_details = details;
    m_details_isSet = true;
}

bool OAINotification_ListByService_default_response_error::is_details_Set() const{
    return m_details_isSet;
}

bool OAINotification_ListByService_default_response_error::is_details_Valid() const{
    return m_details_isValid;
}

QString OAINotification_ListByService_default_response_error::getMessage() const {
    return m_message;
}
void OAINotification_ListByService_default_response_error::setMessage(const QString &message) {
    m_message = message;
    m_message_isSet = true;
}

bool OAINotification_ListByService_default_response_error::is_message_Set() const{
    return m_message_isSet;
}

bool OAINotification_ListByService_default_response_error::is_message_Valid() const{
    return m_message_isValid;
}

bool OAINotification_ListByService_default_response_error::isSet() const {
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

bool OAINotification_ListByService_default_response_error::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
