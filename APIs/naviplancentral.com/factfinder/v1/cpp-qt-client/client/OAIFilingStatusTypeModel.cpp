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

#include "OAIFilingStatusTypeModel.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIFilingStatusTypeModel::OAIFilingStatusTypeModel(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIFilingStatusTypeModel::OAIFilingStatusTypeModel() {
    this->initializeModel();
}

OAIFilingStatusTypeModel::~OAIFilingStatusTypeModel() {}

void OAIFilingStatusTypeModel::initializeModel() {

    m_filing_status_type_id_isSet = false;
    m_filing_status_type_id_isValid = false;

    m_filing_status_type_name_isSet = false;
    m_filing_status_type_name_isValid = false;

    m_has_joint_dependent_isSet = false;
    m_has_joint_dependent_isValid = false;

    m_links_isSet = false;
    m_links_isValid = false;

    m_partner_statuses_isSet = false;
    m_partner_statuses_isValid = false;

    m_valid_for_single_analysis_isSet = false;
    m_valid_for_single_analysis_isValid = false;
}

void OAIFilingStatusTypeModel::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIFilingStatusTypeModel::fromJsonObject(QJsonObject json) {

    m_filing_status_type_id_isValid = ::OpenAPI::fromJsonValue(m_filing_status_type_id, json[QString("filingStatusTypeId")]);
    m_filing_status_type_id_isSet = !json[QString("filingStatusTypeId")].isNull() && m_filing_status_type_id_isValid;

    m_filing_status_type_name_isValid = ::OpenAPI::fromJsonValue(m_filing_status_type_name, json[QString("filingStatusTypeName")]);
    m_filing_status_type_name_isSet = !json[QString("filingStatusTypeName")].isNull() && m_filing_status_type_name_isValid;

    m_has_joint_dependent_isValid = ::OpenAPI::fromJsonValue(m_has_joint_dependent, json[QString("hasJointDependent")]);
    m_has_joint_dependent_isSet = !json[QString("hasJointDependent")].isNull() && m_has_joint_dependent_isValid;

    m_links_isValid = ::OpenAPI::fromJsonValue(m_links, json[QString("links")]);
    m_links_isSet = !json[QString("links")].isNull() && m_links_isValid;

    m_partner_statuses_isValid = ::OpenAPI::fromJsonValue(m_partner_statuses, json[QString("partnerStatuses")]);
    m_partner_statuses_isSet = !json[QString("partnerStatuses")].isNull() && m_partner_statuses_isValid;

    m_valid_for_single_analysis_isValid = ::OpenAPI::fromJsonValue(m_valid_for_single_analysis, json[QString("validForSingleAnalysis")]);
    m_valid_for_single_analysis_isSet = !json[QString("validForSingleAnalysis")].isNull() && m_valid_for_single_analysis_isValid;
}

QString OAIFilingStatusTypeModel::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIFilingStatusTypeModel::asJsonObject() const {
    QJsonObject obj;
    if (m_filing_status_type_id_isSet) {
        obj.insert(QString("filingStatusTypeId"), ::OpenAPI::toJsonValue(m_filing_status_type_id));
    }
    if (m_filing_status_type_name_isSet) {
        obj.insert(QString("filingStatusTypeName"), ::OpenAPI::toJsonValue(m_filing_status_type_name));
    }
    if (m_has_joint_dependent_isSet) {
        obj.insert(QString("hasJointDependent"), ::OpenAPI::toJsonValue(m_has_joint_dependent));
    }
    if (m_links.size() > 0) {
        obj.insert(QString("links"), ::OpenAPI::toJsonValue(m_links));
    }
    if (m_partner_statuses.size() > 0) {
        obj.insert(QString("partnerStatuses"), ::OpenAPI::toJsonValue(m_partner_statuses));
    }
    if (m_valid_for_single_analysis_isSet) {
        obj.insert(QString("validForSingleAnalysis"), ::OpenAPI::toJsonValue(m_valid_for_single_analysis));
    }
    return obj;
}

qint32 OAIFilingStatusTypeModel::getFilingStatusTypeId() const {
    return m_filing_status_type_id;
}
void OAIFilingStatusTypeModel::setFilingStatusTypeId(const qint32 &filing_status_type_id) {
    m_filing_status_type_id = filing_status_type_id;
    m_filing_status_type_id_isSet = true;
}

bool OAIFilingStatusTypeModel::is_filing_status_type_id_Set() const{
    return m_filing_status_type_id_isSet;
}

bool OAIFilingStatusTypeModel::is_filing_status_type_id_Valid() const{
    return m_filing_status_type_id_isValid;
}

QString OAIFilingStatusTypeModel::getFilingStatusTypeName() const {
    return m_filing_status_type_name;
}
void OAIFilingStatusTypeModel::setFilingStatusTypeName(const QString &filing_status_type_name) {
    m_filing_status_type_name = filing_status_type_name;
    m_filing_status_type_name_isSet = true;
}

bool OAIFilingStatusTypeModel::is_filing_status_type_name_Set() const{
    return m_filing_status_type_name_isSet;
}

bool OAIFilingStatusTypeModel::is_filing_status_type_name_Valid() const{
    return m_filing_status_type_name_isValid;
}

bool OAIFilingStatusTypeModel::isHasJointDependent() const {
    return m_has_joint_dependent;
}
void OAIFilingStatusTypeModel::setHasJointDependent(const bool &has_joint_dependent) {
    m_has_joint_dependent = has_joint_dependent;
    m_has_joint_dependent_isSet = true;
}

bool OAIFilingStatusTypeModel::is_has_joint_dependent_Set() const{
    return m_has_joint_dependent_isSet;
}

bool OAIFilingStatusTypeModel::is_has_joint_dependent_Valid() const{
    return m_has_joint_dependent_isValid;
}

QList<OAIObjectLink> OAIFilingStatusTypeModel::getLinks() const {
    return m_links;
}
void OAIFilingStatusTypeModel::setLinks(const QList<OAIObjectLink> &links) {
    m_links = links;
    m_links_isSet = true;
}

bool OAIFilingStatusTypeModel::is_links_Set() const{
    return m_links_isSet;
}

bool OAIFilingStatusTypeModel::is_links_Valid() const{
    return m_links_isValid;
}

QList<qint32> OAIFilingStatusTypeModel::getPartnerStatuses() const {
    return m_partner_statuses;
}
void OAIFilingStatusTypeModel::setPartnerStatuses(const QList<qint32> &partner_statuses) {
    m_partner_statuses = partner_statuses;
    m_partner_statuses_isSet = true;
}

bool OAIFilingStatusTypeModel::is_partner_statuses_Set() const{
    return m_partner_statuses_isSet;
}

bool OAIFilingStatusTypeModel::is_partner_statuses_Valid() const{
    return m_partner_statuses_isValid;
}

bool OAIFilingStatusTypeModel::isValidForSingleAnalysis() const {
    return m_valid_for_single_analysis;
}
void OAIFilingStatusTypeModel::setValidForSingleAnalysis(const bool &valid_for_single_analysis) {
    m_valid_for_single_analysis = valid_for_single_analysis;
    m_valid_for_single_analysis_isSet = true;
}

bool OAIFilingStatusTypeModel::is_valid_for_single_analysis_Set() const{
    return m_valid_for_single_analysis_isSet;
}

bool OAIFilingStatusTypeModel::is_valid_for_single_analysis_Valid() const{
    return m_valid_for_single_analysis_isValid;
}

bool OAIFilingStatusTypeModel::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_filing_status_type_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_filing_status_type_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_has_joint_dependent_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_links.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_partner_statuses.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_valid_for_single_analysis_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIFilingStatusTypeModel::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
