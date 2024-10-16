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

#include "OAIUpdateNetworkWirelessBilling_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUpdateNetworkWirelessBilling_request::OAIUpdateNetworkWirelessBilling_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUpdateNetworkWirelessBilling_request::OAIUpdateNetworkWirelessBilling_request() {
    this->initializeModel();
}

OAIUpdateNetworkWirelessBilling_request::~OAIUpdateNetworkWirelessBilling_request() {}

void OAIUpdateNetworkWirelessBilling_request::initializeModel() {

    m_currency_isSet = false;
    m_currency_isValid = false;

    m_plans_isSet = false;
    m_plans_isValid = false;
}

void OAIUpdateNetworkWirelessBilling_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUpdateNetworkWirelessBilling_request::fromJsonObject(QJsonObject json) {

    m_currency_isValid = ::OpenAPI::fromJsonValue(m_currency, json[QString("currency")]);
    m_currency_isSet = !json[QString("currency")].isNull() && m_currency_isValid;

    m_plans_isValid = ::OpenAPI::fromJsonValue(m_plans, json[QString("plans")]);
    m_plans_isSet = !json[QString("plans")].isNull() && m_plans_isValid;
}

QString OAIUpdateNetworkWirelessBilling_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUpdateNetworkWirelessBilling_request::asJsonObject() const {
    QJsonObject obj;
    if (m_currency_isSet) {
        obj.insert(QString("currency"), ::OpenAPI::toJsonValue(m_currency));
    }
    if (m_plans.size() > 0) {
        obj.insert(QString("plans"), ::OpenAPI::toJsonValue(m_plans));
    }
    return obj;
}

QString OAIUpdateNetworkWirelessBilling_request::getCurrency() const {
    return m_currency;
}
void OAIUpdateNetworkWirelessBilling_request::setCurrency(const QString &currency) {
    m_currency = currency;
    m_currency_isSet = true;
}

bool OAIUpdateNetworkWirelessBilling_request::is_currency_Set() const{
    return m_currency_isSet;
}

bool OAIUpdateNetworkWirelessBilling_request::is_currency_Valid() const{
    return m_currency_isValid;
}

QList<OAIUpdateNetworkWirelessBilling_request_plans_inner> OAIUpdateNetworkWirelessBilling_request::getPlans() const {
    return m_plans;
}
void OAIUpdateNetworkWirelessBilling_request::setPlans(const QList<OAIUpdateNetworkWirelessBilling_request_plans_inner> &plans) {
    m_plans = plans;
    m_plans_isSet = true;
}

bool OAIUpdateNetworkWirelessBilling_request::is_plans_Set() const{
    return m_plans_isSet;
}

bool OAIUpdateNetworkWirelessBilling_request::is_plans_Valid() const{
    return m_plans_isValid;
}

bool OAIUpdateNetworkWirelessBilling_request::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_currency_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_plans.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUpdateNetworkWirelessBilling_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
