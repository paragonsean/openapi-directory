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

#include "OAIRoomWebhookList.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIRoomWebhookList::OAIRoomWebhookList(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIRoomWebhookList::OAIRoomWebhookList() {
    this->initializeModel();
}

OAIRoomWebhookList::~OAIRoomWebhookList() {}

void OAIRoomWebhookList::initializeModel() {

    m_items_isSet = false;
    m_items_isValid = false;

    m_range_isSet = false;
    m_range_isValid = false;
}

void OAIRoomWebhookList::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIRoomWebhookList::fromJsonObject(QJsonObject json) {

    m_items_isValid = ::OpenAPI::fromJsonValue(m_items, json[QString("items")]);
    m_items_isSet = !json[QString("items")].isNull() && m_items_isValid;

    m_range_isValid = ::OpenAPI::fromJsonValue(m_range, json[QString("range")]);
    m_range_isSet = !json[QString("range")].isNull() && m_range_isValid;
}

QString OAIRoomWebhookList::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIRoomWebhookList::asJsonObject() const {
    QJsonObject obj;
    if (m_items.size() > 0) {
        obj.insert(QString("items"), ::OpenAPI::toJsonValue(m_items));
    }
    if (m_range.isSet()) {
        obj.insert(QString("range"), ::OpenAPI::toJsonValue(m_range));
    }
    return obj;
}

QList<OAIRoomWebhook> OAIRoomWebhookList::getItems() const {
    return m_items;
}
void OAIRoomWebhookList::setItems(const QList<OAIRoomWebhook> &items) {
    m_items = items;
    m_items_isSet = true;
}

bool OAIRoomWebhookList::is_items_Set() const{
    return m_items_isSet;
}

bool OAIRoomWebhookList::is_items_Valid() const{
    return m_items_isValid;
}

OAIRange OAIRoomWebhookList::getRange() const {
    return m_range;
}
void OAIRoomWebhookList::setRange(const OAIRange &range) {
    m_range = range;
    m_range_isSet = true;
}

bool OAIRoomWebhookList::is_range_Set() const{
    return m_range_isSet;
}

bool OAIRoomWebhookList::is_range_Valid() const{
    return m_range_isValid;
}

bool OAIRoomWebhookList::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_items.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_range.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIRoomWebhookList::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_items_isValid && m_range_isValid && true;
}

} // namespace OpenAPI
