/**
 * ManagedLabsClient
 * The Managed Labs Client.
 *
 * The version of the OpenAPI document: 2018-10-15
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIResourceSet.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIResourceSet::OAIResourceSet(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIResourceSet::OAIResourceSet() {
    this->initializeModel();
}

OAIResourceSet::~OAIResourceSet() {}

void OAIResourceSet::initializeModel() {

    m_resource_setting_id_isSet = false;
    m_resource_setting_id_isValid = false;

    m_vm_resource_id_isSet = false;
    m_vm_resource_id_isValid = false;
}

void OAIResourceSet::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIResourceSet::fromJsonObject(QJsonObject json) {

    m_resource_setting_id_isValid = ::OpenAPI::fromJsonValue(m_resource_setting_id, json[QString("resourceSettingId")]);
    m_resource_setting_id_isSet = !json[QString("resourceSettingId")].isNull() && m_resource_setting_id_isValid;

    m_vm_resource_id_isValid = ::OpenAPI::fromJsonValue(m_vm_resource_id, json[QString("vmResourceId")]);
    m_vm_resource_id_isSet = !json[QString("vmResourceId")].isNull() && m_vm_resource_id_isValid;
}

QString OAIResourceSet::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIResourceSet::asJsonObject() const {
    QJsonObject obj;
    if (m_resource_setting_id_isSet) {
        obj.insert(QString("resourceSettingId"), ::OpenAPI::toJsonValue(m_resource_setting_id));
    }
    if (m_vm_resource_id_isSet) {
        obj.insert(QString("vmResourceId"), ::OpenAPI::toJsonValue(m_vm_resource_id));
    }
    return obj;
}

QString OAIResourceSet::getResourceSettingId() const {
    return m_resource_setting_id;
}
void OAIResourceSet::setResourceSettingId(const QString &resource_setting_id) {
    m_resource_setting_id = resource_setting_id;
    m_resource_setting_id_isSet = true;
}

bool OAIResourceSet::is_resource_setting_id_Set() const{
    return m_resource_setting_id_isSet;
}

bool OAIResourceSet::is_resource_setting_id_Valid() const{
    return m_resource_setting_id_isValid;
}

QString OAIResourceSet::getVmResourceId() const {
    return m_vm_resource_id;
}
void OAIResourceSet::setVmResourceId(const QString &vm_resource_id) {
    m_vm_resource_id = vm_resource_id;
    m_vm_resource_id_isSet = true;
}

bool OAIResourceSet::is_vm_resource_id_Set() const{
    return m_vm_resource_id_isSet;
}

bool OAIResourceSet::is_vm_resource_id_Valid() const{
    return m_vm_resource_id_isValid;
}

bool OAIResourceSet::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_resource_setting_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_vm_resource_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIResourceSet::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
