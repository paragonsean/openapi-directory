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

#include "OAIHealthInformationNotification_notification_statusNotification_statusResponses_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIHealthInformationNotification_notification_statusNotification_statusResponses_inner::OAIHealthInformationNotification_notification_statusNotification_statusResponses_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIHealthInformationNotification_notification_statusNotification_statusResponses_inner::OAIHealthInformationNotification_notification_statusNotification_statusResponses_inner() {
    this->initializeModel();
}

OAIHealthInformationNotification_notification_statusNotification_statusResponses_inner::~OAIHealthInformationNotification_notification_statusNotification_statusResponses_inner() {}

void OAIHealthInformationNotification_notification_statusNotification_statusResponses_inner::initializeModel() {

    m_care_context_reference_isSet = false;
    m_care_context_reference_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_hi_status_isSet = false;
    m_hi_status_isValid = false;
}

void OAIHealthInformationNotification_notification_statusNotification_statusResponses_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIHealthInformationNotification_notification_statusNotification_statusResponses_inner::fromJsonObject(QJsonObject json) {

    m_care_context_reference_isValid = ::OpenAPI::fromJsonValue(m_care_context_reference, json[QString("careContextReference")]);
    m_care_context_reference_isSet = !json[QString("careContextReference")].isNull() && m_care_context_reference_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_hi_status_isValid = ::OpenAPI::fromJsonValue(m_hi_status, json[QString("hiStatus")]);
    m_hi_status_isSet = !json[QString("hiStatus")].isNull() && m_hi_status_isValid;
}

QString OAIHealthInformationNotification_notification_statusNotification_statusResponses_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIHealthInformationNotification_notification_statusNotification_statusResponses_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_care_context_reference_isSet) {
        obj.insert(QString("careContextReference"), ::OpenAPI::toJsonValue(m_care_context_reference));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_hi_status_isSet) {
        obj.insert(QString("hiStatus"), ::OpenAPI::toJsonValue(m_hi_status));
    }
    return obj;
}

QString OAIHealthInformationNotification_notification_statusNotification_statusResponses_inner::getCareContextReference() const {
    return m_care_context_reference;
}
void OAIHealthInformationNotification_notification_statusNotification_statusResponses_inner::setCareContextReference(const QString &care_context_reference) {
    m_care_context_reference = care_context_reference;
    m_care_context_reference_isSet = true;
}

bool OAIHealthInformationNotification_notification_statusNotification_statusResponses_inner::is_care_context_reference_Set() const{
    return m_care_context_reference_isSet;
}

bool OAIHealthInformationNotification_notification_statusNotification_statusResponses_inner::is_care_context_reference_Valid() const{
    return m_care_context_reference_isValid;
}

QString OAIHealthInformationNotification_notification_statusNotification_statusResponses_inner::getDescription() const {
    return m_description;
}
void OAIHealthInformationNotification_notification_statusNotification_statusResponses_inner::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIHealthInformationNotification_notification_statusNotification_statusResponses_inner::is_description_Set() const{
    return m_description_isSet;
}

bool OAIHealthInformationNotification_notification_statusNotification_statusResponses_inner::is_description_Valid() const{
    return m_description_isValid;
}

QString OAIHealthInformationNotification_notification_statusNotification_statusResponses_inner::getHiStatus() const {
    return m_hi_status;
}
void OAIHealthInformationNotification_notification_statusNotification_statusResponses_inner::setHiStatus(const QString &hi_status) {
    m_hi_status = hi_status;
    m_hi_status_isSet = true;
}

bool OAIHealthInformationNotification_notification_statusNotification_statusResponses_inner::is_hi_status_Set() const{
    return m_hi_status_isSet;
}

bool OAIHealthInformationNotification_notification_statusNotification_statusResponses_inner::is_hi_status_Valid() const{
    return m_hi_status_isValid;
}

bool OAIHealthInformationNotification_notification_statusNotification_statusResponses_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_care_context_reference_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_hi_status_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIHealthInformationNotification_notification_statusNotification_statusResponses_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_care_context_reference_isValid && m_hi_status_isValid && true;
}

} // namespace OpenAPI
