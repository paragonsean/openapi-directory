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

#include "OAIIdentifierType.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIIdentifierType::OAIIdentifierType(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIIdentifierType::OAIIdentifierType() {
    this->initializeModel();
}

OAIIdentifierType::~OAIIdentifierType() {}

void OAIIdentifierType::initializeModel() {

    m_value_isSet = false;
    m_value_isValid = false;
    m_value = eOAIIdentifierType::INVALID_VALUE_OPENAPI_GENERATED;
}

void OAIIdentifierType::fromJson(QString jsonString) {
    
    if ( jsonString.compare("MOBILE", Qt::CaseInsensitive) == 0) {
        m_value = eOAIIdentifierType::MOBILE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("MR", Qt::CaseInsensitive) == 0) {
        m_value = eOAIIdentifierType::MR;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("NDHM_HEALTH_NUMBER", Qt::CaseInsensitive) == 0) {
        m_value = eOAIIdentifierType::NDHM_HEALTH_NUMBER;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("HEALTH_ID", Qt::CaseInsensitive) == 0) {
        m_value = eOAIIdentifierType::HEALTH_ID;
        m_value_isSet = m_value_isValid = true;
    }
}

void OAIIdentifierType::fromJsonValue(QJsonValue json) {
fromJson(json.toString());
}

QString OAIIdentifierType::asJson() const {
    
    QString val;
    switch (m_value){
        case eOAIIdentifierType::MOBILE:
            val = "MOBILE";
            break;
        case eOAIIdentifierType::MR:
            val = "MR";
            break;
        case eOAIIdentifierType::NDHM_HEALTH_NUMBER:
            val = "NDHM_HEALTH_NUMBER";
            break;
        case eOAIIdentifierType::HEALTH_ID:
            val = "HEALTH_ID";
            break;
        default:
            break;
    }
    return val;
}

QJsonValue OAIIdentifierType::asJsonValue() const {
    
    return QJsonValue(asJson());
}


OAIIdentifierType::eOAIIdentifierType OAIIdentifierType::getValue() const {
    return m_value;
}

void OAIIdentifierType::setValue(const OAIIdentifierType::eOAIIdentifierType& value){
    m_value = value;
    m_value_isSet = true;
}
bool OAIIdentifierType::isSet() const {
    
    return m_value_isSet;
}

bool OAIIdentifierType::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_value_isValid;
}

} // namespace OpenAPI
