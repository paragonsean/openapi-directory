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

#include "OAIGetAllVerificationsResponse_list_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetAllVerificationsResponse_list_inner::OAIGetAllVerificationsResponse_list_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetAllVerificationsResponse_list_inner::OAIGetAllVerificationsResponse_list_inner() {
    this->initializeModel();
}

OAIGetAllVerificationsResponse_list_inner::~OAIGetAllVerificationsResponse_list_inner() {}

void OAIGetAllVerificationsResponse_list_inner::initializeModel() {

    m_email_isSet = false;
    m_email_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;

    m_verified_isSet = false;
    m_verified_isValid = false;

    m_verified_at_isSet = false;
    m_verified_at_isValid = false;

    m_verified_by_isSet = false;
    m_verified_by_isValid = false;

    m_sms_isSet = false;
    m_sms_isValid = false;
}

void OAIGetAllVerificationsResponse_list_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetAllVerificationsResponse_list_inner::fromJsonObject(QJsonObject json) {

    m_email_isValid = ::OpenAPI::fromJsonValue(m_email, json[QString("email")]);
    m_email_isSet = !json[QString("email")].isNull() && m_email_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;

    m_verified_isValid = ::OpenAPI::fromJsonValue(m_verified, json[QString("verified")]);
    m_verified_isSet = !json[QString("verified")].isNull() && m_verified_isValid;

    m_verified_at_isValid = ::OpenAPI::fromJsonValue(m_verified_at, json[QString("verifiedAt")]);
    m_verified_at_isSet = !json[QString("verifiedAt")].isNull() && m_verified_at_isValid;

    m_verified_by_isValid = ::OpenAPI::fromJsonValue(m_verified_by, json[QString("verifiedBy")]);
    m_verified_by_isSet = !json[QString("verifiedBy")].isNull() && m_verified_by_isValid;

    m_sms_isValid = ::OpenAPI::fromJsonValue(m_sms, json[QString("sms")]);
    m_sms_isSet = !json[QString("sms")].isNull() && m_sms_isValid;
}

QString OAIGetAllVerificationsResponse_list_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetAllVerificationsResponse_list_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_email_isSet) {
        obj.insert(QString("email"), ::OpenAPI::toJsonValue(m_email));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    if (m_verified_isSet) {
        obj.insert(QString("verified"), ::OpenAPI::toJsonValue(m_verified));
    }
    if (m_verified_at_isSet) {
        obj.insert(QString("verifiedAt"), ::OpenAPI::toJsonValue(m_verified_at));
    }
    if (m_verified_by_isSet) {
        obj.insert(QString("verifiedBy"), ::OpenAPI::toJsonValue(m_verified_by));
    }
    if (m_sms_isSet) {
        obj.insert(QString("sms"), ::OpenAPI::toJsonValue(m_sms));
    }
    return obj;
}

QString OAIGetAllVerificationsResponse_list_inner::getEmail() const {
    return m_email;
}
void OAIGetAllVerificationsResponse_list_inner::setEmail(const QString &email) {
    m_email = email;
    m_email_isSet = true;
}

bool OAIGetAllVerificationsResponse_list_inner::is_email_Set() const{
    return m_email_isSet;
}

bool OAIGetAllVerificationsResponse_list_inner::is_email_Valid() const{
    return m_email_isValid;
}

QString OAIGetAllVerificationsResponse_list_inner::getId() const {
    return m_id;
}
void OAIGetAllVerificationsResponse_list_inner::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIGetAllVerificationsResponse_list_inner::is_id_Set() const{
    return m_id_isSet;
}

bool OAIGetAllVerificationsResponse_list_inner::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIGetAllVerificationsResponse_list_inner::getType() const {
    return m_type;
}
void OAIGetAllVerificationsResponse_list_inner::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIGetAllVerificationsResponse_list_inner::is_type_Set() const{
    return m_type_isSet;
}

bool OAIGetAllVerificationsResponse_list_inner::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIGetAllVerificationsResponse_list_inner::isVerified() const {
    return m_verified;
}
void OAIGetAllVerificationsResponse_list_inner::setVerified(const bool &verified) {
    m_verified = verified;
    m_verified_isSet = true;
}

bool OAIGetAllVerificationsResponse_list_inner::is_verified_Set() const{
    return m_verified_isSet;
}

bool OAIGetAllVerificationsResponse_list_inner::is_verified_Valid() const{
    return m_verified_isValid;
}

QDateTime OAIGetAllVerificationsResponse_list_inner::getVerifiedAt() const {
    return m_verified_at;
}
void OAIGetAllVerificationsResponse_list_inner::setVerifiedAt(const QDateTime &verified_at) {
    m_verified_at = verified_at;
    m_verified_at_isSet = true;
}

bool OAIGetAllVerificationsResponse_list_inner::is_verified_at_Set() const{
    return m_verified_at_isSet;
}

bool OAIGetAllVerificationsResponse_list_inner::is_verified_at_Valid() const{
    return m_verified_at_isValid;
}

QString OAIGetAllVerificationsResponse_list_inner::getVerifiedBy() const {
    return m_verified_by;
}
void OAIGetAllVerificationsResponse_list_inner::setVerifiedBy(const QString &verified_by) {
    m_verified_by = verified_by;
    m_verified_by_isSet = true;
}

bool OAIGetAllVerificationsResponse_list_inner::is_verified_by_Set() const{
    return m_verified_by_isSet;
}

bool OAIGetAllVerificationsResponse_list_inner::is_verified_by_Valid() const{
    return m_verified_by_isValid;
}

QString OAIGetAllVerificationsResponse_list_inner::getSms() const {
    return m_sms;
}
void OAIGetAllVerificationsResponse_list_inner::setSms(const QString &sms) {
    m_sms = sms;
    m_sms_isSet = true;
}

bool OAIGetAllVerificationsResponse_list_inner::is_sms_Set() const{
    return m_sms_isSet;
}

bool OAIGetAllVerificationsResponse_list_inner::is_sms_Valid() const{
    return m_sms_isValid;
}

bool OAIGetAllVerificationsResponse_list_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_email_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_verified_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_verified_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_verified_by_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sms_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGetAllVerificationsResponse_list_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
