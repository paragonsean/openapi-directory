/**
 * Swiss NextGen Banking API-Framework
 * # Summary The **Swiss NextGen API** is based on the NextGenPSD2 *Framework Version 1.3.4* of the Berlin Group which offers a modern, open, harmonised and interoperable set of Application Programming Interfaces (APIs) as the safest and most efficient way to provide data securely. The NextGen Framework reduces XS2A complexity and costs, addresses the problem of multiple competing standards in Europe and, aligned with the goals of the Euro Retail Payments Board, enables European banking customers to benefit from innovative products and services ('Banking as a Service') by granting TPPs safe and secure (authenticated and authorised) access to their bank accounts and financial data.  The Swiss edtion refines the message formats specific to Switzerland and defines some matching examples.  The possible Approaches are:   * Redirect SCA Approach   * *(Not recommended by obp.ch community) OAuth SCA Approach*   * *(Not recommended by obp.ch community) Decoupled SCA Approach*   * *(Not recommended by obp.ch community) Embedded SCA Approach without SCA method*   * *(Not recommended by obp.ch community) Embedded SCA Approach with only one SCA method available*   * *(Not recommended by obp.ch community) Embedded SCA Approach with Selection of a SCA method*    Not every message defined in this API definition is necessary for all approaches.   Furthermore this API definition does not differ between methods which are mandatory, conditional, or optional   Therefore for a particular implementation of a compliant API it is only necessary to support   a certain subset of the methods defined in this API definition.    **Please have a look at the implementation guidelines if you are not sure   which message has to be used for the approach you are going to use.**  ## Some General Remarks Related to this version of the OpenAPI Specification: * **This API definition is based on the Implementation Guidelines of the [Berlin Group API](https://www.berlin-group.org/nextgenpsd2-downloads).**   It is not a replacement in any sense.   The main specification is (at the moment) always the Implementation Guidelines of the Berlin Group API. * **This API definition contains the REST-API for requests from the PISP to the ASPSP.** * **This API definition contains the messages for all different approaches defined in the Implementation Guidelines.** * According to the OpenAPI-Specification [https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.1.md]      \"If in is \"header\" and the name field is \"Accept\", \"Content-Type\" or \"Authorization\", the parameter definition SHALL be ignored.\"    The element \"Accept\" will not be defined in this file at any place.    The elements \"Content-Type\" and \"Authorization\" are implicitly defined by the OpenApi tags \"content\" and \"security\".  * There are several predefined types which might occur in payment initiation messages,   but are not used in the standard JSON messages in the Implementation Guidelines.   Therefore they are not used in the corresponding messages in this file either.   We added them for the convenience of the user.   If there is a payment product, which needs these fields, one can easily use the predefined types.   But the ASPSP need not to accept them in general.  * **We omit the definition of all standard HTTP header elements (mandatory/optional/conditional)   except they are mentioned in the Implementation Guidelines.**   Therefore the implementer might add these in his own realisation of a comlient API in addition to the elements defined in this file.  ## General Remarks on Data Types  The Berlin Group definition of UTF-8 strings in context of the API have to support at least the following characters  a b c d e f g h i j k l m n o p q r s t u v w x y z  A B C D E F G H I J K L M N O P Q R S T U V W X Y Z  0 1 2 3 4 5 6 7 8 9  / - ? : ( ) . , ' +  Space 
 *
 * The version of the OpenAPI document: 1.3.8_2020-12-14 - Swiss edition 1.3.8.1-CH
 * Contact: info@obp.ch
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAddress.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAddress::OAIAddress(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAddress::OAIAddress() {
    this->initializeModel();
}

OAIAddress::~OAIAddress() {}

void OAIAddress::initializeModel() {

    m_building_number_isSet = false;
    m_building_number_isValid = false;

    m_country_isSet = false;
    m_country_isValid = false;

    m_post_code_isSet = false;
    m_post_code_isValid = false;

    m_street_name_isSet = false;
    m_street_name_isValid = false;

    m_town_name_isSet = false;
    m_town_name_isValid = false;
}

void OAIAddress::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAddress::fromJsonObject(QJsonObject json) {

    m_building_number_isValid = ::OpenAPI::fromJsonValue(m_building_number, json[QString("buildingNumber")]);
    m_building_number_isSet = !json[QString("buildingNumber")].isNull() && m_building_number_isValid;

    m_country_isValid = ::OpenAPI::fromJsonValue(m_country, json[QString("country")]);
    m_country_isSet = !json[QString("country")].isNull() && m_country_isValid;

    m_post_code_isValid = ::OpenAPI::fromJsonValue(m_post_code, json[QString("postCode")]);
    m_post_code_isSet = !json[QString("postCode")].isNull() && m_post_code_isValid;

    m_street_name_isValid = ::OpenAPI::fromJsonValue(m_street_name, json[QString("streetName")]);
    m_street_name_isSet = !json[QString("streetName")].isNull() && m_street_name_isValid;

    m_town_name_isValid = ::OpenAPI::fromJsonValue(m_town_name, json[QString("townName")]);
    m_town_name_isSet = !json[QString("townName")].isNull() && m_town_name_isValid;
}

QString OAIAddress::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAddress::asJsonObject() const {
    QJsonObject obj;
    if (m_building_number_isSet) {
        obj.insert(QString("buildingNumber"), ::OpenAPI::toJsonValue(m_building_number));
    }
    if (m_country_isSet) {
        obj.insert(QString("country"), ::OpenAPI::toJsonValue(m_country));
    }
    if (m_post_code_isSet) {
        obj.insert(QString("postCode"), ::OpenAPI::toJsonValue(m_post_code));
    }
    if (m_street_name_isSet) {
        obj.insert(QString("streetName"), ::OpenAPI::toJsonValue(m_street_name));
    }
    if (m_town_name_isSet) {
        obj.insert(QString("townName"), ::OpenAPI::toJsonValue(m_town_name));
    }
    return obj;
}

QString OAIAddress::getBuildingNumber() const {
    return m_building_number;
}
void OAIAddress::setBuildingNumber(const QString &building_number) {
    m_building_number = building_number;
    m_building_number_isSet = true;
}

bool OAIAddress::is_building_number_Set() const{
    return m_building_number_isSet;
}

bool OAIAddress::is_building_number_Valid() const{
    return m_building_number_isValid;
}

QString OAIAddress::getCountry() const {
    return m_country;
}
void OAIAddress::setCountry(const QString &country) {
    m_country = country;
    m_country_isSet = true;
}

bool OAIAddress::is_country_Set() const{
    return m_country_isSet;
}

bool OAIAddress::is_country_Valid() const{
    return m_country_isValid;
}

QString OAIAddress::getPostCode() const {
    return m_post_code;
}
void OAIAddress::setPostCode(const QString &post_code) {
    m_post_code = post_code;
    m_post_code_isSet = true;
}

bool OAIAddress::is_post_code_Set() const{
    return m_post_code_isSet;
}

bool OAIAddress::is_post_code_Valid() const{
    return m_post_code_isValid;
}

QString OAIAddress::getStreetName() const {
    return m_street_name;
}
void OAIAddress::setStreetName(const QString &street_name) {
    m_street_name = street_name;
    m_street_name_isSet = true;
}

bool OAIAddress::is_street_name_Set() const{
    return m_street_name_isSet;
}

bool OAIAddress::is_street_name_Valid() const{
    return m_street_name_isValid;
}

QString OAIAddress::getTownName() const {
    return m_town_name;
}
void OAIAddress::setTownName(const QString &town_name) {
    m_town_name = town_name;
    m_town_name_isSet = true;
}

bool OAIAddress::is_town_name_Set() const{
    return m_town_name_isSet;
}

bool OAIAddress::is_town_name_Valid() const{
    return m_town_name_isValid;
}

bool OAIAddress::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_building_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_country_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_post_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_street_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_town_name_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAddress::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_country_isValid && true;
}

} // namespace OpenAPI
