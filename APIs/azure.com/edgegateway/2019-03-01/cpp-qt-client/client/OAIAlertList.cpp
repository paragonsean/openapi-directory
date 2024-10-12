/**
 * DataBoxEdgeManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-03-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAlertList.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAlertList::OAIAlertList(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAlertList::OAIAlertList() {
    this->initializeModel();
}

OAIAlertList::~OAIAlertList() {}

void OAIAlertList::initializeModel() {

    m_next_link_isSet = false;
    m_next_link_isValid = false;

    m_value_isSet = false;
    m_value_isValid = false;
}

void OAIAlertList::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAlertList::fromJsonObject(QJsonObject json) {

    m_next_link_isValid = ::OpenAPI::fromJsonValue(m_next_link, json[QString("nextLink")]);
    m_next_link_isSet = !json[QString("nextLink")].isNull() && m_next_link_isValid;

    m_value_isValid = ::OpenAPI::fromJsonValue(m_value, json[QString("value")]);
    m_value_isSet = !json[QString("value")].isNull() && m_value_isValid;
}

QString OAIAlertList::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAlertList::asJsonObject() const {
    QJsonObject obj;
    if (m_next_link_isSet) {
        obj.insert(QString("nextLink"), ::OpenAPI::toJsonValue(m_next_link));
    }
    if (m_value.size() > 0) {
        obj.insert(QString("value"), ::OpenAPI::toJsonValue(m_value));
    }
    return obj;
}

QString OAIAlertList::getNextLink() const {
    return m_next_link;
}
void OAIAlertList::setNextLink(const QString &next_link) {
    m_next_link = next_link;
    m_next_link_isSet = true;
}

bool OAIAlertList::is_next_link_Set() const{
    return m_next_link_isSet;
}

bool OAIAlertList::is_next_link_Valid() const{
    return m_next_link_isValid;
}

QList<OAIAlert> OAIAlertList::getValue() const {
    return m_value;
}
void OAIAlertList::setValue(const QList<OAIAlert> &value) {
    m_value = value;
    m_value_isSet = true;
}

bool OAIAlertList::is_value_Set() const{
    return m_value_isSet;
}

bool OAIAlertList::is_value_Valid() const{
    return m_value_isValid;
}

bool OAIAlertList::isSet() const {
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

bool OAIAlertList::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
