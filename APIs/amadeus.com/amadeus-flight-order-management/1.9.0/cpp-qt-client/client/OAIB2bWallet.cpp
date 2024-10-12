/**
 * Flight Order Management
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.9.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIB2bWallet.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIB2bWallet::OAIB2bWallet(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIB2bWallet::OAIB2bWallet() {
    this->initializeModel();
}

OAIB2bWallet::~OAIB2bWallet() {}

void OAIB2bWallet::initializeModel() {

    m_card_friendly_name_isSet = false;
    m_card_friendly_name_isValid = false;

    m_card_id_isSet = false;
    m_card_id_isValid = false;

    m_card_usage_name_isSet = false;
    m_card_usage_name_isValid = false;

    m_flight_offer_ids_isSet = false;
    m_flight_offer_ids_isValid = false;

    m_reporting_data_isSet = false;
    m_reporting_data_isValid = false;

    m_virtual_credit_card_details_isSet = false;
    m_virtual_credit_card_details_isValid = false;
}

void OAIB2bWallet::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIB2bWallet::fromJsonObject(QJsonObject json) {

    m_card_friendly_name_isValid = ::OpenAPI::fromJsonValue(m_card_friendly_name, json[QString("cardFriendlyName")]);
    m_card_friendly_name_isSet = !json[QString("cardFriendlyName")].isNull() && m_card_friendly_name_isValid;

    m_card_id_isValid = ::OpenAPI::fromJsonValue(m_card_id, json[QString("cardId")]);
    m_card_id_isSet = !json[QString("cardId")].isNull() && m_card_id_isValid;

    m_card_usage_name_isValid = ::OpenAPI::fromJsonValue(m_card_usage_name, json[QString("cardUsageName")]);
    m_card_usage_name_isSet = !json[QString("cardUsageName")].isNull() && m_card_usage_name_isValid;

    m_flight_offer_ids_isValid = ::OpenAPI::fromJsonValue(m_flight_offer_ids, json[QString("flightOfferIds")]);
    m_flight_offer_ids_isSet = !json[QString("flightOfferIds")].isNull() && m_flight_offer_ids_isValid;

    m_reporting_data_isValid = ::OpenAPI::fromJsonValue(m_reporting_data, json[QString("reportingData")]);
    m_reporting_data_isSet = !json[QString("reportingData")].isNull() && m_reporting_data_isValid;

    m_virtual_credit_card_details_isValid = ::OpenAPI::fromJsonValue(m_virtual_credit_card_details, json[QString("virtualCreditCardDetails")]);
    m_virtual_credit_card_details_isSet = !json[QString("virtualCreditCardDetails")].isNull() && m_virtual_credit_card_details_isValid;
}

QString OAIB2bWallet::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIB2bWallet::asJsonObject() const {
    QJsonObject obj;
    if (m_card_friendly_name_isSet) {
        obj.insert(QString("cardFriendlyName"), ::OpenAPI::toJsonValue(m_card_friendly_name));
    }
    if (m_card_id_isSet) {
        obj.insert(QString("cardId"), ::OpenAPI::toJsonValue(m_card_id));
    }
    if (m_card_usage_name_isSet) {
        obj.insert(QString("cardUsageName"), ::OpenAPI::toJsonValue(m_card_usage_name));
    }
    if (m_flight_offer_ids.size() > 0) {
        obj.insert(QString("flightOfferIds"), ::OpenAPI::toJsonValue(m_flight_offer_ids));
    }
    if (m_reporting_data.size() > 0) {
        obj.insert(QString("reportingData"), ::OpenAPI::toJsonValue(m_reporting_data));
    }
    if (m_virtual_credit_card_details.isSet()) {
        obj.insert(QString("virtualCreditCardDetails"), ::OpenAPI::toJsonValue(m_virtual_credit_card_details));
    }
    return obj;
}

QString OAIB2bWallet::getCardFriendlyName() const {
    return m_card_friendly_name;
}
void OAIB2bWallet::setCardFriendlyName(const QString &card_friendly_name) {
    m_card_friendly_name = card_friendly_name;
    m_card_friendly_name_isSet = true;
}

bool OAIB2bWallet::is_card_friendly_name_Set() const{
    return m_card_friendly_name_isSet;
}

bool OAIB2bWallet::is_card_friendly_name_Valid() const{
    return m_card_friendly_name_isValid;
}

QString OAIB2bWallet::getCardId() const {
    return m_card_id;
}
void OAIB2bWallet::setCardId(const QString &card_id) {
    m_card_id = card_id;
    m_card_id_isSet = true;
}

bool OAIB2bWallet::is_card_id_Set() const{
    return m_card_id_isSet;
}

bool OAIB2bWallet::is_card_id_Valid() const{
    return m_card_id_isValid;
}

QString OAIB2bWallet::getCardUsageName() const {
    return m_card_usage_name;
}
void OAIB2bWallet::setCardUsageName(const QString &card_usage_name) {
    m_card_usage_name = card_usage_name;
    m_card_usage_name_isSet = true;
}

bool OAIB2bWallet::is_card_usage_name_Set() const{
    return m_card_usage_name_isSet;
}

bool OAIB2bWallet::is_card_usage_name_Valid() const{
    return m_card_usage_name_isValid;
}

QList<QString> OAIB2bWallet::getFlightOfferIds() const {
    return m_flight_offer_ids;
}
void OAIB2bWallet::setFlightOfferIds(const QList<QString> &flight_offer_ids) {
    m_flight_offer_ids = flight_offer_ids;
    m_flight_offer_ids_isSet = true;
}

bool OAIB2bWallet::is_flight_offer_ids_Set() const{
    return m_flight_offer_ids_isSet;
}

bool OAIB2bWallet::is_flight_offer_ids_Valid() const{
    return m_flight_offer_ids_isValid;
}

QList<OAIReportingData> OAIB2bWallet::getReportingData() const {
    return m_reporting_data;
}
void OAIB2bWallet::setReportingData(const QList<OAIReportingData> &reporting_data) {
    m_reporting_data = reporting_data;
    m_reporting_data_isSet = true;
}

bool OAIB2bWallet::is_reporting_data_Set() const{
    return m_reporting_data_isSet;
}

bool OAIB2bWallet::is_reporting_data_Valid() const{
    return m_reporting_data_isValid;
}

OAIVirtualCreditCardDetails OAIB2bWallet::getVirtualCreditCardDetails() const {
    return m_virtual_credit_card_details;
}
void OAIB2bWallet::setVirtualCreditCardDetails(const OAIVirtualCreditCardDetails &virtual_credit_card_details) {
    m_virtual_credit_card_details = virtual_credit_card_details;
    m_virtual_credit_card_details_isSet = true;
}

bool OAIB2bWallet::is_virtual_credit_card_details_Set() const{
    return m_virtual_credit_card_details_isSet;
}

bool OAIB2bWallet::is_virtual_credit_card_details_Valid() const{
    return m_virtual_credit_card_details_isValid;
}

bool OAIB2bWallet::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_card_friendly_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_card_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_card_usage_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_flight_offer_ids.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_reporting_data.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_virtual_credit_card_details.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIB2bWallet::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
