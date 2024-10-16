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

#include "OAIAdvicentNaviPlanRestApiNetWorthModelsLiabilityModel.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAdvicentNaviPlanRestApiNetWorthModelsLiabilityModel::OAIAdvicentNaviPlanRestApiNetWorthModelsLiabilityModel(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAdvicentNaviPlanRestApiNetWorthModelsLiabilityModel::OAIAdvicentNaviPlanRestApiNetWorthModelsLiabilityModel() {
    this->initializeModel();
}

OAIAdvicentNaviPlanRestApiNetWorthModelsLiabilityModel::~OAIAdvicentNaviPlanRestApiNetWorthModelsLiabilityModel() {}

void OAIAdvicentNaviPlanRestApiNetWorthModelsLiabilityModel::initializeModel() {

    m_description_isSet = false;
    m_description_isValid = false;

    m_end_date_isSet = false;
    m_end_date_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_legacy_id_isSet = false;
    m_legacy_id_isValid = false;

    m_outstanding_principal_isSet = false;
    m_outstanding_principal_isValid = false;

    m_outstanding_principal_as_of_date_isSet = false;
    m_outstanding_principal_as_of_date_isValid = false;

    m_owner_isSet = false;
    m_owner_isValid = false;

    m_start_date_isSet = false;
    m_start_date_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIAdvicentNaviPlanRestApiNetWorthModelsLiabilityModel::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAdvicentNaviPlanRestApiNetWorthModelsLiabilityModel::fromJsonObject(QJsonObject json) {

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_end_date_isValid = ::OpenAPI::fromJsonValue(m_end_date, json[QString("endDate")]);
    m_end_date_isSet = !json[QString("endDate")].isNull() && m_end_date_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_legacy_id_isValid = ::OpenAPI::fromJsonValue(m_legacy_id, json[QString("legacyId")]);
    m_legacy_id_isSet = !json[QString("legacyId")].isNull() && m_legacy_id_isValid;

    m_outstanding_principal_isValid = ::OpenAPI::fromJsonValue(m_outstanding_principal, json[QString("outstandingPrincipal")]);
    m_outstanding_principal_isSet = !json[QString("outstandingPrincipal")].isNull() && m_outstanding_principal_isValid;

    m_outstanding_principal_as_of_date_isValid = ::OpenAPI::fromJsonValue(m_outstanding_principal_as_of_date, json[QString("outstandingPrincipalAsOfDate")]);
    m_outstanding_principal_as_of_date_isSet = !json[QString("outstandingPrincipalAsOfDate")].isNull() && m_outstanding_principal_as_of_date_isValid;

    m_owner_isValid = ::OpenAPI::fromJsonValue(m_owner, json[QString("owner")]);
    m_owner_isSet = !json[QString("owner")].isNull() && m_owner_isValid;

    m_start_date_isValid = ::OpenAPI::fromJsonValue(m_start_date, json[QString("startDate")]);
    m_start_date_isSet = !json[QString("startDate")].isNull() && m_start_date_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAIAdvicentNaviPlanRestApiNetWorthModelsLiabilityModel::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAdvicentNaviPlanRestApiNetWorthModelsLiabilityModel::asJsonObject() const {
    QJsonObject obj;
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_end_date_isSet) {
        obj.insert(QString("endDate"), ::OpenAPI::toJsonValue(m_end_date));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_legacy_id_isSet) {
        obj.insert(QString("legacyId"), ::OpenAPI::toJsonValue(m_legacy_id));
    }
    if (m_outstanding_principal_isSet) {
        obj.insert(QString("outstandingPrincipal"), ::OpenAPI::toJsonValue(m_outstanding_principal));
    }
    if (m_outstanding_principal_as_of_date_isSet) {
        obj.insert(QString("outstandingPrincipalAsOfDate"), ::OpenAPI::toJsonValue(m_outstanding_principal_as_of_date));
    }
    if (m_owner.isSet()) {
        obj.insert(QString("owner"), ::OpenAPI::toJsonValue(m_owner));
    }
    if (m_start_date_isSet) {
        obj.insert(QString("startDate"), ::OpenAPI::toJsonValue(m_start_date));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

QString OAIAdvicentNaviPlanRestApiNetWorthModelsLiabilityModel::getDescription() const {
    return m_description;
}
void OAIAdvicentNaviPlanRestApiNetWorthModelsLiabilityModel::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIAdvicentNaviPlanRestApiNetWorthModelsLiabilityModel::is_description_Set() const{
    return m_description_isSet;
}

bool OAIAdvicentNaviPlanRestApiNetWorthModelsLiabilityModel::is_description_Valid() const{
    return m_description_isValid;
}

QDateTime OAIAdvicentNaviPlanRestApiNetWorthModelsLiabilityModel::getEndDate() const {
    return m_end_date;
}
void OAIAdvicentNaviPlanRestApiNetWorthModelsLiabilityModel::setEndDate(const QDateTime &end_date) {
    m_end_date = end_date;
    m_end_date_isSet = true;
}

bool OAIAdvicentNaviPlanRestApiNetWorthModelsLiabilityModel::is_end_date_Set() const{
    return m_end_date_isSet;
}

bool OAIAdvicentNaviPlanRestApiNetWorthModelsLiabilityModel::is_end_date_Valid() const{
    return m_end_date_isValid;
}

qint32 OAIAdvicentNaviPlanRestApiNetWorthModelsLiabilityModel::getId() const {
    return m_id;
}
void OAIAdvicentNaviPlanRestApiNetWorthModelsLiabilityModel::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIAdvicentNaviPlanRestApiNetWorthModelsLiabilityModel::is_id_Set() const{
    return m_id_isSet;
}

bool OAIAdvicentNaviPlanRestApiNetWorthModelsLiabilityModel::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIAdvicentNaviPlanRestApiNetWorthModelsLiabilityModel::getLegacyId() const {
    return m_legacy_id;
}
void OAIAdvicentNaviPlanRestApiNetWorthModelsLiabilityModel::setLegacyId(const QString &legacy_id) {
    m_legacy_id = legacy_id;
    m_legacy_id_isSet = true;
}

bool OAIAdvicentNaviPlanRestApiNetWorthModelsLiabilityModel::is_legacy_id_Set() const{
    return m_legacy_id_isSet;
}

bool OAIAdvicentNaviPlanRestApiNetWorthModelsLiabilityModel::is_legacy_id_Valid() const{
    return m_legacy_id_isValid;
}

double OAIAdvicentNaviPlanRestApiNetWorthModelsLiabilityModel::getOutstandingPrincipal() const {
    return m_outstanding_principal;
}
void OAIAdvicentNaviPlanRestApiNetWorthModelsLiabilityModel::setOutstandingPrincipal(const double &outstanding_principal) {
    m_outstanding_principal = outstanding_principal;
    m_outstanding_principal_isSet = true;
}

bool OAIAdvicentNaviPlanRestApiNetWorthModelsLiabilityModel::is_outstanding_principal_Set() const{
    return m_outstanding_principal_isSet;
}

bool OAIAdvicentNaviPlanRestApiNetWorthModelsLiabilityModel::is_outstanding_principal_Valid() const{
    return m_outstanding_principal_isValid;
}

QDateTime OAIAdvicentNaviPlanRestApiNetWorthModelsLiabilityModel::getOutstandingPrincipalAsOfDate() const {
    return m_outstanding_principal_as_of_date;
}
void OAIAdvicentNaviPlanRestApiNetWorthModelsLiabilityModel::setOutstandingPrincipalAsOfDate(const QDateTime &outstanding_principal_as_of_date) {
    m_outstanding_principal_as_of_date = outstanding_principal_as_of_date;
    m_outstanding_principal_as_of_date_isSet = true;
}

bool OAIAdvicentNaviPlanRestApiNetWorthModelsLiabilityModel::is_outstanding_principal_as_of_date_Set() const{
    return m_outstanding_principal_as_of_date_isSet;
}

bool OAIAdvicentNaviPlanRestApiNetWorthModelsLiabilityModel::is_outstanding_principal_as_of_date_Valid() const{
    return m_outstanding_principal_as_of_date_isValid;
}

OAIAdvicentNaviPlanRestApiModelsOwnerModel OAIAdvicentNaviPlanRestApiNetWorthModelsLiabilityModel::getOwner() const {
    return m_owner;
}
void OAIAdvicentNaviPlanRestApiNetWorthModelsLiabilityModel::setOwner(const OAIAdvicentNaviPlanRestApiModelsOwnerModel &owner) {
    m_owner = owner;
    m_owner_isSet = true;
}

bool OAIAdvicentNaviPlanRestApiNetWorthModelsLiabilityModel::is_owner_Set() const{
    return m_owner_isSet;
}

bool OAIAdvicentNaviPlanRestApiNetWorthModelsLiabilityModel::is_owner_Valid() const{
    return m_owner_isValid;
}

QDateTime OAIAdvicentNaviPlanRestApiNetWorthModelsLiabilityModel::getStartDate() const {
    return m_start_date;
}
void OAIAdvicentNaviPlanRestApiNetWorthModelsLiabilityModel::setStartDate(const QDateTime &start_date) {
    m_start_date = start_date;
    m_start_date_isSet = true;
}

bool OAIAdvicentNaviPlanRestApiNetWorthModelsLiabilityModel::is_start_date_Set() const{
    return m_start_date_isSet;
}

bool OAIAdvicentNaviPlanRestApiNetWorthModelsLiabilityModel::is_start_date_Valid() const{
    return m_start_date_isValid;
}

qint32 OAIAdvicentNaviPlanRestApiNetWorthModelsLiabilityModel::getType() const {
    return m_type;
}
void OAIAdvicentNaviPlanRestApiNetWorthModelsLiabilityModel::setType(const qint32 &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIAdvicentNaviPlanRestApiNetWorthModelsLiabilityModel::is_type_Set() const{
    return m_type_isSet;
}

bool OAIAdvicentNaviPlanRestApiNetWorthModelsLiabilityModel::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIAdvicentNaviPlanRestApiNetWorthModelsLiabilityModel::isSet() const {
    bool isObjectUpdated = false;
    do {
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

        if (m_legacy_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_outstanding_principal_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_outstanding_principal_as_of_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_owner.isSet()) {
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

bool OAIAdvicentNaviPlanRestApiNetWorthModelsLiabilityModel::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
