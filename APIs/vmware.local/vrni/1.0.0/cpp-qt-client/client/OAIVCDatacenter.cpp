/**
 * vRealize Network Insight API Reference
 * vRealize Network Insight API Reference
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIVCDatacenter.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIVCDatacenter::OAIVCDatacenter(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIVCDatacenter::OAIVCDatacenter() {
    this->initializeModel();
}

OAIVCDatacenter::~OAIVCDatacenter() {}

void OAIVCDatacenter::initializeModel() {

    m_entity_id_isSet = false;
    m_entity_id_isValid = false;

    m_entity_type_isSet = false;
    m_entity_type_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_vcenter_manager_isSet = false;
    m_vcenter_manager_isValid = false;

    m_vendor_id_isSet = false;
    m_vendor_id_isValid = false;
}

void OAIVCDatacenter::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIVCDatacenter::fromJsonObject(QJsonObject json) {

    m_entity_id_isValid = ::OpenAPI::fromJsonValue(m_entity_id, json[QString("entity_id")]);
    m_entity_id_isSet = !json[QString("entity_id")].isNull() && m_entity_id_isValid;

    m_entity_type_isValid = ::OpenAPI::fromJsonValue(m_entity_type, json[QString("entity_type")]);
    m_entity_type_isSet = !json[QString("entity_type")].isNull() && m_entity_type_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_vcenter_manager_isValid = ::OpenAPI::fromJsonValue(m_vcenter_manager, json[QString("vcenter_manager")]);
    m_vcenter_manager_isSet = !json[QString("vcenter_manager")].isNull() && m_vcenter_manager_isValid;

    m_vendor_id_isValid = ::OpenAPI::fromJsonValue(m_vendor_id, json[QString("vendor_id")]);
    m_vendor_id_isSet = !json[QString("vendor_id")].isNull() && m_vendor_id_isValid;
}

QString OAIVCDatacenter::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIVCDatacenter::asJsonObject() const {
    QJsonObject obj;
    if (m_entity_id_isSet) {
        obj.insert(QString("entity_id"), ::OpenAPI::toJsonValue(m_entity_id));
    }
    if (m_entity_type.isSet()) {
        obj.insert(QString("entity_type"), ::OpenAPI::toJsonValue(m_entity_type));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_vcenter_manager.isSet()) {
        obj.insert(QString("vcenter_manager"), ::OpenAPI::toJsonValue(m_vcenter_manager));
    }
    if (m_vendor_id_isSet) {
        obj.insert(QString("vendor_id"), ::OpenAPI::toJsonValue(m_vendor_id));
    }
    return obj;
}

QString OAIVCDatacenter::getEntityId() const {
    return m_entity_id;
}
void OAIVCDatacenter::setEntityId(const QString &entity_id) {
    m_entity_id = entity_id;
    m_entity_id_isSet = true;
}

bool OAIVCDatacenter::is_entity_id_Set() const{
    return m_entity_id_isSet;
}

bool OAIVCDatacenter::is_entity_id_Valid() const{
    return m_entity_id_isValid;
}

OAIEntityType OAIVCDatacenter::getEntityType() const {
    return m_entity_type;
}
void OAIVCDatacenter::setEntityType(const OAIEntityType &entity_type) {
    m_entity_type = entity_type;
    m_entity_type_isSet = true;
}

bool OAIVCDatacenter::is_entity_type_Set() const{
    return m_entity_type_isSet;
}

bool OAIVCDatacenter::is_entity_type_Valid() const{
    return m_entity_type_isValid;
}

QString OAIVCDatacenter::getName() const {
    return m_name;
}
void OAIVCDatacenter::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIVCDatacenter::is_name_Set() const{
    return m_name_isSet;
}

bool OAIVCDatacenter::is_name_Valid() const{
    return m_name_isValid;
}

OAIReference OAIVCDatacenter::getVcenterManager() const {
    return m_vcenter_manager;
}
void OAIVCDatacenter::setVcenterManager(const OAIReference &vcenter_manager) {
    m_vcenter_manager = vcenter_manager;
    m_vcenter_manager_isSet = true;
}

bool OAIVCDatacenter::is_vcenter_manager_Set() const{
    return m_vcenter_manager_isSet;
}

bool OAIVCDatacenter::is_vcenter_manager_Valid() const{
    return m_vcenter_manager_isValid;
}

QString OAIVCDatacenter::getVendorId() const {
    return m_vendor_id;
}
void OAIVCDatacenter::setVendorId(const QString &vendor_id) {
    m_vendor_id = vendor_id;
    m_vendor_id_isSet = true;
}

bool OAIVCDatacenter::is_vendor_id_Set() const{
    return m_vendor_id_isSet;
}

bool OAIVCDatacenter::is_vendor_id_Valid() const{
    return m_vendor_id_isValid;
}

bool OAIVCDatacenter::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_entity_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_entity_type.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_vcenter_manager.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_vendor_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIVCDatacenter::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
