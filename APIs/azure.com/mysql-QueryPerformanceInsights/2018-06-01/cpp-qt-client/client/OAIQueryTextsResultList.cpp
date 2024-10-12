/**
 * MySQLManagementClient
 * The Microsoft Azure management API provides create, read, update, and delete functionality for Azure MySQL resources including servers, databases, firewall rules, VNET rules, security alert policies, log files and configurations with new business model.
 *
 * The version of the OpenAPI document: 2018-06-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIQueryTextsResultList.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIQueryTextsResultList::OAIQueryTextsResultList(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIQueryTextsResultList::OAIQueryTextsResultList() {
    this->initializeModel();
}

OAIQueryTextsResultList::~OAIQueryTextsResultList() {}

void OAIQueryTextsResultList::initializeModel() {

    m_next_link_isSet = false;
    m_next_link_isValid = false;

    m_value_isSet = false;
    m_value_isValid = false;
}

void OAIQueryTextsResultList::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIQueryTextsResultList::fromJsonObject(QJsonObject json) {

    m_next_link_isValid = ::OpenAPI::fromJsonValue(m_next_link, json[QString("nextLink")]);
    m_next_link_isSet = !json[QString("nextLink")].isNull() && m_next_link_isValid;

    m_value_isValid = ::OpenAPI::fromJsonValue(m_value, json[QString("value")]);
    m_value_isSet = !json[QString("value")].isNull() && m_value_isValid;
}

QString OAIQueryTextsResultList::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIQueryTextsResultList::asJsonObject() const {
    QJsonObject obj;
    if (m_next_link_isSet) {
        obj.insert(QString("nextLink"), ::OpenAPI::toJsonValue(m_next_link));
    }
    if (m_value.size() > 0) {
        obj.insert(QString("value"), ::OpenAPI::toJsonValue(m_value));
    }
    return obj;
}

QString OAIQueryTextsResultList::getNextLink() const {
    return m_next_link;
}
void OAIQueryTextsResultList::setNextLink(const QString &next_link) {
    m_next_link = next_link;
    m_next_link_isSet = true;
}

bool OAIQueryTextsResultList::is_next_link_Set() const{
    return m_next_link_isSet;
}

bool OAIQueryTextsResultList::is_next_link_Valid() const{
    return m_next_link_isValid;
}

QList<OAIQueryText> OAIQueryTextsResultList::getValue() const {
    return m_value;
}
void OAIQueryTextsResultList::setValue(const QList<OAIQueryText> &value) {
    m_value = value;
    m_value_isSet = true;
}

bool OAIQueryTextsResultList::is_value_Set() const{
    return m_value_isSet;
}

bool OAIQueryTextsResultList::is_value_Valid() const{
    return m_value_isValid;
}

bool OAIQueryTextsResultList::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_next_link_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_value.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIQueryTextsResultList::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
