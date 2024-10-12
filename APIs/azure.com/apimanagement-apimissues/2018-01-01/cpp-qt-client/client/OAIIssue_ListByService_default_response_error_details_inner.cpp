/**
 * ApiManagementClient
 * Use this REST API to get all the issues across an Azure Api Management service.
 *
 * The version of the OpenAPI document: 2018-01-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIIssue_ListByService_default_response_error_details_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIIssue_ListByService_default_response_error_details_inner::OAIIssue_ListByService_default_response_error_details_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIIssue_ListByService_default_response_error_details_inner::OAIIssue_ListByService_default_response_error_details_inner() {
    this->initializeModel();
}

OAIIssue_ListByService_default_response_error_details_inner::~OAIIssue_ListByService_default_response_error_details_inner() {}

void OAIIssue_ListByService_default_response_error_details_inner::initializeModel() {

    m_code_isSet = false;
    m_code_isValid = false;

    m_message_isSet = false;
    m_message_isValid = false;

    m_target_isSet = false;
    m_target_isValid = false;
}

void OAIIssue_ListByService_default_response_error_details_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIIssue_ListByService_default_response_error_details_inner::fromJsonObject(QJsonObject json) {

    m_code_isValid = ::OpenAPI::fromJsonValue(m_code, json[QString("code")]);
    m_code_isSet = !json[QString("code")].isNull() && m_code_isValid;

    m_message_isValid = ::OpenAPI::fromJsonValue(m_message, json[QString("message")]);
    m_message_isSet = !json[QString("message")].isNull() && m_message_isValid;

    m_target_isValid = ::OpenAPI::fromJsonValue(m_target, json[QString("target")]);
    m_target_isSet = !json[QString("target")].isNull() && m_target_isValid;
}

QString OAIIssue_ListByService_default_response_error_details_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIIssue_ListByService_default_response_error_details_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_code_isSet) {
        obj.insert(QString("code"), ::OpenAPI::toJsonValue(m_code));
    }
    if (m_message_isSet) {
        obj.insert(QString("message"), ::OpenAPI::toJsonValue(m_message));
    }
    if (m_target_isSet) {
        obj.insert(QString("target"), ::OpenAPI::toJsonValue(m_target));
    }
    return obj;
}

QString OAIIssue_ListByService_default_response_error_details_inner::getCode() const {
    return m_code;
}
void OAIIssue_ListByService_default_response_error_details_inner::setCode(const QString &code) {
    m_code = code;
    m_code_isSet = true;
}

bool OAIIssue_ListByService_default_response_error_details_inner::is_code_Set() const{
    return m_code_isSet;
}

bool OAIIssue_ListByService_default_response_error_details_inner::is_code_Valid() const{
    return m_code_isValid;
}

QString OAIIssue_ListByService_default_response_error_details_inner::getMessage() const {
    return m_message;
}
void OAIIssue_ListByService_default_response_error_details_inner::setMessage(const QString &message) {
    m_message = message;
    m_message_isSet = true;
}

bool OAIIssue_ListByService_default_response_error_details_inner::is_message_Set() const{
    return m_message_isSet;
}

bool OAIIssue_ListByService_default_response_error_details_inner::is_message_Valid() const{
    return m_message_isValid;
}

QString OAIIssue_ListByService_default_response_error_details_inner::getTarget() const {
    return m_target;
}
void OAIIssue_ListByService_default_response_error_details_inner::setTarget(const QString &target) {
    m_target = target;
    m_target_isSet = true;
}

bool OAIIssue_ListByService_default_response_error_details_inner::is_target_Set() const{
    return m_target_isSet;
}

bool OAIIssue_ListByService_default_response_error_details_inner::is_target_Valid() const{
    return m_target_isValid;
}

bool OAIIssue_ListByService_default_response_error_details_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_message_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_target_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIIssue_ListByService_default_response_error_details_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
