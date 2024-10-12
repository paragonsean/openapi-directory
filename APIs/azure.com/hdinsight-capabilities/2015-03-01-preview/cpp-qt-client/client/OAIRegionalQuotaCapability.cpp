/**
 * HDInsightManagementClient
 * The HDInsight Management Client.
 *
 * The version of the OpenAPI document: 2015-03-01-preview
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIRegionalQuotaCapability.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIRegionalQuotaCapability::OAIRegionalQuotaCapability(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIRegionalQuotaCapability::OAIRegionalQuotaCapability() {
    this->initializeModel();
}

OAIRegionalQuotaCapability::~OAIRegionalQuotaCapability() {}

void OAIRegionalQuotaCapability::initializeModel() {

    m_cores_available_isSet = false;
    m_cores_available_isValid = false;

    m_cores_used_isSet = false;
    m_cores_used_isValid = false;

    m_region_name_isSet = false;
    m_region_name_isValid = false;
}

void OAIRegionalQuotaCapability::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIRegionalQuotaCapability::fromJsonObject(QJsonObject json) {

    m_cores_available_isValid = ::OpenAPI::fromJsonValue(m_cores_available, json[QString("cores_available")]);
    m_cores_available_isSet = !json[QString("cores_available")].isNull() && m_cores_available_isValid;

    m_cores_used_isValid = ::OpenAPI::fromJsonValue(m_cores_used, json[QString("cores_used")]);
    m_cores_used_isSet = !json[QString("cores_used")].isNull() && m_cores_used_isValid;

    m_region_name_isValid = ::OpenAPI::fromJsonValue(m_region_name, json[QString("region_name")]);
    m_region_name_isSet = !json[QString("region_name")].isNull() && m_region_name_isValid;
}

QString OAIRegionalQuotaCapability::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIRegionalQuotaCapability::asJsonObject() const {
    QJsonObject obj;
    if (m_cores_available_isSet) {
        obj.insert(QString("cores_available"), ::OpenAPI::toJsonValue(m_cores_available));
    }
    if (m_cores_used_isSet) {
        obj.insert(QString("cores_used"), ::OpenAPI::toJsonValue(m_cores_used));
    }
    if (m_region_name_isSet) {
        obj.insert(QString("region_name"), ::OpenAPI::toJsonValue(m_region_name));
    }
    return obj;
}

qint64 OAIRegionalQuotaCapability::getCoresAvailable() const {
    return m_cores_available;
}
void OAIRegionalQuotaCapability::setCoresAvailable(const qint64 &cores_available) {
    m_cores_available = cores_available;
    m_cores_available_isSet = true;
}

bool OAIRegionalQuotaCapability::is_cores_available_Set() const{
    return m_cores_available_isSet;
}

bool OAIRegionalQuotaCapability::is_cores_available_Valid() const{
    return m_cores_available_isValid;
}

qint64 OAIRegionalQuotaCapability::getCoresUsed() const {
    return m_cores_used;
}
void OAIRegionalQuotaCapability::setCoresUsed(const qint64 &cores_used) {
    m_cores_used = cores_used;
    m_cores_used_isSet = true;
}

bool OAIRegionalQuotaCapability::is_cores_used_Set() const{
    return m_cores_used_isSet;
}

bool OAIRegionalQuotaCapability::is_cores_used_Valid() const{
    return m_cores_used_isValid;
}

QString OAIRegionalQuotaCapability::getRegionName() const {
    return m_region_name;
}
void OAIRegionalQuotaCapability::setRegionName(const QString &region_name) {
    m_region_name = region_name;
    m_region_name_isSet = true;
}

bool OAIRegionalQuotaCapability::is_region_name_Set() const{
    return m_region_name_isSet;
}

bool OAIRegionalQuotaCapability::is_region_name_Valid() const{
    return m_region_name_isValid;
}

bool OAIRegionalQuotaCapability::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_cores_available_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_cores_used_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_region_name_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIRegionalQuotaCapability::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
