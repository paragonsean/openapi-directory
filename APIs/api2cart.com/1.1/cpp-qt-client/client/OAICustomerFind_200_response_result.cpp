/**
 * Swagger API2Cart
 * API2Cart
 *
 * The version of the OpenAPI document: 1.1
 * Contact: contact@api2cart.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAICustomerFind_200_response_result.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICustomerFind_200_response_result::OAICustomerFind_200_response_result(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICustomerFind_200_response_result::OAICustomerFind_200_response_result() {
    this->initializeModel();
}

OAICustomerFind_200_response_result::~OAICustomerFind_200_response_result() {}

void OAICustomerFind_200_response_result::initializeModel() {

    m_email_isSet = false;
    m_email_isValid = false;

    m_first_name_isSet = false;
    m_first_name_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_last_name_isSet = false;
    m_last_name_isValid = false;
}

void OAICustomerFind_200_response_result::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICustomerFind_200_response_result::fromJsonObject(QJsonObject json) {

    m_email_isValid = ::OpenAPI::fromJsonValue(m_email, json[QString("email")]);
    m_email_isSet = !json[QString("email")].isNull() && m_email_isValid;

    m_first_name_isValid = ::OpenAPI::fromJsonValue(m_first_name, json[QString("first_name")]);
    m_first_name_isSet = !json[QString("first_name")].isNull() && m_first_name_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_last_name_isValid = ::OpenAPI::fromJsonValue(m_last_name, json[QString("last_name")]);
    m_last_name_isSet = !json[QString("last_name")].isNull() && m_last_name_isValid;
}

QString OAICustomerFind_200_response_result::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICustomerFind_200_response_result::asJsonObject() const {
    QJsonObject obj;
    if (m_email_isSet) {
        obj.insert(QString("email"), ::OpenAPI::toJsonValue(m_email));
    }
    if (m_first_name_isSet) {
        obj.insert(QString("first_name"), ::OpenAPI::toJsonValue(m_first_name));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_last_name_isSet) {
        obj.insert(QString("last_name"), ::OpenAPI::toJsonValue(m_last_name));
    }
    return obj;
}

QString OAICustomerFind_200_response_result::getEmail() const {
    return m_email;
}
void OAICustomerFind_200_response_result::setEmail(const QString &email) {
    m_email = email;
    m_email_isSet = true;
}

bool OAICustomerFind_200_response_result::is_email_Set() const{
    return m_email_isSet;
}

bool OAICustomerFind_200_response_result::is_email_Valid() const{
    return m_email_isValid;
}

QString OAICustomerFind_200_response_result::getFirstName() const {
    return m_first_name;
}
void OAICustomerFind_200_response_result::setFirstName(const QString &first_name) {
    m_first_name = first_name;
    m_first_name_isSet = true;
}

bool OAICustomerFind_200_response_result::is_first_name_Set() const{
    return m_first_name_isSet;
}

bool OAICustomerFind_200_response_result::is_first_name_Valid() const{
    return m_first_name_isValid;
}

QString OAICustomerFind_200_response_result::getId() const {
    return m_id;
}
void OAICustomerFind_200_response_result::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAICustomerFind_200_response_result::is_id_Set() const{
    return m_id_isSet;
}

bool OAICustomerFind_200_response_result::is_id_Valid() const{
    return m_id_isValid;
}

QString OAICustomerFind_200_response_result::getLastName() const {
    return m_last_name;
}
void OAICustomerFind_200_response_result::setLastName(const QString &last_name) {
    m_last_name = last_name;
    m_last_name_isSet = true;
}

bool OAICustomerFind_200_response_result::is_last_name_Set() const{
    return m_last_name_isSet;
}

bool OAICustomerFind_200_response_result::is_last_name_Valid() const{
    return m_last_name_isValid;
}

bool OAICustomerFind_200_response_result::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_email_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_first_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_name_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICustomerFind_200_response_result::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
