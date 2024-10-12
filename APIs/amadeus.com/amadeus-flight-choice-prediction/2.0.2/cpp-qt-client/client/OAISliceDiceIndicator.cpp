/**
 * Flight Choice Prediction
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, to see what is included in test please refer to our **[data collection](https://github.com/amadeus4dev/data-collection)**. 
 *
 * The version of the OpenAPI document: 2.0.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAISliceDiceIndicator.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISliceDiceIndicator::OAISliceDiceIndicator(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISliceDiceIndicator::OAISliceDiceIndicator() {
    this->initializeModel();
}

OAISliceDiceIndicator::~OAISliceDiceIndicator() {}

void OAISliceDiceIndicator::initializeModel() {

    m_value_isSet = false;
    m_value_isValid = false;
    m_value = eOAISliceDiceIndicator::INVALID_VALUE_OPENAPI_GENERATED;
}

void OAISliceDiceIndicator::fromJson(QString jsonString) {
    
    if ( jsonString.compare("LOCAL_AVAILABILITY", Qt::CaseInsensitive) == 0) {
        m_value = eOAISliceDiceIndicator::LOCAL_AVAILABILITY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("SUB_OD_AVAILABILITY_1", Qt::CaseInsensitive) == 0) {
        m_value = eOAISliceDiceIndicator::SUB_OD_AVAILABILITY_1;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("SUB_OD_AVAILABILITY_2", Qt::CaseInsensitive) == 0) {
        m_value = eOAISliceDiceIndicator::SUB_OD_AVAILABILITY_2;
        m_value_isSet = m_value_isValid = true;
    }
}

void OAISliceDiceIndicator::fromJsonValue(QJsonValue json) {
fromJson(json.toString());
}

QString OAISliceDiceIndicator::asJson() const {
    
    QString val;
    switch (m_value){
        case eOAISliceDiceIndicator::LOCAL_AVAILABILITY:
            val = "LOCAL_AVAILABILITY";
            break;
        case eOAISliceDiceIndicator::SUB_OD_AVAILABILITY_1:
            val = "SUB_OD_AVAILABILITY_1";
            break;
        case eOAISliceDiceIndicator::SUB_OD_AVAILABILITY_2:
            val = "SUB_OD_AVAILABILITY_2";
            break;
        default:
            break;
    }
    return val;
}

QJsonValue OAISliceDiceIndicator::asJsonValue() const {
    
    return QJsonValue(asJson());
}


OAISliceDiceIndicator::eOAISliceDiceIndicator OAISliceDiceIndicator::getValue() const {
    return m_value;
}

void OAISliceDiceIndicator::setValue(const OAISliceDiceIndicator::eOAISliceDiceIndicator& value){
    m_value = value;
    m_value_isSet = true;
}
bool OAISliceDiceIndicator::isSet() const {
    
    return m_value_isSet;
}

bool OAISliceDiceIndicator::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_value_isValid;
}

} // namespace OpenAPI
