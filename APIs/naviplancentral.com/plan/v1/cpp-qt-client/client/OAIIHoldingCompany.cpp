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

#include "OAIIHoldingCompany.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIIHoldingCompany::OAIIHoldingCompany(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIIHoldingCompany::OAIIHoldingCompany() {
    this->initializeModel();
}

OAIIHoldingCompany::~OAIIHoldingCompany() {}

void OAIIHoldingCompany::initializeModel() {

    m_annual_dividend_yield_isSet = false;
    m_annual_dividend_yield_isValid = false;

    m_ccpc_isSet = false;
    m_ccpc_isValid = false;

    m_common_shares_outstanding_isSet = false;
    m_common_shares_outstanding_isValid = false;

    m_contributions_isSet = false;
    m_contributions_isValid = false;

    m_corporate_year_end_isSet = false;
    m_corporate_year_end_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_dividend_type_isSet = false;
    m_dividend_type_isValid = false;

    m_dividend_type_formatted_isSet = false;
    m_dividend_type_formatted_isValid = false;

    m_estate_details_isSet = false;
    m_estate_details_isValid = false;

    m_historical_data_isSet = false;
    m_historical_data_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_investment_accounts_isSet = false;
    m_investment_accounts_isValid = false;

    m_liabilities_isSet = false;
    m_liabilities_isValid = false;

    m_life_insurance_policies_isSet = false;
    m_life_insurance_policies_isValid = false;

    m_market_value_isSet = false;
    m_market_value_isValid = false;

    m_num_preferred_share_classes_isSet = false;
    m_num_preferred_share_classes_isValid = false;

    m_other_assets_isSet = false;
    m_other_assets_isValid = false;

    m_ownership_as_of_date_isSet = false;
    m_ownership_as_of_date_isValid = false;

    m_ownership_details_isSet = false;
    m_ownership_details_isValid = false;

    m_preferred_shares_outstanding_isSet = false;
    m_preferred_shares_outstanding_isValid = false;

    m_province_of_incorporation_isSet = false;
    m_province_of_incorporation_isValid = false;

    m_province_of_taxation_isSet = false;
    m_province_of_taxation_isValid = false;

    m_real_estate_assets_isSet = false;
    m_real_estate_assets_isValid = false;

    m_value_of_all_common_shares_isSet = false;
    m_value_of_all_common_shares_isValid = false;

    m_value_of_all_preferred_shares_isSet = false;
    m_value_of_all_preferred_shares_isValid = false;

    m_withdrawals_isSet = false;
    m_withdrawals_isValid = false;
}

void OAIIHoldingCompany::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIIHoldingCompany::fromJsonObject(QJsonObject json) {

    m_annual_dividend_yield_isValid = ::OpenAPI::fromJsonValue(m_annual_dividend_yield, json[QString("annualDividendYield")]);
    m_annual_dividend_yield_isSet = !json[QString("annualDividendYield")].isNull() && m_annual_dividend_yield_isValid;

    m_ccpc_isValid = ::OpenAPI::fromJsonValue(m_ccpc, json[QString("ccpc")]);
    m_ccpc_isSet = !json[QString("ccpc")].isNull() && m_ccpc_isValid;

    m_common_shares_outstanding_isValid = ::OpenAPI::fromJsonValue(m_common_shares_outstanding, json[QString("commonSharesOutstanding")]);
    m_common_shares_outstanding_isSet = !json[QString("commonSharesOutstanding")].isNull() && m_common_shares_outstanding_isValid;

    m_contributions_isValid = ::OpenAPI::fromJsonValue(m_contributions, json[QString("contributions")]);
    m_contributions_isSet = !json[QString("contributions")].isNull() && m_contributions_isValid;

    m_corporate_year_end_isValid = ::OpenAPI::fromJsonValue(m_corporate_year_end, json[QString("corporateYearEnd")]);
    m_corporate_year_end_isSet = !json[QString("corporateYearEnd")].isNull() && m_corporate_year_end_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_dividend_type_isValid = ::OpenAPI::fromJsonValue(m_dividend_type, json[QString("dividendType")]);
    m_dividend_type_isSet = !json[QString("dividendType")].isNull() && m_dividend_type_isValid;

    m_dividend_type_formatted_isValid = ::OpenAPI::fromJsonValue(m_dividend_type_formatted, json[QString("dividendTypeFormatted")]);
    m_dividend_type_formatted_isSet = !json[QString("dividendTypeFormatted")].isNull() && m_dividend_type_formatted_isValid;

    m_estate_details_isValid = ::OpenAPI::fromJsonValue(m_estate_details, json[QString("estateDetails")]);
    m_estate_details_isSet = !json[QString("estateDetails")].isNull() && m_estate_details_isValid;

    m_historical_data_isValid = ::OpenAPI::fromJsonValue(m_historical_data, json[QString("historicalData")]);
    m_historical_data_isSet = !json[QString("historicalData")].isNull() && m_historical_data_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_investment_accounts_isValid = ::OpenAPI::fromJsonValue(m_investment_accounts, json[QString("investmentAccounts")]);
    m_investment_accounts_isSet = !json[QString("investmentAccounts")].isNull() && m_investment_accounts_isValid;

    m_liabilities_isValid = ::OpenAPI::fromJsonValue(m_liabilities, json[QString("liabilities")]);
    m_liabilities_isSet = !json[QString("liabilities")].isNull() && m_liabilities_isValid;

    m_life_insurance_policies_isValid = ::OpenAPI::fromJsonValue(m_life_insurance_policies, json[QString("lifeInsurancePolicies")]);
    m_life_insurance_policies_isSet = !json[QString("lifeInsurancePolicies")].isNull() && m_life_insurance_policies_isValid;

    m_market_value_isValid = ::OpenAPI::fromJsonValue(m_market_value, json[QString("marketValue")]);
    m_market_value_isSet = !json[QString("marketValue")].isNull() && m_market_value_isValid;

    m_num_preferred_share_classes_isValid = ::OpenAPI::fromJsonValue(m_num_preferred_share_classes, json[QString("numPreferredShareClasses")]);
    m_num_preferred_share_classes_isSet = !json[QString("numPreferredShareClasses")].isNull() && m_num_preferred_share_classes_isValid;

    m_other_assets_isValid = ::OpenAPI::fromJsonValue(m_other_assets, json[QString("otherAssets")]);
    m_other_assets_isSet = !json[QString("otherAssets")].isNull() && m_other_assets_isValid;

    m_ownership_as_of_date_isValid = ::OpenAPI::fromJsonValue(m_ownership_as_of_date, json[QString("ownershipAsOfDate")]);
    m_ownership_as_of_date_isSet = !json[QString("ownershipAsOfDate")].isNull() && m_ownership_as_of_date_isValid;

    m_ownership_details_isValid = ::OpenAPI::fromJsonValue(m_ownership_details, json[QString("ownershipDetails")]);
    m_ownership_details_isSet = !json[QString("ownershipDetails")].isNull() && m_ownership_details_isValid;

    m_preferred_shares_outstanding_isValid = ::OpenAPI::fromJsonValue(m_preferred_shares_outstanding, json[QString("preferredSharesOutstanding")]);
    m_preferred_shares_outstanding_isSet = !json[QString("preferredSharesOutstanding")].isNull() && m_preferred_shares_outstanding_isValid;

    m_province_of_incorporation_isValid = ::OpenAPI::fromJsonValue(m_province_of_incorporation, json[QString("provinceOfIncorporation")]);
    m_province_of_incorporation_isSet = !json[QString("provinceOfIncorporation")].isNull() && m_province_of_incorporation_isValid;

    m_province_of_taxation_isValid = ::OpenAPI::fromJsonValue(m_province_of_taxation, json[QString("provinceOfTaxation")]);
    m_province_of_taxation_isSet = !json[QString("provinceOfTaxation")].isNull() && m_province_of_taxation_isValid;

    m_real_estate_assets_isValid = ::OpenAPI::fromJsonValue(m_real_estate_assets, json[QString("realEstateAssets")]);
    m_real_estate_assets_isSet = !json[QString("realEstateAssets")].isNull() && m_real_estate_assets_isValid;

    m_value_of_all_common_shares_isValid = ::OpenAPI::fromJsonValue(m_value_of_all_common_shares, json[QString("valueOfAllCommonShares")]);
    m_value_of_all_common_shares_isSet = !json[QString("valueOfAllCommonShares")].isNull() && m_value_of_all_common_shares_isValid;

    m_value_of_all_preferred_shares_isValid = ::OpenAPI::fromJsonValue(m_value_of_all_preferred_shares, json[QString("valueOfAllPreferredShares")]);
    m_value_of_all_preferred_shares_isSet = !json[QString("valueOfAllPreferredShares")].isNull() && m_value_of_all_preferred_shares_isValid;

    m_withdrawals_isValid = ::OpenAPI::fromJsonValue(m_withdrawals, json[QString("withdrawals")]);
    m_withdrawals_isSet = !json[QString("withdrawals")].isNull() && m_withdrawals_isValid;
}

QString OAIIHoldingCompany::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIIHoldingCompany::asJsonObject() const {
    QJsonObject obj;
    if (m_annual_dividend_yield.isSet()) {
        obj.insert(QString("annualDividendYield"), ::OpenAPI::toJsonValue(m_annual_dividend_yield));
    }
    if (m_ccpc.isSet()) {
        obj.insert(QString("ccpc"), ::OpenAPI::toJsonValue(m_ccpc));
    }
    if (m_common_shares_outstanding_isSet) {
        obj.insert(QString("commonSharesOutstanding"), ::OpenAPI::toJsonValue(m_common_shares_outstanding));
    }
    if (m_contributions.isSet()) {
        obj.insert(QString("contributions"), ::OpenAPI::toJsonValue(m_contributions));
    }
    if (m_corporate_year_end.isSet()) {
        obj.insert(QString("corporateYearEnd"), ::OpenAPI::toJsonValue(m_corporate_year_end));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_dividend_type_isSet) {
        obj.insert(QString("dividendType"), ::OpenAPI::toJsonValue(m_dividend_type));
    }
    if (m_dividend_type_formatted_isSet) {
        obj.insert(QString("dividendTypeFormatted"), ::OpenAPI::toJsonValue(m_dividend_type_formatted));
    }
    if (m_estate_details.isSet()) {
        obj.insert(QString("estateDetails"), ::OpenAPI::toJsonValue(m_estate_details));
    }
    if (m_historical_data.isSet()) {
        obj.insert(QString("historicalData"), ::OpenAPI::toJsonValue(m_historical_data));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_investment_accounts.size() > 0) {
        obj.insert(QString("investmentAccounts"), ::OpenAPI::toJsonValue(m_investment_accounts));
    }
    if (m_liabilities.size() > 0) {
        obj.insert(QString("liabilities"), ::OpenAPI::toJsonValue(m_liabilities));
    }
    if (m_life_insurance_policies.size() > 0) {
        obj.insert(QString("lifeInsurancePolicies"), ::OpenAPI::toJsonValue(m_life_insurance_policies));
    }
    if (m_market_value.isSet()) {
        obj.insert(QString("marketValue"), ::OpenAPI::toJsonValue(m_market_value));
    }
    if (m_num_preferred_share_classes_isSet) {
        obj.insert(QString("numPreferredShareClasses"), ::OpenAPI::toJsonValue(m_num_preferred_share_classes));
    }
    if (m_other_assets.size() > 0) {
        obj.insert(QString("otherAssets"), ::OpenAPI::toJsonValue(m_other_assets));
    }
    if (m_ownership_as_of_date.isSet()) {
        obj.insert(QString("ownershipAsOfDate"), ::OpenAPI::toJsonValue(m_ownership_as_of_date));
    }
    if (m_ownership_details.isSet()) {
        obj.insert(QString("ownershipDetails"), ::OpenAPI::toJsonValue(m_ownership_details));
    }
    if (m_preferred_shares_outstanding_isSet) {
        obj.insert(QString("preferredSharesOutstanding"), ::OpenAPI::toJsonValue(m_preferred_shares_outstanding));
    }
    if (m_province_of_incorporation_isSet) {
        obj.insert(QString("provinceOfIncorporation"), ::OpenAPI::toJsonValue(m_province_of_incorporation));
    }
    if (m_province_of_taxation_isSet) {
        obj.insert(QString("provinceOfTaxation"), ::OpenAPI::toJsonValue(m_province_of_taxation));
    }
    if (m_real_estate_assets.size() > 0) {
        obj.insert(QString("realEstateAssets"), ::OpenAPI::toJsonValue(m_real_estate_assets));
    }
    if (m_value_of_all_common_shares.isSet()) {
        obj.insert(QString("valueOfAllCommonShares"), ::OpenAPI::toJsonValue(m_value_of_all_common_shares));
    }
    if (m_value_of_all_preferred_shares.isSet()) {
        obj.insert(QString("valueOfAllPreferredShares"), ::OpenAPI::toJsonValue(m_value_of_all_preferred_shares));
    }
    if (m_withdrawals.isSet()) {
        obj.insert(QString("withdrawals"), ::OpenAPI::toJsonValue(m_withdrawals));
    }
    return obj;
}

OAIPercent OAIIHoldingCompany::getAnnualDividendYield() const {
    return m_annual_dividend_yield;
}
void OAIIHoldingCompany::setAnnualDividendYield(const OAIPercent &annual_dividend_yield) {
    m_annual_dividend_yield = annual_dividend_yield;
    m_annual_dividend_yield_isSet = true;
}

bool OAIIHoldingCompany::is_annual_dividend_yield_Set() const{
    return m_annual_dividend_yield_isSet;
}

bool OAIIHoldingCompany::is_annual_dividend_yield_Valid() const{
    return m_annual_dividend_yield_isValid;
}

OAIDescriptiveBoolean OAIIHoldingCompany::getCcpc() const {
    return m_ccpc;
}
void OAIIHoldingCompany::setCcpc(const OAIDescriptiveBoolean &ccpc) {
    m_ccpc = ccpc;
    m_ccpc_isSet = true;
}

bool OAIIHoldingCompany::is_ccpc_Set() const{
    return m_ccpc_isSet;
}

bool OAIIHoldingCompany::is_ccpc_Valid() const{
    return m_ccpc_isValid;
}

qint32 OAIIHoldingCompany::getCommonSharesOutstanding() const {
    return m_common_shares_outstanding;
}
void OAIIHoldingCompany::setCommonSharesOutstanding(const qint32 &common_shares_outstanding) {
    m_common_shares_outstanding = common_shares_outstanding;
    m_common_shares_outstanding_isSet = true;
}

bool OAIIHoldingCompany::is_common_shares_outstanding_Set() const{
    return m_common_shares_outstanding_isSet;
}

bool OAIIHoldingCompany::is_common_shares_outstanding_Valid() const{
    return m_common_shares_outstanding_isValid;
}

OAIIContributions OAIIHoldingCompany::getContributions() const {
    return m_contributions;
}
void OAIIHoldingCompany::setContributions(const OAIIContributions &contributions) {
    m_contributions = contributions;
    m_contributions_isSet = true;
}

bool OAIIHoldingCompany::is_contributions_Set() const{
    return m_contributions_isSet;
}

bool OAIIHoldingCompany::is_contributions_Valid() const{
    return m_contributions_isValid;
}

OAIDate OAIIHoldingCompany::getCorporateYearEnd() const {
    return m_corporate_year_end;
}
void OAIIHoldingCompany::setCorporateYearEnd(const OAIDate &corporate_year_end) {
    m_corporate_year_end = corporate_year_end;
    m_corporate_year_end_isSet = true;
}

bool OAIIHoldingCompany::is_corporate_year_end_Set() const{
    return m_corporate_year_end_isSet;
}

bool OAIIHoldingCompany::is_corporate_year_end_Valid() const{
    return m_corporate_year_end_isValid;
}

QString OAIIHoldingCompany::getDescription() const {
    return m_description;
}
void OAIIHoldingCompany::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIIHoldingCompany::is_description_Set() const{
    return m_description_isSet;
}

bool OAIIHoldingCompany::is_description_Valid() const{
    return m_description_isValid;
}

QString OAIIHoldingCompany::getDividendType() const {
    return m_dividend_type;
}
void OAIIHoldingCompany::setDividendType(const QString &dividend_type) {
    m_dividend_type = dividend_type;
    m_dividend_type_isSet = true;
}

bool OAIIHoldingCompany::is_dividend_type_Set() const{
    return m_dividend_type_isSet;
}

bool OAIIHoldingCompany::is_dividend_type_Valid() const{
    return m_dividend_type_isValid;
}

QString OAIIHoldingCompany::getDividendTypeFormatted() const {
    return m_dividend_type_formatted;
}
void OAIIHoldingCompany::setDividendTypeFormatted(const QString &dividend_type_formatted) {
    m_dividend_type_formatted = dividend_type_formatted;
    m_dividend_type_formatted_isSet = true;
}

bool OAIIHoldingCompany::is_dividend_type_formatted_Set() const{
    return m_dividend_type_formatted_isSet;
}

bool OAIIHoldingCompany::is_dividend_type_formatted_Valid() const{
    return m_dividend_type_formatted_isValid;
}

OAIIEstateDetails OAIIHoldingCompany::getEstateDetails() const {
    return m_estate_details;
}
void OAIIHoldingCompany::setEstateDetails(const OAIIEstateDetails &estate_details) {
    m_estate_details = estate_details;
    m_estate_details_isSet = true;
}

bool OAIIHoldingCompany::is_estate_details_Set() const{
    return m_estate_details_isSet;
}

bool OAIIHoldingCompany::is_estate_details_Valid() const{
    return m_estate_details_isValid;
}

OAIIHistoricalData OAIIHoldingCompany::getHistoricalData() const {
    return m_historical_data;
}
void OAIIHoldingCompany::setHistoricalData(const OAIIHistoricalData &historical_data) {
    m_historical_data = historical_data;
    m_historical_data_isSet = true;
}

bool OAIIHoldingCompany::is_historical_data_Set() const{
    return m_historical_data_isSet;
}

bool OAIIHoldingCompany::is_historical_data_Valid() const{
    return m_historical_data_isValid;
}

QString OAIIHoldingCompany::getId() const {
    return m_id;
}
void OAIIHoldingCompany::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIIHoldingCompany::is_id_Set() const{
    return m_id_isSet;
}

bool OAIIHoldingCompany::is_id_Valid() const{
    return m_id_isValid;
}

QList<OAIIInvestmentAccount> OAIIHoldingCompany::getInvestmentAccounts() const {
    return m_investment_accounts;
}
void OAIIHoldingCompany::setInvestmentAccounts(const QList<OAIIInvestmentAccount> &investment_accounts) {
    m_investment_accounts = investment_accounts;
    m_investment_accounts_isSet = true;
}

bool OAIIHoldingCompany::is_investment_accounts_Set() const{
    return m_investment_accounts_isSet;
}

bool OAIIHoldingCompany::is_investment_accounts_Valid() const{
    return m_investment_accounts_isValid;
}

QList<OAIILiability> OAIIHoldingCompany::getLiabilities() const {
    return m_liabilities;
}
void OAIIHoldingCompany::setLiabilities(const QList<OAIILiability> &liabilities) {
    m_liabilities = liabilities;
    m_liabilities_isSet = true;
}

bool OAIIHoldingCompany::is_liabilities_Set() const{
    return m_liabilities_isSet;
}

bool OAIIHoldingCompany::is_liabilities_Valid() const{
    return m_liabilities_isValid;
}

QList<OAIILifeInsurancePolicy> OAIIHoldingCompany::getLifeInsurancePolicies() const {
    return m_life_insurance_policies;
}
void OAIIHoldingCompany::setLifeInsurancePolicies(const QList<OAIILifeInsurancePolicy> &life_insurance_policies) {
    m_life_insurance_policies = life_insurance_policies;
    m_life_insurance_policies_isSet = true;
}

bool OAIIHoldingCompany::is_life_insurance_policies_Set() const{
    return m_life_insurance_policies_isSet;
}

bool OAIIHoldingCompany::is_life_insurance_policies_Valid() const{
    return m_life_insurance_policies_isValid;
}

OAICurrency OAIIHoldingCompany::getMarketValue() const {
    return m_market_value;
}
void OAIIHoldingCompany::setMarketValue(const OAICurrency &market_value) {
    m_market_value = market_value;
    m_market_value_isSet = true;
}

bool OAIIHoldingCompany::is_market_value_Set() const{
    return m_market_value_isSet;
}

bool OAIIHoldingCompany::is_market_value_Valid() const{
    return m_market_value_isValid;
}

qint32 OAIIHoldingCompany::getNumPreferredShareClasses() const {
    return m_num_preferred_share_classes;
}
void OAIIHoldingCompany::setNumPreferredShareClasses(const qint32 &num_preferred_share_classes) {
    m_num_preferred_share_classes = num_preferred_share_classes;
    m_num_preferred_share_classes_isSet = true;
}

bool OAIIHoldingCompany::is_num_preferred_share_classes_Set() const{
    return m_num_preferred_share_classes_isSet;
}

bool OAIIHoldingCompany::is_num_preferred_share_classes_Valid() const{
    return m_num_preferred_share_classes_isValid;
}

QList<OAIIRealEstateAsset> OAIIHoldingCompany::getOtherAssets() const {
    return m_other_assets;
}
void OAIIHoldingCompany::setOtherAssets(const QList<OAIIRealEstateAsset> &other_assets) {
    m_other_assets = other_assets;
    m_other_assets_isSet = true;
}

bool OAIIHoldingCompany::is_other_assets_Set() const{
    return m_other_assets_isSet;
}

bool OAIIHoldingCompany::is_other_assets_Valid() const{
    return m_other_assets_isValid;
}

OAIDate OAIIHoldingCompany::getOwnershipAsOfDate() const {
    return m_ownership_as_of_date;
}
void OAIIHoldingCompany::setOwnershipAsOfDate(const OAIDate &ownership_as_of_date) {
    m_ownership_as_of_date = ownership_as_of_date;
    m_ownership_as_of_date_isSet = true;
}

bool OAIIHoldingCompany::is_ownership_as_of_date_Set() const{
    return m_ownership_as_of_date_isSet;
}

bool OAIIHoldingCompany::is_ownership_as_of_date_Valid() const{
    return m_ownership_as_of_date_isValid;
}

OAIIOwnershipDetails OAIIHoldingCompany::getOwnershipDetails() const {
    return m_ownership_details;
}
void OAIIHoldingCompany::setOwnershipDetails(const OAIIOwnershipDetails &ownership_details) {
    m_ownership_details = ownership_details;
    m_ownership_details_isSet = true;
}

bool OAIIHoldingCompany::is_ownership_details_Set() const{
    return m_ownership_details_isSet;
}

bool OAIIHoldingCompany::is_ownership_details_Valid() const{
    return m_ownership_details_isValid;
}

qint32 OAIIHoldingCompany::getPreferredSharesOutstanding() const {
    return m_preferred_shares_outstanding;
}
void OAIIHoldingCompany::setPreferredSharesOutstanding(const qint32 &preferred_shares_outstanding) {
    m_preferred_shares_outstanding = preferred_shares_outstanding;
    m_preferred_shares_outstanding_isSet = true;
}

bool OAIIHoldingCompany::is_preferred_shares_outstanding_Set() const{
    return m_preferred_shares_outstanding_isSet;
}

bool OAIIHoldingCompany::is_preferred_shares_outstanding_Valid() const{
    return m_preferred_shares_outstanding_isValid;
}

QString OAIIHoldingCompany::getProvinceOfIncorporation() const {
    return m_province_of_incorporation;
}
void OAIIHoldingCompany::setProvinceOfIncorporation(const QString &province_of_incorporation) {
    m_province_of_incorporation = province_of_incorporation;
    m_province_of_incorporation_isSet = true;
}

bool OAIIHoldingCompany::is_province_of_incorporation_Set() const{
    return m_province_of_incorporation_isSet;
}

bool OAIIHoldingCompany::is_province_of_incorporation_Valid() const{
    return m_province_of_incorporation_isValid;
}

QString OAIIHoldingCompany::getProvinceOfTaxation() const {
    return m_province_of_taxation;
}
void OAIIHoldingCompany::setProvinceOfTaxation(const QString &province_of_taxation) {
    m_province_of_taxation = province_of_taxation;
    m_province_of_taxation_isSet = true;
}

bool OAIIHoldingCompany::is_province_of_taxation_Set() const{
    return m_province_of_taxation_isSet;
}

bool OAIIHoldingCompany::is_province_of_taxation_Valid() const{
    return m_province_of_taxation_isValid;
}

QList<OAIICorporationRealEstateAsset> OAIIHoldingCompany::getRealEstateAssets() const {
    return m_real_estate_assets;
}
void OAIIHoldingCompany::setRealEstateAssets(const QList<OAIICorporationRealEstateAsset> &real_estate_assets) {
    m_real_estate_assets = real_estate_assets;
    m_real_estate_assets_isSet = true;
}

bool OAIIHoldingCompany::is_real_estate_assets_Set() const{
    return m_real_estate_assets_isSet;
}

bool OAIIHoldingCompany::is_real_estate_assets_Valid() const{
    return m_real_estate_assets_isValid;
}

OAICurrency OAIIHoldingCompany::getValueOfAllCommonShares() const {
    return m_value_of_all_common_shares;
}
void OAIIHoldingCompany::setValueOfAllCommonShares(const OAICurrency &value_of_all_common_shares) {
    m_value_of_all_common_shares = value_of_all_common_shares;
    m_value_of_all_common_shares_isSet = true;
}

bool OAIIHoldingCompany::is_value_of_all_common_shares_Set() const{
    return m_value_of_all_common_shares_isSet;
}

bool OAIIHoldingCompany::is_value_of_all_common_shares_Valid() const{
    return m_value_of_all_common_shares_isValid;
}

OAICurrency OAIIHoldingCompany::getValueOfAllPreferredShares() const {
    return m_value_of_all_preferred_shares;
}
void OAIIHoldingCompany::setValueOfAllPreferredShares(const OAICurrency &value_of_all_preferred_shares) {
    m_value_of_all_preferred_shares = value_of_all_preferred_shares;
    m_value_of_all_preferred_shares_isSet = true;
}

bool OAIIHoldingCompany::is_value_of_all_preferred_shares_Set() const{
    return m_value_of_all_preferred_shares_isSet;
}

bool OAIIHoldingCompany::is_value_of_all_preferred_shares_Valid() const{
    return m_value_of_all_preferred_shares_isValid;
}

OAIIWithdrawals OAIIHoldingCompany::getWithdrawals() const {
    return m_withdrawals;
}
void OAIIHoldingCompany::setWithdrawals(const OAIIWithdrawals &withdrawals) {
    m_withdrawals = withdrawals;
    m_withdrawals_isSet = true;
}

bool OAIIHoldingCompany::is_withdrawals_Set() const{
    return m_withdrawals_isSet;
}

bool OAIIHoldingCompany::is_withdrawals_Valid() const{
    return m_withdrawals_isValid;
}

bool OAIIHoldingCompany::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_annual_dividend_yield.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_ccpc.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_common_shares_outstanding_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_contributions.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_corporate_year_end.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_dividend_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_dividend_type_formatted_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_estate_details.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_historical_data.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_investment_accounts.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_liabilities.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_life_insurance_policies.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_market_value.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_num_preferred_share_classes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_other_assets.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_ownership_as_of_date.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_ownership_details.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_preferred_shares_outstanding_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_province_of_incorporation_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_province_of_taxation_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_real_estate_assets.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_value_of_all_common_shares.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_value_of_all_preferred_shares.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_withdrawals.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIIHoldingCompany::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
