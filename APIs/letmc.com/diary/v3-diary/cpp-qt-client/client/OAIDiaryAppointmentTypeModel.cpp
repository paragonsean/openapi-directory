/**
 * agentOS API V3, Diary Call Group
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v3-diary
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIDiaryAppointmentTypeModel.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIDiaryAppointmentTypeModel::OAIDiaryAppointmentTypeModel(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIDiaryAppointmentTypeModel::OAIDiaryAppointmentTypeModel() {
    this->initializeModel();
}

OAIDiaryAppointmentTypeModel::~OAIDiaryAppointmentTypeModel() {}

void OAIDiaryAppointmentTypeModel::initializeModel() {

    m_e_tag_isSet = false;
    m_e_tag_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_oid_isSet = false;
    m_oid_isValid = false;

    m_system_type_isSet = false;
    m_system_type_isValid = false;
}

void OAIDiaryAppointmentTypeModel::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIDiaryAppointmentTypeModel::fromJsonObject(QJsonObject json) {

    m_e_tag_isValid = ::OpenAPI::fromJsonValue(m_e_tag, json[QString("ETag")]);
    m_e_tag_isSet = !json[QString("ETag")].isNull() && m_e_tag_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("Name")]);
    m_name_isSet = !json[QString("Name")].isNull() && m_name_isValid;

    m_oid_isValid = ::OpenAPI::fromJsonValue(m_oid, json[QString("OID")]);
    m_oid_isSet = !json[QString("OID")].isNull() && m_oid_isValid;

    m_system_type_isValid = ::OpenAPI::fromJsonValue(m_system_type, json[QString("SystemType")]);
    m_system_type_isSet = !json[QString("SystemType")].isNull() && m_system_type_isValid;
}

QString OAIDiaryAppointmentTypeModel::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIDiaryAppointmentTypeModel::asJsonObject() const {
    QJsonObject obj;
    if (m_e_tag_isSet) {
        obj.insert(QString("ETag"), ::OpenAPI::toJsonValue(m_e_tag));
    }
    if (m_name_isSet) {
        obj.insert(QString("Name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_oid_isSet) {
        obj.insert(QString("OID"), ::OpenAPI::toJsonValue(m_oid));
    }
    if (m_system_type_isSet) {
        obj.insert(QString("SystemType"), ::OpenAPI::toJsonValue(m_system_type));
    }
    return obj;
}

QString OAIDiaryAppointmentTypeModel::getETag() const {
    return m_e_tag;
}
void OAIDiaryAppointmentTypeModel::setETag(const QString &e_tag) {
    m_e_tag = e_tag;
    m_e_tag_isSet = true;
}

bool OAIDiaryAppointmentTypeModel::is_e_tag_Set() const{
    return m_e_tag_isSet;
}

bool OAIDiaryAppointmentTypeModel::is_e_tag_Valid() const{
    return m_e_tag_isValid;
}

QString OAIDiaryAppointmentTypeModel::getName() const {
    return m_name;
}
void OAIDiaryAppointmentTypeModel::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIDiaryAppointmentTypeModel::is_name_Set() const{
    return m_name_isSet;
}

bool OAIDiaryAppointmentTypeModel::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIDiaryAppointmentTypeModel::getOid() const {
    return m_oid;
}
void OAIDiaryAppointmentTypeModel::setOid(const QString &oid) {
    m_oid = oid;
    m_oid_isSet = true;
}

bool OAIDiaryAppointmentTypeModel::is_oid_Set() const{
    return m_oid_isSet;
}

bool OAIDiaryAppointmentTypeModel::is_oid_Valid() const{
    return m_oid_isValid;
}

QString OAIDiaryAppointmentTypeModel::getSystemType() const {
    return m_system_type;
}
void OAIDiaryAppointmentTypeModel::setSystemType(const QString &system_type) {
    m_system_type = system_type;
    m_system_type_isSet = true;
}

bool OAIDiaryAppointmentTypeModel::is_system_type_Set() const{
    return m_system_type_isSet;
}

bool OAIDiaryAppointmentTypeModel::is_system_type_Valid() const{
    return m_system_type_isValid;
}

bool OAIDiaryAppointmentTypeModel::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_e_tag_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_oid_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_system_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIDiaryAppointmentTypeModel::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
