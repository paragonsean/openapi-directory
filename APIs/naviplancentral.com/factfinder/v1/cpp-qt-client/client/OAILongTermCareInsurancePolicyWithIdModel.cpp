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

#include "OAILongTermCareInsurancePolicyWithIdModel.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAILongTermCareInsurancePolicyWithIdModel::OAILongTermCareInsurancePolicyWithIdModel(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAILongTermCareInsurancePolicyWithIdModel::OAILongTermCareInsurancePolicyWithIdModel() {
    this->initializeModel();
}

OAILongTermCareInsurancePolicyWithIdModel::~OAILongTermCareInsurancePolicyWithIdModel() {}

void OAILongTermCareInsurancePolicyWithIdModel::initializeModel() {

    m_benefit_isSet = false;
    m_benefit_isValid = false;

    m_benefit_frequency_isSet = false;
    m_benefit_frequency_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_external_destination_id_isSet = false;
    m_external_destination_id_isValid = false;

    m_fact_finder_id_isSet = false;
    m_fact_finder_id_isValid = false;

    m_insurance_policy_id_isSet = false;
    m_insurance_policy_id_isValid = false;

    m_insured_isSet = false;
    m_insured_isValid = false;

    m_links_isSet = false;
    m_links_isValid = false;

    m_premium_isSet = false;
    m_premium_isValid = false;

    m_premium_frequency_isSet = false;
    m_premium_frequency_isValid = false;
}

void OAILongTermCareInsurancePolicyWithIdModel::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAILongTermCareInsurancePolicyWithIdModel::fromJsonObject(QJsonObject json) {

    m_benefit_isValid = ::OpenAPI::fromJsonValue(m_benefit, json[QString("benefit")]);
    m_benefit_isSet = !json[QString("benefit")].isNull() && m_benefit_isValid;

    m_benefit_frequency_isValid = ::OpenAPI::fromJsonValue(m_benefit_frequency, json[QString("benefitFrequency")]);
    m_benefit_frequency_isSet = !json[QString("benefitFrequency")].isNull() && m_benefit_frequency_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_external_destination_id_isValid = ::OpenAPI::fromJsonValue(m_external_destination_id, json[QString("externalDestinationId")]);
    m_external_destination_id_isSet = !json[QString("externalDestinationId")].isNull() && m_external_destination_id_isValid;

    m_fact_finder_id_isValid = ::OpenAPI::fromJsonValue(m_fact_finder_id, json[QString("factFinderId")]);
    m_fact_finder_id_isSet = !json[QString("factFinderId")].isNull() && m_fact_finder_id_isValid;

    m_insurance_policy_id_isValid = ::OpenAPI::fromJsonValue(m_insurance_policy_id, json[QString("insurancePolicyId")]);
    m_insurance_policy_id_isSet = !json[QString("insurancePolicyId")].isNull() && m_insurance_policy_id_isValid;

    m_insured_isValid = ::OpenAPI::fromJsonValue(m_insured, json[QString("insured")]);
    m_insured_isSet = !json[QString("insured")].isNull() && m_insured_isValid;

    m_links_isValid = ::OpenAPI::fromJsonValue(m_links, json[QString("links")]);
    m_links_isSet = !json[QString("links")].isNull() && m_links_isValid;

    m_premium_isValid = ::OpenAPI::fromJsonValue(m_premium, json[QString("premium")]);
    m_premium_isSet = !json[QString("premium")].isNull() && m_premium_isValid;

    m_premium_frequency_isValid = ::OpenAPI::fromJsonValue(m_premium_frequency, json[QString("premiumFrequency")]);
    m_premium_frequency_isSet = !json[QString("premiumFrequency")].isNull() && m_premium_frequency_isValid;
}

QString OAILongTermCareInsurancePolicyWithIdModel::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAILongTermCareInsurancePolicyWithIdModel::asJsonObject() const {
    QJsonObject obj;
    if (m_benefit_isSet) {
        obj.insert(QString("benefit"), ::OpenAPI::toJsonValue(m_benefit));
    }
    if (m_benefit_frequency_isSet) {
        obj.insert(QString("benefitFrequency"), ::OpenAPI::toJsonValue(m_benefit_frequency));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_external_destination_id_isSet) {
        obj.insert(QString("externalDestinationId"), ::OpenAPI::toJsonValue(m_external_destination_id));
    }
    if (m_fact_finder_id_isSet) {
        obj.insert(QString("factFinderId"), ::OpenAPI::toJsonValue(m_fact_finder_id));
    }
    if (m_insurance_policy_id_isSet) {
        obj.insert(QString("insurancePolicyId"), ::OpenAPI::toJsonValue(m_insurance_policy_id));
    }
    if (m_insured_isSet) {
        obj.insert(QString("insured"), ::OpenAPI::toJsonValue(m_insured));
    }
    if (m_links.size() > 0) {
        obj.insert(QString("links"), ::OpenAPI::toJsonValue(m_links));
    }
    if (m_premium_isSet) {
        obj.insert(QString("premium"), ::OpenAPI::toJsonValue(m_premium));
    }
    if (m_premium_frequency_isSet) {
        obj.insert(QString("premiumFrequency"), ::OpenAPI::toJsonValue(m_premium_frequency));
    }
    return obj;
}

double OAILongTermCareInsurancePolicyWithIdModel::getBenefit() const {
    return m_benefit;
}
void OAILongTermCareInsurancePolicyWithIdModel::setBenefit(const double &benefit) {
    m_benefit = benefit;
    m_benefit_isSet = true;
}

bool OAILongTermCareInsurancePolicyWithIdModel::is_benefit_Set() const{
    return m_benefit_isSet;
}

bool OAILongTermCareInsurancePolicyWithIdModel::is_benefit_Valid() const{
    return m_benefit_isValid;
}

qint32 OAILongTermCareInsurancePolicyWithIdModel::getBenefitFrequency() const {
    return m_benefit_frequency;
}
void OAILongTermCareInsurancePolicyWithIdModel::setBenefitFrequency(const qint32 &benefit_frequency) {
    m_benefit_frequency = benefit_frequency;
    m_benefit_frequency_isSet = true;
}

bool OAILongTermCareInsurancePolicyWithIdModel::is_benefit_frequency_Set() const{
    return m_benefit_frequency_isSet;
}

bool OAILongTermCareInsurancePolicyWithIdModel::is_benefit_frequency_Valid() const{
    return m_benefit_frequency_isValid;
}

QString OAILongTermCareInsurancePolicyWithIdModel::getDescription() const {
    return m_description;
}
void OAILongTermCareInsurancePolicyWithIdModel::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAILongTermCareInsurancePolicyWithIdModel::is_description_Set() const{
    return m_description_isSet;
}

bool OAILongTermCareInsurancePolicyWithIdModel::is_description_Valid() const{
    return m_description_isValid;
}

QString OAILongTermCareInsurancePolicyWithIdModel::getExternalDestinationId() const {
    return m_external_destination_id;
}
void OAILongTermCareInsurancePolicyWithIdModel::setExternalDestinationId(const QString &external_destination_id) {
    m_external_destination_id = external_destination_id;
    m_external_destination_id_isSet = true;
}

bool OAILongTermCareInsurancePolicyWithIdModel::is_external_destination_id_Set() const{
    return m_external_destination_id_isSet;
}

bool OAILongTermCareInsurancePolicyWithIdModel::is_external_destination_id_Valid() const{
    return m_external_destination_id_isValid;
}

qint32 OAILongTermCareInsurancePolicyWithIdModel::getFactFinderId() const {
    return m_fact_finder_id;
}
void OAILongTermCareInsurancePolicyWithIdModel::setFactFinderId(const qint32 &fact_finder_id) {
    m_fact_finder_id = fact_finder_id;
    m_fact_finder_id_isSet = true;
}

bool OAILongTermCareInsurancePolicyWithIdModel::is_fact_finder_id_Set() const{
    return m_fact_finder_id_isSet;
}

bool OAILongTermCareInsurancePolicyWithIdModel::is_fact_finder_id_Valid() const{
    return m_fact_finder_id_isValid;
}

qint32 OAILongTermCareInsurancePolicyWithIdModel::getInsurancePolicyId() const {
    return m_insurance_policy_id;
}
void OAILongTermCareInsurancePolicyWithIdModel::setInsurancePolicyId(const qint32 &insurance_policy_id) {
    m_insurance_policy_id = insurance_policy_id;
    m_insurance_policy_id_isSet = true;
}

bool OAILongTermCareInsurancePolicyWithIdModel::is_insurance_policy_id_Set() const{
    return m_insurance_policy_id_isSet;
}

bool OAILongTermCareInsurancePolicyWithIdModel::is_insurance_policy_id_Valid() const{
    return m_insurance_policy_id_isValid;
}

QString OAILongTermCareInsurancePolicyWithIdModel::getInsured() const {
    return m_insured;
}
void OAILongTermCareInsurancePolicyWithIdModel::setInsured(const QString &insured) {
    m_insured = insured;
    m_insured_isSet = true;
}

bool OAILongTermCareInsurancePolicyWithIdModel::is_insured_Set() const{
    return m_insured_isSet;
}

bool OAILongTermCareInsurancePolicyWithIdModel::is_insured_Valid() const{
    return m_insured_isValid;
}

QList<OAIObjectLink> OAILongTermCareInsurancePolicyWithIdModel::getLinks() const {
    return m_links;
}
void OAILongTermCareInsurancePolicyWithIdModel::setLinks(const QList<OAIObjectLink> &links) {
    m_links = links;
    m_links_isSet = true;
}

bool OAILongTermCareInsurancePolicyWithIdModel::is_links_Set() const{
    return m_links_isSet;
}

bool OAILongTermCareInsurancePolicyWithIdModel::is_links_Valid() const{
    return m_links_isValid;
}

double OAILongTermCareInsurancePolicyWithIdModel::getPremium() const {
    return m_premium;
}
void OAILongTermCareInsurancePolicyWithIdModel::setPremium(const double &premium) {
    m_premium = premium;
    m_premium_isSet = true;
}

bool OAILongTermCareInsurancePolicyWithIdModel::is_premium_Set() const{
    return m_premium_isSet;
}

bool OAILongTermCareInsurancePolicyWithIdModel::is_premium_Valid() const{
    return m_premium_isValid;
}

qint32 OAILongTermCareInsurancePolicyWithIdModel::getPremiumFrequency() const {
    return m_premium_frequency;
}
void OAILongTermCareInsurancePolicyWithIdModel::setPremiumFrequency(const qint32 &premium_frequency) {
    m_premium_frequency = premium_frequency;
    m_premium_frequency_isSet = true;
}

bool OAILongTermCareInsurancePolicyWithIdModel::is_premium_frequency_Set() const{
    return m_premium_frequency_isSet;
}

bool OAILongTermCareInsurancePolicyWithIdModel::is_premium_frequency_Valid() const{
    return m_premium_frequency_isValid;
}

bool OAILongTermCareInsurancePolicyWithIdModel::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_benefit_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_benefit_frequency_isSet) {
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

        if (m_fact_finder_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_insurance_policy_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_insured_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_links.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_premium_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_premium_frequency_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAILongTermCareInsurancePolicyWithIdModel::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
