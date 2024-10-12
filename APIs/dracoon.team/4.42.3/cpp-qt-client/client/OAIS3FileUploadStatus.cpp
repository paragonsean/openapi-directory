/**
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIS3FileUploadStatus.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIS3FileUploadStatus::OAIS3FileUploadStatus(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIS3FileUploadStatus::OAIS3FileUploadStatus() {
    this->initializeModel();
}

OAIS3FileUploadStatus::~OAIS3FileUploadStatus() {}

void OAIS3FileUploadStatus::initializeModel() {

    m_error_details_isSet = false;
    m_error_details_isValid = false;

    m_node_isSet = false;
    m_node_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;
}

void OAIS3FileUploadStatus::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIS3FileUploadStatus::fromJsonObject(QJsonObject json) {

    m_error_details_isValid = ::OpenAPI::fromJsonValue(m_error_details, json[QString("errorDetails")]);
    m_error_details_isSet = !json[QString("errorDetails")].isNull() && m_error_details_isValid;

    m_node_isValid = ::OpenAPI::fromJsonValue(m_node, json[QString("node")]);
    m_node_isSet = !json[QString("node")].isNull() && m_node_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;
}

QString OAIS3FileUploadStatus::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIS3FileUploadStatus::asJsonObject() const {
    QJsonObject obj;
    if (m_error_details.isSet()) {
        obj.insert(QString("errorDetails"), ::OpenAPI::toJsonValue(m_error_details));
    }
    if (m_node.isSet()) {
        obj.insert(QString("node"), ::OpenAPI::toJsonValue(m_node));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    return obj;
}

OAIErrorResponse OAIS3FileUploadStatus::getErrorDetails() const {
    return m_error_details;
}
void OAIS3FileUploadStatus::setErrorDetails(const OAIErrorResponse &error_details) {
    m_error_details = error_details;
    m_error_details_isSet = true;
}

bool OAIS3FileUploadStatus::is_error_details_Set() const{
    return m_error_details_isSet;
}

bool OAIS3FileUploadStatus::is_error_details_Valid() const{
    return m_error_details_isValid;
}

OAINode OAIS3FileUploadStatus::getNode() const {
    return m_node;
}
void OAIS3FileUploadStatus::setNode(const OAINode &node) {
    m_node = node;
    m_node_isSet = true;
}

bool OAIS3FileUploadStatus::is_node_Set() const{
    return m_node_isSet;
}

bool OAIS3FileUploadStatus::is_node_Valid() const{
    return m_node_isValid;
}

QString OAIS3FileUploadStatus::getStatus() const {
    return m_status;
}
void OAIS3FileUploadStatus::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIS3FileUploadStatus::is_status_Set() const{
    return m_status_isSet;
}

bool OAIS3FileUploadStatus::is_status_Valid() const{
    return m_status_isValid;
}

bool OAIS3FileUploadStatus::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_error_details.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_node.isSet()) {
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

bool OAIS3FileUploadStatus::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_status_isValid && true;
}

} // namespace OpenAPI
