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

#include "OAISummary.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISummary::OAISummary(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISummary::OAISummary() {
    this->initializeModel();
}

OAISummary::~OAISummary() {}

void OAISummary::initializeModel() {

    m_currency_code_isSet = false;
    m_currency_code_isValid = false;

    m_end_date_isSet = false;
    m_end_date_isValid = false;

    m_fx_rate_date_isSet = false;
    m_fx_rate_date_isValid = false;

    m_indicative_isSet = false;
    m_indicative_isValid = false;

    m_quarter_isSet = false;
    m_quarter_isValid = false;

    m_start_date_isSet = false;
    m_start_date_isValid = false;

    m_tax_amount_isSet = false;
    m_tax_amount_isValid = false;

    m_tax_entity_name_isSet = false;
    m_tax_entity_name_isValid = false;
}

void OAISummary::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISummary::fromJsonObject(QJsonObject json) {

    m_currency_code_isValid = ::OpenAPI::fromJsonValue(m_currency_code, json[QString("currency_code")]);
    m_currency_code_isSet = !json[QString("currency_code")].isNull() && m_currency_code_isValid;

    m_end_date_isValid = ::OpenAPI::fromJsonValue(m_end_date, json[QString("end_date")]);
    m_end_date_isSet = !json[QString("end_date")].isNull() && m_end_date_isValid;

    m_fx_rate_date_isValid = ::OpenAPI::fromJsonValue(m_fx_rate_date, json[QString("fx_rate_date")]);
    m_fx_rate_date_isSet = !json[QString("fx_rate_date")].isNull() && m_fx_rate_date_isValid;

    m_indicative_isValid = ::OpenAPI::fromJsonValue(m_indicative, json[QString("indicative")]);
    m_indicative_isSet = !json[QString("indicative")].isNull() && m_indicative_isValid;

    m_quarter_isValid = ::OpenAPI::fromJsonValue(m_quarter, json[QString("quarter")]);
    m_quarter_isSet = !json[QString("quarter")].isNull() && m_quarter_isValid;

    m_start_date_isValid = ::OpenAPI::fromJsonValue(m_start_date, json[QString("start_date")]);
    m_start_date_isSet = !json[QString("start_date")].isNull() && m_start_date_isValid;

    m_tax_amount_isValid = ::OpenAPI::fromJsonValue(m_tax_amount, json[QString("tax_amount")]);
    m_tax_amount_isSet = !json[QString("tax_amount")].isNull() && m_tax_amount_isValid;

    m_tax_entity_name_isValid = ::OpenAPI::fromJsonValue(m_tax_entity_name, json[QString("tax_entity_name")]);
    m_tax_entity_name_isSet = !json[QString("tax_entity_name")].isNull() && m_tax_entity_name_isValid;
}

QString OAISummary::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISummary::asJsonObject() const {
    QJsonObject obj;
    if (m_currency_code_isSet) {
        obj.insert(QString("currency_code"), ::OpenAPI::toJsonValue(m_currency_code));
    }
    if (m_end_date_isSet) {
        obj.insert(QString("end_date"), ::OpenAPI::toJsonValue(m_end_date));
    }
    if (m_fx_rate_date_isSet) {
        obj.insert(QString("fx_rate_date"), ::OpenAPI::toJsonValue(m_fx_rate_date));
    }
    if (m_indicative_isSet) {
        obj.insert(QString("indicative"), ::OpenAPI::toJsonValue(m_indicative));
    }
    if (m_quarter_isSet) {
        obj.insert(QString("quarter"), ::OpenAPI::toJsonValue(m_quarter));
    }
    if (m_start_date_isSet) {
        obj.insert(QString("start_date"), ::OpenAPI::toJsonValue(m_start_date));
    }
    if (m_tax_amount_isSet) {
        obj.insert(QString("tax_amount"), ::OpenAPI::toJsonValue(m_tax_amount));
    }
    if (m_tax_entity_name_isSet) {
        obj.insert(QString("tax_entity_name"), ::OpenAPI::toJsonValue(m_tax_entity_name));
    }
    return obj;
}

QString OAISummary::getCurrencyCode() const {
    return m_currency_code;
}
void OAISummary::setCurrencyCode(const QString &currency_code) {
    m_currency_code = currency_code;
    m_currency_code_isSet = true;
}

bool OAISummary::is_currency_code_Set() const{
    return m_currency_code_isSet;
}

bool OAISummary::is_currency_code_Valid() const{
    return m_currency_code_isValid;
}

QString OAISummary::getEndDate() const {
    return m_end_date;
}
void OAISummary::setEndDate(const QString &end_date) {
    m_end_date = end_date;
    m_end_date_isSet = true;
}

bool OAISummary::is_end_date_Set() const{
    return m_end_date_isSet;
}

bool OAISummary::is_end_date_Valid() const{
    return m_end_date_isValid;
}

QString OAISummary::getFxRateDate() const {
    return m_fx_rate_date;
}
void OAISummary::setFxRateDate(const QString &fx_rate_date) {
    m_fx_rate_date = fx_rate_date;
    m_fx_rate_date_isSet = true;
}

bool OAISummary::is_fx_rate_date_Set() const{
    return m_fx_rate_date_isSet;
}

bool OAISummary::is_fx_rate_date_Valid() const{
    return m_fx_rate_date_isValid;
}

bool OAISummary::isIndicative() const {
    return m_indicative;
}
void OAISummary::setIndicative(const bool &indicative) {
    m_indicative = indicative;
    m_indicative_isSet = true;
}

bool OAISummary::is_indicative_Set() const{
    return m_indicative_isSet;
}

bool OAISummary::is_indicative_Valid() const{
    return m_indicative_isValid;
}

QString OAISummary::getQuarter() const {
    return m_quarter;
}
void OAISummary::setQuarter(const QString &quarter) {
    m_quarter = quarter;
    m_quarter_isSet = true;
}

bool OAISummary::is_quarter_Set() const{
    return m_quarter_isSet;
}

bool OAISummary::is_quarter_Valid() const{
    return m_quarter_isValid;
}

QString OAISummary::getStartDate() const {
    return m_start_date;
}
void OAISummary::setStartDate(const QString &start_date) {
    m_start_date = start_date;
    m_start_date_isSet = true;
}

bool OAISummary::is_start_date_Set() const{
    return m_start_date_isSet;
}

bool OAISummary::is_start_date_Valid() const{
    return m_start_date_isValid;
}

double OAISummary::getTaxAmount() const {
    return m_tax_amount;
}
void OAISummary::setTaxAmount(const double &tax_amount) {
    m_tax_amount = tax_amount;
    m_tax_amount_isSet = true;
}

bool OAISummary::is_tax_amount_Set() const{
    return m_tax_amount_isSet;
}

bool OAISummary::is_tax_amount_Valid() const{
    return m_tax_amount_isValid;
}

QString OAISummary::getTaxEntityName() const {
    return m_tax_entity_name;
}
void OAISummary::setTaxEntityName(const QString &tax_entity_name) {
    m_tax_entity_name = tax_entity_name;
    m_tax_entity_name_isSet = true;
}

bool OAISummary::is_tax_entity_name_Set() const{
    return m_tax_entity_name_isSet;
}

bool OAISummary::is_tax_entity_name_Valid() const{
    return m_tax_entity_name_isValid;
}

bool OAISummary::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_currency_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_end_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_fx_rate_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_indicative_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_quarter_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_start_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tax_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tax_entity_name_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISummary::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
