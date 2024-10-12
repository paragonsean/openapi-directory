/**
 * Health Repository Provider Specifications for HIU
 * The following are the specifications for the APIs to be implemented at the Health Repository end if an entity is only serving the role of a HIU. The specs are essentially duplicates from the Gateway and Bridge, but put together so as to make it clear to *HIUs* which set of APIs they should implement to participate in the network.     1. The APIs are organized by the flows - **identification**, **consent flow**, **data flow** and **monitoring**. They represent the APIs that are expected to be available at the HIU end by the Gateway.    2. For majority of the APIs, if Gateway has initiated a call, there are corresponding callback APIs on the Gateway. e.g for **_/consents/hiu/notify** API on HIU end, its expected that a corresponding callback API **_/consents/hiu/on-notify** on Gateway is called. Such APIs are organized under the **Gateway** label.    3. Gateway relevant APIs for HIUs are grouped under **Gateway** label. These include the APIs that HIPs are required to call on the Gateway. For example, to request a CM for consent, HIU would call **_/consent-requests/init** API on gateway.    4. **NOTE**, in some of the API documentations below, **X-HIP-ID** is mentioned in header (for example in /auth/on-init). These are the cases, when a particular API is applicable for both HIU and HIP (e.g an entity is playing the role of HRP representing both HIU and HIP). If you are only playing the role of HIP, then only X-HIU-ID header will be sent  
 *
 * The version of the OpenAPI document: 0.5
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIDataNotification_entries_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIDataNotification_entries_inner::OAIDataNotification_entries_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIDataNotification_entries_inner::OAIDataNotification_entries_inner() {
    this->initializeModel();
}

OAIDataNotification_entries_inner::~OAIDataNotification_entries_inner() {}

void OAIDataNotification_entries_inner::initializeModel() {

    m_care_context_reference_isSet = false;
    m_care_context_reference_isValid = false;

    m_checksum_isSet = false;
    m_checksum_isValid = false;

    m_content_isSet = false;
    m_content_isValid = false;

    m_media_isSet = false;
    m_media_isValid = false;

    m_link_isSet = false;
    m_link_isValid = false;
}

void OAIDataNotification_entries_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIDataNotification_entries_inner::fromJsonObject(QJsonObject json) {

    m_care_context_reference_isValid = ::OpenAPI::fromJsonValue(m_care_context_reference, json[QString("careContextReference")]);
    m_care_context_reference_isSet = !json[QString("careContextReference")].isNull() && m_care_context_reference_isValid;

    m_checksum_isValid = ::OpenAPI::fromJsonValue(m_checksum, json[QString("checksum")]);
    m_checksum_isSet = !json[QString("checksum")].isNull() && m_checksum_isValid;

    m_content_isValid = ::OpenAPI::fromJsonValue(m_content, json[QString("content")]);
    m_content_isSet = !json[QString("content")].isNull() && m_content_isValid;

    m_media_isValid = ::OpenAPI::fromJsonValue(m_media, json[QString("media")]);
    m_media_isSet = !json[QString("media")].isNull() && m_media_isValid;

    m_link_isValid = ::OpenAPI::fromJsonValue(m_link, json[QString("link")]);
    m_link_isSet = !json[QString("link")].isNull() && m_link_isValid;
}

QString OAIDataNotification_entries_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIDataNotification_entries_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_care_context_reference_isSet) {
        obj.insert(QString("careContextReference"), ::OpenAPI::toJsonValue(m_care_context_reference));
    }
    if (m_checksum_isSet) {
        obj.insert(QString("checksum"), ::OpenAPI::toJsonValue(m_checksum));
    }
    if (m_content_isSet) {
        obj.insert(QString("content"), ::OpenAPI::toJsonValue(m_content));
    }
    if (m_media_isSet) {
        obj.insert(QString("media"), ::OpenAPI::toJsonValue(m_media));
    }
    if (m_link_isSet) {
        obj.insert(QString("link"), ::OpenAPI::toJsonValue(m_link));
    }
    return obj;
}

QString OAIDataNotification_entries_inner::getCareContextReference() const {
    return m_care_context_reference;
}
void OAIDataNotification_entries_inner::setCareContextReference(const QString &care_context_reference) {
    m_care_context_reference = care_context_reference;
    m_care_context_reference_isSet = true;
}

bool OAIDataNotification_entries_inner::is_care_context_reference_Set() const{
    return m_care_context_reference_isSet;
}

bool OAIDataNotification_entries_inner::is_care_context_reference_Valid() const{
    return m_care_context_reference_isValid;
}

QString OAIDataNotification_entries_inner::getChecksum() const {
    return m_checksum;
}
void OAIDataNotification_entries_inner::setChecksum(const QString &checksum) {
    m_checksum = checksum;
    m_checksum_isSet = true;
}

bool OAIDataNotification_entries_inner::is_checksum_Set() const{
    return m_checksum_isSet;
}

bool OAIDataNotification_entries_inner::is_checksum_Valid() const{
    return m_checksum_isValid;
}

QString OAIDataNotification_entries_inner::getContent() const {
    return m_content;
}
void OAIDataNotification_entries_inner::setContent(const QString &content) {
    m_content = content;
    m_content_isSet = true;
}

bool OAIDataNotification_entries_inner::is_content_Set() const{
    return m_content_isSet;
}

bool OAIDataNotification_entries_inner::is_content_Valid() const{
    return m_content_isValid;
}

QString OAIDataNotification_entries_inner::getMedia() const {
    return m_media;
}
void OAIDataNotification_entries_inner::setMedia(const QString &media) {
    m_media = media;
    m_media_isSet = true;
}

bool OAIDataNotification_entries_inner::is_media_Set() const{
    return m_media_isSet;
}

bool OAIDataNotification_entries_inner::is_media_Valid() const{
    return m_media_isValid;
}

QString OAIDataNotification_entries_inner::getLink() const {
    return m_link;
}
void OAIDataNotification_entries_inner::setLink(const QString &link) {
    m_link = link;
    m_link_isSet = true;
}

bool OAIDataNotification_entries_inner::is_link_Set() const{
    return m_link_isSet;
}

bool OAIDataNotification_entries_inner::is_link_Valid() const{
    return m_link_isValid;
}

bool OAIDataNotification_entries_inner::isSet() const {
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

        if (m_content_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_media_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_link_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIDataNotification_entries_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_care_context_reference_isValid && m_checksum_isValid && m_content_isValid && m_media_isValid && m_link_isValid && true;
}

} // namespace OpenAPI
