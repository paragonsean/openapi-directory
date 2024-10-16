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

#include "OAIGetOrganizationDevicesStatusesOverview_200_response_counts.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetOrganizationDevicesStatusesOverview_200_response_counts::OAIGetOrganizationDevicesStatusesOverview_200_response_counts(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetOrganizationDevicesStatusesOverview_200_response_counts::OAIGetOrganizationDevicesStatusesOverview_200_response_counts() {
    this->initializeModel();
}

OAIGetOrganizationDevicesStatusesOverview_200_response_counts::~OAIGetOrganizationDevicesStatusesOverview_200_response_counts() {}

void OAIGetOrganizationDevicesStatusesOverview_200_response_counts::initializeModel() {

    m_by_status_isSet = false;
    m_by_status_isValid = false;
}

void OAIGetOrganizationDevicesStatusesOverview_200_response_counts::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetOrganizationDevicesStatusesOverview_200_response_counts::fromJsonObject(QJsonObject json) {

    m_by_status_isValid = ::OpenAPI::fromJsonValue(m_by_status, json[QString("byStatus")]);
    m_by_status_isSet = !json[QString("byStatus")].isNull() && m_by_status_isValid;
}

QString OAIGetOrganizationDevicesStatusesOverview_200_response_counts::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetOrganizationDevicesStatusesOverview_200_response_counts::asJsonObject() const {
    QJsonObject obj;
    if (m_by_status.isSet()) {
        obj.insert(QString("byStatus"), ::OpenAPI::toJsonValue(m_by_status));
    }
    return obj;
}

OAIGetOrganizationDevicesStatusesOverview_200_response_counts_byStatus OAIGetOrganizationDevicesStatusesOverview_200_response_counts::getByStatus() const {
    return m_by_status;
}
void OAIGetOrganizationDevicesStatusesOverview_200_response_counts::setByStatus(const OAIGetOrganizationDevicesStatusesOverview_200_response_counts_byStatus &by_status) {
    m_by_status = by_status;
    m_by_status_isSet = true;
}

bool OAIGetOrganizationDevicesStatusesOverview_200_response_counts::is_by_status_Set() const{
    return m_by_status_isSet;
}

bool OAIGetOrganizationDevicesStatusesOverview_200_response_counts::is_by_status_Valid() const{
    return m_by_status_isValid;
}

bool OAIGetOrganizationDevicesStatusesOverview_200_response_counts::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_by_status.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGetOrganizationDevicesStatusesOverview_200_response_counts::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
