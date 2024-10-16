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

#include "OAIUpdateNetworkWirelessBilling_request_plans_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUpdateNetworkWirelessBilling_request_plans_inner::OAIUpdateNetworkWirelessBilling_request_plans_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUpdateNetworkWirelessBilling_request_plans_inner::OAIUpdateNetworkWirelessBilling_request_plans_inner() {
    this->initializeModel();
}

OAIUpdateNetworkWirelessBilling_request_plans_inner::~OAIUpdateNetworkWirelessBilling_request_plans_inner() {}

void OAIUpdateNetworkWirelessBilling_request_plans_inner::initializeModel() {

    m_bandwidth_limits_isSet = false;
    m_bandwidth_limits_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_price_isSet = false;
    m_price_isValid = false;

    m_time_limit_isSet = false;
    m_time_limit_isValid = false;
}

void OAIUpdateNetworkWirelessBilling_request_plans_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUpdateNetworkWirelessBilling_request_plans_inner::fromJsonObject(QJsonObject json) {

    m_bandwidth_limits_isValid = ::OpenAPI::fromJsonValue(m_bandwidth_limits, json[QString("bandwidthLimits")]);
    m_bandwidth_limits_isSet = !json[QString("bandwidthLimits")].isNull() && m_bandwidth_limits_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_price_isValid = ::OpenAPI::fromJsonValue(m_price, json[QString("price")]);
    m_price_isSet = !json[QString("price")].isNull() && m_price_isValid;

    m_time_limit_isValid = ::OpenAPI::fromJsonValue(m_time_limit, json[QString("timeLimit")]);
    m_time_limit_isSet = !json[QString("timeLimit")].isNull() && m_time_limit_isValid;
}

QString OAIUpdateNetworkWirelessBilling_request_plans_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUpdateNetworkWirelessBilling_request_plans_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_bandwidth_limits.isSet()) {
        obj.insert(QString("bandwidthLimits"), ::OpenAPI::toJsonValue(m_bandwidth_limits));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_price_isSet) {
        obj.insert(QString("price"), ::OpenAPI::toJsonValue(m_price));
    }
    if (m_time_limit_isSet) {
        obj.insert(QString("timeLimit"), ::OpenAPI::toJsonValue(m_time_limit));
    }
    return obj;
}

OAIUpdateNetworkWirelessBilling_request_plans_inner_bandwidthLimits OAIUpdateNetworkWirelessBilling_request_plans_inner::getBandwidthLimits() const {
    return m_bandwidth_limits;
}
void OAIUpdateNetworkWirelessBilling_request_plans_inner::setBandwidthLimits(const OAIUpdateNetworkWirelessBilling_request_plans_inner_bandwidthLimits &bandwidth_limits) {
    m_bandwidth_limits = bandwidth_limits;
    m_bandwidth_limits_isSet = true;
}

bool OAIUpdateNetworkWirelessBilling_request_plans_inner::is_bandwidth_limits_Set() const{
    return m_bandwidth_limits_isSet;
}

bool OAIUpdateNetworkWirelessBilling_request_plans_inner::is_bandwidth_limits_Valid() const{
    return m_bandwidth_limits_isValid;
}

QString OAIUpdateNetworkWirelessBilling_request_plans_inner::getId() const {
    return m_id;
}
void OAIUpdateNetworkWirelessBilling_request_plans_inner::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIUpdateNetworkWirelessBilling_request_plans_inner::is_id_Set() const{
    return m_id_isSet;
}

bool OAIUpdateNetworkWirelessBilling_request_plans_inner::is_id_Valid() const{
    return m_id_isValid;
}

float OAIUpdateNetworkWirelessBilling_request_plans_inner::getPrice() const {
    return m_price;
}
void OAIUpdateNetworkWirelessBilling_request_plans_inner::setPrice(const float &price) {
    m_price = price;
    m_price_isSet = true;
}

bool OAIUpdateNetworkWirelessBilling_request_plans_inner::is_price_Set() const{
    return m_price_isSet;
}

bool OAIUpdateNetworkWirelessBilling_request_plans_inner::is_price_Valid() const{
    return m_price_isValid;
}

QString OAIUpdateNetworkWirelessBilling_request_plans_inner::getTimeLimit() const {
    return m_time_limit;
}
void OAIUpdateNetworkWirelessBilling_request_plans_inner::setTimeLimit(const QString &time_limit) {
    m_time_limit = time_limit;
    m_time_limit_isSet = true;
}

bool OAIUpdateNetworkWirelessBilling_request_plans_inner::is_time_limit_Set() const{
    return m_time_limit_isSet;
}

bool OAIUpdateNetworkWirelessBilling_request_plans_inner::is_time_limit_Valid() const{
    return m_time_limit_isValid;
}

bool OAIUpdateNetworkWirelessBilling_request_plans_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_bandwidth_limits.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_price_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_time_limit_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUpdateNetworkWirelessBilling_request_plans_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_bandwidth_limits_isValid && m_price_isValid && m_time_limit_isValid && true;
}

} // namespace OpenAPI
