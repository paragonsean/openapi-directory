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

#include "OAILifeInsurancePolicySubaccountDomainObject.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAILifeInsurancePolicySubaccountDomainObject::OAILifeInsurancePolicySubaccountDomainObject(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAILifeInsurancePolicySubaccountDomainObject::OAILifeInsurancePolicySubaccountDomainObject() {
    this->initializeModel();
}

OAILifeInsurancePolicySubaccountDomainObject::~OAILifeInsurancePolicySubaccountDomainObject() {}

void OAILifeInsurancePolicySubaccountDomainObject::initializeModel() {

    m_description_isSet = false;
    m_description_isValid = false;

    m_external_destination_id_isSet = false;
    m_external_destination_id_isValid = false;

    m_life_insurance_policy_id_isSet = false;
    m_life_insurance_policy_id_isValid = false;

    m_life_insurance_policy_subaccount_id_isSet = false;
    m_life_insurance_policy_subaccount_id_isValid = false;

    m_market_value_isSet = false;
    m_market_value_isValid = false;

    m_symbol_isSet = false;
    m_symbol_isValid = false;
}

void OAILifeInsurancePolicySubaccountDomainObject::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAILifeInsurancePolicySubaccountDomainObject::fromJsonObject(QJsonObject json) {

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_external_destination_id_isValid = ::OpenAPI::fromJsonValue(m_external_destination_id, json[QString("externalDestinationId")]);
    m_external_destination_id_isSet = !json[QString("externalDestinationId")].isNull() && m_external_destination_id_isValid;

    m_life_insurance_policy_id_isValid = ::OpenAPI::fromJsonValue(m_life_insurance_policy_id, json[QString("lifeInsurancePolicyId")]);
    m_life_insurance_policy_id_isSet = !json[QString("lifeInsurancePolicyId")].isNull() && m_life_insurance_policy_id_isValid;

    m_life_insurance_policy_subaccount_id_isValid = ::OpenAPI::fromJsonValue(m_life_insurance_policy_subaccount_id, json[QString("lifeInsurancePolicySubaccountId")]);
    m_life_insurance_policy_subaccount_id_isSet = !json[QString("lifeInsurancePolicySubaccountId")].isNull() && m_life_insurance_policy_subaccount_id_isValid;

    m_market_value_isValid = ::OpenAPI::fromJsonValue(m_market_value, json[QString("marketValue")]);
    m_market_value_isSet = !json[QString("marketValue")].isNull() && m_market_value_isValid;

    m_symbol_isValid = ::OpenAPI::fromJsonValue(m_symbol, json[QString("symbol")]);
    m_symbol_isSet = !json[QString("symbol")].isNull() && m_symbol_isValid;
}

QString OAILifeInsurancePolicySubaccountDomainObject::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAILifeInsurancePolicySubaccountDomainObject::asJsonObject() const {
    QJsonObject obj;
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_external_destination_id_isSet) {
        obj.insert(QString("externalDestinationId"), ::OpenAPI::toJsonValue(m_external_destination_id));
    }
    if (m_life_insurance_policy_id_isSet) {
        obj.insert(QString("lifeInsurancePolicyId"), ::OpenAPI::toJsonValue(m_life_insurance_policy_id));
    }
    if (m_life_insurance_policy_subaccount_id_isSet) {
        obj.insert(QString("lifeInsurancePolicySubaccountId"), ::OpenAPI::toJsonValue(m_life_insurance_policy_subaccount_id));
    }
    if (m_market_value_isSet) {
        obj.insert(QString("marketValue"), ::OpenAPI::toJsonValue(m_market_value));
    }
    if (m_symbol_isSet) {
        obj.insert(QString("symbol"), ::OpenAPI::toJsonValue(m_symbol));
    }
    return obj;
}

QString OAILifeInsurancePolicySubaccountDomainObject::getDescription() const {
    return m_description;
}
void OAILifeInsurancePolicySubaccountDomainObject::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAILifeInsurancePolicySubaccountDomainObject::is_description_Set() const{
    return m_description_isSet;
}

bool OAILifeInsurancePolicySubaccountDomainObject::is_description_Valid() const{
    return m_description_isValid;
}

QString OAILifeInsurancePolicySubaccountDomainObject::getExternalDestinationId() const {
    return m_external_destination_id;
}
void OAILifeInsurancePolicySubaccountDomainObject::setExternalDestinationId(const QString &external_destination_id) {
    m_external_destination_id = external_destination_id;
    m_external_destination_id_isSet = true;
}

bool OAILifeInsurancePolicySubaccountDomainObject::is_external_destination_id_Set() const{
    return m_external_destination_id_isSet;
}

bool OAILifeInsurancePolicySubaccountDomainObject::is_external_destination_id_Valid() const{
    return m_external_destination_id_isValid;
}

qint32 OAILifeInsurancePolicySubaccountDomainObject::getLifeInsurancePolicyId() const {
    return m_life_insurance_policy_id;
}
void OAILifeInsurancePolicySubaccountDomainObject::setLifeInsurancePolicyId(const qint32 &life_insurance_policy_id) {
    m_life_insurance_policy_id = life_insurance_policy_id;
    m_life_insurance_policy_id_isSet = true;
}

bool OAILifeInsurancePolicySubaccountDomainObject::is_life_insurance_policy_id_Set() const{
    return m_life_insurance_policy_id_isSet;
}

bool OAILifeInsurancePolicySubaccountDomainObject::is_life_insurance_policy_id_Valid() const{
    return m_life_insurance_policy_id_isValid;
}

qint32 OAILifeInsurancePolicySubaccountDomainObject::getLifeInsurancePolicySubaccountId() const {
    return m_life_insurance_policy_subaccount_id;
}
void OAILifeInsurancePolicySubaccountDomainObject::setLifeInsurancePolicySubaccountId(const qint32 &life_insurance_policy_subaccount_id) {
    m_life_insurance_policy_subaccount_id = life_insurance_policy_subaccount_id;
    m_life_insurance_policy_subaccount_id_isSet = true;
}

bool OAILifeInsurancePolicySubaccountDomainObject::is_life_insurance_policy_subaccount_id_Set() const{
    return m_life_insurance_policy_subaccount_id_isSet;
}

bool OAILifeInsurancePolicySubaccountDomainObject::is_life_insurance_policy_subaccount_id_Valid() const{
    return m_life_insurance_policy_subaccount_id_isValid;
}

double OAILifeInsurancePolicySubaccountDomainObject::getMarketValue() const {
    return m_market_value;
}
void OAILifeInsurancePolicySubaccountDomainObject::setMarketValue(const double &market_value) {
    m_market_value = market_value;
    m_market_value_isSet = true;
}

bool OAILifeInsurancePolicySubaccountDomainObject::is_market_value_Set() const{
    return m_market_value_isSet;
}

bool OAILifeInsurancePolicySubaccountDomainObject::is_market_value_Valid() const{
    return m_market_value_isValid;
}

QString OAILifeInsurancePolicySubaccountDomainObject::getSymbol() const {
    return m_symbol;
}
void OAILifeInsurancePolicySubaccountDomainObject::setSymbol(const QString &symbol) {
    m_symbol = symbol;
    m_symbol_isSet = true;
}

bool OAILifeInsurancePolicySubaccountDomainObject::is_symbol_Set() const{
    return m_symbol_isSet;
}

bool OAILifeInsurancePolicySubaccountDomainObject::is_symbol_Valid() const{
    return m_symbol_isValid;
}

bool OAILifeInsurancePolicySubaccountDomainObject::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_external_destination_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_life_insurance_policy_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_life_insurance_policy_subaccount_id_isSet) {
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
    } while (false);
    return isObjectUpdated;
}

bool OAILifeInsurancePolicySubaccountDomainObject::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
