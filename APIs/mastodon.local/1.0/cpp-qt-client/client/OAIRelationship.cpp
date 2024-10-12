/**
 * Mastodon API Specification (https://github.com/mastodon/mastodon)
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 * Contact: sardo@hey.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIRelationship.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIRelationship::OAIRelationship(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIRelationship::OAIRelationship() {
    this->initializeModel();
}

OAIRelationship::~OAIRelationship() {}

void OAIRelationship::initializeModel() {

    m_blocked_by_isSet = false;
    m_blocked_by_isValid = false;

    m_blocking_isSet = false;
    m_blocking_isValid = false;

    m_domain_blocking_isSet = false;
    m_domain_blocking_isValid = false;

    m_endorsed_isSet = false;
    m_endorsed_isValid = false;

    m_followed_by_isSet = false;
    m_followed_by_isValid = false;

    m_following_isSet = false;
    m_following_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_muting_isSet = false;
    m_muting_isValid = false;

    m_muting_notifications_isSet = false;
    m_muting_notifications_isValid = false;

    m_note_isSet = false;
    m_note_isValid = false;

    m_notifying_isSet = false;
    m_notifying_isValid = false;

    m_requested_isSet = false;
    m_requested_isValid = false;

    m_showing_reblogs_isSet = false;
    m_showing_reblogs_isValid = false;
}

void OAIRelationship::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIRelationship::fromJsonObject(QJsonObject json) {

    m_blocked_by_isValid = ::OpenAPI::fromJsonValue(m_blocked_by, json[QString("blocked_by")]);
    m_blocked_by_isSet = !json[QString("blocked_by")].isNull() && m_blocked_by_isValid;

    m_blocking_isValid = ::OpenAPI::fromJsonValue(m_blocking, json[QString("blocking")]);
    m_blocking_isSet = !json[QString("blocking")].isNull() && m_blocking_isValid;

    m_domain_blocking_isValid = ::OpenAPI::fromJsonValue(m_domain_blocking, json[QString("domain_blocking")]);
    m_domain_blocking_isSet = !json[QString("domain_blocking")].isNull() && m_domain_blocking_isValid;

    m_endorsed_isValid = ::OpenAPI::fromJsonValue(m_endorsed, json[QString("endorsed")]);
    m_endorsed_isSet = !json[QString("endorsed")].isNull() && m_endorsed_isValid;

    m_followed_by_isValid = ::OpenAPI::fromJsonValue(m_followed_by, json[QString("followed_by")]);
    m_followed_by_isSet = !json[QString("followed_by")].isNull() && m_followed_by_isValid;

    m_following_isValid = ::OpenAPI::fromJsonValue(m_following, json[QString("following")]);
    m_following_isSet = !json[QString("following")].isNull() && m_following_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_muting_isValid = ::OpenAPI::fromJsonValue(m_muting, json[QString("muting")]);
    m_muting_isSet = !json[QString("muting")].isNull() && m_muting_isValid;

    m_muting_notifications_isValid = ::OpenAPI::fromJsonValue(m_muting_notifications, json[QString("muting_notifications")]);
    m_muting_notifications_isSet = !json[QString("muting_notifications")].isNull() && m_muting_notifications_isValid;

    m_note_isValid = ::OpenAPI::fromJsonValue(m_note, json[QString("note")]);
    m_note_isSet = !json[QString("note")].isNull() && m_note_isValid;

    m_notifying_isValid = ::OpenAPI::fromJsonValue(m_notifying, json[QString("notifying")]);
    m_notifying_isSet = !json[QString("notifying")].isNull() && m_notifying_isValid;

    m_requested_isValid = ::OpenAPI::fromJsonValue(m_requested, json[QString("requested")]);
    m_requested_isSet = !json[QString("requested")].isNull() && m_requested_isValid;

    m_showing_reblogs_isValid = ::OpenAPI::fromJsonValue(m_showing_reblogs, json[QString("showing_reblogs")]);
    m_showing_reblogs_isSet = !json[QString("showing_reblogs")].isNull() && m_showing_reblogs_isValid;
}

QString OAIRelationship::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIRelationship::asJsonObject() const {
    QJsonObject obj;
    if (m_blocked_by_isSet) {
        obj.insert(QString("blocked_by"), ::OpenAPI::toJsonValue(m_blocked_by));
    }
    if (m_blocking_isSet) {
        obj.insert(QString("blocking"), ::OpenAPI::toJsonValue(m_blocking));
    }
    if (m_domain_blocking_isSet) {
        obj.insert(QString("domain_blocking"), ::OpenAPI::toJsonValue(m_domain_blocking));
    }
    if (m_endorsed_isSet) {
        obj.insert(QString("endorsed"), ::OpenAPI::toJsonValue(m_endorsed));
    }
    if (m_followed_by_isSet) {
        obj.insert(QString("followed_by"), ::OpenAPI::toJsonValue(m_followed_by));
    }
    if (m_following_isSet) {
        obj.insert(QString("following"), ::OpenAPI::toJsonValue(m_following));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_muting_isSet) {
        obj.insert(QString("muting"), ::OpenAPI::toJsonValue(m_muting));
    }
    if (m_muting_notifications_isSet) {
        obj.insert(QString("muting_notifications"), ::OpenAPI::toJsonValue(m_muting_notifications));
    }
    if (m_note_isSet) {
        obj.insert(QString("note"), ::OpenAPI::toJsonValue(m_note));
    }
    if (m_notifying_isSet) {
        obj.insert(QString("notifying"), ::OpenAPI::toJsonValue(m_notifying));
    }
    if (m_requested_isSet) {
        obj.insert(QString("requested"), ::OpenAPI::toJsonValue(m_requested));
    }
    if (m_showing_reblogs_isSet) {
        obj.insert(QString("showing_reblogs"), ::OpenAPI::toJsonValue(m_showing_reblogs));
    }
    return obj;
}

bool OAIRelationship::isBlockedBy() const {
    return m_blocked_by;
}
void OAIRelationship::setBlockedBy(const bool &blocked_by) {
    m_blocked_by = blocked_by;
    m_blocked_by_isSet = true;
}

bool OAIRelationship::is_blocked_by_Set() const{
    return m_blocked_by_isSet;
}

bool OAIRelationship::is_blocked_by_Valid() const{
    return m_blocked_by_isValid;
}

bool OAIRelationship::isBlocking() const {
    return m_blocking;
}
void OAIRelationship::setBlocking(const bool &blocking) {
    m_blocking = blocking;
    m_blocking_isSet = true;
}

bool OAIRelationship::is_blocking_Set() const{
    return m_blocking_isSet;
}

bool OAIRelationship::is_blocking_Valid() const{
    return m_blocking_isValid;
}

bool OAIRelationship::isDomainBlocking() const {
    return m_domain_blocking;
}
void OAIRelationship::setDomainBlocking(const bool &domain_blocking) {
    m_domain_blocking = domain_blocking;
    m_domain_blocking_isSet = true;
}

bool OAIRelationship::is_domain_blocking_Set() const{
    return m_domain_blocking_isSet;
}

bool OAIRelationship::is_domain_blocking_Valid() const{
    return m_domain_blocking_isValid;
}

bool OAIRelationship::isEndorsed() const {
    return m_endorsed;
}
void OAIRelationship::setEndorsed(const bool &endorsed) {
    m_endorsed = endorsed;
    m_endorsed_isSet = true;
}

bool OAIRelationship::is_endorsed_Set() const{
    return m_endorsed_isSet;
}

bool OAIRelationship::is_endorsed_Valid() const{
    return m_endorsed_isValid;
}

bool OAIRelationship::isFollowedBy() const {
    return m_followed_by;
}
void OAIRelationship::setFollowedBy(const bool &followed_by) {
    m_followed_by = followed_by;
    m_followed_by_isSet = true;
}

bool OAIRelationship::is_followed_by_Set() const{
    return m_followed_by_isSet;
}

bool OAIRelationship::is_followed_by_Valid() const{
    return m_followed_by_isValid;
}

bool OAIRelationship::isFollowing() const {
    return m_following;
}
void OAIRelationship::setFollowing(const bool &following) {
    m_following = following;
    m_following_isSet = true;
}

bool OAIRelationship::is_following_Set() const{
    return m_following_isSet;
}

bool OAIRelationship::is_following_Valid() const{
    return m_following_isValid;
}

QString OAIRelationship::getId() const {
    return m_id;
}
void OAIRelationship::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIRelationship::is_id_Set() const{
    return m_id_isSet;
}

bool OAIRelationship::is_id_Valid() const{
    return m_id_isValid;
}

bool OAIRelationship::isMuting() const {
    return m_muting;
}
void OAIRelationship::setMuting(const bool &muting) {
    m_muting = muting;
    m_muting_isSet = true;
}

bool OAIRelationship::is_muting_Set() const{
    return m_muting_isSet;
}

bool OAIRelationship::is_muting_Valid() const{
    return m_muting_isValid;
}

bool OAIRelationship::isMutingNotifications() const {
    return m_muting_notifications;
}
void OAIRelationship::setMutingNotifications(const bool &muting_notifications) {
    m_muting_notifications = muting_notifications;
    m_muting_notifications_isSet = true;
}

bool OAIRelationship::is_muting_notifications_Set() const{
    return m_muting_notifications_isSet;
}

bool OAIRelationship::is_muting_notifications_Valid() const{
    return m_muting_notifications_isValid;
}

QString OAIRelationship::getNote() const {
    return m_note;
}
void OAIRelationship::setNote(const QString &note) {
    m_note = note;
    m_note_isSet = true;
}

bool OAIRelationship::is_note_Set() const{
    return m_note_isSet;
}

bool OAIRelationship::is_note_Valid() const{
    return m_note_isValid;
}

bool OAIRelationship::isNotifying() const {
    return m_notifying;
}
void OAIRelationship::setNotifying(const bool &notifying) {
    m_notifying = notifying;
    m_notifying_isSet = true;
}

bool OAIRelationship::is_notifying_Set() const{
    return m_notifying_isSet;
}

bool OAIRelationship::is_notifying_Valid() const{
    return m_notifying_isValid;
}

bool OAIRelationship::isRequested() const {
    return m_requested;
}
void OAIRelationship::setRequested(const bool &requested) {
    m_requested = requested;
    m_requested_isSet = true;
}

bool OAIRelationship::is_requested_Set() const{
    return m_requested_isSet;
}

bool OAIRelationship::is_requested_Valid() const{
    return m_requested_isValid;
}

bool OAIRelationship::isShowingReblogs() const {
    return m_showing_reblogs;
}
void OAIRelationship::setShowingReblogs(const bool &showing_reblogs) {
    m_showing_reblogs = showing_reblogs;
    m_showing_reblogs_isSet = true;
}

bool OAIRelationship::is_showing_reblogs_Set() const{
    return m_showing_reblogs_isSet;
}

bool OAIRelationship::is_showing_reblogs_Valid() const{
    return m_showing_reblogs_isValid;
}

bool OAIRelationship::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_blocked_by_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_blocking_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_domain_blocking_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_endorsed_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_followed_by_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_following_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_muting_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_muting_notifications_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_note_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_notifying_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_requested_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_showing_reblogs_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIRelationship::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_blocked_by_isValid && m_blocking_isValid && m_domain_blocking_isValid && m_endorsed_isValid && m_followed_by_isValid && m_following_isValid && m_id_isValid && m_muting_isValid && m_muting_notifications_isValid && m_note_isValid && m_notifying_isValid && m_requested_isValid && m_showing_reblogs_isValid && true;
}

} // namespace OpenAPI
