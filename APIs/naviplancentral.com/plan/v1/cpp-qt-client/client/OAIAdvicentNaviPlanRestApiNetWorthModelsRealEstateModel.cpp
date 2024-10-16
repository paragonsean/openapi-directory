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

#include "OAIAdvicentNaviPlanRestApiNetWorthModelsRealEstateModel.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAdvicentNaviPlanRestApiNetWorthModelsRealEstateModel::OAIAdvicentNaviPlanRestApiNetWorthModelsRealEstateModel(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAdvicentNaviPlanRestApiNetWorthModelsRealEstateModel::OAIAdvicentNaviPlanRestApiNetWorthModelsRealEstateModel() {
    this->initializeModel();
}

OAIAdvicentNaviPlanRestApiNetWorthModelsRealEstateModel::~OAIAdvicentNaviPlanRestApiNetWorthModelsRealEstateModel() {}

void OAIAdvicentNaviPlanRestApiNetWorthModelsRealEstateModel::initializeModel() {

    m_description_isSet = false;
    m_description_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_legacy_id_isSet = false;
    m_legacy_id_isValid = false;

    m_market_value_isSet = false;
    m_market_value_isValid = false;

    m_owner_isSet = false;
    m_owner_isValid = false;

    m_purchase_amount_isSet = false;
    m_purchase_amount_isValid = false;

    m_purchase_date_isSet = false;
    m_purchase_date_isValid = false;

    m_valuation_date_isSet = false;
    m_valuation_date_isValid = false;
}

void OAIAdvicentNaviPlanRestApiNetWorthModelsRealEstateModel::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAdvicentNaviPlanRestApiNetWorthModelsRealEstateModel::fromJsonObject(QJsonObject json) {

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_legacy_id_isValid = ::OpenAPI::fromJsonValue(m_legacy_id, json[QString("legacyId")]);
    m_legacy_id_isSet = !json[QString("legacyId")].isNull() && m_legacy_id_isValid;

    m_market_value_isValid = ::OpenAPI::fromJsonValue(m_market_value, json[QString("marketValue")]);
    m_market_value_isSet = !json[QString("marketValue")].isNull() && m_market_value_isValid;

    m_owner_isValid = ::OpenAPI::fromJsonValue(m_owner, json[QString("owner")]);
    m_owner_isSet = !json[QString("owner")].isNull() && m_owner_isValid;

    m_purchase_amount_isValid = ::OpenAPI::fromJsonValue(m_purchase_amount, json[QString("purchaseAmount")]);
    m_purchase_amount_isSet = !json[QString("purchaseAmount")].isNull() && m_purchase_amount_isValid;

    m_purchase_date_isValid = ::OpenAPI::fromJsonValue(m_purchase_date, json[QString("purchaseDate")]);
    m_purchase_date_isSet = !json[QString("purchaseDate")].isNull() && m_purchase_date_isValid;

    m_valuation_date_isValid = ::OpenAPI::fromJsonValue(m_valuation_date, json[QString("valuationDate")]);
    m_valuation_date_isSet = !json[QString("valuationDate")].isNull() && m_valuation_date_isValid;
}

QString OAIAdvicentNaviPlanRestApiNetWorthModelsRealEstateModel::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAdvicentNaviPlanRestApiNetWorthModelsRealEstateModel::asJsonObject() const {
    QJsonObject obj;
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_legacy_id_isSet) {
        obj.insert(QString("legacyId"), ::OpenAPI::toJsonValue(m_legacy_id));
    }
    if (m_market_value_isSet) {
        obj.insert(QString("marketValue"), ::OpenAPI::toJsonValue(m_market_value));
    }
    if (m_owner.isSet()) {
        obj.insert(QString("owner"), ::OpenAPI::toJsonValue(m_owner));
    }
    if (m_purchase_amount_isSet) {
        obj.insert(QString("purchaseAmount"), ::OpenAPI::toJsonValue(m_purchase_amount));
    }
    if (m_purchase_date_isSet) {
        obj.insert(QString("purchaseDate"), ::OpenAPI::toJsonValue(m_purchase_date));
    }
    if (m_valuation_date_isSet) {
        obj.insert(QString("valuationDate"), ::OpenAPI::toJsonValue(m_valuation_date));
    }
    return obj;
}

QString OAIAdvicentNaviPlanRestApiNetWorthModelsRealEstateModel::getDescription() const {
    return m_description;
}
void OAIAdvicentNaviPlanRestApiNetWorthModelsRealEstateModel::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIAdvicentNaviPlanRestApiNetWorthModelsRealEstateModel::is_description_Set() const{
    return m_description_isSet;
}

bool OAIAdvicentNaviPlanRestApiNetWorthModelsRealEstateModel::is_description_Valid() const{
    return m_description_isValid;
}

qint32 OAIAdvicentNaviPlanRestApiNetWorthModelsRealEstateModel::getId() const {
    return m_id;
}
void OAIAdvicentNaviPlanRestApiNetWorthModelsRealEstateModel::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIAdvicentNaviPlanRestApiNetWorthModelsRealEstateModel::is_id_Set() const{
    return m_id_isSet;
}

bool OAIAdvicentNaviPlanRestApiNetWorthModelsRealEstateModel::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIAdvicentNaviPlanRestApiNetWorthModelsRealEstateModel::getLegacyId() const {
    return m_legacy_id;
}
void OAIAdvicentNaviPlanRestApiNetWorthModelsRealEstateModel::setLegacyId(const QString &legacy_id) {
    m_legacy_id = legacy_id;
    m_legacy_id_isSet = true;
}

bool OAIAdvicentNaviPlanRestApiNetWorthModelsRealEstateModel::is_legacy_id_Set() const{
    return m_legacy_id_isSet;
}

bool OAIAdvicentNaviPlanRestApiNetWorthModelsRealEstateModel::is_legacy_id_Valid() const{
    return m_legacy_id_isValid;
}

double OAIAdvicentNaviPlanRestApiNetWorthModelsRealEstateModel::getMarketValue() const {
    return m_market_value;
}
void OAIAdvicentNaviPlanRestApiNetWorthModelsRealEstateModel::setMarketValue(const double &market_value) {
    m_market_value = market_value;
    m_market_value_isSet = true;
}

bool OAIAdvicentNaviPlanRestApiNetWorthModelsRealEstateModel::is_market_value_Set() const{
    return m_market_value_isSet;
}

bool OAIAdvicentNaviPlanRestApiNetWorthModelsRealEstateModel::is_market_value_Valid() const{
    return m_market_value_isValid;
}

OAIAdvicentNaviPlanRestApiModelsOwnerModel OAIAdvicentNaviPlanRestApiNetWorthModelsRealEstateModel::getOwner() const {
    return m_owner;
}
void OAIAdvicentNaviPlanRestApiNetWorthModelsRealEstateModel::setOwner(const OAIAdvicentNaviPlanRestApiModelsOwnerModel &owner) {
    m_owner = owner;
    m_owner_isSet = true;
}

bool OAIAdvicentNaviPlanRestApiNetWorthModelsRealEstateModel::is_owner_Set() const{
    return m_owner_isSet;
}

bool OAIAdvicentNaviPlanRestApiNetWorthModelsRealEstateModel::is_owner_Valid() const{
    return m_owner_isValid;
}

double OAIAdvicentNaviPlanRestApiNetWorthModelsRealEstateModel::getPurchaseAmount() const {
    return m_purchase_amount;
}
void OAIAdvicentNaviPlanRestApiNetWorthModelsRealEstateModel::setPurchaseAmount(const double &purchase_amount) {
    m_purchase_amount = purchase_amount;
    m_purchase_amount_isSet = true;
}

bool OAIAdvicentNaviPlanRestApiNetWorthModelsRealEstateModel::is_purchase_amount_Set() const{
    return m_purchase_amount_isSet;
}

bool OAIAdvicentNaviPlanRestApiNetWorthModelsRealEstateModel::is_purchase_amount_Valid() const{
    return m_purchase_amount_isValid;
}

QDateTime OAIAdvicentNaviPlanRestApiNetWorthModelsRealEstateModel::getPurchaseDate() const {
    return m_purchase_date;
}
void OAIAdvicentNaviPlanRestApiNetWorthModelsRealEstateModel::setPurchaseDate(const QDateTime &purchase_date) {
    m_purchase_date = purchase_date;
    m_purchase_date_isSet = true;
}

bool OAIAdvicentNaviPlanRestApiNetWorthModelsRealEstateModel::is_purchase_date_Set() const{
    return m_purchase_date_isSet;
}

bool OAIAdvicentNaviPlanRestApiNetWorthModelsRealEstateModel::is_purchase_date_Valid() const{
    return m_purchase_date_isValid;
}

QDateTime OAIAdvicentNaviPlanRestApiNetWorthModelsRealEstateModel::getValuationDate() const {
    return m_valuation_date;
}
void OAIAdvicentNaviPlanRestApiNetWorthModelsRealEstateModel::setValuationDate(const QDateTime &valuation_date) {
    m_valuation_date = valuation_date;
    m_valuation_date_isSet = true;
}

bool OAIAdvicentNaviPlanRestApiNetWorthModelsRealEstateModel::is_valuation_date_Set() const{
    return m_valuation_date_isSet;
}

bool OAIAdvicentNaviPlanRestApiNetWorthModelsRealEstateModel::is_valuation_date_Valid() const{
    return m_valuation_date_isValid;
}

bool OAIAdvicentNaviPlanRestApiNetWorthModelsRealEstateModel::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_legacy_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_market_value_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_owner.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_purchase_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_purchase_date_isSet) {
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

bool OAIAdvicentNaviPlanRestApiNetWorthModelsRealEstateModel::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
