/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAICreateOrganizationInventoryOnboardingCloudMonitoringImport_201_response_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICreateOrganizationInventoryOnboardingCloudMonitoringImport_201_response_inner::OAICreateOrganizationInventoryOnboardingCloudMonitoringImport_201_response_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICreateOrganizationInventoryOnboardingCloudMonitoringImport_201_response_inner::OAICreateOrganizationInventoryOnboardingCloudMonitoringImport_201_response_inner() {
    this->initializeModel();
}

OAICreateOrganizationInventoryOnboardingCloudMonitoringImport_201_response_inner::~OAICreateOrganizationInventoryOnboardingCloudMonitoringImport_201_response_inner() {}

void OAICreateOrganizationInventoryOnboardingCloudMonitoringImport_201_response_inner::initializeModel() {

    m_import_id_isSet = false;
    m_import_id_isValid = false;

    m_message_isSet = false;
    m_message_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;
}

void OAICreateOrganizationInventoryOnboardingCloudMonitoringImport_201_response_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICreateOrganizationInventoryOnboardingCloudMonitoringImport_201_response_inner::fromJsonObject(QJsonObject json) {

    m_import_id_isValid = ::OpenAPI::fromJsonValue(m_import_id, json[QString("importId")]);
    m_import_id_isSet = !json[QString("importId")].isNull() && m_import_id_isValid;

    m_message_isValid = ::OpenAPI::fromJsonValue(m_message, json[QString("message")]);
    m_message_isSet = !json[QString("message")].isNull() && m_message_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;
}

QString OAICreateOrganizationInventoryOnboardingCloudMonitoringImport_201_response_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICreateOrganizationInventoryOnboardingCloudMonitoringImport_201_response_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_import_id_isSet) {
        obj.insert(QString("importId"), ::OpenAPI::toJsonValue(m_import_id));
    }
    if (m_message_isSet) {
        obj.insert(QString("message"), ::OpenAPI::toJsonValue(m_message));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    return obj;
}

QString OAICreateOrganizationInventoryOnboardingCloudMonitoringImport_201_response_inner::getImportId() const {
    return m_import_id;
}
void OAICreateOrganizationInventoryOnboardingCloudMonitoringImport_201_response_inner::setImportId(const QString &import_id) {
    m_import_id = import_id;
    m_import_id_isSet = true;
}

bool OAICreateOrganizationInventoryOnboardingCloudMonitoringImport_201_response_inner::is_import_id_Set() const{
    return m_import_id_isSet;
}

bool OAICreateOrganizationInventoryOnboardingCloudMonitoringImport_201_response_inner::is_import_id_Valid() const{
    return m_import_id_isValid;
}

QString OAICreateOrganizationInventoryOnboardingCloudMonitoringImport_201_response_inner::getMessage() const {
    return m_message;
}
void OAICreateOrganizationInventoryOnboardingCloudMonitoringImport_201_response_inner::setMessage(const QString &message) {
    m_message = message;
    m_message_isSet = true;
}

bool OAICreateOrganizationInventoryOnboardingCloudMonitoringImport_201_response_inner::is_message_Set() const{
    return m_message_isSet;
}

bool OAICreateOrganizationInventoryOnboardingCloudMonitoringImport_201_response_inner::is_message_Valid() const{
    return m_message_isValid;
}

QString OAICreateOrganizationInventoryOnboardingCloudMonitoringImport_201_response_inner::getStatus() const {
    return m_status;
}
void OAICreateOrganizationInventoryOnboardingCloudMonitoringImport_201_response_inner::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAICreateOrganizationInventoryOnboardingCloudMonitoringImport_201_response_inner::is_status_Set() const{
    return m_status_isSet;
}

bool OAICreateOrganizationInventoryOnboardingCloudMonitoringImport_201_response_inner::is_status_Valid() const{
    return m_status_isValid;
}

bool OAICreateOrganizationInventoryOnboardingCloudMonitoringImport_201_response_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_import_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_message_isSet) {
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

bool OAICreateOrganizationInventoryOnboardingCloudMonitoringImport_201_response_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
