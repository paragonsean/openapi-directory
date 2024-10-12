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

#include "OAIWebhookEventCallback.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIWebhookEventCallback::OAIWebhookEventCallback(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIWebhookEventCallback::OAIWebhookEventCallback() {
    this->initializeModel();
}

OAIWebhookEventCallback::~OAIWebhookEventCallback() {}

void OAIWebhookEventCallback::initializeModel() {

    m_data_isSet = false;
    m_data_isValid = false;
}

void OAIWebhookEventCallback::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIWebhookEventCallback::fromJsonObject(QJsonObject json) {

    m_data_isValid = ::OpenAPI::fromJsonValue(m_data, json[QString("data")]);
    m_data_isSet = !json[QString("data")].isNull() && m_data_isValid;
}

QString OAIWebhookEventCallback::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIWebhookEventCallback::asJsonObject() const {
    QJsonObject obj;
    if (m_data.isSet()) {
        obj.insert(QString("data"), ::OpenAPI::toJsonValue(m_data));
    }
    return obj;
}

OAIWebhookEventResource OAIWebhookEventCallback::getData() const {
    return m_data;
}
void OAIWebhookEventCallback::setData(const OAIWebhookEventResource &data) {
    m_data = data;
    m_data_isSet = true;
}

bool OAIWebhookEventCallback::is_data_Set() const{
    return m_data_isSet;
}

bool OAIWebhookEventCallback::is_data_Valid() const{
    return m_data_isValid;
}

bool OAIWebhookEventCallback::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_data.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIWebhookEventCallback::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_data_isValid && true;
}

} // namespace OpenAPI
