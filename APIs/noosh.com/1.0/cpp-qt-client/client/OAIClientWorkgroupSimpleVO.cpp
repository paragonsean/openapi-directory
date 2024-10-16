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

#include "OAIClientWorkgroupSimpleVO.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIClientWorkgroupSimpleVO::OAIClientWorkgroupSimpleVO(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIClientWorkgroupSimpleVO::OAIClientWorkgroupSimpleVO() {
    this->initializeModel();
}

OAIClientWorkgroupSimpleVO::~OAIClientWorkgroupSimpleVO() {}

void OAIClientWorkgroupSimpleVO::initializeModel() {

    m_client_ac_workgroup_id_isSet = false;
    m_client_ac_workgroup_id_isValid = false;

    m_client_workgroup_id_isSet = false;
    m_client_workgroup_id_isValid = false;

    m_client_workgroup_name_isSet = false;
    m_client_workgroup_name_isValid = false;
}

void OAIClientWorkgroupSimpleVO::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIClientWorkgroupSimpleVO::fromJsonObject(QJsonObject json) {

    m_client_ac_workgroup_id_isValid = ::OpenAPI::fromJsonValue(m_client_ac_workgroup_id, json[QString("client_ac_workgroup_id")]);
    m_client_ac_workgroup_id_isSet = !json[QString("client_ac_workgroup_id")].isNull() && m_client_ac_workgroup_id_isValid;

    m_client_workgroup_id_isValid = ::OpenAPI::fromJsonValue(m_client_workgroup_id, json[QString("client_workgroup_id")]);
    m_client_workgroup_id_isSet = !json[QString("client_workgroup_id")].isNull() && m_client_workgroup_id_isValid;

    m_client_workgroup_name_isValid = ::OpenAPI::fromJsonValue(m_client_workgroup_name, json[QString("client_workgroup_name")]);
    m_client_workgroup_name_isSet = !json[QString("client_workgroup_name")].isNull() && m_client_workgroup_name_isValid;
}

QString OAIClientWorkgroupSimpleVO::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIClientWorkgroupSimpleVO::asJsonObject() const {
    QJsonObject obj;
    if (m_client_ac_workgroup_id_isSet) {
        obj.insert(QString("client_ac_workgroup_id"), ::OpenAPI::toJsonValue(m_client_ac_workgroup_id));
    }
    if (m_client_workgroup_id_isSet) {
        obj.insert(QString("client_workgroup_id"), ::OpenAPI::toJsonValue(m_client_workgroup_id));
    }
    if (m_client_workgroup_name_isSet) {
        obj.insert(QString("client_workgroup_name"), ::OpenAPI::toJsonValue(m_client_workgroup_name));
    }
    return obj;
}

qint64 OAIClientWorkgroupSimpleVO::getClientAcWorkgroupId() const {
    return m_client_ac_workgroup_id;
}
void OAIClientWorkgroupSimpleVO::setClientAcWorkgroupId(const qint64 &client_ac_workgroup_id) {
    m_client_ac_workgroup_id = client_ac_workgroup_id;
    m_client_ac_workgroup_id_isSet = true;
}

bool OAIClientWorkgroupSimpleVO::is_client_ac_workgroup_id_Set() const{
    return m_client_ac_workgroup_id_isSet;
}

bool OAIClientWorkgroupSimpleVO::is_client_ac_workgroup_id_Valid() const{
    return m_client_ac_workgroup_id_isValid;
}

qint64 OAIClientWorkgroupSimpleVO::getClientWorkgroupId() const {
    return m_client_workgroup_id;
}
void OAIClientWorkgroupSimpleVO::setClientWorkgroupId(const qint64 &client_workgroup_id) {
    m_client_workgroup_id = client_workgroup_id;
    m_client_workgroup_id_isSet = true;
}

bool OAIClientWorkgroupSimpleVO::is_client_workgroup_id_Set() const{
    return m_client_workgroup_id_isSet;
}

bool OAIClientWorkgroupSimpleVO::is_client_workgroup_id_Valid() const{
    return m_client_workgroup_id_isValid;
}

QString OAIClientWorkgroupSimpleVO::getClientWorkgroupName() const {
    return m_client_workgroup_name;
}
void OAIClientWorkgroupSimpleVO::setClientWorkgroupName(const QString &client_workgroup_name) {
    m_client_workgroup_name = client_workgroup_name;
    m_client_workgroup_name_isSet = true;
}

bool OAIClientWorkgroupSimpleVO::is_client_workgroup_name_Set() const{
    return m_client_workgroup_name_isSet;
}

bool OAIClientWorkgroupSimpleVO::is_client_workgroup_name_Valid() const{
    return m_client_workgroup_name_isValid;
}

bool OAIClientWorkgroupSimpleVO::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_client_ac_workgroup_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_client_workgroup_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_client_workgroup_name_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIClientWorkgroupSimpleVO::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
