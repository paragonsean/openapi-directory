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

#include "OAIIInterCompanyDividendReceived.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIIInterCompanyDividendReceived::OAIIInterCompanyDividendReceived(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIIInterCompanyDividendReceived::OAIIInterCompanyDividendReceived() {
    this->initializeModel();
}

OAIIInterCompanyDividendReceived::~OAIIInterCompanyDividendReceived() {}

void OAIIInterCompanyDividendReceived::initializeModel() {

    m_activity_data_isSet = false;
    m_activity_data_isValid = false;

    m_dividend_type_isSet = false;
    m_dividend_type_isValid = false;

    m_general_rate_of_income_pool_amount_isSet = false;
    m_general_rate_of_income_pool_amount_isValid = false;

    m_received_from_isSet = false;
    m_received_from_isValid = false;
}

void OAIIInterCompanyDividendReceived::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIIInterCompanyDividendReceived::fromJsonObject(QJsonObject json) {

    m_activity_data_isValid = ::OpenAPI::fromJsonValue(m_activity_data, json[QString("activityData")]);
    m_activity_data_isSet = !json[QString("activityData")].isNull() && m_activity_data_isValid;

    m_dividend_type_isValid = ::OpenAPI::fromJsonValue(m_dividend_type, json[QString("dividendType")]);
    m_dividend_type_isSet = !json[QString("dividendType")].isNull() && m_dividend_type_isValid;

    m_general_rate_of_income_pool_amount_isValid = ::OpenAPI::fromJsonValue(m_general_rate_of_income_pool_amount, json[QString("generalRateOfIncomePoolAmount")]);
    m_general_rate_of_income_pool_amount_isSet = !json[QString("generalRateOfIncomePoolAmount")].isNull() && m_general_rate_of_income_pool_amount_isValid;

    m_received_from_isValid = ::OpenAPI::fromJsonValue(m_received_from, json[QString("receivedFrom")]);
    m_received_from_isSet = !json[QString("receivedFrom")].isNull() && m_received_from_isValid;
}

QString OAIIInterCompanyDividendReceived::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIIInterCompanyDividendReceived::asJsonObject() const {
    QJsonObject obj;
    if (m_activity_data.isSet()) {
        obj.insert(QString("activityData"), ::OpenAPI::toJsonValue(m_activity_data));
    }
    if (m_dividend_type.isSet()) {
        obj.insert(QString("dividendType"), ::OpenAPI::toJsonValue(m_dividend_type));
    }
    if (m_general_rate_of_income_pool_amount.isSet()) {
        obj.insert(QString("generalRateOfIncomePoolAmount"), ::OpenAPI::toJsonValue(m_general_rate_of_income_pool_amount));
    }
    if (m_received_from_isSet) {
        obj.insert(QString("receivedFrom"), ::OpenAPI::toJsonValue(m_received_from));
    }
    return obj;
}

OAIIActivityData OAIIInterCompanyDividendReceived::getActivityData() const {
    return m_activity_data;
}
void OAIIInterCompanyDividendReceived::setActivityData(const OAIIActivityData &activity_data) {
    m_activity_data = activity_data;
    m_activity_data_isSet = true;
}

bool OAIIInterCompanyDividendReceived::is_activity_data_Set() const{
    return m_activity_data_isSet;
}

bool OAIIInterCompanyDividendReceived::is_activity_data_Valid() const{
    return m_activity_data_isValid;
}

OAIFormattedEnumType_InterCompanyDividendType OAIIInterCompanyDividendReceived::getDividendType() const {
    return m_dividend_type;
}
void OAIIInterCompanyDividendReceived::setDividendType(const OAIFormattedEnumType_InterCompanyDividendType &dividend_type) {
    m_dividend_type = dividend_type;
    m_dividend_type_isSet = true;
}

bool OAIIInterCompanyDividendReceived::is_dividend_type_Set() const{
    return m_dividend_type_isSet;
}

bool OAIIInterCompanyDividendReceived::is_dividend_type_Valid() const{
    return m_dividend_type_isValid;
}

OAICurrency OAIIInterCompanyDividendReceived::getGeneralRateOfIncomePoolAmount() const {
    return m_general_rate_of_income_pool_amount;
}
void OAIIInterCompanyDividendReceived::setGeneralRateOfIncomePoolAmount(const OAICurrency &general_rate_of_income_pool_amount) {
    m_general_rate_of_income_pool_amount = general_rate_of_income_pool_amount;
    m_general_rate_of_income_pool_amount_isSet = true;
}

bool OAIIInterCompanyDividendReceived::is_general_rate_of_income_pool_amount_Set() const{
    return m_general_rate_of_income_pool_amount_isSet;
}

bool OAIIInterCompanyDividendReceived::is_general_rate_of_income_pool_amount_Valid() const{
    return m_general_rate_of_income_pool_amount_isValid;
}

QString OAIIInterCompanyDividendReceived::getReceivedFrom() const {
    return m_received_from;
}
void OAIIInterCompanyDividendReceived::setReceivedFrom(const QString &received_from) {
    m_received_from = received_from;
    m_received_from_isSet = true;
}

bool OAIIInterCompanyDividendReceived::is_received_from_Set() const{
    return m_received_from_isSet;
}

bool OAIIInterCompanyDividendReceived::is_received_from_Valid() const{
    return m_received_from_isValid;
}

bool OAIIInterCompanyDividendReceived::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_activity_data.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_dividend_type.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_general_rate_of_income_pool_amount.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_received_from_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIIInterCompanyDividendReceived::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
