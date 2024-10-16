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

#include "OAIUserUserPublicKeyList.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUserUserPublicKeyList::OAIUserUserPublicKeyList(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUserUserPublicKeyList::OAIUserUserPublicKeyList() {
    this->initializeModel();
}

OAIUserUserPublicKeyList::~OAIUserUserPublicKeyList() {}

void OAIUserUserPublicKeyList::initializeModel() {

    m_items_isSet = false;
    m_items_isValid = false;
}

void OAIUserUserPublicKeyList::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUserUserPublicKeyList::fromJsonObject(QJsonObject json) {

    m_items_isValid = ::OpenAPI::fromJsonValue(m_items, json[QString("items")]);
    m_items_isSet = !json[QString("items")].isNull() && m_items_isValid;
}

QString OAIUserUserPublicKeyList::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUserUserPublicKeyList::asJsonObject() const {
    QJsonObject obj;
    if (m_items.size() > 0) {
        obj.insert(QString("items"), ::OpenAPI::toJsonValue(m_items));
    }
    return obj;
}

QList<OAIUserUserPublicKey> OAIUserUserPublicKeyList::getItems() const {
    return m_items;
}
void OAIUserUserPublicKeyList::setItems(const QList<OAIUserUserPublicKey> &items) {
    m_items = items;
    m_items_isSet = true;
}

bool OAIUserUserPublicKeyList::is_items_Set() const{
    return m_items_isSet;
}

bool OAIUserUserPublicKeyList::is_items_Valid() const{
    return m_items_isValid;
}

bool OAIUserUserPublicKeyList::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_items.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUserUserPublicKeyList::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_items_isValid && true;
}

} // namespace OpenAPI
