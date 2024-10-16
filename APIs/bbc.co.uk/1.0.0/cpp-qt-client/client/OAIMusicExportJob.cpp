/**
 * Radio & Music Services
 * We encapsulate Radio & Music business logic for iPlayer Radio and BBC Music products on all platforms. We add value by reliably providing the right blend of metadata needed by clients.
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIMusicExportJob.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIMusicExportJob::OAIMusicExportJob(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIMusicExportJob::OAIMusicExportJob() {
    this->initializeModel();
}

OAIMusicExportJob::~OAIMusicExportJob() {}

void OAIMusicExportJob::initializeModel() {

    m_created_at_isSet = false;
    m_created_at_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_job_id_isSet = false;
    m_job_id_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_vendor_isSet = false;
    m_vendor_isValid = false;
}

void OAIMusicExportJob::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIMusicExportJob::fromJsonObject(QJsonObject json) {

    m_created_at_isValid = ::OpenAPI::fromJsonValue(m_created_at, json[QString("created_at")]);
    m_created_at_isSet = !json[QString("created_at")].isNull() && m_created_at_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_job_id_isValid = ::OpenAPI::fromJsonValue(m_job_id, json[QString("job_id")]);
    m_job_id_isSet = !json[QString("job_id")].isNull() && m_job_id_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_vendor_isValid = ::OpenAPI::fromJsonValue(m_vendor, json[QString("vendor")]);
    m_vendor_isSet = !json[QString("vendor")].isNull() && m_vendor_isValid;
}

QString OAIMusicExportJob::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIMusicExportJob::asJsonObject() const {
    QJsonObject obj;
    if (m_created_at_isSet) {
        obj.insert(QString("created_at"), ::OpenAPI::toJsonValue(m_created_at));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_job_id_isSet) {
        obj.insert(QString("job_id"), ::OpenAPI::toJsonValue(m_job_id));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_vendor_isSet) {
        obj.insert(QString("vendor"), ::OpenAPI::toJsonValue(m_vendor));
    }
    return obj;
}

QString OAIMusicExportJob::getCreatedAt() const {
    return m_created_at;
}
void OAIMusicExportJob::setCreatedAt(const QString &created_at) {
    m_created_at = created_at;
    m_created_at_isSet = true;
}

bool OAIMusicExportJob::is_created_at_Set() const{
    return m_created_at_isSet;
}

bool OAIMusicExportJob::is_created_at_Valid() const{
    return m_created_at_isValid;
}

QString OAIMusicExportJob::getId() const {
    return m_id;
}
void OAIMusicExportJob::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIMusicExportJob::is_id_Set() const{
    return m_id_isSet;
}

bool OAIMusicExportJob::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIMusicExportJob::getJobId() const {
    return m_job_id;
}
void OAIMusicExportJob::setJobId(const QString &job_id) {
    m_job_id = job_id;
    m_job_id_isSet = true;
}

bool OAIMusicExportJob::is_job_id_Set() const{
    return m_job_id_isSet;
}

bool OAIMusicExportJob::is_job_id_Valid() const{
    return m_job_id_isValid;
}

QString OAIMusicExportJob::getStatus() const {
    return m_status;
}
void OAIMusicExportJob::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIMusicExportJob::is_status_Set() const{
    return m_status_isSet;
}

bool OAIMusicExportJob::is_status_Valid() const{
    return m_status_isValid;
}

QString OAIMusicExportJob::getVendor() const {
    return m_vendor;
}
void OAIMusicExportJob::setVendor(const QString &vendor) {
    m_vendor = vendor;
    m_vendor_isSet = true;
}

bool OAIMusicExportJob::is_vendor_Set() const{
    return m_vendor_isSet;
}

bool OAIMusicExportJob::is_vendor_Valid() const{
    return m_vendor_isValid;
}

bool OAIMusicExportJob::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_created_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_job_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_vendor_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIMusicExportJob::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_created_at_isValid && m_id_isValid && m_job_id_isValid && m_status_isValid && m_vendor_isValid && true;
}

} // namespace OpenAPI
