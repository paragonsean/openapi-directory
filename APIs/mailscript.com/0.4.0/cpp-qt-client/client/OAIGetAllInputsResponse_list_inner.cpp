/**
 * Mailscript
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.4.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIGetAllInputsResponse_list_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetAllInputsResponse_list_inner::OAIGetAllInputsResponse_list_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetAllInputsResponse_list_inner::OAIGetAllInputsResponse_list_inner() {
    this->initializeModel();
}

OAIGetAllInputsResponse_list_inner::~OAIGetAllInputsResponse_list_inner() {}

void OAIGetAllInputsResponse_list_inner::initializeModel() {

    m_address_isSet = false;
    m_address_isValid = false;

    m_created_at_isSet = false;
    m_created_at_isValid = false;

    m_created_by_isSet = false;
    m_created_by_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_owner_isSet = false;
    m_owner_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIGetAllInputsResponse_list_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetAllInputsResponse_list_inner::fromJsonObject(QJsonObject json) {

    m_address_isValid = ::OpenAPI::fromJsonValue(m_address, json[QString("address")]);
    m_address_isSet = !json[QString("address")].isNull() && m_address_isValid;

    m_created_at_isValid = ::OpenAPI::fromJsonValue(m_created_at, json[QString("createdAt")]);
    m_created_at_isSet = !json[QString("createdAt")].isNull() && m_created_at_isValid;

    m_created_by_isValid = ::OpenAPI::fromJsonValue(m_created_by, json[QString("createdBy")]);
    m_created_by_isSet = !json[QString("createdBy")].isNull() && m_created_by_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_owner_isValid = ::OpenAPI::fromJsonValue(m_owner, json[QString("owner")]);
    m_owner_isSet = !json[QString("owner")].isNull() && m_owner_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAIGetAllInputsResponse_list_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetAllInputsResponse_list_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_address_isSet) {
        obj.insert(QString("address"), ::OpenAPI::toJsonValue(m_address));
    }
    if (m_created_at_isSet) {
        obj.insert(QString("createdAt"), ::OpenAPI::toJsonValue(m_created_at));
    }
    if (m_created_by_isSet) {
        obj.insert(QString("createdBy"), ::OpenAPI::toJsonValue(m_created_by));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_owner_isSet) {
        obj.insert(QString("owner"), ::OpenAPI::toJsonValue(m_owner));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

QString OAIGetAllInputsResponse_list_inner::getAddress() const {
    return m_address;
}
void OAIGetAllInputsResponse_list_inner::setAddress(const QString &address) {
    m_address = address;
    m_address_isSet = true;
}

bool OAIGetAllInputsResponse_list_inner::is_address_Set() const{
    return m_address_isSet;
}

bool OAIGetAllInputsResponse_list_inner::is_address_Valid() const{
    return m_address_isValid;
}

QDateTime OAIGetAllInputsResponse_list_inner::getCreatedAt() const {
    return m_created_at;
}
void OAIGetAllInputsResponse_list_inner::setCreatedAt(const QDateTime &created_at) {
    m_created_at = created_at;
    m_created_at_isSet = true;
}

bool OAIGetAllInputsResponse_list_inner::is_created_at_Set() const{
    return m_created_at_isSet;
}

bool OAIGetAllInputsResponse_list_inner::is_created_at_Valid() const{
    return m_created_at_isValid;
}

QString OAIGetAllInputsResponse_list_inner::getCreatedBy() const {
    return m_created_by;
}
void OAIGetAllInputsResponse_list_inner::setCreatedBy(const QString &created_by) {
    m_created_by = created_by;
    m_created_by_isSet = true;
}

bool OAIGetAllInputsResponse_list_inner::is_created_by_Set() const{
    return m_created_by_isSet;
}

bool OAIGetAllInputsResponse_list_inner::is_created_by_Valid() const{
    return m_created_by_isValid;
}

QString OAIGetAllInputsResponse_list_inner::getId() const {
    return m_id;
}
void OAIGetAllInputsResponse_list_inner::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIGetAllInputsResponse_list_inner::is_id_Set() const{
    return m_id_isSet;
}

bool OAIGetAllInputsResponse_list_inner::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIGetAllInputsResponse_list_inner::getName() const {
    return m_name;
}
void OAIGetAllInputsResponse_list_inner::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIGetAllInputsResponse_list_inner::is_name_Set() const{
    return m_name_isSet;
}

bool OAIGetAllInputsResponse_list_inner::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIGetAllInputsResponse_list_inner::getOwner() const {
    return m_owner;
}
void OAIGetAllInputsResponse_list_inner::setOwner(const QString &owner) {
    m_owner = owner;
    m_owner_isSet = true;
}

bool OAIGetAllInputsResponse_list_inner::is_owner_Set() const{
    return m_owner_isSet;
}

bool OAIGetAllInputsResponse_list_inner::is_owner_Valid() const{
    return m_owner_isValid;
}

QString OAIGetAllInputsResponse_list_inner::getType() const {
    return m_type;
}
void OAIGetAllInputsResponse_list_inner::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIGetAllInputsResponse_list_inner::is_type_Set() const{
    return m_type_isSet;
}

bool OAIGetAllInputsResponse_list_inner::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIGetAllInputsResponse_list_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_address_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_by_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_owner_isSet) {
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

bool OAIGetAllInputsResponse_list_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_address_isValid && m_created_at_isValid && m_created_by_isValid && m_id_isValid && m_name_isValid && m_owner_isValid && m_type_isValid && true;
}

} // namespace OpenAPI
