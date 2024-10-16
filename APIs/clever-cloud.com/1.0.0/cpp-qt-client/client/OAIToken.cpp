/**
 * Clever-Cloud API
 * Public API for managing Clever-Cloud data and products
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIToken.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIToken::OAIToken(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIToken::OAIToken() {
    this->initializeModel();
}

OAIToken::~OAIToken() {}

void OAIToken::initializeModel() {

    m_consumer_isSet = false;
    m_consumer_isValid = false;

    m_creation_date_isSet = false;
    m_creation_date_isValid = false;

    m_last_utilisation_isSet = false;
    m_last_utilisation_isValid = false;

    m_rights_isSet = false;
    m_rights_isValid = false;

    m_token_isSet = false;
    m_token_isValid = false;
}

void OAIToken::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIToken::fromJsonObject(QJsonObject json) {

    m_consumer_isValid = ::OpenAPI::fromJsonValue(m_consumer, json[QString("consumer")]);
    m_consumer_isSet = !json[QString("consumer")].isNull() && m_consumer_isValid;

    m_creation_date_isValid = ::OpenAPI::fromJsonValue(m_creation_date, json[QString("creationDate")]);
    m_creation_date_isSet = !json[QString("creationDate")].isNull() && m_creation_date_isValid;

    m_last_utilisation_isValid = ::OpenAPI::fromJsonValue(m_last_utilisation, json[QString("lastUtilisation")]);
    m_last_utilisation_isSet = !json[QString("lastUtilisation")].isNull() && m_last_utilisation_isValid;

    m_rights_isValid = ::OpenAPI::fromJsonValue(m_rights, json[QString("rights")]);
    m_rights_isSet = !json[QString("rights")].isNull() && m_rights_isValid;

    m_token_isValid = ::OpenAPI::fromJsonValue(m_token, json[QString("token")]);
    m_token_isSet = !json[QString("token")].isNull() && m_token_isValid;
}

QString OAIToken::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIToken::asJsonObject() const {
    QJsonObject obj;
    if (m_consumer.isSet()) {
        obj.insert(QString("consumer"), ::OpenAPI::toJsonValue(m_consumer));
    }
    if (m_creation_date_isSet) {
        obj.insert(QString("creationDate"), ::OpenAPI::toJsonValue(m_creation_date));
    }
    if (m_last_utilisation_isSet) {
        obj.insert(QString("lastUtilisation"), ::OpenAPI::toJsonValue(m_last_utilisation));
    }
    if (m_rights.isSet()) {
        obj.insert(QString("rights"), ::OpenAPI::toJsonValue(m_rights));
    }
    if (m_token_isSet) {
        obj.insert(QString("token"), ::OpenAPI::toJsonValue(m_token));
    }
    return obj;
}

OAIConsumer OAIToken::getConsumer() const {
    return m_consumer;
}
void OAIToken::setConsumer(const OAIConsumer &consumer) {
    m_consumer = consumer;
    m_consumer_isSet = true;
}

bool OAIToken::is_consumer_Set() const{
    return m_consumer_isSet;
}

bool OAIToken::is_consumer_Valid() const{
    return m_consumer_isValid;
}

qint32 OAIToken::getCreationDate() const {
    return m_creation_date;
}
void OAIToken::setCreationDate(const qint32 &creation_date) {
    m_creation_date = creation_date;
    m_creation_date_isSet = true;
}

bool OAIToken::is_creation_date_Set() const{
    return m_creation_date_isSet;
}

bool OAIToken::is_creation_date_Valid() const{
    return m_creation_date_isValid;
}

QString OAIToken::getLastUtilisation() const {
    return m_last_utilisation;
}
void OAIToken::setLastUtilisation(const QString &last_utilisation) {
    m_last_utilisation = last_utilisation;
    m_last_utilisation_isSet = true;
}

bool OAIToken::is_last_utilisation_Set() const{
    return m_last_utilisation_isSet;
}

bool OAIToken::is_last_utilisation_Valid() const{
    return m_last_utilisation_isValid;
}

OAIRights OAIToken::getRights() const {
    return m_rights;
}
void OAIToken::setRights(const OAIRights &rights) {
    m_rights = rights;
    m_rights_isSet = true;
}

bool OAIToken::is_rights_Set() const{
    return m_rights_isSet;
}

bool OAIToken::is_rights_Valid() const{
    return m_rights_isValid;
}

QString OAIToken::getToken() const {
    return m_token;
}
void OAIToken::setToken(const QString &token) {
    m_token = token;
    m_token_isSet = true;
}

bool OAIToken::is_token_Set() const{
    return m_token_isSet;
}

bool OAIToken::is_token_Valid() const{
    return m_token_isValid;
}

bool OAIToken::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_consumer.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_creation_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_utilisation_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_rights.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_token_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIToken::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_consumer_isValid && m_creation_date_isValid && m_last_utilisation_isValid && m_rights_isValid && m_token_isValid && true;
}

} // namespace OpenAPI
