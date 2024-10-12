/**
 * Health Repository Provider Specifications for HIP
 * The following are the specifications for the APIs to be implemented at the Health Repository end if an entity is only serving the role of a HIP. The specs are essentially duplicates from the Gateway and Health Repository, but put together so as to make it clear to *HIPs* which set of APIs they should implement to participate in the network.  
 *
 * The version of the OpenAPI document: 0.5
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIEntryLink.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIEntryLink::OAIEntryLink(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIEntryLink::OAIEntryLink() {
    this->initializeModel();
}

OAIEntryLink::~OAIEntryLink() {}

void OAIEntryLink::initializeModel() {

    m_care_context_reference_isSet = false;
    m_care_context_reference_isValid = false;

    m_checksum_isSet = false;
    m_checksum_isValid = false;

    m_link_isSet = false;
    m_link_isValid = false;

    m_media_isSet = false;
    m_media_isValid = false;
}

void OAIEntryLink::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIEntryLink::fromJsonObject(QJsonObject json) {

    m_care_context_reference_isValid = ::OpenAPI::fromJsonValue(m_care_context_reference, json[QString("careContextReference")]);
    m_care_context_reference_isSet = !json[QString("careContextReference")].isNull() && m_care_context_reference_isValid;

    m_checksum_isValid = ::OpenAPI::fromJsonValue(m_checksum, json[QString("checksum")]);
    m_checksum_isSet = !json[QString("checksum")].isNull() && m_checksum_isValid;

    m_link_isValid = ::OpenAPI::fromJsonValue(m_link, json[QString("link")]);
    m_link_isSet = !json[QString("link")].isNull() && m_link_isValid;

    m_media_isValid = ::OpenAPI::fromJsonValue(m_media, json[QString("media")]);
    m_media_isSet = !json[QString("media")].isNull() && m_media_isValid;
}

QString OAIEntryLink::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIEntryLink::asJsonObject() const {
    QJsonObject obj;
    if (m_care_context_reference_isSet) {
        obj.insert(QString("careContextReference"), ::OpenAPI::toJsonValue(m_care_context_reference));
    }
    if (m_checksum_isSet) {
        obj.insert(QString("checksum"), ::OpenAPI::toJsonValue(m_checksum));
    }
    if (m_link_isSet) {
        obj.insert(QString("link"), ::OpenAPI::toJsonValue(m_link));
    }
    if (m_media_isSet) {
        obj.insert(QString("media"), ::OpenAPI::toJsonValue(m_media));
    }
    return obj;
}

QString OAIEntryLink::getCareContextReference() const {
    return m_care_context_reference;
}
void OAIEntryLink::setCareContextReference(const QString &care_context_reference) {
    m_care_context_reference = care_context_reference;
    m_care_context_reference_isSet = true;
}

bool OAIEntryLink::is_care_context_reference_Set() const{
    return m_care_context_reference_isSet;
}

bool OAIEntryLink::is_care_context_reference_Valid() const{
    return m_care_context_reference_isValid;
}

QString OAIEntryLink::getChecksum() const {
    return m_checksum;
}
void OAIEntryLink::setChecksum(const QString &checksum) {
    m_checksum = checksum;
    m_checksum_isSet = true;
}

bool OAIEntryLink::is_checksum_Set() const{
    return m_checksum_isSet;
}

bool OAIEntryLink::is_checksum_Valid() const{
    return m_checksum_isValid;
}

QString OAIEntryLink::getLink() const {
    return m_link;
}
void OAIEntryLink::setLink(const QString &link) {
    m_link = link;
    m_link_isSet = true;
}

bool OAIEntryLink::is_link_Set() const{
    return m_link_isSet;
}

bool OAIEntryLink::is_link_Valid() const{
    return m_link_isValid;
}

QString OAIEntryLink::getMedia() const {
    return m_media;
}
void OAIEntryLink::setMedia(const QString &media) {
    m_media = media;
    m_media_isSet = true;
}

bool OAIEntryLink::is_media_Set() const{
    return m_media_isSet;
}

bool OAIEntryLink::is_media_Valid() const{
    return m_media_isValid;
}

bool OAIEntryLink::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_care_context_reference_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_checksum_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_link_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_media_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIEntryLink::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_care_context_reference_isValid && m_checksum_isValid && m_link_isValid && m_media_isValid && true;
}

} // namespace OpenAPI
