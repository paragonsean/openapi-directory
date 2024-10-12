/**
 * Up API
 * The Up API gives you programmatic access to your balances and transaction data. You can request past transactions or set up webhooks to receive real-time events when new transactions hit your account. It’s new, it’s exciting and it’s just the beginning. 
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIWebhookInputResource_attributes.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIWebhookInputResource_attributes::OAIWebhookInputResource_attributes(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIWebhookInputResource_attributes::OAIWebhookInputResource_attributes() {
    this->initializeModel();
}

OAIWebhookInputResource_attributes::~OAIWebhookInputResource_attributes() {}

void OAIWebhookInputResource_attributes::initializeModel() {

    m_description_isSet = false;
    m_description_isValid = false;

    m_url_isSet = false;
    m_url_isValid = false;
}

void OAIWebhookInputResource_attributes::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIWebhookInputResource_attributes::fromJsonObject(QJsonObject json) {

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_url_isValid = ::OpenAPI::fromJsonValue(m_url, json[QString("url")]);
    m_url_isSet = !json[QString("url")].isNull() && m_url_isValid;
}

QString OAIWebhookInputResource_attributes::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIWebhookInputResource_attributes::asJsonObject() const {
    QJsonObject obj;
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_url_isSet) {
        obj.insert(QString("url"), ::OpenAPI::toJsonValue(m_url));
    }
    return obj;
}

QString OAIWebhookInputResource_attributes::getDescription() const {
    return m_description;
}
void OAIWebhookInputResource_attributes::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIWebhookInputResource_attributes::is_description_Set() const{
    return m_description_isSet;
}

bool OAIWebhookInputResource_attributes::is_description_Valid() const{
    return m_description_isValid;
}

QString OAIWebhookInputResource_attributes::getUrl() const {
    return m_url;
}
void OAIWebhookInputResource_attributes::setUrl(const QString &url) {
    m_url = url;
    m_url_isSet = true;
}

bool OAIWebhookInputResource_attributes::is_url_Set() const{
    return m_url_isSet;
}

bool OAIWebhookInputResource_attributes::is_url_Valid() const{
    return m_url_isValid;
}

bool OAIWebhookInputResource_attributes::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_url_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIWebhookInputResource_attributes::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_url_isValid && true;
}

} // namespace OpenAPI
