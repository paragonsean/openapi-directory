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

#include "OAIGetNetworkAppliancePrefixesDelegatedStatics_200_response_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetNetworkAppliancePrefixesDelegatedStatics_200_response_inner::OAIGetNetworkAppliancePrefixesDelegatedStatics_200_response_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetNetworkAppliancePrefixesDelegatedStatics_200_response_inner::OAIGetNetworkAppliancePrefixesDelegatedStatics_200_response_inner() {
    this->initializeModel();
}

OAIGetNetworkAppliancePrefixesDelegatedStatics_200_response_inner::~OAIGetNetworkAppliancePrefixesDelegatedStatics_200_response_inner() {}

void OAIGetNetworkAppliancePrefixesDelegatedStatics_200_response_inner::initializeModel() {

    m_created_at_isSet = false;
    m_created_at_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_origin_isSet = false;
    m_origin_isValid = false;

    m_prefix_isSet = false;
    m_prefix_isValid = false;

    m_static_delegated_prefix_id_isSet = false;
    m_static_delegated_prefix_id_isValid = false;

    m_updated_at_isSet = false;
    m_updated_at_isValid = false;
}

void OAIGetNetworkAppliancePrefixesDelegatedStatics_200_response_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetNetworkAppliancePrefixesDelegatedStatics_200_response_inner::fromJsonObject(QJsonObject json) {

    m_created_at_isValid = ::OpenAPI::fromJsonValue(m_created_at, json[QString("createdAt")]);
    m_created_at_isSet = !json[QString("createdAt")].isNull() && m_created_at_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_origin_isValid = ::OpenAPI::fromJsonValue(m_origin, json[QString("origin")]);
    m_origin_isSet = !json[QString("origin")].isNull() && m_origin_isValid;

    m_prefix_isValid = ::OpenAPI::fromJsonValue(m_prefix, json[QString("prefix")]);
    m_prefix_isSet = !json[QString("prefix")].isNull() && m_prefix_isValid;

    m_static_delegated_prefix_id_isValid = ::OpenAPI::fromJsonValue(m_static_delegated_prefix_id, json[QString("staticDelegatedPrefixId")]);
    m_static_delegated_prefix_id_isSet = !json[QString("staticDelegatedPrefixId")].isNull() && m_static_delegated_prefix_id_isValid;

    m_updated_at_isValid = ::OpenAPI::fromJsonValue(m_updated_at, json[QString("updatedAt")]);
    m_updated_at_isSet = !json[QString("updatedAt")].isNull() && m_updated_at_isValid;
}

QString OAIGetNetworkAppliancePrefixesDelegatedStatics_200_response_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetNetworkAppliancePrefixesDelegatedStatics_200_response_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_created_at_isSet) {
        obj.insert(QString("createdAt"), ::OpenAPI::toJsonValue(m_created_at));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_origin.isSet()) {
        obj.insert(QString("origin"), ::OpenAPI::toJsonValue(m_origin));
    }
    if (m_prefix_isSet) {
        obj.insert(QString("prefix"), ::OpenAPI::toJsonValue(m_prefix));
    }
    if (m_static_delegated_prefix_id_isSet) {
        obj.insert(QString("staticDelegatedPrefixId"), ::OpenAPI::toJsonValue(m_static_delegated_prefix_id));
    }
    if (m_updated_at_isSet) {
        obj.insert(QString("updatedAt"), ::OpenAPI::toJsonValue(m_updated_at));
    }
    return obj;
}

QDateTime OAIGetNetworkAppliancePrefixesDelegatedStatics_200_response_inner::getCreatedAt() const {
    return m_created_at;
}
void OAIGetNetworkAppliancePrefixesDelegatedStatics_200_response_inner::setCreatedAt(const QDateTime &created_at) {
    m_created_at = created_at;
    m_created_at_isSet = true;
}

bool OAIGetNetworkAppliancePrefixesDelegatedStatics_200_response_inner::is_created_at_Set() const{
    return m_created_at_isSet;
}

bool OAIGetNetworkAppliancePrefixesDelegatedStatics_200_response_inner::is_created_at_Valid() const{
    return m_created_at_isValid;
}

QString OAIGetNetworkAppliancePrefixesDelegatedStatics_200_response_inner::getDescription() const {
    return m_description;
}
void OAIGetNetworkAppliancePrefixesDelegatedStatics_200_response_inner::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIGetNetworkAppliancePrefixesDelegatedStatics_200_response_inner::is_description_Set() const{
    return m_description_isSet;
}

bool OAIGetNetworkAppliancePrefixesDelegatedStatics_200_response_inner::is_description_Valid() const{
    return m_description_isValid;
}

OAIGetNetworkAppliancePrefixesDelegatedStatics_200_response_inner_origin OAIGetNetworkAppliancePrefixesDelegatedStatics_200_response_inner::getOrigin() const {
    return m_origin;
}
void OAIGetNetworkAppliancePrefixesDelegatedStatics_200_response_inner::setOrigin(const OAIGetNetworkAppliancePrefixesDelegatedStatics_200_response_inner_origin &origin) {
    m_origin = origin;
    m_origin_isSet = true;
}

bool OAIGetNetworkAppliancePrefixesDelegatedStatics_200_response_inner::is_origin_Set() const{
    return m_origin_isSet;
}

bool OAIGetNetworkAppliancePrefixesDelegatedStatics_200_response_inner::is_origin_Valid() const{
    return m_origin_isValid;
}

QString OAIGetNetworkAppliancePrefixesDelegatedStatics_200_response_inner::getPrefix() const {
    return m_prefix;
}
void OAIGetNetworkAppliancePrefixesDelegatedStatics_200_response_inner::setPrefix(const QString &prefix) {
    m_prefix = prefix;
    m_prefix_isSet = true;
}

bool OAIGetNetworkAppliancePrefixesDelegatedStatics_200_response_inner::is_prefix_Set() const{
    return m_prefix_isSet;
}

bool OAIGetNetworkAppliancePrefixesDelegatedStatics_200_response_inner::is_prefix_Valid() const{
    return m_prefix_isValid;
}

QString OAIGetNetworkAppliancePrefixesDelegatedStatics_200_response_inner::getStaticDelegatedPrefixId() const {
    return m_static_delegated_prefix_id;
}
void OAIGetNetworkAppliancePrefixesDelegatedStatics_200_response_inner::setStaticDelegatedPrefixId(const QString &static_delegated_prefix_id) {
    m_static_delegated_prefix_id = static_delegated_prefix_id;
    m_static_delegated_prefix_id_isSet = true;
}

bool OAIGetNetworkAppliancePrefixesDelegatedStatics_200_response_inner::is_static_delegated_prefix_id_Set() const{
    return m_static_delegated_prefix_id_isSet;
}

bool OAIGetNetworkAppliancePrefixesDelegatedStatics_200_response_inner::is_static_delegated_prefix_id_Valid() const{
    return m_static_delegated_prefix_id_isValid;
}

QDateTime OAIGetNetworkAppliancePrefixesDelegatedStatics_200_response_inner::getUpdatedAt() const {
    return m_updated_at;
}
void OAIGetNetworkAppliancePrefixesDelegatedStatics_200_response_inner::setUpdatedAt(const QDateTime &updated_at) {
    m_updated_at = updated_at;
    m_updated_at_isSet = true;
}

bool OAIGetNetworkAppliancePrefixesDelegatedStatics_200_response_inner::is_updated_at_Set() const{
    return m_updated_at_isSet;
}

bool OAIGetNetworkAppliancePrefixesDelegatedStatics_200_response_inner::is_updated_at_Valid() const{
    return m_updated_at_isValid;
}

bool OAIGetNetworkAppliancePrefixesDelegatedStatics_200_response_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_created_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_origin.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_prefix_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_static_delegated_prefix_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_updated_at_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGetNetworkAppliancePrefixesDelegatedStatics_200_response_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
