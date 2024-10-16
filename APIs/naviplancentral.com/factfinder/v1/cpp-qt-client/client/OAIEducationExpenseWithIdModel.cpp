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

#include "OAIEducationExpenseWithIdModel.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIEducationExpenseWithIdModel::OAIEducationExpenseWithIdModel(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIEducationExpenseWithIdModel::OAIEducationExpenseWithIdModel() {
    this->initializeModel();
}

OAIEducationExpenseWithIdModel::~OAIEducationExpenseWithIdModel() {}

void OAIEducationExpenseWithIdModel::initializeModel() {

    m_annual_cost_isSet = false;
    m_annual_cost_isValid = false;

    m_education_expense_id_isSet = false;
    m_education_expense_id_isValid = false;

    m_education_goal_id_isSet = false;
    m_education_goal_id_isValid = false;

    m_external_destination_id_isSet = false;
    m_external_destination_id_isValid = false;

    m_links_isSet = false;
    m_links_isValid = false;

    m_member_isSet = false;
    m_member_isValid = false;

    m_member_dependent_id_isSet = false;
    m_member_dependent_id_isValid = false;

    m_start_year_isSet = false;
    m_start_year_isValid = false;

    m_years_isSet = false;
    m_years_isValid = false;
}

void OAIEducationExpenseWithIdModel::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIEducationExpenseWithIdModel::fromJsonObject(QJsonObject json) {

    m_annual_cost_isValid = ::OpenAPI::fromJsonValue(m_annual_cost, json[QString("annualCost")]);
    m_annual_cost_isSet = !json[QString("annualCost")].isNull() && m_annual_cost_isValid;

    m_education_expense_id_isValid = ::OpenAPI::fromJsonValue(m_education_expense_id, json[QString("educationExpenseId")]);
    m_education_expense_id_isSet = !json[QString("educationExpenseId")].isNull() && m_education_expense_id_isValid;

    m_education_goal_id_isValid = ::OpenAPI::fromJsonValue(m_education_goal_id, json[QString("educationGoalId")]);
    m_education_goal_id_isSet = !json[QString("educationGoalId")].isNull() && m_education_goal_id_isValid;

    m_external_destination_id_isValid = ::OpenAPI::fromJsonValue(m_external_destination_id, json[QString("externalDestinationId")]);
    m_external_destination_id_isSet = !json[QString("externalDestinationId")].isNull() && m_external_destination_id_isValid;

    m_links_isValid = ::OpenAPI::fromJsonValue(m_links, json[QString("links")]);
    m_links_isSet = !json[QString("links")].isNull() && m_links_isValid;

    m_member_isValid = ::OpenAPI::fromJsonValue(m_member, json[QString("member")]);
    m_member_isSet = !json[QString("member")].isNull() && m_member_isValid;

    m_member_dependent_id_isValid = ::OpenAPI::fromJsonValue(m_member_dependent_id, json[QString("memberDependentId")]);
    m_member_dependent_id_isSet = !json[QString("memberDependentId")].isNull() && m_member_dependent_id_isValid;

    m_start_year_isValid = ::OpenAPI::fromJsonValue(m_start_year, json[QString("startYear")]);
    m_start_year_isSet = !json[QString("startYear")].isNull() && m_start_year_isValid;

    m_years_isValid = ::OpenAPI::fromJsonValue(m_years, json[QString("years")]);
    m_years_isSet = !json[QString("years")].isNull() && m_years_isValid;
}

QString OAIEducationExpenseWithIdModel::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIEducationExpenseWithIdModel::asJsonObject() const {
    QJsonObject obj;
    if (m_annual_cost_isSet) {
        obj.insert(QString("annualCost"), ::OpenAPI::toJsonValue(m_annual_cost));
    }
    if (m_education_expense_id_isSet) {
        obj.insert(QString("educationExpenseId"), ::OpenAPI::toJsonValue(m_education_expense_id));
    }
    if (m_education_goal_id_isSet) {
        obj.insert(QString("educationGoalId"), ::OpenAPI::toJsonValue(m_education_goal_id));
    }
    if (m_external_destination_id_isSet) {
        obj.insert(QString("externalDestinationId"), ::OpenAPI::toJsonValue(m_external_destination_id));
    }
    if (m_links.size() > 0) {
        obj.insert(QString("links"), ::OpenAPI::toJsonValue(m_links));
    }
    if (m_member_isSet) {
        obj.insert(QString("member"), ::OpenAPI::toJsonValue(m_member));
    }
    if (m_member_dependent_id_isSet) {
        obj.insert(QString("memberDependentId"), ::OpenAPI::toJsonValue(m_member_dependent_id));
    }
    if (m_start_year_isSet) {
        obj.insert(QString("startYear"), ::OpenAPI::toJsonValue(m_start_year));
    }
    if (m_years_isSet) {
        obj.insert(QString("years"), ::OpenAPI::toJsonValue(m_years));
    }
    return obj;
}

double OAIEducationExpenseWithIdModel::getAnnualCost() const {
    return m_annual_cost;
}
void OAIEducationExpenseWithIdModel::setAnnualCost(const double &annual_cost) {
    m_annual_cost = annual_cost;
    m_annual_cost_isSet = true;
}

bool OAIEducationExpenseWithIdModel::is_annual_cost_Set() const{
    return m_annual_cost_isSet;
}

bool OAIEducationExpenseWithIdModel::is_annual_cost_Valid() const{
    return m_annual_cost_isValid;
}

qint32 OAIEducationExpenseWithIdModel::getEducationExpenseId() const {
    return m_education_expense_id;
}
void OAIEducationExpenseWithIdModel::setEducationExpenseId(const qint32 &education_expense_id) {
    m_education_expense_id = education_expense_id;
    m_education_expense_id_isSet = true;
}

bool OAIEducationExpenseWithIdModel::is_education_expense_id_Set() const{
    return m_education_expense_id_isSet;
}

bool OAIEducationExpenseWithIdModel::is_education_expense_id_Valid() const{
    return m_education_expense_id_isValid;
}

qint32 OAIEducationExpenseWithIdModel::getEducationGoalId() const {
    return m_education_goal_id;
}
void OAIEducationExpenseWithIdModel::setEducationGoalId(const qint32 &education_goal_id) {
    m_education_goal_id = education_goal_id;
    m_education_goal_id_isSet = true;
}

bool OAIEducationExpenseWithIdModel::is_education_goal_id_Set() const{
    return m_education_goal_id_isSet;
}

bool OAIEducationExpenseWithIdModel::is_education_goal_id_Valid() const{
    return m_education_goal_id_isValid;
}

QString OAIEducationExpenseWithIdModel::getExternalDestinationId() const {
    return m_external_destination_id;
}
void OAIEducationExpenseWithIdModel::setExternalDestinationId(const QString &external_destination_id) {
    m_external_destination_id = external_destination_id;
    m_external_destination_id_isSet = true;
}

bool OAIEducationExpenseWithIdModel::is_external_destination_id_Set() const{
    return m_external_destination_id_isSet;
}

bool OAIEducationExpenseWithIdModel::is_external_destination_id_Valid() const{
    return m_external_destination_id_isValid;
}

QList<OAIObjectLink> OAIEducationExpenseWithIdModel::getLinks() const {
    return m_links;
}
void OAIEducationExpenseWithIdModel::setLinks(const QList<OAIObjectLink> &links) {
    m_links = links;
    m_links_isSet = true;
}

bool OAIEducationExpenseWithIdModel::is_links_Set() const{
    return m_links_isSet;
}

bool OAIEducationExpenseWithIdModel::is_links_Valid() const{
    return m_links_isValid;
}

QString OAIEducationExpenseWithIdModel::getMember() const {
    return m_member;
}
void OAIEducationExpenseWithIdModel::setMember(const QString &member) {
    m_member = member;
    m_member_isSet = true;
}

bool OAIEducationExpenseWithIdModel::is_member_Set() const{
    return m_member_isSet;
}

bool OAIEducationExpenseWithIdModel::is_member_Valid() const{
    return m_member_isValid;
}

qint32 OAIEducationExpenseWithIdModel::getMemberDependentId() const {
    return m_member_dependent_id;
}
void OAIEducationExpenseWithIdModel::setMemberDependentId(const qint32 &member_dependent_id) {
    m_member_dependent_id = member_dependent_id;
    m_member_dependent_id_isSet = true;
}

bool OAIEducationExpenseWithIdModel::is_member_dependent_id_Set() const{
    return m_member_dependent_id_isSet;
}

bool OAIEducationExpenseWithIdModel::is_member_dependent_id_Valid() const{
    return m_member_dependent_id_isValid;
}

QDateTime OAIEducationExpenseWithIdModel::getStartYear() const {
    return m_start_year;
}
void OAIEducationExpenseWithIdModel::setStartYear(const QDateTime &start_year) {
    m_start_year = start_year;
    m_start_year_isSet = true;
}

bool OAIEducationExpenseWithIdModel::is_start_year_Set() const{
    return m_start_year_isSet;
}

bool OAIEducationExpenseWithIdModel::is_start_year_Valid() const{
    return m_start_year_isValid;
}

qint32 OAIEducationExpenseWithIdModel::getYears() const {
    return m_years;
}
void OAIEducationExpenseWithIdModel::setYears(const qint32 &years) {
    m_years = years;
    m_years_isSet = true;
}

bool OAIEducationExpenseWithIdModel::is_years_Set() const{
    return m_years_isSet;
}

bool OAIEducationExpenseWithIdModel::is_years_Valid() const{
    return m_years_isValid;
}

bool OAIEducationExpenseWithIdModel::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_annual_cost_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_education_expense_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_education_goal_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_external_destination_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_links.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_member_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_member_dependent_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_start_year_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_years_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIEducationExpenseWithIdModel::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
