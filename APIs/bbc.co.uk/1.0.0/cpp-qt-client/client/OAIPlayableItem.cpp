/**
 * Radio & Music Services
 * We encapsulate Radio & Music business logic for iPlayer Radio and BBC Music products on all platforms. We add value by reliably providing the right blend of metadata needed by clients.
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIPlayableItem.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPlayableItem::OAIPlayableItem(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPlayableItem::OAIPlayableItem() {
    this->initializeModel();
}

OAIPlayableItem::~OAIPlayableItem() {}

void OAIPlayableItem::initializeModel() {

    m_description_isSet = false;
    m_description_isValid = false;

    m_image_url_isSet = false;
    m_image_url_isValid = false;

    m_pid_isSet = false;
    m_pid_isValid = false;

    m_title_isSet = false;
    m_title_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;

    m_version_pid_isSet = false;
    m_version_pid_isValid = false;
}

void OAIPlayableItem::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPlayableItem::fromJsonObject(QJsonObject json) {

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_image_url_isValid = ::OpenAPI::fromJsonValue(m_image_url, json[QString("image_url")]);
    m_image_url_isSet = !json[QString("image_url")].isNull() && m_image_url_isValid;

    m_pid_isValid = ::OpenAPI::fromJsonValue(m_pid, json[QString("pid")]);
    m_pid_isSet = !json[QString("pid")].isNull() && m_pid_isValid;

    m_title_isValid = ::OpenAPI::fromJsonValue(m_title, json[QString("title")]);
    m_title_isSet = !json[QString("title")].isNull() && m_title_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;

    m_version_pid_isValid = ::OpenAPI::fromJsonValue(m_version_pid, json[QString("version_pid")]);
    m_version_pid_isSet = !json[QString("version_pid")].isNull() && m_version_pid_isValid;
}

QString OAIPlayableItem::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPlayableItem::asJsonObject() const {
    QJsonObject obj;
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_image_url_isSet) {
        obj.insert(QString("image_url"), ::OpenAPI::toJsonValue(m_image_url));
    }
    if (m_pid_isSet) {
        obj.insert(QString("pid"), ::OpenAPI::toJsonValue(m_pid));
    }
    if (m_title_isSet) {
        obj.insert(QString("title"), ::OpenAPI::toJsonValue(m_title));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    if (m_version_pid_isSet) {
        obj.insert(QString("version_pid"), ::OpenAPI::toJsonValue(m_version_pid));
    }
    return obj;
}

QString OAIPlayableItem::getDescription() const {
    return m_description;
}
void OAIPlayableItem::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIPlayableItem::is_description_Set() const{
    return m_description_isSet;
}

bool OAIPlayableItem::is_description_Valid() const{
    return m_description_isValid;
}

QString OAIPlayableItem::getImageUrl() const {
    return m_image_url;
}
void OAIPlayableItem::setImageUrl(const QString &image_url) {
    m_image_url = image_url;
    m_image_url_isSet = true;
}

bool OAIPlayableItem::is_image_url_Set() const{
    return m_image_url_isSet;
}

bool OAIPlayableItem::is_image_url_Valid() const{
    return m_image_url_isValid;
}

QString OAIPlayableItem::getPid() const {
    return m_pid;
}
void OAIPlayableItem::setPid(const QString &pid) {
    m_pid = pid;
    m_pid_isSet = true;
}

bool OAIPlayableItem::is_pid_Set() const{
    return m_pid_isSet;
}

bool OAIPlayableItem::is_pid_Valid() const{
    return m_pid_isValid;
}

QString OAIPlayableItem::getTitle() const {
    return m_title;
}
void OAIPlayableItem::setTitle(const QString &title) {
    m_title = title;
    m_title_isSet = true;
}

bool OAIPlayableItem::is_title_Set() const{
    return m_title_isSet;
}

bool OAIPlayableItem::is_title_Valid() const{
    return m_title_isValid;
}

QString OAIPlayableItem::getType() const {
    return m_type;
}
void OAIPlayableItem::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIPlayableItem::is_type_Set() const{
    return m_type_isSet;
}

bool OAIPlayableItem::is_type_Valid() const{
    return m_type_isValid;
}

QString OAIPlayableItem::getVersionPid() const {
    return m_version_pid;
}
void OAIPlayableItem::setVersionPid(const QString &version_pid) {
    m_version_pid = version_pid;
    m_version_pid_isSet = true;
}

bool OAIPlayableItem::is_version_pid_Set() const{
    return m_version_pid_isSet;
}

bool OAIPlayableItem::is_version_pid_Valid() const{
    return m_version_pid_isValid;
}

bool OAIPlayableItem::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_image_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_pid_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_title_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_version_pid_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPlayableItem::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
