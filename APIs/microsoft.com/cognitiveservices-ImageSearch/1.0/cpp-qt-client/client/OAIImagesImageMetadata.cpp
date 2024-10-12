/**
 * Image Search Client
 * The Image Search API lets you send a search query to Bing and get back a list of relevant images. This section provides technical details about the query parameters and headers that you use to request images and the JSON response objects that contain them. For examples that show how to make requests, see [Searching the Web for Images](https://docs.microsoft.com/azure/cognitive-services/bing-image-search/search-the-web).
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIImagesImageMetadata.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIImagesImageMetadata::OAIImagesImageMetadata(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIImagesImageMetadata::OAIImagesImageMetadata() {
    this->initializeModel();
}

OAIImagesImageMetadata::~OAIImagesImageMetadata() {}

void OAIImagesImageMetadata::initializeModel() {

    m_aggregate_offer_isSet = false;
    m_aggregate_offer_isValid = false;

    m_recipe_sources_count_isSet = false;
    m_recipe_sources_count_isValid = false;

    m_shopping_sources_count_isSet = false;
    m_shopping_sources_count_isValid = false;
}

void OAIImagesImageMetadata::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIImagesImageMetadata::fromJsonObject(QJsonObject json) {

    m_aggregate_offer_isValid = ::OpenAPI::fromJsonValue(m_aggregate_offer, json[QString("aggregateOffer")]);
    m_aggregate_offer_isSet = !json[QString("aggregateOffer")].isNull() && m_aggregate_offer_isValid;

    m_recipe_sources_count_isValid = ::OpenAPI::fromJsonValue(m_recipe_sources_count, json[QString("recipeSourcesCount")]);
    m_recipe_sources_count_isSet = !json[QString("recipeSourcesCount")].isNull() && m_recipe_sources_count_isValid;

    m_shopping_sources_count_isValid = ::OpenAPI::fromJsonValue(m_shopping_sources_count, json[QString("shoppingSourcesCount")]);
    m_shopping_sources_count_isSet = !json[QString("shoppingSourcesCount")].isNull() && m_shopping_sources_count_isValid;
}

QString OAIImagesImageMetadata::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIImagesImageMetadata::asJsonObject() const {
    QJsonObject obj;
    if (m_aggregate_offer.isSet()) {
        obj.insert(QString("aggregateOffer"), ::OpenAPI::toJsonValue(m_aggregate_offer));
    }
    if (m_recipe_sources_count_isSet) {
        obj.insert(QString("recipeSourcesCount"), ::OpenAPI::toJsonValue(m_recipe_sources_count));
    }
    if (m_shopping_sources_count_isSet) {
        obj.insert(QString("shoppingSourcesCount"), ::OpenAPI::toJsonValue(m_shopping_sources_count));
    }
    return obj;
}

OAIAggregateOffer OAIImagesImageMetadata::getAggregateOffer() const {
    return m_aggregate_offer;
}
void OAIImagesImageMetadata::setAggregateOffer(const OAIAggregateOffer &aggregate_offer) {
    m_aggregate_offer = aggregate_offer;
    m_aggregate_offer_isSet = true;
}

bool OAIImagesImageMetadata::is_aggregate_offer_Set() const{
    return m_aggregate_offer_isSet;
}

bool OAIImagesImageMetadata::is_aggregate_offer_Valid() const{
    return m_aggregate_offer_isValid;
}

qint32 OAIImagesImageMetadata::getRecipeSourcesCount() const {
    return m_recipe_sources_count;
}
void OAIImagesImageMetadata::setRecipeSourcesCount(const qint32 &recipe_sources_count) {
    m_recipe_sources_count = recipe_sources_count;
    m_recipe_sources_count_isSet = true;
}

bool OAIImagesImageMetadata::is_recipe_sources_count_Set() const{
    return m_recipe_sources_count_isSet;
}

bool OAIImagesImageMetadata::is_recipe_sources_count_Valid() const{
    return m_recipe_sources_count_isValid;
}

qint32 OAIImagesImageMetadata::getShoppingSourcesCount() const {
    return m_shopping_sources_count;
}
void OAIImagesImageMetadata::setShoppingSourcesCount(const qint32 &shopping_sources_count) {
    m_shopping_sources_count = shopping_sources_count;
    m_shopping_sources_count_isSet = true;
}

bool OAIImagesImageMetadata::is_shopping_sources_count_Set() const{
    return m_shopping_sources_count_isSet;
}

bool OAIImagesImageMetadata::is_shopping_sources_count_Valid() const{
    return m_shopping_sources_count_isValid;
}

bool OAIImagesImageMetadata::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_aggregate_offer.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_recipe_sources_count_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_shopping_sources_count_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIImagesImageMetadata::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
