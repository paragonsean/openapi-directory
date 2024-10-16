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

#include "OAIMusicTrackArtist.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIMusicTrackArtist::OAIMusicTrackArtist(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIMusicTrackArtist::OAIMusicTrackArtist() {
    this->initializeModel();
}

OAIMusicTrackArtist::~OAIMusicTrackArtist() {}

void OAIMusicTrackArtist::initializeModel() {

    m_gid_isSet = false;
    m_gid_isValid = false;

    m_image_pid_isSet = false;
    m_image_pid_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_role_isSet = false;
    m_role_isValid = false;

    m_sort_name_isSet = false;
    m_sort_name_isValid = false;
}

void OAIMusicTrackArtist::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIMusicTrackArtist::fromJsonObject(QJsonObject json) {

    m_gid_isValid = ::OpenAPI::fromJsonValue(m_gid, json[QString("gid")]);
    m_gid_isSet = !json[QString("gid")].isNull() && m_gid_isValid;

    m_image_pid_isValid = ::OpenAPI::fromJsonValue(m_image_pid, json[QString("imagePid")]);
    m_image_pid_isSet = !json[QString("imagePid")].isNull() && m_image_pid_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_role_isValid = ::OpenAPI::fromJsonValue(m_role, json[QString("role")]);
    m_role_isSet = !json[QString("role")].isNull() && m_role_isValid;

    m_sort_name_isValid = ::OpenAPI::fromJsonValue(m_sort_name, json[QString("sortName")]);
    m_sort_name_isSet = !json[QString("sortName")].isNull() && m_sort_name_isValid;
}

QString OAIMusicTrackArtist::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIMusicTrackArtist::asJsonObject() const {
    QJsonObject obj;
    if (m_gid_isSet) {
        obj.insert(QString("gid"), ::OpenAPI::toJsonValue(m_gid));
    }
    if (m_image_pid_isSet) {
        obj.insert(QString("imagePid"), ::OpenAPI::toJsonValue(m_image_pid));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_role_isSet) {
        obj.insert(QString("role"), ::OpenAPI::toJsonValue(m_role));
    }
    if (m_sort_name_isSet) {
        obj.insert(QString("sortName"), ::OpenAPI::toJsonValue(m_sort_name));
    }
    return obj;
}

QString OAIMusicTrackArtist::getGid() const {
    return m_gid;
}
void OAIMusicTrackArtist::setGid(const QString &gid) {
    m_gid = gid;
    m_gid_isSet = true;
}

bool OAIMusicTrackArtist::is_gid_Set() const{
    return m_gid_isSet;
}

bool OAIMusicTrackArtist::is_gid_Valid() const{
    return m_gid_isValid;
}

QString OAIMusicTrackArtist::getImagePid() const {
    return m_image_pid;
}
void OAIMusicTrackArtist::setImagePid(const QString &image_pid) {
    m_image_pid = image_pid;
    m_image_pid_isSet = true;
}

bool OAIMusicTrackArtist::is_image_pid_Set() const{
    return m_image_pid_isSet;
}

bool OAIMusicTrackArtist::is_image_pid_Valid() const{
    return m_image_pid_isValid;
}

QString OAIMusicTrackArtist::getName() const {
    return m_name;
}
void OAIMusicTrackArtist::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIMusicTrackArtist::is_name_Set() const{
    return m_name_isSet;
}

bool OAIMusicTrackArtist::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIMusicTrackArtist::getRole() const {
    return m_role;
}
void OAIMusicTrackArtist::setRole(const QString &role) {
    m_role = role;
    m_role_isSet = true;
}

bool OAIMusicTrackArtist::is_role_Set() const{
    return m_role_isSet;
}

bool OAIMusicTrackArtist::is_role_Valid() const{
    return m_role_isValid;
}

QString OAIMusicTrackArtist::getSortName() const {
    return m_sort_name;
}
void OAIMusicTrackArtist::setSortName(const QString &sort_name) {
    m_sort_name = sort_name;
    m_sort_name_isSet = true;
}

bool OAIMusicTrackArtist::is_sort_name_Set() const{
    return m_sort_name_isSet;
}

bool OAIMusicTrackArtist::is_sort_name_Valid() const{
    return m_sort_name_isValid;
}

bool OAIMusicTrackArtist::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_gid_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_image_pid_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_role_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sort_name_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIMusicTrackArtist::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_gid_isValid && m_image_pid_isValid && m_name_isValid && m_role_isValid && m_sort_name_isValid && true;
}

} // namespace OpenAPI
