/**
 * Zalando Shop
 * The shop API empowers developers to build amazing new apps or websites using Zalando shop data and services.
 *
 * The version of the OpenAPI document: v1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIArticle_Review.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIArticle_Review::OAIArticle_Review(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIArticle_Review::OAIArticle_Review() {
    this->initializeModel();
}

OAIArticle_Review::~OAIArticle_Review() {}

void OAIArticle_Review::initializeModel() {

    m_article_id_isSet = false;
    m_article_id_isValid = false;

    m_article_model_id_isSet = false;
    m_article_model_id_isValid = false;

    m_article_size_ratings_isSet = false;
    m_article_size_ratings_isValid = false;

    m_created_isSet = false;
    m_created_isValid = false;

    m_customer_city_isSet = false;
    m_customer_city_isValid = false;

    m_customer_country_isSet = false;
    m_customer_country_isValid = false;

    m_customer_nickname_isSet = false;
    m_customer_nickname_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_helpful_count_isSet = false;
    m_helpful_count_isValid = false;

    m_language_isSet = false;
    m_language_isValid = false;

    m_rating_isSet = false;
    m_rating_isValid = false;

    m_recommend_isSet = false;
    m_recommend_isValid = false;

    m_review_id_isSet = false;
    m_review_id_isValid = false;

    m_title_isSet = false;
    m_title_isValid = false;

    m_unhelpful_count_isSet = false;
    m_unhelpful_count_isValid = false;
}

void OAIArticle_Review::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIArticle_Review::fromJsonObject(QJsonObject json) {

    m_article_id_isValid = ::OpenAPI::fromJsonValue(m_article_id, json[QString("articleId")]);
    m_article_id_isSet = !json[QString("articleId")].isNull() && m_article_id_isValid;

    m_article_model_id_isValid = ::OpenAPI::fromJsonValue(m_article_model_id, json[QString("articleModelId")]);
    m_article_model_id_isSet = !json[QString("articleModelId")].isNull() && m_article_model_id_isValid;

    m_article_size_ratings_isValid = ::OpenAPI::fromJsonValue(m_article_size_ratings, json[QString("articleSizeRatings")]);
    m_article_size_ratings_isSet = !json[QString("articleSizeRatings")].isNull() && m_article_size_ratings_isValid;

    m_created_isValid = ::OpenAPI::fromJsonValue(m_created, json[QString("created")]);
    m_created_isSet = !json[QString("created")].isNull() && m_created_isValid;

    m_customer_city_isValid = ::OpenAPI::fromJsonValue(m_customer_city, json[QString("customerCity")]);
    m_customer_city_isSet = !json[QString("customerCity")].isNull() && m_customer_city_isValid;

    m_customer_country_isValid = ::OpenAPI::fromJsonValue(m_customer_country, json[QString("customerCountry")]);
    m_customer_country_isSet = !json[QString("customerCountry")].isNull() && m_customer_country_isValid;

    m_customer_nickname_isValid = ::OpenAPI::fromJsonValue(m_customer_nickname, json[QString("customerNickname")]);
    m_customer_nickname_isSet = !json[QString("customerNickname")].isNull() && m_customer_nickname_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_helpful_count_isValid = ::OpenAPI::fromJsonValue(m_helpful_count, json[QString("helpfulCount")]);
    m_helpful_count_isSet = !json[QString("helpfulCount")].isNull() && m_helpful_count_isValid;

    m_language_isValid = ::OpenAPI::fromJsonValue(m_language, json[QString("language")]);
    m_language_isSet = !json[QString("language")].isNull() && m_language_isValid;

    m_rating_isValid = ::OpenAPI::fromJsonValue(m_rating, json[QString("rating")]);
    m_rating_isSet = !json[QString("rating")].isNull() && m_rating_isValid;

    m_recommend_isValid = ::OpenAPI::fromJsonValue(m_recommend, json[QString("recommend")]);
    m_recommend_isSet = !json[QString("recommend")].isNull() && m_recommend_isValid;

    m_review_id_isValid = ::OpenAPI::fromJsonValue(m_review_id, json[QString("reviewId")]);
    m_review_id_isSet = !json[QString("reviewId")].isNull() && m_review_id_isValid;

    m_title_isValid = ::OpenAPI::fromJsonValue(m_title, json[QString("title")]);
    m_title_isSet = !json[QString("title")].isNull() && m_title_isValid;

    m_unhelpful_count_isValid = ::OpenAPI::fromJsonValue(m_unhelpful_count, json[QString("unhelpfulCount")]);
    m_unhelpful_count_isSet = !json[QString("unhelpfulCount")].isNull() && m_unhelpful_count_isValid;
}

QString OAIArticle_Review::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIArticle_Review::asJsonObject() const {
    QJsonObject obj;
    if (m_article_id_isSet) {
        obj.insert(QString("articleId"), ::OpenAPI::toJsonValue(m_article_id));
    }
    if (m_article_model_id_isSet) {
        obj.insert(QString("articleModelId"), ::OpenAPI::toJsonValue(m_article_model_id));
    }
    if (m_article_size_ratings.isSet()) {
        obj.insert(QString("articleSizeRatings"), ::OpenAPI::toJsonValue(m_article_size_ratings));
    }
    if (m_created_isSet) {
        obj.insert(QString("created"), ::OpenAPI::toJsonValue(m_created));
    }
    if (m_customer_city_isSet) {
        obj.insert(QString("customerCity"), ::OpenAPI::toJsonValue(m_customer_city));
    }
    if (m_customer_country_isSet) {
        obj.insert(QString("customerCountry"), ::OpenAPI::toJsonValue(m_customer_country));
    }
    if (m_customer_nickname_isSet) {
        obj.insert(QString("customerNickname"), ::OpenAPI::toJsonValue(m_customer_nickname));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_helpful_count_isSet) {
        obj.insert(QString("helpfulCount"), ::OpenAPI::toJsonValue(m_helpful_count));
    }
    if (m_language_isSet) {
        obj.insert(QString("language"), ::OpenAPI::toJsonValue(m_language));
    }
    if (m_rating_isSet) {
        obj.insert(QString("rating"), ::OpenAPI::toJsonValue(m_rating));
    }
    if (m_recommend_isSet) {
        obj.insert(QString("recommend"), ::OpenAPI::toJsonValue(m_recommend));
    }
    if (m_review_id_isSet) {
        obj.insert(QString("reviewId"), ::OpenAPI::toJsonValue(m_review_id));
    }
    if (m_title_isSet) {
        obj.insert(QString("title"), ::OpenAPI::toJsonValue(m_title));
    }
    if (m_unhelpful_count_isSet) {
        obj.insert(QString("unhelpfulCount"), ::OpenAPI::toJsonValue(m_unhelpful_count));
    }
    return obj;
}

QString OAIArticle_Review::getArticleId() const {
    return m_article_id;
}
void OAIArticle_Review::setArticleId(const QString &article_id) {
    m_article_id = article_id;
    m_article_id_isSet = true;
}

bool OAIArticle_Review::is_article_id_Set() const{
    return m_article_id_isSet;
}

bool OAIArticle_Review::is_article_id_Valid() const{
    return m_article_id_isValid;
}

QString OAIArticle_Review::getArticleModelId() const {
    return m_article_model_id;
}
void OAIArticle_Review::setArticleModelId(const QString &article_model_id) {
    m_article_model_id = article_model_id;
    m_article_model_id_isSet = true;
}

bool OAIArticle_Review::is_article_model_id_Set() const{
    return m_article_model_id_isSet;
}

bool OAIArticle_Review::is_article_model_id_Valid() const{
    return m_article_model_id_isValid;
}

OAIArticle_Review_articleSizeRatings OAIArticle_Review::getArticleSizeRatings() const {
    return m_article_size_ratings;
}
void OAIArticle_Review::setArticleSizeRatings(const OAIArticle_Review_articleSizeRatings &article_size_ratings) {
    m_article_size_ratings = article_size_ratings;
    m_article_size_ratings_isSet = true;
}

bool OAIArticle_Review::is_article_size_ratings_Set() const{
    return m_article_size_ratings_isSet;
}

bool OAIArticle_Review::is_article_size_ratings_Valid() const{
    return m_article_size_ratings_isValid;
}

QDateTime OAIArticle_Review::getCreated() const {
    return m_created;
}
void OAIArticle_Review::setCreated(const QDateTime &created) {
    m_created = created;
    m_created_isSet = true;
}

bool OAIArticle_Review::is_created_Set() const{
    return m_created_isSet;
}

bool OAIArticle_Review::is_created_Valid() const{
    return m_created_isValid;
}

QString OAIArticle_Review::getCustomerCity() const {
    return m_customer_city;
}
void OAIArticle_Review::setCustomerCity(const QString &customer_city) {
    m_customer_city = customer_city;
    m_customer_city_isSet = true;
}

bool OAIArticle_Review::is_customer_city_Set() const{
    return m_customer_city_isSet;
}

bool OAIArticle_Review::is_customer_city_Valid() const{
    return m_customer_city_isValid;
}

QString OAIArticle_Review::getCustomerCountry() const {
    return m_customer_country;
}
void OAIArticle_Review::setCustomerCountry(const QString &customer_country) {
    m_customer_country = customer_country;
    m_customer_country_isSet = true;
}

bool OAIArticle_Review::is_customer_country_Set() const{
    return m_customer_country_isSet;
}

bool OAIArticle_Review::is_customer_country_Valid() const{
    return m_customer_country_isValid;
}

QString OAIArticle_Review::getCustomerNickname() const {
    return m_customer_nickname;
}
void OAIArticle_Review::setCustomerNickname(const QString &customer_nickname) {
    m_customer_nickname = customer_nickname;
    m_customer_nickname_isSet = true;
}

bool OAIArticle_Review::is_customer_nickname_Set() const{
    return m_customer_nickname_isSet;
}

bool OAIArticle_Review::is_customer_nickname_Valid() const{
    return m_customer_nickname_isValid;
}

QString OAIArticle_Review::getDescription() const {
    return m_description;
}
void OAIArticle_Review::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIArticle_Review::is_description_Set() const{
    return m_description_isSet;
}

bool OAIArticle_Review::is_description_Valid() const{
    return m_description_isValid;
}

qint32 OAIArticle_Review::getHelpfulCount() const {
    return m_helpful_count;
}
void OAIArticle_Review::setHelpfulCount(const qint32 &helpful_count) {
    m_helpful_count = helpful_count;
    m_helpful_count_isSet = true;
}

bool OAIArticle_Review::is_helpful_count_Set() const{
    return m_helpful_count_isSet;
}

bool OAIArticle_Review::is_helpful_count_Valid() const{
    return m_helpful_count_isValid;
}

QString OAIArticle_Review::getLanguage() const {
    return m_language;
}
void OAIArticle_Review::setLanguage(const QString &language) {
    m_language = language;
    m_language_isSet = true;
}

bool OAIArticle_Review::is_language_Set() const{
    return m_language_isSet;
}

bool OAIArticle_Review::is_language_Valid() const{
    return m_language_isValid;
}

qint32 OAIArticle_Review::getRating() const {
    return m_rating;
}
void OAIArticle_Review::setRating(const qint32 &rating) {
    m_rating = rating;
    m_rating_isSet = true;
}

bool OAIArticle_Review::is_rating_Set() const{
    return m_rating_isSet;
}

bool OAIArticle_Review::is_rating_Valid() const{
    return m_rating_isValid;
}

bool OAIArticle_Review::isRecommend() const {
    return m_recommend;
}
void OAIArticle_Review::setRecommend(const bool &recommend) {
    m_recommend = recommend;
    m_recommend_isSet = true;
}

bool OAIArticle_Review::is_recommend_Set() const{
    return m_recommend_isSet;
}

bool OAIArticle_Review::is_recommend_Valid() const{
    return m_recommend_isValid;
}

QString OAIArticle_Review::getReviewId() const {
    return m_review_id;
}
void OAIArticle_Review::setReviewId(const QString &review_id) {
    m_review_id = review_id;
    m_review_id_isSet = true;
}

bool OAIArticle_Review::is_review_id_Set() const{
    return m_review_id_isSet;
}

bool OAIArticle_Review::is_review_id_Valid() const{
    return m_review_id_isValid;
}

QString OAIArticle_Review::getTitle() const {
    return m_title;
}
void OAIArticle_Review::setTitle(const QString &title) {
    m_title = title;
    m_title_isSet = true;
}

bool OAIArticle_Review::is_title_Set() const{
    return m_title_isSet;
}

bool OAIArticle_Review::is_title_Valid() const{
    return m_title_isValid;
}

qint32 OAIArticle_Review::getUnhelpfulCount() const {
    return m_unhelpful_count;
}
void OAIArticle_Review::setUnhelpfulCount(const qint32 &unhelpful_count) {
    m_unhelpful_count = unhelpful_count;
    m_unhelpful_count_isSet = true;
}

bool OAIArticle_Review::is_unhelpful_count_Set() const{
    return m_unhelpful_count_isSet;
}

bool OAIArticle_Review::is_unhelpful_count_Valid() const{
    return m_unhelpful_count_isValid;
}

bool OAIArticle_Review::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_article_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_article_model_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_article_size_ratings.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_customer_city_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_customer_country_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_customer_nickname_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_helpful_count_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_language_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_rating_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_recommend_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_review_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_title_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_unhelpful_count_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIArticle_Review::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_article_id_isValid && m_article_model_id_isValid && m_created_isValid && m_description_isValid && m_helpful_count_isValid && m_language_isValid && m_rating_isValid && m_review_id_isValid && m_title_isValid && m_unhelpful_count_isValid && true;
}

} // namespace OpenAPI
