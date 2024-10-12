/**
 * Trip Parser
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.
 *
 * The version of the OpenAPI document: 3.0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAITravelAgency.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAITravelAgency::OAITravelAgency(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAITravelAgency::OAITravelAgency() {
    this->initializeModel();
}

OAITravelAgency::~OAITravelAgency() {}

void OAITravelAgency::initializeModel() {

    m_address_isSet = false;
    m_address_isValid = false;

    m_email_isSet = false;
    m_email_isValid = false;

    m_office_name_isSet = false;
    m_office_name_isValid = false;

    m_phone_isSet = false;
    m_phone_isValid = false;
}

void OAITravelAgency::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAITravelAgency::fromJsonObject(QJsonObject json) {

    m_address_isValid = ::OpenAPI::fromJsonValue(m_address, json[QString("address")]);
    m_address_isSet = !json[QString("address")].isNull() && m_address_isValid;

    m_email_isValid = ::OpenAPI::fromJsonValue(m_email, json[QString("email")]);
    m_email_isSet = !json[QString("email")].isNull() && m_email_isValid;

    m_office_name_isValid = ::OpenAPI::fromJsonValue(m_office_name, json[QString("officeName")]);
    m_office_name_isSet = !json[QString("officeName")].isNull() && m_office_name_isValid;

    m_phone_isValid = ::OpenAPI::fromJsonValue(m_phone, json[QString("phone")]);
    m_phone_isSet = !json[QString("phone")].isNull() && m_phone_isValid;
}

QString OAITravelAgency::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAITravelAgency::asJsonObject() const {
    QJsonObject obj;
    if (m_address.isSet()) {
        obj.insert(QString("address"), ::OpenAPI::toJsonValue(m_address));
    }
    if (m_email.isSet()) {
        obj.insert(QString("email"), ::OpenAPI::toJsonValue(m_email));
    }
    if (m_office_name_isSet) {
        obj.insert(QString("officeName"), ::OpenAPI::toJsonValue(m_office_name));
    }
    if (m_phone.isSet()) {
        obj.insert(QString("phone"), ::OpenAPI::toJsonValue(m_phone));
    }
    return obj;
}

OAIAddress OAITravelAgency::getAddress() const {
    return m_address;
}
void OAITravelAgency::setAddress(const OAIAddress &address) {
    m_address = address;
    m_address_isSet = true;
}

bool OAITravelAgency::is_address_Set() const{
    return m_address_isSet;
}

bool OAITravelAgency::is_address_Valid() const{
    return m_address_isValid;
}

OAIEmail OAITravelAgency::getEmail() const {
    return m_email;
}
void OAITravelAgency::setEmail(const OAIEmail &email) {
    m_email = email;
    m_email_isSet = true;
}

bool OAITravelAgency::is_email_Set() const{
    return m_email_isSet;
}

bool OAITravelAgency::is_email_Valid() const{
    return m_email_isValid;
}

QString OAITravelAgency::getOfficeName() const {
    return m_office_name;
}
void OAITravelAgency::setOfficeName(const QString &office_name) {
    m_office_name = office_name;
    m_office_name_isSet = true;
}

bool OAITravelAgency::is_office_name_Set() const{
    return m_office_name_isSet;
}

bool OAITravelAgency::is_office_name_Valid() const{
    return m_office_name_isValid;
}

OAIPhone OAITravelAgency::getPhone() const {
    return m_phone;
}
void OAITravelAgency::setPhone(const OAIPhone &phone) {
    m_phone = phone;
    m_phone_isSet = true;
}

bool OAITravelAgency::is_phone_Set() const{
    return m_phone_isSet;
}

bool OAITravelAgency::is_phone_Valid() const{
    return m_phone_isValid;
}

bool OAITravelAgency::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_address.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_email.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_office_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_phone.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAITravelAgency::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
