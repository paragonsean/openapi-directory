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

#include "OAIShareAttributes.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIShareAttributes::OAIShareAttributes(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIShareAttributes::OAIShareAttributes() {
    this->initializeModel();
}

OAIShareAttributes::~OAIShareAttributes() {}

void OAIShareAttributes::initializeModel() {

    m_access_description_isSet = false;
    m_access_description_isValid = false;

    m_access_mode_isSet = false;
    m_access_mode_isValid = false;

    m_created_isSet = false;
    m_created_isValid = false;

    m_embed_isSet = false;
    m_embed_isValid = false;

    m_expiration_isSet = false;
    m_expiration_isValid = false;

    m_expired_isSet = false;
    m_expired_isValid = false;

    m_file_drop_create_folders_isSet = false;
    m_file_drop_create_folders_isValid = false;

    m_form_id_isSet = false;
    m_form_id_isValid = false;

    m_has_notification_isSet = false;
    m_has_notification_isValid = false;

    m_has_password_isSet = false;
    m_has_password_isValid = false;

    m_hash_isSet = false;
    m_hash_isValid = false;

    m_inherited_isSet = false;
    m_inherited_isValid = false;

    m_messages_isSet = false;
    m_messages_isValid = false;

    m_modified_isSet = false;
    m_modified_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_owner_hash_isSet = false;
    m_owner_hash_isValid = false;

    m_paths_isSet = false;
    m_paths_isValid = false;

    m_r_public_isSet = false;
    m_r_public_isValid = false;

    m_recipients_isSet = false;
    m_recipients_isValid = false;

    m_require_email_isSet = false;
    m_require_email_isValid = false;

    m_resent_isSet = false;
    m_resent_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_tracking_status_isSet = false;
    m_tracking_status_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIShareAttributes::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIShareAttributes::fromJsonObject(QJsonObject json) {

    m_access_description_isValid = ::OpenAPI::fromJsonValue(m_access_description, json[QString("accessDescription")]);
    m_access_description_isSet = !json[QString("accessDescription")].isNull() && m_access_description_isValid;

    m_access_mode_isValid = ::OpenAPI::fromJsonValue(m_access_mode, json[QString("accessMode")]);
    m_access_mode_isSet = !json[QString("accessMode")].isNull() && m_access_mode_isValid;

    m_created_isValid = ::OpenAPI::fromJsonValue(m_created, json[QString("created")]);
    m_created_isSet = !json[QString("created")].isNull() && m_created_isValid;

    m_embed_isValid = ::OpenAPI::fromJsonValue(m_embed, json[QString("embed")]);
    m_embed_isSet = !json[QString("embed")].isNull() && m_embed_isValid;

    m_expiration_isValid = ::OpenAPI::fromJsonValue(m_expiration, json[QString("expiration")]);
    m_expiration_isSet = !json[QString("expiration")].isNull() && m_expiration_isValid;

    m_expired_isValid = ::OpenAPI::fromJsonValue(m_expired, json[QString("expired")]);
    m_expired_isSet = !json[QString("expired")].isNull() && m_expired_isValid;

    m_file_drop_create_folders_isValid = ::OpenAPI::fromJsonValue(m_file_drop_create_folders, json[QString("fileDropCreateFolders")]);
    m_file_drop_create_folders_isSet = !json[QString("fileDropCreateFolders")].isNull() && m_file_drop_create_folders_isValid;

    m_form_id_isValid = ::OpenAPI::fromJsonValue(m_form_id, json[QString("formId")]);
    m_form_id_isSet = !json[QString("formId")].isNull() && m_form_id_isValid;

    m_has_notification_isValid = ::OpenAPI::fromJsonValue(m_has_notification, json[QString("hasNotification")]);
    m_has_notification_isSet = !json[QString("hasNotification")].isNull() && m_has_notification_isValid;

    m_has_password_isValid = ::OpenAPI::fromJsonValue(m_has_password, json[QString("hasPassword")]);
    m_has_password_isSet = !json[QString("hasPassword")].isNull() && m_has_password_isValid;

    m_hash_isValid = ::OpenAPI::fromJsonValue(m_hash, json[QString("hash")]);
    m_hash_isSet = !json[QString("hash")].isNull() && m_hash_isValid;

    m_inherited_isValid = ::OpenAPI::fromJsonValue(m_inherited, json[QString("inherited")]);
    m_inherited_isSet = !json[QString("inherited")].isNull() && m_inherited_isValid;

    m_messages_isValid = ::OpenAPI::fromJsonValue(m_messages, json[QString("messages")]);
    m_messages_isSet = !json[QString("messages")].isNull() && m_messages_isValid;

    m_modified_isValid = ::OpenAPI::fromJsonValue(m_modified, json[QString("modified")]);
    m_modified_isSet = !json[QString("modified")].isNull() && m_modified_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_owner_hash_isValid = ::OpenAPI::fromJsonValue(m_owner_hash, json[QString("ownerHash")]);
    m_owner_hash_isSet = !json[QString("ownerHash")].isNull() && m_owner_hash_isValid;

    m_paths_isValid = ::OpenAPI::fromJsonValue(m_paths, json[QString("paths")]);
    m_paths_isSet = !json[QString("paths")].isNull() && m_paths_isValid;

    m_r_public_isValid = ::OpenAPI::fromJsonValue(m_r_public, json[QString("public")]);
    m_r_public_isSet = !json[QString("public")].isNull() && m_r_public_isValid;

    m_recipients_isValid = ::OpenAPI::fromJsonValue(m_recipients, json[QString("recipients")]);
    m_recipients_isSet = !json[QString("recipients")].isNull() && m_recipients_isValid;

    m_require_email_isValid = ::OpenAPI::fromJsonValue(m_require_email, json[QString("requireEmail")]);
    m_require_email_isSet = !json[QString("requireEmail")].isNull() && m_require_email_isValid;

    m_resent_isValid = ::OpenAPI::fromJsonValue(m_resent, json[QString("resent")]);
    m_resent_isSet = !json[QString("resent")].isNull() && m_resent_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_tracking_status_isValid = ::OpenAPI::fromJsonValue(m_tracking_status, json[QString("trackingStatus")]);
    m_tracking_status_isSet = !json[QString("trackingStatus")].isNull() && m_tracking_status_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAIShareAttributes::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIShareAttributes::asJsonObject() const {
    QJsonObject obj;
    if (m_access_description_isSet) {
        obj.insert(QString("accessDescription"), ::OpenAPI::toJsonValue(m_access_description));
    }
    if (m_access_mode.isSet()) {
        obj.insert(QString("accessMode"), ::OpenAPI::toJsonValue(m_access_mode));
    }
    if (m_created_isSet) {
        obj.insert(QString("created"), ::OpenAPI::toJsonValue(m_created));
    }
    if (m_embed_isSet) {
        obj.insert(QString("embed"), ::OpenAPI::toJsonValue(m_embed));
    }
    if (m_expiration_isSet) {
        obj.insert(QString("expiration"), ::OpenAPI::toJsonValue(m_expiration));
    }
    if (m_expired_isSet) {
        obj.insert(QString("expired"), ::OpenAPI::toJsonValue(m_expired));
    }
    if (m_file_drop_create_folders_isSet) {
        obj.insert(QString("fileDropCreateFolders"), ::OpenAPI::toJsonValue(m_file_drop_create_folders));
    }
    if (m_form_id_isSet) {
        obj.insert(QString("formId"), ::OpenAPI::toJsonValue(m_form_id));
    }
    if (m_has_notification_isSet) {
        obj.insert(QString("hasNotification"), ::OpenAPI::toJsonValue(m_has_notification));
    }
    if (m_has_password_isSet) {
        obj.insert(QString("hasPassword"), ::OpenAPI::toJsonValue(m_has_password));
    }
    if (m_hash_isSet) {
        obj.insert(QString("hash"), ::OpenAPI::toJsonValue(m_hash));
    }
    if (m_inherited_isSet) {
        obj.insert(QString("inherited"), ::OpenAPI::toJsonValue(m_inherited));
    }
    if (m_messages.size() > 0) {
        obj.insert(QString("messages"), ::OpenAPI::toJsonValue(m_messages));
    }
    if (m_modified_isSet) {
        obj.insert(QString("modified"), ::OpenAPI::toJsonValue(m_modified));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_owner_hash_isSet) {
        obj.insert(QString("ownerHash"), ::OpenAPI::toJsonValue(m_owner_hash));
    }
    if (m_paths.size() > 0) {
        obj.insert(QString("paths"), ::OpenAPI::toJsonValue(m_paths));
    }
    if (m_r_public_isSet) {
        obj.insert(QString("public"), ::OpenAPI::toJsonValue(m_r_public));
    }
    if (m_recipients.size() > 0) {
        obj.insert(QString("recipients"), ::OpenAPI::toJsonValue(m_recipients));
    }
    if (m_require_email_isSet) {
        obj.insert(QString("requireEmail"), ::OpenAPI::toJsonValue(m_require_email));
    }
    if (m_resent_isSet) {
        obj.insert(QString("resent"), ::OpenAPI::toJsonValue(m_resent));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_tracking_status_isSet) {
        obj.insert(QString("trackingStatus"), ::OpenAPI::toJsonValue(m_tracking_status));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

QString OAIShareAttributes::getAccessDescription() const {
    return m_access_description;
}
void OAIShareAttributes::setAccessDescription(const QString &access_description) {
    m_access_description = access_description;
    m_access_description_isSet = true;
}

bool OAIShareAttributes::is_access_description_Set() const{
    return m_access_description_isSet;
}

bool OAIShareAttributes::is_access_description_Valid() const{
    return m_access_description_isValid;
}

OAIAccessMode OAIShareAttributes::getAccessMode() const {
    return m_access_mode;
}
void OAIShareAttributes::setAccessMode(const OAIAccessMode &access_mode) {
    m_access_mode = access_mode;
    m_access_mode_isSet = true;
}

bool OAIShareAttributes::is_access_mode_Set() const{
    return m_access_mode_isSet;
}

bool OAIShareAttributes::is_access_mode_Valid() const{
    return m_access_mode_isValid;
}

QDateTime OAIShareAttributes::getCreated() const {
    return m_created;
}
void OAIShareAttributes::setCreated(const QDateTime &created) {
    m_created = created;
    m_created_isSet = true;
}

bool OAIShareAttributes::is_created_Set() const{
    return m_created_isSet;
}

bool OAIShareAttributes::is_created_Valid() const{
    return m_created_isValid;
}

bool OAIShareAttributes::isEmbed() const {
    return m_embed;
}
void OAIShareAttributes::setEmbed(const bool &embed) {
    m_embed = embed;
    m_embed_isSet = true;
}

bool OAIShareAttributes::is_embed_Set() const{
    return m_embed_isSet;
}

bool OAIShareAttributes::is_embed_Valid() const{
    return m_embed_isValid;
}

QString OAIShareAttributes::getExpiration() const {
    return m_expiration;
}
void OAIShareAttributes::setExpiration(const QString &expiration) {
    m_expiration = expiration;
    m_expiration_isSet = true;
}

bool OAIShareAttributes::is_expiration_Set() const{
    return m_expiration_isSet;
}

bool OAIShareAttributes::is_expiration_Valid() const{
    return m_expiration_isValid;
}

bool OAIShareAttributes::isExpired() const {
    return m_expired;
}
void OAIShareAttributes::setExpired(const bool &expired) {
    m_expired = expired;
    m_expired_isSet = true;
}

bool OAIShareAttributes::is_expired_Set() const{
    return m_expired_isSet;
}

bool OAIShareAttributes::is_expired_Valid() const{
    return m_expired_isValid;
}

bool OAIShareAttributes::isFileDropCreateFolders() const {
    return m_file_drop_create_folders;
}
void OAIShareAttributes::setFileDropCreateFolders(const bool &file_drop_create_folders) {
    m_file_drop_create_folders = file_drop_create_folders;
    m_file_drop_create_folders_isSet = true;
}

bool OAIShareAttributes::is_file_drop_create_folders_Set() const{
    return m_file_drop_create_folders_isSet;
}

bool OAIShareAttributes::is_file_drop_create_folders_Valid() const{
    return m_file_drop_create_folders_isValid;
}

qint32 OAIShareAttributes::getFormId() const {
    return m_form_id;
}
void OAIShareAttributes::setFormId(const qint32 &form_id) {
    m_form_id = form_id;
    m_form_id_isSet = true;
}

bool OAIShareAttributes::is_form_id_Set() const{
    return m_form_id_isSet;
}

bool OAIShareAttributes::is_form_id_Valid() const{
    return m_form_id_isValid;
}

bool OAIShareAttributes::isHasNotification() const {
    return m_has_notification;
}
void OAIShareAttributes::setHasNotification(const bool &has_notification) {
    m_has_notification = has_notification;
    m_has_notification_isSet = true;
}

bool OAIShareAttributes::is_has_notification_Set() const{
    return m_has_notification_isSet;
}

bool OAIShareAttributes::is_has_notification_Valid() const{
    return m_has_notification_isValid;
}

bool OAIShareAttributes::isHasPassword() const {
    return m_has_password;
}
void OAIShareAttributes::setHasPassword(const bool &has_password) {
    m_has_password = has_password;
    m_has_password_isSet = true;
}

bool OAIShareAttributes::is_has_password_Set() const{
    return m_has_password_isSet;
}

bool OAIShareAttributes::is_has_password_Valid() const{
    return m_has_password_isValid;
}

QString OAIShareAttributes::getHash() const {
    return m_hash;
}
void OAIShareAttributes::setHash(const QString &hash) {
    m_hash = hash;
    m_hash_isSet = true;
}

bool OAIShareAttributes::is_hash_Set() const{
    return m_hash_isSet;
}

bool OAIShareAttributes::is_hash_Valid() const{
    return m_hash_isValid;
}

bool OAIShareAttributes::isInherited() const {
    return m_inherited;
}
void OAIShareAttributes::setInherited(const bool &inherited) {
    m_inherited = inherited;
    m_inherited_isSet = true;
}

bool OAIShareAttributes::is_inherited_Set() const{
    return m_inherited_isSet;
}

bool OAIShareAttributes::is_inherited_Valid() const{
    return m_inherited_isValid;
}

QList<OAIShareMessage> OAIShareAttributes::getMessages() const {
    return m_messages;
}
void OAIShareAttributes::setMessages(const QList<OAIShareMessage> &messages) {
    m_messages = messages;
    m_messages_isSet = true;
}

bool OAIShareAttributes::is_messages_Set() const{
    return m_messages_isSet;
}

bool OAIShareAttributes::is_messages_Valid() const{
    return m_messages_isValid;
}

QDateTime OAIShareAttributes::getModified() const {
    return m_modified;
}
void OAIShareAttributes::setModified(const QDateTime &modified) {
    m_modified = modified;
    m_modified_isSet = true;
}

bool OAIShareAttributes::is_modified_Set() const{
    return m_modified_isSet;
}

bool OAIShareAttributes::is_modified_Valid() const{
    return m_modified_isValid;
}

QString OAIShareAttributes::getName() const {
    return m_name;
}
void OAIShareAttributes::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIShareAttributes::is_name_Set() const{
    return m_name_isSet;
}

bool OAIShareAttributes::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIShareAttributes::getOwnerHash() const {
    return m_owner_hash;
}
void OAIShareAttributes::setOwnerHash(const QString &owner_hash) {
    m_owner_hash = owner_hash;
    m_owner_hash_isSet = true;
}

bool OAIShareAttributes::is_owner_hash_Set() const{
    return m_owner_hash_isSet;
}

bool OAIShareAttributes::is_owner_hash_Valid() const{
    return m_owner_hash_isValid;
}

QList<QString> OAIShareAttributes::getPaths() const {
    return m_paths;
}
void OAIShareAttributes::setPaths(const QList<QString> &paths) {
    m_paths = paths;
    m_paths_isSet = true;
}

bool OAIShareAttributes::is_paths_Set() const{
    return m_paths_isSet;
}

bool OAIShareAttributes::is_paths_Valid() const{
    return m_paths_isValid;
}

bool OAIShareAttributes::isRPublic() const {
    return m_r_public;
}
void OAIShareAttributes::setRPublic(const bool &r_public) {
    m_r_public = r_public;
    m_r_public_isSet = true;
}

bool OAIShareAttributes::is_r_public_Set() const{
    return m_r_public_isSet;
}

bool OAIShareAttributes::is_r_public_Valid() const{
    return m_r_public_isValid;
}

QList<OAIShareRecipient> OAIShareAttributes::getRecipients() const {
    return m_recipients;
}
void OAIShareAttributes::setRecipients(const QList<OAIShareRecipient> &recipients) {
    m_recipients = recipients;
    m_recipients_isSet = true;
}

bool OAIShareAttributes::is_recipients_Set() const{
    return m_recipients_isSet;
}

bool OAIShareAttributes::is_recipients_Valid() const{
    return m_recipients_isValid;
}

bool OAIShareAttributes::isRequireEmail() const {
    return m_require_email;
}
void OAIShareAttributes::setRequireEmail(const bool &require_email) {
    m_require_email = require_email;
    m_require_email_isSet = true;
}

bool OAIShareAttributes::is_require_email_Set() const{
    return m_require_email_isSet;
}

bool OAIShareAttributes::is_require_email_Valid() const{
    return m_require_email_isValid;
}

QDateTime OAIShareAttributes::getResent() const {
    return m_resent;
}
void OAIShareAttributes::setResent(const QDateTime &resent) {
    m_resent = resent;
    m_resent_isSet = true;
}

bool OAIShareAttributes::is_resent_Set() const{
    return m_resent_isSet;
}

bool OAIShareAttributes::is_resent_Valid() const{
    return m_resent_isValid;
}

qint32 OAIShareAttributes::getStatus() const {
    return m_status;
}
void OAIShareAttributes::setStatus(const qint32 &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIShareAttributes::is_status_Set() const{
    return m_status_isSet;
}

bool OAIShareAttributes::is_status_Valid() const{
    return m_status_isValid;
}

QString OAIShareAttributes::getTrackingStatus() const {
    return m_tracking_status;
}
void OAIShareAttributes::setTrackingStatus(const QString &tracking_status) {
    m_tracking_status = tracking_status;
    m_tracking_status_isSet = true;
}

bool OAIShareAttributes::is_tracking_status_Set() const{
    return m_tracking_status_isSet;
}

bool OAIShareAttributes::is_tracking_status_Valid() const{
    return m_tracking_status_isValid;
}

QString OAIShareAttributes::getType() const {
    return m_type;
}
void OAIShareAttributes::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIShareAttributes::is_type_Set() const{
    return m_type_isSet;
}

bool OAIShareAttributes::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIShareAttributes::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_access_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_access_mode.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_embed_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_expiration_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_expired_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_file_drop_create_folders_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_form_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_has_notification_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_has_password_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_hash_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_inherited_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_messages.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_modified_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_owner_hash_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_paths.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_r_public_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_recipients.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_require_email_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_resent_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tracking_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIShareAttributes::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
