/**
 * PowerTools Developer
 * Apptigent PowerTools Developer Edition is a powerful suite of API endpoints for custom applications running on any stack. Manipulate text, modify collections, format dates and times, convert currency, perform advanced mathematical calculations, shorten URL's, encode strings, convert text to speech, translate content into multiple languages, process images, and more. PowerTools is the ultimate developer toolkit.
 *
 * The version of the OpenAPI document: 2021.1.01
 * Contact: support@apptigent.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIInputCollectionModify.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIInputCollectionModify::OAIInputCollectionModify(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIInputCollectionModify::OAIInputCollectionModify() {
    this->initializeModel();
}

OAIInputCollectionModify::~OAIInputCollectionModify() {}

void OAIInputCollectionModify::initializeModel() {

    m_index_isSet = false;
    m_index_isValid = false;

    m_input_isSet = false;
    m_input_isValid = false;

    m_item_isSet = false;
    m_item_isValid = false;

    m_items_isSet = false;
    m_items_isValid = false;
}

void OAIInputCollectionModify::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIInputCollectionModify::fromJsonObject(QJsonObject json) {

    m_index_isValid = ::OpenAPI::fromJsonValue(m_index, json[QString("index")]);
    m_index_isSet = !json[QString("index")].isNull() && m_index_isValid;

    m_input_isValid = ::OpenAPI::fromJsonValue(m_input, json[QString("input")]);
    m_input_isSet = !json[QString("input")].isNull() && m_input_isValid;

    m_item_isValid = ::OpenAPI::fromJsonValue(m_item, json[QString("item")]);
    m_item_isSet = !json[QString("item")].isNull() && m_item_isValid;

    m_items_isValid = ::OpenAPI::fromJsonValue(m_items, json[QString("items")]);
    m_items_isSet = !json[QString("items")].isNull() && m_items_isValid;
}

QString OAIInputCollectionModify::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIInputCollectionModify::asJsonObject() const {
    QJsonObject obj;
    if (m_index_isSet) {
        obj.insert(QString("index"), ::OpenAPI::toJsonValue(m_index));
    }
    if (m_input.size() > 0) {
        obj.insert(QString("input"), ::OpenAPI::toJsonValue(m_input));
    }
    if (m_item_isSet) {
        obj.insert(QString("item"), ::OpenAPI::toJsonValue(m_item));
    }
    if (m_items.size() > 0) {
        obj.insert(QString("items"), ::OpenAPI::toJsonValue(m_items));
    }
    return obj;
}

QString OAIInputCollectionModify::getIndex() const {
    return m_index;
}
void OAIInputCollectionModify::setIndex(const QString &index) {
    m_index = index;
    m_index_isSet = true;
}

bool OAIInputCollectionModify::is_index_Set() const{
    return m_index_isSet;
}

bool OAIInputCollectionModify::is_index_Valid() const{
    return m_index_isValid;
}

QList<QString> OAIInputCollectionModify::getInput() const {
    return m_input;
}
void OAIInputCollectionModify::setInput(const QList<QString> &input) {
    m_input = input;
    m_input_isSet = true;
}

bool OAIInputCollectionModify::is_input_Set() const{
    return m_input_isSet;
}

bool OAIInputCollectionModify::is_input_Valid() const{
    return m_input_isValid;
}

QString OAIInputCollectionModify::getItem() const {
    return m_item;
}
void OAIInputCollectionModify::setItem(const QString &item) {
    m_item = item;
    m_item_isSet = true;
}

bool OAIInputCollectionModify::is_item_Set() const{
    return m_item_isSet;
}

bool OAIInputCollectionModify::is_item_Valid() const{
    return m_item_isValid;
}

QList<QString> OAIInputCollectionModify::getItems() const {
    return m_items;
}
void OAIInputCollectionModify::setItems(const QList<QString> &items) {
    m_items = items;
    m_items_isSet = true;
}

bool OAIInputCollectionModify::is_items_Set() const{
    return m_items_isSet;
}

bool OAIInputCollectionModify::is_items_Valid() const{
    return m_items_isValid;
}

bool OAIInputCollectionModify::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_index_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_input.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_item_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_items.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIInputCollectionModify::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_input_isValid && true;
}

} // namespace OpenAPI
