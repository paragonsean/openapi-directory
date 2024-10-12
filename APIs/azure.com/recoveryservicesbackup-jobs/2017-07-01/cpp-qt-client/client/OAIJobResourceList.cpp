/**
 * RecoveryServicesBackupClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2017-07-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIJobResourceList.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIJobResourceList::OAIJobResourceList(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIJobResourceList::OAIJobResourceList() {
    this->initializeModel();
}

OAIJobResourceList::~OAIJobResourceList() {}

void OAIJobResourceList::initializeModel() {

    m_value_isSet = false;
    m_value_isValid = false;

    m_next_link_isSet = false;
    m_next_link_isValid = false;
}

void OAIJobResourceList::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIJobResourceList::fromJsonObject(QJsonObject json) {

    m_value_isValid = ::OpenAPI::fromJsonValue(m_value, json[QString("value")]);
    m_value_isSet = !json[QString("value")].isNull() && m_value_isValid;

    m_next_link_isValid = ::OpenAPI::fromJsonValue(m_next_link, json[QString("nextLink")]);
    m_next_link_isSet = !json[QString("nextLink")].isNull() && m_next_link_isValid;
}

QString OAIJobResourceList::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIJobResourceList::asJsonObject() const {
    QJsonObject obj;
    if (m_value.size() > 0) {
        obj.insert(QString("value"), ::OpenAPI::toJsonValue(m_value));
    }
    if (m_next_link_isSet) {
        obj.insert(QString("nextLink"), ::OpenAPI::toJsonValue(m_next_link));
    }
    return obj;
}

QList<OAIJobResource> OAIJobResourceList::getValue() const {
    return m_value;
}
void OAIJobResourceList::setValue(const QList<OAIJobResource> &value) {
    m_value = value;
    m_value_isSet = true;
}

bool OAIJobResourceList::is_value_Set() const{
    return m_value_isSet;
}

bool OAIJobResourceList::is_value_Valid() const{
    return m_value_isValid;
}

QString OAIJobResourceList::getNextLink() const {
    return m_next_link;
}
void OAIJobResourceList::setNextLink(const QString &next_link) {
    m_next_link = next_link;
    m_next_link_isSet = true;
}

bool OAIJobResourceList::is_next_link_Set() const{
    return m_next_link_isSet;
}

bool OAIJobResourceList::is_next_link_Valid() const{
    return m_next_link_isValid;
}

bool OAIJobResourceList::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_value.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_next_link_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIJobResourceList::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
