/**
 * NaviPlan API
 * An API for accessing NaviPlan plan data for a client.
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIIRedemptionStrategies.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIIRedemptionStrategies::OAIIRedemptionStrategies(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIIRedemptionStrategies::OAIIRedemptionStrategies() {
    this->initializeModel();
}

OAIIRedemptionStrategies::~OAIIRedemptionStrategies() {}

void OAIIRedemptionStrategies::initializeModel() {

    m_lump_sum_redemption_strategies_isSet = false;
    m_lump_sum_redemption_strategies_isValid = false;

    m_periodic_redemption_strategies_isSet = false;
    m_periodic_redemption_strategies_isValid = false;
}

void OAIIRedemptionStrategies::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIIRedemptionStrategies::fromJsonObject(QJsonObject json) {

    m_lump_sum_redemption_strategies_isValid = ::OpenAPI::fromJsonValue(m_lump_sum_redemption_strategies, json[QString("lumpSumRedemptionStrategies")]);
    m_lump_sum_redemption_strategies_isSet = !json[QString("lumpSumRedemptionStrategies")].isNull() && m_lump_sum_redemption_strategies_isValid;

    m_periodic_redemption_strategies_isValid = ::OpenAPI::fromJsonValue(m_periodic_redemption_strategies, json[QString("periodicRedemptionStrategies")]);
    m_periodic_redemption_strategies_isSet = !json[QString("periodicRedemptionStrategies")].isNull() && m_periodic_redemption_strategies_isValid;
}

QString OAIIRedemptionStrategies::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIIRedemptionStrategies::asJsonObject() const {
    QJsonObject obj;
    if (m_lump_sum_redemption_strategies.size() > 0) {
        obj.insert(QString("lumpSumRedemptionStrategies"), ::OpenAPI::toJsonValue(m_lump_sum_redemption_strategies));
    }
    if (m_periodic_redemption_strategies.size() > 0) {
        obj.insert(QString("periodicRedemptionStrategies"), ::OpenAPI::toJsonValue(m_periodic_redemption_strategies));
    }
    return obj;
}

QList<OAIILumpSumRedemptionStrategy> OAIIRedemptionStrategies::getLumpSumRedemptionStrategies() const {
    return m_lump_sum_redemption_strategies;
}
void OAIIRedemptionStrategies::setLumpSumRedemptionStrategies(const QList<OAIILumpSumRedemptionStrategy> &lump_sum_redemption_strategies) {
    m_lump_sum_redemption_strategies = lump_sum_redemption_strategies;
    m_lump_sum_redemption_strategies_isSet = true;
}

bool OAIIRedemptionStrategies::is_lump_sum_redemption_strategies_Set() const{
    return m_lump_sum_redemption_strategies_isSet;
}

bool OAIIRedemptionStrategies::is_lump_sum_redemption_strategies_Valid() const{
    return m_lump_sum_redemption_strategies_isValid;
}

QList<OAIIPeriodicRedemptionStrategy> OAIIRedemptionStrategies::getPeriodicRedemptionStrategies() const {
    return m_periodic_redemption_strategies;
}
void OAIIRedemptionStrategies::setPeriodicRedemptionStrategies(const QList<OAIIPeriodicRedemptionStrategy> &periodic_redemption_strategies) {
    m_periodic_redemption_strategies = periodic_redemption_strategies;
    m_periodic_redemption_strategies_isSet = true;
}

bool OAIIRedemptionStrategies::is_periodic_redemption_strategies_Set() const{
    return m_periodic_redemption_strategies_isSet;
}

bool OAIIRedemptionStrategies::is_periodic_redemption_strategies_Valid() const{
    return m_periodic_redemption_strategies_isValid;
}

bool OAIIRedemptionStrategies::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_lump_sum_redemption_strategies.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_periodic_redemption_strategies.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIIRedemptionStrategies::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
