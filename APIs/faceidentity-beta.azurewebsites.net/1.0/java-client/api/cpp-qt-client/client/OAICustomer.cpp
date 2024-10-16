/**
 * Api Documentation
 * Api Documentation
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAICustomer.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICustomer::OAICustomer(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICustomer::OAICustomer() {
    this->initializeModel();
}

OAICustomer::~OAICustomer() {}

void OAICustomer::initializeModel() {

    m_city_isSet = false;
    m_city_isValid = false;

    m_company_description_isSet = false;
    m_company_description_isValid = false;

    m_company_name_isSet = false;
    m_company_name_isValid = false;

    m_country_isSet = false;
    m_country_isValid = false;

    m_face_recognition_type_isSet = false;
    m_face_recognition_type_isValid = false;

    m_first_name_isSet = false;
    m_first_name_isValid = false;

    m_last_name_isSet = false;
    m_last_name_isValid = false;

    m_password_isSet = false;
    m_password_isValid = false;

    m_phone_isSet = false;
    m_phone_isValid = false;

    m_state_isSet = false;
    m_state_isValid = false;

    m_street_address_isSet = false;
    m_street_address_isValid = false;

    m_username_isSet = false;
    m_username_isValid = false;

    m_zip_isSet = false;
    m_zip_isValid = false;
}

void OAICustomer::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICustomer::fromJsonObject(QJsonObject json) {

    m_city_isValid = ::OpenAPI::fromJsonValue(m_city, json[QString("city")]);
    m_city_isSet = !json[QString("city")].isNull() && m_city_isValid;

    m_company_description_isValid = ::OpenAPI::fromJsonValue(m_company_description, json[QString("companyDescription")]);
    m_company_description_isSet = !json[QString("companyDescription")].isNull() && m_company_description_isValid;

    m_company_name_isValid = ::OpenAPI::fromJsonValue(m_company_name, json[QString("companyName")]);
    m_company_name_isSet = !json[QString("companyName")].isNull() && m_company_name_isValid;

    m_country_isValid = ::OpenAPI::fromJsonValue(m_country, json[QString("country")]);
    m_country_isSet = !json[QString("country")].isNull() && m_country_isValid;

    m_face_recognition_type_isValid = ::OpenAPI::fromJsonValue(m_face_recognition_type, json[QString("faceRecognitionType")]);
    m_face_recognition_type_isSet = !json[QString("faceRecognitionType")].isNull() && m_face_recognition_type_isValid;

    m_first_name_isValid = ::OpenAPI::fromJsonValue(m_first_name, json[QString("firstName")]);
    m_first_name_isSet = !json[QString("firstName")].isNull() && m_first_name_isValid;

    m_last_name_isValid = ::OpenAPI::fromJsonValue(m_last_name, json[QString("lastName")]);
    m_last_name_isSet = !json[QString("lastName")].isNull() && m_last_name_isValid;

    m_password_isValid = ::OpenAPI::fromJsonValue(m_password, json[QString("password")]);
    m_password_isSet = !json[QString("password")].isNull() && m_password_isValid;

    m_phone_isValid = ::OpenAPI::fromJsonValue(m_phone, json[QString("phone")]);
    m_phone_isSet = !json[QString("phone")].isNull() && m_phone_isValid;

    m_state_isValid = ::OpenAPI::fromJsonValue(m_state, json[QString("state")]);
    m_state_isSet = !json[QString("state")].isNull() && m_state_isValid;

    m_street_address_isValid = ::OpenAPI::fromJsonValue(m_street_address, json[QString("streetAddress")]);
    m_street_address_isSet = !json[QString("streetAddress")].isNull() && m_street_address_isValid;

    m_username_isValid = ::OpenAPI::fromJsonValue(m_username, json[QString("username")]);
    m_username_isSet = !json[QString("username")].isNull() && m_username_isValid;

    m_zip_isValid = ::OpenAPI::fromJsonValue(m_zip, json[QString("zip")]);
    m_zip_isSet = !json[QString("zip")].isNull() && m_zip_isValid;
}

QString OAICustomer::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICustomer::asJsonObject() const {
    QJsonObject obj;
    if (m_city_isSet) {
        obj.insert(QString("city"), ::OpenAPI::toJsonValue(m_city));
    }
    if (m_company_description_isSet) {
        obj.insert(QString("companyDescription"), ::OpenAPI::toJsonValue(m_company_description));
    }
    if (m_company_name_isSet) {
        obj.insert(QString("companyName"), ::OpenAPI::toJsonValue(m_company_name));
    }
    if (m_country_isSet) {
        obj.insert(QString("country"), ::OpenAPI::toJsonValue(m_country));
    }
    if (m_face_recognition_type_isSet) {
        obj.insert(QString("faceRecognitionType"), ::OpenAPI::toJsonValue(m_face_recognition_type));
    }
    if (m_first_name_isSet) {
        obj.insert(QString("firstName"), ::OpenAPI::toJsonValue(m_first_name));
    }
    if (m_last_name_isSet) {
        obj.insert(QString("lastName"), ::OpenAPI::toJsonValue(m_last_name));
    }
    if (m_password_isSet) {
        obj.insert(QString("password"), ::OpenAPI::toJsonValue(m_password));
    }
    if (m_phone_isSet) {
        obj.insert(QString("phone"), ::OpenAPI::toJsonValue(m_phone));
    }
    if (m_state_isSet) {
        obj.insert(QString("state"), ::OpenAPI::toJsonValue(m_state));
    }
    if (m_street_address_isSet) {
        obj.insert(QString("streetAddress"), ::OpenAPI::toJsonValue(m_street_address));
    }
    if (m_username_isSet) {
        obj.insert(QString("username"), ::OpenAPI::toJsonValue(m_username));
    }
    if (m_zip_isSet) {
        obj.insert(QString("zip"), ::OpenAPI::toJsonValue(m_zip));
    }
    return obj;
}

QString OAICustomer::getCity() const {
    return m_city;
}
void OAICustomer::setCity(const QString &city) {
    m_city = city;
    m_city_isSet = true;
}

bool OAICustomer::is_city_Set() const{
    return m_city_isSet;
}

bool OAICustomer::is_city_Valid() const{
    return m_city_isValid;
}

QString OAICustomer::getCompanyDescription() const {
    return m_company_description;
}
void OAICustomer::setCompanyDescription(const QString &company_description) {
    m_company_description = company_description;
    m_company_description_isSet = true;
}

bool OAICustomer::is_company_description_Set() const{
    return m_company_description_isSet;
}

bool OAICustomer::is_company_description_Valid() const{
    return m_company_description_isValid;
}

QString OAICustomer::getCompanyName() const {
    return m_company_name;
}
void OAICustomer::setCompanyName(const QString &company_name) {
    m_company_name = company_name;
    m_company_name_isSet = true;
}

bool OAICustomer::is_company_name_Set() const{
    return m_company_name_isSet;
}

bool OAICustomer::is_company_name_Valid() const{
    return m_company_name_isValid;
}

QString OAICustomer::getCountry() const {
    return m_country;
}
void OAICustomer::setCountry(const QString &country) {
    m_country = country;
    m_country_isSet = true;
}

bool OAICustomer::is_country_Set() const{
    return m_country_isSet;
}

bool OAICustomer::is_country_Valid() const{
    return m_country_isValid;
}

QString OAICustomer::getFaceRecognitionType() const {
    return m_face_recognition_type;
}
void OAICustomer::setFaceRecognitionType(const QString &face_recognition_type) {
    m_face_recognition_type = face_recognition_type;
    m_face_recognition_type_isSet = true;
}

bool OAICustomer::is_face_recognition_type_Set() const{
    return m_face_recognition_type_isSet;
}

bool OAICustomer::is_face_recognition_type_Valid() const{
    return m_face_recognition_type_isValid;
}

QString OAICustomer::getFirstName() const {
    return m_first_name;
}
void OAICustomer::setFirstName(const QString &first_name) {
    m_first_name = first_name;
    m_first_name_isSet = true;
}

bool OAICustomer::is_first_name_Set() const{
    return m_first_name_isSet;
}

bool OAICustomer::is_first_name_Valid() const{
    return m_first_name_isValid;
}

QString OAICustomer::getLastName() const {
    return m_last_name;
}
void OAICustomer::setLastName(const QString &last_name) {
    m_last_name = last_name;
    m_last_name_isSet = true;
}

bool OAICustomer::is_last_name_Set() const{
    return m_last_name_isSet;
}

bool OAICustomer::is_last_name_Valid() const{
    return m_last_name_isValid;
}

QString OAICustomer::getPassword() const {
    return m_password;
}
void OAICustomer::setPassword(const QString &password) {
    m_password = password;
    m_password_isSet = true;
}

bool OAICustomer::is_password_Set() const{
    return m_password_isSet;
}

bool OAICustomer::is_password_Valid() const{
    return m_password_isValid;
}

QString OAICustomer::getPhone() const {
    return m_phone;
}
void OAICustomer::setPhone(const QString &phone) {
    m_phone = phone;
    m_phone_isSet = true;
}

bool OAICustomer::is_phone_Set() const{
    return m_phone_isSet;
}

bool OAICustomer::is_phone_Valid() const{
    return m_phone_isValid;
}

QString OAICustomer::getState() const {
    return m_state;
}
void OAICustomer::setState(const QString &state) {
    m_state = state;
    m_state_isSet = true;
}

bool OAICustomer::is_state_Set() const{
    return m_state_isSet;
}

bool OAICustomer::is_state_Valid() const{
    return m_state_isValid;
}

QString OAICustomer::getStreetAddress() const {
    return m_street_address;
}
void OAICustomer::setStreetAddress(const QString &street_address) {
    m_street_address = street_address;
    m_street_address_isSet = true;
}

bool OAICustomer::is_street_address_Set() const{
    return m_street_address_isSet;
}

bool OAICustomer::is_street_address_Valid() const{
    return m_street_address_isValid;
}

QString OAICustomer::getUsername() const {
    return m_username;
}
void OAICustomer::setUsername(const QString &username) {
    m_username = username;
    m_username_isSet = true;
}

bool OAICustomer::is_username_Set() const{
    return m_username_isSet;
}

bool OAICustomer::is_username_Valid() const{
    return m_username_isValid;
}

QString OAICustomer::getZip() const {
    return m_zip;
}
void OAICustomer::setZip(const QString &zip) {
    m_zip = zip;
    m_zip_isSet = true;
}

bool OAICustomer::is_zip_Set() const{
    return m_zip_isSet;
}

bool OAICustomer::is_zip_Valid() const{
    return m_zip_isValid;
}

bool OAICustomer::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_city_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_company_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_company_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_country_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_face_recognition_type_isSet) {
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

        if (m_password_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_phone_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_state_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_street_address_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_username_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_zip_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICustomer::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_company_name_isValid && m_face_recognition_type_isValid && m_password_isValid && m_username_isValid && true;
}

} // namespace OpenAPI
