/**
 * Storage Cache Mgmt Client
 * A Storage Cache provides scalable caching service for NAS clients, serving data from either NFSv3 or Blob at-rest storage (referred to as \"Storage Targets\"). These operations allow you to manage caches.
 *
 * The version of the OpenAPI document: 2019-08-01-preview
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIStorageTarget_properties.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIStorageTarget_properties::OAIStorageTarget_properties(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIStorageTarget_properties::OAIStorageTarget_properties() {
    this->initializeModel();
}

OAIStorageTarget_properties::~OAIStorageTarget_properties() {}

void OAIStorageTarget_properties::initializeModel() {

    m_clfs_isSet = false;
    m_clfs_isValid = false;

    m_junctions_isSet = false;
    m_junctions_isValid = false;

    m_nfs3_isSet = false;
    m_nfs3_isValid = false;

    m_provisioning_state_isSet = false;
    m_provisioning_state_isValid = false;

    m_target_type_isSet = false;
    m_target_type_isValid = false;

    m_unknown_isSet = false;
    m_unknown_isValid = false;
}

void OAIStorageTarget_properties::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIStorageTarget_properties::fromJsonObject(QJsonObject json) {

    m_clfs_isValid = ::OpenAPI::fromJsonValue(m_clfs, json[QString("clfs")]);
    m_clfs_isSet = !json[QString("clfs")].isNull() && m_clfs_isValid;

    m_junctions_isValid = ::OpenAPI::fromJsonValue(m_junctions, json[QString("junctions")]);
    m_junctions_isSet = !json[QString("junctions")].isNull() && m_junctions_isValid;

    m_nfs3_isValid = ::OpenAPI::fromJsonValue(m_nfs3, json[QString("nfs3")]);
    m_nfs3_isSet = !json[QString("nfs3")].isNull() && m_nfs3_isValid;

    m_provisioning_state_isValid = ::OpenAPI::fromJsonValue(m_provisioning_state, json[QString("provisioningState")]);
    m_provisioning_state_isSet = !json[QString("provisioningState")].isNull() && m_provisioning_state_isValid;

    m_target_type_isValid = ::OpenAPI::fromJsonValue(m_target_type, json[QString("targetType")]);
    m_target_type_isSet = !json[QString("targetType")].isNull() && m_target_type_isValid;

    m_unknown_isValid = ::OpenAPI::fromJsonValue(m_unknown, json[QString("unknown")]);
    m_unknown_isSet = !json[QString("unknown")].isNull() && m_unknown_isValid;
}

QString OAIStorageTarget_properties::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIStorageTarget_properties::asJsonObject() const {
    QJsonObject obj;
    if (m_clfs.isSet()) {
        obj.insert(QString("clfs"), ::OpenAPI::toJsonValue(m_clfs));
    }
    if (m_junctions.size() > 0) {
        obj.insert(QString("junctions"), ::OpenAPI::toJsonValue(m_junctions));
    }
    if (m_nfs3.isSet()) {
        obj.insert(QString("nfs3"), ::OpenAPI::toJsonValue(m_nfs3));
    }
    if (m_provisioning_state_isSet) {
        obj.insert(QString("provisioningState"), ::OpenAPI::toJsonValue(m_provisioning_state));
    }
    if (m_target_type_isSet) {
        obj.insert(QString("targetType"), ::OpenAPI::toJsonValue(m_target_type));
    }
    if (m_unknown.isSet()) {
        obj.insert(QString("unknown"), ::OpenAPI::toJsonValue(m_unknown));
    }
    return obj;
}

OAIClfsTarget OAIStorageTarget_properties::getClfs() const {
    return m_clfs;
}
void OAIStorageTarget_properties::setClfs(const OAIClfsTarget &clfs) {
    m_clfs = clfs;
    m_clfs_isSet = true;
}

bool OAIStorageTarget_properties::is_clfs_Set() const{
    return m_clfs_isSet;
}

bool OAIStorageTarget_properties::is_clfs_Valid() const{
    return m_clfs_isValid;
}

QList<OAINamespaceJunction> OAIStorageTarget_properties::getJunctions() const {
    return m_junctions;
}
void OAIStorageTarget_properties::setJunctions(const QList<OAINamespaceJunction> &junctions) {
    m_junctions = junctions;
    m_junctions_isSet = true;
}

bool OAIStorageTarget_properties::is_junctions_Set() const{
    return m_junctions_isSet;
}

bool OAIStorageTarget_properties::is_junctions_Valid() const{
    return m_junctions_isValid;
}

OAINfs3Target OAIStorageTarget_properties::getNfs3() const {
    return m_nfs3;
}
void OAIStorageTarget_properties::setNfs3(const OAINfs3Target &nfs3) {
    m_nfs3 = nfs3;
    m_nfs3_isSet = true;
}

bool OAIStorageTarget_properties::is_nfs3_Set() const{
    return m_nfs3_isSet;
}

bool OAIStorageTarget_properties::is_nfs3_Valid() const{
    return m_nfs3_isValid;
}

QString OAIStorageTarget_properties::getProvisioningState() const {
    return m_provisioning_state;
}
void OAIStorageTarget_properties::setProvisioningState(const QString &provisioning_state) {
    m_provisioning_state = provisioning_state;
    m_provisioning_state_isSet = true;
}

bool OAIStorageTarget_properties::is_provisioning_state_Set() const{
    return m_provisioning_state_isSet;
}

bool OAIStorageTarget_properties::is_provisioning_state_Valid() const{
    return m_provisioning_state_isValid;
}

QString OAIStorageTarget_properties::getTargetType() const {
    return m_target_type;
}
void OAIStorageTarget_properties::setTargetType(const QString &target_type) {
    m_target_type = target_type;
    m_target_type_isSet = true;
}

bool OAIStorageTarget_properties::is_target_type_Set() const{
    return m_target_type_isSet;
}

bool OAIStorageTarget_properties::is_target_type_Valid() const{
    return m_target_type_isValid;
}

OAIUnknownTarget OAIStorageTarget_properties::getUnknown() const {
    return m_unknown;
}
void OAIStorageTarget_properties::setUnknown(const OAIUnknownTarget &unknown) {
    m_unknown = unknown;
    m_unknown_isSet = true;
}

bool OAIStorageTarget_properties::is_unknown_Set() const{
    return m_unknown_isSet;
}

bool OAIStorageTarget_properties::is_unknown_Valid() const{
    return m_unknown_isValid;
}

bool OAIStorageTarget_properties::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_clfs.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_junctions.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_nfs3.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_provisioning_state_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_target_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_unknown.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIStorageTarget_properties::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
