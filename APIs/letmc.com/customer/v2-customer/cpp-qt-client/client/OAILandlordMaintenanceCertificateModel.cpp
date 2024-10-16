/**
 * agentOS Api V2, Customer Login Call Group
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v2-customer
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAILandlordMaintenanceCertificateModel.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAILandlordMaintenanceCertificateModel::OAILandlordMaintenanceCertificateModel(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAILandlordMaintenanceCertificateModel::OAILandlordMaintenanceCertificateModel() {
    this->initializeModel();
}

OAILandlordMaintenanceCertificateModel::~OAILandlordMaintenanceCertificateModel() {}

void OAILandlordMaintenanceCertificateModel::initializeModel() {

    m_due_isSet = false;
    m_due_isValid = false;

    m_files_isSet = false;
    m_files_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAILandlordMaintenanceCertificateModel::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAILandlordMaintenanceCertificateModel::fromJsonObject(QJsonObject json) {

    m_due_isValid = ::OpenAPI::fromJsonValue(m_due, json[QString("Due")]);
    m_due_isSet = !json[QString("Due")].isNull() && m_due_isValid;

    m_files_isValid = ::OpenAPI::fromJsonValue(m_files, json[QString("Files")]);
    m_files_isSet = !json[QString("Files")].isNull() && m_files_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("Status")]);
    m_status_isSet = !json[QString("Status")].isNull() && m_status_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("Type")]);
    m_type_isSet = !json[QString("Type")].isNull() && m_type_isValid;
}

QString OAILandlordMaintenanceCertificateModel::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAILandlordMaintenanceCertificateModel::asJsonObject() const {
    QJsonObject obj;
    if (m_due_isSet) {
        obj.insert(QString("Due"), ::OpenAPI::toJsonValue(m_due));
    }
    if (m_files.size() > 0) {
        obj.insert(QString("Files"), ::OpenAPI::toJsonValue(m_files));
    }
    if (m_status_isSet) {
        obj.insert(QString("Status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_type_isSet) {
        obj.insert(QString("Type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

QDateTime OAILandlordMaintenanceCertificateModel::getDue() const {
    return m_due;
}
void OAILandlordMaintenanceCertificateModel::setDue(const QDateTime &due) {
    m_due = due;
    m_due_isSet = true;
}

bool OAILandlordMaintenanceCertificateModel::is_due_Set() const{
    return m_due_isSet;
}

bool OAILandlordMaintenanceCertificateModel::is_due_Valid() const{
    return m_due_isValid;
}

QList<OAILettingsLandlordDocument> OAILandlordMaintenanceCertificateModel::getFiles() const {
    return m_files;
}
void OAILandlordMaintenanceCertificateModel::setFiles(const QList<OAILettingsLandlordDocument> &files) {
    m_files = files;
    m_files_isSet = true;
}

bool OAILandlordMaintenanceCertificateModel::is_files_Set() const{
    return m_files_isSet;
}

bool OAILandlordMaintenanceCertificateModel::is_files_Valid() const{
    return m_files_isValid;
}

QString OAILandlordMaintenanceCertificateModel::getStatus() const {
    return m_status;
}
void OAILandlordMaintenanceCertificateModel::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAILandlordMaintenanceCertificateModel::is_status_Set() const{
    return m_status_isSet;
}

bool OAILandlordMaintenanceCertificateModel::is_status_Valid() const{
    return m_status_isValid;
}

QString OAILandlordMaintenanceCertificateModel::getType() const {
    return m_type;
}
void OAILandlordMaintenanceCertificateModel::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAILandlordMaintenanceCertificateModel::is_type_Set() const{
    return m_type_isSet;
}

bool OAILandlordMaintenanceCertificateModel::is_type_Valid() const{
    return m_type_isValid;
}

bool OAILandlordMaintenanceCertificateModel::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_due_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_files.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
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

bool OAILandlordMaintenanceCertificateModel::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
