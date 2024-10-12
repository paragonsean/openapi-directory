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

#include "OAIConsentRequestInitResponse.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIConsentRequestInitResponse::OAIConsentRequestInitResponse(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIConsentRequestInitResponse::OAIConsentRequestInitResponse() {
    this->initializeModel();
}

OAIConsentRequestInitResponse::~OAIConsentRequestInitResponse() {}

void OAIConsentRequestInitResponse::initializeModel() {

    m_consent_request_isSet = false;
    m_consent_request_isValid = false;

    m_error_isSet = false;
    m_error_isValid = false;

    m_request_id_isSet = false;
    m_request_id_isValid = false;

    m_resp_isSet = false;
    m_resp_isValid = false;

    m_timestamp_isSet = false;
    m_timestamp_isValid = false;
}

void OAIConsentRequestInitResponse::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIConsentRequestInitResponse::fromJsonObject(QJsonObject json) {

    m_consent_request_isValid = ::OpenAPI::fromJsonValue(m_consent_request, json[QString("consentRequest")]);
    m_consent_request_isSet = !json[QString("consentRequest")].isNull() && m_consent_request_isValid;

    m_error_isValid = ::OpenAPI::fromJsonValue(m_error, json[QString("error")]);
    m_error_isSet = !json[QString("error")].isNull() && m_error_isValid;

    m_request_id_isValid = ::OpenAPI::fromJsonValue(m_request_id, json[QString("requestId")]);
    m_request_id_isSet = !json[QString("requestId")].isNull() && m_request_id_isValid;

    m_resp_isValid = ::OpenAPI::fromJsonValue(m_resp, json[QString("resp")]);
    m_resp_isSet = !json[QString("resp")].isNull() && m_resp_isValid;

    m_timestamp_isValid = ::OpenAPI::fromJsonValue(m_timestamp, json[QString("timestamp")]);
    m_timestamp_isSet = !json[QString("timestamp")].isNull() && m_timestamp_isValid;
}

QString OAIConsentRequestInitResponse::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIConsentRequestInitResponse::asJsonObject() const {
    QJsonObject obj;
    if (m_consent_request.isSet()) {
        obj.insert(QString("consentRequest"), ::OpenAPI::toJsonValue(m_consent_request));
    }
    if (m_error.isSet()) {
        obj.insert(QString("error"), ::OpenAPI::toJsonValue(m_error));
    }
    if (m_request_id_isSet) {
        obj.insert(QString("requestId"), ::OpenAPI::toJsonValue(m_request_id));
    }
    if (m_resp.isSet()) {
        obj.insert(QString("resp"), ::OpenAPI::toJsonValue(m_resp));
    }
    if (m_timestamp_isSet) {
        obj.insert(QString("timestamp"), ::OpenAPI::toJsonValue(m_timestamp));
    }
    return obj;
}

OAIConsentRequestInitResponse_consentRequest OAIConsentRequestInitResponse::getConsentRequest() const {
    return m_consent_request;
}
void OAIConsentRequestInitResponse::setConsentRequest(const OAIConsentRequestInitResponse_consentRequest &consent_request) {
    m_consent_request = consent_request;
    m_consent_request_isSet = true;
}

bool OAIConsentRequestInitResponse::is_consent_request_Set() const{
    return m_consent_request_isSet;
}

bool OAIConsentRequestInitResponse::is_consent_request_Valid() const{
    return m_consent_request_isValid;
}

OAIError OAIConsentRequestInitResponse::getError() const {
    return m_error;
}
void OAIConsentRequestInitResponse::setError(const OAIError &error) {
    m_error = error;
    m_error_isSet = true;
}

bool OAIConsentRequestInitResponse::is_error_Set() const{
    return m_error_isSet;
}

bool OAIConsentRequestInitResponse::is_error_Valid() const{
    return m_error_isValid;
}

QString OAIConsentRequestInitResponse::getRequestId() const {
    return m_request_id;
}
void OAIConsentRequestInitResponse::setRequestId(const QString &request_id) {
    m_request_id = request_id;
    m_request_id_isSet = true;
}

bool OAIConsentRequestInitResponse::is_request_id_Set() const{
    return m_request_id_isSet;
}

bool OAIConsentRequestInitResponse::is_request_id_Valid() const{
    return m_request_id_isValid;
}

OAIRequestReference OAIConsentRequestInitResponse::getResp() const {
    return m_resp;
}
void OAIConsentRequestInitResponse::setResp(const OAIRequestReference &resp) {
    m_resp = resp;
    m_resp_isSet = true;
}

bool OAIConsentRequestInitResponse::is_resp_Set() const{
    return m_resp_isSet;
}

bool OAIConsentRequestInitResponse::is_resp_Valid() const{
    return m_resp_isValid;
}

QDateTime OAIConsentRequestInitResponse::getTimestamp() const {
    return m_timestamp;
}
void OAIConsentRequestInitResponse::setTimestamp(const QDateTime &timestamp) {
    m_timestamp = timestamp;
    m_timestamp_isSet = true;
}

bool OAIConsentRequestInitResponse::is_timestamp_Set() const{
    return m_timestamp_isSet;
}

bool OAIConsentRequestInitResponse::is_timestamp_Valid() const{
    return m_timestamp_isValid;
}

bool OAIConsentRequestInitResponse::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_consent_request.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_error.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_request_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_resp.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_timestamp_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIConsentRequestInitResponse::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_request_id_isValid && m_resp_isValid && m_timestamp_isValid && true;
}

} // namespace OpenAPI
