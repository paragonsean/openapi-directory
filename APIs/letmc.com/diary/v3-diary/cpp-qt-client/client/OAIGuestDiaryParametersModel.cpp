/**
 * agentOS API V3, Diary Call Group
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v3-diary
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIGuestDiaryParametersModel.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGuestDiaryParametersModel::OAIGuestDiaryParametersModel(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGuestDiaryParametersModel::OAIGuestDiaryParametersModel() {
    this->initializeModel();
}

OAIGuestDiaryParametersModel::~OAIGuestDiaryParametersModel() {}

void OAIGuestDiaryParametersModel::initializeModel() {

    m_contact_mobile_isSet = false;
    m_contact_mobile_isValid = false;

    m_email_address_isSet = false;
    m_email_address_isValid = false;

    m_forename_isSet = false;
    m_forename_isValid = false;

    m_oid_isSet = false;
    m_oid_isValid = false;

    m_surname_isSet = false;
    m_surname_isValid = false;
}

void OAIGuestDiaryParametersModel::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGuestDiaryParametersModel::fromJsonObject(QJsonObject json) {

    m_contact_mobile_isValid = ::OpenAPI::fromJsonValue(m_contact_mobile, json[QString("ContactMobile")]);
    m_contact_mobile_isSet = !json[QString("ContactMobile")].isNull() && m_contact_mobile_isValid;

    m_email_address_isValid = ::OpenAPI::fromJsonValue(m_email_address, json[QString("EmailAddress")]);
    m_email_address_isSet = !json[QString("EmailAddress")].isNull() && m_email_address_isValid;

    m_forename_isValid = ::OpenAPI::fromJsonValue(m_forename, json[QString("Forename")]);
    m_forename_isSet = !json[QString("Forename")].isNull() && m_forename_isValid;

    m_oid_isValid = ::OpenAPI::fromJsonValue(m_oid, json[QString("OID")]);
    m_oid_isSet = !json[QString("OID")].isNull() && m_oid_isValid;

    m_surname_isValid = ::OpenAPI::fromJsonValue(m_surname, json[QString("Surname")]);
    m_surname_isSet = !json[QString("Surname")].isNull() && m_surname_isValid;
}

QString OAIGuestDiaryParametersModel::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGuestDiaryParametersModel::asJsonObject() const {
    QJsonObject obj;
    if (m_contact_mobile_isSet) {
        obj.insert(QString("ContactMobile"), ::OpenAPI::toJsonValue(m_contact_mobile));
    }
    if (m_email_address_isSet) {
        obj.insert(QString("EmailAddress"), ::OpenAPI::toJsonValue(m_email_address));
    }
    if (m_forename_isSet) {
        obj.insert(QString("Forename"), ::OpenAPI::toJsonValue(m_forename));
    }
    if (m_oid_isSet) {
        obj.insert(QString("OID"), ::OpenAPI::toJsonValue(m_oid));
    }
    if (m_surname_isSet) {
        obj.insert(QString("Surname"), ::OpenAPI::toJsonValue(m_surname));
    }
    return obj;
}

QString OAIGuestDiaryParametersModel::getContactMobile() const {
    return m_contact_mobile;
}
void OAIGuestDiaryParametersModel::setContactMobile(const QString &contact_mobile) {
    m_contact_mobile = contact_mobile;
    m_contact_mobile_isSet = true;
}

bool OAIGuestDiaryParametersModel::is_contact_mobile_Set() const{
    return m_contact_mobile_isSet;
}

bool OAIGuestDiaryParametersModel::is_contact_mobile_Valid() const{
    return m_contact_mobile_isValid;
}

QString OAIGuestDiaryParametersModel::getEmailAddress() const {
    return m_email_address;
}
void OAIGuestDiaryParametersModel::setEmailAddress(const QString &email_address) {
    m_email_address = email_address;
    m_email_address_isSet = true;
}

bool OAIGuestDiaryParametersModel::is_email_address_Set() const{
    return m_email_address_isSet;
}

bool OAIGuestDiaryParametersModel::is_email_address_Valid() const{
    return m_email_address_isValid;
}

QString OAIGuestDiaryParametersModel::getForename() const {
    return m_forename;
}
void OAIGuestDiaryParametersModel::setForename(const QString &forename) {
    m_forename = forename;
    m_forename_isSet = true;
}

bool OAIGuestDiaryParametersModel::is_forename_Set() const{
    return m_forename_isSet;
}

bool OAIGuestDiaryParametersModel::is_forename_Valid() const{
    return m_forename_isValid;
}

QString OAIGuestDiaryParametersModel::getOid() const {
    return m_oid;
}
void OAIGuestDiaryParametersModel::setOid(const QString &oid) {
    m_oid = oid;
    m_oid_isSet = true;
}

bool OAIGuestDiaryParametersModel::is_oid_Set() const{
    return m_oid_isSet;
}

bool OAIGuestDiaryParametersModel::is_oid_Valid() const{
    return m_oid_isValid;
}

QString OAIGuestDiaryParametersModel::getSurname() const {
    return m_surname;
}
void OAIGuestDiaryParametersModel::setSurname(const QString &surname) {
    m_surname = surname;
    m_surname_isSet = true;
}

bool OAIGuestDiaryParametersModel::is_surname_Set() const{
    return m_surname_isSet;
}

bool OAIGuestDiaryParametersModel::is_surname_Valid() const{
    return m_surname_isValid;
}

bool OAIGuestDiaryParametersModel::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_contact_mobile_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_email_address_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_forename_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_oid_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_surname_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGuestDiaryParametersModel::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
