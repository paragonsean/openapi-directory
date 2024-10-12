/**
 * LinQR
 * This is LinQR QR Code API documentation. This API allows you to generate custom, visually attractive QR Codes. The cloud infrastructure guarantees high availability and autoscalability of the service. You can generate hundreds of thousands of images this way and use them however you like.  We realize that your API use case may require custom solutions, and perhaps we lack functionality that is very important to you. In that case feel free to write an email to our support and tell us about it. We have repeatedly added new functions of our service directly after the requests of our users.  **General remarks:**  - maximum request size is fixed at 32MB.  - request timeout is fixed at 180 seconds.
 *
 * The version of the OpenAPI document: 2.0
 * Contact: support@linqr.app
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIModuleShapes.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIModuleShapes::OAIModuleShapes(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIModuleShapes::OAIModuleShapes() {
    this->initializeModel();
}

OAIModuleShapes::~OAIModuleShapes() {}

void OAIModuleShapes::initializeModel() {

    m_value_isSet = false;
    m_value_isValid = false;
    m_value = eOAIModuleShapes::INVALID_VALUE_OPENAPI_GENERATED;
}

void OAIModuleShapes::fromJson(QString jsonString) {
    
    if ( jsonString.compare("arrow", Qt::CaseInsensitive) == 0) {
        m_value = eOAIModuleShapes::ARROW;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("circle", Qt::CaseInsensitive) == 0) {
        m_value = eOAIModuleShapes::CIRCLE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("classic", Qt::CaseInsensitive) == 0) {
        m_value = eOAIModuleShapes::CLASSIC;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("default", Qt::CaseInsensitive) == 0) {
        m_value = eOAIModuleShapes::DEFAULT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("heart", Qt::CaseInsensitive) == 0) {
        m_value = eOAIModuleShapes::HEART;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("heavyround", Qt::CaseInsensitive) == 0) {
        m_value = eOAIModuleShapes::HEAVYROUND;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("horizontal_lines", Qt::CaseInsensitive) == 0) {
        m_value = eOAIModuleShapes::HORIZONTAL_LINES;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("lightround", Qt::CaseInsensitive) == 0) {
        m_value = eOAIModuleShapes::LIGHTROUND;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("sharp", Qt::CaseInsensitive) == 0) {
        m_value = eOAIModuleShapes::SHARP;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("sieve", Qt::CaseInsensitive) == 0) {
        m_value = eOAIModuleShapes::SIEVE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("vertical_lines", Qt::CaseInsensitive) == 0) {
        m_value = eOAIModuleShapes::VERTICAL_LINES;
        m_value_isSet = m_value_isValid = true;
    }
}

void OAIModuleShapes::fromJsonValue(QJsonValue json) {
fromJson(json.toString());
}

QString OAIModuleShapes::asJson() const {
    
    QString val;
    switch (m_value){
        case eOAIModuleShapes::ARROW:
            val = "arrow";
            break;
        case eOAIModuleShapes::CIRCLE:
            val = "circle";
            break;
        case eOAIModuleShapes::CLASSIC:
            val = "classic";
            break;
        case eOAIModuleShapes::DEFAULT:
            val = "default";
            break;
        case eOAIModuleShapes::HEART:
            val = "heart";
            break;
        case eOAIModuleShapes::HEAVYROUND:
            val = "heavyround";
            break;
        case eOAIModuleShapes::HORIZONTAL_LINES:
            val = "horizontal_lines";
            break;
        case eOAIModuleShapes::LIGHTROUND:
            val = "lightround";
            break;
        case eOAIModuleShapes::SHARP:
            val = "sharp";
            break;
        case eOAIModuleShapes::SIEVE:
            val = "sieve";
            break;
        case eOAIModuleShapes::VERTICAL_LINES:
            val = "vertical_lines";
            break;
        default:
            break;
    }
    return val;
}

QJsonValue OAIModuleShapes::asJsonValue() const {
    
    return QJsonValue(asJson());
}


OAIModuleShapes::eOAIModuleShapes OAIModuleShapes::getValue() const {
    return m_value;
}

void OAIModuleShapes::setValue(const OAIModuleShapes::eOAIModuleShapes& value){
    m_value = value;
    m_value_isSet = true;
}
bool OAIModuleShapes::isSet() const {
    
    return m_value_isSet;
}

bool OAIModuleShapes::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_value_isValid;
}

} // namespace OpenAPI
