/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIUsers_getUserMetadata_200_response.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUsers_getUserMetadata_200_response::OAIUsers_getUserMetadata_200_response(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUsers_getUserMetadata_200_response::OAIUsers_getUserMetadata_200_response() {
    this->initializeModel();
}

OAIUsers_getUserMetadata_200_response::~OAIUsers_getUserMetadata_200_response() {}

void OAIUsers_getUserMetadata_200_response::initializeModel() {

    m_metadata_isSet = false;
    m_metadata_isValid = false;

    m_user_id_isSet = false;
    m_user_id_isValid = false;
}

void OAIUsers_getUserMetadata_200_response::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUsers_getUserMetadata_200_response::fromJsonObject(QJsonObject json) {

    m_metadata_isValid = ::OpenAPI::fromJsonValue(m_metadata, json[QString("metadata")]);
    m_metadata_isSet = !json[QString("metadata")].isNull() && m_metadata_isValid;

    m_user_id_isValid = ::OpenAPI::fromJsonValue(m_user_id, json[QString("userId")]);
    m_user_id_isSet = !json[QString("userId")].isNull() && m_user_id_isValid;
}

QString OAIUsers_getUserMetadata_200_response::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUsers_getUserMetadata_200_response::asJsonObject() const {
    QJsonObject obj;
    if (m_metadata_isSet) {
        obj.insert(QString("metadata"), ::OpenAPI::toJsonValue(m_metadata));
    }
    if (m_user_id_isSet) {
        obj.insert(QString("userId"), ::OpenAPI::toJsonValue(m_user_id));
    }
    return obj;
}

OAIObject OAIUsers_getUserMetadata_200_response::getMetadata() const {
    return m_metadata;
}
void OAIUsers_getUserMetadata_200_response::setMetadata(const OAIObject &metadata) {
    m_metadata = metadata;
    m_metadata_isSet = true;
}

bool OAIUsers_getUserMetadata_200_response::is_metadata_Set() const{
    return m_metadata_isSet;
}

bool OAIUsers_getUserMetadata_200_response::is_metadata_Valid() const{
    return m_metadata_isValid;
}

QString OAIUsers_getUserMetadata_200_response::getUserId() const {
    return m_user_id;
}
void OAIUsers_getUserMetadata_200_response::setUserId(const QString &user_id) {
    m_user_id = user_id;
    m_user_id_isSet = true;
}

bool OAIUsers_getUserMetadata_200_response::is_user_id_Set() const{
    return m_user_id_isSet;
}

bool OAIUsers_getUserMetadata_200_response::is_user_id_Valid() const{
    return m_user_id_isValid;
}

bool OAIUsers_getUserMetadata_200_response::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_metadata_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_user_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUsers_getUserMetadata_200_response::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
