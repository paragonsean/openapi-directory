/**
 * www.zoomconnect.com
 * The world's greatest SMS API
 *
 * The version of the OpenAPI document: 1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIWebServiceUser.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIWebServiceUser::OAIWebServiceUser(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIWebServiceUser::OAIWebServiceUser() {
    this->initializeModel();
}

OAIWebServiceUser::~OAIWebServiceUser() {}

void OAIWebServiceUser::initializeModel() {

    m_company_isSet = false;
    m_company_isValid = false;

    m_contact_number_isSet = false;
    m_contact_number_isValid = false;

    m_credit_balance_isSet = false;
    m_credit_balance_isValid = false;

    m_email_address_isSet = false;
    m_email_address_isValid = false;

    m_first_name_isSet = false;
    m_first_name_isValid = false;

    m_last_name_isSet = false;
    m_last_name_isValid = false;

    m_password_isSet = false;
    m_password_isValid = false;

    m_user_id_isSet = false;
    m_user_id_isValid = false;
}

void OAIWebServiceUser::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIWebServiceUser::fromJsonObject(QJsonObject json) {

    m_company_isValid = ::OpenAPI::fromJsonValue(m_company, json[QString("company")]);
    m_company_isSet = !json[QString("company")].isNull() && m_company_isValid;

    m_contact_number_isValid = ::OpenAPI::fromJsonValue(m_contact_number, json[QString("contactNumber")]);
    m_contact_number_isSet = !json[QString("contactNumber")].isNull() && m_contact_number_isValid;

    m_credit_balance_isValid = ::OpenAPI::fromJsonValue(m_credit_balance, json[QString("creditBalance")]);
    m_credit_balance_isSet = !json[QString("creditBalance")].isNull() && m_credit_balance_isValid;

    m_email_address_isValid = ::OpenAPI::fromJsonValue(m_email_address, json[QString("emailAddress")]);
    m_email_address_isSet = !json[QString("emailAddress")].isNull() && m_email_address_isValid;

    m_first_name_isValid = ::OpenAPI::fromJsonValue(m_first_name, json[QString("firstName")]);
    m_first_name_isSet = !json[QString("firstName")].isNull() && m_first_name_isValid;

    m_last_name_isValid = ::OpenAPI::fromJsonValue(m_last_name, json[QString("lastName")]);
    m_last_name_isSet = !json[QString("lastName")].isNull() && m_last_name_isValid;

    m_password_isValid = ::OpenAPI::fromJsonValue(m_password, json[QString("password")]);
    m_password_isSet = !json[QString("password")].isNull() && m_password_isValid;

    m_user_id_isValid = ::OpenAPI::fromJsonValue(m_user_id, json[QString("userId")]);
    m_user_id_isSet = !json[QString("userId")].isNull() && m_user_id_isValid;
}

QString OAIWebServiceUser::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIWebServiceUser::asJsonObject() const {
    QJsonObject obj;
    if (m_company_isSet) {
        obj.insert(QString("company"), ::OpenAPI::toJsonValue(m_company));
    }
    if (m_contact_number_isSet) {
        obj.insert(QString("contactNumber"), ::OpenAPI::toJsonValue(m_contact_number));
    }
    if (m_credit_balance_isSet) {
        obj.insert(QString("creditBalance"), ::OpenAPI::toJsonValue(m_credit_balance));
    }
    if (m_email_address_isSet) {
        obj.insert(QString("emailAddress"), ::OpenAPI::toJsonValue(m_email_address));
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
    if (m_user_id_isSet) {
        obj.insert(QString("userId"), ::OpenAPI::toJsonValue(m_user_id));
    }
    return obj;
}

QString OAIWebServiceUser::getCompany() const {
    return m_company;
}
void OAIWebServiceUser::setCompany(const QString &company) {
    m_company = company;
    m_company_isSet = true;
}

bool OAIWebServiceUser::is_company_Set() const{
    return m_company_isSet;
}

bool OAIWebServiceUser::is_company_Valid() const{
    return m_company_isValid;
}

QString OAIWebServiceUser::getContactNumber() const {
    return m_contact_number;
}
void OAIWebServiceUser::setContactNumber(const QString &contact_number) {
    m_contact_number = contact_number;
    m_contact_number_isSet = true;
}

bool OAIWebServiceUser::is_contact_number_Set() const{
    return m_contact_number_isSet;
}

bool OAIWebServiceUser::is_contact_number_Valid() const{
    return m_contact_number_isValid;
}

double OAIWebServiceUser::getCreditBalance() const {
    return m_credit_balance;
}
void OAIWebServiceUser::setCreditBalance(const double &credit_balance) {
    m_credit_balance = credit_balance;
    m_credit_balance_isSet = true;
}

bool OAIWebServiceUser::is_credit_balance_Set() const{
    return m_credit_balance_isSet;
}

bool OAIWebServiceUser::is_credit_balance_Valid() const{
    return m_credit_balance_isValid;
}

QString OAIWebServiceUser::getEmailAddress() const {
    return m_email_address;
}
void OAIWebServiceUser::setEmailAddress(const QString &email_address) {
    m_email_address = email_address;
    m_email_address_isSet = true;
}

bool OAIWebServiceUser::is_email_address_Set() const{
    return m_email_address_isSet;
}

bool OAIWebServiceUser::is_email_address_Valid() const{
    return m_email_address_isValid;
}

QString OAIWebServiceUser::getFirstName() const {
    return m_first_name;
}
void OAIWebServiceUser::setFirstName(const QString &first_name) {
    m_first_name = first_name;
    m_first_name_isSet = true;
}

bool OAIWebServiceUser::is_first_name_Set() const{
    return m_first_name_isSet;
}

bool OAIWebServiceUser::is_first_name_Valid() const{
    return m_first_name_isValid;
}

QString OAIWebServiceUser::getLastName() const {
    return m_last_name;
}
void OAIWebServiceUser::setLastName(const QString &last_name) {
    m_last_name = last_name;
    m_last_name_isSet = true;
}

bool OAIWebServiceUser::is_last_name_Set() const{
    return m_last_name_isSet;
}

bool OAIWebServiceUser::is_last_name_Valid() const{
    return m_last_name_isValid;
}

QString OAIWebServiceUser::getPassword() const {
    return m_password;
}
void OAIWebServiceUser::setPassword(const QString &password) {
    m_password = password;
    m_password_isSet = true;
}

bool OAIWebServiceUser::is_password_Set() const{
    return m_password_isSet;
}

bool OAIWebServiceUser::is_password_Valid() const{
    return m_password_isValid;
}

qint64 OAIWebServiceUser::getUserId() const {
    return m_user_id;
}
void OAIWebServiceUser::setUserId(const qint64 &user_id) {
    m_user_id = user_id;
    m_user_id_isSet = true;
}

bool OAIWebServiceUser::is_user_id_Set() const{
    return m_user_id_isSet;
}

bool OAIWebServiceUser::is_user_id_Valid() const{
    return m_user_id_isValid;
}

bool OAIWebServiceUser::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_company_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_contact_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_credit_balance_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_email_address_isSet) {
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

        if (m_user_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIWebServiceUser::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
