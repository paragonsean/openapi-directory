/**
 * API for the COVID-19 Tracking QR Code Signin Server.
 * This is the API for the COVID-19 Contact Tracing QRCode Signin Server
 *
 * The version of the OpenAPI document: 1.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIUserRecord.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUserRecord::OAIUserRecord(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUserRecord::OAIUserRecord() {
    this->initializeModel();
}

OAIUserRecord::~OAIUserRecord() {}

void OAIUserRecord::initializeModel() {

    m_admin_isSet = false;
    m_admin_isValid = false;

    m_email_isSet = false;
    m_email_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_read_only_isSet = false;
    m_read_only_isValid = false;
}

void OAIUserRecord::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUserRecord::fromJsonObject(QJsonObject json) {

    m_admin_isValid = ::OpenAPI::fromJsonValue(m_admin, json[QString("admin")]);
    m_admin_isSet = !json[QString("admin")].isNull() && m_admin_isValid;

    m_email_isValid = ::OpenAPI::fromJsonValue(m_email, json[QString("email")]);
    m_email_isSet = !json[QString("email")].isNull() && m_email_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_read_only_isValid = ::OpenAPI::fromJsonValue(m_read_only, json[QString("read_only")]);
    m_read_only_isSet = !json[QString("read_only")].isNull() && m_read_only_isValid;
}

QString OAIUserRecord::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUserRecord::asJsonObject() const {
    QJsonObject obj;
    if (m_admin_isSet) {
        obj.insert(QString("admin"), ::OpenAPI::toJsonValue(m_admin));
    }
    if (m_email_isSet) {
        obj.insert(QString("email"), ::OpenAPI::toJsonValue(m_email));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_read_only_isSet) {
        obj.insert(QString("read_only"), ::OpenAPI::toJsonValue(m_read_only));
    }
    return obj;
}

bool OAIUserRecord::isAdmin() const {
    return m_admin;
}
void OAIUserRecord::setAdmin(const bool &admin) {
    m_admin = admin;
    m_admin_isSet = true;
}

bool OAIUserRecord::is_admin_Set() const{
    return m_admin_isSet;
}

bool OAIUserRecord::is_admin_Valid() const{
    return m_admin_isValid;
}

QString OAIUserRecord::getEmail() const {
    return m_email;
}
void OAIUserRecord::setEmail(const QString &email) {
    m_email = email;
    m_email_isSet = true;
}

bool OAIUserRecord::is_email_Set() const{
    return m_email_isSet;
}

bool OAIUserRecord::is_email_Valid() const{
    return m_email_isValid;
}

qint32 OAIUserRecord::getId() const {
    return m_id;
}
void OAIUserRecord::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIUserRecord::is_id_Set() const{
    return m_id_isSet;
}

bool OAIUserRecord::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIUserRecord::getName() const {
    return m_name;
}
void OAIUserRecord::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIUserRecord::is_name_Set() const{
    return m_name_isSet;
}

bool OAIUserRecord::is_name_Valid() const{
    return m_name_isValid;
}

bool OAIUserRecord::isReadOnly() const {
    return m_read_only;
}
void OAIUserRecord::setReadOnly(const bool &read_only) {
    m_read_only = read_only;
    m_read_only_isSet = true;
}

bool OAIUserRecord::is_read_only_Set() const{
    return m_read_only_isSet;
}

bool OAIUserRecord::is_read_only_Valid() const{
    return m_read_only_isValid;
}

bool OAIUserRecord::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_admin_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_email_isSet) {
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

        if (m_read_only_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUserRecord::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
