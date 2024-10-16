/**
 * Native Ads Publisher API
 * This is a Native Ads Publisher API it provides same functionality as Native Ads Publisher Account GUI. 
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIReportsDailyItem.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIReportsDailyItem::OAIReportsDailyItem(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIReportsDailyItem::OAIReportsDailyItem() {
    this->initializeModel();
}

OAIReportsDailyItem::~OAIReportsDailyItem() {}

void OAIReportsDailyItem::initializeModel() {

    m_clicks_isSet = false;
    m_clicks_isValid = false;

    m_cpc_isSet = false;
    m_cpc_isValid = false;

    m_ctr_isSet = false;
    m_ctr_isValid = false;

    m_date_isSet = false;
    m_date_isValid = false;

    m_earnings_isSet = false;
    m_earnings_isValid = false;

    m_impressions_isSet = false;
    m_impressions_isValid = false;

    m_net_ecpm_isSet = false;
    m_net_ecpm_isValid = false;

    m_rpm_isSet = false;
    m_rpm_isValid = false;
}

void OAIReportsDailyItem::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIReportsDailyItem::fromJsonObject(QJsonObject json) {

    m_clicks_isValid = ::OpenAPI::fromJsonValue(m_clicks, json[QString("clicks")]);
    m_clicks_isSet = !json[QString("clicks")].isNull() && m_clicks_isValid;

    m_cpc_isValid = ::OpenAPI::fromJsonValue(m_cpc, json[QString("cpc")]);
    m_cpc_isSet = !json[QString("cpc")].isNull() && m_cpc_isValid;

    m_ctr_isValid = ::OpenAPI::fromJsonValue(m_ctr, json[QString("ctr")]);
    m_ctr_isSet = !json[QString("ctr")].isNull() && m_ctr_isValid;

    m_date_isValid = ::OpenAPI::fromJsonValue(m_date, json[QString("date")]);
    m_date_isSet = !json[QString("date")].isNull() && m_date_isValid;

    m_earnings_isValid = ::OpenAPI::fromJsonValue(m_earnings, json[QString("earnings")]);
    m_earnings_isSet = !json[QString("earnings")].isNull() && m_earnings_isValid;

    m_impressions_isValid = ::OpenAPI::fromJsonValue(m_impressions, json[QString("impressions")]);
    m_impressions_isSet = !json[QString("impressions")].isNull() && m_impressions_isValid;

    m_net_ecpm_isValid = ::OpenAPI::fromJsonValue(m_net_ecpm, json[QString("net_ecpm")]);
    m_net_ecpm_isSet = !json[QString("net_ecpm")].isNull() && m_net_ecpm_isValid;

    m_rpm_isValid = ::OpenAPI::fromJsonValue(m_rpm, json[QString("rpm")]);
    m_rpm_isSet = !json[QString("rpm")].isNull() && m_rpm_isValid;
}

QString OAIReportsDailyItem::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIReportsDailyItem::asJsonObject() const {
    QJsonObject obj;
    if (m_clicks_isSet) {
        obj.insert(QString("clicks"), ::OpenAPI::toJsonValue(m_clicks));
    }
    if (m_cpc_isSet) {
        obj.insert(QString("cpc"), ::OpenAPI::toJsonValue(m_cpc));
    }
    if (m_ctr_isSet) {
        obj.insert(QString("ctr"), ::OpenAPI::toJsonValue(m_ctr));
    }
    if (m_date_isSet) {
        obj.insert(QString("date"), ::OpenAPI::toJsonValue(m_date));
    }
    if (m_earnings_isSet) {
        obj.insert(QString("earnings"), ::OpenAPI::toJsonValue(m_earnings));
    }
    if (m_impressions_isSet) {
        obj.insert(QString("impressions"), ::OpenAPI::toJsonValue(m_impressions));
    }
    if (m_net_ecpm_isSet) {
        obj.insert(QString("net_ecpm"), ::OpenAPI::toJsonValue(m_net_ecpm));
    }
    if (m_rpm_isSet) {
        obj.insert(QString("rpm"), ::OpenAPI::toJsonValue(m_rpm));
    }
    return obj;
}

QString OAIReportsDailyItem::getClicks() const {
    return m_clicks;
}
void OAIReportsDailyItem::setClicks(const QString &clicks) {
    m_clicks = clicks;
    m_clicks_isSet = true;
}

bool OAIReportsDailyItem::is_clicks_Set() const{
    return m_clicks_isSet;
}

bool OAIReportsDailyItem::is_clicks_Valid() const{
    return m_clicks_isValid;
}

QString OAIReportsDailyItem::getCpc() const {
    return m_cpc;
}
void OAIReportsDailyItem::setCpc(const QString &cpc) {
    m_cpc = cpc;
    m_cpc_isSet = true;
}

bool OAIReportsDailyItem::is_cpc_Set() const{
    return m_cpc_isSet;
}

bool OAIReportsDailyItem::is_cpc_Valid() const{
    return m_cpc_isValid;
}

QString OAIReportsDailyItem::getCtr() const {
    return m_ctr;
}
void OAIReportsDailyItem::setCtr(const QString &ctr) {
    m_ctr = ctr;
    m_ctr_isSet = true;
}

bool OAIReportsDailyItem::is_ctr_Set() const{
    return m_ctr_isSet;
}

bool OAIReportsDailyItem::is_ctr_Valid() const{
    return m_ctr_isValid;
}

QString OAIReportsDailyItem::getDate() const {
    return m_date;
}
void OAIReportsDailyItem::setDate(const QString &date) {
    m_date = date;
    m_date_isSet = true;
}

bool OAIReportsDailyItem::is_date_Set() const{
    return m_date_isSet;
}

bool OAIReportsDailyItem::is_date_Valid() const{
    return m_date_isValid;
}

QString OAIReportsDailyItem::getEarnings() const {
    return m_earnings;
}
void OAIReportsDailyItem::setEarnings(const QString &earnings) {
    m_earnings = earnings;
    m_earnings_isSet = true;
}

bool OAIReportsDailyItem::is_earnings_Set() const{
    return m_earnings_isSet;
}

bool OAIReportsDailyItem::is_earnings_Valid() const{
    return m_earnings_isValid;
}

QString OAIReportsDailyItem::getImpressions() const {
    return m_impressions;
}
void OAIReportsDailyItem::setImpressions(const QString &impressions) {
    m_impressions = impressions;
    m_impressions_isSet = true;
}

bool OAIReportsDailyItem::is_impressions_Set() const{
    return m_impressions_isSet;
}

bool OAIReportsDailyItem::is_impressions_Valid() const{
    return m_impressions_isValid;
}

QString OAIReportsDailyItem::getNetEcpm() const {
    return m_net_ecpm;
}
void OAIReportsDailyItem::setNetEcpm(const QString &net_ecpm) {
    m_net_ecpm = net_ecpm;
    m_net_ecpm_isSet = true;
}

bool OAIReportsDailyItem::is_net_ecpm_Set() const{
    return m_net_ecpm_isSet;
}

bool OAIReportsDailyItem::is_net_ecpm_Valid() const{
    return m_net_ecpm_isValid;
}

QString OAIReportsDailyItem::getRpm() const {
    return m_rpm;
}
void OAIReportsDailyItem::setRpm(const QString &rpm) {
    m_rpm = rpm;
    m_rpm_isSet = true;
}

bool OAIReportsDailyItem::is_rpm_Set() const{
    return m_rpm_isSet;
}

bool OAIReportsDailyItem::is_rpm_Valid() const{
    return m_rpm_isValid;
}

bool OAIReportsDailyItem::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_clicks_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_cpc_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ctr_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_earnings_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_impressions_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_net_ecpm_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_rpm_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIReportsDailyItem::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
