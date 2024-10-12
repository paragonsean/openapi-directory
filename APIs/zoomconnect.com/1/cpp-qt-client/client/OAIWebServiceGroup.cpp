/**
 * www.zoomconnect.com
 * The world's greatest SMS API
 *
 * The version of the OpenAPI document: 1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIWebServiceGroup.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIWebServiceGroup::OAIWebServiceGroup(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIWebServiceGroup::OAIWebServiceGroup() {
    this->initializeModel();
}

OAIWebServiceGroup::~OAIWebServiceGroup() {}

void OAIWebServiceGroup::initializeModel() {

    m_group_id_isSet = false;
    m_group_id_isValid = false;

    m_links_isSet = false;
    m_links_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;
}

void OAIWebServiceGroup::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIWebServiceGroup::fromJsonObject(QJsonObject json) {

    m_group_id_isValid = ::OpenAPI::fromJsonValue(m_group_id, json[QString("groupId")]);
    m_group_id_isSet = !json[QString("groupId")].isNull() && m_group_id_isValid;

    m_links_isValid = ::OpenAPI::fromJsonValue(m_links, json[QString("links")]);
    m_links_isSet = !json[QString("links")].isNull() && m_links_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;
}

QString OAIWebServiceGroup::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIWebServiceGroup::asJsonObject() const {
    QJsonObject obj;
    if (m_group_id_isSet) {
        obj.insert(QString("groupId"), ::OpenAPI::toJsonValue(m_group_id));
    }
    if (m_links.size() > 0) {
        obj.insert(QString("links"), ::OpenAPI::toJsonValue(m_links));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    return obj;
}

QString OAIWebServiceGroup::getGroupId() const {
    return m_group_id;
}
void OAIWebServiceGroup::setGroupId(const QString &group_id) {
    m_group_id = group_id;
    m_group_id_isSet = true;
}

bool OAIWebServiceGroup::is_group_id_Set() const{
    return m_group_id_isSet;
}

bool OAIWebServiceGroup::is_group_id_Valid() const{
    return m_group_id_isValid;
}

QList<OAILink> OAIWebServiceGroup::getLinks() const {
    return m_links;
}
void OAIWebServiceGroup::setLinks(const QList<OAILink> &links) {
    m_links = links;
    m_links_isSet = true;
}

bool OAIWebServiceGroup::is_links_Set() const{
    return m_links_isSet;
}

bool OAIWebServiceGroup::is_links_Valid() const{
    return m_links_isValid;
}

QString OAIWebServiceGroup::getName() const {
    return m_name;
}
void OAIWebServiceGroup::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIWebServiceGroup::is_name_Set() const{
    return m_name_isSet;
}

bool OAIWebServiceGroup::is_name_Valid() const{
    return m_name_isValid;
}

bool OAIWebServiceGroup::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_group_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_links.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIWebServiceGroup::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
