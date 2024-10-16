/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAICreateOrganizationPolicyObject_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICreateOrganizationPolicyObject_request::OAICreateOrganizationPolicyObject_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICreateOrganizationPolicyObject_request::OAICreateOrganizationPolicyObject_request() {
    this->initializeModel();
}

OAICreateOrganizationPolicyObject_request::~OAICreateOrganizationPolicyObject_request() {}

void OAICreateOrganizationPolicyObject_request::initializeModel() {

    m_category_isSet = false;
    m_category_isValid = false;

    m_cidr_isSet = false;
    m_cidr_isValid = false;

    m_fqdn_isSet = false;
    m_fqdn_isValid = false;

    m_group_ids_isSet = false;
    m_group_ids_isValid = false;

    m_ip_isSet = false;
    m_ip_isValid = false;

    m_mask_isSet = false;
    m_mask_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAICreateOrganizationPolicyObject_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICreateOrganizationPolicyObject_request::fromJsonObject(QJsonObject json) {

    m_category_isValid = ::OpenAPI::fromJsonValue(m_category, json[QString("category")]);
    m_category_isSet = !json[QString("category")].isNull() && m_category_isValid;

    m_cidr_isValid = ::OpenAPI::fromJsonValue(m_cidr, json[QString("cidr")]);
    m_cidr_isSet = !json[QString("cidr")].isNull() && m_cidr_isValid;

    m_fqdn_isValid = ::OpenAPI::fromJsonValue(m_fqdn, json[QString("fqdn")]);
    m_fqdn_isSet = !json[QString("fqdn")].isNull() && m_fqdn_isValid;

    m_group_ids_isValid = ::OpenAPI::fromJsonValue(m_group_ids, json[QString("groupIds")]);
    m_group_ids_isSet = !json[QString("groupIds")].isNull() && m_group_ids_isValid;

    m_ip_isValid = ::OpenAPI::fromJsonValue(m_ip, json[QString("ip")]);
    m_ip_isSet = !json[QString("ip")].isNull() && m_ip_isValid;

    m_mask_isValid = ::OpenAPI::fromJsonValue(m_mask, json[QString("mask")]);
    m_mask_isSet = !json[QString("mask")].isNull() && m_mask_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAICreateOrganizationPolicyObject_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICreateOrganizationPolicyObject_request::asJsonObject() const {
    QJsonObject obj;
    if (m_category_isSet) {
        obj.insert(QString("category"), ::OpenAPI::toJsonValue(m_category));
    }
    if (m_cidr_isSet) {
        obj.insert(QString("cidr"), ::OpenAPI::toJsonValue(m_cidr));
    }
    if (m_fqdn_isSet) {
        obj.insert(QString("fqdn"), ::OpenAPI::toJsonValue(m_fqdn));
    }
    if (m_group_ids.size() > 0) {
        obj.insert(QString("groupIds"), ::OpenAPI::toJsonValue(m_group_ids));
    }
    if (m_ip_isSet) {
        obj.insert(QString("ip"), ::OpenAPI::toJsonValue(m_ip));
    }
    if (m_mask_isSet) {
        obj.insert(QString("mask"), ::OpenAPI::toJsonValue(m_mask));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

QString OAICreateOrganizationPolicyObject_request::getCategory() const {
    return m_category;
}
void OAICreateOrganizationPolicyObject_request::setCategory(const QString &category) {
    m_category = category;
    m_category_isSet = true;
}

bool OAICreateOrganizationPolicyObject_request::is_category_Set() const{
    return m_category_isSet;
}

bool OAICreateOrganizationPolicyObject_request::is_category_Valid() const{
    return m_category_isValid;
}

QString OAICreateOrganizationPolicyObject_request::getCidr() const {
    return m_cidr;
}
void OAICreateOrganizationPolicyObject_request::setCidr(const QString &cidr) {
    m_cidr = cidr;
    m_cidr_isSet = true;
}

bool OAICreateOrganizationPolicyObject_request::is_cidr_Set() const{
    return m_cidr_isSet;
}

bool OAICreateOrganizationPolicyObject_request::is_cidr_Valid() const{
    return m_cidr_isValid;
}

QString OAICreateOrganizationPolicyObject_request::getFqdn() const {
    return m_fqdn;
}
void OAICreateOrganizationPolicyObject_request::setFqdn(const QString &fqdn) {
    m_fqdn = fqdn;
    m_fqdn_isSet = true;
}

bool OAICreateOrganizationPolicyObject_request::is_fqdn_Set() const{
    return m_fqdn_isSet;
}

bool OAICreateOrganizationPolicyObject_request::is_fqdn_Valid() const{
    return m_fqdn_isValid;
}

QList<qint32> OAICreateOrganizationPolicyObject_request::getGroupIds() const {
    return m_group_ids;
}
void OAICreateOrganizationPolicyObject_request::setGroupIds(const QList<qint32> &group_ids) {
    m_group_ids = group_ids;
    m_group_ids_isSet = true;
}

bool OAICreateOrganizationPolicyObject_request::is_group_ids_Set() const{
    return m_group_ids_isSet;
}

bool OAICreateOrganizationPolicyObject_request::is_group_ids_Valid() const{
    return m_group_ids_isValid;
}

QString OAICreateOrganizationPolicyObject_request::getIp() const {
    return m_ip;
}
void OAICreateOrganizationPolicyObject_request::setIp(const QString &ip) {
    m_ip = ip;
    m_ip_isSet = true;
}

bool OAICreateOrganizationPolicyObject_request::is_ip_Set() const{
    return m_ip_isSet;
}

bool OAICreateOrganizationPolicyObject_request::is_ip_Valid() const{
    return m_ip_isValid;
}

QString OAICreateOrganizationPolicyObject_request::getMask() const {
    return m_mask;
}
void OAICreateOrganizationPolicyObject_request::setMask(const QString &mask) {
    m_mask = mask;
    m_mask_isSet = true;
}

bool OAICreateOrganizationPolicyObject_request::is_mask_Set() const{
    return m_mask_isSet;
}

bool OAICreateOrganizationPolicyObject_request::is_mask_Valid() const{
    return m_mask_isValid;
}

QString OAICreateOrganizationPolicyObject_request::getName() const {
    return m_name;
}
void OAICreateOrganizationPolicyObject_request::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAICreateOrganizationPolicyObject_request::is_name_Set() const{
    return m_name_isSet;
}

bool OAICreateOrganizationPolicyObject_request::is_name_Valid() const{
    return m_name_isValid;
}

QString OAICreateOrganizationPolicyObject_request::getType() const {
    return m_type;
}
void OAICreateOrganizationPolicyObject_request::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAICreateOrganizationPolicyObject_request::is_type_Set() const{
    return m_type_isSet;
}

bool OAICreateOrganizationPolicyObject_request::is_type_Valid() const{
    return m_type_isValid;
}

bool OAICreateOrganizationPolicyObject_request::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_category_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_cidr_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_fqdn_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_group_ids.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_ip_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_mask_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICreateOrganizationPolicyObject_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_category_isValid && m_name_isValid && m_type_isValid && true;
}

} // namespace OpenAPI
