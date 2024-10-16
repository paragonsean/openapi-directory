/**
 * ExaVault
 * ExaVaults API allows you to incorporate ExaVaults suite of file transfer and user management tools into your own application.\\nExaVault supports both POST (recommended when requesting large data sets) and GET operations, and requires an API key in order to use.
 *
 * The version of the OpenAPI document: 2.0
 * Contact: support@exavault.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIResource_relationships.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIResource_relationships::OAIResource_relationships(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIResource_relationships::OAIResource_relationships() {
    this->initializeModel();
}

OAIResource_relationships::~OAIResource_relationships() {}

void OAIResource_relationships::initializeModel() {

    m_direct_file_isSet = false;
    m_direct_file_isValid = false;

    m_notifications_isSet = false;
    m_notifications_isValid = false;

    m_parent_resource_isSet = false;
    m_parent_resource_isValid = false;

    m_share_isSet = false;
    m_share_isValid = false;
}

void OAIResource_relationships::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIResource_relationships::fromJsonObject(QJsonObject json) {

    m_direct_file_isValid = ::OpenAPI::fromJsonValue(m_direct_file, json[QString("directFile")]);
    m_direct_file_isSet = !json[QString("directFile")].isNull() && m_direct_file_isValid;

    m_notifications_isValid = ::OpenAPI::fromJsonValue(m_notifications, json[QString("notifications")]);
    m_notifications_isSet = !json[QString("notifications")].isNull() && m_notifications_isValid;

    m_parent_resource_isValid = ::OpenAPI::fromJsonValue(m_parent_resource, json[QString("parentResource")]);
    m_parent_resource_isSet = !json[QString("parentResource")].isNull() && m_parent_resource_isValid;

    m_share_isValid = ::OpenAPI::fromJsonValue(m_share, json[QString("share")]);
    m_share_isSet = !json[QString("share")].isNull() && m_share_isValid;
}

QString OAIResource_relationships::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIResource_relationships::asJsonObject() const {
    QJsonObject obj;
    if (m_direct_file.isSet()) {
        obj.insert(QString("directFile"), ::OpenAPI::toJsonValue(m_direct_file));
    }
    if (m_notifications.size() > 0) {
        obj.insert(QString("notifications"), ::OpenAPI::toJsonValue(m_notifications));
    }
    if (m_parent_resource.isSet()) {
        obj.insert(QString("parentResource"), ::OpenAPI::toJsonValue(m_parent_resource));
    }
    if (m_share.isSet()) {
        obj.insert(QString("share"), ::OpenAPI::toJsonValue(m_share));
    }
    return obj;
}

OAIResource_relationships_directFile OAIResource_relationships::getDirectFile() const {
    return m_direct_file;
}
void OAIResource_relationships::setDirectFile(const OAIResource_relationships_directFile &direct_file) {
    m_direct_file = direct_file;
    m_direct_file_isSet = true;
}

bool OAIResource_relationships::is_direct_file_Set() const{
    return m_direct_file_isSet;
}

bool OAIResource_relationships::is_direct_file_Valid() const{
    return m_direct_file_isValid;
}

QList<OAIResource_relationships_notifications_inner> OAIResource_relationships::getNotifications() const {
    return m_notifications;
}
void OAIResource_relationships::setNotifications(const QList<OAIResource_relationships_notifications_inner> &notifications) {
    m_notifications = notifications;
    m_notifications_isSet = true;
}

bool OAIResource_relationships::is_notifications_Set() const{
    return m_notifications_isSet;
}

bool OAIResource_relationships::is_notifications_Valid() const{
    return m_notifications_isValid;
}

OAIResource_relationships_parentResource OAIResource_relationships::getParentResource() const {
    return m_parent_resource;
}
void OAIResource_relationships::setParentResource(const OAIResource_relationships_parentResource &parent_resource) {
    m_parent_resource = parent_resource;
    m_parent_resource_isSet = true;
}

bool OAIResource_relationships::is_parent_resource_Set() const{
    return m_parent_resource_isSet;
}

bool OAIResource_relationships::is_parent_resource_Valid() const{
    return m_parent_resource_isValid;
}

OAIResource_relationships_share OAIResource_relationships::getShare() const {
    return m_share;
}
void OAIResource_relationships::setShare(const OAIResource_relationships_share &share) {
    m_share = share;
    m_share_isSet = true;
}

bool OAIResource_relationships::is_share_Set() const{
    return m_share_isSet;
}

bool OAIResource_relationships::is_share_Valid() const{
    return m_share_isValid;
}

bool OAIResource_relationships::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_direct_file.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_notifications.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_parent_resource.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_share.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIResource_relationships::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
