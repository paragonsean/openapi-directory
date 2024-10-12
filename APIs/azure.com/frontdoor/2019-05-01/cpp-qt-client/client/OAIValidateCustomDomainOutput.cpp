/**
 * FrontDoorManagementClient
 * Use these APIs to manage Azure Front Door resources through the Azure Resource Manager. You must make sure that requests made to these resources are secure.
 *
 * The version of the OpenAPI document: 2019-05-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIValidateCustomDomainOutput.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIValidateCustomDomainOutput::OAIValidateCustomDomainOutput(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIValidateCustomDomainOutput::OAIValidateCustomDomainOutput() {
    this->initializeModel();
}

OAIValidateCustomDomainOutput::~OAIValidateCustomDomainOutput() {}

void OAIValidateCustomDomainOutput::initializeModel() {

    m_custom_domain_validated_isSet = false;
    m_custom_domain_validated_isValid = false;

    m_message_isSet = false;
    m_message_isValid = false;

    m_reason_isSet = false;
    m_reason_isValid = false;
}

void OAIValidateCustomDomainOutput::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIValidateCustomDomainOutput::fromJsonObject(QJsonObject json) {

    m_custom_domain_validated_isValid = ::OpenAPI::fromJsonValue(m_custom_domain_validated, json[QString("customDomainValidated")]);
    m_custom_domain_validated_isSet = !json[QString("customDomainValidated")].isNull() && m_custom_domain_validated_isValid;

    m_message_isValid = ::OpenAPI::fromJsonValue(m_message, json[QString("message")]);
    m_message_isSet = !json[QString("message")].isNull() && m_message_isValid;

    m_reason_isValid = ::OpenAPI::fromJsonValue(m_reason, json[QString("reason")]);
    m_reason_isSet = !json[QString("reason")].isNull() && m_reason_isValid;
}

QString OAIValidateCustomDomainOutput::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIValidateCustomDomainOutput::asJsonObject() const {
    QJsonObject obj;
    if (m_custom_domain_validated_isSet) {
        obj.insert(QString("customDomainValidated"), ::OpenAPI::toJsonValue(m_custom_domain_validated));
    }
    if (m_message_isSet) {
        obj.insert(QString("message"), ::OpenAPI::toJsonValue(m_message));
    }
    if (m_reason_isSet) {
        obj.insert(QString("reason"), ::OpenAPI::toJsonValue(m_reason));
    }
    return obj;
}

bool OAIValidateCustomDomainOutput::isCustomDomainValidated() const {
    return m_custom_domain_validated;
}
void OAIValidateCustomDomainOutput::setCustomDomainValidated(const bool &custom_domain_validated) {
    m_custom_domain_validated = custom_domain_validated;
    m_custom_domain_validated_isSet = true;
}

bool OAIValidateCustomDomainOutput::is_custom_domain_validated_Set() const{
    return m_custom_domain_validated_isSet;
}

bool OAIValidateCustomDomainOutput::is_custom_domain_validated_Valid() const{
    return m_custom_domain_validated_isValid;
}

QString OAIValidateCustomDomainOutput::getMessage() const {
    return m_message;
}
void OAIValidateCustomDomainOutput::setMessage(const QString &message) {
    m_message = message;
    m_message_isSet = true;
}

bool OAIValidateCustomDomainOutput::is_message_Set() const{
    return m_message_isSet;
}

bool OAIValidateCustomDomainOutput::is_message_Valid() const{
    return m_message_isValid;
}

QString OAIValidateCustomDomainOutput::getReason() const {
    return m_reason;
}
void OAIValidateCustomDomainOutput::setReason(const QString &reason) {
    m_reason = reason;
    m_reason_isSet = true;
}

bool OAIValidateCustomDomainOutput::is_reason_Set() const{
    return m_reason_isSet;
}

bool OAIValidateCustomDomainOutput::is_reason_Valid() const{
    return m_reason_isValid;
}

bool OAIValidateCustomDomainOutput::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_custom_domain_validated_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_message_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_reason_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIValidateCustomDomainOutput::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
