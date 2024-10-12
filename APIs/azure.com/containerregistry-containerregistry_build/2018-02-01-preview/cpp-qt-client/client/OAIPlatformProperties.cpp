/**
 * ContainerRegistryManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2018-02-01-preview
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIPlatformProperties.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPlatformProperties::OAIPlatformProperties(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPlatformProperties::OAIPlatformProperties() {
    this->initializeModel();
}

OAIPlatformProperties::~OAIPlatformProperties() {}

void OAIPlatformProperties::initializeModel() {

    m_cpu_isSet = false;
    m_cpu_isValid = false;

    m_os_type_isSet = false;
    m_os_type_isValid = false;
}

void OAIPlatformProperties::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPlatformProperties::fromJsonObject(QJsonObject json) {

    m_cpu_isValid = ::OpenAPI::fromJsonValue(m_cpu, json[QString("cpu")]);
    m_cpu_isSet = !json[QString("cpu")].isNull() && m_cpu_isValid;

    m_os_type_isValid = ::OpenAPI::fromJsonValue(m_os_type, json[QString("osType")]);
    m_os_type_isSet = !json[QString("osType")].isNull() && m_os_type_isValid;
}

QString OAIPlatformProperties::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPlatformProperties::asJsonObject() const {
    QJsonObject obj;
    if (m_cpu_isSet) {
        obj.insert(QString("cpu"), ::OpenAPI::toJsonValue(m_cpu));
    }
    if (m_os_type_isSet) {
        obj.insert(QString("osType"), ::OpenAPI::toJsonValue(m_os_type));
    }
    return obj;
}

qint32 OAIPlatformProperties::getCpu() const {
    return m_cpu;
}
void OAIPlatformProperties::setCpu(const qint32 &cpu) {
    m_cpu = cpu;
    m_cpu_isSet = true;
}

bool OAIPlatformProperties::is_cpu_Set() const{
    return m_cpu_isSet;
}

bool OAIPlatformProperties::is_cpu_Valid() const{
    return m_cpu_isValid;
}

QString OAIPlatformProperties::getOsType() const {
    return m_os_type;
}
void OAIPlatformProperties::setOsType(const QString &os_type) {
    m_os_type = os_type;
    m_os_type_isSet = true;
}

bool OAIPlatformProperties::is_os_type_Set() const{
    return m_os_type_isSet;
}

bool OAIPlatformProperties::is_os_type_Valid() const{
    return m_os_type_isValid;
}

bool OAIPlatformProperties::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_cpu_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_os_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPlatformProperties::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_os_type_isValid && true;
}

} // namespace OpenAPI
