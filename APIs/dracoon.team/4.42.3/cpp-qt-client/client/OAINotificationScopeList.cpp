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

#include "OAINotificationScopeList.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAINotificationScopeList::OAINotificationScopeList(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAINotificationScopeList::OAINotificationScopeList() {
    this->initializeModel();
}

OAINotificationScopeList::~OAINotificationScopeList() {}

void OAINotificationScopeList::initializeModel() {

    m_items_isSet = false;
    m_items_isValid = false;
}

void OAINotificationScopeList::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAINotificationScopeList::fromJsonObject(QJsonObject json) {

    m_items_isValid = ::OpenAPI::fromJsonValue(m_items, json[QString("items")]);
    m_items_isSet = !json[QString("items")].isNull() && m_items_isValid;
}

QString OAINotificationScopeList::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAINotificationScopeList::asJsonObject() const {
    QJsonObject obj;
    if (m_items.size() > 0) {
        obj.insert(QString("items"), ::OpenAPI::toJsonValue(m_items));
    }
    return obj;
}

QList<OAINotificationScope> OAINotificationScopeList::getItems() const {
    return m_items;
}
void OAINotificationScopeList::setItems(const QList<OAINotificationScope> &items) {
    m_items = items;
    m_items_isSet = true;
}

bool OAINotificationScopeList::is_items_Set() const{
    return m_items_isSet;
}

bool OAINotificationScopeList::is_items_Valid() const{
    return m_items_isValid;
}

bool OAINotificationScopeList::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_items.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAINotificationScopeList::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_items_isValid && true;
}

} // namespace OpenAPI
