/**
 * ManagedLabsClient
 * The Managed Labs Client.
 *
 * The version of the OpenAPI document: 2018-10-15
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAddUsersPayload.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAddUsersPayload::OAIAddUsersPayload(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAddUsersPayload::OAIAddUsersPayload() {
    this->initializeModel();
}

OAIAddUsersPayload::~OAIAddUsersPayload() {}

void OAIAddUsersPayload::initializeModel() {

    m_email_addresses_isSet = false;
    m_email_addresses_isValid = false;
}

void OAIAddUsersPayload::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAddUsersPayload::fromJsonObject(QJsonObject json) {

    m_email_addresses_isValid = ::OpenAPI::fromJsonValue(m_email_addresses, json[QString("emailAddresses")]);
    m_email_addresses_isSet = !json[QString("emailAddresses")].isNull() && m_email_addresses_isValid;
}

QString OAIAddUsersPayload::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAddUsersPayload::asJsonObject() const {
    QJsonObject obj;
    if (m_email_addresses.size() > 0) {
        obj.insert(QString("emailAddresses"), ::OpenAPI::toJsonValue(m_email_addresses));
    }
    return obj;
}

QList<QString> OAIAddUsersPayload::getEmailAddresses() const {
    return m_email_addresses;
}
void OAIAddUsersPayload::setEmailAddresses(const QList<QString> &email_addresses) {
    m_email_addresses = email_addresses;
    m_email_addresses_isSet = true;
}

bool OAIAddUsersPayload::is_email_addresses_Set() const{
    return m_email_addresses_isSet;
}

bool OAIAddUsersPayload::is_email_addresses_Valid() const{
    return m_email_addresses_isValid;
}

bool OAIAddUsersPayload::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_email_addresses.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAddUsersPayload::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_email_addresses_isValid && true;
}

} // namespace OpenAPI
