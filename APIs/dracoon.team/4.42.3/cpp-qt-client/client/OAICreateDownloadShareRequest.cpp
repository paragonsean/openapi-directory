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

#include "OAICreateDownloadShareRequest.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICreateDownloadShareRequest::OAICreateDownloadShareRequest(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICreateDownloadShareRequest::OAICreateDownloadShareRequest() {
    this->initializeModel();
}

OAICreateDownloadShareRequest::~OAICreateDownloadShareRequest() {}

void OAICreateDownloadShareRequest::initializeModel() {

    m_creator_language_isSet = false;
    m_creator_language_isValid = false;

    m_expiration_isSet = false;
    m_expiration_isValid = false;

    m_file_key_isSet = false;
    m_file_key_isValid = false;

    m_internal_notes_isSet = false;
    m_internal_notes_isValid = false;

    m_key_pair_isSet = false;
    m_key_pair_isValid = false;

    m_mail_body_isSet = false;
    m_mail_body_isValid = false;

    m_mail_recipients_isSet = false;
    m_mail_recipients_isValid = false;

    m_mail_subject_isSet = false;
    m_mail_subject_isValid = false;

    m_max_downloads_isSet = false;
    m_max_downloads_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_node_id_isSet = false;
    m_node_id_isValid = false;

    m_notes_isSet = false;
    m_notes_isValid = false;

    m_notify_creator_isSet = false;
    m_notify_creator_isValid = false;

    m_password_isSet = false;
    m_password_isValid = false;

    m_receiver_language_isSet = false;
    m_receiver_language_isValid = false;

    m_send_mail_isSet = false;
    m_send_mail_isValid = false;

    m_send_sms_isSet = false;
    m_send_sms_isValid = false;

    m_show_creator_name_isSet = false;
    m_show_creator_name_isValid = false;

    m_show_creator_username_isSet = false;
    m_show_creator_username_isValid = false;

    m_sms_recipients_isSet = false;
    m_sms_recipients_isValid = false;

    m_text_message_recipients_isSet = false;
    m_text_message_recipients_isValid = false;
}

void OAICreateDownloadShareRequest::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICreateDownloadShareRequest::fromJsonObject(QJsonObject json) {

    m_creator_language_isValid = ::OpenAPI::fromJsonValue(m_creator_language, json[QString("creatorLanguage")]);
    m_creator_language_isSet = !json[QString("creatorLanguage")].isNull() && m_creator_language_isValid;

    m_expiration_isValid = ::OpenAPI::fromJsonValue(m_expiration, json[QString("expiration")]);
    m_expiration_isSet = !json[QString("expiration")].isNull() && m_expiration_isValid;

    m_file_key_isValid = ::OpenAPI::fromJsonValue(m_file_key, json[QString("fileKey")]);
    m_file_key_isSet = !json[QString("fileKey")].isNull() && m_file_key_isValid;

    m_internal_notes_isValid = ::OpenAPI::fromJsonValue(m_internal_notes, json[QString("internalNotes")]);
    m_internal_notes_isSet = !json[QString("internalNotes")].isNull() && m_internal_notes_isValid;

    m_key_pair_isValid = ::OpenAPI::fromJsonValue(m_key_pair, json[QString("keyPair")]);
    m_key_pair_isSet = !json[QString("keyPair")].isNull() && m_key_pair_isValid;

    m_mail_body_isValid = ::OpenAPI::fromJsonValue(m_mail_body, json[QString("mailBody")]);
    m_mail_body_isSet = !json[QString("mailBody")].isNull() && m_mail_body_isValid;

    m_mail_recipients_isValid = ::OpenAPI::fromJsonValue(m_mail_recipients, json[QString("mailRecipients")]);
    m_mail_recipients_isSet = !json[QString("mailRecipients")].isNull() && m_mail_recipients_isValid;

    m_mail_subject_isValid = ::OpenAPI::fromJsonValue(m_mail_subject, json[QString("mailSubject")]);
    m_mail_subject_isSet = !json[QString("mailSubject")].isNull() && m_mail_subject_isValid;

    m_max_downloads_isValid = ::OpenAPI::fromJsonValue(m_max_downloads, json[QString("maxDownloads")]);
    m_max_downloads_isSet = !json[QString("maxDownloads")].isNull() && m_max_downloads_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_node_id_isValid = ::OpenAPI::fromJsonValue(m_node_id, json[QString("nodeId")]);
    m_node_id_isSet = !json[QString("nodeId")].isNull() && m_node_id_isValid;

    m_notes_isValid = ::OpenAPI::fromJsonValue(m_notes, json[QString("notes")]);
    m_notes_isSet = !json[QString("notes")].isNull() && m_notes_isValid;

    m_notify_creator_isValid = ::OpenAPI::fromJsonValue(m_notify_creator, json[QString("notifyCreator")]);
    m_notify_creator_isSet = !json[QString("notifyCreator")].isNull() && m_notify_creator_isValid;

    m_password_isValid = ::OpenAPI::fromJsonValue(m_password, json[QString("password")]);
    m_password_isSet = !json[QString("password")].isNull() && m_password_isValid;

    m_receiver_language_isValid = ::OpenAPI::fromJsonValue(m_receiver_language, json[QString("receiverLanguage")]);
    m_receiver_language_isSet = !json[QString("receiverLanguage")].isNull() && m_receiver_language_isValid;

    m_send_mail_isValid = ::OpenAPI::fromJsonValue(m_send_mail, json[QString("sendMail")]);
    m_send_mail_isSet = !json[QString("sendMail")].isNull() && m_send_mail_isValid;

    m_send_sms_isValid = ::OpenAPI::fromJsonValue(m_send_sms, json[QString("sendSms")]);
    m_send_sms_isSet = !json[QString("sendSms")].isNull() && m_send_sms_isValid;

    m_show_creator_name_isValid = ::OpenAPI::fromJsonValue(m_show_creator_name, json[QString("showCreatorName")]);
    m_show_creator_name_isSet = !json[QString("showCreatorName")].isNull() && m_show_creator_name_isValid;

    m_show_creator_username_isValid = ::OpenAPI::fromJsonValue(m_show_creator_username, json[QString("showCreatorUsername")]);
    m_show_creator_username_isSet = !json[QString("showCreatorUsername")].isNull() && m_show_creator_username_isValid;

    m_sms_recipients_isValid = ::OpenAPI::fromJsonValue(m_sms_recipients, json[QString("smsRecipients")]);
    m_sms_recipients_isSet = !json[QString("smsRecipients")].isNull() && m_sms_recipients_isValid;

    m_text_message_recipients_isValid = ::OpenAPI::fromJsonValue(m_text_message_recipients, json[QString("textMessageRecipients")]);
    m_text_message_recipients_isSet = !json[QString("textMessageRecipients")].isNull() && m_text_message_recipients_isValid;
}

QString OAICreateDownloadShareRequest::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICreateDownloadShareRequest::asJsonObject() const {
    QJsonObject obj;
    if (m_creator_language_isSet) {
        obj.insert(QString("creatorLanguage"), ::OpenAPI::toJsonValue(m_creator_language));
    }
    if (m_expiration.isSet()) {
        obj.insert(QString("expiration"), ::OpenAPI::toJsonValue(m_expiration));
    }
    if (m_file_key.isSet()) {
        obj.insert(QString("fileKey"), ::OpenAPI::toJsonValue(m_file_key));
    }
    if (m_internal_notes_isSet) {
        obj.insert(QString("internalNotes"), ::OpenAPI::toJsonValue(m_internal_notes));
    }
    if (m_key_pair.isSet()) {
        obj.insert(QString("keyPair"), ::OpenAPI::toJsonValue(m_key_pair));
    }
    if (m_mail_body_isSet) {
        obj.insert(QString("mailBody"), ::OpenAPI::toJsonValue(m_mail_body));
    }
    if (m_mail_recipients_isSet) {
        obj.insert(QString("mailRecipients"), ::OpenAPI::toJsonValue(m_mail_recipients));
    }
    if (m_mail_subject_isSet) {
        obj.insert(QString("mailSubject"), ::OpenAPI::toJsonValue(m_mail_subject));
    }
    if (m_max_downloads_isSet) {
        obj.insert(QString("maxDownloads"), ::OpenAPI::toJsonValue(m_max_downloads));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_node_id_isSet) {
        obj.insert(QString("nodeId"), ::OpenAPI::toJsonValue(m_node_id));
    }
    if (m_notes_isSet) {
        obj.insert(QString("notes"), ::OpenAPI::toJsonValue(m_notes));
    }
    if (m_notify_creator_isSet) {
        obj.insert(QString("notifyCreator"), ::OpenAPI::toJsonValue(m_notify_creator));
    }
    if (m_password_isSet) {
        obj.insert(QString("password"), ::OpenAPI::toJsonValue(m_password));
    }
    if (m_receiver_language_isSet) {
        obj.insert(QString("receiverLanguage"), ::OpenAPI::toJsonValue(m_receiver_language));
    }
    if (m_send_mail_isSet) {
        obj.insert(QString("sendMail"), ::OpenAPI::toJsonValue(m_send_mail));
    }
    if (m_send_sms_isSet) {
        obj.insert(QString("sendSms"), ::OpenAPI::toJsonValue(m_send_sms));
    }
    if (m_show_creator_name_isSet) {
        obj.insert(QString("showCreatorName"), ::OpenAPI::toJsonValue(m_show_creator_name));
    }
    if (m_show_creator_username_isSet) {
        obj.insert(QString("showCreatorUsername"), ::OpenAPI::toJsonValue(m_show_creator_username));
    }
    if (m_sms_recipients_isSet) {
        obj.insert(QString("smsRecipients"), ::OpenAPI::toJsonValue(m_sms_recipients));
    }
    if (m_text_message_recipients.size() > 0) {
        obj.insert(QString("textMessageRecipients"), ::OpenAPI::toJsonValue(m_text_message_recipients));
    }
    return obj;
}

QString OAICreateDownloadShareRequest::getCreatorLanguage() const {
    return m_creator_language;
}
void OAICreateDownloadShareRequest::setCreatorLanguage(const QString &creator_language) {
    m_creator_language = creator_language;
    m_creator_language_isSet = true;
}

bool OAICreateDownloadShareRequest::is_creator_language_Set() const{
    return m_creator_language_isSet;
}

bool OAICreateDownloadShareRequest::is_creator_language_Valid() const{
    return m_creator_language_isValid;
}

OAIObjectExpiration OAICreateDownloadShareRequest::getExpiration() const {
    return m_expiration;
}
void OAICreateDownloadShareRequest::setExpiration(const OAIObjectExpiration &expiration) {
    m_expiration = expiration;
    m_expiration_isSet = true;
}

bool OAICreateDownloadShareRequest::is_expiration_Set() const{
    return m_expiration_isSet;
}

bool OAICreateDownloadShareRequest::is_expiration_Valid() const{
    return m_expiration_isValid;
}

OAIFileKey OAICreateDownloadShareRequest::getFileKey() const {
    return m_file_key;
}
void OAICreateDownloadShareRequest::setFileKey(const OAIFileKey &file_key) {
    m_file_key = file_key;
    m_file_key_isSet = true;
}

bool OAICreateDownloadShareRequest::is_file_key_Set() const{
    return m_file_key_isSet;
}

bool OAICreateDownloadShareRequest::is_file_key_Valid() const{
    return m_file_key_isValid;
}

QString OAICreateDownloadShareRequest::getInternalNotes() const {
    return m_internal_notes;
}
void OAICreateDownloadShareRequest::setInternalNotes(const QString &internal_notes) {
    m_internal_notes = internal_notes;
    m_internal_notes_isSet = true;
}

bool OAICreateDownloadShareRequest::is_internal_notes_Set() const{
    return m_internal_notes_isSet;
}

bool OAICreateDownloadShareRequest::is_internal_notes_Valid() const{
    return m_internal_notes_isValid;
}

OAIUserKeyPairContainer OAICreateDownloadShareRequest::getKeyPair() const {
    return m_key_pair;
}
void OAICreateDownloadShareRequest::setKeyPair(const OAIUserKeyPairContainer &key_pair) {
    m_key_pair = key_pair;
    m_key_pair_isSet = true;
}

bool OAICreateDownloadShareRequest::is_key_pair_Set() const{
    return m_key_pair_isSet;
}

bool OAICreateDownloadShareRequest::is_key_pair_Valid() const{
    return m_key_pair_isValid;
}

QString OAICreateDownloadShareRequest::getMailBody() const {
    return m_mail_body;
}
void OAICreateDownloadShareRequest::setMailBody(const QString &mail_body) {
    m_mail_body = mail_body;
    m_mail_body_isSet = true;
}

bool OAICreateDownloadShareRequest::is_mail_body_Set() const{
    return m_mail_body_isSet;
}

bool OAICreateDownloadShareRequest::is_mail_body_Valid() const{
    return m_mail_body_isValid;
}

QString OAICreateDownloadShareRequest::getMailRecipients() const {
    return m_mail_recipients;
}
void OAICreateDownloadShareRequest::setMailRecipients(const QString &mail_recipients) {
    m_mail_recipients = mail_recipients;
    m_mail_recipients_isSet = true;
}

bool OAICreateDownloadShareRequest::is_mail_recipients_Set() const{
    return m_mail_recipients_isSet;
}

bool OAICreateDownloadShareRequest::is_mail_recipients_Valid() const{
    return m_mail_recipients_isValid;
}

QString OAICreateDownloadShareRequest::getMailSubject() const {
    return m_mail_subject;
}
void OAICreateDownloadShareRequest::setMailSubject(const QString &mail_subject) {
    m_mail_subject = mail_subject;
    m_mail_subject_isSet = true;
}

bool OAICreateDownloadShareRequest::is_mail_subject_Set() const{
    return m_mail_subject_isSet;
}

bool OAICreateDownloadShareRequest::is_mail_subject_Valid() const{
    return m_mail_subject_isValid;
}

qint32 OAICreateDownloadShareRequest::getMaxDownloads() const {
    return m_max_downloads;
}
void OAICreateDownloadShareRequest::setMaxDownloads(const qint32 &max_downloads) {
    m_max_downloads = max_downloads;
    m_max_downloads_isSet = true;
}

bool OAICreateDownloadShareRequest::is_max_downloads_Set() const{
    return m_max_downloads_isSet;
}

bool OAICreateDownloadShareRequest::is_max_downloads_Valid() const{
    return m_max_downloads_isValid;
}

QString OAICreateDownloadShareRequest::getName() const {
    return m_name;
}
void OAICreateDownloadShareRequest::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAICreateDownloadShareRequest::is_name_Set() const{
    return m_name_isSet;
}

bool OAICreateDownloadShareRequest::is_name_Valid() const{
    return m_name_isValid;
}

qint64 OAICreateDownloadShareRequest::getNodeId() const {
    return m_node_id;
}
void OAICreateDownloadShareRequest::setNodeId(const qint64 &node_id) {
    m_node_id = node_id;
    m_node_id_isSet = true;
}

bool OAICreateDownloadShareRequest::is_node_id_Set() const{
    return m_node_id_isSet;
}

bool OAICreateDownloadShareRequest::is_node_id_Valid() const{
    return m_node_id_isValid;
}

QString OAICreateDownloadShareRequest::getNotes() const {
    return m_notes;
}
void OAICreateDownloadShareRequest::setNotes(const QString &notes) {
    m_notes = notes;
    m_notes_isSet = true;
}

bool OAICreateDownloadShareRequest::is_notes_Set() const{
    return m_notes_isSet;
}

bool OAICreateDownloadShareRequest::is_notes_Valid() const{
    return m_notes_isValid;
}

bool OAICreateDownloadShareRequest::isNotifyCreator() const {
    return m_notify_creator;
}
void OAICreateDownloadShareRequest::setNotifyCreator(const bool &notify_creator) {
    m_notify_creator = notify_creator;
    m_notify_creator_isSet = true;
}

bool OAICreateDownloadShareRequest::is_notify_creator_Set() const{
    return m_notify_creator_isSet;
}

bool OAICreateDownloadShareRequest::is_notify_creator_Valid() const{
    return m_notify_creator_isValid;
}

QString OAICreateDownloadShareRequest::getPassword() const {
    return m_password;
}
void OAICreateDownloadShareRequest::setPassword(const QString &password) {
    m_password = password;
    m_password_isSet = true;
}

bool OAICreateDownloadShareRequest::is_password_Set() const{
    return m_password_isSet;
}

bool OAICreateDownloadShareRequest::is_password_Valid() const{
    return m_password_isValid;
}

QString OAICreateDownloadShareRequest::getReceiverLanguage() const {
    return m_receiver_language;
}
void OAICreateDownloadShareRequest::setReceiverLanguage(const QString &receiver_language) {
    m_receiver_language = receiver_language;
    m_receiver_language_isSet = true;
}

bool OAICreateDownloadShareRequest::is_receiver_language_Set() const{
    return m_receiver_language_isSet;
}

bool OAICreateDownloadShareRequest::is_receiver_language_Valid() const{
    return m_receiver_language_isValid;
}

bool OAICreateDownloadShareRequest::isSendMail() const {
    return m_send_mail;
}
void OAICreateDownloadShareRequest::setSendMail(const bool &send_mail) {
    m_send_mail = send_mail;
    m_send_mail_isSet = true;
}

bool OAICreateDownloadShareRequest::is_send_mail_Set() const{
    return m_send_mail_isSet;
}

bool OAICreateDownloadShareRequest::is_send_mail_Valid() const{
    return m_send_mail_isValid;
}

bool OAICreateDownloadShareRequest::isSendSms() const {
    return m_send_sms;
}
void OAICreateDownloadShareRequest::setSendSms(const bool &send_sms) {
    m_send_sms = send_sms;
    m_send_sms_isSet = true;
}

bool OAICreateDownloadShareRequest::is_send_sms_Set() const{
    return m_send_sms_isSet;
}

bool OAICreateDownloadShareRequest::is_send_sms_Valid() const{
    return m_send_sms_isValid;
}

bool OAICreateDownloadShareRequest::isShowCreatorName() const {
    return m_show_creator_name;
}
void OAICreateDownloadShareRequest::setShowCreatorName(const bool &show_creator_name) {
    m_show_creator_name = show_creator_name;
    m_show_creator_name_isSet = true;
}

bool OAICreateDownloadShareRequest::is_show_creator_name_Set() const{
    return m_show_creator_name_isSet;
}

bool OAICreateDownloadShareRequest::is_show_creator_name_Valid() const{
    return m_show_creator_name_isValid;
}

bool OAICreateDownloadShareRequest::isShowCreatorUsername() const {
    return m_show_creator_username;
}
void OAICreateDownloadShareRequest::setShowCreatorUsername(const bool &show_creator_username) {
    m_show_creator_username = show_creator_username;
    m_show_creator_username_isSet = true;
}

bool OAICreateDownloadShareRequest::is_show_creator_username_Set() const{
    return m_show_creator_username_isSet;
}

bool OAICreateDownloadShareRequest::is_show_creator_username_Valid() const{
    return m_show_creator_username_isValid;
}

QString OAICreateDownloadShareRequest::getSmsRecipients() const {
    return m_sms_recipients;
}
void OAICreateDownloadShareRequest::setSmsRecipients(const QString &sms_recipients) {
    m_sms_recipients = sms_recipients;
    m_sms_recipients_isSet = true;
}

bool OAICreateDownloadShareRequest::is_sms_recipients_Set() const{
    return m_sms_recipients_isSet;
}

bool OAICreateDownloadShareRequest::is_sms_recipients_Valid() const{
    return m_sms_recipients_isValid;
}

QList<QString> OAICreateDownloadShareRequest::getTextMessageRecipients() const {
    return m_text_message_recipients;
}
void OAICreateDownloadShareRequest::setTextMessageRecipients(const QList<QString> &text_message_recipients) {
    m_text_message_recipients = text_message_recipients;
    m_text_message_recipients_isSet = true;
}

bool OAICreateDownloadShareRequest::is_text_message_recipients_Set() const{
    return m_text_message_recipients_isSet;
}

bool OAICreateDownloadShareRequest::is_text_message_recipients_Valid() const{
    return m_text_message_recipients_isValid;
}

bool OAICreateDownloadShareRequest::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_creator_language_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_expiration.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_file_key.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_internal_notes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_key_pair.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_mail_body_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_mail_recipients_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_mail_subject_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_max_downloads_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_node_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_notes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_notify_creator_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_password_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_receiver_language_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_send_mail_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_send_sms_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_show_creator_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_show_creator_username_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sms_recipients_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_text_message_recipients.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICreateDownloadShareRequest::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_node_id_isValid && true;
}

} // namespace OpenAPI
