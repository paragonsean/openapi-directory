/**
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIUploadShareLinkEmail.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUploadShareLinkEmail::OAIUploadShareLinkEmail(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUploadShareLinkEmail::OAIUploadShareLinkEmail() {
    this->initializeModel();
}

OAIUploadShareLinkEmail::~OAIUploadShareLinkEmail() {}

void OAIUploadShareLinkEmail::initializeModel() {

    m_body_isSet = false;
    m_body_isValid = false;

    m_receiver_language_isSet = false;
    m_receiver_language_isValid = false;

    m_recipients_isSet = false;
    m_recipients_isValid = false;
}

void OAIUploadShareLinkEmail::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUploadShareLinkEmail::fromJsonObject(QJsonObject json) {

    m_body_isValid = ::OpenAPI::fromJsonValue(m_body, json[QString("body")]);
    m_body_isSet = !json[QString("body")].isNull() && m_body_isValid;

    m_receiver_language_isValid = ::OpenAPI::fromJsonValue(m_receiver_language, json[QString("receiverLanguage")]);
    m_receiver_language_isSet = !json[QString("receiverLanguage")].isNull() && m_receiver_language_isValid;

    m_recipients_isValid = ::OpenAPI::fromJsonValue(m_recipients, json[QString("recipients")]);
    m_recipients_isSet = !json[QString("recipients")].isNull() && m_recipients_isValid;
}

QString OAIUploadShareLinkEmail::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUploadShareLinkEmail::asJsonObject() const {
    QJsonObject obj;
    if (m_body_isSet) {
        obj.insert(QString("body"), ::OpenAPI::toJsonValue(m_body));
    }
    if (m_receiver_language_isSet) {
        obj.insert(QString("receiverLanguage"), ::OpenAPI::toJsonValue(m_receiver_language));
    }
    if (m_recipients.size() > 0) {
        obj.insert(QString("recipients"), ::OpenAPI::toJsonValue(m_recipients));
    }
    return obj;
}

QString OAIUploadShareLinkEmail::getBody() const {
    return m_body;
}
void OAIUploadShareLinkEmail::setBody(const QString &body) {
    m_body = body;
    m_body_isSet = true;
}

bool OAIUploadShareLinkEmail::is_body_Set() const{
    return m_body_isSet;
}

bool OAIUploadShareLinkEmail::is_body_Valid() const{
    return m_body_isValid;
}

QString OAIUploadShareLinkEmail::getReceiverLanguage() const {
    return m_receiver_language;
}
void OAIUploadShareLinkEmail::setReceiverLanguage(const QString &receiver_language) {
    m_receiver_language = receiver_language;
    m_receiver_language_isSet = true;
}

bool OAIUploadShareLinkEmail::is_receiver_language_Set() const{
    return m_receiver_language_isSet;
}

bool OAIUploadShareLinkEmail::is_receiver_language_Valid() const{
    return m_receiver_language_isValid;
}

QList<QString> OAIUploadShareLinkEmail::getRecipients() const {
    return m_recipients;
}
void OAIUploadShareLinkEmail::setRecipients(const QList<QString> &recipients) {
    m_recipients = recipients;
    m_recipients_isSet = true;
}

bool OAIUploadShareLinkEmail::is_recipients_Set() const{
    return m_recipients_isSet;
}

bool OAIUploadShareLinkEmail::is_recipients_Valid() const{
    return m_recipients_isValid;
}

bool OAIUploadShareLinkEmail::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_body_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_receiver_language_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_recipients.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUploadShareLinkEmail::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_body_isValid && m_recipients_isValid && true;
}

} // namespace OpenAPI
