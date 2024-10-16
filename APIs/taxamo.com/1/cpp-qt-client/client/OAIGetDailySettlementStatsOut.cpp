/**
 * Taxamo
 * Taxamo’s elegant suite of APIs and comprehensive reporting dashboard enables digital merchants to easily comply with EU regulatory requirements on tax calculation, evidence collection, tax return creation and data storage.
 *
 * The version of the OpenAPI document: 1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIGetDailySettlementStatsOut.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetDailySettlementStatsOut::OAIGetDailySettlementStatsOut(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetDailySettlementStatsOut::OAIGetDailySettlementStatsOut() {
    this->initializeModel();
}

OAIGetDailySettlementStatsOut::~OAIGetDailySettlementStatsOut() {}

void OAIGetDailySettlementStatsOut::initializeModel() {

    m_settlement_daily_isSet = false;
    m_settlement_daily_isValid = false;
}

void OAIGetDailySettlementStatsOut::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetDailySettlementStatsOut::fromJsonObject(QJsonObject json) {

    m_settlement_daily_isValid = ::OpenAPI::fromJsonValue(m_settlement_daily, json[QString("settlement_daily")]);
    m_settlement_daily_isSet = !json[QString("settlement_daily")].isNull() && m_settlement_daily_isValid;
}

QString OAIGetDailySettlementStatsOut::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetDailySettlementStatsOut::asJsonObject() const {
    QJsonObject obj;
    if (m_settlement_daily.size() > 0) {
        obj.insert(QString("settlement_daily"), ::OpenAPI::toJsonValue(m_settlement_daily));
    }
    return obj;
}

QList<OAISettlement_daily_stats_schema> OAIGetDailySettlementStatsOut::getSettlementDaily() const {
    return m_settlement_daily;
}
void OAIGetDailySettlementStatsOut::setSettlementDaily(const QList<OAISettlement_daily_stats_schema> &settlement_daily) {
    m_settlement_daily = settlement_daily;
    m_settlement_daily_isSet = true;
}

bool OAIGetDailySettlementStatsOut::is_settlement_daily_Set() const{
    return m_settlement_daily_isSet;
}

bool OAIGetDailySettlementStatsOut::is_settlement_daily_Valid() const{
    return m_settlement_daily_isValid;
}

bool OAIGetDailySettlementStatsOut::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_settlement_daily.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGetDailySettlementStatsOut::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
