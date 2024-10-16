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

#include "OAICreateOrganizationAdaptivePolicyPolicy_request_destinationGroup.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICreateOrganizationAdaptivePolicyPolicy_request_destinationGroup::OAICreateOrganizationAdaptivePolicyPolicy_request_destinationGroup(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICreateOrganizationAdaptivePolicyPolicy_request_destinationGroup::OAICreateOrganizationAdaptivePolicyPolicy_request_destinationGroup() {
    this->initializeModel();
}

OAICreateOrganizationAdaptivePolicyPolicy_request_destinationGroup::~OAICreateOrganizationAdaptivePolicyPolicy_request_destinationGroup() {}

void OAICreateOrganizationAdaptivePolicyPolicy_request_destinationGroup::initializeModel() {

    m_id_isSet = false;
    m_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_sgt_isSet = false;
    m_sgt_isValid = false;
}

void OAICreateOrganizationAdaptivePolicyPolicy_request_destinationGroup::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICreateOrganizationAdaptivePolicyPolicy_request_destinationGroup::fromJsonObject(QJsonObject json) {

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_sgt_isValid = ::OpenAPI::fromJsonValue(m_sgt, json[QString("sgt")]);
    m_sgt_isSet = !json[QString("sgt")].isNull() && m_sgt_isValid;
}

QString OAICreateOrganizationAdaptivePolicyPolicy_request_destinationGroup::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICreateOrganizationAdaptivePolicyPolicy_request_destinationGroup::asJsonObject() const {
    QJsonObject obj;
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_sgt_isSet) {
        obj.insert(QString("sgt"), ::OpenAPI::toJsonValue(m_sgt));
    }
    return obj;
}

QString OAICreateOrganizationAdaptivePolicyPolicy_request_destinationGroup::getId() const {
    return m_id;
}
void OAICreateOrganizationAdaptivePolicyPolicy_request_destinationGroup::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAICreateOrganizationAdaptivePolicyPolicy_request_destinationGroup::is_id_Set() const{
    return m_id_isSet;
}

bool OAICreateOrganizationAdaptivePolicyPolicy_request_destinationGroup::is_id_Valid() const{
    return m_id_isValid;
}

QString OAICreateOrganizationAdaptivePolicyPolicy_request_destinationGroup::getName() const {
    return m_name;
}
void OAICreateOrganizationAdaptivePolicyPolicy_request_destinationGroup::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAICreateOrganizationAdaptivePolicyPolicy_request_destinationGroup::is_name_Set() const{
    return m_name_isSet;
}

bool OAICreateOrganizationAdaptivePolicyPolicy_request_destinationGroup::is_name_Valid() const{
    return m_name_isValid;
}

qint32 OAICreateOrganizationAdaptivePolicyPolicy_request_destinationGroup::getSgt() const {
    return m_sgt;
}
void OAICreateOrganizationAdaptivePolicyPolicy_request_destinationGroup::setSgt(const qint32 &sgt) {
    m_sgt = sgt;
    m_sgt_isSet = true;
}

bool OAICreateOrganizationAdaptivePolicyPolicy_request_destinationGroup::is_sgt_Set() const{
    return m_sgt_isSet;
}

bool OAICreateOrganizationAdaptivePolicyPolicy_request_destinationGroup::is_sgt_Valid() const{
    return m_sgt_isValid;
}

bool OAICreateOrganizationAdaptivePolicyPolicy_request_destinationGroup::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sgt_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICreateOrganizationAdaptivePolicyPolicy_request_destinationGroup::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
