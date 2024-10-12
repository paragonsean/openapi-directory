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

#include "OAIEC2NetworkInterface.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIEC2NetworkInterface::OAIEC2NetworkInterface(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIEC2NetworkInterface::OAIEC2NetworkInterface() {
    this->initializeModel();
}

OAIEC2NetworkInterface::~OAIEC2NetworkInterface() {}

void OAIEC2NetworkInterface::initializeModel() {

    m_entity_id_isSet = false;
    m_entity_id_isValid = false;

    m_entity_type_isSet = false;
    m_entity_type_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_ip_addresses_isSet = false;
    m_ip_addresses_isValid = false;

    m_layer2_network_isSet = false;
    m_layer2_network_isValid = false;

    m_vlan_isSet = false;
    m_vlan_isValid = false;

    m_vm_isSet = false;
    m_vm_isValid = false;
}

void OAIEC2NetworkInterface::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIEC2NetworkInterface::fromJsonObject(QJsonObject json) {

    m_entity_id_isValid = ::OpenAPI::fromJsonValue(m_entity_id, json[QString("entity_id")]);
    m_entity_id_isSet = !json[QString("entity_id")].isNull() && m_entity_id_isValid;

    m_entity_type_isValid = ::OpenAPI::fromJsonValue(m_entity_type, json[QString("entity_type")]);
    m_entity_type_isSet = !json[QString("entity_type")].isNull() && m_entity_type_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_ip_addresses_isValid = ::OpenAPI::fromJsonValue(m_ip_addresses, json[QString("ip_addresses")]);
    m_ip_addresses_isSet = !json[QString("ip_addresses")].isNull() && m_ip_addresses_isValid;

    m_layer2_network_isValid = ::OpenAPI::fromJsonValue(m_layer2_network, json[QString("layer2_network")]);
    m_layer2_network_isSet = !json[QString("layer2_network")].isNull() && m_layer2_network_isValid;

    m_vlan_isValid = ::OpenAPI::fromJsonValue(m_vlan, json[QString("vlan")]);
    m_vlan_isSet = !json[QString("vlan")].isNull() && m_vlan_isValid;

    m_vm_isValid = ::OpenAPI::fromJsonValue(m_vm, json[QString("vm")]);
    m_vm_isSet = !json[QString("vm")].isNull() && m_vm_isValid;
}

QString OAIEC2NetworkInterface::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIEC2NetworkInterface::asJsonObject() const {
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
    if (m_ip_addresses.size() > 0) {
        obj.insert(QString("ip_addresses"), ::OpenAPI::toJsonValue(m_ip_addresses));
    }
    if (m_layer2_network.isSet()) {
        obj.insert(QString("layer2_network"), ::OpenAPI::toJsonValue(m_layer2_network));
    }
    if (m_vlan.isSet()) {
        obj.insert(QString("vlan"), ::OpenAPI::toJsonValue(m_vlan));
    }
    if (m_vm.isSet()) {
        obj.insert(QString("vm"), ::OpenAPI::toJsonValue(m_vm));
    }
    return obj;
}

QString OAIEC2NetworkInterface::getEntityId() const {
    return m_entity_id;
}
void OAIEC2NetworkInterface::setEntityId(const QString &entity_id) {
    m_entity_id = entity_id;
    m_entity_id_isSet = true;
}

bool OAIEC2NetworkInterface::is_entity_id_Set() const{
    return m_entity_id_isSet;
}

bool OAIEC2NetworkInterface::is_entity_id_Valid() const{
    return m_entity_id_isValid;
}

OAIEntityType OAIEC2NetworkInterface::getEntityType() const {
    return m_entity_type;
}
void OAIEC2NetworkInterface::setEntityType(const OAIEntityType &entity_type) {
    m_entity_type = entity_type;
    m_entity_type_isSet = true;
}

bool OAIEC2NetworkInterface::is_entity_type_Set() const{
    return m_entity_type_isSet;
}

bool OAIEC2NetworkInterface::is_entity_type_Valid() const{
    return m_entity_type_isValid;
}

QString OAIEC2NetworkInterface::getName() const {
    return m_name;
}
void OAIEC2NetworkInterface::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIEC2NetworkInterface::is_name_Set() const{
    return m_name_isSet;
}

bool OAIEC2NetworkInterface::is_name_Valid() const{
    return m_name_isValid;
}

QList<OAIIpV4Address> OAIEC2NetworkInterface::getIpAddresses() const {
    return m_ip_addresses;
}
void OAIEC2NetworkInterface::setIpAddresses(const QList<OAIIpV4Address> &ip_addresses) {
    m_ip_addresses = ip_addresses;
    m_ip_addresses_isSet = true;
}

bool OAIEC2NetworkInterface::is_ip_addresses_Set() const{
    return m_ip_addresses_isSet;
}

bool OAIEC2NetworkInterface::is_ip_addresses_Valid() const{
    return m_ip_addresses_isValid;
}

OAIReference OAIEC2NetworkInterface::getLayer2Network() const {
    return m_layer2_network;
}
void OAIEC2NetworkInterface::setLayer2Network(const OAIReference &layer2_network) {
    m_layer2_network = layer2_network;
    m_layer2_network_isSet = true;
}

bool OAIEC2NetworkInterface::is_layer2_network_Set() const{
    return m_layer2_network_isSet;
}

bool OAIEC2NetworkInterface::is_layer2_network_Valid() const{
    return m_layer2_network_isValid;
}

OAIVlan OAIEC2NetworkInterface::getVlan() const {
    return m_vlan;
}
void OAIEC2NetworkInterface::setVlan(const OAIVlan &vlan) {
    m_vlan = vlan;
    m_vlan_isSet = true;
}

bool OAIEC2NetworkInterface::is_vlan_Set() const{
    return m_vlan_isSet;
}

bool OAIEC2NetworkInterface::is_vlan_Valid() const{
    return m_vlan_isValid;
}

OAIReference OAIEC2NetworkInterface::getVm() const {
    return m_vm;
}
void OAIEC2NetworkInterface::setVm(const OAIReference &vm) {
    m_vm = vm;
    m_vm_isSet = true;
}

bool OAIEC2NetworkInterface::is_vm_Set() const{
    return m_vm_isSet;
}

bool OAIEC2NetworkInterface::is_vm_Valid() const{
    return m_vm_isValid;
}

bool OAIEC2NetworkInterface::isSet() const {
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

        if (m_ip_addresses.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_layer2_network.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_vlan.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_vm.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIEC2NetworkInterface::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
