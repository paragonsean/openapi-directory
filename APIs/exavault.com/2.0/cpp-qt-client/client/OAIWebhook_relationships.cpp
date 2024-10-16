/**
 * ExaVault
 * ExaVaults API allows you to incorporate ExaVaults suite of file transfer and user management tools into your own application.\\nExaVault supports both POST (recommended when requesting large data sets) and GET operations, and requires an API key in order to use.
 *
 * The version of the OpenAPI document: 2.0
 * Contact: support@exavault.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIWebhook_relationships.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIWebhook_relationships::OAIWebhook_relationships(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIWebhook_relationships::OAIWebhook_relationships() {
    this->initializeModel();
}

OAIWebhook_relationships::~OAIWebhook_relationships() {}

void OAIWebhook_relationships::initializeModel() {

    m_owner_account_isSet = false;
    m_owner_account_isValid = false;

    m_resource_isSet = false;
    m_resource_isValid = false;
}

void OAIWebhook_relationships::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIWebhook_relationships::fromJsonObject(QJsonObject json) {

    m_owner_account_isValid = ::OpenAPI::fromJsonValue(m_owner_account, json[QString("ownerAccount")]);
    m_owner_account_isSet = !json[QString("ownerAccount")].isNull() && m_owner_account_isValid;

    m_resource_isValid = ::OpenAPI::fromJsonValue(m_resource, json[QString("resource")]);
    m_resource_isSet = !json[QString("resource")].isNull() && m_resource_isValid;
}

QString OAIWebhook_relationships::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIWebhook_relationships::asJsonObject() const {
    QJsonObject obj;
    if (m_owner_account.isSet()) {
        obj.insert(QString("ownerAccount"), ::OpenAPI::toJsonValue(m_owner_account));
    }
    if (m_resource.isSet()) {
        obj.insert(QString("resource"), ::OpenAPI::toJsonValue(m_resource));
    }
    return obj;
}

OAIWebhook_relationships_ownerAccount OAIWebhook_relationships::getOwnerAccount() const {
    return m_owner_account;
}
void OAIWebhook_relationships::setOwnerAccount(const OAIWebhook_relationships_ownerAccount &owner_account) {
    m_owner_account = owner_account;
    m_owner_account_isSet = true;
}

bool OAIWebhook_relationships::is_owner_account_Set() const{
    return m_owner_account_isSet;
}

bool OAIWebhook_relationships::is_owner_account_Valid() const{
    return m_owner_account_isValid;
}

OAIWebhook_relationships_resource OAIWebhook_relationships::getResource() const {
    return m_resource;
}
void OAIWebhook_relationships::setResource(const OAIWebhook_relationships_resource &resource) {
    m_resource = resource;
    m_resource_isSet = true;
}

bool OAIWebhook_relationships::is_resource_Set() const{
    return m_resource_isSet;
}

bool OAIWebhook_relationships::is_resource_Valid() const{
    return m_resource_isValid;
}

bool OAIWebhook_relationships::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_owner_account.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_resource.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIWebhook_relationships::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
