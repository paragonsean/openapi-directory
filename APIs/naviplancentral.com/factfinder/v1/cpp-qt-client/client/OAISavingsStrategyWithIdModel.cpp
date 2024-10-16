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

#include "OAISavingsStrategyWithIdModel.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISavingsStrategyWithIdModel::OAISavingsStrategyWithIdModel(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISavingsStrategyWithIdModel::OAISavingsStrategyWithIdModel() {
    this->initializeModel();
}

OAISavingsStrategyWithIdModel::~OAISavingsStrategyWithIdModel() {}

void OAISavingsStrategyWithIdModel::initializeModel() {

    m_account_id_isSet = false;
    m_account_id_isValid = false;

    m_employer_savings_amount_isSet = false;
    m_employer_savings_amount_isValid = false;

    m_employer_savings_amount_type_isSet = false;
    m_employer_savings_amount_type_isValid = false;

    m_end_date_isSet = false;
    m_end_date_isValid = false;

    m_external_destination_id_isSet = false;
    m_external_destination_id_isValid = false;

    m_frequency_id_isSet = false;
    m_frequency_id_isValid = false;

    m_mandatory_amount_isSet = false;
    m_mandatory_amount_isValid = false;

    m_mandatory_amount_type_isSet = false;
    m_mandatory_amount_type_isValid = false;

    m_post_tax_savings_amount_isSet = false;
    m_post_tax_savings_amount_isValid = false;

    m_post_tax_savings_amount_type_isSet = false;
    m_post_tax_savings_amount_type_isValid = false;

    m_pre_tax_savings_amount_isSet = false;
    m_pre_tax_savings_amount_isValid = false;

    m_pre_tax_savings_amount_type_isSet = false;
    m_pre_tax_savings_amount_type_isValid = false;

    m_savings_strategy_id_isSet = false;
    m_savings_strategy_id_isValid = false;

    m_start_date_isSet = false;
    m_start_date_isValid = false;
}

void OAISavingsStrategyWithIdModel::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISavingsStrategyWithIdModel::fromJsonObject(QJsonObject json) {

    m_account_id_isValid = ::OpenAPI::fromJsonValue(m_account_id, json[QString("accountId")]);
    m_account_id_isSet = !json[QString("accountId")].isNull() && m_account_id_isValid;

    m_employer_savings_amount_isValid = ::OpenAPI::fromJsonValue(m_employer_savings_amount, json[QString("employerSavingsAmount")]);
    m_employer_savings_amount_isSet = !json[QString("employerSavingsAmount")].isNull() && m_employer_savings_amount_isValid;

    m_employer_savings_amount_type_isValid = ::OpenAPI::fromJsonValue(m_employer_savings_amount_type, json[QString("employerSavingsAmountType")]);
    m_employer_savings_amount_type_isSet = !json[QString("employerSavingsAmountType")].isNull() && m_employer_savings_amount_type_isValid;

    m_end_date_isValid = ::OpenAPI::fromJsonValue(m_end_date, json[QString("endDate")]);
    m_end_date_isSet = !json[QString("endDate")].isNull() && m_end_date_isValid;

    m_external_destination_id_isValid = ::OpenAPI::fromJsonValue(m_external_destination_id, json[QString("externalDestinationId")]);
    m_external_destination_id_isSet = !json[QString("externalDestinationId")].isNull() && m_external_destination_id_isValid;

    m_frequency_id_isValid = ::OpenAPI::fromJsonValue(m_frequency_id, json[QString("frequencyId")]);
    m_frequency_id_isSet = !json[QString("frequencyId")].isNull() && m_frequency_id_isValid;

    m_mandatory_amount_isValid = ::OpenAPI::fromJsonValue(m_mandatory_amount, json[QString("mandatoryAmount")]);
    m_mandatory_amount_isSet = !json[QString("mandatoryAmount")].isNull() && m_mandatory_amount_isValid;

    m_mandatory_amount_type_isValid = ::OpenAPI::fromJsonValue(m_mandatory_amount_type, json[QString("mandatoryAmountType")]);
    m_mandatory_amount_type_isSet = !json[QString("mandatoryAmountType")].isNull() && m_mandatory_amount_type_isValid;

    m_post_tax_savings_amount_isValid = ::OpenAPI::fromJsonValue(m_post_tax_savings_amount, json[QString("postTaxSavingsAmount")]);
    m_post_tax_savings_amount_isSet = !json[QString("postTaxSavingsAmount")].isNull() && m_post_tax_savings_amount_isValid;

    m_post_tax_savings_amount_type_isValid = ::OpenAPI::fromJsonValue(m_post_tax_savings_amount_type, json[QString("postTaxSavingsAmountType")]);
    m_post_tax_savings_amount_type_isSet = !json[QString("postTaxSavingsAmountType")].isNull() && m_post_tax_savings_amount_type_isValid;

    m_pre_tax_savings_amount_isValid = ::OpenAPI::fromJsonValue(m_pre_tax_savings_amount, json[QString("preTaxSavingsAmount")]);
    m_pre_tax_savings_amount_isSet = !json[QString("preTaxSavingsAmount")].isNull() && m_pre_tax_savings_amount_isValid;

    m_pre_tax_savings_amount_type_isValid = ::OpenAPI::fromJsonValue(m_pre_tax_savings_amount_type, json[QString("preTaxSavingsAmountType")]);
    m_pre_tax_savings_amount_type_isSet = !json[QString("preTaxSavingsAmountType")].isNull() && m_pre_tax_savings_amount_type_isValid;

    m_savings_strategy_id_isValid = ::OpenAPI::fromJsonValue(m_savings_strategy_id, json[QString("savingsStrategyId")]);
    m_savings_strategy_id_isSet = !json[QString("savingsStrategyId")].isNull() && m_savings_strategy_id_isValid;

    m_start_date_isValid = ::OpenAPI::fromJsonValue(m_start_date, json[QString("startDate")]);
    m_start_date_isSet = !json[QString("startDate")].isNull() && m_start_date_isValid;
}

QString OAISavingsStrategyWithIdModel::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISavingsStrategyWithIdModel::asJsonObject() const {
    QJsonObject obj;
    if (m_account_id_isSet) {
        obj.insert(QString("accountId"), ::OpenAPI::toJsonValue(m_account_id));
    }
    if (m_employer_savings_amount_isSet) {
        obj.insert(QString("employerSavingsAmount"), ::OpenAPI::toJsonValue(m_employer_savings_amount));
    }
    if (m_employer_savings_amount_type_isSet) {
        obj.insert(QString("employerSavingsAmountType"), ::OpenAPI::toJsonValue(m_employer_savings_amount_type));
    }
    if (m_end_date_isSet) {
        obj.insert(QString("endDate"), ::OpenAPI::toJsonValue(m_end_date));
    }
    if (m_external_destination_id_isSet) {
        obj.insert(QString("externalDestinationId"), ::OpenAPI::toJsonValue(m_external_destination_id));
    }
    if (m_frequency_id_isSet) {
        obj.insert(QString("frequencyId"), ::OpenAPI::toJsonValue(m_frequency_id));
    }
    if (m_mandatory_amount_isSet) {
        obj.insert(QString("mandatoryAmount"), ::OpenAPI::toJsonValue(m_mandatory_amount));
    }
    if (m_mandatory_amount_type_isSet) {
        obj.insert(QString("mandatoryAmountType"), ::OpenAPI::toJsonValue(m_mandatory_amount_type));
    }
    if (m_post_tax_savings_amount_isSet) {
        obj.insert(QString("postTaxSavingsAmount"), ::OpenAPI::toJsonValue(m_post_tax_savings_amount));
    }
    if (m_post_tax_savings_amount_type_isSet) {
        obj.insert(QString("postTaxSavingsAmountType"), ::OpenAPI::toJsonValue(m_post_tax_savings_amount_type));
    }
    if (m_pre_tax_savings_amount_isSet) {
        obj.insert(QString("preTaxSavingsAmount"), ::OpenAPI::toJsonValue(m_pre_tax_savings_amount));
    }
    if (m_pre_tax_savings_amount_type_isSet) {
        obj.insert(QString("preTaxSavingsAmountType"), ::OpenAPI::toJsonValue(m_pre_tax_savings_amount_type));
    }
    if (m_savings_strategy_id_isSet) {
        obj.insert(QString("savingsStrategyId"), ::OpenAPI::toJsonValue(m_savings_strategy_id));
    }
    if (m_start_date_isSet) {
        obj.insert(QString("startDate"), ::OpenAPI::toJsonValue(m_start_date));
    }
    return obj;
}

qint32 OAISavingsStrategyWithIdModel::getAccountId() const {
    return m_account_id;
}
void OAISavingsStrategyWithIdModel::setAccountId(const qint32 &account_id) {
    m_account_id = account_id;
    m_account_id_isSet = true;
}

bool OAISavingsStrategyWithIdModel::is_account_id_Set() const{
    return m_account_id_isSet;
}

bool OAISavingsStrategyWithIdModel::is_account_id_Valid() const{
    return m_account_id_isValid;
}

double OAISavingsStrategyWithIdModel::getEmployerSavingsAmount() const {
    return m_employer_savings_amount;
}
void OAISavingsStrategyWithIdModel::setEmployerSavingsAmount(const double &employer_savings_amount) {
    m_employer_savings_amount = employer_savings_amount;
    m_employer_savings_amount_isSet = true;
}

bool OAISavingsStrategyWithIdModel::is_employer_savings_amount_Set() const{
    return m_employer_savings_amount_isSet;
}

bool OAISavingsStrategyWithIdModel::is_employer_savings_amount_Valid() const{
    return m_employer_savings_amount_isValid;
}

QString OAISavingsStrategyWithIdModel::getEmployerSavingsAmountType() const {
    return m_employer_savings_amount_type;
}
void OAISavingsStrategyWithIdModel::setEmployerSavingsAmountType(const QString &employer_savings_amount_type) {
    m_employer_savings_amount_type = employer_savings_amount_type;
    m_employer_savings_amount_type_isSet = true;
}

bool OAISavingsStrategyWithIdModel::is_employer_savings_amount_type_Set() const{
    return m_employer_savings_amount_type_isSet;
}

bool OAISavingsStrategyWithIdModel::is_employer_savings_amount_type_Valid() const{
    return m_employer_savings_amount_type_isValid;
}

QDateTime OAISavingsStrategyWithIdModel::getEndDate() const {
    return m_end_date;
}
void OAISavingsStrategyWithIdModel::setEndDate(const QDateTime &end_date) {
    m_end_date = end_date;
    m_end_date_isSet = true;
}

bool OAISavingsStrategyWithIdModel::is_end_date_Set() const{
    return m_end_date_isSet;
}

bool OAISavingsStrategyWithIdModel::is_end_date_Valid() const{
    return m_end_date_isValid;
}

QString OAISavingsStrategyWithIdModel::getExternalDestinationId() const {
    return m_external_destination_id;
}
void OAISavingsStrategyWithIdModel::setExternalDestinationId(const QString &external_destination_id) {
    m_external_destination_id = external_destination_id;
    m_external_destination_id_isSet = true;
}

bool OAISavingsStrategyWithIdModel::is_external_destination_id_Set() const{
    return m_external_destination_id_isSet;
}

bool OAISavingsStrategyWithIdModel::is_external_destination_id_Valid() const{
    return m_external_destination_id_isValid;
}

qint32 OAISavingsStrategyWithIdModel::getFrequencyId() const {
    return m_frequency_id;
}
void OAISavingsStrategyWithIdModel::setFrequencyId(const qint32 &frequency_id) {
    m_frequency_id = frequency_id;
    m_frequency_id_isSet = true;
}

bool OAISavingsStrategyWithIdModel::is_frequency_id_Set() const{
    return m_frequency_id_isSet;
}

bool OAISavingsStrategyWithIdModel::is_frequency_id_Valid() const{
    return m_frequency_id_isValid;
}

double OAISavingsStrategyWithIdModel::getMandatoryAmount() const {
    return m_mandatory_amount;
}
void OAISavingsStrategyWithIdModel::setMandatoryAmount(const double &mandatory_amount) {
    m_mandatory_amount = mandatory_amount;
    m_mandatory_amount_isSet = true;
}

bool OAISavingsStrategyWithIdModel::is_mandatory_amount_Set() const{
    return m_mandatory_amount_isSet;
}

bool OAISavingsStrategyWithIdModel::is_mandatory_amount_Valid() const{
    return m_mandatory_amount_isValid;
}

QString OAISavingsStrategyWithIdModel::getMandatoryAmountType() const {
    return m_mandatory_amount_type;
}
void OAISavingsStrategyWithIdModel::setMandatoryAmountType(const QString &mandatory_amount_type) {
    m_mandatory_amount_type = mandatory_amount_type;
    m_mandatory_amount_type_isSet = true;
}

bool OAISavingsStrategyWithIdModel::is_mandatory_amount_type_Set() const{
    return m_mandatory_amount_type_isSet;
}

bool OAISavingsStrategyWithIdModel::is_mandatory_amount_type_Valid() const{
    return m_mandatory_amount_type_isValid;
}

double OAISavingsStrategyWithIdModel::getPostTaxSavingsAmount() const {
    return m_post_tax_savings_amount;
}
void OAISavingsStrategyWithIdModel::setPostTaxSavingsAmount(const double &post_tax_savings_amount) {
    m_post_tax_savings_amount = post_tax_savings_amount;
    m_post_tax_savings_amount_isSet = true;
}

bool OAISavingsStrategyWithIdModel::is_post_tax_savings_amount_Set() const{
    return m_post_tax_savings_amount_isSet;
}

bool OAISavingsStrategyWithIdModel::is_post_tax_savings_amount_Valid() const{
    return m_post_tax_savings_amount_isValid;
}

QString OAISavingsStrategyWithIdModel::getPostTaxSavingsAmountType() const {
    return m_post_tax_savings_amount_type;
}
void OAISavingsStrategyWithIdModel::setPostTaxSavingsAmountType(const QString &post_tax_savings_amount_type) {
    m_post_tax_savings_amount_type = post_tax_savings_amount_type;
    m_post_tax_savings_amount_type_isSet = true;
}

bool OAISavingsStrategyWithIdModel::is_post_tax_savings_amount_type_Set() const{
    return m_post_tax_savings_amount_type_isSet;
}

bool OAISavingsStrategyWithIdModel::is_post_tax_savings_amount_type_Valid() const{
    return m_post_tax_savings_amount_type_isValid;
}

double OAISavingsStrategyWithIdModel::getPreTaxSavingsAmount() const {
    return m_pre_tax_savings_amount;
}
void OAISavingsStrategyWithIdModel::setPreTaxSavingsAmount(const double &pre_tax_savings_amount) {
    m_pre_tax_savings_amount = pre_tax_savings_amount;
    m_pre_tax_savings_amount_isSet = true;
}

bool OAISavingsStrategyWithIdModel::is_pre_tax_savings_amount_Set() const{
    return m_pre_tax_savings_amount_isSet;
}

bool OAISavingsStrategyWithIdModel::is_pre_tax_savings_amount_Valid() const{
    return m_pre_tax_savings_amount_isValid;
}

QString OAISavingsStrategyWithIdModel::getPreTaxSavingsAmountType() const {
    return m_pre_tax_savings_amount_type;
}
void OAISavingsStrategyWithIdModel::setPreTaxSavingsAmountType(const QString &pre_tax_savings_amount_type) {
    m_pre_tax_savings_amount_type = pre_tax_savings_amount_type;
    m_pre_tax_savings_amount_type_isSet = true;
}

bool OAISavingsStrategyWithIdModel::is_pre_tax_savings_amount_type_Set() const{
    return m_pre_tax_savings_amount_type_isSet;
}

bool OAISavingsStrategyWithIdModel::is_pre_tax_savings_amount_type_Valid() const{
    return m_pre_tax_savings_amount_type_isValid;
}

qint32 OAISavingsStrategyWithIdModel::getSavingsStrategyId() const {
    return m_savings_strategy_id;
}
void OAISavingsStrategyWithIdModel::setSavingsStrategyId(const qint32 &savings_strategy_id) {
    m_savings_strategy_id = savings_strategy_id;
    m_savings_strategy_id_isSet = true;
}

bool OAISavingsStrategyWithIdModel::is_savings_strategy_id_Set() const{
    return m_savings_strategy_id_isSet;
}

bool OAISavingsStrategyWithIdModel::is_savings_strategy_id_Valid() const{
    return m_savings_strategy_id_isValid;
}

QDateTime OAISavingsStrategyWithIdModel::getStartDate() const {
    return m_start_date;
}
void OAISavingsStrategyWithIdModel::setStartDate(const QDateTime &start_date) {
    m_start_date = start_date;
    m_start_date_isSet = true;
}

bool OAISavingsStrategyWithIdModel::is_start_date_Set() const{
    return m_start_date_isSet;
}

bool OAISavingsStrategyWithIdModel::is_start_date_Valid() const{
    return m_start_date_isValid;
}

bool OAISavingsStrategyWithIdModel::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_account_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_employer_savings_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_employer_savings_amount_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_end_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_external_destination_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_frequency_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_mandatory_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_mandatory_amount_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_post_tax_savings_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_post_tax_savings_amount_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_pre_tax_savings_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_pre_tax_savings_amount_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_savings_strategy_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_start_date_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISavingsStrategyWithIdModel::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
