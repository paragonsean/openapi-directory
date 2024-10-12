/**
 * Mailscript
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.4.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAddActionReplyRequest_config.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAddActionReplyRequest_config::OAIAddActionReplyRequest_config(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAddActionReplyRequest_config::OAIAddActionReplyRequest_config() {
    this->initializeModel();
}

OAIAddActionReplyRequest_config::~OAIAddActionReplyRequest_config() {}

void OAIAddActionReplyRequest_config::initializeModel() {

    m_from_isSet = false;
    m_from_isValid = false;

    m_html_isSet = false;
    m_html_isValid = false;

    m_key_isSet = false;
    m_key_isValid = false;

    m_text_isSet = false;
    m_text_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIAddActionReplyRequest_config::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAddActionReplyRequest_config::fromJsonObject(QJsonObject json) {

    m_from_isValid = ::OpenAPI::fromJsonValue(m_from, json[QString("from")]);
    m_from_isSet = !json[QString("from")].isNull() && m_from_isValid;

    m_html_isValid = ::OpenAPI::fromJsonValue(m_html, json[QString("html")]);
    m_html_isSet = !json[QString("html")].isNull() && m_html_isValid;

    m_key_isValid = ::OpenAPI::fromJsonValue(m_key, json[QString("key")]);
    m_key_isSet = !json[QString("key")].isNull() && m_key_isValid;

    m_text_isValid = ::OpenAPI::fromJsonValue(m_text, json[QString("text")]);
    m_text_isSet = !json[QString("text")].isNull() && m_text_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAIAddActionReplyRequest_config::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAddActionReplyRequest_config::asJsonObject() const {
    QJsonObject obj;
    if (m_from_isSet) {
        obj.insert(QString("from"), ::OpenAPI::toJsonValue(m_from));
    }
    if (m_html_isSet) {
        obj.insert(QString("html"), ::OpenAPI::toJsonValue(m_html));
    }
    if (m_key_isSet) {
        obj.insert(QString("key"), ::OpenAPI::toJsonValue(m_key));
    }
    if (m_text_isSet) {
        obj.insert(QString("text"), ::OpenAPI::toJsonValue(m_text));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

QString OAIAddActionReplyRequest_config::getFrom() const {
    return m_from;
}
void OAIAddActionReplyRequest_config::setFrom(const QString &from) {
    m_from = from;
    m_from_isSet = true;
}

bool OAIAddActionReplyRequest_config::is_from_Set() const{
    return m_from_isSet;
}

bool OAIAddActionReplyRequest_config::is_from_Valid() const{
    return m_from_isValid;
}

QString OAIAddActionReplyRequest_config::getHtml() const {
    return m_html;
}
void OAIAddActionReplyRequest_config::setHtml(const QString &html) {
    m_html = html;
    m_html_isSet = true;
}

bool OAIAddActionReplyRequest_config::is_html_Set() const{
    return m_html_isSet;
}

bool OAIAddActionReplyRequest_config::is_html_Valid() const{
    return m_html_isValid;
}

QString OAIAddActionReplyRequest_config::getKey() const {
    return m_key;
}
void OAIAddActionReplyRequest_config::setKey(const QString &key) {
    m_key = key;
    m_key_isSet = true;
}

bool OAIAddActionReplyRequest_config::is_key_Set() const{
    return m_key_isSet;
}

bool OAIAddActionReplyRequest_config::is_key_Valid() const{
    return m_key_isValid;
}

QString OAIAddActionReplyRequest_config::getText() const {
    return m_text;
}
void OAIAddActionReplyRequest_config::setText(const QString &text) {
    m_text = text;
    m_text_isSet = true;
}

bool OAIAddActionReplyRequest_config::is_text_Set() const{
    return m_text_isSet;
}

bool OAIAddActionReplyRequest_config::is_text_Valid() const{
    return m_text_isValid;
}

QString OAIAddActionReplyRequest_config::getType() const {
    return m_type;
}
void OAIAddActionReplyRequest_config::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIAddActionReplyRequest_config::is_type_Set() const{
    return m_type_isSet;
}

bool OAIAddActionReplyRequest_config::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIAddActionReplyRequest_config::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_from_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_html_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_key_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_text_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAddActionReplyRequest_config::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_from_isValid && m_key_isValid && m_type_isValid && true;
}

} // namespace OpenAPI
