/**
 * CallFire API Documentation
 * CallFire
 *
 * The version of the OpenAPI document: V2
 * Contact: support@callfire.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIMedia.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIMedia::OAIMedia(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIMedia::OAIMedia() {
    this->initializeModel();
}

OAIMedia::~OAIMedia() {}

void OAIMedia::initializeModel() {

    m_account_id_isSet = false;
    m_account_id_isValid = false;

    m_created_isSet = false;
    m_created_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_length_in_bytes_isSet = false;
    m_length_in_bytes_isValid = false;

    m_media_type_isSet = false;
    m_media_type_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_public_url_isSet = false;
    m_public_url_isValid = false;
}

void OAIMedia::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIMedia::fromJsonObject(QJsonObject json) {

    m_account_id_isValid = ::OpenAPI::fromJsonValue(m_account_id, json[QString("accountId")]);
    m_account_id_isSet = !json[QString("accountId")].isNull() && m_account_id_isValid;

    m_created_isValid = ::OpenAPI::fromJsonValue(m_created, json[QString("created")]);
    m_created_isSet = !json[QString("created")].isNull() && m_created_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_length_in_bytes_isValid = ::OpenAPI::fromJsonValue(m_length_in_bytes, json[QString("lengthInBytes")]);
    m_length_in_bytes_isSet = !json[QString("lengthInBytes")].isNull() && m_length_in_bytes_isValid;

    m_media_type_isValid = ::OpenAPI::fromJsonValue(m_media_type, json[QString("mediaType")]);
    m_media_type_isSet = !json[QString("mediaType")].isNull() && m_media_type_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_public_url_isValid = ::OpenAPI::fromJsonValue(m_public_url, json[QString("publicUrl")]);
    m_public_url_isSet = !json[QString("publicUrl")].isNull() && m_public_url_isValid;
}

QString OAIMedia::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIMedia::asJsonObject() const {
    QJsonObject obj;
    if (m_account_id_isSet) {
        obj.insert(QString("accountId"), ::OpenAPI::toJsonValue(m_account_id));
    }
    if (m_created_isSet) {
        obj.insert(QString("created"), ::OpenAPI::toJsonValue(m_created));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_length_in_bytes_isSet) {
        obj.insert(QString("lengthInBytes"), ::OpenAPI::toJsonValue(m_length_in_bytes));
    }
    if (m_media_type_isSet) {
        obj.insert(QString("mediaType"), ::OpenAPI::toJsonValue(m_media_type));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_public_url_isSet) {
        obj.insert(QString("publicUrl"), ::OpenAPI::toJsonValue(m_public_url));
    }
    return obj;
}

qint64 OAIMedia::getAccountId() const {
    return m_account_id;
}
void OAIMedia::setAccountId(const qint64 &account_id) {
    m_account_id = account_id;
    m_account_id_isSet = true;
}

bool OAIMedia::is_account_id_Set() const{
    return m_account_id_isSet;
}

bool OAIMedia::is_account_id_Valid() const{
    return m_account_id_isValid;
}

qint64 OAIMedia::getCreated() const {
    return m_created;
}
void OAIMedia::setCreated(const qint64 &created) {
    m_created = created;
    m_created_isSet = true;
}

bool OAIMedia::is_created_Set() const{
    return m_created_isSet;
}

bool OAIMedia::is_created_Valid() const{
    return m_created_isValid;
}

qint64 OAIMedia::getId() const {
    return m_id;
}
void OAIMedia::setId(const qint64 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIMedia::is_id_Set() const{
    return m_id_isSet;
}

bool OAIMedia::is_id_Valid() const{
    return m_id_isValid;
}

qint64 OAIMedia::getLengthInBytes() const {
    return m_length_in_bytes;
}
void OAIMedia::setLengthInBytes(const qint64 &length_in_bytes) {
    m_length_in_bytes = length_in_bytes;
    m_length_in_bytes_isSet = true;
}

bool OAIMedia::is_length_in_bytes_Set() const{
    return m_length_in_bytes_isSet;
}

bool OAIMedia::is_length_in_bytes_Valid() const{
    return m_length_in_bytes_isValid;
}

QString OAIMedia::getMediaType() const {
    return m_media_type;
}
void OAIMedia::setMediaType(const QString &media_type) {
    m_media_type = media_type;
    m_media_type_isSet = true;
}

bool OAIMedia::is_media_type_Set() const{
    return m_media_type_isSet;
}

bool OAIMedia::is_media_type_Valid() const{
    return m_media_type_isValid;
}

QString OAIMedia::getName() const {
    return m_name;
}
void OAIMedia::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIMedia::is_name_Set() const{
    return m_name_isSet;
}

bool OAIMedia::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIMedia::getPublicUrl() const {
    return m_public_url;
}
void OAIMedia::setPublicUrl(const QString &public_url) {
    m_public_url = public_url;
    m_public_url_isSet = true;
}

bool OAIMedia::is_public_url_Set() const{
    return m_public_url_isSet;
}

bool OAIMedia::is_public_url_Valid() const{
    return m_public_url_isValid;
}

bool OAIMedia::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_account_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_length_in_bytes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_media_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_public_url_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIMedia::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
