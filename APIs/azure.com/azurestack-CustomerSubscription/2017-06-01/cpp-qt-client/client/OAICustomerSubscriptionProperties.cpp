/**
 * AzureStack Azure Bridge Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2017-06-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAICustomerSubscriptionProperties.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICustomerSubscriptionProperties::OAICustomerSubscriptionProperties(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICustomerSubscriptionProperties::OAICustomerSubscriptionProperties() {
    this->initializeModel();
}

OAICustomerSubscriptionProperties::~OAICustomerSubscriptionProperties() {}

void OAICustomerSubscriptionProperties::initializeModel() {

    m_tenant_id_isSet = false;
    m_tenant_id_isValid = false;
}

void OAICustomerSubscriptionProperties::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICustomerSubscriptionProperties::fromJsonObject(QJsonObject json) {

    m_tenant_id_isValid = ::OpenAPI::fromJsonValue(m_tenant_id, json[QString("tenantId")]);
    m_tenant_id_isSet = !json[QString("tenantId")].isNull() && m_tenant_id_isValid;
}

QString OAICustomerSubscriptionProperties::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICustomerSubscriptionProperties::asJsonObject() const {
    QJsonObject obj;
    if (m_tenant_id_isSet) {
        obj.insert(QString("tenantId"), ::OpenAPI::toJsonValue(m_tenant_id));
    }
    return obj;
}

QString OAICustomerSubscriptionProperties::getTenantId() const {
    return m_tenant_id;
}
void OAICustomerSubscriptionProperties::setTenantId(const QString &tenant_id) {
    m_tenant_id = tenant_id;
    m_tenant_id_isSet = true;
}

bool OAICustomerSubscriptionProperties::is_tenant_id_Set() const{
    return m_tenant_id_isSet;
}

bool OAICustomerSubscriptionProperties::is_tenant_id_Valid() const{
    return m_tenant_id_isValid;
}

bool OAICustomerSubscriptionProperties::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_tenant_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICustomerSubscriptionProperties::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
