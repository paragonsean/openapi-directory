/**
 * Noosh API application
 * Full description of Noosh API
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIUserDetailsVO.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUserDetailsVO::OAIUserDetailsVO(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUserDetailsVO::OAIUserDetailsVO() {
    this->initializeModel();
}

OAIUserDetailsVO::~OAIUserDetailsVO() {}

void OAIUserDetailsVO::initializeModel() {

    m_address_isSet = false;
    m_address_isValid = false;

    m_company_name_isSet = false;
    m_company_name_isValid = false;

    m_email_isSet = false;
    m_email_isValid = false;

    m_fax_number_isSet = false;
    m_fax_number_isValid = false;

    m_first_name_isSet = false;
    m_first_name_isValid = false;

    m_last_name_isSet = false;
    m_last_name_isValid = false;

    m_locale_isSet = false;
    m_locale_isValid = false;

    m_middle_name_isSet = false;
    m_middle_name_isValid = false;

    m_organization_isSet = false;
    m_organization_isValid = false;

    m_phone_number_isSet = false;
    m_phone_number_isValid = false;

    m_time_zone_isSet = false;
    m_time_zone_isValid = false;

    m_title_isSet = false;
    m_title_isValid = false;

    m_user_id_isSet = false;
    m_user_id_isValid = false;
}

void OAIUserDetailsVO::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUserDetailsVO::fromJsonObject(QJsonObject json) {

    m_address_isValid = ::OpenAPI::fromJsonValue(m_address, json[QString("address")]);
    m_address_isSet = !json[QString("address")].isNull() && m_address_isValid;

    m_company_name_isValid = ::OpenAPI::fromJsonValue(m_company_name, json[QString("company_name")]);
    m_company_name_isSet = !json[QString("company_name")].isNull() && m_company_name_isValid;

    m_email_isValid = ::OpenAPI::fromJsonValue(m_email, json[QString("email")]);
    m_email_isSet = !json[QString("email")].isNull() && m_email_isValid;

    m_fax_number_isValid = ::OpenAPI::fromJsonValue(m_fax_number, json[QString("fax_number")]);
    m_fax_number_isSet = !json[QString("fax_number")].isNull() && m_fax_number_isValid;

    m_first_name_isValid = ::OpenAPI::fromJsonValue(m_first_name, json[QString("first_name")]);
    m_first_name_isSet = !json[QString("first_name")].isNull() && m_first_name_isValid;

    m_last_name_isValid = ::OpenAPI::fromJsonValue(m_last_name, json[QString("last_name")]);
    m_last_name_isSet = !json[QString("last_name")].isNull() && m_last_name_isValid;

    m_locale_isValid = ::OpenAPI::fromJsonValue(m_locale, json[QString("locale")]);
    m_locale_isSet = !json[QString("locale")].isNull() && m_locale_isValid;

    m_middle_name_isValid = ::OpenAPI::fromJsonValue(m_middle_name, json[QString("middle_name")]);
    m_middle_name_isSet = !json[QString("middle_name")].isNull() && m_middle_name_isValid;

    m_organization_isValid = ::OpenAPI::fromJsonValue(m_organization, json[QString("organization")]);
    m_organization_isSet = !json[QString("organization")].isNull() && m_organization_isValid;

    m_phone_number_isValid = ::OpenAPI::fromJsonValue(m_phone_number, json[QString("phone_number")]);
    m_phone_number_isSet = !json[QString("phone_number")].isNull() && m_phone_number_isValid;

    m_time_zone_isValid = ::OpenAPI::fromJsonValue(m_time_zone, json[QString("time_zone")]);
    m_time_zone_isSet = !json[QString("time_zone")].isNull() && m_time_zone_isValid;

    m_title_isValid = ::OpenAPI::fromJsonValue(m_title, json[QString("title")]);
    m_title_isSet = !json[QString("title")].isNull() && m_title_isValid;

    m_user_id_isValid = ::OpenAPI::fromJsonValue(m_user_id, json[QString("user_id")]);
    m_user_id_isSet = !json[QString("user_id")].isNull() && m_user_id_isValid;
}

QString OAIUserDetailsVO::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUserDetailsVO::asJsonObject() const {
    QJsonObject obj;
    if (m_address_isSet) {
        obj.insert(QString("address"), ::OpenAPI::toJsonValue(m_address));
    }
    if (m_company_name_isSet) {
        obj.insert(QString("company_name"), ::OpenAPI::toJsonValue(m_company_name));
    }
    if (m_email_isSet) {
        obj.insert(QString("email"), ::OpenAPI::toJsonValue(m_email));
    }
    if (m_fax_number_isSet) {
        obj.insert(QString("fax_number"), ::OpenAPI::toJsonValue(m_fax_number));
    }
    if (m_first_name_isSet) {
        obj.insert(QString("first_name"), ::OpenAPI::toJsonValue(m_first_name));
    }
    if (m_last_name_isSet) {
        obj.insert(QString("last_name"), ::OpenAPI::toJsonValue(m_last_name));
    }
    if (m_locale_isSet) {
        obj.insert(QString("locale"), ::OpenAPI::toJsonValue(m_locale));
    }
    if (m_middle_name_isSet) {
        obj.insert(QString("middle_name"), ::OpenAPI::toJsonValue(m_middle_name));
    }
    if (m_organization_isSet) {
        obj.insert(QString("organization"), ::OpenAPI::toJsonValue(m_organization));
    }
    if (m_phone_number_isSet) {
        obj.insert(QString("phone_number"), ::OpenAPI::toJsonValue(m_phone_number));
    }
    if (m_time_zone_isSet) {
        obj.insert(QString("time_zone"), ::OpenAPI::toJsonValue(m_time_zone));
    }
    if (m_title_isSet) {
        obj.insert(QString("title"), ::OpenAPI::toJsonValue(m_title));
    }
    if (m_user_id_isSet) {
        obj.insert(QString("user_id"), ::OpenAPI::toJsonValue(m_user_id));
    }
    return obj;
}

QJsonValue OAIUserDetailsVO::getAddress() const {
    return m_address;
}
void OAIUserDetailsVO::setAddress(const QJsonValue &address) {
    m_address = address;
    m_address_isSet = true;
}

bool OAIUserDetailsVO::is_address_Set() const{
    return m_address_isSet;
}

bool OAIUserDetailsVO::is_address_Valid() const{
    return m_address_isValid;
}

QString OAIUserDetailsVO::getCompanyName() const {
    return m_company_name;
}
void OAIUserDetailsVO::setCompanyName(const QString &company_name) {
    m_company_name = company_name;
    m_company_name_isSet = true;
}

bool OAIUserDetailsVO::is_company_name_Set() const{
    return m_company_name_isSet;
}

bool OAIUserDetailsVO::is_company_name_Valid() const{
    return m_company_name_isValid;
}

QString OAIUserDetailsVO::getEmail() const {
    return m_email;
}
void OAIUserDetailsVO::setEmail(const QString &email) {
    m_email = email;
    m_email_isSet = true;
}

bool OAIUserDetailsVO::is_email_Set() const{
    return m_email_isSet;
}

bool OAIUserDetailsVO::is_email_Valid() const{
    return m_email_isValid;
}

QString OAIUserDetailsVO::getFaxNumber() const {
    return m_fax_number;
}
void OAIUserDetailsVO::setFaxNumber(const QString &fax_number) {
    m_fax_number = fax_number;
    m_fax_number_isSet = true;
}

bool OAIUserDetailsVO::is_fax_number_Set() const{
    return m_fax_number_isSet;
}

bool OAIUserDetailsVO::is_fax_number_Valid() const{
    return m_fax_number_isValid;
}

QString OAIUserDetailsVO::getFirstName() const {
    return m_first_name;
}
void OAIUserDetailsVO::setFirstName(const QString &first_name) {
    m_first_name = first_name;
    m_first_name_isSet = true;
}

bool OAIUserDetailsVO::is_first_name_Set() const{
    return m_first_name_isSet;
}

bool OAIUserDetailsVO::is_first_name_Valid() const{
    return m_first_name_isValid;
}

QString OAIUserDetailsVO::getLastName() const {
    return m_last_name;
}
void OAIUserDetailsVO::setLastName(const QString &last_name) {
    m_last_name = last_name;
    m_last_name_isSet = true;
}

bool OAIUserDetailsVO::is_last_name_Set() const{
    return m_last_name_isSet;
}

bool OAIUserDetailsVO::is_last_name_Valid() const{
    return m_last_name_isValid;
}

QString OAIUserDetailsVO::getLocale() const {
    return m_locale;
}
void OAIUserDetailsVO::setLocale(const QString &locale) {
    m_locale = locale;
    m_locale_isSet = true;
}

bool OAIUserDetailsVO::is_locale_Set() const{
    return m_locale_isSet;
}

bool OAIUserDetailsVO::is_locale_Valid() const{
    return m_locale_isValid;
}

QString OAIUserDetailsVO::getMiddleName() const {
    return m_middle_name;
}
void OAIUserDetailsVO::setMiddleName(const QString &middle_name) {
    m_middle_name = middle_name;
    m_middle_name_isSet = true;
}

bool OAIUserDetailsVO::is_middle_name_Set() const{
    return m_middle_name_isSet;
}

bool OAIUserDetailsVO::is_middle_name_Valid() const{
    return m_middle_name_isValid;
}

QString OAIUserDetailsVO::getOrganization() const {
    return m_organization;
}
void OAIUserDetailsVO::setOrganization(const QString &organization) {
    m_organization = organization;
    m_organization_isSet = true;
}

bool OAIUserDetailsVO::is_organization_Set() const{
    return m_organization_isSet;
}

bool OAIUserDetailsVO::is_organization_Valid() const{
    return m_organization_isValid;
}

QString OAIUserDetailsVO::getPhoneNumber() const {
    return m_phone_number;
}
void OAIUserDetailsVO::setPhoneNumber(const QString &phone_number) {
    m_phone_number = phone_number;
    m_phone_number_isSet = true;
}

bool OAIUserDetailsVO::is_phone_number_Set() const{
    return m_phone_number_isSet;
}

bool OAIUserDetailsVO::is_phone_number_Valid() const{
    return m_phone_number_isValid;
}

QString OAIUserDetailsVO::getTimeZone() const {
    return m_time_zone;
}
void OAIUserDetailsVO::setTimeZone(const QString &time_zone) {
    m_time_zone = time_zone;
    m_time_zone_isSet = true;
}

bool OAIUserDetailsVO::is_time_zone_Set() const{
    return m_time_zone_isSet;
}

bool OAIUserDetailsVO::is_time_zone_Valid() const{
    return m_time_zone_isValid;
}

QString OAIUserDetailsVO::getTitle() const {
    return m_title;
}
void OAIUserDetailsVO::setTitle(const QString &title) {
    m_title = title;
    m_title_isSet = true;
}

bool OAIUserDetailsVO::is_title_Set() const{
    return m_title_isSet;
}

bool OAIUserDetailsVO::is_title_Valid() const{
    return m_title_isValid;
}

qint64 OAIUserDetailsVO::getUserId() const {
    return m_user_id;
}
void OAIUserDetailsVO::setUserId(const qint64 &user_id) {
    m_user_id = user_id;
    m_user_id_isSet = true;
}

bool OAIUserDetailsVO::is_user_id_Set() const{
    return m_user_id_isSet;
}

bool OAIUserDetailsVO::is_user_id_Valid() const{
    return m_user_id_isValid;
}

bool OAIUserDetailsVO::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_address_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_company_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_email_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_fax_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_first_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_locale_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_middle_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_organization_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_phone_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_time_zone_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_title_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_user_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUserDetailsVO::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
