/**
 * Microcks API v1.7
 * API offered by Microcks, the Kubernetes native tools for API and microservices mocking and testing (microcks.io)
 *
 * The version of the OpenAPI document: 1.7.0
 * Contact: laurent@microcks.io
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIResponse.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIResponse::OAIResponse(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIResponse::OAIResponse() {
    this->initializeModel();
}

OAIResponse::~OAIResponse() {}

void OAIResponse::initializeModel() {

    m_content_isSet = false;
    m_content_isValid = false;

    m_headers_isSet = false;
    m_headers_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_operation_id_isSet = false;
    m_operation_id_isValid = false;

    m_test_case_id_isSet = false;
    m_test_case_id_isValid = false;
}

void OAIResponse::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIResponse::fromJsonObject(QJsonObject json) {

    m_content_isValid = ::OpenAPI::fromJsonValue(m_content, json[QString("content")]);
    m_content_isSet = !json[QString("content")].isNull() && m_content_isValid;

    m_headers_isValid = ::OpenAPI::fromJsonValue(m_headers, json[QString("headers")]);
    m_headers_isSet = !json[QString("headers")].isNull() && m_headers_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_operation_id_isValid = ::OpenAPI::fromJsonValue(m_operation_id, json[QString("operationId")]);
    m_operation_id_isSet = !json[QString("operationId")].isNull() && m_operation_id_isValid;

    m_test_case_id_isValid = ::OpenAPI::fromJsonValue(m_test_case_id, json[QString("testCaseId")]);
    m_test_case_id_isSet = !json[QString("testCaseId")].isNull() && m_test_case_id_isValid;
}

QString OAIResponse::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIResponse::asJsonObject() const {
    QJsonObject obj;
    if (m_content_isSet) {
        obj.insert(QString("content"), ::OpenAPI::toJsonValue(m_content));
    }
    if (m_headers.size() > 0) {
        obj.insert(QString("headers"), ::OpenAPI::toJsonValue(m_headers));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_operation_id_isSet) {
        obj.insert(QString("operationId"), ::OpenAPI::toJsonValue(m_operation_id));
    }
    if (m_test_case_id_isSet) {
        obj.insert(QString("testCaseId"), ::OpenAPI::toJsonValue(m_test_case_id));
    }
    return obj;
}

QString OAIResponse::getContent() const {
    return m_content;
}
void OAIResponse::setContent(const QString &content) {
    m_content = content;
    m_content_isSet = true;
}

bool OAIResponse::is_content_Set() const{
    return m_content_isSet;
}

bool OAIResponse::is_content_Valid() const{
    return m_content_isValid;
}

QList<OAIHeader> OAIResponse::getHeaders() const {
    return m_headers;
}
void OAIResponse::setHeaders(const QList<OAIHeader> &headers) {
    m_headers = headers;
    m_headers_isSet = true;
}

bool OAIResponse::is_headers_Set() const{
    return m_headers_isSet;
}

bool OAIResponse::is_headers_Valid() const{
    return m_headers_isValid;
}

QString OAIResponse::getId() const {
    return m_id;
}
void OAIResponse::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIResponse::is_id_Set() const{
    return m_id_isSet;
}

bool OAIResponse::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIResponse::getName() const {
    return m_name;
}
void OAIResponse::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIResponse::is_name_Set() const{
    return m_name_isSet;
}

bool OAIResponse::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIResponse::getOperationId() const {
    return m_operation_id;
}
void OAIResponse::setOperationId(const QString &operation_id) {
    m_operation_id = operation_id;
    m_operation_id_isSet = true;
}

bool OAIResponse::is_operation_id_Set() const{
    return m_operation_id_isSet;
}

bool OAIResponse::is_operation_id_Valid() const{
    return m_operation_id_isValid;
}

QString OAIResponse::getTestCaseId() const {
    return m_test_case_id;
}
void OAIResponse::setTestCaseId(const QString &test_case_id) {
    m_test_case_id = test_case_id;
    m_test_case_id_isSet = true;
}

bool OAIResponse::is_test_case_id_Set() const{
    return m_test_case_id_isSet;
}

bool OAIResponse::is_test_case_id_Valid() const{
    return m_test_case_id_isValid;
}

bool OAIResponse::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_content_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_headers.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_operation_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_test_case_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIResponse::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_name_isValid && m_operation_id_isValid && true;
}

} // namespace OpenAPI
