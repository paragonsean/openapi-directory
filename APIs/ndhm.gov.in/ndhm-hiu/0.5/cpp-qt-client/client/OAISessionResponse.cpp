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

#include "OAISessionResponse.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISessionResponse::OAISessionResponse(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISessionResponse::OAISessionResponse() {
    this->initializeModel();
}

OAISessionResponse::~OAISessionResponse() {}

void OAISessionResponse::initializeModel() {

    m_access_token_isSet = false;
    m_access_token_isValid = false;

    m_expires_in_isSet = false;
    m_expires_in_isValid = false;

    m_refresh_expires_in_isSet = false;
    m_refresh_expires_in_isValid = false;

    m_refresh_token_isSet = false;
    m_refresh_token_isValid = false;

    m_token_type_isSet = false;
    m_token_type_isValid = false;
}

void OAISessionResponse::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISessionResponse::fromJsonObject(QJsonObject json) {

    m_access_token_isValid = ::OpenAPI::fromJsonValue(m_access_token, json[QString("accessToken")]);
    m_access_token_isSet = !json[QString("accessToken")].isNull() && m_access_token_isValid;

    m_expires_in_isValid = ::OpenAPI::fromJsonValue(m_expires_in, json[QString("expiresIn")]);
    m_expires_in_isSet = !json[QString("expiresIn")].isNull() && m_expires_in_isValid;

    m_refresh_expires_in_isValid = ::OpenAPI::fromJsonValue(m_refresh_expires_in, json[QString("refreshExpiresIn")]);
    m_refresh_expires_in_isSet = !json[QString("refreshExpiresIn")].isNull() && m_refresh_expires_in_isValid;

    m_refresh_token_isValid = ::OpenAPI::fromJsonValue(m_refresh_token, json[QString("refreshToken")]);
    m_refresh_token_isSet = !json[QString("refreshToken")].isNull() && m_refresh_token_isValid;

    m_token_type_isValid = ::OpenAPI::fromJsonValue(m_token_type, json[QString("tokenType")]);
    m_token_type_isSet = !json[QString("tokenType")].isNull() && m_token_type_isValid;
}

QString OAISessionResponse::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISessionResponse::asJsonObject() const {
    QJsonObject obj;
    if (m_access_token_isSet) {
        obj.insert(QString("accessToken"), ::OpenAPI::toJsonValue(m_access_token));
    }
    if (m_expires_in_isSet) {
        obj.insert(QString("expiresIn"), ::OpenAPI::toJsonValue(m_expires_in));
    }
    if (m_refresh_expires_in_isSet) {
        obj.insert(QString("refreshExpiresIn"), ::OpenAPI::toJsonValue(m_refresh_expires_in));
    }
    if (m_refresh_token_isSet) {
        obj.insert(QString("refreshToken"), ::OpenAPI::toJsonValue(m_refresh_token));
    }
    if (m_token_type_isSet) {
        obj.insert(QString("tokenType"), ::OpenAPI::toJsonValue(m_token_type));
    }
    return obj;
}

QString OAISessionResponse::getAccessToken() const {
    return m_access_token;
}
void OAISessionResponse::setAccessToken(const QString &access_token) {
    m_access_token = access_token;
    m_access_token_isSet = true;
}

bool OAISessionResponse::is_access_token_Set() const{
    return m_access_token_isSet;
}

bool OAISessionResponse::is_access_token_Valid() const{
    return m_access_token_isValid;
}

qint32 OAISessionResponse::getExpiresIn() const {
    return m_expires_in;
}
void OAISessionResponse::setExpiresIn(const qint32 &expires_in) {
    m_expires_in = expires_in;
    m_expires_in_isSet = true;
}

bool OAISessionResponse::is_expires_in_Set() const{
    return m_expires_in_isSet;
}

bool OAISessionResponse::is_expires_in_Valid() const{
    return m_expires_in_isValid;
}

qint32 OAISessionResponse::getRefreshExpiresIn() const {
    return m_refresh_expires_in;
}
void OAISessionResponse::setRefreshExpiresIn(const qint32 &refresh_expires_in) {
    m_refresh_expires_in = refresh_expires_in;
    m_refresh_expires_in_isSet = true;
}

bool OAISessionResponse::is_refresh_expires_in_Set() const{
    return m_refresh_expires_in_isSet;
}

bool OAISessionResponse::is_refresh_expires_in_Valid() const{
    return m_refresh_expires_in_isValid;
}

QString OAISessionResponse::getRefreshToken() const {
    return m_refresh_token;
}
void OAISessionResponse::setRefreshToken(const QString &refresh_token) {
    m_refresh_token = refresh_token;
    m_refresh_token_isSet = true;
}

bool OAISessionResponse::is_refresh_token_Set() const{
    return m_refresh_token_isSet;
}

bool OAISessionResponse::is_refresh_token_Valid() const{
    return m_refresh_token_isValid;
}

QString OAISessionResponse::getTokenType() const {
    return m_token_type;
}
void OAISessionResponse::setTokenType(const QString &token_type) {
    m_token_type = token_type;
    m_token_type_isSet = true;
}

bool OAISessionResponse::is_token_type_Set() const{
    return m_token_type_isSet;
}

bool OAISessionResponse::is_token_type_Valid() const{
    return m_token_type_isValid;
}

bool OAISessionResponse::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_access_token_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_expires_in_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_refresh_expires_in_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_refresh_token_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_token_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISessionResponse::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
