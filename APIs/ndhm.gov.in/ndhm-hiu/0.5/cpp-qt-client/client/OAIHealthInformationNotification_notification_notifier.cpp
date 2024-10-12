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

#include "OAIHealthInformationNotification_notification_notifier.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIHealthInformationNotification_notification_notifier::OAIHealthInformationNotification_notification_notifier(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIHealthInformationNotification_notification_notifier::OAIHealthInformationNotification_notification_notifier() {
    this->initializeModel();
}

OAIHealthInformationNotification_notification_notifier::~OAIHealthInformationNotification_notification_notifier() {}

void OAIHealthInformationNotification_notification_notifier::initializeModel() {

    m_id_isSet = false;
    m_id_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIHealthInformationNotification_notification_notifier::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIHealthInformationNotification_notification_notifier::fromJsonObject(QJsonObject json) {

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAIHealthInformationNotification_notification_notifier::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIHealthInformationNotification_notification_notifier::asJsonObject() const {
    QJsonObject obj;
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

QString OAIHealthInformationNotification_notification_notifier::getId() const {
    return m_id;
}
void OAIHealthInformationNotification_notification_notifier::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIHealthInformationNotification_notification_notifier::is_id_Set() const{
    return m_id_isSet;
}

bool OAIHealthInformationNotification_notification_notifier::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIHealthInformationNotification_notification_notifier::getType() const {
    return m_type;
}
void OAIHealthInformationNotification_notification_notifier::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIHealthInformationNotification_notification_notifier::is_type_Set() const{
    return m_type_isSet;
}

bool OAIHealthInformationNotification_notification_notifier::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIHealthInformationNotification_notification_notifier::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_id_isSet) {
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

bool OAIHealthInformationNotification_notification_notifier::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_id_isValid && m_type_isValid && true;
}

} // namespace OpenAPI
