/**
 * Otoroshi Admin API
 * Admin API of the Otoroshi reverse proxy
 *
 * The version of the OpenAPI document: 1.5.0-dev
 * Contact: oss@maif.fr
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIInMemoryUser.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIInMemoryUser::OAIInMemoryUser(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIInMemoryUser::OAIInMemoryUser() {
    this->initializeModel();
}

OAIInMemoryUser::~OAIInMemoryUser() {}

void OAIInMemoryUser::initializeModel() {

    m_email_isSet = false;
    m_email_isValid = false;

    m_metadata_isSet = false;
    m_metadata_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_password_isSet = false;
    m_password_isValid = false;
}

void OAIInMemoryUser::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIInMemoryUser::fromJsonObject(QJsonObject json) {

    m_email_isValid = ::OpenAPI::fromJsonValue(m_email, json[QString("email")]);
    m_email_isSet = !json[QString("email")].isNull() && m_email_isValid;

    m_metadata_isValid = ::OpenAPI::fromJsonValue(m_metadata, json[QString("metadata")]);
    m_metadata_isSet = !json[QString("metadata")].isNull() && m_metadata_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_password_isValid = ::OpenAPI::fromJsonValue(m_password, json[QString("password")]);
    m_password_isSet = !json[QString("password")].isNull() && m_password_isValid;
}

QString OAIInMemoryUser::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIInMemoryUser::asJsonObject() const {
    QJsonObject obj;
    if (m_email_isSet) {
        obj.insert(QString("email"), ::OpenAPI::toJsonValue(m_email));
    }
    if (m_metadata.size() > 0) {
        obj.insert(QString("metadata"), ::OpenAPI::toJsonValue(m_metadata));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_password_isSet) {
        obj.insert(QString("password"), ::OpenAPI::toJsonValue(m_password));
    }
    return obj;
}

QString OAIInMemoryUser::getEmail() const {
    return m_email;
}
void OAIInMemoryUser::setEmail(const QString &email) {
    m_email = email;
    m_email_isSet = true;
}

bool OAIInMemoryUser::is_email_Set() const{
    return m_email_isSet;
}

bool OAIInMemoryUser::is_email_Valid() const{
    return m_email_isValid;
}

QMap<QString, QString> OAIInMemoryUser::getMetadata() const {
    return m_metadata;
}
void OAIInMemoryUser::setMetadata(const QMap<QString, QString> &metadata) {
    m_metadata = metadata;
    m_metadata_isSet = true;
}

bool OAIInMemoryUser::is_metadata_Set() const{
    return m_metadata_isSet;
}

bool OAIInMemoryUser::is_metadata_Valid() const{
    return m_metadata_isValid;
}

QString OAIInMemoryUser::getName() const {
    return m_name;
}
void OAIInMemoryUser::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIInMemoryUser::is_name_Set() const{
    return m_name_isSet;
}

bool OAIInMemoryUser::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIInMemoryUser::getPassword() const {
    return m_password;
}
void OAIInMemoryUser::setPassword(const QString &password) {
    m_password = password;
    m_password_isSet = true;
}

bool OAIInMemoryUser::is_password_Set() const{
    return m_password_isSet;
}

bool OAIInMemoryUser::is_password_Valid() const{
    return m_password_isValid;
}

bool OAIInMemoryUser::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_email_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_metadata.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_password_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIInMemoryUser::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_email_isValid && m_metadata_isValid && m_name_isValid && m_password_isValid && true;
}

} // namespace OpenAPI
