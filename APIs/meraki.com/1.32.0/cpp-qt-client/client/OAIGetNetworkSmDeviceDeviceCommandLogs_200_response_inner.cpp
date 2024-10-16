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

#include "OAIGetNetworkSmDeviceDeviceCommandLogs_200_response_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetNetworkSmDeviceDeviceCommandLogs_200_response_inner::OAIGetNetworkSmDeviceDeviceCommandLogs_200_response_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetNetworkSmDeviceDeviceCommandLogs_200_response_inner::OAIGetNetworkSmDeviceDeviceCommandLogs_200_response_inner() {
    this->initializeModel();
}

OAIGetNetworkSmDeviceDeviceCommandLogs_200_response_inner::~OAIGetNetworkSmDeviceDeviceCommandLogs_200_response_inner() {}

void OAIGetNetworkSmDeviceDeviceCommandLogs_200_response_inner::initializeModel() {

    m_action_isSet = false;
    m_action_isValid = false;

    m_dashboard_user_isSet = false;
    m_dashboard_user_isValid = false;

    m_details_isSet = false;
    m_details_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_ts_isSet = false;
    m_ts_isValid = false;
}

void OAIGetNetworkSmDeviceDeviceCommandLogs_200_response_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetNetworkSmDeviceDeviceCommandLogs_200_response_inner::fromJsonObject(QJsonObject json) {

    m_action_isValid = ::OpenAPI::fromJsonValue(m_action, json[QString("action")]);
    m_action_isSet = !json[QString("action")].isNull() && m_action_isValid;

    m_dashboard_user_isValid = ::OpenAPI::fromJsonValue(m_dashboard_user, json[QString("dashboardUser")]);
    m_dashboard_user_isSet = !json[QString("dashboardUser")].isNull() && m_dashboard_user_isValid;

    m_details_isValid = ::OpenAPI::fromJsonValue(m_details, json[QString("details")]);
    m_details_isSet = !json[QString("details")].isNull() && m_details_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_ts_isValid = ::OpenAPI::fromJsonValue(m_ts, json[QString("ts")]);
    m_ts_isSet = !json[QString("ts")].isNull() && m_ts_isValid;
}

QString OAIGetNetworkSmDeviceDeviceCommandLogs_200_response_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetNetworkSmDeviceDeviceCommandLogs_200_response_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_action_isSet) {
        obj.insert(QString("action"), ::OpenAPI::toJsonValue(m_action));
    }
    if (m_dashboard_user_isSet) {
        obj.insert(QString("dashboardUser"), ::OpenAPI::toJsonValue(m_dashboard_user));
    }
    if (m_details_isSet) {
        obj.insert(QString("details"), ::OpenAPI::toJsonValue(m_details));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_ts_isSet) {
        obj.insert(QString("ts"), ::OpenAPI::toJsonValue(m_ts));
    }
    return obj;
}

QString OAIGetNetworkSmDeviceDeviceCommandLogs_200_response_inner::getAction() const {
    return m_action;
}
void OAIGetNetworkSmDeviceDeviceCommandLogs_200_response_inner::setAction(const QString &action) {
    m_action = action;
    m_action_isSet = true;
}

bool OAIGetNetworkSmDeviceDeviceCommandLogs_200_response_inner::is_action_Set() const{
    return m_action_isSet;
}

bool OAIGetNetworkSmDeviceDeviceCommandLogs_200_response_inner::is_action_Valid() const{
    return m_action_isValid;
}

QString OAIGetNetworkSmDeviceDeviceCommandLogs_200_response_inner::getDashboardUser() const {
    return m_dashboard_user;
}
void OAIGetNetworkSmDeviceDeviceCommandLogs_200_response_inner::setDashboardUser(const QString &dashboard_user) {
    m_dashboard_user = dashboard_user;
    m_dashboard_user_isSet = true;
}

bool OAIGetNetworkSmDeviceDeviceCommandLogs_200_response_inner::is_dashboard_user_Set() const{
    return m_dashboard_user_isSet;
}

bool OAIGetNetworkSmDeviceDeviceCommandLogs_200_response_inner::is_dashboard_user_Valid() const{
    return m_dashboard_user_isValid;
}

QString OAIGetNetworkSmDeviceDeviceCommandLogs_200_response_inner::getDetails() const {
    return m_details;
}
void OAIGetNetworkSmDeviceDeviceCommandLogs_200_response_inner::setDetails(const QString &details) {
    m_details = details;
    m_details_isSet = true;
}

bool OAIGetNetworkSmDeviceDeviceCommandLogs_200_response_inner::is_details_Set() const{
    return m_details_isSet;
}

bool OAIGetNetworkSmDeviceDeviceCommandLogs_200_response_inner::is_details_Valid() const{
    return m_details_isValid;
}

QString OAIGetNetworkSmDeviceDeviceCommandLogs_200_response_inner::getName() const {
    return m_name;
}
void OAIGetNetworkSmDeviceDeviceCommandLogs_200_response_inner::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIGetNetworkSmDeviceDeviceCommandLogs_200_response_inner::is_name_Set() const{
    return m_name_isSet;
}

bool OAIGetNetworkSmDeviceDeviceCommandLogs_200_response_inner::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIGetNetworkSmDeviceDeviceCommandLogs_200_response_inner::getTs() const {
    return m_ts;
}
void OAIGetNetworkSmDeviceDeviceCommandLogs_200_response_inner::setTs(const QString &ts) {
    m_ts = ts;
    m_ts_isSet = true;
}

bool OAIGetNetworkSmDeviceDeviceCommandLogs_200_response_inner::is_ts_Set() const{
    return m_ts_isSet;
}

bool OAIGetNetworkSmDeviceDeviceCommandLogs_200_response_inner::is_ts_Valid() const{
    return m_ts_isValid;
}

bool OAIGetNetworkSmDeviceDeviceCommandLogs_200_response_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_action_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_dashboard_user_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_details_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ts_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGetNetworkSmDeviceDeviceCommandLogs_200_response_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
