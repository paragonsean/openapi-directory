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

#include "OAIHouseholdExternalModel.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIHouseholdExternalModel::OAIHouseholdExternalModel(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIHouseholdExternalModel::OAIHouseholdExternalModel() {
    this->initializeModel();
}

OAIHouseholdExternalModel::~OAIHouseholdExternalModel() {}

void OAIHouseholdExternalModel::initializeModel() {

    m_accessible_plans_isSet = false;
    m_accessible_plans_isValid = false;

    m_client_description_isSet = false;
    m_client_description_isValid = false;

    m_household_id_isSet = false;
    m_household_id_isValid = false;

    m_legacy_client_id_isSet = false;
    m_legacy_client_id_isValid = false;
}

void OAIHouseholdExternalModel::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIHouseholdExternalModel::fromJsonObject(QJsonObject json) {

    m_accessible_plans_isValid = ::OpenAPI::fromJsonValue(m_accessible_plans, json[QString("accessiblePlans")]);
    m_accessible_plans_isSet = !json[QString("accessiblePlans")].isNull() && m_accessible_plans_isValid;

    m_client_description_isValid = ::OpenAPI::fromJsonValue(m_client_description, json[QString("clientDescription")]);
    m_client_description_isSet = !json[QString("clientDescription")].isNull() && m_client_description_isValid;

    m_household_id_isValid = ::OpenAPI::fromJsonValue(m_household_id, json[QString("householdId")]);
    m_household_id_isSet = !json[QString("householdId")].isNull() && m_household_id_isValid;

    m_legacy_client_id_isValid = ::OpenAPI::fromJsonValue(m_legacy_client_id, json[QString("legacyClientId")]);
    m_legacy_client_id_isSet = !json[QString("legacyClientId")].isNull() && m_legacy_client_id_isValid;
}

QString OAIHouseholdExternalModel::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIHouseholdExternalModel::asJsonObject() const {
    QJsonObject obj;
    if (m_accessible_plans.size() > 0) {
        obj.insert(QString("accessiblePlans"), ::OpenAPI::toJsonValue(m_accessible_plans));
    }
    if (m_client_description_isSet) {
        obj.insert(QString("clientDescription"), ::OpenAPI::toJsonValue(m_client_description));
    }
    if (m_household_id_isSet) {
        obj.insert(QString("householdId"), ::OpenAPI::toJsonValue(m_household_id));
    }
    if (m_legacy_client_id_isSet) {
        obj.insert(QString("legacyClientId"), ::OpenAPI::toJsonValue(m_legacy_client_id));
    }
    return obj;
}

QList<OAIPublishedPlanModel> OAIHouseholdExternalModel::getAccessiblePlans() const {
    return m_accessible_plans;
}
void OAIHouseholdExternalModel::setAccessiblePlans(const QList<OAIPublishedPlanModel> &accessible_plans) {
    m_accessible_plans = accessible_plans;
    m_accessible_plans_isSet = true;
}

bool OAIHouseholdExternalModel::is_accessible_plans_Set() const{
    return m_accessible_plans_isSet;
}

bool OAIHouseholdExternalModel::is_accessible_plans_Valid() const{
    return m_accessible_plans_isValid;
}

QString OAIHouseholdExternalModel::getClientDescription() const {
    return m_client_description;
}
void OAIHouseholdExternalModel::setClientDescription(const QString &client_description) {
    m_client_description = client_description;
    m_client_description_isSet = true;
}

bool OAIHouseholdExternalModel::is_client_description_Set() const{
    return m_client_description_isSet;
}

bool OAIHouseholdExternalModel::is_client_description_Valid() const{
    return m_client_description_isValid;
}

qint32 OAIHouseholdExternalModel::getHouseholdId() const {
    return m_household_id;
}
void OAIHouseholdExternalModel::setHouseholdId(const qint32 &household_id) {
    m_household_id = household_id;
    m_household_id_isSet = true;
}

bool OAIHouseholdExternalModel::is_household_id_Set() const{
    return m_household_id_isSet;
}

bool OAIHouseholdExternalModel::is_household_id_Valid() const{
    return m_household_id_isValid;
}

QString OAIHouseholdExternalModel::getLegacyClientId() const {
    return m_legacy_client_id;
}
void OAIHouseholdExternalModel::setLegacyClientId(const QString &legacy_client_id) {
    m_legacy_client_id = legacy_client_id;
    m_legacy_client_id_isSet = true;
}

bool OAIHouseholdExternalModel::is_legacy_client_id_Set() const{
    return m_legacy_client_id_isSet;
}

bool OAIHouseholdExternalModel::is_legacy_client_id_Valid() const{
    return m_legacy_client_id_isValid;
}

bool OAIHouseholdExternalModel::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_accessible_plans.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_client_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_household_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_legacy_client_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIHouseholdExternalModel::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
