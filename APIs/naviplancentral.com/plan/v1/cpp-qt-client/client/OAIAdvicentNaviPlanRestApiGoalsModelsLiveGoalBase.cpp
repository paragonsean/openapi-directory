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

#include "OAIAdvicentNaviPlanRestApiGoalsModelsLiveGoalBase.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAdvicentNaviPlanRestApiGoalsModelsLiveGoalBase::OAIAdvicentNaviPlanRestApiGoalsModelsLiveGoalBase(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAdvicentNaviPlanRestApiGoalsModelsLiveGoalBase::OAIAdvicentNaviPlanRestApiGoalsModelsLiveGoalBase() {
    this->initializeModel();
}

OAIAdvicentNaviPlanRestApiGoalsModelsLiveGoalBase::~OAIAdvicentNaviPlanRestApiGoalsModelsLiveGoalBase() {}

void OAIAdvicentNaviPlanRestApiGoalsModelsLiveGoalBase::initializeModel() {

    m_amount_isSet = false;
    m_amount_isValid = false;

    m_coverage_percentage_isSet = false;
    m_coverage_percentage_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_end_date_isSet = false;
    m_end_date_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_inflation_rate_isSet = false;
    m_inflation_rate_isValid = false;

    m_owners_isSet = false;
    m_owners_isValid = false;

    m_start_date_isSet = false;
    m_start_date_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIAdvicentNaviPlanRestApiGoalsModelsLiveGoalBase::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAdvicentNaviPlanRestApiGoalsModelsLiveGoalBase::fromJsonObject(QJsonObject json) {

    m_amount_isValid = ::OpenAPI::fromJsonValue(m_amount, json[QString("amount")]);
    m_amount_isSet = !json[QString("amount")].isNull() && m_amount_isValid;

    m_coverage_percentage_isValid = ::OpenAPI::fromJsonValue(m_coverage_percentage, json[QString("coveragePercentage")]);
    m_coverage_percentage_isSet = !json[QString("coveragePercentage")].isNull() && m_coverage_percentage_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_end_date_isValid = ::OpenAPI::fromJsonValue(m_end_date, json[QString("endDate")]);
    m_end_date_isSet = !json[QString("endDate")].isNull() && m_end_date_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_inflation_rate_isValid = ::OpenAPI::fromJsonValue(m_inflation_rate, json[QString("inflationRate")]);
    m_inflation_rate_isSet = !json[QString("inflationRate")].isNull() && m_inflation_rate_isValid;

    m_owners_isValid = ::OpenAPI::fromJsonValue(m_owners, json[QString("owners")]);
    m_owners_isSet = !json[QString("owners")].isNull() && m_owners_isValid;

    m_start_date_isValid = ::OpenAPI::fromJsonValue(m_start_date, json[QString("startDate")]);
    m_start_date_isSet = !json[QString("startDate")].isNull() && m_start_date_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAIAdvicentNaviPlanRestApiGoalsModelsLiveGoalBase::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAdvicentNaviPlanRestApiGoalsModelsLiveGoalBase::asJsonObject() const {
    QJsonObject obj;
    if (m_amount_isSet) {
        obj.insert(QString("amount"), ::OpenAPI::toJsonValue(m_amount));
    }
    if (m_coverage_percentage_isSet) {
        obj.insert(QString("coveragePercentage"), ::OpenAPI::toJsonValue(m_coverage_percentage));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_end_date_isSet) {
        obj.insert(QString("endDate"), ::OpenAPI::toJsonValue(m_end_date));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_inflation_rate_isSet) {
        obj.insert(QString("inflationRate"), ::OpenAPI::toJsonValue(m_inflation_rate));
    }
    if (m_owners.size() > 0) {
        obj.insert(QString("owners"), ::OpenAPI::toJsonValue(m_owners));
    }
    if (m_start_date_isSet) {
        obj.insert(QString("startDate"), ::OpenAPI::toJsonValue(m_start_date));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

double OAIAdvicentNaviPlanRestApiGoalsModelsLiveGoalBase::getAmount() const {
    return m_amount;
}
void OAIAdvicentNaviPlanRestApiGoalsModelsLiveGoalBase::setAmount(const double &amount) {
    m_amount = amount;
    m_amount_isSet = true;
}

bool OAIAdvicentNaviPlanRestApiGoalsModelsLiveGoalBase::is_amount_Set() const{
    return m_amount_isSet;
}

bool OAIAdvicentNaviPlanRestApiGoalsModelsLiveGoalBase::is_amount_Valid() const{
    return m_amount_isValid;
}

double OAIAdvicentNaviPlanRestApiGoalsModelsLiveGoalBase::getCoveragePercentage() const {
    return m_coverage_percentage;
}
void OAIAdvicentNaviPlanRestApiGoalsModelsLiveGoalBase::setCoveragePercentage(const double &coverage_percentage) {
    m_coverage_percentage = coverage_percentage;
    m_coverage_percentage_isSet = true;
}

bool OAIAdvicentNaviPlanRestApiGoalsModelsLiveGoalBase::is_coverage_percentage_Set() const{
    return m_coverage_percentage_isSet;
}

bool OAIAdvicentNaviPlanRestApiGoalsModelsLiveGoalBase::is_coverage_percentage_Valid() const{
    return m_coverage_percentage_isValid;
}

QString OAIAdvicentNaviPlanRestApiGoalsModelsLiveGoalBase::getDescription() const {
    return m_description;
}
void OAIAdvicentNaviPlanRestApiGoalsModelsLiveGoalBase::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIAdvicentNaviPlanRestApiGoalsModelsLiveGoalBase::is_description_Set() const{
    return m_description_isSet;
}

bool OAIAdvicentNaviPlanRestApiGoalsModelsLiveGoalBase::is_description_Valid() const{
    return m_description_isValid;
}

QDateTime OAIAdvicentNaviPlanRestApiGoalsModelsLiveGoalBase::getEndDate() const {
    return m_end_date;
}
void OAIAdvicentNaviPlanRestApiGoalsModelsLiveGoalBase::setEndDate(const QDateTime &end_date) {
    m_end_date = end_date;
    m_end_date_isSet = true;
}

bool OAIAdvicentNaviPlanRestApiGoalsModelsLiveGoalBase::is_end_date_Set() const{
    return m_end_date_isSet;
}

bool OAIAdvicentNaviPlanRestApiGoalsModelsLiveGoalBase::is_end_date_Valid() const{
    return m_end_date_isValid;
}

qint32 OAIAdvicentNaviPlanRestApiGoalsModelsLiveGoalBase::getId() const {
    return m_id;
}
void OAIAdvicentNaviPlanRestApiGoalsModelsLiveGoalBase::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIAdvicentNaviPlanRestApiGoalsModelsLiveGoalBase::is_id_Set() const{
    return m_id_isSet;
}

bool OAIAdvicentNaviPlanRestApiGoalsModelsLiveGoalBase::is_id_Valid() const{
    return m_id_isValid;
}

double OAIAdvicentNaviPlanRestApiGoalsModelsLiveGoalBase::getInflationRate() const {
    return m_inflation_rate;
}
void OAIAdvicentNaviPlanRestApiGoalsModelsLiveGoalBase::setInflationRate(const double &inflation_rate) {
    m_inflation_rate = inflation_rate;
    m_inflation_rate_isSet = true;
}

bool OAIAdvicentNaviPlanRestApiGoalsModelsLiveGoalBase::is_inflation_rate_Set() const{
    return m_inflation_rate_isSet;
}

bool OAIAdvicentNaviPlanRestApiGoalsModelsLiveGoalBase::is_inflation_rate_Valid() const{
    return m_inflation_rate_isValid;
}

QList<OAIAdvicentNaviPlanRestApiModelsOwnerModel> OAIAdvicentNaviPlanRestApiGoalsModelsLiveGoalBase::getOwners() const {
    return m_owners;
}
void OAIAdvicentNaviPlanRestApiGoalsModelsLiveGoalBase::setOwners(const QList<OAIAdvicentNaviPlanRestApiModelsOwnerModel> &owners) {
    m_owners = owners;
    m_owners_isSet = true;
}

bool OAIAdvicentNaviPlanRestApiGoalsModelsLiveGoalBase::is_owners_Set() const{
    return m_owners_isSet;
}

bool OAIAdvicentNaviPlanRestApiGoalsModelsLiveGoalBase::is_owners_Valid() const{
    return m_owners_isValid;
}

QDateTime OAIAdvicentNaviPlanRestApiGoalsModelsLiveGoalBase::getStartDate() const {
    return m_start_date;
}
void OAIAdvicentNaviPlanRestApiGoalsModelsLiveGoalBase::setStartDate(const QDateTime &start_date) {
    m_start_date = start_date;
    m_start_date_isSet = true;
}

bool OAIAdvicentNaviPlanRestApiGoalsModelsLiveGoalBase::is_start_date_Set() const{
    return m_start_date_isSet;
}

bool OAIAdvicentNaviPlanRestApiGoalsModelsLiveGoalBase::is_start_date_Valid() const{
    return m_start_date_isValid;
}

QString OAIAdvicentNaviPlanRestApiGoalsModelsLiveGoalBase::getType() const {
    return m_type;
}
void OAIAdvicentNaviPlanRestApiGoalsModelsLiveGoalBase::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIAdvicentNaviPlanRestApiGoalsModelsLiveGoalBase::is_type_Set() const{
    return m_type_isSet;
}

bool OAIAdvicentNaviPlanRestApiGoalsModelsLiveGoalBase::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIAdvicentNaviPlanRestApiGoalsModelsLiveGoalBase::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_coverage_percentage_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_end_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_inflation_rate_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_owners.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_start_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAdvicentNaviPlanRestApiGoalsModelsLiveGoalBase::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
