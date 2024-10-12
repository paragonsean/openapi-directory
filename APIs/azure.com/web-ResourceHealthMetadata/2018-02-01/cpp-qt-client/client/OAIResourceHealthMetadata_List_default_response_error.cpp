/**
 * ResourceHealthMetadata API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2018-02-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIResourceHealthMetadata_List_default_response_error.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIResourceHealthMetadata_List_default_response_error::OAIResourceHealthMetadata_List_default_response_error(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIResourceHealthMetadata_List_default_response_error::OAIResourceHealthMetadata_List_default_response_error() {
    this->initializeModel();
}

OAIResourceHealthMetadata_List_default_response_error::~OAIResourceHealthMetadata_List_default_response_error() {}

void OAIResourceHealthMetadata_List_default_response_error::initializeModel() {

    m_code_isSet = false;
    m_code_isValid = false;

    m_details_isSet = false;
    m_details_isValid = false;

    m_innererror_isSet = false;
    m_innererror_isValid = false;

    m_message_isSet = false;
    m_message_isValid = false;

    m_target_isSet = false;
    m_target_isValid = false;
}

void OAIResourceHealthMetadata_List_default_response_error::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIResourceHealthMetadata_List_default_response_error::fromJsonObject(QJsonObject json) {

    m_code_isValid = ::OpenAPI::fromJsonValue(m_code, json[QString("code")]);
    m_code_isSet = !json[QString("code")].isNull() && m_code_isValid;

    m_details_isValid = ::OpenAPI::fromJsonValue(m_details, json[QString("details")]);
    m_details_isSet = !json[QString("details")].isNull() && m_details_isValid;

    m_innererror_isValid = ::OpenAPI::fromJsonValue(m_innererror, json[QString("innererror")]);
    m_innererror_isSet = !json[QString("innererror")].isNull() && m_innererror_isValid;

    m_message_isValid = ::OpenAPI::fromJsonValue(m_message, json[QString("message")]);
    m_message_isSet = !json[QString("message")].isNull() && m_message_isValid;

    m_target_isValid = ::OpenAPI::fromJsonValue(m_target, json[QString("target")]);
    m_target_isSet = !json[QString("target")].isNull() && m_target_isValid;
}

QString OAIResourceHealthMetadata_List_default_response_error::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIResourceHealthMetadata_List_default_response_error::asJsonObject() const {
    QJsonObject obj;
    if (m_code_isSet) {
        obj.insert(QString("code"), ::OpenAPI::toJsonValue(m_code));
    }
    if (m_details.size() > 0) {
        obj.insert(QString("details"), ::OpenAPI::toJsonValue(m_details));
    }
    if (m_innererror_isSet) {
        obj.insert(QString("innererror"), ::OpenAPI::toJsonValue(m_innererror));
    }
    if (m_message_isSet) {
        obj.insert(QString("message"), ::OpenAPI::toJsonValue(m_message));
    }
    if (m_target_isSet) {
        obj.insert(QString("target"), ::OpenAPI::toJsonValue(m_target));
    }
    return obj;
}

QString OAIResourceHealthMetadata_List_default_response_error::getCode() const {
    return m_code;
}
void OAIResourceHealthMetadata_List_default_response_error::setCode(const QString &code) {
    m_code = code;
    m_code_isSet = true;
}

bool OAIResourceHealthMetadata_List_default_response_error::is_code_Set() const{
    return m_code_isSet;
}

bool OAIResourceHealthMetadata_List_default_response_error::is_code_Valid() const{
    return m_code_isValid;
}

QList<OAIResourceHealthMetadata_List_default_response_error_details_inner> OAIResourceHealthMetadata_List_default_response_error::getDetails() const {
    return m_details;
}
void OAIResourceHealthMetadata_List_default_response_error::setDetails(const QList<OAIResourceHealthMetadata_List_default_response_error_details_inner> &details) {
    m_details = details;
    m_details_isSet = true;
}

bool OAIResourceHealthMetadata_List_default_response_error::is_details_Set() const{
    return m_details_isSet;
}

bool OAIResourceHealthMetadata_List_default_response_error::is_details_Valid() const{
    return m_details_isValid;
}

QString OAIResourceHealthMetadata_List_default_response_error::getInnererror() const {
    return m_innererror;
}
void OAIResourceHealthMetadata_List_default_response_error::setInnererror(const QString &innererror) {
    m_innererror = innererror;
    m_innererror_isSet = true;
}

bool OAIResourceHealthMetadata_List_default_response_error::is_innererror_Set() const{
    return m_innererror_isSet;
}

bool OAIResourceHealthMetadata_List_default_response_error::is_innererror_Valid() const{
    return m_innererror_isValid;
}

QString OAIResourceHealthMetadata_List_default_response_error::getMessage() const {
    return m_message;
}
void OAIResourceHealthMetadata_List_default_response_error::setMessage(const QString &message) {
    m_message = message;
    m_message_isSet = true;
}

bool OAIResourceHealthMetadata_List_default_response_error::is_message_Set() const{
    return m_message_isSet;
}

bool OAIResourceHealthMetadata_List_default_response_error::is_message_Valid() const{
    return m_message_isValid;
}

QString OAIResourceHealthMetadata_List_default_response_error::getTarget() const {
    return m_target;
}
void OAIResourceHealthMetadata_List_default_response_error::setTarget(const QString &target) {
    m_target = target;
    m_target_isSet = true;
}

bool OAIResourceHealthMetadata_List_default_response_error::is_target_Set() const{
    return m_target_isSet;
}

bool OAIResourceHealthMetadata_List_default_response_error::is_target_Valid() const{
    return m_target_isValid;
}

bool OAIResourceHealthMetadata_List_default_response_error::isSet() const {
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

        if (m_innererror_isSet) {
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

bool OAIResourceHealthMetadata_List_default_response_error::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
