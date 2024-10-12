/**
 * ManagedLabsClient
 * The Managed Labs Client.
 *
 * The version of the OpenAPI document: 2018-10-15
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAILatestOperationResult.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAILatestOperationResult::OAILatestOperationResult(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAILatestOperationResult::OAILatestOperationResult() {
    this->initializeModel();
}

OAILatestOperationResult::~OAILatestOperationResult() {}

void OAILatestOperationResult::initializeModel() {

    m_error_code_isSet = false;
    m_error_code_isValid = false;

    m_error_message_isSet = false;
    m_error_message_isValid = false;

    m_http_method_isSet = false;
    m_http_method_isValid = false;

    m_operation_url_isSet = false;
    m_operation_url_isValid = false;

    m_request_uri_isSet = false;
    m_request_uri_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;
}

void OAILatestOperationResult::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAILatestOperationResult::fromJsonObject(QJsonObject json) {

    m_error_code_isValid = ::OpenAPI::fromJsonValue(m_error_code, json[QString("errorCode")]);
    m_error_code_isSet = !json[QString("errorCode")].isNull() && m_error_code_isValid;

    m_error_message_isValid = ::OpenAPI::fromJsonValue(m_error_message, json[QString("errorMessage")]);
    m_error_message_isSet = !json[QString("errorMessage")].isNull() && m_error_message_isValid;

    m_http_method_isValid = ::OpenAPI::fromJsonValue(m_http_method, json[QString("httpMethod")]);
    m_http_method_isSet = !json[QString("httpMethod")].isNull() && m_http_method_isValid;

    m_operation_url_isValid = ::OpenAPI::fromJsonValue(m_operation_url, json[QString("operationUrl")]);
    m_operation_url_isSet = !json[QString("operationUrl")].isNull() && m_operation_url_isValid;

    m_request_uri_isValid = ::OpenAPI::fromJsonValue(m_request_uri, json[QString("requestUri")]);
    m_request_uri_isSet = !json[QString("requestUri")].isNull() && m_request_uri_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;
}

QString OAILatestOperationResult::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAILatestOperationResult::asJsonObject() const {
    QJsonObject obj;
    if (m_error_code_isSet) {
        obj.insert(QString("errorCode"), ::OpenAPI::toJsonValue(m_error_code));
    }
    if (m_error_message_isSet) {
        obj.insert(QString("errorMessage"), ::OpenAPI::toJsonValue(m_error_message));
    }
    if (m_http_method_isSet) {
        obj.insert(QString("httpMethod"), ::OpenAPI::toJsonValue(m_http_method));
    }
    if (m_operation_url_isSet) {
        obj.insert(QString("operationUrl"), ::OpenAPI::toJsonValue(m_operation_url));
    }
    if (m_request_uri_isSet) {
        obj.insert(QString("requestUri"), ::OpenAPI::toJsonValue(m_request_uri));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    return obj;
}

QString OAILatestOperationResult::getErrorCode() const {
    return m_error_code;
}
void OAILatestOperationResult::setErrorCode(const QString &error_code) {
    m_error_code = error_code;
    m_error_code_isSet = true;
}

bool OAILatestOperationResult::is_error_code_Set() const{
    return m_error_code_isSet;
}

bool OAILatestOperationResult::is_error_code_Valid() const{
    return m_error_code_isValid;
}

QString OAILatestOperationResult::getErrorMessage() const {
    return m_error_message;
}
void OAILatestOperationResult::setErrorMessage(const QString &error_message) {
    m_error_message = error_message;
    m_error_message_isSet = true;
}

bool OAILatestOperationResult::is_error_message_Set() const{
    return m_error_message_isSet;
}

bool OAILatestOperationResult::is_error_message_Valid() const{
    return m_error_message_isValid;
}

QString OAILatestOperationResult::getHttpMethod() const {
    return m_http_method;
}
void OAILatestOperationResult::setHttpMethod(const QString &http_method) {
    m_http_method = http_method;
    m_http_method_isSet = true;
}

bool OAILatestOperationResult::is_http_method_Set() const{
    return m_http_method_isSet;
}

bool OAILatestOperationResult::is_http_method_Valid() const{
    return m_http_method_isValid;
}

QString OAILatestOperationResult::getOperationUrl() const {
    return m_operation_url;
}
void OAILatestOperationResult::setOperationUrl(const QString &operation_url) {
    m_operation_url = operation_url;
    m_operation_url_isSet = true;
}

bool OAILatestOperationResult::is_operation_url_Set() const{
    return m_operation_url_isSet;
}

bool OAILatestOperationResult::is_operation_url_Valid() const{
    return m_operation_url_isValid;
}

QString OAILatestOperationResult::getRequestUri() const {
    return m_request_uri;
}
void OAILatestOperationResult::setRequestUri(const QString &request_uri) {
    m_request_uri = request_uri;
    m_request_uri_isSet = true;
}

bool OAILatestOperationResult::is_request_uri_Set() const{
    return m_request_uri_isSet;
}

bool OAILatestOperationResult::is_request_uri_Valid() const{
    return m_request_uri_isValid;
}

QString OAILatestOperationResult::getStatus() const {
    return m_status;
}
void OAILatestOperationResult::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAILatestOperationResult::is_status_Set() const{
    return m_status_isSet;
}

bool OAILatestOperationResult::is_status_Valid() const{
    return m_status_isValid;
}

bool OAILatestOperationResult::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_error_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_error_message_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_http_method_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_operation_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_request_uri_isSet) {
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

bool OAILatestOperationResult::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
