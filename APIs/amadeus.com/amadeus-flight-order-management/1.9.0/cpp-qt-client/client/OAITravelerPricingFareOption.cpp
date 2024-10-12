/**
 * Flight Order Management
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.9.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAITravelerPricingFareOption.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAITravelerPricingFareOption::OAITravelerPricingFareOption(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAITravelerPricingFareOption::OAITravelerPricingFareOption() {
    this->initializeModel();
}

OAITravelerPricingFareOption::~OAITravelerPricingFareOption() {}

void OAITravelerPricingFareOption::initializeModel() {

    m_value_isSet = false;
    m_value_isValid = false;
    m_value = eOAITravelerPricingFareOption::INVALID_VALUE_OPENAPI_GENERATED;
}

void OAITravelerPricingFareOption::fromJson(QString jsonString) {
    
    if ( jsonString.compare("STANDARD", Qt::CaseInsensitive) == 0) {
        m_value = eOAITravelerPricingFareOption::STANDARD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("INCLUSIVE_TOUR", Qt::CaseInsensitive) == 0) {
        m_value = eOAITravelerPricingFareOption::INCLUSIVE_TOUR;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("SPANISH_MELILLA_RESIDENT", Qt::CaseInsensitive) == 0) {
        m_value = eOAITravelerPricingFareOption::SPANISH_MELILLA_RESIDENT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("SPANISH_CEUTA_RESIDENT", Qt::CaseInsensitive) == 0) {
        m_value = eOAITravelerPricingFareOption::SPANISH_CEUTA_RESIDENT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("SPANISH_CANARY_RESIDENT", Qt::CaseInsensitive) == 0) {
        m_value = eOAITravelerPricingFareOption::SPANISH_CANARY_RESIDENT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("SPANISH_BALEARIC_RESIDENT", Qt::CaseInsensitive) == 0) {
        m_value = eOAITravelerPricingFareOption::SPANISH_BALEARIC_RESIDENT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("AIR_FRANCE_METROPOLITAN_DISCOUNT_PASS", Qt::CaseInsensitive) == 0) {
        m_value = eOAITravelerPricingFareOption::AIR_FRANCE_METROPOLITAN_DISCOUNT_PASS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("AIR_FRANCE_DOM_DISCOUNT_PASS", Qt::CaseInsensitive) == 0) {
        m_value = eOAITravelerPricingFareOption::AIR_FRANCE_DOM_DISCOUNT_PASS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("AIR_FRANCE_COMBINED_DISCOUNT_PASS", Qt::CaseInsensitive) == 0) {
        m_value = eOAITravelerPricingFareOption::AIR_FRANCE_COMBINED_DISCOUNT_PASS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("AIR_FRANCE_FAMILY", Qt::CaseInsensitive) == 0) {
        m_value = eOAITravelerPricingFareOption::AIR_FRANCE_FAMILY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ADULT_WITH_COMPANION", Qt::CaseInsensitive) == 0) {
        m_value = eOAITravelerPricingFareOption::ADULT_WITH_COMPANION;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("COMPANION", Qt::CaseInsensitive) == 0) {
        m_value = eOAITravelerPricingFareOption::COMPANION;
        m_value_isSet = m_value_isValid = true;
    }
}

void OAITravelerPricingFareOption::fromJsonValue(QJsonValue json) {
fromJson(json.toString());
}

QString OAITravelerPricingFareOption::asJson() const {
    
    QString val;
    switch (m_value){
        case eOAITravelerPricingFareOption::STANDARD:
            val = "STANDARD";
            break;
        case eOAITravelerPricingFareOption::INCLUSIVE_TOUR:
            val = "INCLUSIVE_TOUR";
            break;
        case eOAITravelerPricingFareOption::SPANISH_MELILLA_RESIDENT:
            val = "SPANISH_MELILLA_RESIDENT";
            break;
        case eOAITravelerPricingFareOption::SPANISH_CEUTA_RESIDENT:
            val = "SPANISH_CEUTA_RESIDENT";
            break;
        case eOAITravelerPricingFareOption::SPANISH_CANARY_RESIDENT:
            val = "SPANISH_CANARY_RESIDENT";
            break;
        case eOAITravelerPricingFareOption::SPANISH_BALEARIC_RESIDENT:
            val = "SPANISH_BALEARIC_RESIDENT";
            break;
        case eOAITravelerPricingFareOption::AIR_FRANCE_METROPOLITAN_DISCOUNT_PASS:
            val = "AIR_FRANCE_METROPOLITAN_DISCOUNT_PASS";
            break;
        case eOAITravelerPricingFareOption::AIR_FRANCE_DOM_DISCOUNT_PASS:
            val = "AIR_FRANCE_DOM_DISCOUNT_PASS";
            break;
        case eOAITravelerPricingFareOption::AIR_FRANCE_COMBINED_DISCOUNT_PASS:
            val = "AIR_FRANCE_COMBINED_DISCOUNT_PASS";
            break;
        case eOAITravelerPricingFareOption::AIR_FRANCE_FAMILY:
            val = "AIR_FRANCE_FAMILY";
            break;
        case eOAITravelerPricingFareOption::ADULT_WITH_COMPANION:
            val = "ADULT_WITH_COMPANION";
            break;
        case eOAITravelerPricingFareOption::COMPANION:
            val = "COMPANION";
            break;
        default:
            break;
    }
    return val;
}

QJsonValue OAITravelerPricingFareOption::asJsonValue() const {
    
    return QJsonValue(asJson());
}


OAITravelerPricingFareOption::eOAITravelerPricingFareOption OAITravelerPricingFareOption::getValue() const {
    return m_value;
}

void OAITravelerPricingFareOption::setValue(const OAITravelerPricingFareOption::eOAITravelerPricingFareOption& value){
    m_value = value;
    m_value_isSet = true;
}
bool OAITravelerPricingFareOption::isSet() const {
    
    return m_value_isSet;
}

bool OAITravelerPricingFareOption::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_value_isValid;
}

} // namespace OpenAPI
