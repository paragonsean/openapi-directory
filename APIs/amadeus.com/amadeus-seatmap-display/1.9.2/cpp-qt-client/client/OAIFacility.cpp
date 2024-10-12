/**
 * Seatmap Display
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.9.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIFacility.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIFacility::OAIFacility(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIFacility::OAIFacility() {
    this->initializeModel();
}

OAIFacility::~OAIFacility() {}

void OAIFacility::initializeModel() {

    m_code_isSet = false;
    m_code_isValid = false;

    m_column_isSet = false;
    m_column_isValid = false;

    m_coordinates_isSet = false;
    m_coordinates_isValid = false;

    m_position_isSet = false;
    m_position_isValid = false;

    m_row_isSet = false;
    m_row_isValid = false;
}

void OAIFacility::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIFacility::fromJsonObject(QJsonObject json) {

    m_code_isValid = ::OpenAPI::fromJsonValue(m_code, json[QString("code")]);
    m_code_isSet = !json[QString("code")].isNull() && m_code_isValid;

    m_column_isValid = ::OpenAPI::fromJsonValue(m_column, json[QString("column")]);
    m_column_isSet = !json[QString("column")].isNull() && m_column_isValid;

    m_coordinates_isValid = ::OpenAPI::fromJsonValue(m_coordinates, json[QString("coordinates")]);
    m_coordinates_isSet = !json[QString("coordinates")].isNull() && m_coordinates_isValid;

    m_position_isValid = ::OpenAPI::fromJsonValue(m_position, json[QString("position")]);
    m_position_isSet = !json[QString("position")].isNull() && m_position_isValid;

    m_row_isValid = ::OpenAPI::fromJsonValue(m_row, json[QString("row")]);
    m_row_isSet = !json[QString("row")].isNull() && m_row_isValid;
}

QString OAIFacility::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIFacility::asJsonObject() const {
    QJsonObject obj;
    if (m_code_isSet) {
        obj.insert(QString("code"), ::OpenAPI::toJsonValue(m_code));
    }
    if (m_column_isSet) {
        obj.insert(QString("column"), ::OpenAPI::toJsonValue(m_column));
    }
    if (m_coordinates.isSet()) {
        obj.insert(QString("coordinates"), ::OpenAPI::toJsonValue(m_coordinates));
    }
    if (m_position_isSet) {
        obj.insert(QString("position"), ::OpenAPI::toJsonValue(m_position));
    }
    if (m_row_isSet) {
        obj.insert(QString("row"), ::OpenAPI::toJsonValue(m_row));
    }
    return obj;
}

QString OAIFacility::getCode() const {
    return m_code;
}
void OAIFacility::setCode(const QString &code) {
    m_code = code;
    m_code_isSet = true;
}

bool OAIFacility::is_code_Set() const{
    return m_code_isSet;
}

bool OAIFacility::is_code_Valid() const{
    return m_code_isValid;
}

QString OAIFacility::getColumn() const {
    return m_column;
}
void OAIFacility::setColumn(const QString &column) {
    m_column = column;
    m_column_isSet = true;
}

bool OAIFacility::is_column_Set() const{
    return m_column_isSet;
}

bool OAIFacility::is_column_Valid() const{
    return m_column_isValid;
}

OAICoordinates OAIFacility::getCoordinates() const {
    return m_coordinates;
}
void OAIFacility::setCoordinates(const OAICoordinates &coordinates) {
    m_coordinates = coordinates;
    m_coordinates_isSet = true;
}

bool OAIFacility::is_coordinates_Set() const{
    return m_coordinates_isSet;
}

bool OAIFacility::is_coordinates_Valid() const{
    return m_coordinates_isValid;
}

QString OAIFacility::getPosition() const {
    return m_position;
}
void OAIFacility::setPosition(const QString &position) {
    m_position = position;
    m_position_isSet = true;
}

bool OAIFacility::is_position_Set() const{
    return m_position_isSet;
}

bool OAIFacility::is_position_Valid() const{
    return m_position_isValid;
}

QString OAIFacility::getRow() const {
    return m_row;
}
void OAIFacility::setRow(const QString &row) {
    m_row = row;
    m_row_isSet = true;
}

bool OAIFacility::is_row_Set() const{
    return m_row_isSet;
}

bool OAIFacility::is_row_Valid() const{
    return m_row_isValid;
}

bool OAIFacility::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_column_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_coordinates.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_position_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_row_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIFacility::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
