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

#include "OAIAssetsFundingGoalSummary.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAssetsFundingGoalSummary::OAIAssetsFundingGoalSummary(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAssetsFundingGoalSummary::OAIAssetsFundingGoalSummary() {
    this->initializeModel();
}

OAIAssetsFundingGoalSummary::~OAIAssetsFundingGoalSummary() {}

void OAIAssetsFundingGoalSummary::initializeModel() {

    m_contributions_isSet = false;
    m_contributions_isValid = false;

    m_end_of_year_assets_isSet = false;
    m_end_of_year_assets_isValid = false;

    m_goal_type_isSet = false;
    m_goal_type_isValid = false;

    m_growth_and_reinvestments_isSet = false;
    m_growth_and_reinvestments_isValid = false;

    m_identifier_isSet = false;
    m_identifier_isValid = false;

    m_net_withdrawals_isSet = false;
    m_net_withdrawals_isValid = false;

    m_withdrawals_isSet = false;
    m_withdrawals_isValid = false;
}

void OAIAssetsFundingGoalSummary::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAssetsFundingGoalSummary::fromJsonObject(QJsonObject json) {

    m_contributions_isValid = ::OpenAPI::fromJsonValue(m_contributions, json[QString("contributions")]);
    m_contributions_isSet = !json[QString("contributions")].isNull() && m_contributions_isValid;

    m_end_of_year_assets_isValid = ::OpenAPI::fromJsonValue(m_end_of_year_assets, json[QString("endOfYearAssets")]);
    m_end_of_year_assets_isSet = !json[QString("endOfYearAssets")].isNull() && m_end_of_year_assets_isValid;

    m_goal_type_isValid = ::OpenAPI::fromJsonValue(m_goal_type, json[QString("goalType")]);
    m_goal_type_isSet = !json[QString("goalType")].isNull() && m_goal_type_isValid;

    m_growth_and_reinvestments_isValid = ::OpenAPI::fromJsonValue(m_growth_and_reinvestments, json[QString("growthAndReinvestments")]);
    m_growth_and_reinvestments_isSet = !json[QString("growthAndReinvestments")].isNull() && m_growth_and_reinvestments_isValid;

    m_identifier_isValid = ::OpenAPI::fromJsonValue(m_identifier, json[QString("identifier")]);
    m_identifier_isSet = !json[QString("identifier")].isNull() && m_identifier_isValid;

    m_net_withdrawals_isValid = ::OpenAPI::fromJsonValue(m_net_withdrawals, json[QString("netWithdrawals")]);
    m_net_withdrawals_isSet = !json[QString("netWithdrawals")].isNull() && m_net_withdrawals_isValid;

    m_withdrawals_isValid = ::OpenAPI::fromJsonValue(m_withdrawals, json[QString("withdrawals")]);
    m_withdrawals_isSet = !json[QString("withdrawals")].isNull() && m_withdrawals_isValid;
}

QString OAIAssetsFundingGoalSummary::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAssetsFundingGoalSummary::asJsonObject() const {
    QJsonObject obj;
    if (m_contributions.isSet()) {
        obj.insert(QString("contributions"), ::OpenAPI::toJsonValue(m_contributions));
    }
    if (m_end_of_year_assets.isSet()) {
        obj.insert(QString("endOfYearAssets"), ::OpenAPI::toJsonValue(m_end_of_year_assets));
    }
    if (m_goal_type_isSet) {
        obj.insert(QString("goalType"), ::OpenAPI::toJsonValue(m_goal_type));
    }
    if (m_growth_and_reinvestments.isSet()) {
        obj.insert(QString("growthAndReinvestments"), ::OpenAPI::toJsonValue(m_growth_and_reinvestments));
    }
    if (m_identifier_isSet) {
        obj.insert(QString("identifier"), ::OpenAPI::toJsonValue(m_identifier));
    }
    if (m_net_withdrawals_isSet) {
        obj.insert(QString("netWithdrawals"), ::OpenAPI::toJsonValue(m_net_withdrawals));
    }
    if (m_withdrawals.isSet()) {
        obj.insert(QString("withdrawals"), ::OpenAPI::toJsonValue(m_withdrawals));
    }
    return obj;
}

OAIIAccumulationCategoryData OAIAssetsFundingGoalSummary::getContributions() const {
    return m_contributions;
}
void OAIAssetsFundingGoalSummary::setContributions(const OAIIAccumulationCategoryData &contributions) {
    m_contributions = contributions;
    m_contributions_isSet = true;
}

bool OAIAssetsFundingGoalSummary::is_contributions_Set() const{
    return m_contributions_isSet;
}

bool OAIAssetsFundingGoalSummary::is_contributions_Valid() const{
    return m_contributions_isValid;
}

OAIIAccumulationCategoryData OAIAssetsFundingGoalSummary::getEndOfYearAssets() const {
    return m_end_of_year_assets;
}
void OAIAssetsFundingGoalSummary::setEndOfYearAssets(const OAIIAccumulationCategoryData &end_of_year_assets) {
    m_end_of_year_assets = end_of_year_assets;
    m_end_of_year_assets_isSet = true;
}

bool OAIAssetsFundingGoalSummary::is_end_of_year_assets_Set() const{
    return m_end_of_year_assets_isSet;
}

bool OAIAssetsFundingGoalSummary::is_end_of_year_assets_Valid() const{
    return m_end_of_year_assets_isValid;
}

QString OAIAssetsFundingGoalSummary::getGoalType() const {
    return m_goal_type;
}
void OAIAssetsFundingGoalSummary::setGoalType(const QString &goal_type) {
    m_goal_type = goal_type;
    m_goal_type_isSet = true;
}

bool OAIAssetsFundingGoalSummary::is_goal_type_Set() const{
    return m_goal_type_isSet;
}

bool OAIAssetsFundingGoalSummary::is_goal_type_Valid() const{
    return m_goal_type_isValid;
}

OAIIAccumulationCategoryData OAIAssetsFundingGoalSummary::getGrowthAndReinvestments() const {
    return m_growth_and_reinvestments;
}
void OAIAssetsFundingGoalSummary::setGrowthAndReinvestments(const OAIIAccumulationCategoryData &growth_and_reinvestments) {
    m_growth_and_reinvestments = growth_and_reinvestments;
    m_growth_and_reinvestments_isSet = true;
}

bool OAIAssetsFundingGoalSummary::is_growth_and_reinvestments_Set() const{
    return m_growth_and_reinvestments_isSet;
}

bool OAIAssetsFundingGoalSummary::is_growth_and_reinvestments_Valid() const{
    return m_growth_and_reinvestments_isValid;
}

qint32 OAIAssetsFundingGoalSummary::getIdentifier() const {
    return m_identifier;
}
void OAIAssetsFundingGoalSummary::setIdentifier(const qint32 &identifier) {
    m_identifier = identifier;
    m_identifier_isSet = true;
}

bool OAIAssetsFundingGoalSummary::is_identifier_Set() const{
    return m_identifier_isSet;
}

bool OAIAssetsFundingGoalSummary::is_identifier_Valid() const{
    return m_identifier_isValid;
}

double OAIAssetsFundingGoalSummary::getNetWithdrawals() const {
    return m_net_withdrawals;
}
void OAIAssetsFundingGoalSummary::setNetWithdrawals(const double &net_withdrawals) {
    m_net_withdrawals = net_withdrawals;
    m_net_withdrawals_isSet = true;
}

bool OAIAssetsFundingGoalSummary::is_net_withdrawals_Set() const{
    return m_net_withdrawals_isSet;
}

bool OAIAssetsFundingGoalSummary::is_net_withdrawals_Valid() const{
    return m_net_withdrawals_isValid;
}

OAIIAccumulationCategoryData OAIAssetsFundingGoalSummary::getWithdrawals() const {
    return m_withdrawals;
}
void OAIAssetsFundingGoalSummary::setWithdrawals(const OAIIAccumulationCategoryData &withdrawals) {
    m_withdrawals = withdrawals;
    m_withdrawals_isSet = true;
}

bool OAIAssetsFundingGoalSummary::is_withdrawals_Set() const{
    return m_withdrawals_isSet;
}

bool OAIAssetsFundingGoalSummary::is_withdrawals_Valid() const{
    return m_withdrawals_isValid;
}

bool OAIAssetsFundingGoalSummary::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_contributions.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_end_of_year_assets.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_goal_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_growth_and_reinvestments.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_identifier_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_net_withdrawals_isSet) {
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

bool OAIAssetsFundingGoalSummary::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
