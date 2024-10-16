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

#include "OAIGetOrganizationSummaryTopAppliancesByUtilization_200_response_inner_utilization_average.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetOrganizationSummaryTopAppliancesByUtilization_200_response_inner_utilization_average::OAIGetOrganizationSummaryTopAppliancesByUtilization_200_response_inner_utilization_average(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetOrganizationSummaryTopAppliancesByUtilization_200_response_inner_utilization_average::OAIGetOrganizationSummaryTopAppliancesByUtilization_200_response_inner_utilization_average() {
    this->initializeModel();
}

OAIGetOrganizationSummaryTopAppliancesByUtilization_200_response_inner_utilization_average::~OAIGetOrganizationSummaryTopAppliancesByUtilization_200_response_inner_utilization_average() {}

void OAIGetOrganizationSummaryTopAppliancesByUtilization_200_response_inner_utilization_average::initializeModel() {

    m_percentage_isSet = false;
    m_percentage_isValid = false;
}

void OAIGetOrganizationSummaryTopAppliancesByUtilization_200_response_inner_utilization_average::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetOrganizationSummaryTopAppliancesByUtilization_200_response_inner_utilization_average::fromJsonObject(QJsonObject json) {

    m_percentage_isValid = ::OpenAPI::fromJsonValue(m_percentage, json[QString("percentage")]);
    m_percentage_isSet = !json[QString("percentage")].isNull() && m_percentage_isValid;
}

QString OAIGetOrganizationSummaryTopAppliancesByUtilization_200_response_inner_utilization_average::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetOrganizationSummaryTopAppliancesByUtilization_200_response_inner_utilization_average::asJsonObject() const {
    QJsonObject obj;
    if (m_percentage_isSet) {
        obj.insert(QString("percentage"), ::OpenAPI::toJsonValue(m_percentage));
    }
    return obj;
}

float OAIGetOrganizationSummaryTopAppliancesByUtilization_200_response_inner_utilization_average::getPercentage() const {
    return m_percentage;
}
void OAIGetOrganizationSummaryTopAppliancesByUtilization_200_response_inner_utilization_average::setPercentage(const float &percentage) {
    m_percentage = percentage;
    m_percentage_isSet = true;
}

bool OAIGetOrganizationSummaryTopAppliancesByUtilization_200_response_inner_utilization_average::is_percentage_Set() const{
    return m_percentage_isSet;
}

bool OAIGetOrganizationSummaryTopAppliancesByUtilization_200_response_inner_utilization_average::is_percentage_Valid() const{
    return m_percentage_isValid;
}

bool OAIGetOrganizationSummaryTopAppliancesByUtilization_200_response_inner_utilization_average::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_percentage_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGetOrganizationSummaryTopAppliancesByUtilization_200_response_inner_utilization_average::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
