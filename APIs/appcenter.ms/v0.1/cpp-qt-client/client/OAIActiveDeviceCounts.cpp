/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIActiveDeviceCounts.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIActiveDeviceCounts::OAIActiveDeviceCounts(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIActiveDeviceCounts::OAIActiveDeviceCounts() {
    this->initializeModel();
}

OAIActiveDeviceCounts::~OAIActiveDeviceCounts() {}

void OAIActiveDeviceCounts::initializeModel() {

    m_daily_isSet = false;
    m_daily_isValid = false;

    m_monthly_isSet = false;
    m_monthly_isValid = false;

    m_weekly_isSet = false;
    m_weekly_isValid = false;
}

void OAIActiveDeviceCounts::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIActiveDeviceCounts::fromJsonObject(QJsonObject json) {

    m_daily_isValid = ::OpenAPI::fromJsonValue(m_daily, json[QString("daily")]);
    m_daily_isSet = !json[QString("daily")].isNull() && m_daily_isValid;

    m_monthly_isValid = ::OpenAPI::fromJsonValue(m_monthly, json[QString("monthly")]);
    m_monthly_isSet = !json[QString("monthly")].isNull() && m_monthly_isValid;

    m_weekly_isValid = ::OpenAPI::fromJsonValue(m_weekly, json[QString("weekly")]);
    m_weekly_isSet = !json[QString("weekly")].isNull() && m_weekly_isValid;
}

QString OAIActiveDeviceCounts::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIActiveDeviceCounts::asJsonObject() const {
    QJsonObject obj;
    if (m_daily.size() > 0) {
        obj.insert(QString("daily"), ::OpenAPI::toJsonValue(m_daily));
    }
    if (m_monthly.size() > 0) {
        obj.insert(QString("monthly"), ::OpenAPI::toJsonValue(m_monthly));
    }
    if (m_weekly.size() > 0) {
        obj.insert(QString("weekly"), ::OpenAPI::toJsonValue(m_weekly));
    }
    return obj;
}

QList<OAIAnalytics_DeviceCounts_200_response_daily_inner> OAIActiveDeviceCounts::getDaily() const {
    return m_daily;
}
void OAIActiveDeviceCounts::setDaily(const QList<OAIAnalytics_DeviceCounts_200_response_daily_inner> &daily) {
    m_daily = daily;
    m_daily_isSet = true;
}

bool OAIActiveDeviceCounts::is_daily_Set() const{
    return m_daily_isSet;
}

bool OAIActiveDeviceCounts::is_daily_Valid() const{
    return m_daily_isValid;
}

QList<OAIAnalytics_DeviceCounts_200_response_daily_inner> OAIActiveDeviceCounts::getMonthly() const {
    return m_monthly;
}
void OAIActiveDeviceCounts::setMonthly(const QList<OAIAnalytics_DeviceCounts_200_response_daily_inner> &monthly) {
    m_monthly = monthly;
    m_monthly_isSet = true;
}

bool OAIActiveDeviceCounts::is_monthly_Set() const{
    return m_monthly_isSet;
}

bool OAIActiveDeviceCounts::is_monthly_Valid() const{
    return m_monthly_isValid;
}

QList<OAIAnalytics_DeviceCounts_200_response_daily_inner> OAIActiveDeviceCounts::getWeekly() const {
    return m_weekly;
}
void OAIActiveDeviceCounts::setWeekly(const QList<OAIAnalytics_DeviceCounts_200_response_daily_inner> &weekly) {
    m_weekly = weekly;
    m_weekly_isSet = true;
}

bool OAIActiveDeviceCounts::is_weekly_Set() const{
    return m_weekly_isSet;
}

bool OAIActiveDeviceCounts::is_weekly_Valid() const{
    return m_weekly_isValid;
}

bool OAIActiveDeviceCounts::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_daily.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_monthly.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_weekly.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIActiveDeviceCounts::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
