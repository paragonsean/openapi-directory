/**
 * DataLakeStoreAccountManagementClient
 * Creates an Azure Data Lake Store account management client.
 *
 * The version of the OpenAPI document: 2016-11-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAICreateOrUpdateVirtualNetworkRuleProperties.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICreateOrUpdateVirtualNetworkRuleProperties::OAICreateOrUpdateVirtualNetworkRuleProperties(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICreateOrUpdateVirtualNetworkRuleProperties::OAICreateOrUpdateVirtualNetworkRuleProperties() {
    this->initializeModel();
}

OAICreateOrUpdateVirtualNetworkRuleProperties::~OAICreateOrUpdateVirtualNetworkRuleProperties() {}

void OAICreateOrUpdateVirtualNetworkRuleProperties::initializeModel() {

    m_subnet_id_isSet = false;
    m_subnet_id_isValid = false;
}

void OAICreateOrUpdateVirtualNetworkRuleProperties::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICreateOrUpdateVirtualNetworkRuleProperties::fromJsonObject(QJsonObject json) {

    m_subnet_id_isValid = ::OpenAPI::fromJsonValue(m_subnet_id, json[QString("subnetId")]);
    m_subnet_id_isSet = !json[QString("subnetId")].isNull() && m_subnet_id_isValid;
}

QString OAICreateOrUpdateVirtualNetworkRuleProperties::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICreateOrUpdateVirtualNetworkRuleProperties::asJsonObject() const {
    QJsonObject obj;
    if (m_subnet_id_isSet) {
        obj.insert(QString("subnetId"), ::OpenAPI::toJsonValue(m_subnet_id));
    }
    return obj;
}

QString OAICreateOrUpdateVirtualNetworkRuleProperties::getSubnetId() const {
    return m_subnet_id;
}
void OAICreateOrUpdateVirtualNetworkRuleProperties::setSubnetId(const QString &subnet_id) {
    m_subnet_id = subnet_id;
    m_subnet_id_isSet = true;
}

bool OAICreateOrUpdateVirtualNetworkRuleProperties::is_subnet_id_Set() const{
    return m_subnet_id_isSet;
}

bool OAICreateOrUpdateVirtualNetworkRuleProperties::is_subnet_id_Valid() const{
    return m_subnet_id_isValid;
}

bool OAICreateOrUpdateVirtualNetworkRuleProperties::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_subnet_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICreateOrUpdateVirtualNetworkRuleProperties::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_subnet_id_isValid && true;
}

} // namespace OpenAPI
