/**
 * Noosh API application
 * Full description of Noosh API
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAISpecSimpleVO.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISpecSimpleVO::OAISpecSimpleVO(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISpecSimpleVO::OAISpecSimpleVO() {
    this->initializeModel();
}

OAISpecSimpleVO::~OAISpecSimpleVO() {}

void OAISpecSimpleVO::initializeModel() {

    m_client_status_isSet = false;
    m_client_status_isValid = false;

    m_create_date_isSet = false;
    m_create_date_isValid = false;

    m_created_by_isSet = false;
    m_created_by_isValid = false;

    m_job_id_isSet = false;
    m_job_id_isValid = false;

    m_last_updated_isSet = false;
    m_last_updated_isValid = false;

    m_reference_number_isSet = false;
    m_reference_number_isValid = false;

    m_spec_id_isSet = false;
    m_spec_id_isValid = false;

    m_spec_name_isSet = false;
    m_spec_name_isValid = false;

    m_spec_options_complete_isSet = false;
    m_spec_options_complete_isValid = false;

    m_supplier_status_isSet = false;
    m_supplier_status_isValid = false;

    m_uofms_isSet = false;
    m_uofms_isValid = false;

    m_user_state_isSet = false;
    m_user_state_isValid = false;
}

void OAISpecSimpleVO::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISpecSimpleVO::fromJsonObject(QJsonObject json) {

    m_client_status_isValid = ::OpenAPI::fromJsonValue(m_client_status, json[QString("client_status")]);
    m_client_status_isSet = !json[QString("client_status")].isNull() && m_client_status_isValid;

    m_create_date_isValid = ::OpenAPI::fromJsonValue(m_create_date, json[QString("create_date")]);
    m_create_date_isSet = !json[QString("create_date")].isNull() && m_create_date_isValid;

    m_created_by_isValid = ::OpenAPI::fromJsonValue(m_created_by, json[QString("created_by")]);
    m_created_by_isSet = !json[QString("created_by")].isNull() && m_created_by_isValid;

    m_job_id_isValid = ::OpenAPI::fromJsonValue(m_job_id, json[QString("job_id")]);
    m_job_id_isSet = !json[QString("job_id")].isNull() && m_job_id_isValid;

    m_last_updated_isValid = ::OpenAPI::fromJsonValue(m_last_updated, json[QString("last_updated")]);
    m_last_updated_isSet = !json[QString("last_updated")].isNull() && m_last_updated_isValid;

    m_reference_number_isValid = ::OpenAPI::fromJsonValue(m_reference_number, json[QString("reference_number")]);
    m_reference_number_isSet = !json[QString("reference_number")].isNull() && m_reference_number_isValid;

    m_spec_id_isValid = ::OpenAPI::fromJsonValue(m_spec_id, json[QString("spec_id")]);
    m_spec_id_isSet = !json[QString("spec_id")].isNull() && m_spec_id_isValid;

    m_spec_name_isValid = ::OpenAPI::fromJsonValue(m_spec_name, json[QString("spec_name")]);
    m_spec_name_isSet = !json[QString("spec_name")].isNull() && m_spec_name_isValid;

    m_spec_options_complete_isValid = ::OpenAPI::fromJsonValue(m_spec_options_complete, json[QString("spec_options_complete")]);
    m_spec_options_complete_isSet = !json[QString("spec_options_complete")].isNull() && m_spec_options_complete_isValid;

    m_supplier_status_isValid = ::OpenAPI::fromJsonValue(m_supplier_status, json[QString("supplier_status")]);
    m_supplier_status_isSet = !json[QString("supplier_status")].isNull() && m_supplier_status_isValid;

    m_uofms_isValid = ::OpenAPI::fromJsonValue(m_uofms, json[QString("uofms")]);
    m_uofms_isSet = !json[QString("uofms")].isNull() && m_uofms_isValid;

    m_user_state_isValid = ::OpenAPI::fromJsonValue(m_user_state, json[QString("user_state")]);
    m_user_state_isSet = !json[QString("user_state")].isNull() && m_user_state_isValid;
}

QString OAISpecSimpleVO::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISpecSimpleVO::asJsonObject() const {
    QJsonObject obj;
    if (m_client_status_isSet) {
        obj.insert(QString("client_status"), ::OpenAPI::toJsonValue(m_client_status));
    }
    if (m_create_date_isSet) {
        obj.insert(QString("create_date"), ::OpenAPI::toJsonValue(m_create_date));
    }
    if (m_created_by.isSet()) {
        obj.insert(QString("created_by"), ::OpenAPI::toJsonValue(m_created_by));
    }
    if (m_job_id_isSet) {
        obj.insert(QString("job_id"), ::OpenAPI::toJsonValue(m_job_id));
    }
    if (m_last_updated_isSet) {
        obj.insert(QString("last_updated"), ::OpenAPI::toJsonValue(m_last_updated));
    }
    if (m_reference_number_isSet) {
        obj.insert(QString("reference_number"), ::OpenAPI::toJsonValue(m_reference_number));
    }
    if (m_spec_id_isSet) {
        obj.insert(QString("spec_id"), ::OpenAPI::toJsonValue(m_spec_id));
    }
    if (m_spec_name_isSet) {
        obj.insert(QString("spec_name"), ::OpenAPI::toJsonValue(m_spec_name));
    }
    if (m_spec_options_complete.size() > 0) {
        obj.insert(QString("spec_options_complete"), ::OpenAPI::toJsonValue(m_spec_options_complete));
    }
    if (m_supplier_status_isSet) {
        obj.insert(QString("supplier_status"), ::OpenAPI::toJsonValue(m_supplier_status));
    }
    if (m_uofms.size() > 0) {
        obj.insert(QString("uofms"), ::OpenAPI::toJsonValue(m_uofms));
    }
    if (m_user_state_isSet) {
        obj.insert(QString("user_state"), ::OpenAPI::toJsonValue(m_user_state));
    }
    return obj;
}

QString OAISpecSimpleVO::getClientStatus() const {
    return m_client_status;
}
void OAISpecSimpleVO::setClientStatus(const QString &client_status) {
    m_client_status = client_status;
    m_client_status_isSet = true;
}

bool OAISpecSimpleVO::is_client_status_Set() const{
    return m_client_status_isSet;
}

bool OAISpecSimpleVO::is_client_status_Valid() const{
    return m_client_status_isValid;
}

QDate OAISpecSimpleVO::getCreateDate() const {
    return m_create_date;
}
void OAISpecSimpleVO::setCreateDate(const QDate &create_date) {
    m_create_date = create_date;
    m_create_date_isSet = true;
}

bool OAISpecSimpleVO::is_create_date_Set() const{
    return m_create_date_isSet;
}

bool OAISpecSimpleVO::is_create_date_Valid() const{
    return m_create_date_isValid;
}

OAIPersonVO OAISpecSimpleVO::getCreatedBy() const {
    return m_created_by;
}
void OAISpecSimpleVO::setCreatedBy(const OAIPersonVO &created_by) {
    m_created_by = created_by;
    m_created_by_isSet = true;
}

bool OAISpecSimpleVO::is_created_by_Set() const{
    return m_created_by_isSet;
}

bool OAISpecSimpleVO::is_created_by_Valid() const{
    return m_created_by_isValid;
}

qint64 OAISpecSimpleVO::getJobId() const {
    return m_job_id;
}
void OAISpecSimpleVO::setJobId(const qint64 &job_id) {
    m_job_id = job_id;
    m_job_id_isSet = true;
}

bool OAISpecSimpleVO::is_job_id_Set() const{
    return m_job_id_isSet;
}

bool OAISpecSimpleVO::is_job_id_Valid() const{
    return m_job_id_isValid;
}

QDate OAISpecSimpleVO::getLastUpdated() const {
    return m_last_updated;
}
void OAISpecSimpleVO::setLastUpdated(const QDate &last_updated) {
    m_last_updated = last_updated;
    m_last_updated_isSet = true;
}

bool OAISpecSimpleVO::is_last_updated_Set() const{
    return m_last_updated_isSet;
}

bool OAISpecSimpleVO::is_last_updated_Valid() const{
    return m_last_updated_isValid;
}

QString OAISpecSimpleVO::getReferenceNumber() const {
    return m_reference_number;
}
void OAISpecSimpleVO::setReferenceNumber(const QString &reference_number) {
    m_reference_number = reference_number;
    m_reference_number_isSet = true;
}

bool OAISpecSimpleVO::is_reference_number_Set() const{
    return m_reference_number_isSet;
}

bool OAISpecSimpleVO::is_reference_number_Valid() const{
    return m_reference_number_isValid;
}

qint64 OAISpecSimpleVO::getSpecId() const {
    return m_spec_id;
}
void OAISpecSimpleVO::setSpecId(const qint64 &spec_id) {
    m_spec_id = spec_id;
    m_spec_id_isSet = true;
}

bool OAISpecSimpleVO::is_spec_id_Set() const{
    return m_spec_id_isSet;
}

bool OAISpecSimpleVO::is_spec_id_Valid() const{
    return m_spec_id_isValid;
}

QString OAISpecSimpleVO::getSpecName() const {
    return m_spec_name;
}
void OAISpecSimpleVO::setSpecName(const QString &spec_name) {
    m_spec_name = spec_name;
    m_spec_name_isSet = true;
}

bool OAISpecSimpleVO::is_spec_name_Set() const{
    return m_spec_name_isSet;
}

bool OAISpecSimpleVO::is_spec_name_Valid() const{
    return m_spec_name_isValid;
}

QList<OAISpecSimpleVO> OAISpecSimpleVO::getSpecOptionsComplete() const {
    return m_spec_options_complete;
}
void OAISpecSimpleVO::setSpecOptionsComplete(const QList<OAISpecSimpleVO> &spec_options_complete) {
    m_spec_options_complete = spec_options_complete;
    m_spec_options_complete_isSet = true;
}

bool OAISpecSimpleVO::is_spec_options_complete_Set() const{
    return m_spec_options_complete_isSet;
}

bool OAISpecSimpleVO::is_spec_options_complete_Valid() const{
    return m_spec_options_complete_isValid;
}

QString OAISpecSimpleVO::getSupplierStatus() const {
    return m_supplier_status;
}
void OAISpecSimpleVO::setSupplierStatus(const QString &supplier_status) {
    m_supplier_status = supplier_status;
    m_supplier_status_isSet = true;
}

bool OAISpecSimpleVO::is_supplier_status_Set() const{
    return m_supplier_status_isSet;
}

bool OAISpecSimpleVO::is_supplier_status_Valid() const{
    return m_supplier_status_isValid;
}

QList<OAIUofmSimpleVO> OAISpecSimpleVO::getUofms() const {
    return m_uofms;
}
void OAISpecSimpleVO::setUofms(const QList<OAIUofmSimpleVO> &uofms) {
    m_uofms = uofms;
    m_uofms_isSet = true;
}

bool OAISpecSimpleVO::is_uofms_Set() const{
    return m_uofms_isSet;
}

bool OAISpecSimpleVO::is_uofms_Valid() const{
    return m_uofms_isValid;
}

QString OAISpecSimpleVO::getUserState() const {
    return m_user_state;
}
void OAISpecSimpleVO::setUserState(const QString &user_state) {
    m_user_state = user_state;
    m_user_state_isSet = true;
}

bool OAISpecSimpleVO::is_user_state_Set() const{
    return m_user_state_isSet;
}

bool OAISpecSimpleVO::is_user_state_Valid() const{
    return m_user_state_isValid;
}

bool OAISpecSimpleVO::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_client_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_create_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_by.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_job_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_updated_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_reference_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_spec_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_spec_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_spec_options_complete.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_supplier_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_uofms.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_user_state_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISpecSimpleVO::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
