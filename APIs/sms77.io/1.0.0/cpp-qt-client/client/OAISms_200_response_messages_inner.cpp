/**
 * seven.io API
 * seven.io Swagger API. Get your API-Key now at seven.io.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: support@seven.io
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAISms_200_response_messages_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISms_200_response_messages_inner::OAISms_200_response_messages_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISms_200_response_messages_inner::OAISms_200_response_messages_inner() {
    this->initializeModel();
}

OAISms_200_response_messages_inner::~OAISms_200_response_messages_inner() {}

void OAISms_200_response_messages_inner::initializeModel() {

    m_encoding_isSet = false;
    m_encoding_isValid = false;

    m_error_isSet = false;
    m_error_isValid = false;

    m_error_text_isSet = false;
    m_error_text_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_messages_isSet = false;
    m_messages_isValid = false;

    m_parts_isSet = false;
    m_parts_isValid = false;

    m_price_isSet = false;
    m_price_isValid = false;

    m_recipient_isSet = false;
    m_recipient_isValid = false;

    m_sender_isSet = false;
    m_sender_isValid = false;

    m_success_isSet = false;
    m_success_isValid = false;

    m_text_isSet = false;
    m_text_isValid = false;
}

void OAISms_200_response_messages_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISms_200_response_messages_inner::fromJsonObject(QJsonObject json) {

    m_encoding_isValid = ::OpenAPI::fromJsonValue(m_encoding, json[QString("encoding")]);
    m_encoding_isSet = !json[QString("encoding")].isNull() && m_encoding_isValid;

    m_error_isValid = ::OpenAPI::fromJsonValue(m_error, json[QString("error")]);
    m_error_isSet = !json[QString("error")].isNull() && m_error_isValid;

    m_error_text_isValid = ::OpenAPI::fromJsonValue(m_error_text, json[QString("error_text")]);
    m_error_text_isSet = !json[QString("error_text")].isNull() && m_error_text_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_messages_isValid = ::OpenAPI::fromJsonValue(m_messages, json[QString("messages")]);
    m_messages_isSet = !json[QString("messages")].isNull() && m_messages_isValid;

    m_parts_isValid = ::OpenAPI::fromJsonValue(m_parts, json[QString("parts")]);
    m_parts_isSet = !json[QString("parts")].isNull() && m_parts_isValid;

    m_price_isValid = ::OpenAPI::fromJsonValue(m_price, json[QString("price")]);
    m_price_isSet = !json[QString("price")].isNull() && m_price_isValid;

    m_recipient_isValid = ::OpenAPI::fromJsonValue(m_recipient, json[QString("recipient")]);
    m_recipient_isSet = !json[QString("recipient")].isNull() && m_recipient_isValid;

    m_sender_isValid = ::OpenAPI::fromJsonValue(m_sender, json[QString("sender")]);
    m_sender_isSet = !json[QString("sender")].isNull() && m_sender_isValid;

    m_success_isValid = ::OpenAPI::fromJsonValue(m_success, json[QString("success")]);
    m_success_isSet = !json[QString("success")].isNull() && m_success_isValid;

    m_text_isValid = ::OpenAPI::fromJsonValue(m_text, json[QString("text")]);
    m_text_isSet = !json[QString("text")].isNull() && m_text_isValid;
}

QString OAISms_200_response_messages_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISms_200_response_messages_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_encoding_isSet) {
        obj.insert(QString("encoding"), ::OpenAPI::toJsonValue(m_encoding));
    }
    if (m_error_isSet) {
        obj.insert(QString("error"), ::OpenAPI::toJsonValue(m_error));
    }
    if (m_error_text_isSet) {
        obj.insert(QString("error_text"), ::OpenAPI::toJsonValue(m_error_text));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_messages.size() > 0) {
        obj.insert(QString("messages"), ::OpenAPI::toJsonValue(m_messages));
    }
    if (m_parts_isSet) {
        obj.insert(QString("parts"), ::OpenAPI::toJsonValue(m_parts));
    }
    if (m_price_isSet) {
        obj.insert(QString("price"), ::OpenAPI::toJsonValue(m_price));
    }
    if (m_recipient_isSet) {
        obj.insert(QString("recipient"), ::OpenAPI::toJsonValue(m_recipient));
    }
    if (m_sender_isSet) {
        obj.insert(QString("sender"), ::OpenAPI::toJsonValue(m_sender));
    }
    if (m_success_isSet) {
        obj.insert(QString("success"), ::OpenAPI::toJsonValue(m_success));
    }
    if (m_text_isSet) {
        obj.insert(QString("text"), ::OpenAPI::toJsonValue(m_text));
    }
    return obj;
}

QString OAISms_200_response_messages_inner::getEncoding() const {
    return m_encoding;
}
void OAISms_200_response_messages_inner::setEncoding(const QString &encoding) {
    m_encoding = encoding;
    m_encoding_isSet = true;
}

bool OAISms_200_response_messages_inner::is_encoding_Set() const{
    return m_encoding_isSet;
}

bool OAISms_200_response_messages_inner::is_encoding_Valid() const{
    return m_encoding_isValid;
}

QString OAISms_200_response_messages_inner::getError() const {
    return m_error;
}
void OAISms_200_response_messages_inner::setError(const QString &error) {
    m_error = error;
    m_error_isSet = true;
}

bool OAISms_200_response_messages_inner::is_error_Set() const{
    return m_error_isSet;
}

bool OAISms_200_response_messages_inner::is_error_Valid() const{
    return m_error_isValid;
}

QString OAISms_200_response_messages_inner::getErrorText() const {
    return m_error_text;
}
void OAISms_200_response_messages_inner::setErrorText(const QString &error_text) {
    m_error_text = error_text;
    m_error_text_isSet = true;
}

bool OAISms_200_response_messages_inner::is_error_text_Set() const{
    return m_error_text_isSet;
}

bool OAISms_200_response_messages_inner::is_error_text_Valid() const{
    return m_error_text_isValid;
}

QString OAISms_200_response_messages_inner::getId() const {
    return m_id;
}
void OAISms_200_response_messages_inner::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAISms_200_response_messages_inner::is_id_Set() const{
    return m_id_isSet;
}

bool OAISms_200_response_messages_inner::is_id_Valid() const{
    return m_id_isValid;
}

QList<QString> OAISms_200_response_messages_inner::getMessages() const {
    return m_messages;
}
void OAISms_200_response_messages_inner::setMessages(const QList<QString> &messages) {
    m_messages = messages;
    m_messages_isSet = true;
}

bool OAISms_200_response_messages_inner::is_messages_Set() const{
    return m_messages_isSet;
}

bool OAISms_200_response_messages_inner::is_messages_Valid() const{
    return m_messages_isValid;
}

qint32 OAISms_200_response_messages_inner::getParts() const {
    return m_parts;
}
void OAISms_200_response_messages_inner::setParts(const qint32 &parts) {
    m_parts = parts;
    m_parts_isSet = true;
}

bool OAISms_200_response_messages_inner::is_parts_Set() const{
    return m_parts_isSet;
}

bool OAISms_200_response_messages_inner::is_parts_Valid() const{
    return m_parts_isValid;
}

qint32 OAISms_200_response_messages_inner::getPrice() const {
    return m_price;
}
void OAISms_200_response_messages_inner::setPrice(const qint32 &price) {
    m_price = price;
    m_price_isSet = true;
}

bool OAISms_200_response_messages_inner::is_price_Set() const{
    return m_price_isSet;
}

bool OAISms_200_response_messages_inner::is_price_Valid() const{
    return m_price_isValid;
}

QString OAISms_200_response_messages_inner::getRecipient() const {
    return m_recipient;
}
void OAISms_200_response_messages_inner::setRecipient(const QString &recipient) {
    m_recipient = recipient;
    m_recipient_isSet = true;
}

bool OAISms_200_response_messages_inner::is_recipient_Set() const{
    return m_recipient_isSet;
}

bool OAISms_200_response_messages_inner::is_recipient_Valid() const{
    return m_recipient_isValid;
}

QString OAISms_200_response_messages_inner::getSender() const {
    return m_sender;
}
void OAISms_200_response_messages_inner::setSender(const QString &sender) {
    m_sender = sender;
    m_sender_isSet = true;
}

bool OAISms_200_response_messages_inner::is_sender_Set() const{
    return m_sender_isSet;
}

bool OAISms_200_response_messages_inner::is_sender_Valid() const{
    return m_sender_isValid;
}

bool OAISms_200_response_messages_inner::isSuccess() const {
    return m_success;
}
void OAISms_200_response_messages_inner::setSuccess(const bool &success) {
    m_success = success;
    m_success_isSet = true;
}

bool OAISms_200_response_messages_inner::is_success_Set() const{
    return m_success_isSet;
}

bool OAISms_200_response_messages_inner::is_success_Valid() const{
    return m_success_isValid;
}

QString OAISms_200_response_messages_inner::getText() const {
    return m_text;
}
void OAISms_200_response_messages_inner::setText(const QString &text) {
    m_text = text;
    m_text_isSet = true;
}

bool OAISms_200_response_messages_inner::is_text_Set() const{
    return m_text_isSet;
}

bool OAISms_200_response_messages_inner::is_text_Valid() const{
    return m_text_isValid;
}

bool OAISms_200_response_messages_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_encoding_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_error_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_error_text_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_messages.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_parts_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_price_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_recipient_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sender_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_success_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_text_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISms_200_response_messages_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
