/**
 * Advicent.FactFinderService
 * An API for accessing the NaviPlan Fact Finder.
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAccountHoldingModel.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAccountHoldingModel::OAIAccountHoldingModel(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAccountHoldingModel::OAIAccountHoldingModel() {
    this->initializeModel();
}

OAIAccountHoldingModel::~OAIAccountHoldingModel() {}

void OAIAccountHoldingModel::initializeModel() {

    m_cost_basis_isSet = false;
    m_cost_basis_isValid = false;

    m_cusip_isSet = false;
    m_cusip_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_external_destination_id_isSet = false;
    m_external_destination_id_isValid = false;

    m_market_value_isSet = false;
    m_market_value_isValid = false;

    m_symbol_isSet = false;
    m_symbol_isValid = false;

    m_valuation_date_isSet = false;
    m_valuation_date_isValid = false;
}

void OAIAccountHoldingModel::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAccountHoldingModel::fromJsonObject(QJsonObject json) {

    m_cost_basis_isValid = ::OpenAPI::fromJsonValue(m_cost_basis, json[QString("costBasis")]);
    m_cost_basis_isSet = !json[QString("costBasis")].isNull() && m_cost_basis_isValid;

    m_cusip_isValid = ::OpenAPI::fromJsonValue(m_cusip, json[QString("cusip")]);
    m_cusip_isSet = !json[QString("cusip")].isNull() && m_cusip_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_external_destination_id_isValid = ::OpenAPI::fromJsonValue(m_external_destination_id, json[QString("externalDestinationId")]);
    m_external_destination_id_isSet = !json[QString("externalDestinationId")].isNull() && m_external_destination_id_isValid;

    m_market_value_isValid = ::OpenAPI::fromJsonValue(m_market_value, json[QString("marketValue")]);
    m_market_value_isSet = !json[QString("marketValue")].isNull() && m_market_value_isValid;

    m_symbol_isValid = ::OpenAPI::fromJsonValue(m_symbol, json[QString("symbol")]);
    m_symbol_isSet = !json[QString("symbol")].isNull() && m_symbol_isValid;

    m_valuation_date_isValid = ::OpenAPI::fromJsonValue(m_valuation_date, json[QString("valuationDate")]);
    m_valuation_date_isSet = !json[QString("valuationDate")].isNull() && m_valuation_date_isValid;
}

QString OAIAccountHoldingModel::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAccountHoldingModel::asJsonObject() const {
    QJsonObject obj;
    if (m_cost_basis_isSet) {
        obj.insert(QString("costBasis"), ::OpenAPI::toJsonValue(m_cost_basis));
    }
    if (m_cusip_isSet) {
        obj.insert(QString("cusip"), ::OpenAPI::toJsonValue(m_cusip));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_external_destination_id_isSet) {
        obj.insert(QString("externalDestinationId"), ::OpenAPI::toJsonValue(m_external_destination_id));
    }
    if (m_market_value_isSet) {
        obj.insert(QString("marketValue"), ::OpenAPI::toJsonValue(m_market_value));
    }
    if (m_symbol_isSet) {
        obj.insert(QString("symbol"), ::OpenAPI::toJsonValue(m_symbol));
    }
    if (m_valuation_date_isSet) {
        obj.insert(QString("valuationDate"), ::OpenAPI::toJsonValue(m_valuation_date));
    }
    return obj;
}

double OAIAccountHoldingModel::getCostBasis() const {
    return m_cost_basis;
}
void OAIAccountHoldingModel::setCostBasis(const double &cost_basis) {
    m_cost_basis = cost_basis;
    m_cost_basis_isSet = true;
}

bool OAIAccountHoldingModel::is_cost_basis_Set() const{
    return m_cost_basis_isSet;
}

bool OAIAccountHoldingModel::is_cost_basis_Valid() const{
    return m_cost_basis_isValid;
}

QString OAIAccountHoldingModel::getCusip() const {
    return m_cusip;
}
void OAIAccountHoldingModel::setCusip(const QString &cusip) {
    m_cusip = cusip;
    m_cusip_isSet = true;
}

bool OAIAccountHoldingModel::is_cusip_Set() const{
    return m_cusip_isSet;
}

bool OAIAccountHoldingModel::is_cusip_Valid() const{
    return m_cusip_isValid;
}

QString OAIAccountHoldingModel::getDescription() const {
    return m_description;
}
void OAIAccountHoldingModel::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIAccountHoldingModel::is_description_Set() const{
    return m_description_isSet;
}

bool OAIAccountHoldingModel::is_description_Valid() const{
    return m_description_isValid;
}

QString OAIAccountHoldingModel::getExternalDestinationId() const {
    return m_external_destination_id;
}
void OAIAccountHoldingModel::setExternalDestinationId(const QString &external_destination_id) {
    m_external_destination_id = external_destination_id;
    m_external_destination_id_isSet = true;
}

bool OAIAccountHoldingModel::is_external_destination_id_Set() const{
    return m_external_destination_id_isSet;
}

bool OAIAccountHoldingModel::is_external_destination_id_Valid() const{
    return m_external_destination_id_isValid;
}

double OAIAccountHoldingModel::getMarketValue() const {
    return m_market_value;
}
void OAIAccountHoldingModel::setMarketValue(const double &market_value) {
    m_market_value = market_value;
    m_market_value_isSet = true;
}

bool OAIAccountHoldingModel::is_market_value_Set() const{
    return m_market_value_isSet;
}

bool OAIAccountHoldingModel::is_market_value_Valid() const{
    return m_market_value_isValid;
}

QString OAIAccountHoldingModel::getSymbol() const {
    return m_symbol;
}
void OAIAccountHoldingModel::setSymbol(const QString &symbol) {
    m_symbol = symbol;
    m_symbol_isSet = true;
}

bool OAIAccountHoldingModel::is_symbol_Set() const{
    return m_symbol_isSet;
}

bool OAIAccountHoldingModel::is_symbol_Valid() const{
    return m_symbol_isValid;
}

QDateTime OAIAccountHoldingModel::getValuationDate() const {
    return m_valuation_date;
}
void OAIAccountHoldingModel::setValuationDate(const QDateTime &valuation_date) {
    m_valuation_date = valuation_date;
    m_valuation_date_isSet = true;
}

bool OAIAccountHoldingModel::is_valuation_date_Set() const{
    return m_valuation_date_isSet;
}

bool OAIAccountHoldingModel::is_valuation_date_Valid() const{
    return m_valuation_date_isValid;
}

bool OAIAccountHoldingModel::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_cost_basis_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_cusip_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_external_destination_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_market_value_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_symbol_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_valuation_date_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAccountHoldingModel::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_description_isValid && true;
}

} // namespace OpenAPI
