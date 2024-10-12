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

#include "OAICerts.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICerts::OAICerts(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICerts::OAICerts() {
    this->initializeModel();
}

OAICerts::~OAICerts() {}

void OAICerts::initializeModel() {

    m_keys_isSet = false;
    m_keys_isValid = false;
}

void OAICerts::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICerts::fromJsonObject(QJsonObject json) {

    m_keys_isValid = ::OpenAPI::fromJsonValue(m_keys, json[QString("keys")]);
    m_keys_isSet = !json[QString("keys")].isNull() && m_keys_isValid;
}

QString OAICerts::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICerts::asJsonObject() const {
    QJsonObject obj;
    if (m_keys.size() > 0) {
        obj.insert(QString("keys"), ::OpenAPI::toJsonValue(m_keys));
    }
    return obj;
}

QList<OAICertificateOrKeyGetSchema> OAICerts::getKeys() const {
    return m_keys;
}
void OAICerts::setKeys(const QList<OAICertificateOrKeyGetSchema> &keys) {
    m_keys = keys;
    m_keys_isSet = true;
}

bool OAICerts::is_keys_Set() const{
    return m_keys_isSet;
}

bool OAICerts::is_keys_Valid() const{
    return m_keys_isValid;
}

bool OAICerts::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_keys.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICerts::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
