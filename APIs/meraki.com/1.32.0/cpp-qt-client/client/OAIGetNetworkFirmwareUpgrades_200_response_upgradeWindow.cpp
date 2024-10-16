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

#include "OAIGetNetworkFirmwareUpgrades_200_response_upgradeWindow.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetNetworkFirmwareUpgrades_200_response_upgradeWindow::OAIGetNetworkFirmwareUpgrades_200_response_upgradeWindow(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetNetworkFirmwareUpgrades_200_response_upgradeWindow::OAIGetNetworkFirmwareUpgrades_200_response_upgradeWindow() {
    this->initializeModel();
}

OAIGetNetworkFirmwareUpgrades_200_response_upgradeWindow::~OAIGetNetworkFirmwareUpgrades_200_response_upgradeWindow() {}

void OAIGetNetworkFirmwareUpgrades_200_response_upgradeWindow::initializeModel() {

    m_day_of_week_isSet = false;
    m_day_of_week_isValid = false;

    m_hour_of_day_isSet = false;
    m_hour_of_day_isValid = false;
}

void OAIGetNetworkFirmwareUpgrades_200_response_upgradeWindow::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetNetworkFirmwareUpgrades_200_response_upgradeWindow::fromJsonObject(QJsonObject json) {

    m_day_of_week_isValid = ::OpenAPI::fromJsonValue(m_day_of_week, json[QString("dayOfWeek")]);
    m_day_of_week_isSet = !json[QString("dayOfWeek")].isNull() && m_day_of_week_isValid;

    m_hour_of_day_isValid = ::OpenAPI::fromJsonValue(m_hour_of_day, json[QString("hourOfDay")]);
    m_hour_of_day_isSet = !json[QString("hourOfDay")].isNull() && m_hour_of_day_isValid;
}

QString OAIGetNetworkFirmwareUpgrades_200_response_upgradeWindow::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetNetworkFirmwareUpgrades_200_response_upgradeWindow::asJsonObject() const {
    QJsonObject obj;
    if (m_day_of_week_isSet) {
        obj.insert(QString("dayOfWeek"), ::OpenAPI::toJsonValue(m_day_of_week));
    }
    if (m_hour_of_day_isSet) {
        obj.insert(QString("hourOfDay"), ::OpenAPI::toJsonValue(m_hour_of_day));
    }
    return obj;
}

QString OAIGetNetworkFirmwareUpgrades_200_response_upgradeWindow::getDayOfWeek() const {
    return m_day_of_week;
}
void OAIGetNetworkFirmwareUpgrades_200_response_upgradeWindow::setDayOfWeek(const QString &day_of_week) {
    m_day_of_week = day_of_week;
    m_day_of_week_isSet = true;
}

bool OAIGetNetworkFirmwareUpgrades_200_response_upgradeWindow::is_day_of_week_Set() const{
    return m_day_of_week_isSet;
}

bool OAIGetNetworkFirmwareUpgrades_200_response_upgradeWindow::is_day_of_week_Valid() const{
    return m_day_of_week_isValid;
}

QString OAIGetNetworkFirmwareUpgrades_200_response_upgradeWindow::getHourOfDay() const {
    return m_hour_of_day;
}
void OAIGetNetworkFirmwareUpgrades_200_response_upgradeWindow::setHourOfDay(const QString &hour_of_day) {
    m_hour_of_day = hour_of_day;
    m_hour_of_day_isSet = true;
}

bool OAIGetNetworkFirmwareUpgrades_200_response_upgradeWindow::is_hour_of_day_Set() const{
    return m_hour_of_day_isSet;
}

bool OAIGetNetworkFirmwareUpgrades_200_response_upgradeWindow::is_hour_of_day_Valid() const{
    return m_hour_of_day_isValid;
}

bool OAIGetNetworkFirmwareUpgrades_200_response_upgradeWindow::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_day_of_week_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_hour_of_day_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGetNetworkFirmwareUpgrades_200_response_upgradeWindow::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
